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
- [x] Ireland - Residency (183/280-day test, ordinary residence after 3
      years), CFC (ATAD non-genuine-arrangements test, >50% control), Thin
      Cap (no fixed ratio; 30% EBITDA ILR since 2022, EUR3m de minimis,
      standalone/legacy-debt exclusions), Treaty Network (78 signed/75 in
      force per Chambers 2026)
- [x] Luxembourg - Residency (domicile/6-month habitual abode test),
      CFC (Article 164ter, 50% control + <50%-of-Lux-rate threshold,
      EUR750k/10%-opex exclusion), Thin Cap (85:15 administrative
      benchmark, not legally binding per courts + 30% EBITDA ATAD rule),
      Treaty Network (94 signed/88 in force per PwC)
- [x] Austria - Residency (domicile/6-month habitual abode test), CFC
      (Section 10a, 12.5% low-tax threshold, 1/3-passive-income
      exclusion), Thin Cap (no statutory ratio, hidden-equity case law +
      Section 12a 30pct EBITDA rule), Treaty Network (100 countries)
- [x] Denmark - Residency (permanent residence + qualifying stay or
      6-month presence), CFC (50pct control + 1/3-income test, no
      jurisdiction list), Thin Cap (triple-layer: 4:1 ratio / interest
      ceiling de minimis / 30pct EBITDA), Treaty Network (77 countries)
- [x] Norway - Residency (183/270-day + domicile test, emigration exit
      conditions), CFC (NOKUS, 50pct control + two-thirds-rate threshold,
      treaty/EEA exemptions), Thin Cap (no fixed ratio; 25pct EBITDA cap
      since 2019, NOK25m/NOK5m thresholds), Treaty Network (89 countries)
- [x] Singapore - Residency (183-day test with 2-year straddle concession),
      CFC (confirmed: NO CFC regime), Thin Cap (confirmed: NO formal
      thin cap rule, GAAR/transfer pricing backstop only), Treaty Network
      (98 comprehensive + 8 limited DTAs, NO US treaty flagged, 2025
      substance requirement noted)
- [x] Portugal - Residency (183-day + habitual abode test, exit tax noted),
      CFC (ATAD 25pct/10pct thresholds, 50pct-rate/60pct-rate tests, EU/EEA
      substance carve-out), Thin Cap (no ratio; EUR1m/30pct EBITDA cap),
      Treaty Network (~78-80 countries, UK 2026 update, Finland/Sweden
      terminations)
- [x] Czech Republic - Residency (permanent home/183-day test, deemed-
      resident categories regardless of days), CFC (ATAD 50pct threshold),
      Thin Cap (30pct EBITDA rule), Treaty Network (99 treaties per
      official gov.cz list, Belarus suspension 2024-2026 noted)
- [x] Finland - Residency (permanent home/6-month test), CFC (25pct
      ownership + three-fifths-of-Finnish-rate threshold, EEA/non-EEA
      escape rules), Thin Cap (no ratio; EUR500k/25pct EBITDA rule + EUR3m
      non-group carveout), Treaty Network (70+ countries)
- [x] Hong Kong SAR - Residency (territorial system, residency mainly
      relevant for treaty access; CMC test for companies, ordinary-
      residence/180-300-day test for individuals), CFC (confirmed: NO CFC
      regime), Thin Cap (confirmed: NO thin cap rules; FSIE 2023 exception
      flagged), Treaty Network (~45-51 CDTAs, exact count flagged as
      varying by source)
- [x] UAE - Residency (183/90-day + center-of-financial-interests tests,
      TRC vs domestic residency gap noted), CFC (confirmed: NO CFC regime
      - resolved a genuine source conflict by cross-checking PwC/Chambers
      against a claim of CFC rules from a lower-quality source; also
      flagged the reverse risk of home-country CFC rules attributing UAE
      income back to foreign shareholders), Thin Cap (no ratio; Article 30
      30pct EBITDA/AED12m interest cap), Treaty Network (130-140+
      countries, exact count flagged as approximate, no US treaty)
