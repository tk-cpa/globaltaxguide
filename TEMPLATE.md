# GlobalTaxGuide.com — Canonical Country Page Template (v1)

Locked August 8, 2026. Every country/territory page must conform to this exact
structure. This supersedes all prior ad-hoc formats. Fixing a page to match
this template is a required step whenever that page is touched for any
reason - not just for pages flagged in a dedicated sweep.

## Required section order and EXACT heading text (no local-name variants in headings)

1. <h2>Corporate Tax Rate</h2>
2. <h2>Personal Tax Rate</h2>
3. <h2>VAT / GST Rate</h2>
4. <h2>Residency</h2>
5. <h2>CFC (Controlled Foreign Company) Rules: Yes</h2>  -- or --  <h2>CFC (Controlled Foreign Company) Rules: No</h2>
   - No other verdict strings permitted in the heading itself ("Not identified," "Not applicable," "Varies," partial-credit phrasings, etc.)
   - If the true answer is genuinely nuanced (e.g. Puerto Rico's "No locally / Yes federal overlay", Lesotho's "no classic CFC but a specific anti-avoidance provision"), the heading is STILL exactly "Yes" or "No" (pick whichever is closer to the real-world practical answer for a resident structuring a foreign holding), and the nuance goes ENTIRELY into the prose paragraph beneath it.
   - Local regime names (Section 9D, FAPI, NOKUS, Hinzurechnungsbesteuerung, REFIPRES, Transparencia Fiscal Internacional, Subpart F, etc.) belong in the first sentence of the prose, never in the heading.
6. <h2>Thin Capitalization</h2>
   - Local regime names (Zinsschranke, earnings stripping, etc.) go in prose, not the heading. Heading is always exactly "Thin Capitalization" even if the mechanism is technically an earnings-stripping or interest-limitation rule rather than a classic debt/equity ratio - the prose explains the actual mechanism.
7. <h2>Foreign Bank Account / Foreign Financial Asset Reporting</h2>
   - MANDATORY on every page, no exceptions. Currently missing from 105/229 pages - this is the top backfill priority.
8. <h2>Treaty Network</h2>

Optional additional sections (only when genuinely warranted by the country's
own facts - do not add filler): "Political and Economic Status" (for
disputed/limited-recognition territories only), country-specific notes.

## Minimum content standard per section

**Corporate Tax Rate**: headline rate + basis (worldwide vs. territorial) +
any standard reduced-rate tier (small business, sector-specific, SEZ) if one
exists. A bare percentage with zero context is NOT sufficient once a page is
touched.

**Personal Tax Rate**: flat-vs-progressive designation is MANDATORY. If
progressive, state at minimum the top bracket threshold and top rate. If the
top rate is income-type-specific (e.g. applies only to wages, or only to
investment income), that must be stated explicitly - do not let a bare "top
rate: X%" imply a single flat rate if the truth is a bracket structure.

**VAT / GST Rate**: headline rate + confirmation of whether reduced/zero
rates exist for defined categories (food, medicine, exports, etc.) - full
enumeration of every reduced-rate category is not required, but the
existence of a multi-tier system must be flagged if one exists so the
headline rate isn't read as universal.

**Residency**: the actual day-count or facts-and-circumstances test for
individuals; the actual incorporation/management test for entities. A vague
restatement ("residency is determined by the applicable law") does not meet
the bar.

**CFC**: per heading rules above. Prose must state the actual mechanism
(ownership threshold, passive-income test, substance carve-out, etc.) when
the answer is Yes; when No, prose should note if this differs from what a
parent/neighbor jurisdiction has (avoiding the "assumed inherited regime"
error already caught and fixed multiple times this session - Faroe
Islands/Denmark, Saint Barthelemy/France, Sint Maarten/Netherlands, Falkland
Islands/UK).

**Thin Capitalization**: state the actual mechanism - debt/equity ratio with
the specific ratio, OR earnings-stripping/EBITDA-percentage rule with the
specific percentage, OR genuine absence. "No statutory ratio" is an
acceptable and sufficient finding IF it reflects an actual review of the
governing tax code/law, not a search-effort shortfall.

