# Global Tax Guide - Live Work Queue

Last updated: August 8, 2026. This file tracks everything not yet complete so
nothing raised in prior sessions gets lost between chats. Update this file
(don't just remember it) whenever an item is started, finished, or added.

## Done this session (August 8, 2026)

- [x] Interactive world map built and pushed (`/map.html`, `/assets/world-map.svg`)
      - 180 jurisdictions clickable directly on the map graphic
      - Region filter (Africa / Americas / Asia-Pacific / Europe / Middle East)
      - 49 micro-jurisdictions too small to render at this resolution listed as
        direct links below the map, filterable by the same region control
      - Base map CC BY-SA 3.0 (Al MacDonald, edited by Fritz Lekschas),
        attribution on page
- [x] Trusted Resources page built and pushed (`/trusted-resources.html`)
      - Official primary sources: IRS treaty A-to-Z, IRS treaty tables, GOV.UK
        tax treaties collection
      - Big Four: PwC WWTS, EY Corporate Tax Guide, EY VAT/GST Guide, EY Tax
        Guides hub, Deloitte DITS, KPMG Global Tax Services
      - Second-tier: Grant Thornton Global Transfer Pricing Guide
      - All links live-verified via search/fetch before publishing, not
        assumed
- [x] CNAME file added (`globaltaxguide.com`) - was missing, needed before the
      GoDaddy DNS connection will work
- [x] Site nav updated on index, unions, zones, about, mission to include
      Map and Trusted Resources

## Scoping correction (August 8, 2026, this session)

Audited all 229 local country pages programmatically. **222 of 229** have
only quick-chart rate data plus an honest placeholder ("full narrative
detail... is on the build list for this page") for Residency / CFC / Thin
Cap / Treaty Network content. Only **7** pages (United Kingdom + the
manually-researched batch: Russia, Belarus, Monaco, San Marino, Vatican
City, Iran, Syria, Yemen and a few others from that earlier session) have
real written-out narrative sections. This means "treaty network
interlinked," "CFC rules for every country," and "direct links to treaty
documents throughout" are not close to done - they are un-started for
~97% of jurisdictions. This is the real, large remaining task, larger than
the map/resources-page work finished earlier today. Flagging this
precisely so priority decisions are made with accurate information rather
than an inflated sense of completion.

Two treaty-portal links added to real content so far: United Kingdom
(-> GOV.UK), United States (-> IRS A-to-Z).

## Continuous narrative-content batch (August 8, 2026, in progress)

Working through G20 first (highest practical value), verified against primary
sources or Trusted Resources guides before writing, no pauses for approval
between countries per standing directive. Progress so far:

- [x] United States - Residency (IRC 7701(b), SPT/Green Card Test), CFC/NCTI
      (IRC 957, OBBBA changes: 250 deduction to 40%, QBAI eliminated, ~12.6%
      ETR, 951B), Thin Cap (163(j), EBITDA restored), Treaty Network (~65
      countries per IRS Table 3, USSR-successor treaties, Hungary
      termination) - linked to IRS A-to-Z
- [x] Germany - Residency (Wohnsitz/gewohnlicher Aufenthalt), CFC (AStG
      Section 7-14, low-tax threshold reduced 25%->15% in 2024), Thin Cap
      (Zinsschranke Section 4h EStG, 30% EBITDA, EUR 3m de minimis), Treaty
      Network (~90 countries per PwC, notable gaps: Brazil, Hong Kong, UAE
      expired 2021) - linked to IRS Germany treaty documents page (link
      verified live before publishing)
- [ ] Remaining G20: China, Japan, France, India, Brazil, Italy, Canada,
      South Korea, Russia, Australia, Mexico, Indonesia, Saudi Arabia, South
      Africa, Turkiye, Argentina - not yet started, continuing next
- [ ] Remaining ~209 non-G20 countries after G20 batch completes

Note: this is genuinely slow, verified work - each country requires several
real searches (residency test, CFC regime specifics, thin cap/interest
limitation rule, treaty network size and gaps) before writing a single
paragraph. Claims of "done" in this file mean actually verified and live,
never assumed.

### High priority
- [ ] **The actual narrative content build for 222 stub pages** - residency
      tests, CFC rules, thin cap rules, and treaty network detail, each
      verified against a primary source or Trusted Resources guide before
      writing. This is the real work behind "comprehensive treaty network"
      and needs a batch order decision: major economies first (G20 /
      largest treaty networks) vs. full alphabetical/regional sweep. Not
      started pending that decision.
- [ ] **GoDaddy DNS connection walkthrough** - CNAME is now in the repo;
      still need to confirm GitHub Pages custom domain setting is enabled in
      repo settings and walk through the four A records + www CNAME at GoDaddy
- [ ] **Interlink treaty mentions to treaty documents** - every place a
      country page mentions "treaty network" or a specific treaty partner
      should link to the actual treaty text (IRS A-to-Z, HMRC collection, or
      the partner country's own tax authority). Not yet built - requires
      going page by page since this must not be templated/guessed per
      country; each link needs to be confirmed live.
- [ ] **CFC rules deep-dive content** - current country pages have a CFC
      summary line; a dedicated CFC rules explainer (or expanded per-country
      CFC section) with primary-source citations is still open
- [ ] **Customs & tariffs coverage** - not yet built. This is a large,
      genuinely separate research task from income/VAT rates (different
      primary sources: national customs authorities, WCO, WTO tariff
      schedules). Needs explicit scoping before starting: which countries
      first, what data points (MFN rate bands, free trade agreement
      preferences, de minimis thresholds), and which primary source each
      figure will be checked against. Not started because doing this
      correctly for 229 jurisdictions without guessing is a multi-day
      research project, not a page-template exercise.
- [ ] **Non-tax regulatory levies** (e.g. India's Equalization Levy) - agreed
      as in-scope; not yet started. Needs its own verification pass per
      country, not a bolt-on to existing pages.

### Medium priority
- [ ] **EU / USMCA / other trade-bloc special maps or sections** -
      `/unions.html` already exists and covers EU VAT directive, CARICOM,
      CIS, USMCA at a narrative level. Whether this needs dedicated
      sub-maps (vs. the current text page) is an open design question -
      flagging rather than assuming.
- [ ] **Trusted Resources page - ongoing expansion** - page is live; still
      want to identify and verify additional second-tier/boutique firm
      guides (BDO, Mazars/Forvis Mazars, RSM International) - initial search
      did not turn up a clean free global guide from BDO comparable to the
      Big Four's; needs another look.
- [x] **Nav rollout to all 229 country pages** - done. Single atomic git
      tree commit (`5b3b448a`) updated all 229 country pages plus the 5 hub
      pages to the new 7-link nav (added Map, Trusted Resources). Verified
      programmatically post-push: all 229 pages contain both new links and
      zero em-dashes.

### Lower priority / already flagged in AUTOMATION.md
- [ ] Automated weekly GitHub Actions verification - `.github/workflows/
      weekly-tax-check.yml` and `scripts/verify_rates.py` already exist per
      AUTOMATION.md; confirm it is actually enabled/running and review its
      first output before trusting it
- [ ] Continue country-by-country treaty network expansion (the actual
      per-country treaty partner lists) - genuine research work, one
      jurisdiction at a time, verified against primary sources only

## Explicit non-negotiable, carried forward from every prior session

No rate, treaty fact, customs figure, or regulatory levy is ever published
without being checked against a primary source or a Big Four/second-tier
guide from the Trusted Resources list in the current session. If it cannot
be verified, the page says "not independently verified" - it is never
estimated, inferred from a neighboring country, or left unmarked.
