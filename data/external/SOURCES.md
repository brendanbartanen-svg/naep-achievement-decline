# External data provenance (retrieved June 9, 2026)

## CSDH_state_learning_model_shares_2020_21.csv
Enrollment-weighted state shares of the 2020-21 school year (Oct 2020–May 2021) spent
in-person/hybrid/virtual, computed from the COVID-19 School Data Hub district file
`District_Overall_Shares_03.08.23.csv` (14,967 districts) weighted by NCES 2020-21
district enrollment. Verified against CSDH state pages (MA: 27/53/20 site vs 26.9/53.3/19.8
computed; WA: 5/36/59 vs 4.8/36.0/59.2).
- https://www.covidschooldatahub.com/for_researchers
- District shares CSV: https://assets.ctfassets.net/9fbw4onh0qc1/XfBEuMLMOBgHrhmjBdVpc/8e555b362876da16ba52c85be5b2effe/District_Overall_Shares_03.08.23.csv
- Coverage: 47 states + DC. Missing: IA, MT, OK. DC = DCPS only.
- Shares = most common monthly model districts *offered*, not student-level choices.

## FutureEd_state_chronic_absenteeism.csv
State chronic-absenteeism rates (state-agency definitions) compiled by FutureEd,
extracted from the Flourish visualization (id 15345306) embedded at
https://www.future-ed.org/tracking-state-trends-in-chronic-absenteeism/
- Columns: 2018-19, 2021-22, 2022-23, 2023-24, 2024-25 (partial).
- Missing states: AR, MT, NH, VT, WY; MN missing 2018-19.

## EDFacts SY2022-23 (not committed: SY2223_Chronic_Absenteeism_EDE.zip)
Federal chronic-absenteeism file (DG814PCT, SEA level), definitions differ from FutureEd
(e.g., AZ 28.1 FutureEd vs 41.2 EDFacts) — do not mix within one analysis.
- https://eddataexpress.ed.gov/resources/reports-and-files/chronic-absenteeism-data

## Not committed (size): NCES_2020-2021_District_Demographics.csv (9.7MB, weights for the
state aggregation), SY2223 zip/folder. Re-download via URLs above to reproduce.
