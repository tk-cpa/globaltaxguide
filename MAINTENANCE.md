# Global Tax Guide - Site Maintenance & Operations Manual

**Site:** globaltaxguide.com
**GitHub Repo:** https://github.com/tk-cpa/globaltaxguide
**Branch:** main (deploys via GitHub Pages)
**Owner:** tk.cpa AI Lab

---

## 1. Deployment architecture

Plain static HTML/CSS/JS. No build step, no npm, no server-side rendering. Push to `main`, GitHub Pages serves it.

## 2. Header and footer: single source of truth (as of August 8, 2026)

**Do not hand-edit `<header class="site-header">` or `<footer class="site-footer">` blocks in individual page files.** Every page's header and footer is generated from two canonical files:

- `partials/header.html`
- `partials/footer.html`

Each contains `{{HOME}}` and `{{BASE}}` tokens, substituted per-file depending on directory depth:

| File location | HOME | BASE |
|---|---|---|
| Root pages (`index.html`, `about.html`, `map.html`, `zones.html`, `unions.html`, `trusted-resources.html`, `mission.html`, `disclaimer.html`) | `./` | `` (empty) |
| `countries/*.html` | `../` | `../` |

### To change the header or footer sitewide

1. Edit `partials/header.html` and/or `partials/footer.html` only.
2. Run `tools/apply_partials.py` (requires `GH_TOKEN` in the environment).
3. It rewrites the `<header>`/`<footer>` block in every HTML file on the site and pushes the result as **one atomic git tree commit** (not 230 separate commits).

