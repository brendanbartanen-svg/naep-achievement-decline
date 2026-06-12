# Project task log

Every discrete task that went into building this project, in roughly chronological
order, grouped by phase. Written June 10, 2026 (v1.8). "Pulled" = retrieved
programmatically; "hand-coded" = assembled by reading documents; papers listed were
actually read/consulted, not just cited.

## Phase 0 — Setup and data acquisition (v1.0)

- Probed the NCES NAEP Data Service API (`GetAdhocData.aspx`), discovered its
  undocumented failure modes by trial: pre-2003 years require sample-suffix codes
  (1990R2, 2000R3) or the server 400s/hangs; large requests hang silently; learned to
  chunk ~4 years × ~13 jurisdictions with 40-second timeouts.
- Wrote `naep_pull.py`: national means, percentiles (PC:P1/P2/P5/P7/P9 = 10/25/50/75/90),
  standard deviations, and subgroup breakdowns (race, sex, NSLP eligibility) for grades
  4/8, math and reading, 1990–2024; plus all-state mean panels → `data/naep_main.csv`
  (2,074 rows). Killed and rewrote the first version after a 25-minute hang
  (missing year suffixes); re-pulled math 2003–2007 separately after learning math was
  not assessed in 2002.
- Pulled NAEP Long-Term Trend (age 9/13/17) via the separate NRCDataService
  (Program=LTT, subscales RRPSCT/MRPSCT, cohort codes); hand-compiled `data/ltt.csv`
  means from Digest of Education Statistics tables 221.85/222.85 and cross-validated
  the two sources against each other (documented in `evidence/ltt_evidence.md`).
- Pulled the LTT student-survey reading-for-fun series (variable S003501) and the
  main-NAEP days-absent crosstab (variable B018101); debugged pandas silently
  converting the "None" absence category to NaN (`keep_default_na=False`).
- Gathered international series (PISA 2000–2022, TIMSS 2023 US highlights) and
  contextual facts (teen smartphone ownership from Pew 2013/2018; Common Sense census
  screen-time; school spending series; teacher-vacancy literature), each fact recorded
  with its source URL in `evidence/hypotheses_evidence.md`.

## Phase 1 — Core analysis and report (v1.0)

- Wrote `analyze.py`: trend decomposition around the 2013 peak, percentile divergence,
  90–10 gap series, within-subgroup declines, state scatter; produced most figures and
  `data/summary.json`.
- Wrote `analyze_ltt.py` and `analyze_intl.py` (LTT percentile divergence, reading-for-fun,
  PISA/TIMSS comparison figures).
- Formulated eight candidate hypotheses (pandemic, digital media, accountability
  retreat, funding cuts, demographics, absenteeism, reading practice, teachers/grade
  inflation) and derived testable predictions for each across timing, distribution,
  subgroups, geography, and international comparison.
- Read/consulted for the hypothesis tests: Goldhaber et al. 2023 and Jack et al. 2023
  (closure effects), Dee 2024 and CEA 2023 (absenteeism), Jackson et al. school-finance
  papers and Jackson–Wigger (funding), Leachman 2017, Dee–Jacob 2011 (NCLB effects),
  Haidt 2024, Twenge's descriptive work, OECD PISA Volumes I–II.
- Wrote the LaTeX report (16 pp at v1.0) and compiled with tectonic; built the
  hypothesis-scorecard table; established the two-phase framing.
- Moved the whole project out of the Overleaf folder into `~/Documents/CC Sandbox/`
  per project-hygiene decision; created the private GitHub repo; tagged v1.0 with a
  PDF release.

## Phase 2 — Discriminating tests (v1.1)

- Wrote `naep_pull_v11.py`: school-sector trends (public/private/Catholic via SCHTYPE)
  and the full state × year × percentile panel → `data/naep_v11.csv` (9,580 rows).
  Debugged: SCHTYP2 queries silently fail for 2019+ (private-school suppression kills
  the whole query) — switched to the SCHTYPE addendum variable.
- Hand-coded `data/waivers.csv`: every state's ESEA/NCLB waiver approval date and group
  (early/late/never/revoked) from ED approval letters, CRS reports, and EdWeek coverage.
- Wrote `analyze_cohort.py`: cohort-matched pseudo-growth decomposition
  (G8(t) − G4(t−4)), splitting every grade-8 change into entry and growth components.
