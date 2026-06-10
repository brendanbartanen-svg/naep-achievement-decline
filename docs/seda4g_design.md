# Design scoping: 4G/LTE rollout × SEDA test scores (free data only)

Scoped 2026-06-10 (agent-verified: sample files downloaded, schemas inspected,
FCC report statistics read from the PDFs). Status: **GO, conditionally** — feasible
with 100% free data, but NOT with FCC Form 477 alone.

**UPDATE 2026-06-10, validation exercise complete: QUALIFIED PASS.** Pipeline in
`seda4g/` (01_download.sh, 02_build_exposure.py, 03_validate.py); county×wave panel
in `seda4g/exposure_county_panel.csv` (national 3,234 counties × 7 waves from NBM
Analyze Tables + 8-state block-level builds); all numbers in
`seda4g/validation_results.json`. Key results: (a) trajectory matches FCC benchmarks
(t7 share 57.9% Jun-11 → 90.4% Dec-12 → 98.2% Jun-14; FCC's 85.6% Oct-12 interpolates
exactly); (b) Verizon Dec-2010 launch metros visible (Dallas .93, Seattle .97 vs
non-launch mean .14–.16; rural RUCC-8/9 = 0.0); (c) rural lag confirmed —
Spearman(RUCC, rollout wave)=0.61, metro crosses 50% ≈late-2011 vs nonmetro
≈early-2013; (d) Form 477 Dec-2015 splice: 477 ≥ SBDD in 93–100% of counties,
Spearman .63–.70 where variance remains. The <2-sq-mi large-block problem does NOT
apply to wireless (coverage of state pop ≥95.7% every wave; corr 0.994 vs NTIA's own
overlays). TWO CAVEATS: (1) Analyze-Table speed-tier columns include FIXED wireless
(WISP leakage 2.5pp pop-weighted at Dec-2012, county p90 = 20pp) — primary exposure
must be built from state Wireless CSVs (`transtech==80`) for all 9 waves × 51 states
(~10–15GB, few hours; pipeline already does it for 8 states); Analyze Tables are for
validation only. (2) Grantee speed-coding heterogeneity in early waves (MA/DE coded
LTE tier 7; TX/WA tier 6; CO invisible until Dec-2011; CO/MO artifacts Jun-2011) —
mandatory tier≥6/tier-7/Verizon-only robustness codings + state FE. Also note
2010-wave files use 2000-census blocks (2000 PL94-171 weights), naming scheme
`SBDD_XX_Fall2010.zip`, some zips need Deflate64 handling. SEDA county long 5.0
downloads directly with no registration:
`https://stacks.stanford.edu/file/druid:cs829jn7849/seda_county_long_cs_5.0.csv`
(354,949 rows, 3,104 counties, 2009–2019); local district-level copy + crosswalk
per `seda4g/SEDA_LOCAL_COPY.md`. Companion literature context
in `evidence/fertility_parallel.md`. As of June 2026 nobody has run mobile-rollout
variation against US test scores (adjacent work: fertility — Myers & Hooper w35310,
Hudson & Moscoso Boedo; phone bans — Figlio & Özek w34388, Dee w35132; cross-country
3G×PISA — Jain & Stemper; fiber × NC scores). Topicality risk: others are likely
circling; move fast.

## The identification problem with Form 477 alone

Any-LTE population coverage (FCC Mobile Competition Reports 16/17/19, verified):
0% (mid-2010) → 85.6% (Oct 2012, Mosaik) → 98.5% (Jan 2014) → 99.7% (Dec 2015,
Form 477). The first FREE Form 477 mobile vintage is **Dec 2014** (shapefile only;
block CSVs from Dec 2015) — i.e., after the extensive margin is gone. Remaining
477-era variation is the number-of-LTE-providers margin (4+ providers: rural 55.8%
vs non-rural 96.4% of pop, Dec 2015) — usable for "depth" designs but endogenous to
demand and not the saturation wave.

## The rescue: NTIA SBDD / National Broadband Map archive (free, alive, no login)

https://www2.ntia.gov/broadband-data — semiannual **census-block × provider** files,
**9 waves Jun 2010 → Jun 2014**, exactly the 0%→95% LTE rollout window. Separate
Wireless CSV per state (e.g. `/files/broadband-data/DE-NBM-CSV-Dec-2013.zip`;
national zip ~1.7GB/wave; per-state files small). Schema: FRN, provider, 15-digit
block FIPS, `transtech` (80 = terrestrial mobile wireless), `maxaddown` speed tier,
spectrum, `pct_blk_in_shape`.