- [x] Poland - Residency (183-day/center-of-interests test), CFC
      (multi-test regime: 50pct control + 25pct-lower-rate + 33pct-passive-
      income, plus tax-haven catch-all; flat 19% CFC rate applies even to
      undistributed profits), Thin Cap (Article 15c, PLN3m/30pct EBITDA
      cap), Treaty Network (~100 countries per Ministry of Finance)
- [x] Malaysia - Residency (Section 7(1) four alternative tests: 182-day/
      linked-182/90-day-with-history/no-presence-but-history), CFC
      (confirmed: NO CFC regime), Thin Cap (no formal ratio; 20pct EBITDA
      interest cap per source, forfeited on shareholder change), Treaty
      Network (70+ countries, no US treaty)
- [x] Thailand - Residency (Section 41, 180-day test), CFC (confirmed:
      NO CFC provisions), Thin Cap (confirmed: NO general rule, incentive-
      linked exceptions only), Treaty Network (61 countries, 2024
      remittance rule change flagged as key context)
- [x] Vietnam - Residency (183-day/permanent-residence/leased-housing
      tests), CFC (confirmed: NO CFC legislation), Thin Cap (no formal
      rule; Decree 132 30pct EBITDA cap on related-party interest, license-
      based debt cap separately), Treaty Network (81 countries per PwC,
      US treaty status resolved: signed 2015/ratified by Vietnam 2017 but
      not ratified by US, so not in force)
- [x] Philippines - Residency (Section 23, 183-day test), CFC (confirmed:
      NO CFC regime), Thin Cap (confirmed: NO formal rule; tax arbitrage
      interest reduction noted, exact percentage flagged as needing
      reconfirmation), Treaty Network (~40-44 countries, 10 more in
      negotiation as of mid-2026, TTRA process required)
- [x] Taiwan - Residency (Article 7, 183-day/domicile test), CFC (50pct
      ownership + <14pct-rate threshold, substance/de-minimis exemptions),
      Thin Cap (3:1 ratio), Treaty Network (35 countries, no US treaty,
      reciprocal relief framework flagged as pending)
- [x] Pakistan - Residency (183-day/120+365-day tests), CFC (50pct + 60pct-
      of-rate threshold), Thin Cap (3:1 ratio + fixed-ratio test), Treaty
      Network (68 countries per PwC)
- [x] Bangladesh - Residency (182-day/90-day-with-4yr-history test), CFC
      (confirmed: NO CFC rules per PwC), Thin Cap (confirmed: NO regime,
      70:30 non-binding BIDA guideline noted), Treaty Network (40+
      countries, NBR TRC required)
- [x] Sri Lanka - Residency (183-day test, 2-consecutive-year/12-month-
      absence rule), CFC (confirmed: NO CFC regime), Thin Cap (3:1
      manufacturers/4:1 others, 6-year carryforward), Treaty Network
      (44 countries, India PPT protocol update flagged)
- [x] Nepal - Residency (Section 2(ka), 183-day/365-day-window test), CFC
      (honestly flagged: no dedicated CFC attribution regime found;
      GAAR/transfer pricing reliance noted instead of asserting a
      confident "no"), Thin Cap (Section 14 interest limitation exists,
      exact ratio flagged as unconfirmed across sources), Treaty Network
      (11 countries, dual-resident anti-abuse rule)

## South Asia batch complete (India, Pakistan, Bangladesh, Sri Lanka,
## Nepal all done)

- [x] Greece - Residency (183-day/center-of-interests test, tourism/
      medical exclusion), CFC (ATAD-aligned, 50pct threshold, taxes
      passive income only), Thin Cap (no ratio; Article 49 30pct EBITDA
      cap), Treaty Network (57 countries, Sweden termination flagged)
- [x] Hungary - Residency (citizenship/EEA/vital-interests hierarchy),
      CFC (50pct + half-rate threshold since 2019, genuine-arrangement
      carveout), Thin Cap (30pct EBITDA cap + 3:1 grandfather option),
      Treaty Network (80+ countries, no US treaty, Russia suspension
      flagged)
