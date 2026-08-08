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
- [x] China - Residency (183-day/6-year rule, domicile), CFC (12.5% threshold,
      50%/10% ownership, white list, RMB 5m de minimis), Thin Cap (2:1/5:1
      safe harbor ratios), Treaty Network (114 countries/regions per PwC
      30 June 2026, HK/Macao SAR arrangements, TIEAs)
- [x] Japan - Residency (permanent/non-permanent resident split, 5-of-10-year
      test), CFC (FRC >50% ownership, 20%/27%/30% trigger rates), Thin Cap
      (3:1 safe harbor + separate 20% earnings stripping rule), Treaty
      Network (90 conventions / 157 jurisdictions per PwC 1 May 2026)
- [x] France - Residency (Article 4B: home/183-day/economic-interest tests,
      any one sufficient), CFC (Article 209B, >50% ownership, 40%-lower
      privileged-regime threshold), Thin Cap (2019 ATAD reform, EUR 3m/30%
      EBITDA, 1.5 debt-equity ratio), Treaty Network (120+ countries,
      Mali/Niger terminations, Russia suspension, unratified treaties noted)
- [x] India - Residency (Section 6, 182/60-day tests, RNOR/Ordinarily
      Resident split), CFC (confirmed: India has NO CFC regime, relies on
      GAAR + transfer pricing instead - flagged honestly, not templated),
      Thin Cap (Section 94B, 30% EBITDA cap, INR 1 crore threshold), Treaty
      Network (~94 comprehensive DTAAs + 8 limited, MLI since Oct 2019)
- [x] Brazil - Residency (183-day/12-month rolling window), CFC (Lei
      14.754/2023, annual deemed-profit inclusion regardless of
      distribution, flat 15% individual rate, control aggregation across
      family), Thin Cap (2:1 / 0.3:1 low-tax-jurisdiction ratio, IN RFB
      1,154/2011), Treaty Network (~36 countries per PwC, notably NO US
      treaty - flagged)
- [x] Italy - Residency (2023 reform: Anagrafe/domicile/physical-presence
      tests, any one for 183 days), CFC (2024 simplified 15% ETR + 1/3
      passive-income test, 15% substitute-tax election), Thin Cap (ROL
      30% gross operating margin, formal thin cap abolished), Treaty
      Network (~100 countries per Agenzia delle Entrate)
- [x] Canada - Residency (significant residential ties + 183-day deemed-
      resident test), CFC (FAPI/Controlled Foreign Affiliate, >50%
      ownership, $5,000 de minimis), Thin Cap (1.5:1 ratio + newer EIFEL
      30% tax-EBITDA rule effective Oct 2023, exclusions for CCPCs),
      Treaty Network (~90-95 countries, Russia suspended Nov 2024)
- [x] South Korea - Residency (domicile/183-day rolling test, 2026 anti-
      split-year rule), CFC (10% ownership, ETR <70% of top CIT rate
      ~16.8%), Thin Cap (2:1/6:1 + 30% BEPS interest cap), Treaty Network
      (97 countries per PwC Jan 2026, TIEAs with low-tax jurisdictions)
- [x] Russia - Residency (Article 207, 183-day rolling 12-month test),
      CFC (25%/10% ownership thresholds, lump-sum election option),
      Thin Cap (Article 269, 3:1/12.5:1 ratios), Treaty Network (~84
      treaties, Decree 585 suspended 38 "unfriendly" countries' reduced
      rates in 2023, permanent denunciations by Netherlands/Denmark/
      Latvia/Lithuania flagged, US suspension noted)
- [x] Australia - Residency (4 independent tests: Resides/Domicile/183-day/
      Superannuation, bright-line reform noted as pending), CFC
      (attributable income, listed/unlisted country + active income test),
      Thin Cap (2023 EBITDA reform: Fixed Ratio/Group Ratio/Third-Party
      Debt tests replacing asset-based rule), Treaty Network (46 countries
      per PwC, several signed-not-in-force treaties flagged)
- [x] Mexico - Residency (Article 9: permanent home + center-of-vital-
      interests test, REFIPRE 5-year tail for departing citizens), CFC
      (REFIPRES framework, 75%-of-Mexican-rate threshold, case-by-case),
      Thin Cap (3:1 ratio + 30% BEPS interest cap, 40% REFIPRE withholding),
      Treaty Network (60 countries, notable gaps listed, MLI since July
      2023 with US/Germany exceptions)
- [x] Indonesia - Residency (Article 2, 183-day/12-month cumulative test),
      CFC (PMK-93/2019, 50% paid-up capital threshold, deemed dividend
      timing rules), Thin Cap (4:1 debt-equity ratio), Treaty Network
      (71 countries, UN Model-based)
