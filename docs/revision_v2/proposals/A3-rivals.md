# Proposal A3-rivals — rival hypotheses (D5) and age profile (D7)

*Agent A3. Phase 1, read-only. All new facts below were verified against live sources on 2026-07-02; exact values, URLs, and verification paths are in the VERIFIED FACTS and CLAIMS-AUDIT sections. No number already in the paper is altered by any edit.*

## Summary (3 sentences)

This proposal adds adolescent mental health as an honestly-assessed rival hypothesis (a ~235-word block at the end of H8, a scorecard row, two sentences in the Synthesis dual-criterion paragraph, and one Limitations sentence), with every new number verified against CDC YRBS and Mojtabai/Olfson/Han (2016, *Pediatrics*) primary sources. It dispatches the other reader-proposed candidates (rising immigration, political polarization) and signposts school-discipline reform to the set-asides section, in a new H8 intro paragraph that credits readers of an earlier draft. It adds the D7 age-profile paragraph to H2 reconciling adolescent concentration with the adult PIAAC decline (gradient, not cliff; the fertility literature's adult null concerns births, not skills), plus clause-level phrasing directives for the three co-owned passages that currently say "strikes whoever is an adolescent."

## Top-3 structural recommendations

1. **Keep all reader-response material inside H8** (intro dispatch paragraph + closing mental-health block) rather than in the bare Candidate Explanations enumerate, so it survives E's possible D9(a) merge. If E merges the Candidate Explanations section into Testing the Hypotheses, the dispatch paragraph travels with H8, not with the enumerate.
2. **The new scorecard row is identical to H2's row — present that as the finding, not a defect.** The six columns cannot separate digital media from the mental-health rival; the separation argument (ban studies with achievement outcomes, reading displacement, exposure gradients) lives off-table. Recommend P5 add a one-line table note saying so and pointing to §H8/Synthesis (I did not draft the note; table notes are P5's).
3. **Adopt gradient language paper-wide.** A2's "What the tests jointly imply" rewrite and A1's Conclusion + H2 Assessment calibration should replace "strikes whoever is an adolescent"/"adolescent-specific" with "concentrates among adolescents (with a weaker adult counterpart)" — exact suggested clauses in the D7 DIRECTIVES section below, so D7 does not live only in my new paragraph.

## Deliberately left alone

- **Line "If instead something in the post-2012 environment harms whoever is an adolescent at the time..." (§7.1 cohort design, line 306):** left as is. It states the discriminating logic of a grade-4-vs-grade-8 test, not a claim about the phenomenon's full age profile; softening it would blur the test. The adult margin is handled where the claim is substantive (new H2 paragraph, directives below).
- **"the same adolescent-specific period effect" inside the fertility paragraph (§6 H2, line 239):** accurate as a description of that literature's finding (fertility effects do vanish for adults); my new paragraph sits immediately after it and supplies the births-vs-skills reconciliation, so no change needed there.
- **The existing H8 enumerate item's omission of Common Core** (prose covers it; item doesn't): pre-existing inconsistency, flagged for P3/E; I only append mental health (EDIT A3-1) and do not otherwise rework the item.
- **School-discipline reform** gets a signpost only (per adjudication): it is already scoped in §sec:setaside; I do not add substance to it.

---

## Edits (document order)

### EDIT A3-1 [replace]
ANCHOR: `\item[H8.] \textbf{Other: teacher shortages, lowered expectations/grade inflation.}`
SECTION: Candidate Explanations (enumerate item H8)
PROPOSED:
```latex
\item[H8.] \textbf{Other: teacher shortages, lowered expectations/grade inflation, adolescent mental health.}
```
WHY: D5 — mental health becomes a named candidate within H8, so the new scorecard row and the Synthesis mention have a home in the candidate list.
RISK: collides:E (D9a may merge this section; the item text should travel unchanged).