- [x] Romania - Residency (domicile/vital-interests/183-day test), CFC
      (ATAD proportional inclusion), Thin Cap (no ratio; 30pct EBITDA/
      EUR1m cap), Treaty Network (90+ countries)
- [x] Slovakia - Residency (183-day/dwelling test + anti-avoidance
      fallback), CFC (extended to individuals 2019, non-cooperative
      jurisdiction catch), Thin Cap (30pct-of-adjusted-base rule),
      Treaty Network (60-70 countries)
- [x] Croatia - Residency (multi-test incl. real-estate-availability
      trigger, not a simple day count), CFC (50pct threshold since 2019),
      Thin Cap (dual: 4:1 safe harbor + 30pct EBITDA ATAD), Treaty
      Network (60-65 countries, US/Australia/NZ treaties pending)
- [x] Slovenia - Residency (formal/actual residential tie test), CFC
      (50pct threshold since 2019, taxes passive income only), Thin Cap
      (abolished Jan 2025 - flagged as recent change), Treaty Network
      (60+ countries)
- [x] Bulgaria - Residency (183-day/vital-interests test), CFC (50pct +
      half-rate threshold, substance carveout), Thin Cap (dual: 3:1 ratio
      + EUR3m ATAD interest limitation), Treaty Network (70+ countries)
- [x] Iceland - Residency (183-day/domicile test, 3-year post-departure
      tail), CFC (50pct low-tax-list threshold, EEA/treaty carveouts),
      Thin Cap (no ratio; 30pct EBITDA/ISK100m cap), Treaty Network
      (44 countries + Nordic multilateral)
- [x] Malta - Residency (domicile/permanent-home basis, non-dom
      remittance system), CFC (ATAD 50pct + low-tax test since 2019),
      Thin Cap (confirmed: NO ratio; 30pct EBITDA/EUR3m interest cap),
      Treaty Network (~70 countries)
- [x] Cyprus - Residency (183-day/60-day dual test, 2026 dual-residency
      reform removing exclusivity condition), CFC (ATAD 50pct non-genuine-
      arrangement test since 2019), Thin Cap (no ratio; 30pct EBITDA/
      EUR3m cap), Treaty Network (65-67 countries, France treaty 2026
      approval flagged)
- [x] Estonia - Residency (183-day rolling/permanent-home test), CFC
      (ATAD since 2019), Thin Cap (ATAD rules exist, mechanics flagged as
      needing confirmation given Estonia's unique deferred-tax corporate
      system), Treaty Network (60+ countries, US treaty in force)
- [x] Latvia - Residency (183-day/declared-residence test), CFC (dual
      corporate/individual regimes, 50pct/25pct thresholds), Thin Cap
      (deemed-dividend rule + EUR3m ATAD cap), Treaty Network (60+
      countries, distributed-profits-only CIT system flagged)
- [x] Lithuania - Residency (183/280-day multi-test), CFC (50pct+10pct
      + 75pct-of-rate threshold, passive income only), Thin Cap (dual:
      4:1 whole-disallowance + 30pct EBITDA/EUR3m), Treaty Network
      (58 countries)

## Baltic states complete (Estonia, Latvia, Lithuania all done)

- [x] Serbia - Residency (183-day/vital-interests test), CFC (confirmed:
      NO CFC rules), Thin Cap (4:1/10:1 ratios), Treaty Network (64
      countries, no US treaty)
- [x] Ukraine - Residency (cascading OECD-style test), CFC (2022 regime,
      13pct-rate/50pct-passive/EUR2m thresholds), Thin Cap (3.5:1 ratio +
      30pct interest cap), Treaty Network (70 in force per Ministry of
      Finance, war-related terminations and 2025-2026 new treaties
      flagged)
- [x] Bosnia and Herzegovina - Residency (entity-fragmented FBiH/RS/BD
      system, 183-day/vital-interests test), CFC (confirmed: NO CFC
      rules), Thin Cap (FBiH-only 4:1 ratio, RS/BD have none), Treaty
      Network (40+ countries)
