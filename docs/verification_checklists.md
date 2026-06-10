# Human verification checklists

*Built 2026-06-10 as part of the verification package (see also `evidence/claims_audit.md`
and `python3 checks.py`). Two checklists: (A) spot-check the hand-coded policy/treatment
CSVs against their sources; (B) pull five headline numbers yourself from the NAEP Data
Explorer. Estimated total time: ~35 min for A, ~15 min for B.*

---

## A. Hand-coded data spot-check (~2 min per row)

Rows below were drawn with `pandas.DataFrame.sample(n, random_state=42)` from each CSV
(reproduce with the same call). For each row: confirm the coded value against the listed
source. Where the repo records no URL for that specific row, the row says
**no recorded source — flag**: verify it from the general source named in the report
footnote and, if it cannot be found in ~2 minutes, flag the row for re-coding.

### A1. `data/waivers.csv` (ESEA/NCLB waiver approval dates) — 9 rows

General sources recorded in report.tex (fn. 3) and README: ED's per-state ESEA flexibility
pages, CRS Report R42328, EdWeek state-by-state tracking. No per-row URL is recorded in the
repo, so each row below inherits **no recorded per-row source — verify against ED/CRS/EdWeek
and flag if not found**. Practical path: search `ed.gov ESEA flexibility "<state>" approval`
or check CRS R42328's approval-date table (Table 1).

| state | approval | group | notes in CSV | check |
|---|---|---|---|---|
| AR | 2012-06 | early | — | ☐ approval month = June 2012? |
| ID | 2012-10 | early | approval letter Oct 17 2012 | ☐ letter dated Oct 17, 2012? |
| KY | 2012-02 | early | first round | ☐ among the first 10/11 approved Feb 2012? |
| MS | 2012-07 | early | — | ☐ approved July 2012? |
| NM | 2012-02 | early | approved Feb 15 2012 | ☐ Feb 15, 2012 (NM was approved days after the Feb 9 first round)? |
| NY | 2012-05 | early | — | ☐ approved May 2012? |
| SC | 2012-07 | early | — | ☐ approved July 2012? |
| TX | 2013-09 | late | — | ☐ approved Sept 2013 (late wave)? |
| VA | 2012-06 | early | — | ☐ approved June 2012? |

Analysis-critical extra checks (not sampled but load-bearing for the design):
☐ the seven never-waiver states are CA, IA, MT, NE, ND, VT, WY (report §7.3);
☐ WA coded `revoked` (Apr 2014) and dropped after 2013.

### A2. `data/phonebans.csv` (state phone-ban coding for the NAEP-2026 design) — 9 rows

No URLs recorded anywhere in the repo for this file (the `instrument` column carries the
bill/EO number, which is the verification handle). STATE.md marks the coding "agent-verified
June 2026; re-verify IL signature and CO/MD dates at analysis time". Every row is therefore
**no recorded source — verify by searching the named instrument** (e.g. legiscan.com or the
state legislature site for "`<state> <bill number>` phone").

| state | type_2025_26 | instrument | enacted | first_sy_effect | exposure group | check |
|---|---|---|---|---|---|---|
| AR | BTB | SB142 Act 122 | 2025-02 | 2025-26 | short | ☐ bell-to-bell, signed Feb 2025, effective 2025-26? |
| ID | DISTRICT | EO 2024-11 + SB1032 | 2024-10 | 2025-26 | minimal | ☐ district-policy mandate, policies due Dec 31, 2025? |
| KY | INSTR | HB208 | 2025 | 2025-26 | short | ☐ instructional-time ban from 2025-26? |
| MS | none | — | — | — | untreated | ☐ no statewide ban as of 2025-26? |
| NM | DISTRICT | SB11 | 2025 | 2025-26 | short | ☐ district-policy requirement effective 2025-26? |
| NY | BTB | FY2026 budget | 2025-05 | 2025-26 | short | ☐ bell-to-bell via FY2026 budget, effective 2025-26? |
| SC | BTB | Proviso 1.103 + SBOE model policy | 2024-07 | 2024-25 | medium | ☐ effective 2024-25, statewide from Jan 2025 (mid-year flag)? |
| TX | BTB | HB1481 | 2025-06 | 2025-26 | short | ☐ signed June 2025, effective 2025-26? |
| VA | DISTRICT_EO_then_BTB | EO33 2024; HB1961/SB738 2025 | 2024-07 | 2024-25 | medium | ☐ EO33 July 2024 with policies from Jan 2025, then statute 2025? |

### A3. `data/commoncore.csv` (Common Core adoption/repeal status) — 8 rows

Source recorded in report.tex (fn. 4): **NCES State Education Reforms, Table 2.17**
("State adoption of the Common Core State Standards…"), cross-checked against
contemporaneous coverage; navigate from nces.ed.gov → Programs → State Education Reforms
(no deep URL recorded in the repo). Coding rule to keep in mind: post-2015 rebrands that
retained aligned content count as `adopted`.

