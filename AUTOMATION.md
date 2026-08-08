# Automated Weekly Rate Verification - Setup Guide

This repo includes a working GitHub Actions workflow that checks a rotating
batch of country pages every week against PwC, KPMG, EY, BDO, Grant Thornton,
and national tax authority sources, and opens a pull request with anything it
finds - it does not silently edit the live site.

## What's already built

- `.github/workflows/weekly-tax-check.yml` - runs every Monday at 09:00 UTC,
  or on demand from the Actions tab (with an optional single-country input
  for testing on one page before trusting it on the whole site).
- `scripts/verify_rates.py` - the actual verification logic. Picks the 30
  pages with the oldest "last verified" date (so the full ~230-page site
  cycles through roughly every 7 weeks), asks Claude with web search enabled
  to check each one against named reference sources, and only touches a
  page if the finding is marked high-confidence.
- Every run produces a pull request titled "Weekly rate verification -
  YYYY-MM-DD" with a markdown table showing exactly what was checked, what
  (if anything) changed, and which source supports each change - reviewable
  before merging.

## One-time setup to activate it

1. Get an Anthropic API key from console.anthropic.com if you don't already
   have one for this purpose.
2. In the GitHub repo (`tk-cpa/globaltaxguide`): **Settings > Secrets and
   variables > Actions > New repository secret**.
   - Name: `ANTHROPIC_API_KEY`
   - Value: your key
3. That's it. The workflow will run automatically starting the following
   Monday, or you can trigger it immediately: **Actions tab > Weekly Tax
   Rate Verification > Run workflow**.

## Recommended first run

Before trusting it on the full batch, test it on one page:
**Actions > Weekly Tax Rate Verification > Run workflow > country_slug:
`united-kingdom`** (or any slug you want to spot-check). Review the PR it
opens. If the change looks right and the source citation is real, you can
trust the weekly batch runs.

## How to move from "opens a PR" to "auto-merges"

By default every run opens a PR for review - nothing goes live without a
human looking at it first. Once you've watched a few weeks of runs and
trust the output, you can either:
- Tick `auto_merge: true` when manually triggering a run, or
- Edit the workflow's scheduled trigger to pass `auto_merge: true` by
  default (change the `workflow_dispatch` default, or add
  `--auto-merge` unconditionally in the "Auto-merge if requested" step).

Given how consequential silently wrong tax data would be, the recommended
posture is to keep human review in the loop indefinitely, even after the
system has proven reliable - the PR review takes a couple of minutes a week.

## Extending the source list

`scripts/verify_rates.py` has a `REFERENCE_SOURCES` list at the top. Add or
reorder entries there to change what Claude is instructed to prioritize.
Currently: PwC Worldwide Tax Summaries, KPMG Tax Rates Online, EY Worldwide
Corporate Tax Guide, EY Worldwide VAT/GST/Sales Tax Guide, BDO Global Tax
Guides, Grant Thornton international tax guides, and each jurisdiction's own
national tax authority site where locatable.

## Known limitations of this first version

- It only updates the three headline rate numbers and the "last verified"
  date - it does not (yet) rewrite the narrative residency/CFC/treaty
  sections, which still need to be built out page-by-page separately.
- It checks a rotating batch, not the whole site every week, to keep API
  costs and review burden manageable - full-site coverage takes ~7 weeks.
- Confidence scoring is self-reported by the model; spot-check its stated
  sources periodically rather than assuming "high confidence" is infallible.
- Currently wired to the `united-kingdom`-style narrative pages and the
  simpler quickchart-only pages equally - it does not yet distinguish
  between them when deciding what to touch (which is intentional: it never
  touches narrative prose regardless of page type).
