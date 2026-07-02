# P5-mechanism-synthesis — proposal (lines 385–473: Mechanism Checks, set-asides, Synthesis)

## Summary

This proposal is a D8 line-level edit of the schooling-mode, attendance, effort, and set-asides subsections (topic sentences first, em-dashes cut to zero in every rewritten paragraph, 40+-word sentences split, all numbers and citations carried verbatim), plus the structural work the charter assigns P5: an H8-to-set-asides signpost for the opioid dispatch (A3-4 already covers school discipline), scorecard caption and table notes reframed as a consistency screen that accommodates A3-6's mental-health row without further prose change, and topic-sentence splits of the synthesis phase-one and phase-two mega-paragraphs built on A1-26/A2-12's substance with owner-named merge slots. Where A-agents own substance in my range (dual-criterion paragraph, section retitle, "digital-media mechanism" phrase) I defer to their filed edits and supply merge instructions rather than competing variants. Nothing here changes a number, a citation, a label, or a finding.

## Top-3 structural recommendations

1. **Adopt A4-7's retitle of `sec:mechanism`** ("Channel Checks: Schooling Mode and Attendance"), optionally extended to "Channel Checks: Schooling Mode, Attendance, and Test Effort" so the title matches the section's four subsections; `\label{sec:mechanism}` preserved either way. My intro rewrite (EDIT P5-2) works under either title and folds in A4-8's terminology fix.
2. **Set-asides become an itemized list** (EDIT P5-10) paired with two H8 signposts — A3-4's school-discipline pointer and my opioid pointer (EDIT P5-1) — so a reader arriving from the critique's candidate list ("shifts in school discipline, and so on") finds each dispatch in one hop.
3. **Reconciliation recipe for the Synthesis block:** dual-criterion paragraph = A1-25's D8-styled frame with its "Two candidates..." sentence swapped for A3-7's two-sentence version (which carries `\ref{sec:h8}` and the ban-studies clause; depends on A3-3's new label). Phase one = whichever A1-26 × A2-12 substance merge wins, laid out in my three-paragraph split (EDIT P5-13). Phase two = my two-paragraph split (EDIT P5-14), which no A-agent contests.

## Deliberately left alone (and why)

- **Line 385 section heading** — A4-7 owns the D6 retitle and has filed it; I endorse it (see rec 1) and file no competing edit.
- **Line 466 dual-criterion paragraph** — A1-25 and A3-7 have both filed full versions; a third variant from me would add reconciler load without new content. Merge instruction in rec 3. One styling note for the reconciler: A3-7 retains the original double-em-dash constructions; A1-25's frame is the D8-compliant one.
- **Line 404** ("The decomposition is associational...") — already two clean sentences with a topic sentence and no em-dashes.
- **Subsection headings at lines 390, 399, 406, 415** — descriptive of the evidence, not verdict-announcing; D1-compliant as they stand.
- **Figure captions at lines 423, 430, 437** (`fig:tuda`, `fig:dose`, `fig:absence`) — short, accurate, source-noted.
- **Line 441 Synthesis section heading** — "A Two-Phase Decline With Different Causes" states the report's established two-phase finding (H1 confirmed for phase two is not in dispute); recalibration, if any, is A1's call.
- **Scorecard table body and column headers** — symbols and rows frozen; A3-6 adds the mental-health row. My caption/notes edits (P5-11, P5-12) are row-count-agnostic by design.

---

## Edits (document order)

### EDIT P5-1 [insert-after]
ANCHOR: High-school GPAs rose from 3.17 (2010) to 3.36 (2021)
SECTION: Testing the Hypotheses > H8: Other candidates (end of subsection)
PROPOSED:

```latex
One further family-environment candidate, the opioid epidemic, was tested directly: state-level estimates are right-signed but statistically null, and Section~\ref{sec:setaside} records it alongside the other avenues examined and set aside.
```

NOTE FOR RECONCILER: A3-4's H8 intro paragraph already signposts school discipline to `sec:setaside`; this sentence completes the pair for opioids (my role assignment names both dispatches). If A3-4 lands, prefer splicing this sentence into A3-4's dispatch paragraph immediately after its school-discipline sentence (it reads correctly there) rather than keeping it as a separate closing paragraph; if A3-4 does not land, it stands alone here. A3-5 inserts its mental-health block after this same paragraph; order the insertions signpost-first, mental-health-block-second so the block closes the subsection.
WHY: D5 signposting per adjudication ("make both findable"): the opioid set-aside is otherwise findable only by reading Section 8 end-to-end.
RISK: collides:A3 (shares the insertion locus with A3-5; complements A3-4) | collides:P3 (P3 styles line 296; anchor is in the current file, so the insertion point resolves regardless)

### EDIT P5-2 [replace]
ANCHOR: Two further analyses probe the phase-two mechanisms directly
SECTION: Mechanism/Channel Checks, section intro paragraph
PROPOSED:

```latex
The tests of Section~\ref{sec:sharper} discriminate between explanations for phase one; this section turns to phase two and to measurement. Two analyses probe the channels behind phase two directly: merging state NAEP changes with measured pandemic schooling mode, and exploiting NAEP's own student-reported attendance data. A third subsection asks whether the measured decline could instead be an artifact of falling test-taking effort. The section closes with the avenues examined and set aside.
```

NOTE FOR RECONCILER: this is A4-8's terminology-and-accuracy fix (mechanisms → channels; the intro now announces all four subsections) with a D8 topic sentence prepended and A4-8's long second sentence split. Substance identical to A4-8; adopt either, not both.
WHY: D6 terminology + D8 topic-sentence/roadmap; the current intro announces two of four subsections.
RISK: collides:A4 (builds on A4-8, which flags this collision in reverse)

### EDIT P5-3 [replace]
ANCHOR: states' 2019--2022 NAEP changes can be regressed on the share of the 2020--21 school year
SECTION: Schooling mode subsection (`sec:dose`), first paragraph
PROPOSED:

```latex
Between-state variation in pandemic schooling mode explains almost none of the between-state variation in NAEP score declines. The treatment measure comes from the COVID-19 School Data Hub's district learning-model records, aggregated to enrollment-weighted state shares (47 states plus DC; Iowa, Montana, and Oklahoma are uncovered). In a regression of states' 2019--2022 NAEP changes on the share of the 2020--21 school year spent fully virtual, the relationship is right-signed but weak in mathematics ($-0.33$ points per 10 percentage points virtual at grade 4, $p=0.13$; $-0.18$ at grade 8, $p=0.35$), absent in reading (grade 8 is wrong-signed), and essentially zero pooled across the four series ($-0.04$ points per 10pp, $p=0.80$, clustered by state); Figure~\ref{fig:dose} (left) shows the grade 4 mathematics scatter. The result is robust to excluding DC and, if anything, strengthens under enrollment weighting (weighted slopes are zero in mathematics).
```

WHY: D8 — the paragraph's conclusion becomes its topic sentence (removing the duplicate closing sentence); every estimate, p-value, and coverage detail carried verbatim.
RISK: number-adjacent (all values unchanged)

### EDIT P5-4 [replace]
ANCHOR: The same exercise can be pushed below the state level
SECTION: Schooling mode subsection (`sec:dose`), TUDA paragraph
PROPOSED:

```latex
The same exercise pushed below the state level, to NAEP's Trial Urban District Assessment, again finds only a weak dose-response (Figure~\ref{fig:tuda}). The 26 TUDA districts span essentially the full treatment range (Dallas, Miami-Dade, and Hillsborough were near-fully in person; Atlanta and Philadelphia fully virtual), and each is matched here to its own CSDH district record. Even with that contrast, the gradient in NAEP is weak: $-0.29$ to $-0.34$ points per 10pp virtual at grade 4 ($p\approx0.12$--$0.16$), zero at grade 8, $-0.18$ pooled ($p=0.23$), and no relationship between virtual share and 2019--2024 net change. The confidence intervals are wide enough to admit effects of the size the growth-based literature reports. The right reading is therefore not contradiction but limitation: NAEP's cross-sectional district samples (with standard errors of 1.5--2.5 points) and the restricted, all-urban TUDA sample blur a gradient that longitudinal growth data resolve.
```

WHY: D8 — topic sentence states the result; the 45-word limitation sentence split in two; all estimates verbatim.
RISK: number-adjacent

### EDIT P5-5 [replace]
ANCHOR: The basic state-level fact was observed when the 2022 scores were released
SECTION: Schooling mode subsection (`sec:dose`), interpretation paragraph
PROPOSED:

```latex
This state-level fact is not new, and it is not a refutation of the closure literature. It was observed when the 2022 scores were released \citep{barnum2022} and formalized by \citet{lsae2025}; the pooled estimate here confirms it. The district-level studies \citep{goldhaber2023,jack2023} exploit far larger within-state treatment variation with apter controls, and state aggregation compresses both the treatment (few states were mostly virtual on average) and the outcome (state NAEP changes carry sampling errors of roughly a point). The useful calibration is this: \emph{schooling mode explains the timing of the national 2019--2022 drop better than it explains which states fell most}. Factors that varied little between states (the disruption itself, the absenteeism surge, whatever was already eroding the bottom) dominate the state cross-section.
```

WHY: D8 — dissolves a 60-word double-em-dash sentence into three; citations and the emphasized calibration sentence carried verbatim.
RISK: none

### EDIT P5-6 [replace — split into two paragraphs]
ANCHOR: NAEP asks students how many days of school they missed in the month
SECTION: Attendance subsection (`sec:attendance`), main evidence paragraph
PROPOSED (two paragraphs; blank line = paragraph break, one physical line each per file convention):

```latex
NAEP's own attendance item shows disengagement rising before the pandemic, earlier than administrative records indicate. The assessment asks students how many days of school they missed in the month before the assessment, providing an attendance measure tied directly to scores and consistent since 2002. Three facts emerge (Figure~\ref{fig:absence}). First, the share reporting three or more missed days sat in the 19--22\% range from 2003 through 2013 with no trend, then \emph{began rising before the pandemic}, reaching 24\% at grade 4 by 2019; it jumped to 32--35\% in 2022 and remained near 30\% in 2024. This mirrors the administrative chronic-absenteeism record \citep{malkus2025} while revealing a disengagement pre-trend that the administrative data (flat at $\sim$15\% through 2019) understate. Second, the score penalty associated with absence widened sharply \emph{before} COVID: the gap between students missing no days and those missing more than ten grew from 29 to 42 points in grade 8 reading between 2013 and 2019. Absence became more academically costly, or increasingly selected the most disengaged students, exactly when the bottom of the distribution was collapsing.

Third, a Kitagawa decomposition splits each mean change into the part from students shifting into higher-absence categories and the part from score declines within categories. The absence shift accounts for roughly 25--42\% of the 2019--2024 declines (e.g., 42\% in grade 4 mathematics, 25\% in grade 8 mathematics), closely bracketing the Council of Economic Advisers' estimate, but for only 7--19\% of the pre-pandemic grade 8 declines. Phase one was not an attendance phenomenon.
```

WHY: D8 — splits a ~230-word paragraph at its natural seam (survey facts vs.\ decomposition), adds a topic sentence, removes all four em-dash constructions; every percentage and point value verbatim.
RISK: number-adjacent

### EDIT P5-7 [replace]
ANCHOR: NAEP, PISA, and PIAAC are all low-stakes for the test-taker
SECTION: Effort subsection (`sec:effort`), setup paragraph
PROPOSED:

```latex
A remaining measurement alternative deserves a direct check rather than a footnote: perhaps students did not lose skill but stopped trying. NAEP, PISA, and PIAAC are all low-stakes for the test-taker, and effort demonstrably matters for their \emph{levels}: a surprise monetary incentive raised U.S. high-schoolers' scores on PISA-style items by roughly a quarter of a standard deviation (with no effect in Shanghai) \citep{gneezy2019}; incentives raised grade 12 NAEP-style reading scores by at least 5 points \citep{braun2011}; and effort proxies explain a third of cross-country PISA variation \citep{zamarro2019}. If students simply began trying less hard after 2012, part of the measured decline could be motivational rather than cognitive.
```

WHY: D8 — the buried "deserves a direct check rather than a footnote" becomes the topic sentence; evidence list and citations verbatim.
RISK: none

### EDIT P5-8 [replace]
ANCHOR: Three pieces of evidence bound the concern.
SECTION: Effort subsection (`sec:effort`), evidence paragraph
PROPOSED:

```latex
Three pieces of evidence bound the concern. First, PISA's ``effort thermometer'' asks students to rate (1--10) the effort they invested and the effort they would have invested had the test counted, in both 2018 and 2022. In the microdata, reported effort fell by just 0.13 points in the U.S. and 0.16 across the OECD; multiplying by the cross-sectional effort--score gradient (3.9 points per effort point, ESCS-adjusted, itself an upper bound on the causal effect) implies an effort-attributable change of roughly \emph{half a point} of the 13--15-point 2018--2022 PISA decline, under five percent. Second, the OECD's behavioral indicators move the wrong way for an effort story. The within-test fatigue gap (first vs.\ second hour) \emph{narrowed} in 2022, meaning scores fell most at the \emph{beginning} of the test; answer straight-lining declined; and the OECD concluded that administration conditions ``remained similar,'' singling out only Albania \citep{oecd2023}. Rapid-guessing prevalence across countries is essentially uncorrelated with mean performance \citep{avvisati2024}, and no NCES analysis documents rising disengaged responding on digital NAEP. Third, and decisive for the U.S. case, the same 2013--2019 decline appears where the motivation story cannot follow it. It shows up in \emph{state accountability tests}, which carry stakes for schools: the SEDA archive of roughly 70 million students' consequential state assessments \citep{dewey2026}. And it shows up among PIAAC adults, where the school-test motivation dynamic does not apply.
```

WHY: D8 — removes three double-em-dash constructions and splits the 55-word third item; all effort values, gradients, and citations verbatim.
RISK: number-adjacent

### EDIT P5-9 [replace]
ANCHOR: A caution survives: across countries
SECTION: Effort subsection (`sec:effort`), closing paragraph
PROPOSED:

```latex
A caution survives. Across countries, the change in even \emph{hypothetical} (``if it counted'') effort correlates 0.64 with the change in mathematics performance, so motivation and measured skill co-move, most plausibly because both are downstream of the same disengagement that the absence and reading-practice data record. The honest conclusion is that effort is a real wedge in score \emph{levels}, but the change in effort is far too small to explain the decline. To the extent motivation has eroded, it is part of the phenomenon, not an artifact contaminating it.
```

WHY: D8 — em-dash removed, final two-clause sentence split; the 0.64 correlation and conclusion unchanged.
RISK: none

### EDIT P5-10 [replace — paragraph becomes intro line + itemized list]
ANCHOR: Several further hypotheses were tested or scoped
SECTION: Avenues examined and set aside (`sec:setaside`)
PROPOSED:

```latex
Several further hypotheses were tested or scoped and judged not to merit headline treatment; they are recorded here so the reader knows they were not overlooked.
\begin{itemize}
\item \emph{Opioid epidemic / family distress.} Regressing states' 2013--2019 bottom-decile changes on the change in CDC age-adjusted drug-overdose death rates yields right-signed but statistically null estimates in three of four series (the largest, grade 4 reading, has $r=-0.32$, $p=0.12$). With heavy geographic confounding and no dose-response consistency, the test neither supports nor rules out a contributing role.
\item \emph{School discipline reform.} The 2014 federal guidance and the accompanying decline in suspensions have the right timing and a bottom-concentrated prediction, but there is no clean cross-state policy variation independent of the accountability and political variables already examined. The hypothesis remains untested rather than rejected.
\item \emph{Cross-country smartphone-adoption timing vs.\ PISA declines.} Country-level adoption series are too inconsistently measured across sources to support a credible event-time alignment; this remains the right design for future work with better data.
\item \emph{Cannabis legalization.} This fails on first inspection: adolescent use was roughly flat through the 2010s in national surveys, and legalization timing is collinear with state politics and pandemic schooling mode.
\item \emph{PISA smartphone-use frequency.} The ICT item available for U.S. students was examined and discarded as an exposure measure: ``uses a smartphone several times daily'' is positively associated with scores (+70 points vs.\ never-users, SES-adjusted) because, in a 95\%-saturated population, the abstainers are a highly atypical, disadvantaged group. Frequency of use measures access, not excess; the hours-of-use and distraction items of Section~\ref{sec:h2} do not share this defect.
\end{itemize}
```

WHY: D5 findability — the critique names school discipline; readers signposted from H8 (A3-4, P5-1) must be able to locate each dispatch by scanning, which a five-topic run-on paragraph defeats; content and every number carried verbatim, one em-dash construction removed, "items above" made an explicit `\ref{sec:h2}`.
RISK: number-adjacent (values unchanged; core LaTeX `itemize`, no new packages)

### EDIT P5-11 [replace]
ANCHOR: \caption{Hypothesis scorecard against the facts of Section~\ref{sec:verify}.}
SECTION: Synthesis, Table `tab:scorecard` caption
PROPOSED:

```latex
\caption{Hypothesis scorecard: consistency of each candidate explanation with the facts of Section~\ref{sec:verify}.}
```

WHY: D2/D3 — names the table's epistemic status (a consistency record, not a causal ranking) and stays agnostic to row count, accommodating A3-6's mental-health row with no further prose change.
RISK: none

### EDIT P5-12 [replace]
ANCHOR: $\times$ = inconsistent or silent
SECTION: Synthesis, Table `tab:scorecard` notes (the `\multicolumn` note row)
PROPOSED (the existing note line, terminated with `\\`, plus one new note line):

```latex
\multicolumn{7}{l}{\footnotesize \checkmark{} = consistent; $\sim$ = partially consistent; $\times$ = inconsistent or silent.}\\
\multicolumn{7}{l}{\footnotesize Consistency is a screen, not a causal attribution; direct tests: Sections~\ref{sec:sharper} and~\ref{sec:mechanism}.}
```

WHY: D2/D3 — the scorecard is where a skimming reader takes the ranking from, so the screen-not-proof caveat must sit on the table itself; also does the accommodation work for A3-6's added row (whose symbols match H2's) by telling the reader the table alone cannot separate candidates.
RISK: none (both `\ref` targets exist in the current file; symbol line unchanged, `\\` added to permit the second note row)

