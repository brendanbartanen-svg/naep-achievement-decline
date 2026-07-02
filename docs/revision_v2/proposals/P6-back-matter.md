# P6-back-matter — proposal (lines 474–499: Limitations, Verification, Conclusion)

*Agent P6-back-matter, 2026-07-02. Read-only phase; no repo file touched except this proposal.*

## Summary

This proposal restructures the ~500-word monolithic Limitations paragraph into four thematic paragraphs with topic sentences (inferential status; data and measurement; design caveats for the report's own tests; digital-media evidence caveats), preserving every caveat and number exactly and preserving verbatim the substring that A3's EDIT A3-8 anchors on, with a marked placeholder for A3's mental-health sentence at its merge point. It gives Verification a light D8 pass (two paragraphs split for sentence length and em-dash removal, two edits that incorporate A1-27's and A4-10's substantive word changes verbatim so style and substance land in one edit each). It offers a P6 variant of A1-28's Conclusion that keeps every A1 calibration sentence word-for-word but applies the D9c shrink: the five-item evidence chain (triple-stated in §jointly, Synthesis, and Conclusion) is replaced by a one-clause pointer to Section~\ref{sec:synthesis}, cutting the Conclusion from ~230 to ~205 words while the Limitations edit nets slightly negative, so the back matter contributes savings to the length budget.

## Top-3 structural recommendations

1. **D9(c) implications home.** The Synthesis "Three implications follow" paragraph (line 472, P5's) and the Conclusion overlap. Recommended division: Synthesis keeps the ranking *and* the three implications; the Conclusion stays the compact coda proposed in P6-5 (headline facts, calibrated ranking pointer, absenteeism lock-in, policy landing). If E instead moves the implications paragraph into the Conclusion, use P6-5 as the base and append that paragraph after its fourth sentence; do not leave the implications stated in both places. (Coordinate with P5 and E.)
2. **Apply-order within lines 474–499.** Apply P6-1 (Limitations restructure) *before* A3-8: A3-8's insert-after anchor (`a 28\% U.S. response rate in 2023 and a change to tablet-only administration`) survives verbatim inside P6-1's fourth paragraph, so A3's sentence lands exactly at the digital-media caveats paragraph, and per A3's own RISK note it should be merged as that paragraph's final sentence (placeholder comment marks the spot). For the three paragraph-level collisions, pick exactly one of each pair: {A1-27, P6-3}, {A1-28, P6-5}, and apply P6-4 (which subsumes A4-10, making A4-10 a no-op).
3. **Limitations/§jointly echo (D4).** P6-1's design-caveats paragraph states the shared blind spot of the two timing designs ("a nationally synchronized change ... absorbed in year effects") in clause structure that echoes A2's §jointly rewrite ("a nationally synchronized channel that year effects absorb"). Reconciler should keep the two phrasings aligned if A2's final wording shifts; A2's proposal explicitly defers the Limitations restatement to P6.

## Deliberately left alone

- **Verification: Claims-audit (line 483), Assertion-suite (line 485), External-anchoring (line 489) paragraphs.** Each already has a topic-sentence run-in, at most one em-dash (within the D8 budget), no sentences whose length isn't doing list work, and dense frozen numbers (42/13/3/26 claims, 71 assertions, table 222.32a-adjacent material). Risk-minimizing to not touch.
- **Section headings** `\section{Limitations}`, `\section{Verification}` + `\label{sec:verification}`, `\section{Conclusion}`: unchanged; no labels exist in my range besides `sec:verification`, which survives untouched.
- **D1/D6 occurrences in my range** are all handled inside the paragraph edits below ("every published verdict" via A1-27's wording in P6-3; colloquial "mechanism" via A4-10's wording in P6-4); no global-substitute needed from P6.

## Collision map (for the reconciler)

| Line | Sibling edit | Relation to P6 edit |
|---|---|---|
| 476 | A3-8 [insert-after] | P6-1 preserves A3-8's anchor verbatim in paragraph 4 and marks the merge point |
| 487 | A1-27 [replace] | P6-3 = A1-27's rename ("every conclusion published here") + D8 sentence splits; apply one, not both |
| 491 | A4-10 [global-substitute] | P6-4 incorporates A4-10's replacement text verbatim; if P6-4 lands, A4-10 no-ops |
| 495 | A1-28 [replace] | P6-5 = A1-28 with the D9(c) shrink; every calibration sentence is A1's verbatim; apply one, not both |

---

## Edits (document order)

### EDIT P6-back-matter-1 [replace]
ANCHOR: This analysis is observational. The hypothesis tests rest on timing
SECTION: Limitations (the single monolithic paragraph, replaced by four paragraphs)
PROPOSED:
```latex
This analysis is observational. The hypothesis tests rest on timing, distributional incidence, and cross-sectional comparisons, not experimental variation. Several causes plausibly interact (absenteeism is partly downstream of screens and of weakened school engagement), so the phase shares above are accounting decompositions, not causal attributions.

The data series themselves carry known measurement caveats. NAEP percentile statistics for the oldest years use no-accommodation samples; the NSLP-eligibility series ends in 2022 and is affected by community-eligibility expansion; PISA OECD averages shift membership across cycles; and PIAAC cross-cycle comparisons involve assessment changes and should be read as NCES advises. The LTT format changed in 2004 (results are bridged). The 2025 LTT wave is reported from Data Service point estimates whose standard errors are not yet published in the Digest, so significance language for 2023$\rightarrow$2025 changes follows the NCES release. Measurement artifacts, by contrast, can be largely ruled out as an explanation of the decline itself: NAEP exclusion rates were flat at 1--3\% of all students from 2013 through 2024 even as SD/EL identification rose; student participation was identical in 2022 and 2024 (92\% at grade 4, 89\% at grade 8); and public-school participation was complete. Neither rising exclusion nor falling participation can explain the declines; grade 12, with 68\% student participation in 2024, is the exception and is treated cautiously.

The report's own tests (Sections~\ref{sec:sharper} and~\ref{sec:mechanism}) carry design caveats. In the waiver analysis, the never-waiver comparison group is seven states, so inference uses randomization rather than cluster asymptotics and the minimum-detectable-effect calculation bounds what the null can claim; pre-2011 trend differences are visible ($p=0.08$ jointly); and waivers capture only the formal step of deregulation. The 4G-rollout test is informative only about local arrival timing and has imperfect pre-trends. Neither timing design can see a nationally synchronized change: a national accountability climate and a national adoption wave alike are absorbed in year effects. Catholic-school samples are small and selected, so only their trends, not their levels, are informative, and only the reading trends are estimated precisely enough to discriminate. The schooling-mode state regressions are aggregation-limited: state-level treatment variance is a fraction of district-level variance, and three states lack schooling-mode data. NAEP's absence item covers only the month before the assessment, and the Kitagawa decomposition treats absence as exogenous when it partly proxies disengagement.

Finally, the digital-media evidence is a composite, and each component carries limits of its own. The PISA distraction and screen-time gradients are cross-sectional associations: low performance may drive device retreat as well as the reverse, and the leisure-hours items were not administered to U.S. students. The quasi-experimental ban literature is small, though consistent. The rollout-based causal designs concern outcomes that are either non-U.S. test scores or non-achievement domains (fertility, mental health). The causal magnitudes at the population scale of the U.S. decline therefore remain uncertain, and the adult PIAAC comparison carries its own caveats beyond the cross-cycle caution noted above: a 28\% U.S. response rate in 2023 and a change to tablet-only administration. % [PLACEHOLDER (D5/A3): EDIT A3-8's mental-health-rival sentence merges here as this paragraph's final sentence, per A3's own RISK note; delete this comment when it lands.]
```
WHY: P6 mandate + D8 — the monolithic paragraph becomes four topic-sentenced thematic paragraphs (inferential status; data/measurement; own-test design; digital-media evidence) with every caveat and number carried through exactly and em-dashes cut from six to zero; the joint blind-spot sentence restates existing text from §sec:waiver and §sec:fourg symmetrically per D4.
RISK: number-adjacent (18 frozen values carried through verbatim); collides:A3 (A3-8's anchor string preserved verbatim in paragraph 4; placeholder marks its merge point); collides:A2 (the nationally-synchronized-change sentence should track A2's final §jointly phrasing); cross-ref (keeps \ref{sec:sharper} and \ref{sec:mechanism}; drops one redundant \ref{sec:fourg}, which remains referenced at lines 49, 239, 372, 489)

### EDIT P6-back-matter-2 [replace]
ANCHOR: a division of labor that raises a legitimate reliability question
SECTION: Verification (opening paragraph)
PROPOSED:
```latex
This report was produced by a language-model agent (Claude Fable 5) directed and verified by the author. That division of labor raises a legitimate reliability question: the volume of data work involved (dozens of API pulls, fourteen analysis scripts, hand-coded policy datasets, two-gigabyte microdata files) exceeds what any reader, including the author, can efficiently audit line by line. Rather than asking for trust, the project carries a layered verification record, all of it in the public repository alongside the code and data (\url{https://github.com/brendanbartanen-svg/naep-achievement-decline}).
```
WHY: D8 — splits a 62-word opening sentence and converts the em-dash pair to parentheses; clarity only, content unchanged.
RISK: none

### EDIT P6-back-matter-3 [replace]
ANCHOR: The five computed results judged most error-prone
SECTION: Verification, blind clean-room replication paragraph
PROPOSED:
```latex
\textbf{Blind clean-room replication.} The five computed results judged most error-prone were independently re-derived by separate agents that were denied access to this project's analysis code, results files, and text, and instructed not to search for the answers. Each re-pulled the data from the NCES API or read the raw PISA files directly. All five reproduce. The cohort decomposition matched to the decimal ($-4.45 = +1.57 - 6.02$ against the published $-4.4 = +1.6 - 6.0$). The PISA distraction estimate matched exactly for the U.S. ($-13.25$ vs.\ $-13.2$), and the replicating agent independently recovered the counterintuitive item coding (1 = ``every lesson'') from the file's own metadata, precisely the step where a sign error is most likely. The Kitagawa inputs matched to the decimal, and the decomposition shares fell inside the published bands. The Catholic-sector changes matched exactly, with NAEP's official significance tests agreeing with every conclusion published here. The waiver analysis reproduced the null and the informative MDE while showing that the near-zero point estimate is window- and pooling-dependent, which is why it is reported as $\approx$0 rather than as a precise value. No pipeline errors were found; every divergence traced to a documented convention choice (weighting, window, or standard-error construction). The full comparison is in \texttt{verification/cleanroom/COMPARISON.md}.
```
WHY: D8 — the ~120-word five-result semicolon chain becomes five parallel sentences and both em-dashes go; adopts A1-27's D1 rename ("every published verdict" → "every conclusion published here") verbatim so one edit carries substance and style.
RISK: number-adjacent (all replication figures carried unchanged); collides:A1 (variant of A1-27 — apply exactly one of the two; this version is A1-27 plus the D8 splits)

### EDIT P6-back-matter-4 [replace]
ANCHOR: The components that machine verification cannot reach
SECTION: Verification, human-verification paragraph
PROPOSED:
```latex
\textbf{Human verification.} The components that machine verification cannot reach were checked by the author. The four hand-coded policy datasets (waiver dates, phone-ban statutes, Common Core adoption status, and the TUDA--CSDH crosswalk) were spot-checked against primary documents, with attention to the rows where a coding error would change treatment assignment; the five headline NAEP numbers were re-pulled manually from the Data Explorer; and the Synthesis section was reviewed adversarially by an independent colleague. The residual risks are stated rather than hidden: the interpretive weighting of Section~\ref{sec:synthesis} is a judgment no audit can certify, and the pre-registered NAEP 2026 phone-ban test is how the project lets future data discipline it.
```
WHY: D8 clarity (topic sentence split off; "remaining residual" de-duplicated) and D6 terminology discipline via A4-10's exact replacement ("is how the project lets future data discipline it"), incorporated verbatim so A4-10 becomes a no-op.
RISK: collides:A4 (subsumes A4-10; apply this and drop A4-10, or vice versa); cross-ref (keeps \ref{sec:synthesis})

### EDIT P6-back-matter-5 [replace]
ANCHOR: The decline in American student achievement is real, large, and verifiable
SECTION: Conclusion
PROPOSED:
```latex
The decline in American student achievement is real, large, and verifiable from primary data: roughly one grade level of learning lost at grade 8 since 2013, the lowest grade 8 reading scores ever recorded, and the widest achievement gaps in NAEP's history. It happened in two phases with different causes. For the pre-pandemic erosion, nearly invisible in averages because it was confined to the bottom of the distribution, the best-supported remaining candidate is the post-2012 saturation of adolescent life by smartphones and digital media; the full case is assembled in Section~\ref{sec:synthesis}. That conclusion is a ranking by consistency with the evidence, not a causal estimate; the pre-registered state phone-ban test against NAEP 2026 is the next opportunity to corroborate or overturn it, and adolescent mental-health deterioration remains an entangled rival these data cannot separate. The retreat from test-based accountability likely contributed at the margins, most visibly at the public-school grade 4 bottom decile, but failed the direct tests this report could put to it. The pandemic then imposed the largest schooling shock in modern history, whose effects, far from fading, have been locked in by chronic absenteeism that remains half again its pre-pandemic level. Funding cuts, demographic change, and teacher shortages are, on the evidence, second-order. The policy conclusion is uncomfortable but clear: returning to 2019 practices would only return the country to a trajectory that was already pointing down.
```
WHY: D9(c) — Conclusion shrinks toward implications: the five-item evidence chain (stated again in §jointly line 383 and Synthesis line 468) becomes a one-clause pointer to \ref{sec:synthesis}, which also removes the Conclusion instance of "strikes whoever is an adolescent" flagged under D7; every calibration sentence (banned-phrase fix, ranking-not-causal-estimate, pending-2026, mental-health rival) is A1-28's wording verbatim, since calibration here is A1's.
RISK: collides:A1 (variant of A1-28 — apply exactly one of the two; the only delta is the D9(c) cut); collides:A3 (mental-health clause, carried from A1-28 unchanged); collides:E/P5 (if E moves the Synthesis implications paragraph here, use this as the base and append it); number-adjacent (dropped clause's content — Catholic schools, NCLB release, rich-world recurrence, halving of voluntary reading — all appears verbatim-equivalent elsewhere per non-negotiable 1a)