### EDIT A3-2 [insert-after]
ANCHOR: `fixed-line broadband, a work tool for adults, if anything`
SECTION: §6 H2 (Smartphones and digital media), new paragraph after the fertility-corroboration paragraph, before the Verdict/Assessment line
PROPOSED:
```latex
\textbf{The age profile: a gradient, not a cliff.} The report's reliance on adolescent concentration may seem to sit awkwardly beside its use of the adult PIAAC decline as confirming evidence (Section~\ref{sec:adults}); the two are reconcilable, and the reconciliation is a prediction of the hypothesis rather than a patch to it. Exposure to the post-2012 digital environment is universal, but dose and developmental sensitivity are not: adolescents combine the heaviest and least-regulated use with the developmental window in which displaced reading, sleep, and attention compound into measured skill deficits. The hypothesis therefore predicts a gradient, not a cliff: effects largest among adolescents, present but weaker among adults. That is what the data show: the steepest collapse at age 13, record lows at grade 12, and a bottom-concentrated adult decline across nineteen OECD countries. The fertility literature's adult null is not a counterexample; it concerns births, not skills---PIAAC shows adult skills moved even where adult fertility did not. The 2025 LTT age split (9-year-olds recovering while 13-year-olds stagnate) fits the same gradient, since smartphone saturation at ages 11--14 far exceeds ages 5--9.
```
WHY: D7 — reconciles adolescent-specificity with the adult PIAAC decline; every fact restated here (age-13 collapse, grade-12 record lows, nineteen OECD countries, 2025 LTT age split, saturation ages 11--14 vs 5--9) already appears in the paper with its numbers unchanged.
RISK: collides:A4 (placement only — A4 inserts the mechanism taxonomy elsewhere in H2; reconciler orders the two insertions; no shared sentences).

### EDIT A3-3 [replace]
ANCHOR: `\subsection{H8: Other candidates}`
SECTION: §6 H8 heading
PROPOSED:
```latex
\subsection{H8: Other candidates}\label{sec:h8}
```
WHY: D5 — Synthesis (EDIT A3-7) and Limitations (EDIT A3-8) need a resolvable cross-reference to H8; no existing label is touched (`sec:h8` does not exist in the current file; verified by grep).
RISK: cross-ref (A3-5, A3-7, A3-8 reference `\ref{sec:h8}` and depend on this edit landing); collides:A1 only if A1 retitles H8 — any retitle must keep this label.

