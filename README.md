# Why Did American Student Achievement Decline?

Self-contained analysis verifying the post-2013 NAEP decline and testing eight candidate
explanations. Final deliverable: `report/report.pdf` (16 pp).

## Structure
- `naep_pull.py` — pulls main-NAEP national means/percentiles, subgroups (race, sex, NSLP),
  and state means from the NCES NAEP Data Service API → `data/naep_main.csv`
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
- Verdicts: pandemic disruption = dominant cause of phase 2 only; accountability retreat +
  smartphone/digital-media displacement = best-supported phase-1 drivers; chronic absenteeism =
  main brake on recovery; demographics, funding cuts, teacher shortages = minor.
