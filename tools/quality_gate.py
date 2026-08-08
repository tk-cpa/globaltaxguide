"""
tools/quality_gate.py

MANDATORY: run this before claiming ANY country page (or batch of pages) is
"done," "verified," or ready to report as complete. This is not optional
polish - it exists because on August 8, 2026, a published page told a
reader to go verify a fact themselves instead of resolving it, and a
site-wide audit then found the same pattern on 13 pages, plus a separate
templating bug duplicating text on 137 pages, plus misleading headline
numbers on at least one page (Bahrain showing a sector-specific 46% rate
as if it were the general rate). None of this was caught before those
pages were reported as complete. This script exists so that never happens
silently again.

USAGE
-----
    python3 tools/quality_gate.py                  # scan every country page
    python3 tools/quality_gate.py slug1 slug2 ...   # scan specific pages only

Exits non-zero and prints every hit if anything is found. A clean run
(no output, exit 0) is required before reporting a page or batch as done.

WHAT IT CHECKS
--------------
1. PUNT_PATTERNS - "confirm directly with X", "should be confirmed
   directly", etc. A resolvable factual question was punted back to the
   reader instead of being resolved via primary-source research. This is
   NEVER acceptable as a final answer - see QUEUE.md's standing rule.
2. CONFLICT_UNRESOLVED - "sources conflict", "genuinely uncertain", etc.
   without a resolution. Conflicting sources must be resolved via
   government/primary sources or multiple independent practitioner
   sources before publishing; if genuinely irreconcilable after real
   effort, the page must say so AND give the best-supported figure with
   the conflict explicitly noted, not just present the conflict and stop.
3. UNVERIFIED_LANGUAGE - "not independently verified", "not confirmed
   this session", etc. left in place on a page without resolution.
4. HEADLINE_CELL_PLACEHOLDER - the quickchart summary cards (the most
   visible, most-skimmed part of every page) showing "Varies",
   "Unverified", or "N/A" for a fact that is very likely knowable (e.g.
   personal or VAT rate for a well-documented country). Every hit here
   needs a human/agent judgment call: either resolve it to a real figure,
   or confirm "N/A" is genuinely the correct answer (e.g. "N/A" for a US
   national VAT rate is correct since there isn't one; "N/A" for a
   Gulf state's personal tax should almost always be "0%" instead).
5. DUPLICATED_PREFIX_BUG - the "X's headline rate is X's headline rate
   is Y" templating artifact fixed sitewide on August 8, 2026. Checking
   for regression in case a future edit reintroduces the broken pattern.

This script does NOT check for misleading-headline-number cases like
Bahrain's 46%-shown-as-general-rate defect - that requires reading the
prose against the summary card, which isn't reliably regex-able. Do that
check by eye whenever a country has an unusual or sector-specific rate.
"""
import os, re, sys, json, urllib.request, concurrent.futures

RAW = "https://raw.githubusercontent.com/tk-cpa/globaltaxguide/main"

PUNT_PATTERNS = [
    r"confirm directly with the",
    r"confirm directly with a",
    r"should be confirmed directly",
    r"rather than relied on from this page",
    r"confirm current (treaty|cfc|thin cap) status directly",
    r"sources conflict enough to flag rather than",
]
CONFLICT_UNRESOLVED = [
    r"sources conflict(?!.{0,300}(confirmed|resolved|named|specific))",
    r"genuinely conflicting",
    r"genuinely uncertain",
]
UNVERIFIED_LANGUAGE = [
    r"not independently verified",
    r"not independently confirmed",
    r"could not be independently verified",
    r"not confirmed this session",
    r"not verified this session",
]
HEADLINE_CELL_PLACEHOLDER = [
    r'"value">Varies<',
    r'"value">Unverified<',
    r'"value">N/A<',
]
DUPLICATED_PREFIX_BUG = [
    r"headline corporate tax rate is [\w\s.'()-]+? headline corporate income tax",
    r"is The headline personal income tax",
    r"is The standard VAT/GST",
]

