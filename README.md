# Why Did American Student Achievement Decline?

Self-contained analysis verifying the post-2013 NAEP decline and testing eight candidate
explanations, discriminating tests (v1.1), mechanism checks (v1.2), an inference/robustness
upgrade with verified related-literature positioning (v1.3), and an exhaustive-avenues
extension (v1.4: Common Core test, TUDA district dose-response, adult-PIAAC mirror, grade 12,
validity checks, documented try-and-cut analyses). Final deliverable: `report/report.pdf` (27 pp).

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
  P10 −12.6 pts 2012→2020 vs P90 +0.1); 2020-2022 across-the-board pandemic drop; no aggregate
  recovery since (reading still falling; 90-10 gaps widest on record).
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
  (AK,NE,TX,VA) declined as much or more (pooled P10 diff −0.4, p=0.72); Minnesota's non-CC math
  fell *less* than its CC reading; (ii) TUDA district dose-response (26 districts × CSDH shares,
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