| state | cc_status | repeal_year | notes in CSV | check |
|---|---|---|---|---|
| ID | adopted | — | replaced 2022 post-period | ☐ adopter; replacement postdates the 2013–19 window? |
| KY | adopted | — | revision 2017 | ☐ adopter (first state to adopt, 2010)? |
| MS | adopted | — | — | ☐ adopter? |
| NM | adopted | — | — | ☐ adopter? |
| NY | adopted | — | implementation backlash | ☐ adopter (backlash ≠ repeal)? |
| SC | adopted | 2014 | repeal 2014, new standards 2015-16 | ☐ formally repealed 2014? |
| TX | never | — | — | ☐ never adopted? |
| VA | never | — | — | ☐ never adopted? |

Analysis-critical extra check: ☐ never-adopters are exactly AK, NE, TX, VA, and
MN is `partial_ela_only` (math never adopted) — these drive the §7.4 test.

### A4. `data/tuda_csdh_match.csv` (TUDA district × CSDH 2020-21 virtual share) — 8 rows

Recorded source (data/external/SOURCES.md): COVID-19 School Data Hub district file
`District_Overall_Shares_03.08.23.csv` — local copy in `data/external/`, canonical download
https://assets.ctfassets.net/9fbw4onh0qc1/XfBEuMLMOBgHrhmjBdVpc/8e555b362876da16ba52c85be5b2effe/District_Overall_Shares_03.08.23.csv
(researcher page: https://www.covidschooldatahub.com/for_researchers). Fastest check:
`grep -i "<district>" data/external/District_Overall_Shares_03.08.23.csv` and compare the
share-virtual column; NYC is the mean of its 32 geographic districts (recompute or accept).

| jur | district (CSDH name) | share_virtual coded | check |
|---|---|---|---|
| XA | Atlanta Public Schools | 1.00 | ☐ |
| XB | Boston | 0.47 | ☐ |
| XI | Miami-Dade | 0.03 | ☐ |
| XJ | Jefferson County (KY) | 0.78 | ☐ |
| XL | Los Angeles Unified | 0.73 | ☐ |
| XN | NYC geographic districts (mean of 32) | 0.146 | ☐ recompute mean or flag for code review |
| XQ | Albuquerque Public Schools | 0.79 | ☐ |
| XY | Denver County 1 | 0.60 | ☐ |

---

## B. NAEP Data Explorer 15-minute check — five headline numbers

Pull each number yourself from nationsreportcard.gov. Two routes work; instructions use the
faster report/trend pages where possible and the Data Explorer (NDE) where needed.
NDE: https://www.nationsreportcard.gov/ndecore/landing → "Main NDE".

**B1. Grade 8 reading 2024 national mean = 258 (lowest ever recorded).**
Go to https://www.nationsreportcard.gov/reports/reading/2024/g8/national-trends/.
Read the 2024 average scale score (258) and scan the trend line back to 1992: no year is
lower. (NDE route: Reading → Grade 8 → jurisdiction National → All students → average scale
scores → select all years.) Matches report Table 1 and abstract.

**B2. Grade 8 math: 2013 = 285, 2019 = 282, 2022 = 274, 2024 = 274 (−10.8 total; pandemic window ≈ 71%).**
Same page for mathematics: https://www.nationsreportcard.gov/reports/mathematics/2024/g8/national-trends/.
Hover the trend chart at 2013/2019/2022/2024 (284.6 / 282.0 / 274.3 / 273.8 unrounded).
Check 2024 sits at roughly the 2000 level (273).

**B3. Bottom-decile collapse vs stable top, G8 math 2013→2019: P10 −6.6, P90 +2.7.**
NDE: Mathematics → Grade 8 → National → All students; under statistics options choose
**percentiles** (10th and 90th); select years 2013 and 2019. Compute the two differences:
P10 237.4→230.8 (−6.6), P90 330.6→333.3 (+2.7). This is the report's central
distributional fact (§4.3, Fig 3).

**B4. 90–10 gap at a record: G8 math gap 2013 = 93, 2024 = 109.**
Same NDE percentile query as B3 but add 2024: gap = P90 − P10 = 330.6 − 237.4 ≈ 93.2 in
2013 and 328.3 − 219.3 ≈ 108.9 in 2024 — and confirm 2024 is the largest gap of any year
you add to the query (2019 gives 102.5).

**B5. Catholic-school G8 reading fell ≈ −7.8 between 2013 and 2019 (the sector test).**
NDE: Reading → Grade 8 → National → cross-tab variable **school type** (public/private/
Catholic; "Type of school" under School Factors) → years 2013 and 2019 → average scale
scores. Catholic: ≈286.2 (2013) → ≈278.4 (2019), change −7.8 — at least as large as the
public-school change (−4.0). Matches §7.2 and `v11_results.json`.

*(Bonus, +3 min) B6. LTT age-13 math P10 fell 12.6 pts 2012→2020 while P90 was flat.*
https://www.nationsreportcard.gov/highlights/ltt/2023/ → age 13 mathematics percentile
section (P10 240 → 227 between 2012 and 2020; P90 unchanged). Cross-check the means against
Digest table 222.85: https://nces.ed.gov/programs/digest/d23/tables/dt23_222.85.asp.
This number is hand-compiled in this repo (see claims_audit.md, known gap #1), so the
external check matters more than usual.
