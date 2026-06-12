# NAEP Long-Term Trend (LTT) data — verified against Digest tables 221.85/222.85 and LTT highlights pages
API supports LTT: https://www.nationsreportcard.gov/NRCDataService/GetAdhocData.aspx?...&Program=LTT (subscales RRPSCT/MRPSCT, cohort=1 (age9) / 2 (age13))

Timing notes: age 9 "2020" = Jan-Mar 2020 (PRE-pandemic); age 9 "2022" = Jan-Mar 2022; age 13 "2020" = fall 2019; age 13 "2023" = fall 2022; "2025" wave (both ages) administered in the 2024-25 school year (age 13 fall 2024, age 9 early 2025; released 2026-06-10). Revised format 2004+.

## National means (revised format era)
Age 9 reading: 2004: 216 | 2008: 220 | 2012: 221 (PEAK) | 2020: 220 | 2022: 215 | 2025: 218 (+3.8 recovery, −2.4 vs 2012)
Age 9 math:    2004: 239 | 2008: 243 | 2012: 244 (PEAK) | 2020: 241 | 2022: 234 | 2025: 238 (+3.8 recovery, −6.3 vs 2012; first-ever 2022 decline)
Age 13 reading: 2004: 257 | 2008: 260 | 2012: 263 (PEAK) | 2020: 260 | 2023: 256 (≈1971 level: 255) | 2025: 256 (flat)
Age 13 math:    2004: 279 | 2008: 281 | 2012: 285 (PEAK) | 2020: 280 | 2023: 271 (≈1992 level) | 2025: 270 (flat; −14.7 vs 2012)
Early years (original format): age9 read 1971: 208, 1980: 215, 1999: 212; age9 math 1973: 219, 1999: 232; age13 read 1971: 255, 1999: 259; age13 math 1973: 266, 1999: 276.

## Percentile changes
Age 13 MATH:   P10: 240.1→227.5→213.5 (Δ12-20: −12.6; Δ20-23: −14.0) | P25: −7.4/−11.5 | P50: −4.4/−8.1 | P75: −1.5/−5.8 | P90: +0.1/−6.5
Age 13 READ:   P10: −5.6/−6.7 | P25: −3.3/−5.6 | P50: −2.3/−4.2 | P75: −1.3/−3.7 | P90: −0.6/−3.1
Age 9 MATH (2012→2020→2022):  P10: −6.0/−12.3 | P25: −4.2/−10.6 | P50: −2.2/−7.5 | P75: −0.9/−5.2 | P90: −0.5/−2.5
Age 9 READ:    P10: −6.6/−9.5 | P25: −2.7/−7.6 | P50: −0.7/−4.3 | P75: +0.7/−2.8 | P90: +2.0/−2.4
Post-pandemic window (2022/23→2025), full levels in evidence/ltt_2025.md:
Age 13 MATH:   P10 −2.8 (213.5→210.7) | P25 −1.1 | P50 −0.8 | P75 −0.4 | P90 **+2.3** (322.4→324.7) → fan-out CONTINUES; 90-10 gap 88.7 (2012) → 108.9 (2023) → 114.0 (2025), widest ever
Age 13 READ:   P10 +1.2 | P25 +0.3 | P50 +0.1 | P75 +0.1 | P90 +0.6 (all flat)
Age 9 MATH:    P10 **+7.5** (178.4→185.9) | P25 +5.9 | P50 +3.5 | P75 +1.6 | P90 +0.7 → bottom-led recovery (P10 still −10.8 vs 2012)
Age 9 READ:    P10 **+9.3** (154.7→164.0, back to 2020 level) | P25 +6.3 | P50 +2.5 | P75 +1.2 | P90 +0.9
KEY: 2012→2020 (pre-pandemic) declines are concentrated almost entirely at the bottom; top decile flat or rising. COVID then hit everyone, still worst at bottom. 2022/23→2025: at age 13 the bottom keeps falling in math while the top recovers; at age 9 the recovery is real and bottom-led.

## Reading for fun "almost every day" (S003501)
Age 9:  2008: 47.6 | 2012: 52.5 | 2020: 42.0 | 2022: 39.3 | 2025: 37.0 (still drifting down)
Age 13: 1984: 35.1 | 1992: 37.0 | 2004: 29.5 | 2008: 25.6 | 2012: 27.1 | 2020: 17.1 | 2023: 14.3 | 2025: 14.2 (floor)
Age 13 "never or hardly ever": 2012: 21.9 → 2020: 29.1 → 2023: 31.2 → 2025: 28.9
NOTE: the big drop happened 2012→2020, BEFORE the pandemic.

Sources:
- https://nces.ed.gov/programs/digest/d23/tables/dt23_221.85.asp
- https://nces.ed.gov/programs/digest/d23/tables/dt23_222.85.asp
- https://www.nationsreportcard.gov/highlights/ltt/2022/
- https://www.nationsreportcard.gov/highlights/ltt/2023/
- 2025 wave: API pull 2026-06-12 (see evidence/ltt_2025.md for full tables, press anchors, and release links)