**Foreign Bank Account / Foreign Financial Asset Reporting**: (1) whether a
domestic FBAR/foreign-asset-reporting equivalent exists for residents of
that jurisdiction; (2) FATCA/CRS participation status; (3) the standard
boilerplate reminder that US persons remain independently subject to FinCEN
Form 114 (FBAR) and potentially Form 8938 regardless of the local
jurisdiction's own rules. This third element can be a shared boilerplate
sentence, but elements (1) and (2) must be genuinely researched per country,
not copy-pasted.

**Treaty Network**: exact current treaty count if known + explicit statement
of whether a US treaty exists + the largest few economically-significant
named partners (roughly 5-10, more only for small/simple networks) + a
direct link to the jurisdiction's own official treaty list where one exists.
For networks of ~15 or fewer treaties, name every partner - low maintenance
cost, high value at that scale. Never present a vague "approximately N
treaties" as the entire answer without at least the US-treaty-status
confirmation, since that is the single highest-value fact for this
practice's client base.

## Prohibited (unchanged from MAINTENANCE.md, restated here for visibility)
- No hedge phrases describing the research process ("not confirmed this
  session," "no English-language sources," "not independently verified,"
  etc.) as a substitute for actually finding the answer.
- No em-dashes.
- No forbidden strings (license numbers, PTIN, last name).

## Rollout plan (in priority order)
1. Fix the one remaining page with the raw legacy combined heading
   (Northern Cyprus) - converts it to the full 8-section structure.
2. Backfill the Foreign Bank Account / Foreign Financial Asset Reporting
   section on the 105 pages currently missing it entirely. Highest-volume,
   most mechanical of the remaining work - most of these need only items
   (1) and (2) above researched, since item (3) is shared boilerplate.
3. Reformat all bare "CFC Rules" headings (97 pages) and "Not identified"
   headings (33 pages, ~30 of which need genuine primary-law research, ~3
   just need reformatting since they already have a real substantive
   answer) to the Yes/No standard.
4. Add the 20 confirmed-missing jurisdictions as new pages built to this
   template from the start.
5. Apply the Personal Tax Rate and Treaty Network minimum-content standards
   sitewide - lower priority, since these are enhancement passes on pages
   that otherwise already function, versus items 1-4 which are structural
   gaps or outright missing content.


## CFC section: no generic "other countries have their own rules" filler

A recurring bad pattern: adding a caveat like "this doesn't override CFC
rules that may exist in a beneficial owner's home jurisdiction (e.g., US
Subpart F/GILTI)" to a CFC section, as a supposedly helpful disclaimer.
DO NOT do this by default. It is an obvious universal truth that applies to
literally every country on Earth - every sovereign's own tax laws remain
unaffected by any other country's absence of a CFC regime, everywhere,
always. Stating it explicitly, especially with an arbitrarily-chosen example
country, adds zero information and reads as random filler.

**The only legitimate case for this kind of caveat**: the jurisdiction is a
dependency, collectivity, or constituent country of one SPECIFIC named
sovereign state, where a reader could plausibly and reasonably assume the
territory automatically inherited that specific parent's CFC regime, given
the real constitutional/administrative relationship. Examples where this is
genuinely warranted: Faroe Islands (autonomous, but part of the Kingdom of
Denmark - reader might assume Danish CFC rules apply), Saint Barthelemy and
Saint-Martin (French collectivities - reader might assume French CFC rules
apply), Falkland Islands and Isle of Man (UK-connected - reader might assume
UK CFC rules apply). In these cases, name ONLY the actual specific parent
country - never a generic or arbitrary example unrelated to that
jurisdiction's real political status.

Do NOT add this caveat to a jurisdiction with no such specific relationship
(e.g., Cook Islands, Andorra, Armenia - self-governing/independent states
with no single obviously-assumed "parent" whose rules a reader would
mistakenly think apply). For these, state the CFC finding plainly and stop.

