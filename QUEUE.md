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

## In queue - not yet started

### High priority
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
- [ ] **Nav rollout to all 229 country pages** - the Map and Trusted
      Resources links were added to the five hub pages (index, unions,
      zones, about, mission) only. The 229 individual country pages were
      not touched this session and still show the old 5-link nav. Rolling
      this out means a real batch edit across 229 files - queued, not done.

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