### EDIT P5-13 [replace — split into three paragraphs]
ANCHOR: \textbf{Phase one (2013--2019): erosion at the bottom.}
SECTION: Synthesis, phase-one paragraph (substance co-owned by A1+A2+A3; this edit is the paragraphing scaffold, built from A1-26 and A2-12's filed sentences)
PROPOSED (three paragraphs; substance slots in brackets name the owner; blank line = paragraph break):

```latex
\textbf{Phase one (2013--2019): erosion at the bottom.} Slow national decline, concentrated almost entirely among the lowest-performing students, present in most states and many countries, alongside collapsing voluntary reading. Two hypotheses fit these basic facts most directly: the accountability retreat (which predicts the bottom-concentration and the U.S. policy timing, and is corroborated in mirror image by Mississippi) and digital-media displacement (which predicts the international synchrony and the reading-practice collapse). [SUBSTANCE: A3 --- optional one-clause acknowledgment of adolescent mental health as a further candidate fitting these facts, if the reconciler wants it named here in addition to the dual-criterion paragraph; adjust the count if so.]

The timing tests of Section~\ref{sec:sharper} reject the strong local form of each hypothesis, using each hypothesis's own variation: release from NCLB did not move a state's bottom decile, and 4G arrival did not move a county's scores. What favors digital media is positive evidence rather than survival of elimination. The losses accrue during adolescence, to cohorts that arrived at grade 4 at record levels. They appear equally inside Catholic schools that accountability never governed, and in states that never adopted the Common Core. And in the widest version of the same test, they reappear among adults across nineteen OECD countries (Section~\ref{sec:adults}), a population no school policy touches. [SUBSTANCE: A1/A2 --- the closing T5 ranking sentence; reconciler harmonizes A1-26's ``best-supported remaining candidate for phase one, not an established cause ... candidate list, which stays open'' with A2-12's ``pending the pre-registered 2026 state-ban test'' qualifier.]

The accountability retreat retains a plausible supporting role (as a national climate shift, and at the public-school grade 4 bottom decile, where the sector contrast does point its way), but the strong version in which deregulation drove the floor down is rejected by its own state-level test. Funding, demographics, and teacher supply fail on timing, distribution, or magnitude. [SUBSTANCE: A2 --- if A2-12's variant wins, its ``no longer claims a demonstrated state-level channel'' clause replaces the ``rejected by its own state-level test'' clause; keep matched to the form-of-hypothesis clauses of Sections~\ref{sec:waiver} and~\ref{sec:fourg}.]
```

WHY: Role mandate + D8 — the ~200-word mega-paragraph becomes three paragraphs (what phase one was / what the tests showed and how digital media ranks / what survives and what fails), each opening with a topic sentence; all sentences are drawn from the current file, A1-26, or A2-12, with zero em-dashes and no numbers altered.
RISK: collides:A1 | collides:A2 | collides:A3 (strictly stylistic scaffold; the bracketed slots are not final text and must be resolved by the reconciler from the named owners' filed edits)

### EDIT P5-14 [replace — split into two paragraphs]
ANCHOR: \textbf{Phase two (2019--2024): shock without recovery.}
SECTION: Synthesis, phase-two paragraph
PROPOSED (two paragraphs; blank line = paragraph break):

```latex
\textbf{Phase two (2019--2024): shock without recovery.} The pandemic caused the large 2019--2022 drop (the schooling-mode dose-response evidence is decisive) and hit the whole distribution. What demands explanation is the aftermath. Four-plus years on, aggregate recovery is negligible, reading is still falling, and among adolescents the bottom decile continues to sink while the top rebounds; the 2025 LTT shows the first exception, a bottom-led rebound among 9-year-olds, while 13-year-olds remain stuck. Persistently doubled chronic absenteeism is the leading proximate cause, with the phase-one forces (weak accountability pressure, screen displacement) plausibly explaining why disengagement has not self-corrected.

The magnitudes in Table~\ref{tab:changes} put the two phases in proportion: phase one accounts for roughly 20--45\% of the total 2013--2024 decline depending on the series, the pandemic window for roughly 30--70\%, and the post-2022 period for the remainder. Even a complete reversal of pandemic losses would therefore leave the United States well below its 2013 peak.
```

WHY: D8 — splits the mega-paragraph at its seam (the aftermath story vs.\ the magnitude accounting), removes all four em-dash constructions, keeps every share, date, and claim verbatim.
RISK: collides:A1 (claim-strength words such as ``decisive'' and ``leading proximate cause'' are carried unchanged from the current text; final calibration is A1's)

### EDIT P5-15 [replace]
ANCHOR: Three implications follow.
SECTION: Synthesis, implications paragraph
PROPOSED:

```latex
Three implications follow. First, ``COVID recovery'' framing understates the problem: grade 8 reading was already down 4.4 points before the pandemic, and the forces behind that slide are still operating. Second, because losses are concentrated at the bottom, average-score targets understate the equity emergency; the 90--10 gap is the widest ever measured. Third, with the school-policy explanations weakened by the tests of Section~\ref{sec:sharper}, the empirical frontier shifts to the digital-media hypothesis and its pathways, where causal evidence is accumulating. Existing ban studies \citep{belandmurphy2016,abrahamsson2024,beneito2022,figlio2025} consistently find gains concentrated among low achievers, and the staggered adoption of U.S. state bans (roughly thirty states by 2025--26) against NAEP 2026 offers exactly the kind of test that waiver timing provided here; this project's repository pre-specifies the design and treatment coding. Mississippi's literacy reform remains the strongest evidence that aggressive instructional policy can buck the trend even if policy retreat did not cause it.
```

WHY: D6 + D8 — incorporates A4-9's exact substitution ("the digital-media hypothesis and its pathways") into the styled paragraph, splits the 70-word third implication, and removes the em-dash; the waiver-analog clause (D4 symmetry) is the current text's own wording, kept verbatim.
RISK: collides:A4 (adopts A4-9; apply one, not both) | collides:A2 (the waiver-analog clause echoes A2-11's ``smartphone-side analog'' sentence in Section~\ref{sec:sharper}; acceptable as a synthesis recap, reconciler may trim)