ALL_CHECKS = {
    "PUNT_PATTERNS (never acceptable - resolve via primary source)": PUNT_PATTERNS,
    "CONFLICT_UNRESOLVED (resolve or explicitly justify why not)": CONFLICT_UNRESOLVED,
    "UNVERIFIED_LANGUAGE (resolve before calling page done)": UNVERIFIED_LANGUAGE,
    "HEADLINE_CELL_PLACEHOLDER (fix or confirm N/A is truly correct)": HEADLINE_CELL_PLACEHOLDER,
    "DUPLICATED_PREFIX_BUG (regression check)": DUPLICATED_PREFIX_BUG,
}

# CELL_VS_PROSE_MISMATCH: found August 8, 2026 on San Marino and Iran (and 13
# more pages once swept sitewide) - the quickchart summary cell for "Top
# personal rate" or "Corporate rate" showed the BOTTOM of a progressive range
# (e.g. "9%") instead of the actual top/general rate (e.g. "35%"), while the
# detailed prose two lines down had it correct. This is checked separately
# below (not a simple regex) because it requires comparing a cell value
# against the highest number in a "X% to Y%" range in the adjacent prose.
import re as _re
_CELL_P = _re.compile(r'<div class="label">Top personal rate</div><div class="value">([\d.]+)%\*?</div>')
_CELL_C = _re.compile(r'<div class="label">Corporate rate</div><div class="value">([\d.]+)%\*?</div>')
_RANGE_PAT = _re.compile(r'(\d+(?:\.\d+)?)%\s*to\s*(?:a\s*)?(\d+(?:\.\d+)?)%', _re.IGNORECASE)

def check_cell_vs_prose_mismatch(content):
    """Returns a list of mismatch descriptions, or empty list if clean."""
    issues = []
    for label, cellpat, h2 in [('personal', _CELL_P, '<h2>Personal Tax Rate</h2>'), ('corporate', _CELL_C, '<h2>Corporate Tax Rate</h2>')]:
        cell_match = cellpat.search(content)
        idx = content.find(h2)
        if cell_match and idx != -1:
            end = content.find('</p>', idx)
            if end == -1:
                continue
            prose_section = content[idx:end]
            cell_val = float(cell_match.group(1))
            range_matches = _RANGE_PAT.findall(prose_section)
            if range_matches:
                max_prose_val = max(float(b) for a, b in range_matches)
                if max_prose_val > cell_val + 1:
                    issues.append(f"{label}: cell shows {cell_val}% but prose describes a range up to {max_prose_val}%")
    return issues

def fetch(slug):
    req = urllib.request.Request(f"{RAW}/countries/{slug}.html", headers={"User-Agent": "x"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="replace")

def scan(slug):
    try:
        content = fetch(slug)
    except Exception as e:
        return (slug, {"FETCH_ERROR": [str(e)]})
    hits = {}
    for label, patterns in ALL_CHECKS.items():
        found = []
        for pat in patterns:
            for m in re.finditer(pat, content, re.IGNORECASE):
                start, end = max(0, m.start() - 80), min(len(content), m.end() + 80)
                found.append(content[start:end].replace("\n", " "))
        if found:
            hits[label] = found
    cell_mismatches = check_cell_vs_prose_mismatch(content)
    if cell_mismatches:
        hits["CELL_VS_PROSE_MISMATCH (found Aug 8 2026 on San Marino/Iran - top-rate cell showing bottom bracket)"] = cell_mismatches
    return (slug, hits)

def main():
    if len(sys.argv) > 1:
        slugs = sys.argv[1:]
    else:
        req = urllib.request.Request(f"{RAW}/data/countries.json", headers={"User-Agent": "x"})
        with urllib.request.urlopen(req) as resp:
            countries = json.loads(resp.read().decode())
        slugs = [c["slug"] for c in countries]

    any_hits = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as ex:
        for slug, hits in ex.map(scan, slugs):
            if hits:
                any_hits = True
                print(f"\n=== {slug} ===")
                for label, snippets in hits.items():
                    print(f"  [{label}]")
                    for s in snippets:
                        print(f"    - {s}")

    if any_hits:
        print("\nGATE FAILED - resolve every item above before reporting these pages as done.")
        sys.exit(1)
    else:
        print(f"Clean: {len(slugs)} pages checked, no defects found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