- Wrote `analyze_v11.py`: public-vs-Catholic comparison and the staggered waiver
  event study / DiD on state P10 scores. Debugged a degenerate event-study plot
  (coefficients at 1e19): the full treatment×year interaction set is collinear with
  state fixed effects — rebuilt with manual event-time dummies omitting the base year.
- Updated the report to v1.1; tagged and released.

## Phase 3 — Mechanism checks (v1.2)

- Downloaded COVID-19 School Data Hub district schooling-mode shares
  (`District_Overall_Shares_03.08.23.csv`, 14,967 districts) and computed
  enrollment-weighted state shares; spot-validated against CSDH's own state pages.
- Extracted FutureEd's state chronic-absenteeism table from its embedded Flourish
  visualization; recorded provenance in `data/external/SOURCES.md`.
- Wrote `analyze_doseresponse.py`: state NAEP changes vs 2020-21 virtual share and vs
  absenteeism rise. Debugged a column collision (`group` present in both merged CSVs).
- Wrote `analyze_absence.py`: B018101 absence shares, score-by-absence gradients, and
  Kitagawa/Oaxaca decompositions of mean changes into composition vs within components.
- Updated report to v1.2; tagged and released.

## Phase 4 — Inference upgrade and positioning (v1.3)

- Wrote `analyze_v13.py`: randomization inference for the waiver DiD (2,000
  permutations of the waiver-date vector across states), MDE80 = 2.8×sd(perm) power
  benchmark, pre-trend joint test, sector z-tests on published standard errors, and a
  weighted dose-response variant.
