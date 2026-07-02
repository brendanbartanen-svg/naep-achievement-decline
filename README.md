# Why Did American Student Achievement Decline?

Self-contained analysis verifying the post-2013 NAEP decline and testing eight candidate
explanations, discriminating tests (v1.1), mechanism checks (v1.2), an inference/robustness
upgrade with verified related-literature positioning (v1.3), and an exhaustive-avenues
extension (v1.4: Common Core test, TUDA district dose-response, adult-PIAAC mirror, grade 12,
validity checks, documented try-and-cut analyses). v1.5 adds a PISA 2022 student-microdata analysis (613,744 students; Rubin-combined PVs,
school-clustered, ESCS-adjusted): the distraction (−13 US / −15 OECD) and 5+hr leisure-use
(−40.5) score gaps survive SES adjustment, and device over-engagement is monotonically
concentrated among low performers within countries while flat across SES — matching the
decline's bottom-heavy signature (`analyze_pisa.py`; raw 2GB SAV gitignored, re-download via
https://webfs.oecd.org/pisa2022/STU_QQQ_SPSS.zip). Bleiberg due diligence in
`evidence/novelty_check.md`. v1.6 closes the test-effort confounder (PISA effort thermometer
2018→2022 via both microdata files: effort fell 0.13-0.16/10 pts → implies <5% of the score
decline; OECD behavioral indicators stable; same decline on consequential SEDA state tests)
and adds the quasi-experimental phone-ban literature to H2 (Beland-Murphy +0.14 SD for low
achievers; Abrahamsson; Beneito; Figlio-Özek Florida) plus a pre-registered NAEP-2026 ban
design (`docs/phoneban_design.md`, `data/phonebans.csv` — 50-state coding with effective
dates). `analyze_effort.py`; 2018 PISA file gitignored
(https://webfs.oecd.org/pisa2018/SPSS_STU_QQQ.zip). v1.7 integrates the 2025–26
smartphone–fertility causal literature (Myers & Hooper NBER w35310 iPhone/AT&T design;
Hudson & Moscoso Boedo 4G ruggedness IV — same shock, same 2007 timing, same
adolescent-specific age profile as the achievement decline) plus Jain & Stemper's
3G×PISA estimates (−0.04 to −0.08 SD, 82 countries) into H2 and Related Work, and adds
a dual-criterion synthesis framing borrowed from the fertility-puzzle genre
(`evidence/fertility_parallel.md`). v1.8 executes the within-US 4G-rollout design end to
end (first of its kind): county high-speed-mobile coverage built from the free archived
National Broadband Map (459/459 state-waves, validated against FCC benchmarks and
Verizon's Dec-2010 launch markets; `seda4g/` pipeline) × SEDA 5.0 county scores
2009-2019 — Callaway–Sant'Anna event study, continuous dose, and an adolescent-exposure
gradient all return a precise null on the arrival-timing margin (dose −0.002 SD,
perm p=.66, MDE80 0.013; gradient +0.011/yr, perm p=.12, MDE80 0.016; 10-spec
robustness grid all |coef|≤0.003 with flipping signs; visible urban-rural pre-trend
disclosed). Read: the decline did not ride on local cell-tower timing — disciplines the
mechanics of H2 without touching its national, adoption-driven channel (report §4G).
v1.8 also adds a verification layer: `evidence/claims_audit.md` (41 load-bearing claims
with <5-min verification paths), `checks.py` (62 assertions, all passing),
`docs/verification_checklists.md` (human spot-check lists), and blind clean-room
replications of the riskiest computed numbers in `verification/cleanroom/`
(cohort decomposition, PISA distraction, Kitagawa, waiver null all reproduce).
v1.9 (June 12, 2026) folds in the 2025 Long-Term Trend wave released June 10, 2026
(ages 9/13, 2024-25 school year; pulled directly from the LTT Data Service,
`evidence/ltt_2025.md`): age 13 stays flat at multi-decade lows with the mathematics
bottom decile still falling while the top recovers (90-10 gap 114.0, widest ever);
age 9 posts the data's first bottom-led recovery (+3.8 both subjects, P10 +7.5/+9.3);
reading-for-fun at age 13 holds at its 14% floor. Verdicts unchanged, sharpened.
v1.9 also adds a version/date stamp and a "How this report was produced" disclosure
paragraph (human-AI division of labor) ahead of the abstract; claims audit grows to
42 rows, `checks.py` to 71 assertions.
v2.0 (July 2, 2026) responds to a written external review with no changes to analyses,
estimates, or data: claim-strength calibration throughout (the synthesis now claims a
consistency ranking, not a causal estimate, with the inferential strategy stated in the
Introduction); symmetric five-part treatment of the two null designs (waiver timing and
4G rollout, the latter framed as the project's own adversarial test of its leading
candidate); adolescent mental health added as a named rival hypothesis with web-verified
CDC YRBS and Mojtabai et al. sourcing (claims audit rows B15--B16; audit now 44 rows),
its own scorecard row, and an honest cannot-separate assessment; an exposure-vs-pathway
taxonomy for H2; and a full organizational and line-level edit (abstract 300 words,
em-dashes cut 87%, Limitations restructured). One directional misreading of the Minnesota
Common Core triple-difference was found during the revision and corrected with in-text
disclosure (claims-audit row B9 updated). Process artifacts (charter, 11 agent proposals,
reconciled edit plan, apply log, and a point-by-point response memo) are in
`docs/revision_v2/`.
Final deliverables: `report/report.pdf` (~39 pp), `report/brief.pdf` (2 pp policy brief), `report/slides.pdf` (28-slide academic talk; `slides.tex`).

## Structure
- `naep_pull.py` — pulls main-NAEP national means/percentiles, subgroups (race, sex, NSLP),
  and state means from the NCES NAEP Data Service API → `data/naep_main.csv`
- `naep_pull_v11.py` — school-sector (public/private/Catholic) trends and the state × year
  percentile panel → `data/naep_v11.csv` (+ `data/naep_schtype_pct.csv`)
- `data/waivers.csv` — state ESEA/NCLB waiver approval dates (ED/CRS/EdWeek, agent-verified)
- `analyze_cohort.py` — cohort-vs-period decomposition (pseudo-growth G4→G8)
- `analyze_v11.py` — public-vs-Catholic comparison; waiver event study/DiD on state P10
- `analyze_doseresponse.py` — state NAEP changes vs CSDH 2020-21 virtual share and vs
  rise in chronic absenteeism (FutureEd); `data/external/` holds the downloaded sources
- `analyze_absence.py` — within-NAEP attendance crosswalk (B018101): shares, gradients,
  Kitagawa decomposition → `data/absence_results.json`
- `analyze_v13.py` — robustness/inference: permutation (randomization) inference and MDE
  for the waiver DiD, pre-trend test, sector z-tests on published SEs, weighted dose-response
- `evidence/novelty_check.md` — agent-verified positioning vs closest prior work
  (Dewey et al. 2026; Malkus 2025 "Testing Theories of Why"; Wyckoff 2025; Petrilli 2020;
  Malkus 2015; Barnum 2022)
- `data/ltt.csv` — NAEP Long-Term Trend means (hand-compiled from Digest tables 221.85/222.85,
  cross-validated against the LTT Data Service API; see `evidence/ltt_evidence.md`)
- `analyze.py` — main analysis: trend decomposition, percentile divergence, 90-10 gaps,
  subgroups, state scatter → `data/summary.json` + most figures
- `analyze_ltt.py`, `analyze_intl.py` — LTT, reading-for-fun, and PISA/TIMSS figures
- `evidence/` — sourced fact files gathered from NCES/OECD/Pew/research literature
  (each fact carries its source URL)
- `figures/` — all PDF figures
- `report/` — LaTeX source (`report.tex`, `refs.bib`); compile with `tectonic report.tex`

## Reproduce
```bash
python3 naep_pull.py        # ~5 min; hits the NCES API (pre-2003 years need R2/R3 suffixes)
python3 analyze.py && python3 analyze_ltt.py && python3 analyze_intl.py
cd report && tectonic report.tex
```

## Headline findings
- All four main-NAEP series peaked 2013 (G4 reading 2015); 2024 levels: G4 math ≈ 2005,
  G8 math ≈ 2000, G4 reading < 1998, G8 reading = lowest ever recorded.
- Two-phase decline: 2013-2019 erosion concentrated at the bottom decile (LTT age-13 math
  P10 −12.6 pts 2012→2020 vs P90 +0.1); 2020-2022 across-the-board pandemic drop; among
  adolescents no aggregate recovery since (reading still falling; age-13 math P10 fell further
  through 2025 while P90 recovered; 90-10 gaps widest on record). The 2025 LTT wave shows the
  first genuine bright spot: a bottom-led age-9 rebound (+3.8 in both subjects vs 2022).
- Verdicts: pandemic disruption = dominant cause of phase 2 only; chronic absenteeism =
  main brake on recovery; demographics, funding cuts, teacher shortages = minor.
- v1.1 discriminating tests (all three favor the digital-media hypothesis over accountability
  retreat for phase 1): (i) cohort decomposition — G8 losses accrue *during* middle school to
  cohorts that arrived at G4 at record levels (period effect in adolescence); (ii) Catholic
  schools (never under NCLB accountability) declined in step with publics pre-pandemic;
  (iii) waiver event study — state P10 scores show no relationship to when states were
  released from NCLB (pooled DiD +0.09 z, p=0.50).
- v1.3 credibility upgrade: waiver null holds under randomization inference (perm p=0.46;
  pre-trend p=0.08 caveat) and is informative — MDE80 ≈ 3.2 pts on G8 math P10, under half
  the Dee-Jacob NCLB effect (~7 pts); sector test formalized with published SEs (Catholic
  G8 reading 2013-19 decline z=−3.4; math uninformative; 2019-24 G8 math divergence z=−2.6);
  novelty verified: first staggered waiver event study on state NAEP percentiles (Dewey et
  al. 2026 call this counterfactual "never tested"), first formal cohort/period decomposition,
  first systematic sector test of the accountability hypothesis.
- v1.4 exhaustive-avenues sprint: (i) Common Core fails its state-variation test — never-adopters
  (AK,NE,TX,VA) declined as much or more (pooled P10 diff −0.4, p=0.72); Minnesota's spared (non-CC) mathematics showed no
  protective effect relative to other states (v2.0 corrects an earlier directional misreading
  of its +2.3 triple-difference); (ii) TUDA district dose-response (26 districts × CSDH shares,
  0→100% virtual range): weak gradient (pooled −0.18 pts/10pp, p=0.23), wide CIs — limitation,
  not contradiction, of the growth-based literature; (iii) adult-PIAAC mirror: US literacy −12
  (2017→2023), ≤Level-1 share 19%→28%, top stable; declines in 19 OECD countries — adults are
  untouched by school policy; (iv) G12 2024: lowest math/reading ever, same bottom-heavy
  signature; (v) validity: exclusion flat 1-3%, participation unchanged 2022→2024 — artifact
  explanations ruled out; (vi) tried-and-cut: opioid correlation (null/inconsistent, kept in
  analyze_v14.py), cross-country smartphone timing (data quality), cannabis, discipline reform
  (no clean variation) — documented in report §"Avenues examined and set aside".
- v1.2 mechanism checks: (i) between-state variation in 2020-21 virtual schooling explains
  almost none of between-state NAEP declines (pooled −0.04 pts/10pp virtual, p=0.80) — the
  district-level closure effect washes out under state aggregation; (ii) NAEP's own absence
  item shows disengagement rising pre-pandemic (3+ days absent: ~19.5% 2013 → 24% 2019 →
  ~30% 2024) and a Kitagawa decomposition attributes 25-42% of the 2019-24 declines (but
  only 7-19% of pre-pandemic G8 declines) to the absence shift.

## License and data terms
Code and text in this repository are MIT-licensed (see LICENSE). Data notes:
- **NAEP/NCES, PIAAC, NTIA SBDD/National Broadband Map, FCC Form 477**: U.S. federal
  government data, public domain; small extracts are committed in `data/`.
- **COVID-19 School Data Hub** and **FutureEd** absenteeism compilations: redistributed
  small derived tables with attribution; provenance and URLs in `data/external/SOURCES.md`.
- **SEDA 5.0** (Stanford Education Data Archive) and **PISA microdata** are NOT
  redistributed here (gitignored); download from edopportunity.org and oecd.org under
  their own terms. Only derived aggregate estimates appear in this repository.
- Policy codings (`data/waivers.csv`, `data/phonebans.csv`, `data/commoncore.csv`,
  `data/tuda_csdh_match.csv`) were hand-assembled for this project; verify before reuse
  (see `docs/verification_checklists.md`).