**4G proxy:** `transtech==80 & maxaddown>=7` (10–25 Mbps advertised). Verified
against ground truth: in Dec 2010 Delaware the only tier-7 mobile provider is
Verizon (LTE launched that month); by Dec 2013 all four nationals, tier-7 rows
5,760 → 75,998. Also check `All-NBM-Analyze-Table-*.zip` (likely pre-built
geographic summaries — could skip block-level processing entirely).

Caveats: tier-7 can capture WiMAX/Clearwire and T-Mobile HSPA+ ("4G" marketing) —
run tier≥6/tier≥7/provider-specific codings; advertised ≠ experienced coverage
(rural overstatement, non-classical error); state-grantee quality varies;
**measurement splice at 2014/2015** when switching SBDD → Form 477 (477 has explicit
LTE tech codes, SBDD doesn't) — use source×period FE, or SBDD-only for timing and
477 only to extend the post period.

## Data inventory (all free)

| Ingredient | Source | Notes |
|---|---|---|
| Mobile coverage 2010–2014 | NTIA SBDD block×provider CSVs, 9 waves | the identifying variation |
| Mobile coverage 2014–2021 | FCC Form 477 mobile (fcc.gov/mobile-deployment-form-477-data; files on us-fcc.box.com — fcc.gov blocks scripted access intermittently) | Dec 2014 shapefile-only; block CSVs (centroid + actual-area) Dec 2015+ |
| County mobile summaries | DO NOT EXIST from FCC (Area API = fixed only) | aggregate blocks yourself with block pop weights |
| Outcomes | SEDA 5.0 (Mar 2024): SY 2008-09–2018-19, grades 3–8, math+RLA; school/district/**county**/CZ/state; CS scale | edopportunity.org downloads, free registration; SEDA2023 supplement adds 2019/22/23 districts |
| Smartphone adoption checks | NTIA Internet Use Survey (Jul 2011/2013/2015…, state microdata); ACS S2801 (2016+, county) | first-stage / mechanism |
| Ruggedness IV | USDA ERS Area & Road Ruggedness Scales (county CSV) — Nunn-Puga is country-level only | |
| Lightning IV | NASA LIS/OTD climatology, 0.5° grid, GHRC DAAC (free Earthdata login) | |

## Minimal viable design

- **Exposure:** county (and geodist) pop share in blocks with ≥1 high-speed mobile
  provider, semiannual 2010–2014 (SBDD) extended 2015–2019 (477 LTE codes).
  Treatment date = first wave share crosses 50% (robustness 25/75%, continuous dose).
- **Outcome:** SEDA 5.0 county/geodist long, CS scale, math & RLA, 2009–2019.
  Exploit grade×cohort exposure: a county treated 2012 exposes its 2019 G8 cohort
  for 7 adolescent years but its 2013 G8 cohort for 1 — within-county across-grade
  gradients absorb county×year shocks (second identification margin).
- **Estimator:** Callaway–Sant'Anna / Sun-Abraham event study, never/late-treated
  controls; county + grade×year×subject FE; state×year (or CZ) FE.
- **IV for the dose design:** ruggedness and lightning × national 4G adoption trend
  (Bartik-style), mirroring Hudson & Moscoso Boedo (their first-stage F≈82 on the
  same county 4G measure).
- **Pre-period:** SEDA starts 2008-09 → 2–3 pre years for early-treated metros
  (thin), 4–5 for late-treated.

## Threats (in order)

1. **Exclusion of ruggedness** — rurality correlates with achievement trends
   (the Reason critique of the fertility papers). Pre-empt: 2009–2011 placebo
   trends, rich rural-trend controls.
2. **Common Core / assessment transitions land on the treatment window
   (2012–2015).** State×year FE essential — which shrinks identifying variation to
   within-state rollout timing (real, via the rural lag, but smaller).
3. **Fixed broadband co-moves** — control using SBDD fixed-tech files.
4. Coverage overstatement + the 2014/15 splice (above).
5. **Anticipation via 3G smartphones** (iPhone on 3G from 2008) — control with
   SBDD lower-tier 3G coverage.

## Binding constraints / first steps if pursued

1. **Validation exercise first** (design lives or dies here): SBDD Jun-2014 vs
   Form 477 Dec-2014 overlay; county high-speed shares vs FCC-published aggregates.
2. Build the county×wave exposure panel from the 9 SBDD waves (start with the
   Analyze-Table zips; fall back to state Wireless CSVs).
3. Register for SEDA 5.0, pull county long file + covariates + crosswalks.
4. Decision point after validation: if SBDD tier-coding validates, proceed to
   event study; if not, the free path fails and the design needs licensed
   Mosaik/Collins Bartholomew coverage.