- Dispatched literature agents to verify novelty; read/processed: Dewey et al. 2026
  (Education Recovery Scorecard; source of the "never been tested" quote), Bleiberg's
  2020 dissertation (binary waiver DiD on means through 2013 — corroborating null) and
  his published 2026 school-improvement paper, Malkus 2025 "Testing Theories of Why"
  (corrected my own misremembered title — the half-recalled "Of Backpacks and
  Smartphones" does not exist), Malkus 2015, Wyckoff 2025 "Puzzling Over Declining
  Academic Achievement," Petrilli 2020, Barnum 2022, Hemelt–Jacob 2020,
  Dee–Dizon-Ross 2019.
- Wrote the "Related Work and Contribution" section staking three novelty claims
  (first staggered waiver event study on state percentiles; first formal cohort/period
  decomposition; first systematic sector test). Tagged v1.3.

## Phase 5 — Exhaustive avenues (v1.4)

- Hand-coded `data/commoncore.csv` (adoption/repeal status by state, incl. the four
  never-adopters and Minnesota's math-only non-adoption) and pulled CDC overdose-death
  rates by state (`data/overdose.csv`).
- Pulled TUDA urban-district NAEP panels (jurisdiction codes XA–XZ) and hand-curated
  the 26-district TUDA→CSDH crosswalk (`data/tuda_csdh_match.csv`; Austin = NCES
  4808940, NYC = mean of 32 component districts).
- Pulled PIAAC 2017/2023 adult literacy/numeracy results and G12 NAEP 2024; compiled
  exclusion-rate and participation-rate series 2013–2024 for the measurement-artifact
  test (`evidence/piaac_g12_validity.md`).
- Wrote `analyze_v14.py`: Common Core never-adopter test (+ Minnesota triple-diff),
  TUDA dose-response, opioid correlation.
- Tried and cut (documented in the report's "Avenues examined and set aside"):
  opioid-exposure correlation (null/inconsistent), cross-country smartphone-adoption
  timing (data quality), cannabis legalization and discipline reform (no clean
  variation). Tagged v1.4.

## Phase 6 — PISA microdata (v1.5)

- Downloaded the PISA 2022 student questionnaire SAV (2 GB) from OECD; learned to read
  it with pyreadstat using `usecols`; mapped the missing-code conventions (95/97/98/99).
- Discovered by reading `meta.variable_value_labels` that ST273Q06JA is coded
  1 = "Every lesson" (inverted from intuition); caught and fixed a wrong-signed (+15)
  first run.
- Wrote `analyze_pisa.py`: Rubin's-rules combination over 10 plausible values, final
  student weights, school-clustered SEs, ESCS-quadratic adjustment; distraction and
  leisure-device gaps; device-engagement profiles by within-country score quartile vs
  ESCS quartile (the bottom-performer-not-low-income result).
- Discovered ST326/ST322 were not administered in the USA (0 nonmissing); examined the
  IC171 fallback and CUT it as an access artifact (abstainers atypical in a
  95%-saturated population).
- Performed Bleiberg due diligence (`evidence/novelty_check.md`). Tagged v1.5.

## Phase 7 — Effort confounder and phone bans (v1.6)

- Downloaded the PISA 2018 SAV (1.9 GB); wrote `analyze_effort.py` comparing the
  effort-thermometer items (EFFORT1/EFFORT2) across 2018→2022 in both microdata files;
  bounded the test-effort confounder at <5% of the decline; checked OECD behavioral
  indicators and the SEDA consequential-test argument.
- Read the school-phone-ban causal literature: Beland & Murphy 2016 (England),
  Abrahamsson 2024 (Norway), Beneito & Vicente-Chirivella 2022 (Spain), Kessel et al.
  2020 (Sweden null), Figlio & Özek 2025 (Florida).
- Hand-coded `data/phonebans.csv`: 50-state school phone-ban statutes with effective
  dates and bindingness classes; wrote the pre-registered NAEP-2026 analysis plan
  (`docs/phoneban_design.md`) with exposure groups, estimators, predictions, and
  threats — frozen before data exist. Tagged v1.6.
- Wrote the 2-page policy brief (`report/brief.tex`) for non-technical readers.
- Wrote `docs/STATE.md` as the frozen single-source-of-truth state document.

## Phase 8 — Fertility-literature parallel (v1.7)

- Ran two parallel literature-scan agents on the smartphones→fertility literature;
  read/processed: Myers & Hooper 2026 (NBER w35310, iPhone/AT&T-exclusivity design),
  Hudson & Moscoso Boedo 2026a/b (terrain-ruggedness IV for 4G; "Wide and Shallow"
  full PDF), Guldi & Herbst 2017, Billari–Giuntella–Stella 2019, Bellou 2015,
  Breen–Koebe–Kashyap 2025 (Nigeria), Gao et al. 2026, Büyükeren–Makarin–Xiong 2026
  (Tinder), Jung & Lusher 2026, Ershov–Fong–Yildirim 2026, Kearney–Levine–Pardue 2022
  JEP, Kearney & Levine 2025, Alice Evans's fertility essays, Burn-Murdoch's FT
  coverage, the Reason/UnHerd critiques, Twenge & Park 2019.
- Identified the transferable methods cases: Jain & Stemper 2024 (3G×PISA, 82
  countries), Guriev–Melnikov–Zhuravskaya 2021, Manacorda & Tesei 2020 (lightning IV),
  Falck–Gold–Heblich instrument lineage, Golin 2022, Donati et al. 2025,
  Braghieri–Levy–Makarin 2022 (Facebook rollout), Churchill & Johnson 2026
  (broadband×YRBS), Vigdor–Ladd–Martinez 2014, Caldarulo et al. 2023.
- Wrote `evidence/fertility_parallel.md`; integrated into the report (new H2
  corroboration paragraph, Related Work additions, Evans-style dual-criterion framing
  in Synthesis, Limitations hedge); added six bibliography entries. Tagged v1.7.

## Phase 9 — 4G×SEDA causal design (v1.8)

- Scoped data feasibility by agent: enumerated FCC Form 477 mobile vintages (free data
  starts Dec 2014 — too late, LTE already 98.5% covered per FCC Mobile Competition
  Reports 16/17/19, read from the PDFs); discovered the archived NTIA SBDD/National
  Broadband Map (block×provider mobile coverage, 9 semiannual waves Jun 2010–Jun 2014,
  free, no login) as the rescue; verified its 4G proxy against Verizon's Dec-2010 LTE
  launch; located USDA ERS ruggedness and NASA LIS/OTD lightning IV ingredients;
  confirmed by repeated search that no one has run mobile rollout × US test scores.
  Wrote `docs/seda4g_design.md`.
- Ran the validation exercise (`seda4g/01_download.sh`–`03_validate.py`): probed the
  NBM Analyze Tables; built block-level pilot exposures for 8 states; proved the
  <2-sq-mi large-block restriction does NOT apply to wireless (≥95.7% pop coverage in
  every wave); validated the national trajectory against FCC benchmarks, the Verizon
  launch metros, the rural lag (Spearman 0.61), and the Form 477 Dec-2015 splice;
  diagnosed grantee tier-coding heterogeneity (MA/DE coded LTE tier 7, TX/WA tier 6,
  CO invisible until Dec-2011) and quantified fixed-wireless leakage in the Analyze
  Tables (2.5pp national, 20pp county p90 at Dec-2012) — forcing the primary measure
  onto mobile-only block CSVs. Handled Deflate64 zips, 2000-vs-2010 census-block
  vintages, and the `SBDD_XX_Fall2010.zip` naming scheme.
- Built the national exposure panel: downloaded and processed 459/459 state-wave
  wireless files (~48 min, parallel, resumable), computed county population shares
  under five codings (any-mobile, tier≥6, tier-7, Verizon-only ×2) with 2000/2010
  PL94-171 block weights, derived treatment dates (25/50/75% crossings) →
  `seda4g/exposure_county_panel_national.csv` (28,283 rows), `treatment_dates.csv`.
- Located SEDA 5.0 already on local disk (district long file from a prior project) and
  confirmed the county file downloads directly from Stanford's repository.
- Wrote and ran `seda4g/04_eventstudy.py`: manual Callaway–Sant'Anna ATT(g,t) with
  not-yet/never-treated controls and county-block bootstrap; TWFE continuous dose with
  county + state×year×grade×subject FE (manual alternating-projection absorption);
  adolescent-exposure gradient (within county-year, across grades); 500-draw
  within-state permutation inference; 10-spec robustness grid. Result: precise null on
  the arrival-timing margin (MDE80 0.013 SD), pre-trend drift disclosed.
- Integrated as report §"4G rollout timing" with figure; updated Related Work, H2,
  Limitations. Tagged v1.8.

## Phase 10 — Verification layer (v1.8)

- Built `evidence/claims_audit.md`: audited 41 load-bearing claims (26 computed /
  2 pulled / 13 citation), each with a <5-minute human verification path; external-
  anchors table; identified the one provenance gap (LTT P10 −12.6 exists only as
  hard-coded Digest-sourced literals).
- Wrote `checks.py`: 62 assertions (tier 1 recomputes headline facts from raw CSVs;
  tier 2 freezes every results JSON); runs clean.
- Wrote `docs/verification_checklists.md`: seeded random spot-check of 34 hand-coded
  policy rows with source links, and a 5-number NAEP Data Explorer walkthrough.
- Ran five clean-room replications (blind agents barred from reading the analysis
  code, re-deriving from fresh API pulls / raw microdata): cohort decomposition
  (exact match), PISA distraction (exact US match; item coding independently confirmed
  from SAV metadata; OECD difference traced to senate-vs-raw weighting), Kitagawa
  absence (exact data match; exposed a G4/G8 label blur in internal summaries — report
  itself correct), waiver event study (null + MDE qualitatively confirmed; point
  estimate shown to be window/pooling-dependent), Catholic sector (in progress).
- Audited report.tex against every results JSON (no numerical discrepancies found);
  fixed one cosmetic wording issue (2003 absence band).

## Phase 11 — Public-readiness

- Audited the repo for secrets (none), personal information, large blobs (none), and
  data-redistribution compliance (SEDA/PISA not redistributed; CSDH/FutureEd
  attributed; federal data public domain).
- Scrubbed absolute local paths from tracked scripts and docs; untracked a local-notes
  file containing personal directory paths and purged it from git history
  (filter-branch over the affected commits, tag re-pointed, verified tree parity).
- Added LICENSE (MIT) and a README "License and data terms" section.

## Standing infrastructure used throughout

- Git/GitHub: 16 commits, tags v1.0–v1.8, each tagged release carrying the compiled PDF.
- tectonic for all LaTeX compilation (natbib/plain bibtex).
- Background research/build agents for literature scans, large downloads, and
  blind replications; all agent findings written to `evidence/` dossiers with URLs.
- Memory/state docs (`docs/STATE.md`, `docs/TASKLOG.md`) maintained so the project
  survives context resets.

## 2026-06-12 — LTT 2025 release assessment
- Identified the 2026-06-10 release (NYT link from user; NYT paywalled) as the LTT 2025
  wave, ages 9/13, via NAGB/NPR/Chalkbeat.
- Pulled full 2025 wave from NAEP Data Service API: 4 means, 20 percentiles, S003501
  reading-for-fun shares; anchored against American Experiment summary (−7 read / −15 math,
  age 13 vs 2012 — match). Recorded in evidence/ltt_2025.md with v1.9 scope.
- Verified checks.py LTT assertions are year-indexed → appending 2025 rows is safe.
- Verdict: update warranted but modest; verdicts unchanged/strengthened; one claim
  ("no aggregate recovery") needs an age-9 nuance. Report not yet touched.
