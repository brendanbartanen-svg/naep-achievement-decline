# Project state (frozen 2026-06-10, post-v1.6)

Single source of truth for resuming work. Repo: github.com/brendanbartanen-svg/naep-achievement-decline (private). Local: `/Users/yvp3tf/Documents/CC Sandbox/naep-achievement-decline/`. Deliverables: `report/report.pdf` (30pp), `report/brief.pdf` (2pp policy brief). Compile: `cd report && tectonic report.tex` (plain bibtex/natbib — NOT the AERJ pinned-biber setup).

## Versions (all tagged + GitHub releases with PDF)
- v1.0 baseline: trends verified from NCES API; 8 hypotheses tested; 16pp.
- v1.1 discriminating tests: cohort/period decomposition; public-vs-Catholic; waiver event study.
- v1.2 mechanism checks: state closure dose-response (CSDH merge); within-NAEP absence crosswalk (B018101, Kitagawa).
- v1.3 credibility: randomization inference + MDE for waiver test; sector z-tests on published SEs; Related Work section (agent-verified novelty).
- v1.4 exhaustive avenues: Common Core test; TUDA district dose-response; adult PIAAC mirror; G12; exclusion/participation validity; opioid/cannabis/discipline set-asides.
- v1.5 PISA 2022 microdata (613,744 students): distraction −13 US/−15 OECD ESCS-adj; 5+hr leisure −40.5; exposure concentrated in bottom score quartile but FLAT across SES; Bleiberg due diligence.
- v1.7 fertility-literature parallel: Myers-Hooper (NBER w35310, iPhone/AT&T exclusivity → births −4.5–8% teens, 33–52% of GFR decline), Hudson-Moscoso Boedo (4G ruggedness IV → teen-fertility collapse + teen suicides; 25+ null = our predicted age profile), Jain-Stemper (3G×PISA 82 countries, −0.04 to −0.08 SD) folded into H2/Related Work; Evans dual-criterion framing in Synthesis; dossier `evidence/fertility_parallel.md`. US mobile-rollout × test scores design confirmed OPEN (Wyckoff gap statement citable); scoping in `docs/seda4g_design.md`.
- v1.6 effort confounder bounded (thermometer 2018→2022 both microdata files: −0.13 US/−0.16 OECD of 10 → <5% of decline; OECD behavioral indicators stable/opposite-signed; SEDA consequential tests show same decline); phone-ban causal lit into H2 (Beland&Murphy +0.142 SD low achievers; Abrahamsson; Beneito; Figlio&Özek FL; Kessel null-where-nonbinding); pre-registered NAEP-2026 ban design (`docs/phoneban_design.md`, `data/phonebans.csv`).

## Headline findings (key numbers)
- Peaks 2013 (G4 reading 2015). 2024 levels: G4 math≈2005, G8 math≈2000 (273.8), G4 reading<1998, G8 reading 258.0 = lowest ever; G12 2024 math 146.9 & reading 282.6 = lowest ever. Total 2013→2024: −0.14 to −0.30 SD.
- Two phases: 2013-19 bottom-only (LTT age-13 math P10 −12.6 vs P90 +0.1, 2012→2020); 2019-22 uniform COVID drop; 2022-24 top recovers, bottom keeps falling. 90-10 gaps widest ever (e.g., G8 math 93→109).
- Cohort decomposition: G8 2013-19 reading −4.4 = +1.6 entry − 6.0 growth → period effect in adolescence (cohorts arrived at G4 at record levels).
- Sector: Catholic G8 reading 2013-19 −7.8 (z=−3.4) ≥ public −4.0; Catholic math uninformative (SE 1.6); 2019-24 G8 math divergence pub−cath −7.9 (z=−2.6).
- Waiver event study: pooled P10 +0.09 SD, perm p=0.46; MDE80=3.2 pts G8-math-P10 (< half Dee-Jacob 7.2); pre-trend p=0.08 caveat; Bleiberg 2020 diss. (binary, means, ≤2013) also null — corroborates.
- Common Core: never-adopters (AK,NE,TX,VA) declined ≥ adopters (pooled P10 diff −0.4, p=0.72); MN math-only triple-diff +2.3 (wrong sign for CC harm).
- Closures: decisive at district level (Goldhaber/Jack-Oster) but between-state R²≈0 (pooled −0.04/10pp virtual, p=0.80); TUDA 26-district version weak too (−0.18/10pp, p=0.23, wide CIs).
- Absence: NAEP B018101 3+days/month ~19.5% (2013) → 24% (2019) → 35% (2022) → 30% (2024); Kitagawa: absence shift = 25-42% of 2019-24 declines, 7-19% of pre-pandemic G8.
- Adults (PIAAC 2023): US literacy −12 (2017→2023), ≤L1 19%→28%, top stable; 19 OECD countries declined. Caveats: 28% US response rate, tablet-only.
- Validity: exclusion flat 1-3% 2013-2024; participation 92/89 in both 2022 & 2024.
- Reading for fun (age 13): 27% (2012) → 17% (2020) → 14% (2023).
- Verdicts: H2 digital media = best-supported phase-1 driver (timing, international+adult synchrony, cohort, sector, microdata exposure profile, ban-study heterogeneity); accountability = weakened to marginal/G4-bottom; absenteeism = phase-2 amplifier + recovery brake; demographics/funding/CC/teachers/effort/artifacts = rejected or minor; opioids tested null; cannabis/discipline/cross-country-smartphone-timing = documented set-asides.

## Data/API gotchas (hard-won)
- NAEP API `nationsreportcard.gov/DataService/GetAdhocData.aspx`: percentiles PC:P1/P2/P5/P7/P9 = 10/25/50/75/90; pre-2003 years need sample suffix (1990R2, 2000R3) else 400; chunk years ~4 & jurisdictions ~13 (big requests hang); SLUNCH3 dead in 2024; SCHTYP2 queries fail 2019+ (private suppression) — use SCHTYPE; TUDA codes XA..XZ (XA=Atlanta…XZ=Fort Worth, see data/tuda_csdh_match.csv); LTT via NRCDataService + Program=LTT, subscales RRPSCT/MRPSCT, cohort=1/2; no SE stattype exists (SD:SD yes); G12 subscale MWPCM (math, 0-300).
- PISA: 2022 SAV CY08MSP_STU_QQQ.SAV + 2018 STU/CY07_MSU_STU_QQQ.sav under data/external/pisa/ (gitignored; URLs in README/.gitignore context); ST273Q06 coding 1=Every lesson (don't invert!); ST326/ST322 NOT administered in USA; IC171 frequency = access artifact (do not use as exposure); EFFORT1/EFFORT2 in both cycles; pandas read_csv eats "None" as NaN (keep_default_na=False for B018101 absence categories).
- Analysis scripts: analyze.py (main), analyze_ltt.py, analyze_intl.py, analyze_cohort.py, analyze_v11.py (sector+waiver), analyze_v13.py (permutation/MDE), analyze_doseresponse.py, analyze_absence.py, analyze_v14.py (CC/TUDA/opioid), analyze_pisa.py, analyze_effort.py. Results JSONs in data/. Evidence dossiers with all URLs in evidence/*.md.

## Open items / future work
- NAEP 2026 phone-ban test: design + 50-state coding frozen (docs/phoneban_design.md; re-verify IL signature, CO/MD dates at analysis time). Results expected ~early 2027.
- Before any journal submission: re-check Bleiberg's pipeline for percentile extensions; restricted-use NAEP microdata path; PISA 2012 ICT panel (ASCII+control-file parsing, ~1 day).
- SEDA/broadband district design = best remaining causal idea for H2 pre-pandemic.
