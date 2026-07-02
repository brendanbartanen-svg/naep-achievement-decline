# Proposal P2-verify-decline — Verifying the Decline (report.tex lines 71–197)

**Agent:** P2 (part editor). **Scope:** Section "Verifying the Decline": seven subsections plus the F1–F8 summary-of-facts list. **Charter basis:** D8 throughout (topic sentences, split >40-word sentences, cut em-dashes by two-thirds, trim intensifiers, active voice); caption self-containedness per role instructions; D2 tier check (this section is T1 data description throughout).

## Summary (3 sentences)

This proposal makes 20 whole-paragraph/caption replacements that apply D8 line editing to the verification section: topic sentences now state what each paragraph establishes, every sentence over ~40 words is split, the section's ~11 em-dash usages drop to zero, and intensifiers ("More striking," "Notably," "prominent," "single most," "in free fall," "considerably") are trimmed. All eight figure captions in the range are rewritten to state what to see and then the source; the fig:lttpct caption, which already did this, gets only a sentence split. Every number, citation, footnote, `\label`, and `\ref` is carried through unchanged, and the F1–F8 list keeps its numbering and content exactly aligned with what the subsections establish, gaining only a lead-in topic sentence and losing two em-dash pairs.

## Top-3 structural recommendations

1. **Split the long distributional paragraph into two** (proposed here as EDIT P2-9): pandemic-era pattern (uniform 2019–22 drop, post-2022 divergence) vs. the 2025-LTT age split. The single current paragraph carries two distinct findings; each half gets its own topic sentence. This is the only edit in this proposal that changes paragraph count (one physical line becomes two paragraph lines plus a blank line).
2. **(For P5/E, not executed here)** Add a forward pointer tying the F1–F8 list to the scorecard (`Table~\ref{tab:scorecard}`), so the list's role as the scoring rubric is explicit at the point where it is defined. The scorecard table and its notes are P5's turf; P2 keeps the list itself stable.
3. **Keep F1–F8 inline as a single paragraph**, not an itemized list (length discipline, non-negotiable 6). If E restructures it anyway, the F-numbering must survive verbatim: the scorecard header row keys columns to F1–F7, the synthesis references the facts by number, and A3's new mental-health row will be scored against these same facts.

## Deliberately left alone (and why)

- **The `tab:changes` discussion paragraph** ("Table~\ref{tab:changes} decomposes the decline. Three observations matter...") — already D8-compliant: clear topic sentence, enumerated First/Second/Third structure, no em-dashes, sentences within bounds.
- **The subgroups paragraph** ("Score declines appear \emph{within} essentially every demographic subgroup...") — already compliant; strong topic sentence that states the inferential point (constrains compositional explanations), no em-dashes.
- **The `tab:changes` table caption** — table captions read as titles and the table is self-explanatory; adequate as is.
- **All subsection headings in the range** — each describes the evidence examined ("The Long-Term Trend assessment confirms the timing," "Geography: a national phenomenon...") and none pre-announces a hypothesis winner, so D1 is not implicated. All `\label`s untouched.
- **"rule out the possibility that the main-NAEP decline is an artifact"** (LTT paragraph) — kept. This is T1 cross-instrument data description (two independent instruments, same decline), not a T3 quasi-experimental null, so D2's "never 'rules out the hypothesis'" ban does not apply.
- **"A force that simultaneously lowers the floor ... is, almost by construction, not an education-policy variable"** (adults paragraph) — kept verbatim. It is a rejection-side claim of exactly the kind D3 endorses as the report's strongest claim type, and it does not assert the smartphone conclusion; it is equally compatible with A3's new mental-health rival (D5). Flagged for A1/A2/A3 awareness rather than restyled.

Convention note on captions: rewritten captions restate only facts and numbers already established in the same subsection's text or already present in the caption; no new numeric values are introduced anywhere in this proposal.

---

## Edits (document order)

### EDIT P2-1 [replace]
ANCHOR: All four rose strongly through the 2000s, peaked in 2013
SECTION: Verifying the Decline > National trends
PROPOSED: All four main NAEP series trace the same arc: strong gains, a peak around 2013, and decline since. Figure~\ref{fig:national} plots the national average scale scores. Each series rose strongly through the 2000s, peaked in 2013 (grade 4 reading in 2015, fractionally above its 2013 level), drifted downward through 2019, and dropped sharply between 2019 and 2022. Except for a partial rebound in grade 4 mathematics, every series continued falling or stagnated through 2024.
WHY: D8 — topic sentence states the finding instead of opening with a figure pointer; splits a 50-word sentence; removes the em-dash parenthetical.
RISK: number-adjacent

