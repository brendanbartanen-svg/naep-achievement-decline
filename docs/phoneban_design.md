# Pre-registered design: state phone-ban rollout vs NAEP 2026

*Specified 2026-06-10, before NAEP 2026 results exist (administration Jan–Mar 2026;
expected release late 2026/early 2027). Policy coding frozen in `data/phonebans.csv`
(agent-verified June 2026; re-verify IL signature and CO/MD signing dates at analysis time).*

## Treatment groups (exposure by the NAEP 2026 window)
- **long** (≈2.5 yr): FL (instructional-time ban from 2023-24; K-8 bell-to-bell from 2025-26)
- **medium** (≈1.5 yr): IN, LA, SC, VA (effective 2024-25; SC and VA mid-year Jan 2025)
- **short** (≈0.5 yr): the 2025-26 wave — BTB: AL, AR, MO, NE, NH, NY, ND, OK, TX; INSTR: AZ, IA, KY, NC, TN, UT, WV; DISTRICT: AK, NV, NM
- **minimal** (<2 months / weak): OH, OR (full bans Jan 2026), ID (policies due Dec 2025), MN (district-policy only)
- **untreated / not-yet-treated** (preferred controls): CA, CO, DE, GA, HI, IL, KS, ME, MD, MI, NJ, RI, VT, WI (enacted, effective 2026-27+) plus MA, MS, MT, SD, WY, CT, WA, PA (none/recommendation)
- DC: partial (DCPS-only 2025-26; charters 2026-27) — exclude or flag.

## Outcomes
State NAEP 2026 minus 2024: means and P10/P25 (math & reading, G4 & G8), from the
NAEP API as in `naep_pull.py` / `naep_pull_v11.py`.

## Estimators
1. Primary: DiD of 2024→2026 change, treated (long+medium+short) vs not-yet-treated,
   pooled across the four cells in within-cell SD units, state-clustered + randomization
   inference permuting the treatment assignment (pipeline of `analyze_v13.py`).
2. Dose ordering: long > medium > short > minimal > untreated (Jonckheere-style trend test
   / regression on exposure years).
3. Intensity: bell-to-bell vs instructional-time vs district-discretion within the treated group.
4. Placebo/pre-trend: same specification on 2022→2024 changes (no state had a ban before
   spring 2023 NAEP-relevant exposure except none; FL's 2023-24 start postdates the Jan–Mar
   2024 administration window almost entirely — verify exposure months).

## Predictions under the digital-media hypothesis (H2)
- Positive treatment effects concentrated at P10/P25 and at grade 8 (where v1.5 PISA
  microdata show device over-engagement concentrates among low performers).
- Larger effects for bell-to-bell than instructional-time bans, and for longer exposure.
- Under H2-null (e.g., the decline is effort/culture-driven only), bans should do nothing.

## Threats
- Policy endogeneity: states adopting early may be those declining worst (check 2013–2024
  trends by adoption wave as a balance test).
- Concurrent policies (absenteeism crackdowns, tutoring, science-of-reading laws) — code
  the major ones for the treated states before analysis.
- Compliance heterogeneity (district-discretion states); attenuates toward null.
- Short exposure for the 2025-26 wave; the design is honest about power — compute MDE
  from the permutation distribution as in the waiver test.

## External benchmarks to compare against
Causal phone-ban literature (effect sizes; see evidence/effort_phonebans.md once written):
Beland & Murphy (2016, UK); Abrahamsson (2024, Norway); Beneito & Vicente-Chirivella (Spain).