This was deliberately built as a build-time propagation script rather than a client-side JS include (the pattern cpavalidated.com's `shared.js` uses for nav only). Reasoning: crawlers and LLMs that don't execute JavaScript need the real header/footer markup present in the HTML that's actually served, not injected after page load. A JS-injected header/footer would be invisible to any non-JS-executing crawler and would also risk the layout-shift issues `shared.js` has on cpavalidated.com.

### If you add a new root-level page

Add its filename to the `ROOT_PAGES` list at the top of `tools/apply_partials.py` before running it, or it won't get the header/footer treatment automatically.

### Why this exists

Prior to August 8, 2026, header and footer HTML was hand-duplicated into every one of 229+ country pages plus the hub pages, with no single source of truth - the same weakness cpavalidated.com still has today (documented "canonical snippet to copy-paste" in its own MAINTENANCE.md, no propagation script). This was flagged as unacceptable for a site aiming for full consistency and AI/crawler-friendliness, and fixed the same session it was raised. If a future session is tempted to hand-edit a header or footer in a single file "just this once," don't - fix the partial and run the script instead, or the drift comes back.

## 3. Footer structure (current)

The footer has three parts:
1. Tagline + link row (`tk.cpa`, `cpavalidated.com`, `About`) - `tk.cpa` links to the parent practice, `cpavalidated.com` to the sister US-tax-focused resource, `About` stays in-site.
2. A full disclaimer paragraph, present on every page (previously this only existed as an easy-to-miss low-opacity line on the homepage and about page - now sitewide).
3. A "Full disclaimer" link to `disclaimer.html`, a dedicated page (mirrors cpavalidated.com's `disclaimer.html`, which GTG didn't have until this was built).

## 4. Country page content build

See `QUEUE.md` for the live work queue, verification standard, and session-by-session history of which countries have full Residency/CFC/Thin Cap/Foreign Account Reporting/Treaty Network narrative content versus placeholder-only pages.

## 5. Things that break the site

- Editing a header/footer directly inside a single page file instead of through the partials + script. Causes drift, defeats the entire point of section 2.
- Adding a new root-level page without adding it to `ROOT_PAGES` in `tools/apply_partials.py`.
- Forgetting that `raw.githubusercontent.com` caches for a few minutes - always verify recent pushes via the Contents API (`gh.fetch()`), not the raw CDN URL, when checking whether a push actually landed.

## 6. Content quality standards - READ THIS BEFORE TOUCHING ANY COUNTRY PAGE

These rules exist because every one of them was violated at least once during production, caught by the site owner (not self-caught), and cost real time and trust to fix. They are not aspirational - they are the minimum bar. If you are a new session picking up this project, read this entire section before writing or editing a single country page.

### 6.1 Never publish a research-status report as if it were the answer

**Absolutely forbidden**, in any form, anywhere on any page: "not identified in available sources," "no sources show X," "was not confirmed this session," "flagged as an honest gap," or any variant that describes what you did or didn't find instead of what the law says.

This is not a wording problem you can fix by rephrasing. It is a research problem. The fix is to go get a better source - specifically, fetch the actual primary statute - not to reword the sentence so it doesn't match a banned-phrase search.

**What actually works:** fetch the primary tax law directly (national legal database, official government gazette, or the country's own Code/Act as hosted by a legal-aid or intergovernmental site) and read the relevant sections in full. Two real examples from this project where this changed the outcome entirely:

- **Lesotho CFC**: looked unresolvable via secondary sources. Fetching the full Income Tax Order 1993 directly found Section 106 ("Tax Havens") - a real, specific anti-avoidance mechanism, structurally different from a classic CFC regime but a genuine, citable answer.
- **Tuvalu CFC**: multiple sessions reported "not identified." The actual Income Tax Act 1992, Section 24(2), contains a real CFC-style attribution provision - it was just folded into the general anti-avoidance section instead of being separately labeled "CFC rules," so nobody had actually read that far into the statute.

If, after genuinely fetching and reading the primary law (not just searching secondary summaries again), no provision exists either way, that is a legitimate structural finding and should be stated as one - e.g., "X has no [tax] and therefore no domestic base for a CFC regime to operate against" - not as an unresolved search result.

### 6.2 Never invent cross-country reasoning to justify a gap

Forbidden: citing a neighboring country's law, a trade bloc's rules, or "the typical [regional] pattern" as if it's evidence about the subject country's own law. A customs union, geographic proximity, or a made-up phrase like "the typical Pacific-jurisdiction pattern" is not evidence of anything about the country you're writing about, and using it to sound more confident than you actually are is fabrication dressed as caution.

**Real example that was published and had to be pulled**: "given Lesotho's close economic integration with South Africa (which does have detailed CFC rules) and its Southern African Customs Union membership, confirm..." - South Africa's tax law has zero bearing on whether Lesotho has CFC rules. This sentence manufactured a false signal.

**Legitimate and different**: telling a reader that even though the subject country has no CFC regime of its own, *their own home country's* CFC rules may still apply to them if they're a tax resident elsewhere. That's a real, correctly-scoped legal fact about a different question (the reader's own exposure), not speculation about the subject country's law dressed up as relevant. But even this legitimate point should not be padded into a paragraph about four other countries' domestic rules on every page - state it in one sentence if it's genuinely useful, or leave it out. A jurisdiction's own reference page is not the place for a survey of other countries' law.

### 6.3 State the fact. Do not narrate the research process.

**Forbidden**: "Confirmed via a complete, direct review of the full primary text of [Act], both Chapter X and Chapter Y - the entirety of [country]'s national tax law, reviewed via [source]... this is a definitive finding from full statutory review rather than a gap." This is about the researcher, not about the country. Nobody reading a tax reference page needs proof that the work was done - they need the answer.

**Do this instead**: "Confirmed via [Act/source]: [the actual fact, in one or two sentences]." Match the concise, source-then-fact style already used correctly across most of the site, e.g. "Confirmed via GSL: Vanuatu has no Controlled Foreign Company rules." Cite the specific statute section inline where it adds real information (e.g., "Section 24(2)") but do not describe the process of finding it, the number of sections read, or make a meta-claim about the rigor of the finding. The citation and the source-row link are where rigor is demonstrated - not through adjectives in the prose.

### 6.4 Verify every citation link resolves - periodically, sitewide, with real HTTP checks

A citation with a dead link is worse than no citation. This project shipped 33 broken/unreliable citation URLs across the site (about 4.4% of all unique citation links) before this was caught - some genuinely dead (DNS failures, pages removed), some just transient. Do not assume a URL is good because a search snippet returned real-looking content from it - the search index can be stale.

**Run this check periodically** (script pattern established in `tools/` or reconstructed each session): extract every `href="https?://..."` from every country page's citation sections, HTTP-check each one (HEAD first, GET fallback, 2-3 retries with delay for anything that fails, since transient 503s are common and shouldn't cause a working link to be pulled), and triage:
- **Confirmed 404 or DNS failure on retry** → find a working replacement or remove the citation (never leave a dead link standing because the underlying fact is "probably still true")
- **403 on a known-legitimate site (law firm publications, established secondary sources)** → likely bot-blocking, not actually dead; verify by fetching once via a different method before concluding it's broken, then leave it
- **Redirect loop or persistent 503 across multiple retries with delay** → treat as broken, replace or remove