### EDIT P2-2 [replace]
ANCHOR: Dotted line marks 2013; shaded band marks the period
SECTION: Verifying the Decline > National trends (fig:national caption)
PROPOSED: \caption{National average NAEP scale scores, 1990--2024. All four series peak around 2013 and decline thereafter, with the sharpest drop in the pandemic window. The dotted line marks 2013; the shaded band marks pandemic-disrupted schooling. Data: NAEP Data Service API.}
WHY: Caption self-containedness — states what to see (peak, two-step decline), then plot conventions, then source.
RISK: number-adjacent

### EDIT P2-3 [replace]
ANCHOR: age 13 mathematics fell from 285 in 2012 to 280 in fall 2019
SECTION: Verifying the Decline > The Long-Term Trend assessment confirms the timing
PROPOSED: The LTT data (Figure~\ref{fig:ltt}) rule out the possibility that the main-NAEP decline is an artifact of framework or administration changes. On test content held essentially constant since the 1970s, age 9 and age 13 scores peaked in 2012 and were already falling before the pandemic. Age 13 mathematics fell from 285 in 2012 to 280 in fall 2019, and age 13 reading from 263 to 260, \emph{before any school closed}. The pandemic then produced the largest drops ever recorded in the series. Age 9 mathematics fell 7 points between early 2020 and 2022 (its first statistically significant decline ever), and age 13 mathematics fell 9 further points by fall 2022, landing at its 1992 level. Age 13 reading in 2023 (256) was statistically indistinguishable from its 1971 baseline: a half-century of progress erased for the median young adolescent. The 2025 wave, released in June 2026, shows the post-pandemic period diverging by age. At age 9, students recovered 3.8 points in both subjects, putting reading within 1.3 points of its pre-pandemic level. At age 13, scores were flat (mathematics 270.3 against 270.7 in 2023; reading 256.1 against 255.7), leaving age-13 mathematics 14.7 points below its 2012 peak and age-13 reading still at its 1971 level.
WHY: D8 — splits a 50-word sentence and a 60-word em-dash-laden sentence; removes all three em-dash usages; all numbers carried through unchanged.
RISK: number-adjacent

### EDIT P2-4 [replace]
ANCHOR: The age 9 ``2020'' point was assessed January--March 2020
SECTION: Verifying the Decline > LTT (fig:ltt caption)
PROPOSED: \caption{NAEP Long-Term Trend average scores, ages 9 and 13, 1971--2025. Both ages peak in 2012 and decline before the pandemic; the pandemic-era drops are the largest in the series. The age 9 ``2020'' point was assessed January--March 2020 (pre-pandemic) and the age 13 ``2020'' point in fall 2019; the 2025 points were assessed in the 2024--25 school year. The dotted line marks 2012. Data: NCES Digest tables 221.85/222.85, validated against the LTT Data Service; 2025 wave from the LTT Data Service (\texttt{evidence/ltt\_2025.md}).}
WHY: Caption self-containedness — adds the what-to-see sentence ahead of the timing conventions and source; no new numbers.
RISK: number-adjacent

### EDIT P2-5 [replace]
ANCHOR: The single most diagnostic fact in the data
SECTION: Verifying the Decline > The distributional signature
PROPOSED: The most diagnostic fact in the data is \emph{where} in the achievement distribution the losses occurred. Figure~\ref{fig:pctile} plots score changes since 2013 at the 10th through 90th percentiles for grade 8; Figure~\ref{fig:lttpct} shows the same comparison for the LTT, split into pre-pandemic (2012$\rightarrow$2020), pandemic (2020$\rightarrow$2022/23), and post-pandemic (2022/23$\rightarrow$2025) windows.
WHY: D8 intensifier trim ("single most" to "most"); rest unchanged. Minor; reconciler may drop.
RISK: none

### EDIT P2-6 [replace]
ANCHOR: Grade 8 score changes since 2013 by percentile.
SECTION: Verifying the Decline > Distributional signature (fig:pctile caption)
PROPOSED: \caption{Grade 8 score changes since 2013 by percentile. Losses are deepest at the bottom of the distribution; before the pandemic the top held steady or improved. Data: NAEP Data Service API.}
WHY: Caption self-containedness — the bare original states neither the pattern nor what makes it diagnostic; wording mirrors the adjacent text's own characterization.
RISK: none

