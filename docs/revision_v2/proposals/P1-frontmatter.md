# P1-frontmatter proposal — preamble, title/date, disclosure, introduction, Related Work, Data (report.tex lines 1–70)

## Summary

This proposal executes D10 exactly (version stamp to v2.0 / July 2, 2026, and the disclosure sentence, with the disclosure paragraph rewritten whole for D8 compliance), splits the introduction's purpose-plus-finding paragraph in two, and adds the D9(d) end-of-introduction roadmap that also pre-announces the D4 symmetric design standard. It breaks the Related Work mega-paragraph (line 49) into three topic-sentence paragraphs, removes its running-prose "verdict" per D1, and consolidates the Bleiberg waiver material from the closing paragraph into the *First* (waiver) contribution paragraph so the section closes on the integrative device alone. The two Data paragraphs I touch are sentence-split only; every number, citation key, quotation, label, and `\ref` in lines 1–70 is carried through verbatim.

## Top-3 structural recommendations

1. **A1's D3 inferential-strategy paragraph should REPLACE the current third introduction paragraph** (line 44, "The analysis is descriptive and abductive rather than causal in the experimental sense: ...") in place — same slot, third paragraph of the introduction — rather than be added alongside it. The existing paragraph is a compressed draft of exactly what D3 specifies; keeping both would state "consistency is a screen, not proof" twice. A1's draft must preserve the existing paragraph's operational device (each hypothesis generates predictions on the five evidence dimensions and is scored against all five), since the abstract, §Testing, and the scorecard all lean on it. No further connective tissue is needed in that slot: my split paragraph 2b ends on "...that any complete explanation must fit," which hands off naturally to a how-we-infer paragraph.
2. **Adopt the end-of-introduction roadmap (EDIT P1-frontmatter-5, per D9d).** It is phrased section-count-agnostically ("The report then states the candidate explanations and tests each against those facts") so it survives the possible D9(a) merge of Candidate Explanations into Testing the Hypotheses, and it contains the one-clause promise of the symmetric design standard that D9(e) wants a reader to meet before §sec:sharper.
3. **Apply EDITs P1-frontmatter-7 and -8 as a pair (both or neither).** They move the Bleiberg 2020/2026 waiver-precedent material from the section-closing paragraph into the *First* (waiver) contribution paragraph. Applied singly, bleiberg2020/bleiberg2026 would either duplicate or vanish from Related Work. (§sec:waiver's own one-line Bleiberg mention at line 338 is A2's and is unaffected.)

## Flags for other agents (no edits proposed here)

- **Abstract (A1 owns; flagged only).** (i) ~430 words vs the D8 ceiling of 300. (ii) Running-prose "verdict": "Three further discriminating tests sharpen the verdict on phase one" (D1). (iii) D2-banned "uniquely predicts" ("which uniquely predicts an adolescent-led, sector-neutral, geographically uniform, international decline extending to adults") — soften to "is the only candidate examined here that predicts." (iv) "leave ... smartphones and digital media---...---as the explanation most consistent with the full pattern of evidence" is the exact construction the critique quotes; needs T5 ladder language ("best-supported remaining candidate ... pending the pre-registered 2026 test"). (v) "Together these results weaken every school-policy hypothesis" should say which form is weakened (the strong local forms; D4). (vi) Two 60–70-word sentences and roughly ten em dashes. (vii) After D5, the abstract needs one clause acknowledging the adolescent mental-health rival that also clears the dual-criterion screen (A1+A3 coordinate).
- **Intro count sync (A3).** My paragraph 2a retains the current "eight candidate explanations." Under D5 mental health lives inside H8 and the count stays eight; if A3's implementation instead changes the enumeration, this phrase (and the abstract's "eight") must be synced.
- **Reconciler.** EDIT P1-frontmatter-5's anchor sits on line 44, which structural rec 1 recommends A1 replace. If A1's replacement is adopted, re-anchor the roadmap insert to follow A1's final paragraph text (same position: last paragraph of the introduction).

