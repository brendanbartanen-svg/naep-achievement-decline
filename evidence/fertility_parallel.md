# The smartphone–fertility literature: findings and lessons for the achievement paper

Compiled 2026-06-10 from two agent literature scans (papers + methods). Purpose: extract
corroborating evidence, transferable identification designs, and caveats for the H2
(digital media) hypothesis in the achievement-decline report.

## 1. The new causal papers (2025–2026)

**Myers & Hooper (2026), "Is the iPhone Birth Control?" NBER WP 35310** (June 2026)
https://www.nber.org/papers/w35310
- Natural experiment: AT&T's exclusive iPhone carrier deal (June 2007–Feb 2011) →
  iPhone access varied with pre-existing AT&T 3G coverage across counties.
  Entropy-balanced Poisson + synthetic DiD; Verizon/Sprint coverage placebos null.
- iPhone access reduced births 4.5–8.0% (ages 15–19), 3.2–6.6% (ages 20–24),
  smaller at older ages; diffusion explains 33–52% of the GFR (15–44) decline.
- Mechanisms (ATUS/survey): less in-person interaction, less sex, more pornography;
  partly faster contraception information (benign channel for teens).

**Hudson & Moscoso Boedo (2026a), "The Collapse of Teen Fertility in the Digital Era"**
(SSRN 6676839; UC WP, April 2026)
- Terrain-ruggedness IV (Nunn–Puga) for county broadband/4G rollout → teen births
  2003–2018; parallel England & Wales design; cross-country event studies.
- Teen fertility −71% since 2007; fell first/fastest where high-speed mobile arrived
  earliest. Same instrument produces a teen-suicide surge.
- **Authors' own caveat: "Whatever the smartphone shock is doing to fertility, it is
  doing to teens. The entire 25+ population exhibits no detrended response."**
  US births 2007–2024: −71% (15–19), −43% (20–24), −23% (25–29), +9% (35–39).

**Hudson & Moscoso Boedo (2026b), "Wide and Shallow"** (UC WP, June 2026)
https://homepages.uc.edu/~moscoshn/Personal_webpage/papers/Wide_Shallow_web.pdf
- 10pp more long-run 4G infrastructure → 9.8pp larger decline in 15–19 birth rates
  (F=82); cohort-Bartik: full LTE saturation cuts cohort female ever-married by 0.34.
- Calibrated model: freezing phone prices at 2007 level accounts for 43% of the US
  children-per-adult decline (model counterfactual, not quasi-experimental).

**Contrast — fixed-line broadband (older lit, sign flips):**
- Guldi & Herbst 2017 (J Pop Econ): US county broadband 1999–2007 → teen births down,
  ≥13% of the teen-birth decline.
- Billari, Giuntella & Stella 2019 (Pop Studies): German DSL (Falck IV) → fertility UP
  for educated women 25+ (work-flexibility channel). Mobile = social displacement for
  the young; fixed-line = work tool for adults. Sign is mechanism-dependent.