### EDIT P2-7 [replace]
ANCHOR: after 2022/23 the recovery is bottom-led at age 9
SECTION: Verifying the Decline > Distributional signature (fig:lttpct caption)
PROPOSED: \caption{LTT score changes by percentile in three windows: pre-pandemic (left), pandemic era (center), and post-pandemic (right). The pre-pandemic decline is concentrated almost entirely among low performers. The pandemic-era decline hits everywhere but is steepest at the bottom. After 2022/23 the recovery is bottom-led at age 9, while at age 13 the bottom of the mathematics distribution keeps falling as the top recovers. Data: LTT Data Service.}
WHY: D8 — this caption already models self-containedness; the only change is splitting a 50-word semicolon chain into three sentences.
RISK: none

### EDIT P2-8 [replace]
ANCHOR: age 13 LTT mathematics fell 12.6 points at the 10th percentile
SECTION: Verifying the Decline > The distributional signature
PROPOSED: Before the pandemic, the decline was almost exclusively a bottom-of-the-distribution phenomenon. Between 2012 and 2020, age 13 LTT mathematics fell 12.6 points at the 10th percentile, 7.4 at the 25th, and 4.4 at the median, while \emph{rising} 0.1 points at the 90th. Main NAEP shows the same pattern: between 2013 and 2019, grade 8 mathematics fell 6.6 points at the 10th percentile while \emph{gaining} 2.7 points at the 90th, and grade 8 reading fell 10.2 points at the 10th percentile against 1.1 at the 90th. America's strongest students were holding steady or improving through 2019; its weakest students had been losing ground for years before anyone had heard of COVID-19.
WHY: D8 — removes the em-dash; replaces the "free fall" metaphor with plain description (register calibration per the critique's closing point); "identical" softened to "same" (the point values differ).
RISK: number-adjacent

### EDIT P2-9 [replace]
ANCHOR: The pandemic broke this pattern in an informative way
SECTION: Verifying the Decline > The distributional signature
PROPOSED: The pandemic broke this pattern in an informative way: the 2019--2022 losses appear across the entire distribution. In grade 8 mathematics the drop was essentially uniform, 6--9 points at every percentile, consistent with a shock (school disruption) that hit all students rather than only struggling ones. After 2022, the top of the distribution began recovering while the bottom kept falling: in grade 4 mathematics, 2022--2024 changes ranged from $+2.7$ points at the 75th percentile to $-0.6$ at the 10th.

The 2025 LTT results (Figure~\ref{fig:lttpct}, right panel) extend this divergence and split it by age. At age 13 the fan-out continued: between the 2023 and 2025 assessments, mathematics fell a further 2.8 points at the 10th percentile while rising 2.3 points at the 90th. That pushed the age-13 mathematics 90--10 gap to 114 points, 25 points wider than in 2012 and the widest in the series' half-century history. At age 9, by contrast, the recovery is real and concentrated where the losses were: +7.5 points at the 10th percentile in mathematics and +9.3 in reading, against +0.7 and +0.9 at the 90th. The age-9 turnaround is the first bottom-led improvement anywhere in this report's data. It also post-dates the 2024 main-NAEP assessment, where the grade 4 bottom decile was still falling. The two are consistent if the youngest students' rebound began only in the 2024--25 school year, a reading the 2026 main NAEP will adjudicate.
WHY: D8 — splits a ~200-word paragraph carrying two findings into two topic-sentenced paragraphs (structural rec 1); removes both em-dashes and a 45-word sentence. NOTE: replacement is two paragraphs (one blank line between); all numbers unchanged.
RISK: number-adjacent

### EDIT P2-10 [replace]
ANCHOR: The cumulative effect on inequality is unprecedented
SECTION: Verifying the Decline > The distributional signature
PROPOSED: The cumulative effect on inequality is unprecedented in NAEP's history. The 90--10 gap (Figure~\ref{fig:gap}) widened between 2013 and 2024 by 13 points in grade 4 mathematics (75$\rightarrow$89), 16 points in grade 8 mathematics (93$\rightarrow$109), 15 points in grade 4 reading, and 16 points in grade 8 reading. In every case the 2024 gap is the widest ever recorded.
WHY: D8 — replaces the trailing em-dash clause with a short closing sentence; "unprecedented" retained as an earned T1 description (widest on record).
RISK: number-adjacent

### EDIT P2-11 [replace]
ANCHOR: Gap between the 90th and 10th percentile scores, 2003--2024.
SECTION: Verifying the Decline > Distributional signature (fig:gap caption)
PROPOSED: \caption{Gap between the 90th and 10th percentile scores, 2003--2024. The gap widens after 2013 in every series; by 2024 each is the widest on record. Data: NAEP Data Service API.}
WHY: Caption self-containedness — states the pattern (record-wide gaps) before the source; reuses only numbers already established in the adjacent paragraph.
RISK: number-adjacent

### EDIT P2-12 [replace]
ANCHOR: Average scores by National School Lunch Program eligibility (available through 2022)
SECTION: Verifying the Decline > Subgroups (fig:lunch caption)
PROPOSED: \caption{Average scores by National School Lunch Program eligibility (available through 2022). Both groups decline through 2022, with larger pre-pandemic losses among eligible (lower-income) students. Data: NAEP Data Service API.}
WHY: Caption self-containedness — adds the what-to-see sentence, taken directly from the subgroups paragraph's established facts.
RISK: number-adjacent

### EDIT P2-13 [replace]
ANCHOR: Between 2013 and 2019, 75--94\% of states (depending on series) posted declines
SECTION: Verifying the Decline > Geography
PROPOSED: The decline is not regional. Between 2013 and 2019, 75--94\% of states (depending on series) posted declines; by 2024, between 88\% and 100\% of states remained below their 2013 level. No state escaped the national trend in grade 8 mathematics. Two partial exceptions are instructive. Mississippi rose from 49th to 29th in grade 4 reading between 2013 and 2019 following its 2013 early-literacy reform \citep{spencer2024}, and a handful of states (e.g., Alabama, Louisiana) regained or exceeded pre-pandemic grade 4 mathematics levels by 2024.
WHY: D8 — splits a 45-word sentence at the exceptions and trims "prominent"; numbers and citation unchanged.
RISK: number-adjacent

### EDIT P2-14 [replace]
ANCHOR: State variation \emph{within} the pandemic window
SECTION: Verifying the Decline > Geography
PROPOSED: State variation \emph{within} the pandemic window lines up with schooling-mode differences (Section~\ref{sec:h1}). States' 2019--2022 drops in grade 4 mathematics ranged from about $-13$ points to roughly zero. The states that fell most recovered somewhat faster afterward (correlation between 2019--22 change and 2022--24 change $\approx -0.3$ to $-0.5$; Figure~\ref{fig:states}), consistent with partial mean reversion as in-person schooling resumed. But the rebound slopes are shallow (about $-0.4$): most of the pandemic-window loss has, so far, been persistent rather than transitory.
WHY: D8 — splits the 50-word closing sentence at the em-dash; the persistence conclusion becomes its own sentence.
RISK: number-adjacent

### EDIT P2-15 [replace]
ANCHOR: State-level pandemic losses versus post-pandemic recovery, mathematics.
SECTION: Verifying the Decline > Geography (fig:states caption)
PROPOSED: \caption{State-level pandemic losses versus post-pandemic recovery, mathematics. Each point is a state. States that lost the most during the pandemic window recovered somewhat faster afterward, but the rebound is shallow relative to the losses. Data: NAEP Data Service API.}
WHY: Caption self-containedness — states the relationship to see (negative slope, shallow rebound) before the source; no numerals introduced.
RISK: none

### EDIT P2-16 [replace]
ANCHOR: The OECD-average PISA mathematics score fell 22 points
SECTION: Verifying the Decline > International context
PROPOSED: The U.S. decline is part of a broader rich-world phenomenon (Figure~\ref{fig:intl}). The OECD-average PISA mathematics score fell 22 points between 2012 and 2022 (494$\rightarrow$472) and reading fell 20 points, declines that began \emph{before} the pandemic. The OECD itself concluded that the fall was ``only partly attributable to the COVID-19 pandemic,'' noting that reading and science had been sliding for roughly a decade \citep{oecd2023}. Twelve OECD systems, including Finland, the Netherlands, Belgium, and Canada, show statistically significant mathematics declines beginning before 2018. One U.S. series is an apparent exception: U.S. PISA \emph{reading} was flat (505$\rightarrow$504) between 2018 and 2022 while the OECD average fell 11 points, so the U.S. position relative to peers improved even as its NAEP reading scores fell. One reconciliation is that PISA samples 15-year-olds, whose NAEP-cohort losses were smaller than younger students'. U.S. TIMSS mathematics tells the same story as NAEP: grade 8 scores fell 27 points between 2019 and 2023, back to mid-1990s levels, with the lowest 10th-percentile scores since the study began \citep{nces2024timss}.
WHY: D8 — removes all three em-dash usages, splits the 48-word "Notably" sentence in two, and trims "Notably"/"actually"; all numbers and citations unchanged.
RISK: number-adjacent

### EDIT P2-17 [replace]
ANCHOR: International assessments: PISA mathematics and reading
SECTION: Verifying the Decline > International context (fig:intl caption)
PROPOSED: \caption{International assessments: PISA mathematics and reading (U.S. vs.\ OECD average) and U.S. TIMSS mathematics. The OECD-average declines begin before the pandemic; U.S. TIMSS falls in step with NAEP. Data: NCES/OECD publications.}
WHY: Caption self-containedness — adds the what-to-see sentence (pre-pandemic OECD decline, TIMSS-NAEP agreement) before the source.
RISK: none

### EDIT P2-18 [replace]
ANCHOR: Two further populations complete the picture
SECTION: Verifying the Decline > Seniors and adults
PROPOSED: Two further populations complete the picture, and both carry unusual inferential weight because the usual school-policy explanations apply to them weakly or not at all. Grade 12 NAEP (2024 results released in September 2025) shows the same pattern as the younger grades. Mathematics peaked in 2013 (153.5), drifted down through 2019 (150.3), and fell to its lowest level ever recorded in 2024 (146.9), with 2019--2024 losses of 5 points at the 10th percentile against no significant change at the 90th. Reading fell to its own record low (282.6); its 1992--2024 percentile changes ($-24$ at the 10th percentile, $-2$ at the 75th) are the three-decade version of the bottom-collapse \citep{nces2025g12}.\footnote{Grade 12 weighted student participation was 68\% in 2024, well below the grades 4/8 rates; G12 levels warrant more caution than the younger-grade series.}
WHY: D8 — splits a ~75-word sentence into three; footnote, citation, and every number preserved verbatim.
RISK: number-adjacent

### EDIT P2-19 [replace]
ANCHOR: More striking is the adult evidence.
SECTION: Verifying the Decline > Seniors and adults
PROPOSED: The adult evidence is the more telling of the two. The 2023 PIAAC assessment of adults aged 16--65 \citep{ncespiaac2024,oecd2024adult} found U.S. literacy down 12 points from 2017 and numeracy down 6. The decline was concentrated almost entirely at the bottom: the share at or below Level~1 rose from 19\% to 28\% in literacy and from 29\% to 34\% in numeracy, while the share at Levels 4--5 was stable. The same happened across the OECD: literacy fell in 19 OECD countries between 2012 and 2023, with the bottom decile declining and the top decile improving in most. Adults are not subject to school accountability, the Common Core, school funding, teacher quality, or school absenteeism. A force that simultaneously lowers the floor of measured literacy and numeracy among 40-year-olds in nineteen countries and among 13-year-olds in American public \emph{and} Catholic schools is, almost by construction, not an education-policy variable. \citet{malkus2025theories} flagged the adult parallel using earlier PIAAC rounds as one of his four keys; the 2023 cycle sharpens it.\footnote{NCES cautions that cross-cycle PIAAC comparisons involve assessment and scoring changes; the trend-comparable estimates show the same pattern with a smaller literacy decline (9 points).}
WHY: D8 — splits a ~70-word em-dash sentence into three, trims "More striking" and "considerably"; the "almost by construction" rejection-side inference is deliberately preserved (see front matter), substance untouched.
RISK: number-adjacent

### EDIT P2-20 [replace]
ANCHOR: Any successful explanation must account for: (F1)
SECTION: Verifying the Decline > Summary of facts to be explained
PROPOSED: The preceding subsections establish eight facts. Any successful explanation must account for: (F1) a peak in 2012--2013 and slow decline through 2019; (F2) pre-2019 losses concentrated overwhelmingly at the bottom of the distribution, with the top flat or rising; (F3) a large, across-the-distribution drop in 2019--2022; (F4) continued post-2022 decline in reading and at the bottom of the adolescent distributions, against recovery at the top and (first visible in the 2025 LTT) a bottom-led rebound among 9-year-olds; (F5) declines within every demographic group and nearly every state; (F6) similar pre-pandemic declines across many rich countries; (F7) record-high achievement inequality; and (F8) the same bottom-concentrated decline among high-school seniors and, in PIAAC, among adults across the OECD, populations to which most school-policy explanations do not apply.
WHY: D8 + role instruction — adds a topic sentence, replaces the two em-dash pairs with parentheses/commas; F-numbering and content preserved exactly (load-bearing for the scorecard and synthesis, including A3's new row).
RISK: number-adjacent