Puerto Rico and Bermuda are different again - not a caveat, but the actual
substantive answer (PR's CFC exposure IS a matter of US federal law; Bermuda
has a real statutory provision in its own CIT Act addressing double-counting
with foreign CFC regimes). Keep this kind of content when it is the genuine
core answer to the "does CFC apply" question, not a bolted-on disclaimer.


## CFC section: MUST specify who the regime applies to (individuals, corporations, or both)

Flagged directly by the user on Peru's page - a CFC verdict that just says "a
Peruvian resident" without stating whether that means individuals,
corporate entities, or both is genuinely ambiguous and not an acceptable
final state. This is likely a widespread gap, not isolated to Peru.

**Mandatory going forward**: every CFC section stating "Yes" (a real regime
exists) must explicitly state whether the regime reaches:
- Individuals only (natural persons)
- Corporate/legal entities only
- Both (most common - state this explicitly rather than leaving it
  ambiguous via a generic "resident" or "taxpayer" reference)

Do not rely on words like "resident," "taxpayer," or "person" alone to imply
scope - these are frequently ambiguous in translation from the primary
source and readers should not have to guess. If the primary source itself
doesn't clearly resolve this, say so explicitly rather than defaulting to
an unstated assumption.

This same specificity requirement extends to other sections that use
similarly vague scope language - Thin Capitalization (does the rule apply
to companies only, or also to individual/entrepreneur borrowers?), Foreign
Bank Account Reporting (individuals only, or entities too?), and Residency
(the two tests - individual and corporate - must each be stated separately
and not conflated).


## NEW STANDARD - Official Tax Authority link per country (added per user request)

Every country page should include the name and official website of that
country's main tax authority (or authorities, where there are separate
bodies for direct vs. indirect tax) - e.g. IRS for the US, CRA for Canada,
HMRC for the UK. This is separate from the "Sources" citation list (which
covers secondary compilations like PwC/EY/BDO) - the tax authority link is
the actual government body a reader would contact or file with.

**Placement**: a new line at the top of the source-row, before "Sources:",
formatted as:
`Official tax authority: [Full Name] ([acronym if applicable]) - [domain,
not full URL, to keep it scannable]`

Example (United States):
`Official tax authority: Internal Revenue Service (IRS) - irs.gov`

Where a country has genuinely separate authorities for direct and indirect
tax (e.g., a country with a separate customs/VAT authority), name both.
Only include authorities that are real and independently confirmed - do not
guess a plausible-sounding name/acronym.

This is a large rollout across all 229 country pages - being done in
batches, prioritizing major/well-documented economies first where the
correct authority name is easy to confirm with high confidence, then
working through the rest.


## POLICY REVERSAL #1 - CFC heading format (per direct user correction)

The earlier "Yes"/"No" in the heading itself is REVOKED. User does not want
verdicts baked into section titles. New standard:

Heading is always exactly: `<h2>CFC (Controlled Foreign Company) Rules</h2>`
- no "Yes", no "No", no verdict of any kind in the heading text.

The actual finding goes in the FIRST SENTENCE of the prose immediately
below, stated plainly: "[Country] has no CFC regime." or "[Country] has the
following CFC regime: [description]." Do not bury the verdict later in the
paragraph - it should be the very first thing a reader sees under the
heading, just not in the heading itself.

## POLICY REVERSAL #2 - Foreign Bank Account / Foreign Financial Asset
## Reporting section (per direct user correction)

