# Why Did American Student Achievement Decline?

Self-contained analysis verifying the post-2013 NAEP decline and testing eight candidate
explanations, plus three discriminating tests (v1.1). Final deliverable: `report/report.pdf` (20 pp).

## Structure
- `naep_pull.py` — pulls main-NAEP national means/percentiles, subgroups (race, sex, NSLP),
  and state means from the NCES NAEP Data Service API → `data/naep_main.csv`
- `naep_pull_v11.py` — school-sector (public/private/Catholic) trends and the state × year
  percentile panel → `data/naep_v11.csv` (+ `data/naep_schtype_pct.csv`)
- `data/waivers.csv` — state ESEA/NCLB waiver approval dates (ED/CRS/EdWeek, agent-verified)
- `analyze_cohort.py` — cohort-vs-period decomposition (pseudo-growth G4→G8)
- `analyze_v11.py` — public-vs-Catholic comparison; waiver event study/DiD on state P10
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