**Public debate:** Burn-Murdoch FT May 2026 (phones as "accelerators, amplifiers,
internationalizers"); Alice Evans (ggd.world) — coupling-decline hypothesis, explicitly
"merely a hypothesis"; Reason critique (2026-05-18): early-4G areas urban/liberal
(selection), and the 25+ null means smartphones can't explain the (increasingly 25+)
baby bust.

## 2. What corroborates the achievement paper's H2

1. **Same shock, same timing, same age profile, independent outcome.** The causal
   fertility papers date the break at 2007-iPhone compounding through the 2010–2015
   4G wave — exactly the window before the 2013 NAEP peak-and-decline. Effects are
   monotonically declining in age and null for 25+ — matching our cohort decomposition
   (period effect in adolescence; cohorts arrived at G4 at record levels and lost
   ground in middle school).
2. **The fertility critics' strongest objection is our prediction.** "The effect is
   teen-specific" undermines smartphones-explain-the-baby-bust but is precisely what
   the achievement hypothesis requires — our outcome population is adolescents.
3. **Mechanism convergence:** ATUS time-diaries show teen in-person socializing roughly
   halved and digital leisure tripled (Hudson–Moscoso Boedo); Myers–Hooper find reduced
   in-person interaction. Matches our reading-for-fun collapse (27%→14%) and PISA
   distraction profile.
4. **Same instrument → teen suicide surge** links to the broadband→adolescent-mental-
   health rollout literature (Donati et al. JHE 2025 Italy: +0.08 SD mental-disorder
   prevalence for 1985–95 birth cohorts, null for older — an adolescent-exposure
   cohort effect, structurally identical to our decomposition).

## 3. Transferable designs (and whether they're taken)

- **3G × PISA (taken, cross-country): Jain & Stemper (Zurich WP 453, 2024)**
  https://ronak-jain.com/3G_Internet_and_PISA.pdf — Collins Bartholomew 3G shapefiles
  × 2.5M PISA scores, 82 countries: 3G arrival → −0.04 to −0.08 SD math/reading/science
  (~¼ school year), worst for girls and low-parental-education students. Lightning +
  legacy-2G IVs. Geography is coarse (291 country×urbanicity cells); no within-US analysis.
  **This is the closest existing paper to a causal smartphone→achievement estimate and
  belongs in the report's related work.**
- **US mobile rollout × test scores: OPEN.** Nobody has run 4G/LTE rollout against SEDA
  or NAEP. Existing US broadband×SEDA work (Caldarulo et al. 2023) uses fixed-line
  subscription rates, no instrument, finds small POSITIVE effects (homework channel).
  Wyckoff (EdWP 25-1197) states direct causal smartphone→achievement evidence is
  lacking — citable gap statement.
- **Feasible build:** 4G/LTE rollout 2010–2015 (FCC Form 477 mobile shapefiles Dec 2014+,
  free; Mosaik/American Roamer or Collins Bartholomew for pre-2014, proprietary) ×
  SEDA district scores 2009–2019; lightning-strike or terrain-ruggedness IV portable.
  Alternative: Myers–Hooper's AT&T-exclusivity coverage × early SEDA (2008-09+) —
  cleaner instrument (device access, not generic connectivity) but early timing.
- **Caveat to import:** fixed-line broadband coefficients on achievement are positive —
  connectivity bundles a homework channel with a distraction channel. The treatment
  must be MOBILE/device-specific (carrier exclusivity, 4G vs 2G, smartphone adoption),
  not "internet."
- **Datasets:** FCC Form 477 (mobile Dec 2014–2021; county fixed-line 2009–2024; ZIP
  provider counts to 1999, all free); NTIA Internet Use Survey (state-level smartphone
  items since 2011, free microdata); ACS S2801 (smartphone from 2016, county); ATUS;
  Monitoring the Future (social-media hours since ~2013; finer geography restricted);
  YRBS screen-time item (Churchill & Johnson NBER w34614 used it for mental health).

## 4. Rhetorical lessons from the "puzzle" genre

- **Kearney–Levine–Pardue (JEP 2022)** template (we already mirror it): document the
  break → long-differenced state-panel elimination of candidates (candidly "presumed
  exogeneity") → pivot from period to cohort → name the residual explanation and own
  its speculativeness ("the remainder of this section is thus speculative"). The
  authority comes from rigorous elimination, which buys license for the conjecture.
  They convert "you can't test it" into a claim about where the explanation must live
  (cohort-formative environment, not state-year policy).
- **Alice Evans's dual-criterion test:** any candidate must explain BOTH the global
  synchrony AND the local/compositional variation. Portable: our version is
  "must explain US + international + adult synchrony AND bottom-of-distribution
  concentration AND adolescent-period timing." Policy explanations fail criterion 1;
  COVID fails criterion 3 (pre-2019 onset).
- **The genre's payoff number** is a share-of-aggregate-decline-explained decomposition
  (Myers–Hooper 33–52%; Guldi–Herbst ≥13%), not a coefficient. A 4G×SEDA design could
  deliver the achievement analog.

## 5. Tension to acknowledge

The fertility literature's 25+ null sits beside our PIAAC adult-literacy decline.
Not contradictory — fertility is a behavior with strong age structure; skills can
erode at any age, and adult PIAAC declines are bottom-concentrated like the student
ones. But the report should not lean on the fertility lit for the adult-skills claim;
its corroboration is specifically about the adolescent margin.