The earlier policy ("only include this section if a genuine domestic
regime exists, omit entirely otherwise") is REVOKED. New standard:

**This section is MANDATORY on every single country page, with no
exceptions.** If a genuine domestic regime exists, describe it in full
(threshold, filing body, penalties, primary source). If no such regime
exists, the section still appears, with a plain, direct statement: "No
foreign bank account or foreign financial asset reporting regime exists in
[Country]." Do not omit the section either way - the point is 100%
structural consistency across every page, not selectively hiding a
"boring" answer.

This does NOT reverse the OTHER part of the earlier FBAR correction: this
section must still never contain US-specific content (FinCEN Form 114,
Form 8938, "US citizens must file...") on any non-US country's page. That
part of the earlier fix stands. What's reversed is only the
include/omit-the-whole-section decision - the section itself is now always
present, the US-boilerplate ban within it remains in force.

**Newly confirmed additional genuine domestic regimes** (missed in the
original sweep, found via direct user tip-off): Kazakhstan (National Bank
of Kazakhstan account-registration and quarterly reporting requirement
under the Law "On Currency Regulation and Currency Control" - a resident
opening a foreign bank account must obtain an account number from the NBK
and, for legal entities, file quarterly reports). This is now the 12th
country with a genuine regime. Given this was missed despite an earlier
supposedly-thorough sweep, treat the current 12-country "genuine regime"
list as provisional, not exhaustive - a fresh per-country check is
warranted rather than assuming the existing list is complete.

## Lesson logged: writing clarity self-check

User caught a real, embarrassing bug: Afghanistan's CFC section, as
originally written, read (on a plain reading) as if claiming ALL foreign
companies worldwide are taxed by Afghanistan - a sentence that was
technically defensible if parsed very carefully but genuinely confusing on
a normal read. Going forward: after drafting any prose sentence involving
"foreign companies" or similar broad-sounding phrases, re-read it as a
first-time reader would, not as the person who already knows what it's
supposed to mean. If a sentence could be misread as a universal claim,
rewrite it to be unambiguous, even at the cost of being slightly longer.


## NEW SECTION - Tax System Basis (added per direct user request)

New mandatory section, placed FIRST in the country body (before Corporate
Tax Rate), since it's the foundational fact everything else depends on.

Heading: exactly `<h2>Tax System</h2>`

Content must cover TWO distinct things in the same section:

1. **Basis of taxation**: territorial (only local-source income taxed),
   worldwide (residents taxed on all income regardless of source), or
   citizenship-based (the rare case - currently only the US and Eritrea
   confirmed - where citizenship alone, not residence, creates a tax
   filing obligation). State this plainly as the first sentence. Many
   countries are genuinely hybrid (e.g., worldwide for residents,
   territorial for non-residents) - say so rather than forcing a single
   label where the reality is mixed.

2. **Assessment mechanism**: how the tax actually gets collected and
   finalized. DO NOT force a false binary ("self-assessment" vs
   "administrative assessment") - most real systems are a genuine mix of:
   - Withholding at source (employer withholding on wages, bank withholding
     on interest, etc.)
   - Taxpayer self-filing (a return the taxpayer prepares and submits)
   - Authority-issued assessment notice (a formal document from the tax
     authority - Steuerbescheid in Germany, avis d'imposition in France,
     Notice of Assessment in Canada/Australia - confirming or adjusting
     the taxpayer's own calculation)
   Describe the ACTUAL mechanism for that specific country - which of
   these elements exist, and how they combine - rather than picking one
   label. This is a genuinely new research item per country, not just
   restating existing content, and should be sourced properly like any
   other fact on the page.

This section should be BRIEF - 2-4 sentences covering both points. It is
context-setting for everything that follows, not a full treatise.

## Section order updated

Tax System now comes FIRST: Tax System / Corporate Tax Rate / Personal Tax
Rate / VAT-GST Rate / Residency / CFC / Thin Capitalization / Foreign
Bank Account Reporting / Treaty Network. (9 body sections, plus Official
Tax Authority in the source-row, for 10 total data points - hero stat on
index.html should be updated again once this rollout is complete.)


## TWO NEW SECTIONS + FINAL SECTION ORDER (per user request)

### Tax Year & Key Deadlines (new, placed 2nd - right after Tax System)

Heading: exactly `<h2>Tax Year & Key Deadlines</h2>`

Content: (1) the tax year itself - calendar year is the global default, but
flag genuine exceptions clearly (e.g. UK 6 April-5 April, Japan 1 April-31
March for corporate, Australia 1 July-30 June); (2) 2-4 genuinely key dates
- the main individual filing/payment deadline, any extended deadline if
one commonly exists, and the main corporate filing deadline if materially
different from the individual one. This is NOT a full tax calendar -
resist the urge to list every provisional-payment date. If a fact doesn't
help someone plan around it in a five-second scan, leave it out.

### Foreign Tax Credit (new, placed 10th - immediately before Treaty
### Network, since both are double-tax relief mechanisms)

Heading: exactly `<h2>Foreign Tax Credit</h2>`

Content must state: (1) whether a foreign tax credit regime exists at all;
(2) if yes, whether it's available to individuals, corporations, or both -
this is the same individual/corporate scope-clarity standard already
mandatory for CFC sections, applied here too; (3) the basic mechanism in
one or two sentences (ordinary credit capped at domestic tax on the same
income vs. full/exemption method vs. no credit at all); (4) if a specific,
well-known form exists for claiming it (e.g., US Form 1116 for individuals
/ Form 1118 for corporations), name it briefly - this does not need to
become a forms-and-instructions guide, one clause is enough.

### FINAL section order, updated

1. Tax System
2. Tax Year & Key Deadlines
3. Corporate Tax Rate
4. Personal Tax Rate
5. VAT / GST Rate
6. Residency
7. CFC (Controlled Foreign Company) Rules
8. Thin Capitalization
9. Foreign Bank Account / Foreign Financial Asset Reporting
10. Foreign Tax Credit
11. Treaty Network
(Official Tax Authority remains in the source-row, not a body section)

11 body sections + 1 source-row item = 12 total data points per page once
both new sections are rolled out. Hero stat and homepage explainer grid
will need a further update once rollout is substantially complete.


## THREE MORE NEW SECTIONS + updated final order (per user request)

### Permanent Establishment (new - split out from Residency)

Heading: exactly `<h2>Permanent Establishment</h2>`

Content: what specifically triggers a taxable corporate presence for a
non-resident entity - fixed place of business, dependent agent PE,
construction/service PE day-count thresholds, and any digital/significant-
economic-presence rules. This is a CORPORATE question, distinct from
individual Residency, and was previously often buried or absent - now gets
its own section.

### Hybrid Entity / Anti-Hybrid Rules (new)

Heading: exactly `<h2>Hybrid Entity Rules</h2>`

Content: (1) how the jurisdiction classifies foreign entities for tax
purposes (does it have a "check-the-box"-style elective system like the
US, or fixed classification by entity type?); (2) whether the jurisdiction
has enacted ATAD2-style anti-hybrid rules denying deductions or requiring
inclusion where a hybrid mismatch would otherwise produce a double
deduction or deduction-without-inclusion outcome; (3) brief note on how
the jurisdiction's own domestic entities (e.g., US LLCs, UK LPs) are
commonly used or treated in cross-border structuring, where genuinely
relevant and well-documented - not speculative.

### Participation Exemption / Dividend Exemption Regime (new)

Heading: exactly `<h2>Participation Exemption</h2>`

Content: whether a participation exemption exists for qualifying
dividends and/or capital gains from a subsidiary, the minimum ownership
threshold and holding period required to qualify, and any subject-to-tax
or anti-abuse conditions attached (a common feature - many participation
exemptions are conditioned on the underlying subsidiary being subject to
a minimum level of tax abroad, to prevent stacking with the CFC section's
own coverage of low-tax entities).

## FINAL section order (locked)

1. Tax System
2. Tax Year & Key Deadlines
3. Corporate Tax Rate
4. Personal Tax Rate
5. VAT / GST Rate
6. Residency
7. Permanent Establishment
8. CFC (Controlled Foreign Company) Rules
9. Thin Capitalization
10. Hybrid Entity Rules
11. Foreign Bank Account / Foreign Financial Asset Reporting
12. Participation Exemption
13. Foreign Tax Credit
14. Treaty Network

14 body sections + Official Tax Authority in source-row = 15 total data
points once fully rolled out. Hero stat and homepage explainer grid need
another update pass once this is substantially complete - do not update
prematurely while most pages still show the old, smaller count.


## *** CRITICAL STYLE RULE - NO INLINE SOURCE ATTRIBUTION IN BODY PROSE ***
## (per direct, strongly-worded user correction)

BANNED PATTERNS in body prose, effective immediately, retroactively being
removed sitewide:
- "Confirmed via [source]:"
- "Confirmed directly via [source]:"
- "confirmed via a specialist [x] source"
- "per [source]"
- Any inline phrase in the body text that names where a fact came from or
  vouches for the source's credibility

WHY: This site IS the trusted source. Citations belong in ONE place - the
source-row at the bottom of each page, where they already exist. Repeating
"confirmed via X" in every paragraph is not rigor, it's noise - it reads
as if the page itself doesn't trust its own facts and needs to keep
proving its homework sentence by sentence. State facts directly and
plainly, the way an authoritative reference does. The verification still
happens - it just doesn't need to be narrated in the prose.

CORRECT: "Curacao's corporate profit tax is 22%, with a reduced ~2-3%
effective rate for qualifying e-zone companies."

WRONG: "Confirmed via a specialist Curacao tax source: the corporate
profit tax is 22%, with a reduced effective rate of approximately 2-3%
for qualifying e-zone companies."

This applies to ALL body sections (Tax System, Corporate/Personal/VAT,
Residency, PE, CFC, Thin Cap, Hybrid Entity, FBAR, Participation
Exemption, FTC, Treaty Network) - write every fact as a direct, plain
statement. Genuine uncertainty or a real source conflict can still be
flagged plainly ("sources conflict on X" or "confirm current figure
directly") - that's different from narrating routine verification.


## CLEANUP COMPLETE (sitewide) - verified, not just claimed

Per direct user correction (screenshot showing the pattern in the wild),
executed a full sitewide removal of inline source-attribution phrasing
("Confirmed via X", "confirmed directly via X", "Per PwC") from body
prose across all 249 pages. This required THREE passes because the first
two regex attempts had real bugs (caught via testing, not shipped blind):
1. First regex broke grammar on abbreviations like "U.S.C." by treating
   internal periods as sentence boundaries - caught in testing, redesigned.
2. Second regex missed dash-prefixed and parenthetical variants - caught
   via post-deployment verification, added.
3. Remaining ~20 mid-sentence "verb-phrase" cases (structurally different,
   "confirmed via" acting as the sentence's main verb) were fixed by hand,
   one at a time, to guarantee correct grammar rather than risk further
   regex corruption.

Also fixed in the same pass, discovered while investigating the
attribution issue:
- Missing "%" signs on rate figures (a genuine factual error, e.g. "rate
  is 25." instead of "rate is 25%.") - affected dozens of pages,
  concentrated in an earlier bulk-generation batch. Fixed via a
  callback-based regex that checks for already-present "%" before
  inserting (caught and fixed a backtracking bug that corrupted
  "23.87%" into "23%.87%" before deployment).
- Generic unfilled boilerplate sentence ("Registration thresholds,
  zero-rated and exempt categories... see the source link below for the
  full detail on this jurisdiction") - a placeholder that added no real
  value - removed sitewide, two phrasing variants.
- Cross-page self-reference noise ("as already described elsewhere on
  this page", "(see France's own page on this site)") - removed.
- A handful of pre-existing capitalization bugs (lowercase "the" starting
  a sentence after a period) - fixed as found, unrelated to the main
  cleanup but caught during verification.

**Final verified state (re-checked directly, not assumed): 0 pages with
body-prose "confirmed via" language, 0 pages with the boilerplate
sentence, 0 pages with genuinely missing % signs (range-aware check).**

## POLICY LOCKED IN: no inline source attribution, ever, going forward

This is not just a retroactive cleanup - it is now the permanent writing
standard for every future page and edit. State facts directly. Citations
live only in the source-row. No "confirmed via", no "per X", no narrating
which source said what mid-paragraph.
