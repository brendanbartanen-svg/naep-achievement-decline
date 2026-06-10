# Clean-room replication comparison

Five independent agents re-derived the project's riskiest computed numbers with NO
access to the analysis code, results files, report, or evidence dossiers (each was
also instructed not to web-search for the answers). Each pulled data fresh from the
NCES NAEP API or read the raw PISA microdata directly. Scripts and results.json in
the subfolders. Comparison written 2026-06-10 against the published values in
report.tex / docs/STATE.md.

| # | Target | Original | Blind replication | Verdict |
|---|--------|----------|-------------------|---------|
| 1 | Cohort decomposition, G8 reading 2013–19 | −4.4 = +1.6 entry − 6.0 growth | −4.45 = +1.57 − 6.02 | **EXACT** |
| 2 | PISA distraction gap, US, ESCS-adj | −13.2 (SE 3.9) | −13.25 (SE 3.91); item coding independently confirmed from SAV metadata (1 = "Every lesson") | **EXACT** |
| 3 | PISA distraction gap, OECD pooled | −15.0 (SE 1.3) | −13.28 (SE 0.63) | **MATCH, convention-attributable**: original uses raw W_FSTUWT + country FE; replication used senate weights. Same sign/magnitude class. |
| 4 | Kitagawa absence, G8 shares + decomposition | shares 19.6/21.6/32.5/29.5 (math, 2013/19/22/24); composition = 25–42% of 2019–24, 7–19% pre-pandemic | shares identical to the decimal; 24.7–30.6% of 2019–24, 7.5/19.2% pre | **EXACT on data; decomposition within band** |
| 5 | Waiver event study, G8 math P10 | pooled ≈0 (+0.09 SD), perm p=0.46, MDE80=3.2 pts | −1.13 pts (−0.135 SD) 2009–19 / +0.21 pts 2003–19, RI p=0.25/0.87, MDE80=2.74 pts; pre-trend drift reproduced | **QUALITATIVE**: null + informative MDE robust; the point estimate is window/pooling-dependent and should be reported as ≈0, not a precise value |
| 6 | Catholic sector, G8 reading 2013–19 | Catholic −7.8 (z=−3.4) vs public −4.0 | Catholic −7.80 (z≈−4.0 approx-SE) vs public −4.02; NAEP official significance tests agree | **EXACT on changes; z differs only by SE method** |
| 7 | Catholic math (uninformative) + 2019–24 divergence | math SE too large to discriminate; pub−cath math DiD −7.9 (z=−2.6) | math −1.46 (z≈−0.7, officially "EQUAL"); DiD −7.87 (z≈−2.8, officially significant) | **MATCH** |

## Notes and flags

- **No pipeline errors were found.** Every divergence traced to a defensible
  convention choice (weighting, window, SE construction), not a bug.
- The PISA replication independently re-derived the ST273Q06JA coding direction from
  the file's own value labels — the exact spot where the original implementation
  briefly had a sign error (caught in development). The blind agent confirms the
  published sign is right.
- The Kitagawa replication exposed that internal summaries (STATE.md/README prose)
  blurred G4 vs G8 absence shares; the report itself was always correctly labeled.
  Fixed in v1.8.
- The waiver point estimate flips sign across estimation windows (−0.13 to +0.03 SD)
  — exactly what a true near-zero effect looks like. The robust claims are the null
  and the MDE, which both replications agree on.
- Sector SEs: the ad-hoc API has no SE stattype. The original used published SEs;
  the replication approximated from SD/n/design-effect and anchored on NAEP's own
  official significance tests (type=sigacrossyear), which agree with every published
  verdict. Process flag: the replication agent accepted the standard NCES
  data-usage notice in the browser while attempting to retrieve exact SEs from the
  NAEP Data Explorer (statistical-use-only terms; retrieval was instructed).
- Replication-purity boundaries (stated in advance): the waiver replication consumed
  `data/waivers.csv` as treatment input (the hand-coded dates are verified separately
  by the human checklist in docs/verification_checklists.md), and agents received API
  *mechanics* hints (chunk sizes, suffixes, one pandas NA trap) but never result values.