### EDIT A3-4 [insert-after]
ANCHOR: `\subsection{H8: Other candidates}`
SECTION: §6 H8, new intro paragraph (before the "Teacher shortages and quality" block)
PROPOSED:
```latex
Readers of an earlier draft pressed four candidates on this report: rising immigration, increasing political polarization, school-discipline reform, and deteriorating adolescent mental health---the last of which the report had treated only as an outcome of the device shock, not as a rival cause of the decline. The first three can be handled briefly. Rising immigration is a compositional story and fails the same arithmetic as H5: scores fell within every demographic group, reweighting bounds the compositional contribution at 1--2 points (Section~\ref{sec:h5}), and the decline appears in Catholic schools, across rich countries, and among adults. Political polarization names a real change in American life but supplies no articulated pathway to a decline that is bottom-concentrated, adolescent-specific, internationally synchronized, and present among adults; its intensity is also distinctly American, while the decline is not. School-discipline reform has the right timing and a bottom-concentrated prediction but no clean policy variation independent of the variables already examined; Section~\ref{sec:setaside} records it as untested rather than rejected. Adolescent mental health cannot be dispatched; it is taken up at the end of this section.
```
WHY: D5 dispatch sentences + adjudication ("make immigration and school discipline findable via signposting"), with the required clause crediting readers of a draft. The 1--2 point bound carries the paper's existing H5 number unchanged.
RISK: none (anchored on the same heading line as A3-3; A3-3's replacement keeps the anchor as a verbatim substring, so both edits apply in either order).

### EDIT A3-5 [insert-after]
ANCHOR: `direction of causality unclear`
SECTION: §6 H8, new closing block (after the "Lowered expectations and grade inflation" paragraph)
PROPOSED:
```latex
\textbf{Adolescent mental health.} The strongest reader-proposed candidate warrants a fuller assessment. Adolescent mental health deteriorated on nearly the same schedule as achievement. The share of high-school students reporting persistent sadness or hopelessness rose from 28\% in 2011 to 37\% in 2019 (before the pandemic) and 42\% in 2021 \citep{cdcyrbs2023}, retreating only to 40\% in 2023 \citep{cdcyrbs2024}; the twelve-month prevalence of major depressive episodes among adolescents rose from 8.7\% in 2005 to 11.3\% in 2014 (stable through 2011, rising thereafter), an increase concentrated at ages 12--20 \citep{mojtabai2016}. This candidate passes the screens that eliminate the school-policy hypotheses (right timing, international reach \citep{haidt2024}, adolescent concentration) and clears both bars of the dual-criterion test in Section~\ref{sec:synthesis}. Its fit is imperfect: the distress rise is steepest among girls, a concentration with no counterpart in the achievement data. But no test in this report eliminates it, and this report's data cannot separate it from H2: the rollout designs that link smartphone arrival to teen fertility also link it to worse adolescent mental health \citep{hudsonmoscoso2026}, and the Norwegian ban study finds that removing phones improves mental health and achievement together \citep{abrahamsson2024}. Distress may be a pathway from devices to disengagement, a joint product of the same shock, or an independent force for which devices are a covariate; the evidence assembled here cannot say which. \emph{Assessment: right timing, international, adolescent-specific; the strongest unresolved rival to the digital-media hypothesis, and not separable from it with this report's data.}
```
WHY: D5 — the new rival block (~235 words; charter asked ~200, flagged). All numbers are from the verified list below (URLs included); entanglement argument uses only existing keys (hudsonmoscoso2026, abrahamsson2024, haidt2024) as instructed; Assessment line written in D1/D2-compliant register from birth.
RISK: number-adjacent (adds new verified numbers; touches no existing number). Requires the three new bib entries below.

### EDIT A3-6 [insert-after]
ANCHOR: `H8 Teachers/inflation`
SECTION: §9 Synthesis, Table `tab:scorecard`
PROPOSED:
```latex
H8 Mental health       & \checkmark & $\sim$ & $\times$ & \checkmark & \checkmark & \checkmark \\
```
WHY: D5 — scorecard gains one row. Judgments justified below (SCORECARD JUSTIFICATION); the row is deliberately identical to H2's row, which is the honest headline: the table's six facts cannot separate the two, and the separation argument lives off-table.
RISK: collides:P5 (P5 owns scorecard table notes; the row itself is mine).

### EDIT A3-7 [replace]
ANCHOR: `A useful discipline can be borrowed from the parallel debate`
SECTION: §9 Synthesis, dual-criterion paragraph
PROPOSED:
```latex
A useful discipline can be borrowed from the parallel debate over collapsing birth rates, which shares this puzzle's structure---a synchronized post-2010 break across rich countries that resists every standard policy explanation \citep{kearneylevine2022,evans2024}: a candidate cause must clear two bars \emph{simultaneously}. It must explain the synchrony---the same decline appearing across countries with disparate school systems, funding trends, and accountability regimes, and among adults no school policy touches---and it must explain the local signature: bottom-of-distribution concentration, adolescent-period timing, sector neutrality. Every school-policy explanation fails the first bar by construction; the pandemic fails the second for phase one, having arrived six years late. Two candidates examined here clear both bars: digital media and the deterioration in adolescent mental health (Section~\ref{sec:h8}), rivals that the causal literature itself entangles and that differ mainly on whether devices are the cause or a covariate of the distress rise. The ban studies, in which removing devices improves achievement and mental health together, favor the first reading, but nothing in this report's evidence eliminates the second. With that framing, the evidence is not consistent with any single-cause account, but it is well organized by a two-phase model (Table~\ref{tab:scorecard}):
```
WHY: D5(c) — my substantive change is confined to replacing the single sentence "Digital media is the only candidate examined here that clears both." with the two new sentences ("Two candidates examined here clear both bars... eliminates the second."); every other sentence is verbatim from the current file so the reconciler can lift my two sentences into whichever merged version of this paragraph wins.
RISK: collides:A1+A2 (charter assigns this paragraph to A1+A2+A3, reconciler merges); cross-ref (uses `\ref{sec:h8}`, depends on A3-3).

### EDIT A3-8 [insert-after]
ANCHOR: `a 28\% U.S. response rate in 2023 and a change to tablet-only administration`
SECTION: §10 Limitations, new final one-sentence paragraph
PROPOSED:
```latex
The adolescent mental-health rival added in Section~\ref{sec:h8} is acknowledged rather than resolved: the rollout and ban literatures entangle the distress rise with the device shock in both directions, and nothing in this report's data identifies whether devices are cause, joint product, or mere covariate of deteriorating adolescent mental health.
```
WHY: D5 — Limitations gains one sentence.
RISK: collides:P6 (P6 restructures Limitations into thematic paragraphs; this sentence should be merged into whichever paragraph carries the digital-media caveats); cross-ref (uses `\ref{sec:h8}`, depends on A3-3).

---

## SCORECARD JUSTIFICATION (EDIT A3-6, column by column)

Columns: F1 Timing | F2 Bottom-heavy | F3 COVID drop | F4 No recovery | F5/F7 Within-group | F6 Intern'l. Legend: ✓ consistent, ~ partially consistent, × inconsistent or silent.

- **F1 Timing: ✓.** The adolescent MDE series is stable 2005–2011 and rises thereafter (8.7% in 2005 → 11.3% by 2014), an inflection at the achievement peak; YRBS persistent sadness rises 28→30→30→31→37 over 2011–2019, i.e., clearly pre-pandemic. Honest nuance (recorded here, not in the paper): the steepest YRBS rise is 2017–2019, later than the 2013 break — the onset aligns via the MDE series, the acceleration lags slightly.
- **F2 Bottom-heavy: ~.** A distress channel plausibly harms the least-resourced, least-regulated students most, but nothing in the trend data specifically predicts a flat-to-rising top decile, and the rise is broad-based. Matches H2's ~ on the same column (symmetric treatment).
- **F3 COVID drop: ×.** Same treatment as H2's ×: the 2019–2022 drop is causally attributed to schooling disruption (H1); the contemporaneous distress spike (37→42) is plausibly a product of the same shock, not an independent cause of the drop.
- **F4 No recovery: ✓.** Distress remains far above baseline after the pandemic (40% in 2023 vs 28% in 2011), consistent with the stalled bottom-of-distribution recovery.
- **F5/F7 Within-group: ✓.** The distress rise appears within every sex and racial/ethnic group YRBS reports (each group's trend marked "increased" 2011–2021), so it operates within groups like the decline does. The sex skew (girls 36→57 vs boys 21→29) is the residual tension, stated in the H8 block text.
- **F6 International: ✓.** The adolescent mental-health deterioration is international across rich countries, documented in the source the paper already cites for this literature (haidt2024).

The resulting row equals H2's row (✓ ~ × ✓ ✓ ✓). That identity is the point of the addition: the scorecard's facts cannot discriminate between devices-as-cause and devices-as-covariate; the discrimination rests on evidence outside the table (ban studies with achievement outcomes, the reading-practice collapse, exposure gradients), which is what the H8 block, the Synthesis sentences, and the Limitations sentence say.

## VERIFIED FACTS (web-verified 2026-07-02; do not alter values)

| # | Fact | Exact value(s) | Source (live URL) | How verified |
|---|---|---|---|---|
| V1 | YRBS, % of U.S. high-school students who experienced persistent feelings of sadness or hopelessness, all students | 2011: 28; 2013: 30; 2015: 30; 2017: 31; 2019: 37; 2021: 42 | https://www.cdc.gov/yrbs/dstr/pdf/YRBS_Data-Summary-Trends_Report2023_508.pdf (CDC, YRBS Data Summary & Trends Report 2011–2021) | PDF fetched 2026-07-02; trend table, "Mental Health and Suicidality" chapter (printed p. 58): row "Experienced persistent feelings of sadness or hopelessness" reads 28 30 30 31 37 42 |
| V2 | Same indicator, by sex, 2011→2021 | Female 36%→57%; Male 21%→29% | Same PDF, by-sex trend chart (printed p. 61) | Values extracted from the fetched PDF text; supports "steepest among girls" clause |
| V3 | Same indicator, 2023 | 40% (down from 42% in 2021) | https://www.cdc.gov/yrbs/results/2023-yrbs-results.html | Page fetched 2026-07-02: "persistent feelings of sadness or hopelessness (42% to 40%)" 2021→2023 |
| V4 | Adolescent (12–17) 12-month major depressive episode prevalence | 8.7% (2005) → 11.3% (2014); increase "larger and statistically significant only in the age range of 12 to 20 years"; young adults 8.8%→9.6% | https://pubmed.ncbi.nlm.nih.gov/27940701/ ; DOI https://doi.org/10.1542/peds.2016-1878 (Mojtabai, Olfson & Han 2016, *Pediatrics* 138(6): e20161878) | Abstract fetched 2026-07-02; both prevalence values and the age-concentration statement confirmed |
| V5 | Timing of the MDE inflection | "In adolescents, the prevalence of 12-month MDE was stable over the 2005 to 2011 period; however, it gradually increased in later years." Young-adult rise limited to ages 18–20, negligible at 21–25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5127071/ (full text) | Full text fetched 2026-07-02; sentence quoted verbatim |

Nothing I attempted to verify failed verification; no fact was excluded for verification failure. (One candidate fact I chose not to use: CDC's "nearly 60%" characterization of the decade increase for girls — redundant given V2's exact values.)

## BIBTEX ENTRIES (add to refs.bib)

Formatted to match the file's existing conventions (institutional authors in double braces; URLs in `note` for reports/web pages). The `note` in mojtabai2016 may be stripped by the reconciler for style consistency with other @article entries; the URL + access date is preserved here and in the claims audit regardless.

```bibtex
@techreport{cdcyrbs2023,
  author      = {{Centers for Disease Control and Prevention}},
  title       = {Youth Risk Behavior Survey Data Summary \& Trends Report: 2011--2021},
  institution = {U.S. Department of Health and Human Services},
  year        = {2023},
  note        = {\url{https://www.cdc.gov/yrbs/dstr/pdf/YRBS_Data-Summary-Trends_Report2023_508.pdf}, accessed July 2, 2026}
}

@article{mojtabai2016,
  author  = {Mojtabai, Ramin and Olfson, Mark and Han, Beth},
  title   = {National Trends in the Prevalence and Treatment of Depression in Adolescents and Young Adults},
  journal = {Pediatrics},
  year    = {2016},
  volume  = {138},
  number  = {6},
  pages   = {e20161878},
  note    = {\url{https://doi.org/10.1542/peds.2016-1878}, accessed July 2, 2026}
}

@misc{cdcyrbs2024,
  author = {{Centers for Disease Control and Prevention}},
  title  = {2023 Youth Risk Behavior Survey Results},
  year   = {2024},
  note   = {\url{https://www.cdc.gov/yrbs/results/2023-yrbs-results.html}, accessed July 2, 2026}
}
```

The third entry (cdcyrbs2024) goes beyond the charter's two suggested keys; it supports only the "retreating only to 40\% in 2023" clause in EDIT A3-5, which in turn supports the F4 ✓ in the scorecard. If the reconciler wants to hold new references to two, cut that clause and the entry together — and then downgrade F4 in EDIT A3-6 to ~, since the in-paper support for "no recovery" would end at 2021.

## CLAIMS-AUDIT ROWS (drafts; type CITATION; renumber as the reconciler sees fit)

For `evidence/claims_audit.md`, section B (hypothesis tests). My edits shift no section numbers, so existing location keys are untouched.

| # | Claim (report location) | Value | Type | Producing script / source | 5-minute verification path |
|---|---|---|---|---|---|
| B15 | YRBS: high-school students with persistent sadness/hopelessness 28% (2011) → 37% (2019) → 42% (2021), 40% (2023); rise steepest among girls (§6 H8) | 28/37/42; 40 | CITATION | CDC YRBS Data Summary & Trends Report 2011–2021; CDC 2023 YRBS results page | Open https://www.cdc.gov/yrbs/dstr/pdf/YRBS_Data-Summary-Trends_Report2023_508.pdf, "Mental Health and Suicidality" trend table (printed p. 58): row reads 28, 30, 30, 31, 37, 42 for 2011–2021 (by-sex chart, printed p. 61: female 36→57, male 21→29); then https://www.cdc.gov/yrbs/results/2023-yrbs-results.html for the 2023 value (40%) |
| B16 | Mojtabai, Olfson & Han (2016): adolescent (12–17) 12-month MDE prevalence rose 8.7% (2005) → 11.3% (2014), stable through 2011, increase concentrated at ages 12–20 (§6 H8) | 8.7 → 11.3 | CITATION | Mojtabai, Olfson & Han, *Pediatrics* 138(6): e20161878 | Read the abstract at https://pubmed.ncbi.nlm.nih.gov/27940701/ (Results: both values; age concentration). For the stable-through-2011 clause: https://pmc.ncbi.nlm.nih.gov/articles/PMC5127071/, Results, first paragraph |

## D7 DIRECTIVES for co-owned passages (suggested clauses, strictly stylistic; owners decide)

1. **To A2** — §7.6 "What the tests jointly imply" (current line begins "These tests were designed so the leading phase-one hypotheses..."): in the D4 rewrite, replace the clause "(i) strikes whoever is an adolescent after $\sim$2012 regardless of how the cohort looked at age 9" with "(i) concentrates among adolescents after $\sim$2012 regardless of how the cohort looked at age 9 (with a weaker adult echo in PIAAC; Section~\ref{sec:adults})". RISK: collides:A2.
2. **To A1** — Conclusion (current line begins "The decline in American student achievement is real, large..."): replace "the losses strike whoever is an adolescent after that date (not particular cohorts)" with "the losses concentrate among adolescents after that date (not particular cohorts), with a weaker counterpart among adults". RISK: collides:A1.
3. **To A1** — H2 Verdict→Assessment line (current line begins "\textbf{Verdict.} \emph{Strongly supported as a major driver..."): in recalibrating, prefer "adolescent-concentrated, 2007-onset shock" over "adolescent-specific, 2007-onset shock", consistent with the new gradient paragraph (EDIT A3-2). RISK: collides:A1.
4. **To A1 (optional)** — if the abstract rewrite keeps a mental-health mention, the calibrated formula consistent with my edits is: "adolescent mental health, which deteriorated on the same schedule, is the strongest unresolved rival and is not separable from the device account with these data."

## Length accounting

New text across all edits: roughly 660 words (~0.75 compiled page): dispatch ~185, mental-health block ~235, age-profile ~185, synthesis +30 net, limitations ~50, plus one table row. Within my share of the ≤2-page budget; the redundancy harvest assigned to other agents is unaffected.
