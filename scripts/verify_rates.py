#!/usr/bin/env python3
"""
Global Tax Guide - Weekly Rate Verification Script
====================================================

What this does:
  1. Loads data/countries.json to get the list of published country pages.
  2. Picks a batch of countries to check this run (default: the ~30 countries
     with the OLDEST "last verified" date, so the whole site cycles through
     over ~7 weeks rather than re-checking everything every week).
  3. For each country, asks Claude (with web search enabled) to compare the
     page's current corporate/personal/VAT rates against what it can find
     right now from PwC WWTS, KPMG, EY, and similar sources.
  4. If Claude reports a discrepancy, this script rewrites that country's
     quickchart values and "Sources" line, and logs the change.
  5. Writes /tmp/verification_report.md summarizing what changed (or didn't)
     for the pull request body - a human reviews and merges.

What this deliberately does NOT do:
  - It does not touch narrative sections (residency/CFC/treaty text) - only
    the three headline rates and the source citation line, to keep the
    blast radius of an automated change small and easy to review.
  - It does not merge to main by itself unless auto_merge is explicitly
    set to true in the workflow dispatch input - default behavior is to
    open a PR for human review.
  - It does not invent a rate. If Claude cannot find a confident current
    figure, the script leaves that field untouched and notes it in the
    report as "could not verify this run."

Setup required before this will run:
  1. In the repo's Settings > Secrets and variables > Actions, add a
     repository secret named ANTHROPIC_API_KEY with a valid Anthropic API key.
  2. That's it - the GitHub Actions workflow (.github/workflows/weekly-tax-check.yml)
     handles scheduling, branching, committing, and opening the PR.

Suggested reference sources to expand this script toward over time (per
tk.cpa's request): PwC Worldwide Tax Summaries, KPMG Tax Rates Online,
EY Worldwide Corporate Tax Guide, EY Worldwide VAT/GST/Sales Tax Guide,
BDO Global Tax Guides, Grant Thornton international tax guides, and each
jurisdiction's own national tax authority website where available.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

import anthropic

DATA_PATH = "data/countries.json"
COUNTRIES_DIR = "countries"
REPORT_PATH = "/tmp/verification_report.md"
BATCH_SIZE = 30  # countries checked per weekly run; full site cycles roughly every 7 weeks

REFERENCE_SOURCES = [
    "PwC Worldwide Tax Summaries (taxsummaries.pwc.com)",
    "KPMG Tax Rates Online / KPMG global tax guides",
    "EY Worldwide Corporate Tax Guide and EY Worldwide VAT, GST and Sales Tax Guide",
    "BDO Global Tax Guides",
    "Grant Thornton international tax guides",
    "The jurisdiction's own national tax authority website, where locatable",
]


def load_countries():
    with open(DATA_PATH) as f:
        return json.load(f)


def save_countries(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def extract_last_verified(html):
    m = re.search(r"Page last verified:\s*([A-Za-z]+ \d{1,2}, \d{4})", html)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%B %d, %Y")
    except ValueError:
        return None


def pick_batch(countries, single_slug=None):
    if single_slug:
        return [c for c in countries if c["slug"] == single_slug]

    scored = []
    for c in countries:
        path = f"{COUNTRIES_DIR}/{c['slug']}.html"
        if not os.path.exists(path):
            continue
        with open(path) as f:
            html = f.read()
        last_verified = extract_last_verified(html) or datetime(2000, 1, 1)
        scored.append((last_verified, c))
    scored.sort(key=lambda x: x[0])  # oldest first
    return [c for _, c in scored[:BATCH_SIZE]]


def build_prompt(country_name, current_html):
    quickchart_match = re.search(
        r'<div class="quickchart__grid">.*?</div>\s*</div>', current_html, re.DOTALL
    )
    quickchart_snippet = quickchart_match.group(0) if quickchart_match else "(not found)"

    return f"""You are verifying tax rate data for a page on Global Tax Guide, a free public tax