## Deliberately left alone

- **Preamble (lines 1–15), title, author (17–20):** compile-critical, no new packages allowed, and the title/subtitle describes the exercise without pre-announcing the winner — no D1 issue.
- **Introduction paragraph 1 (line 40):** already D8-compliant (short sentences, no em dashes, earned intensity); rewriting it would be churn.
- **Line 44:** skipped, not styled — A1 owns its replacement (D3); see structural rec 1.
- **Line 51 and the *Second*/*Third* contribution paragraphs (lines 55, 57):** each is within the em-dash budget (≤1) and their long sentences are inventories doing real work.
- **Data paragraphs "International assessments" and "Contextual evidence" (lines 67, 69):** already compliant.
- **The em dash in the date stamp ("July 2, 2026 --- Version 2.0"):** retained deliberately; it is a title-page separator, not prose, and matches the v1.9 stamp's typography.

## Edit-pairing notes for the reconciler

- P1-frontmatter-1 and -2 jointly replace the two physical lines of the `\date{...}` construct; apply both or neither (brace structure spans the pair).
- P1-frontmatter-7 and -8: apply both or neither (see structural rec 3).
- P1-frontmatter-4 replaces one physical line with two paragraph lines (blank line between); P1-frontmatter-6 replaces one physical line with three paragraph lines.

---

### EDIT P1-frontmatter-1 [replace]
ANCHOR: \date{{\normalsize June 12, 2026 --- Version 1.9\\[1pt]
SECTION: Title page (\date, first physical line of the two-line construct)
PROPOSED: \date{{\normalsize July 2, 2026 --- Version 2.0\\[1pt]
WHY: D10 version stamp: v2.0, July 2, 2026.
RISK: number-adjacent

### EDIT P1-frontmatter-2 [replace]
ANCHOR: First version: June 9, 2026 (v1.0). This version incorporates
SECTION: Title page (\date, second physical line of the two-line construct)
PROPOSED: {\small First version: June 9, 2026 (v1.0); v1.9 (June 12, 2026) incorporated the NAEP Long-Term Trend results for 2025\\ released June 10, 2026; v2.0 responds to a written external review, with no changes to analyses, estimates, or data.\\ Version history: GitHub releases v1.0--v2.0 at \url{github.com/brendanbartanen-svg/naep-achievement-decline}.}}}
WHY: D10: the version note now attributes the LTT incorporation to v1.9 (no longer "this version") and states what v2.0 is; release range updated to v1.0--v2.0. All prior dates retained; closing brace structure identical to the original line.
RISK: number-adjacent

### EDIT P1-frontmatter-3 [replace]
ANCHOR: \small\noindent\textbf{How this report was produced.}
SECTION: Title page disclosure minipage ("How this report was produced")
PROPOSED: \small\noindent\textbf{How this report was produced.} This document is an experiment in AI-conducted research, and the division of labor behind it is unusual enough to state plainly rather than leave to a byline. The research and the text were produced by Claude (Fable 5), an AI model from Anthropic, over a series of interactive sessions in June 2026. The model pulled all data from federal APIs and survey microdata files, wrote and ran every analysis script, produced every figure, and drafted every sentence of this document, including this paragraph and the Limitations and Verification sections. The listed author directed and verified rather than executed: posing the initial question, choosing which directions to pursue and when to stop, supplying occasional leads from outside the sessions (most recently the June 2026 release of the 2025 Long-Term Trend results, incorporated in v1.9), carrying out the human verification steps recorded in the repository, and deciding what was release-ready. The author wrote none of the code and none of the prose. The byline follows the scholarly convention that reserves authorship for the human who takes responsibility for the work and asks that AI involvement be disclosed rather than credited; this paragraph is that disclosure. Version 2.0 (July 2026) responds to a written external review with claim-strength calibration, symmetric treatment of the report's two null designs (waiver timing and 4G rollout), an added rival-hypothesis analysis (adolescent mental health), and a full organizational and line-level edit, carried out under the same division of labor; no analyses, estimates, or data changed. No human has line-edited the text or re-derived the full analysis. In place of that, the project carries the layered verification record described in Section~\ref{sec:verification}: a typed audit of every load-bearing claim with a human-executable check, an assertion suite frozen against the published numbers, blind replications of the riskiest results by independent AI agents denied access to this project's code, external anchoring to published estimates, and the author's spot-checks of the hand-coded datasets and headline numbers at the scopes recorded in the repository. The repository is public, with code, data extracts, evidence files, and version history, at \url{https://github.com/brendanbartanen-svg/naep-achievement-decline}. Readers should weigh the report as what it is: machine-produced analysis with documented provenance, verified at the stated scopes and no further.
WHY: D10 disclosure sentence added (near-verbatim charter text, placed after the byline-convention sentence and before "No human has line-edited," with "carried out under the same division of labor" keeping the no-line-edit claim coherent); whole-paragraph D8 pass removes all three em-dash pairs and splits the three 60–90-word sentences while preserving every factual element, the URL, and \ref{sec:verification}. "June 2026" retained for original production; the new sentence carries the July 2026 date.
RISK: number-adjacent

### EDIT P1-frontmatter-4 [replace]
ANCHOR: This report does two things.
SECTION: Introduction, second paragraph (splits into two paragraphs)
PROPOSED: This report does two things. First, it \emph{verifies} the decline directly from primary data, pulling national, state, percentile, and subgroup statistics from the NCES NAEP Data Service API rather than relying on secondary summaries \citep{naepapi}. Second, it \emph{tests} eight candidate explanations against five kinds of evidence: (i) the timing of the decline; (ii) its distribution across the achievement spectrum; (iii) its incidence across demographic subgroups; (iv) its geography across states; and (v) its presence or absence in other countries.

Most public discussion attributes the decline to the COVID-19 pandemic. A central finding of this report is that the pandemic explanation, while clearly correct for the 2019--2022 drop, is incomplete. Between a quarter and three-quarters of the total decline, depending on grade and subject, either predates March 2020 or postdates the return to in-person schooling. The pre-pandemic phase also has a distinctive signature that any complete explanation must fit: losses concentrated almost entirely among low performers.
WHY: D8: the paragraph did two jobs (statement of purpose; headline finding) — split with topic sentences, the 70-word closing sentence broken in two, and the em-dash pair converted to a colon. All numbers and \citep{naepapi} carried verbatim.
RISK: none

### EDIT P1-frontmatter-5 [insert-after]
ANCHOR: Hypotheses that fit one fact but contradict another are weighed accordingly.
SECTION: Introduction, new final paragraph (roadmap)
PROPOSED: The report proceeds as follows. Section~\ref{sec:related} situates the contribution. Section~\ref{sec:verify} establishes the facts to be explained, culminating in a list (F1--F8) that any candidate explanation must fit. The report then states the candidate explanations and tests each against those facts. Section~\ref{sec:sharper} reports discriminating tests built on cohort, sector, and policy- and technology-rollout timing, holding the accountability and digital-media hypotheses to the same design standard. Section~\ref{sec:mechanism} examines schooling mode and attendance directly. Section~\ref{sec:synthesis} assembles the resulting ranking of explanations, and the report closes with limitations, the verification record (Section~\ref{sec:verification}), and implications.
WHY: D9(d) roadmap; the "same design standard" clause delivers D9(e)'s promise of D4 symmetry at first mention. Phrased to survive the D9(a) merge; all five \ref labels verified present. If A1 replaces the anchor paragraph (structural rec 1), re-anchor this insert to follow A1's final paragraph.
RISK: collides:E

### EDIT P1-frontmatter-6 [replace]
ANCHOR: The decline itself is well documented.
SECTION: Related Work and Contribution, opening paragraph (splits into three paragraphs)
PROPOSED: The decline itself is well documented. NCES's own releases established the 2012--2013 peak and the concentration of losses among low performers. \citet{malkus2025theories} assembles percentile trends across 21 assessments and distills four facts any explanation must fit: a $\sim$2013 onset, bottom-half concentration, internationally outsized U.S. gap growth, and parallel declines among \emph{adults} on PIAAC. Section~\ref{sec:adults} incorporates that last fact and sharpens it with the 2023 Cycle 2 results. \citet{wyckoff2025} documents the same patterns at the state level, and the Education Recovery Scorecard project has traced the pandemic shock and recovery at district scale \citep{kane2024,kane2025,dewey2026}.

The hypothesis-weighing genre is likewise established. \citet{malkus2025theories} and \citet{wyckoff2025} evaluate candidate explanations narratively against descriptive patterns, and the conclusions this report reaches on the COVID and absenteeism hypotheses rest on existing causal work \citep{goldhaber2023,jack2023,cea2023,dee2024}. The weak state-level correlation between pandemic schooling mode and NAEP changes was noted on release day in 2022 (by Chalkbeat's analysis and by the NCES commissioner; \citealp{barnum2022}) and has an academic treatment in \citet{lsae2025}; Section~\ref{sec:dose} confirms it with a pooled design and supplies the aggregation interpretation.

On the digital-media hypothesis specifically, the nearest causal antecedents sit outside the U.S. achievement literature. \citet{jainstemper2024} estimate the effect of 3G arrival on PISA scores across 82 countries, and a 2025--26 rollout-based literature traces the same smartphone shock through fertility and family formation \citep{myershooper2026,hudsonmoscoso2026}; Section~\ref{sec:h2} imports both. No within-U.S. mobile-rollout design against test scores previously existed; \citet{wyckoff2025} states the direct causal evidence is lacking. Section~\ref{sec:fourg} supplies a first pass: a county-level 4G-rollout event study built from the archived National Broadband Map, which returns a precise null on the arrival-timing margin while leaving the national and adoption margins open.
WHY: Role duty + D8: the one dense line-paragraph becomes three paragraphs with topic sentences (documentation / hypothesis-weighing genre / digital-media antecedents); all three em-dash constructions removed; D1 removes running-prose "the verdict this report reaches" (now "the conclusions ... rest on"). All 14 citation keys and all four \refs carried verbatim.
RISK: none

### EDIT P1-frontmatter-7 [replace]
ANCHOR: \emph{First}, the waiver-timing event study (Section~\ref{sec:waiver}).
SECTION: Related Work and Contribution, "First" (waiver) contribution paragraph
PROPOSED: \emph{First}, the waiver-timing event study (Section~\ref{sec:waiver}). \citet{dewey2026} make the descriptive observation that post-2013 declines were similar in waiver and non-waiver states, and write of the sustained-accountability counterfactual that it ``has never been tested.'' The causal waiver literature is within-state: regression-discontinuity studies of priority/focus designations in Michigan, Kentucky, and Louisiana \citep{hemeltjacob2020,deedizonross2019}. \citet{deejacob2011} identify NCLB's \emph{adoption} effects from cross-state timing of prior accountability; Section~\ref{sec:waiver} runs that design in reverse on the policy's dismantling. The closest prior empirical estimate is \citet{bleiberg2020}, whose dissertation difference-in-differences of waiver receipt (binary, by 2013) on mean student-level NAEP scores through 2013 finds no average effect, a result that corroborates ours at the mean; his published waiver work concerns school-improvement designations within waiver states \citep{bleiberg2026}. What remains distinct here is the staggered-timing-plus-never-treated design carried through 2019, the percentile outcomes that the bottom-concentrated decline makes essential, and the randomization inference with an explicit power benchmark.
WHY: Local organization: all waiver-precedent material (including Bleiberg, moved from the section's closing paragraph) now lives in the waiver contribution paragraph; em-dash pair converted to a colon; no content or citation lost. Pair with P1-frontmatter-8.
RISK: none

### EDIT P1-frontmatter-8 [replace]
ANCHOR: Beyond the three tests, the report's integrative device
SECTION: Related Work and Contribution, closing paragraph
PROPOSED: Beyond the three tests, the report's integrative device derives distinct predictions from each hypothesis across timing, distribution, cohort structure, sector, geography, and international comparisons, and scores all hypotheses against all facts. We believe this is a more disciplined version of an argument that has so far been conducted one hypothesis at a time.
WHY: D8 + local organization: with the Bleiberg material moved to the waiver paragraph (P1-frontmatter-7), the closer states the integrative device in two sentences instead of one 55-word em-dash sentence plus waiver residue. Pair with P1-frontmatter-7.
RISK: none

### EDIT P1-frontmatter-9 [replace]
ANCHOR: \paragraph{Main NAEP.}
SECTION: Data, "Main NAEP" paragraph
PROPOSED: \paragraph{Main NAEP.} The primary data are national public- and private-school average scale scores and percentile scores (10th, 25th, 50th, 75th, 90th) for mathematics and reading at grades 4 and 8, for all assessment years from 1990 (mathematics) and 1992 (reading) through 2024, retrieved from the NAEP Data Service API \citep{naepapi}. Subgroup means (race/ethnicity, sex, National School Lunch Program eligibility), school-sector results (public, Catholic, private), state-level means for 2013--2024, and a state $\times$ year panel of percentile scores (2003--2024) come from the same source. State ESEA-waiver approval dates were compiled from Department of Education records, CRS Report R42328, and EdWeek's state-by-state tracking.\footnote{NSLP-eligibility breakdowns are available through 2022; the API does not return them for 2024. Pre-2003 national figures use the no-accommodations samples for 1990--1996 and accommodated samples thereafter, following NAEP reporting conventions. All scores were re-validated against published NAEP report-card values.} NAEP scale scores are reported on 0--500 scales. The within-grade student standard deviation (SD), estimated from the 2013 percentile spread, is roughly 29 points for grade 4 mathematics, 36 for grade 8 mathematics, and 34--36 for reading. A useful rule of thumb is that 10--12 NAEP points correspond to roughly one grade level of learning.
WHY: D8 clarity: the two spliced semicolon sentences become four sentences; the inventory first sentence is retained (length doing real work). Footnote and every number carried verbatim.
RISK: number-adjacent

### EDIT P1-frontmatter-10 [replace]
ANCHOR: \paragraph{Long-Term Trend (LTT) NAEP.}
SECTION: Data, "Long-Term Trend (LTT) NAEP" paragraph
PROPOSED: \paragraph{Long-Term Trend (LTT) NAEP.} The LTT assessment has measured 9-, 13-, and 17-year-olds with substantially unchanged content since the early 1970s, providing the longest consistent yardstick. National means and percentiles for ages 9 and 13 (1971--2025) were compiled from the Digest of Education Statistics and the LTT Data Service and cross-validated against published highlights \citep{nces2023ltt}. The 2025 wave, administered in the 2024--25 school year and released June 10, 2026, was pulled directly from the LTT Data Service, with the full extraction and press anchors recorded in \texttt{evidence/ltt\_2025.md}. Two timing facts make the LTT unusually valuable here: the age 9 ``2020'' assessment was administered in January--March 2020, \emph{immediately before} the pandemic school closures, and the age 13 ``2020'' assessment in fall 2019. These provide clean pre-pandemic endpoints.
WHY: D8 (minor, skippable if the reconciler is trimming): the 65-word semicolon sentence becomes two sentences; nothing else changes. All dates, citation, and file path carried verbatim.
RISK: number-adjacent