- [x] North Macedonia - Residency (183-day/permanent-residence test),
      CFC (confirmed: NO CFC rules), Thin Cap (3:1 ratio, 20pct
      shareholder threshold, 3-year startup exemption), Treaty Network
      (48 countries)
- [x] Montenegro - Residency (183-day/domicile/vital-interests test),
      CFC (confirmed: NO CFC rules), Thin Cap (confirmed: NO thin cap
      rules), Treaty Network (44 countries)
- [x] Albania - Residency (183-day/permanent-home test), CFC (Law 29/2023
      individual-only regime since 2024), Thin Cap (abolished, replaced by
      30pct EBITDA rule on all debt - resolved conflict with outdated 4:1
      ratio claim), Treaty Network (40+ countries)
- [x] Kosovo - Residency (183-day/vital-interests test), CFC (confirmed:
      NO regime), Thin Cap (confirmed: NO rules), Treaty Network (21
      countries per ATK, reflects recent statehood, no US treaty)

## Balkans/Southeast Europe complete (Serbia, Ukraine, Bosnia, North
## Macedonia, Montenegro, Albania, Kosovo all done)

- [x] Chile - Residency (Law 21.210 2020 183-day test, resolved PwC's
      own page citing outdated pre-2020 six-month rule; domicile
      alternative), CFC (Article 41 G, 10pct/80pct passive-income tests +
      UF2400 threshold), Thin Cap (3:1 ratio + 35pct excess tax, interest
      still deductible), Treaty Network (37 countries, US treaty since
      2024, no Germany treaty)
- [x] Colombia - Residency (183-day/365-window test + national-specific
      tests), CFC (10pct threshold, 80pct-passive-deemed rule), Thin Cap
      (2019-reformed 2:1 related-party-only ratio), Treaty Network
      (~15 countries, no US treaty)
- [x] Peru - Residency (183-day domiciled test, year-start fixation rule),
      CFC (since 2013, 50pct + tax-haven threshold), Thin Cap (evolution
      from 3:1 ratio to 30pct EBITDA rule since 2021), Treaty Network
      (~9-16 countries + Andean Community framework, new UK 2026 treaty,
      no US treaty)
- [x] Uruguay - Residency (vital-interests/investment-based routes), CFC
      (confirmed: NO corporate regime, individual-only 2017 Fiscal
      Transparency Law), Thin Cap (confirmed: NONE), Treaty Network
      (named list + 30+ TIEAs)
- [x] Ecuador - Residency (183-day/economic-interests test), CFC (2024
      regime, 25pct + 15pct-rate threshold, PwC/Chambers figures
      reconciled as consistent), Thin Cap (20pct-of-pretax-profit),
      Treaty Network (named list + Andean Community)
- [x] Panama - Residency (territorial system, 183-day test of limited
      relevance), CFC (confirmed: NONE), Thin Cap (confirmed: NONE),
      Treaty Network (17-18 countries, no US/Canada treaty)
- [x] Paraguay - Residency (territorial, no 183-day test), CFC (confirmed:
      NONE), Thin Cap (honestly flagged as conflicting across sources),
      Treaty Network (3-6 countries, very limited)
- [x] Bolivia - Residency (territorial, 183-day/permanent-home test), CFC
      (confirmed: NONE), Thin Cap (shareholder-funding restriction only,
      no formal ratio), Treaty Network (~15 countries, unilateral
      terminations of Luxembourg/Netherlands/Spain/Switzerland/UK/US
      treaties flagged)
- [x] Costa Rica - Residency (183-day test), CFC (confirmed: NONE), Thin
      Cap (confirmed: NONE), Treaty Network (~5 countries, 2023 reform
      added multinational-group passive-income exception to
      territoriality, no US treaty)

## Core Latin America complete (Chile, Colombia, Peru, Uruguay, Ecuador,
## Panama, Paraguay, Bolivia, Costa Rica all done)

- [ ] Next: Venezuela, Caribbean nations, then Middle East (Qatar,
      Kuwait, Jordan, Oman, Bahrain) - continuing
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