- [x] Saudi Arabia - Residency/Zakat split (no personal income tax; Zakat
      2.5% for Saudi/GCC shareholders vs 20% CIT for non-Saudi share, 183-
      day PE test), CFC (confirmed: NO CFC regime), Thin Cap (confirmed:
      NO formal thin cap rule, only 50%-of-taxable-income interest cap),
      Treaty Network (61 treaties, MLI since 2018)
- [x] South Africa - Residency (ordinarily-resident + 91/915-day physical
      presence tests, 330-day exit rule), CFC (Section 9D, >50% ownership,
      10% de minimis, FBE exemption, 67.5% high-tax exemption), Thin Cap
      (arm's-length test since 2012, former 3:1 safe harbor abolished),
      Treaty Network (79 countries, largest in Africa)
- [x] Turkiye - Residency (GVK Article 4: domicile OR 6-month presence,
      Article 5 exceptions), CFC (KVK Article 7: 50% control + 25% passive
      income + <10% ETR + TRY 100k threshold), Thin Cap (3:1/6:1 ratios,
      Law 5520 Article 12), Treaty Network (85+ countries)
- [x] Argentina - Residency (Article 116, 12-month continuous presence,
      90-day absence tolerance/reset), CFC (2019 regime, 50pct+ ownership,
      75pct-of-Argentine-rate threshold, majority-passive-income test),
      Thin Cap (30% EBITDA-style cap, BEPS Action 4), Treaty Network
      (24 countries, no US treaty, MLI effective Jan 2026)

## G20 BATCH COMPLETE (August 8, 2026)

All 19 G20 jurisdictions (US, UK already done pre-session, Germany, China,
Japan, France, India, Brazil, Italy, Canada, South Korea, Russia,
Australia, Mexico, Indonesia, Saudi Arabia, South Africa, Turkiye,
Argentina) now have verified Residency/CFC/Thin Cap/Treaty Network
narrative content, each checked against primary sources or PwC/national
tax authority guides in the current session, no fabrication, no template
copy-paste across countries (several - India, Saudi Arabia - honestly
report NO CFC regime rather than forcing a template answer).

## Non-G20 batch, major economies first (in progress)

- [x] Spain - Residency (183-day + economic-interest test), CFC
      (Transparencia Fiscal Internacional, Art 100 LIS/91 LIRPF, 50pct
      ownership + 75pct-of-Spanish-rate threshold), Thin Cap (repealed
      formal ratio; 30% EBITDA + EUR 1m minimum since 2024 reform),
      Treaty Network (90+ countries, MLI phase-in dates)
- [x] Netherlands - Residency (facts-and-circumstances test, no fixed day
      count), CFC (2019 ATAD regime, 50pct ownership + <9pct-rate/blacklist
      + 30pct-passive-income test, substance carve-out), Thin Cap (no
      formal ratio; strict 24.5% EBITDA earnings-stripping rule for 2026,
      tighter than ATAD minimum), Treaty Network (~90-100 countries,
      Russia termination noted)
- [x] Switzerland - Residency (30-day-with-work/90-day-without-work rules,
      no 183-day threshold, domicile alternative), CFC (confirmed: NO CFC
      regime, one of few developed economies without one; substance-based
      case law safeguard only), Thin Cap (no fixed ratio; per-asset-class
      FTA safe-harbor percentages, 6:1 for finance companies), Treaty
      Network (100+ countries plus separate estate/inheritance treaties)
- [x] Sweden - Residency (essential connection/vasentlig anknytning,
      6-month/10-year presumption rules), CFC (25% ownership + 55%-of-
      Swedish-rate threshold, white-list/EEA exclusions), Thin Cap (no
      formal ratio; 30% EBITDA cap since 2019, SEK 5m de minimis, targeted
      anti-avoidance rule), Treaty Network (count honestly flagged as
      uncertain - sources range 44 to 100+, pointed to Skatteverket as
      authoritative rather than asserting an unverified figure)
- [x] Belgium - Residency (domicile/seat-of-wealth test, National Register
      presumption, irrebuttable family-residence presumption for married
      individuals), CFC (2023/2024 Model A entity-approach reform, 50pct
      ownership + half-Belgian-rate threshold, 1/3-passive-income safe
      harbor), Thin Cap (layered 1:1 director loans / 5:1 tax-haven loans
      / 30pct-EBITDA-or-EUR3m general rule), Treaty Network (150+
      countries per PwC, 99 designated MLI Covered Tax Agreements)
- [ ] Next: additional major non-G20 economies - continuing
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