Also watch for **malformed cell values** in the quickchart summary boxes (the three-box Corporate/Personal/VAT rate display at the top of each page) - these should always be a clean percentage, or one of the accepted placeholder tokens (`Unverified`, `Varies`). A garbled value like a literal `"2027%"` (an automation artifact from prose text about a proposed future rate getting parsed into the numeric field) or a non-standard label like `"Real*"` should never ship. Run a structural sweep for any cell value that doesn't match `\d+(\.\d+)?%\*?` or an accepted token - this catches a different defect class than a citation-link check and both are needed.

### 6.5 Sourcing hierarchy - don't name one firm as "the main source"

Describe sourcing in tiers, not by naming a single dominant secondary compiler: (1) national tax authority publications and the primary tax statute itself, where accessible - always preferred when available; (2) reputable Big Four / second-tier firm guides (PwC Worldwide Tax Summaries, EY, Deloitte, KPMG, etc.) as the standard secondary cross-check; (3) independent data compilations (e.g., Tax Foundation's annual global corporate rate comparison, which is genuinely valuable for cross-checking and Pillar Two/QDMTT status) for further corroboration. See `trusted-resources.html` for the maintained list. Do not write anything in `about.html` or elsewhere implying the site's rates come "mostly from PwC" - that's both slightly inaccurate (many pages are now primary-law-sourced) and reads as an admission of thin sourcing rather than a description of a real hierarchy.

### 6.6 When two sources conflict, resolve it - don't just flag it

If one source says X and another says Y, the job is not finished by noting the disagreement. Check dates (a newer reform may have superseded an older figure - this happened repeatedly this session: Kazakhstan's 2026 Tax Code, Afghanistan's 2026 reform, Macau's 2026 Tax Code all invalidated older secondary-source figures that were still being cited elsewhere), check authority (a government's own primary document beats a secondary aggregator - the UK government's own archived treaty document, literally filed as "...terminated.pdf," resolved a Lesotho-UK treaty status conflict definitively), and check specificity (a source citing a named statute section beats one making a general claim). Only present a conflict as genuinely unresolved after this kind of triage has actually been attempted and failed - and even then, don't just describe the disagreement; say plainly which figure the page uses and why, with the rejected figure noted briefly for transparency.

### 6.7 A rate cell should show the general/default rate, not an exception dressed as the headline

Multiple pages this session were caught showing a sector-specific, non-representative rate in the general corporate/personal rate cell (an oil-sector rate for Bahrain, a listed-company rate for Bangladesh, an excise rate mislabeled as VAT for Syria, a "major corporation" flat 21% rate presented instead of the 3% Gross Revenue Tax that actually applies to nearly all Micronesian businesses). When a jurisdiction has a notably unusual-looking headline number, trace it back to what population of taxpayers it actually applies to before trusting it as the general answer.