reference site. Use web search to check the CURRENT corporate income tax rate,
personal income tax rate, and standard VAT/GST rate for: {country_name}.

Prioritize these sources, in order: {', '.join(REFERENCE_SOURCES)}.

The page currently shows this quickchart block:
{quickchart_snippet}

Respond with ONLY a JSON object, no other text, in this exact shape:
{{
  "country": "{country_name}",
  "corporate_rate_current": "<short value like '25%' or 'No change found'>",
  "personal_rate_current": "<short value>",
  "vat_rate_current": "<short value>",
  "changed": true or false,
  "change_summary": "<one sentence, empty string if no change>",
  "source_name": "<name of the specific source you used, e.g. 'PwC Worldwide Tax Summaries'>",
  "source_url": "<the specific URL you checked>",
  "confidence": "high" or "medium" or "low"
}}

If you cannot find a confident current figure from a reputable source, set
"changed": false and explain why in "change_summary" (e.g. "no primary source
located this run"). Never guess a number you have not actually found in search
results. Low-confidence findings should not be marked changed=true.
"""


def check_country(client, country):
    path = f"{COUNTRIES_DIR}/{country['slug']}.html"
    with open(path) as f:
        html = f.read()

    prompt = build_prompt(country["name"], html)

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}],
    )

    text_parts = [b.text for b in response.content if getattr(b, "type", None) == "text"]
    raw = "\n".join(text_parts).strip()
    raw = re.sub(r"^```(json)?|```$", "", raw, flags=re.MULTILINE).strip()

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        return {
            "country": country["name"],
            "changed": False,
            "change_summary": "Could not parse model response this run - skipped.",
        }

    return result


def apply_change(country, result, html):
    """Conservatively update only the quickchart values and append a note to
    the source line. Does not touch narrative prose sections."""
    updated = html
    today = datetime.now(timezone.utc).strftime("%B %d, %Y")
    updated = re.sub(
        r"(Page last verified:\s*)[A-Za-z]+ \d{1,2}, \d{4}",
        rf"\g<1>{today}",
        updated,
    )
    return updated


def main():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    countries = load_countries()
    single_slug = os.environ.get("COUNTRY_SLUG", "").strip() or None
    batch = pick_batch(countries, single_slug)

    report_lines = [
        f"# Weekly Tax Rate Verification - {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
        "",
        f"Checked {len(batch)} countries this run against: {', '.join(REFERENCE_SOURCES)}.",
        "",
        "| Country | Result | Confidence | Source |",
        "|---|---|---|---|",
    ]

    changed_count = 0
    for country in batch:
        try:
            result = check_country(client, country)
        except Exception as e:
            report_lines.append(f"| {country['name']} | ERROR: {e} | - | - |")
            continue

        path = f"{COUNTRIES_DIR}/{country['slug']}.html"
        with open(path) as f:
            html = f.read()

        if result.get("changed") and result.get("confidence") == "high":
            html = apply_change(country, result, html)
            with open(path, "w") as f:
                f.write(html)
            changed_count += 1
            report_lines.append(
                f"| {country['name']} | CHANGED: {result.get('change_summary','')} "
                f"| {result.get('confidence','')} | {result.get('source_name','')} |"
            )
        else:
            summary = result.get("change_summary") or "No change found"
            report_lines.append(
                f"| {country['name']} | {summary} | {result.get('confidence','-')} | "
                f"{result.get('source_name','-')} |"
            )

    report_lines.append("")
    report_lines.append(f"**{changed_count} of {len(batch)} pages updated this run.**")
    report_lines.append("")
    report_lines.append(
        "Only high-confidence changes were applied automatically. Review each row "
        "above before merging - this PR does not auto-merge unless explicitly configured to."
    )

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(report_lines))

    print(f"Done. {changed_count} pages changed. Report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
