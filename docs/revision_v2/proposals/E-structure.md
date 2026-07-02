# E-structure — section architecture and organization proposal (D9)

**Summary.** This proposal keeps the top-level section count and order intact (12 sections, zero claims-audit renumbering), rejecting the §5-merge and the H7-fold in favor of cheaper structural fixes: an expanded Candidate Explanations section with signposting, H7 kept as a re-headed pointer to H2's displacement pathway (endorsing A4-4/A4-5), and the set-aside subsection relocated from Mechanism Checks to the end of Testing the Hypotheses where candidate triage belongs. The verdicts/synthesis/conclusion triple-redundancy is resolved by making Synthesis own the ranking, cutting the Conclusion's five-fact re-argument, and moving the Synthesis-final implications paragraph into a rebuilt two-paragraph Conclusion that incorporates A1-28's calibration sentence verbatim. Three misplaced figure blocks in §8 are moved to their referencing paragraphs (also repairing an out-of-order figure-number/reference sequence), a roadmap paragraph is added to the introduction end, and A2-1's Sharper Tests intro is confirmed in the slot A2 chose.

## Top-3 structural recommendations

1. **Do not merge §5 (Candidate Explanations) into §6, and do not fold H7 into H2.** The merge shifts every §6–§12 key in `evidence/claims_audit.md` (26 rows; full contingency table in Part 4 below) to buy nothing the cheaper fix — a two-sentence closing signpost paragraph that de-orphans §5 — doesn't already buy. The fold would break the H1–H8 numbering used by the scorecard, the audit's "§6 H2"-style keys, and the abstract, while bloating the paper's longest subsection; the re-headed pointer (A4-4 heading + A4-5 body) achieves the repositioning at zero blast radius.
2. **Synthesis owns the ranking; the Conclusion becomes findings-in-one-breath plus implications.** Cut the Conclusion's five-fact ranking re-argument (it appears in §7.6 and §9 already — this is the main D9(c)/length harvest), keep A1-28's self-contained calibration sentence, and move the "Three implications follow" paragraph from the end of §9 into the Conclusion as its second paragraph (with A4-9's terminology substitution applied in transit). EDIT E-13/E-14 below supersede A1-28 by incorporation.
3. **Move §8.4 "Avenues examined and set aside" to the end of §6 (new §6.9), and move the three stranded figure blocks (`fig:tuda`, `fig:dose`, `fig:absence`) up to their referencing paragraphs.** The set-asides are rival-candidate triage, not a phase-two channel check; placing them after H8 (which, post-A3, ends on the mental-health rival) completes the candidate-triage story inside the section that does candidate triage, and makes A3-4's `\ref{sec:setaside}` signpost near-adjacent. Verified: **zero** claims-audit rows key §8.4 or any §6.x subsection number, so this move renumbers nothing the audit uses. The float moves fix a real defect: `fig:dose` (currently Figure 16) is referenced before `fig:tuda` (currently Figure 15), so figure numbers appear out of order in the text; after the move the reference order and numbering agree.

## Deliberately left alone (and why)

- **§7.6 "What the tests jointly imply"** — A2-11 rewrites it (D4); architecturally it stays where it is, as the tests-level summary distinct in altitude from §9's all-evidence ranking. No structural change needed.
- **§9 Synthesis phase-one / dual-criterion paragraphs** — A1+A2+A3 merged zone. One structural note for the reconciler: after A2-11 lands, the §9 phase-one paragraph's four-fact enumeration (A1-26 zone) duplicates A2-11's ¶2 nearly item-for-item; recommend the reconciler compress the §9 version to one clause plus `Section~\ref{sec:sharper}` pointer. I do not issue an edit because the merged wording is theirs.
- **§7.3/§7.5 heading pair** — three proposals exist (A1-24, A2-2+A2-7, A4-6). **Adjudication: adopt A2-2 + A2-7**, the verbatim-parallel pair ("no detectable effect on the release-timing margin" / "no detectable effect on the arrival-timing margin"). It is the only variant that makes the D4 symmetry typographically impossible to miss, which is the adjudicated fix for critique point 2; it also preserves parallelism with the other three §7 headings (topic-colon-result). A1-24 and A4-6 should be withdrawn in reconciliation.
- **§8 section title and intro sentence** — A4-7 ("Channel Checks: Schooling Mode and Attendance") and A4-8 own these; endorsed. One rider if my E-9 move lands: A4-8's final clause "and the section closes with the avenues examined and set aside" must be dropped (rider text in E-9).
- **H8 internal order** — A3 places the mental-health block last in H8 (after grade inflation), with the dispatch intro first. Endorsed: §6 then ends H8 → mental health (strongest unresolved rival) → §6.9 set-asides → §7 sharper tests, which reads as escalating seriousness of triage.
- **Scorecard table (`tab:scorecard`) position** — top of §9, floats to a page top, referenced twice within the section; fine. A3-6 adds one row; no placement change needed.
- **D10 version stamp/disclosure** — P1's zone (preamble).
- **Abstract structure** — A1-1's zone. One flag: A1-1 should mirror A4-7's "Channel Checks" rename if it survives (the current abstract says "Two mechanism checks complete the picture").

---

# Part 1 — Section-architecture assessment (the five D9 flagged candidates)

**Current architecture** (sections §1–§12; labels in parentheses): 1 Introduction; 2 Related Work (sec:related); 3 Data; 4 Verifying the Decline (sec:verify, 8 subsections); 5 Candidate Explanations (one paragraph + enumerate); 6 Testing the Hypotheses (H1–H8 = §6.1–§6.8); 7 Sharper Tests (sec:sharper, 5 tests + jointly-imply); 8 Mechanism Checks (sec:mechanism, 4 subsections); 9 Synthesis (sec:synthesis); 10 Limitations; 11 Verification (sec:verification); 12 Conclusion.

## (a) Merge Candidate Explanations into Testing the Hypotheses — **REJECTED**

The merge deletes a top-level section, shifting §6→§5, §7→§6, §8→§7, §9→§8, §10→§9, §11→§10, §12→§11. `evidence/claims_audit.md` keys 26 rows to those numbers (list in Part 4). Non-negotiable 5 demands a compelling reason for changing the section count; the only benefit — de-orphaning a one-paragraph section — is fully captured by EDIT E-5, which adds a closing signpost paragraph to §5 (openness of the list + pointers to A3's reader-proposed-candidates block in `sec:h8` and to `sec:setaside`). With A3-1 also extending the H8 enumerate item and E-9 moving the set-asides adjacent, §5 stops being an orphan and becomes the natural landing page for a reader arriving from the critique asking "what about X?". §6 needs no new intro paragraph: §5's closing paragraph is the bridge, and §6.1 opens two lines later.

## (b) H7: fold into H2 vs. re-headed pointer — **KEEP as §6.7 with re-headed pointer** (endorse A4-4 + A4-5)

Folding H7 into H2 would: (i) desynchronize the clean §6.k = Hk correspondence and delete a scorecard row just as D5 adds one (churning the paper's signature device in two directions at once); (ii) orphan the audit-style "H7"-free keying only by luck while breaking the H1–H8 enumeration cited in the abstract, §5, §9, and Table 2; (iii) push H2 — already the longest subsection, gaining A4's ~180-word taxonomy and A3-2's age-gradient paragraph — past readable length. The paper already states H7 is H2's pathway; the structural fix is to make the heading say so. **Adjudication among the three claimants:** adopt **A4-4** heading ("H7: Declining reading practice --- H2's displacement pathway, measured directly" — it states the repositioning, which is the point of D9(b)) and **A4-5** body (which adds the `\ref{sec:h2}` pointer and D6 terminology), with A1 harmonizing the closing Assessment line's wording during reconciliation. A1-17/A1-18 are superseded. H7 does not move physically (moving it next to H2 would break §6.k = Hk). I issue no H7 edit of my own; this decision is the deliverable.

## (c) Verdicts / synthesis / conclusion triple-redundancy — **what moves where, what gets cut**

The ranking is currently argued four times: per-hypothesis Assessment lines (§6, stays — A1 recalibrates), §7.6 (stays — A2-11's rewrite is the tests-level summary), §9 phase-one + dual-criterion (stays — Synthesis **owns the ranking**), and §12 (cut). Concretely:

- **CUT** from the Conclusion: the five-fact re-argument ("the losses arise during adolescence... appear identically in Catholic schools... show no relationship to when states were released from NCLB... recur across the rich world... coincide with a halving of voluntary reading"). Every clause repeats §7.6/§9 verbatim-in-substance; no unique numbers are lost (the "halving" appears at lines 231/288). This is the main D9(c) length harvest.
- **MOVE** the "Three implications follow" paragraph from the end of §9 into the Conclusion as ¶2, verbatim except A4-9's substitution ("digital-media mechanism" → "digital-media hypothesis and its pathways"), which is applied in transit (A4-9 then moot). §9 ends on the phase-two paragraph, handing off cleanly to Limitations; the Conclusion becomes: one calibrated findings paragraph (incorporating A1-28's load-bearing calibration sentence verbatim) + one implications paragraph + the existing final policy sentence as closer.
- **Supersession:** E-14 incorporates and supersedes A1-28 (per A1's own front-matter rec 2, which anticipated exactly this cut). P6 styles what remains.

## (d) End-of-introduction roadmap — **drafted (EDIT E-1)**

One paragraph, inserted after the current epistemics paragraph (line 44). Sequencing is load-bearing: A1-2 *replaces* that same paragraph, so **E-1 must be applied before A1-2** (insert-after leaves the anchor line intact for A1-2's subsequent replace). Final order in the intro: ¶1 the reversal, ¶2 what the report does, ¶3 A1-2's inferential-strategy paragraph, ¶4 roadmap. The roadmap references only labeled sections; EDITs E-2/E-4/E-6 add the three missing labels (`sec:data`, `sec:candidates`, `sec:testing`) so no hard-coded section numbers can go stale. It deliberately does not restate the symmetry contract (A1's rec 3: state it once, in the Sharper intro) — it maps, it does not argue.

## (e) Placement of A2's Sharper Tests intro — **confirmed: replaces the stale one-liner at the top of §7 (A2-1's slot)**

A2-1 replaces "The verdicts above lean on timing and incidence..." at the section top, before §7.1 — the correct and only placement: the symmetric-standard promise must be read before either null, not inside one of them. A2-1 also fixes the stale count (the paragraph says "three tests"; the section has five test subsections). **Adjudication:** A2-1 wins the three-way collision on that paragraph (A1-22 is subsumed — the rename is included; P4's style version layers on top or yields). One companion structural fix is mine: the §7 section *heading* still reads "...and Policy Variation," which excludes the 4G rollout design; EDIT E-7 retitles to "...Policy and Rollout Variation" (label `sec:sharper` untouched, next line).

---

# Part 2 — Figure and table placement sanity check

| Float | Defined | First referenced | Status |
|---|---|---|---|
| `fig:national` (1), `tab:changes` (T1) | §4.1 | §4.1 | OK |
| `fig:ltt` (2) | §4.2 | §4.2 | OK |
| `fig:pctile` (3), `fig:lttpct` (4), `fig:gap` (5) | §4.3 | §4.3 | OK |
| `fig:lunch` (6) | §4.4 | §4.4 | OK |
| `fig:states` (7) | §4.5 | §4.5 | OK |
| `fig:intl` (8) | §4.6 | §4.6 | OK |
| `fig:fun` (9) | end of §6.2 (after the Assessment line) | §6.2 timing paragraph | Acceptable — same subsection; `[section]` placeins scopes floats to §6; leave (H2 is a heavy A3/A4 edit zone) |
| `fig:cohort` (10), `fig:pubcath` (11), `fig:waiver` (12), `fig:cc` (13), `fig:fourg` (14) | own subsections | own subsections | OK |
| `fig:tuda` (15) | **after §8.4** | §8.1 ¶2 | **DEFECT — fix (E-10)** |
| `fig:dose` (16) | **after §8.4** | §8.1 ¶1 | **DEFECT — fix (E-11); also referenced (16) before `fig:tuda` (15): number/reference order inverted** |
| `fig:absence` (17) | **after §8.4** | §8.2 ¶1 | **DEFECT — fix (E-12)** |
| `tab:scorecard` (T2) | top of §9 | §9 ¶1 | OK |

The three §8 float blocks sit after the set-aside subsection, two subsections downstream of their references; since LaTeX cannot place a float earlier than its source position, they cannot land on the pages where they are discussed. E-10/E-11/E-12 move each block to immediately after its referencing paragraph. Post-move file order (dose, tuda, absence) makes reference order equal numbering order (15, 16, 17). Also noted, not fixed (content matter): `fig:dose`'s right panel (absenteeism vs. net change) is never explicitly referenced in the text; flag for P5.

# Part 3 — Heading-parallelism audit

House pattern: *sentence-case, "Topic: finding/evidence" colon form* for evidence subsections; plain noun phrases for function subsections (Summary of facts / What the tests jointly imply / Avenues examined and set aside — consistent as a class; leave).

| Heading | Pattern status | Action |
|---|---|---|
| §4.1, §4.3–§4.7 | colon form | OK |
| §4.2 "The Long-Term Trend assessment confirms the timing" | only §4 evidence heading without colon | E-3 retitles (form only; A1 judged the claim T1-licensed) |
| §6.1–§6.8 "Hk: name --- descriptor" | consistent frame | Keep the frame; A1 owns descriptor recalibration (D1). Recommend to A1: uniform *evidence-examined noun phrases* after the em-dash, as in D1's own H2 example |
| §7.1, §7.2, §7.4 | colon + result (T1) | OK |
| §7.3 vs §7.5 | asymmetric (accountability's null headlined; 4G's null euphemized as "a first...test") | Adopt **A2-2 + A2-7** matched pair (adjudicated in Part 1e); A1-24/A4-6 withdrawn |
| §8.1, §8.2 | colon + result | OK |
| §8.3 "Could it be test-taking effort rather than skill?" | only question-form heading in the paper | E-8 retitles to colon form (droppable; P5 may re-style) |
| §8 section title | undersells contents; D6 terminology | A4-7 endorsed ("Channel Checks..."); with E-9, contents become exactly schooling mode + attendance + effort, so A4-7's title needs no further extension |

# Part 4 — CRITICAL constraint check: claims-audit keying (non-negotiable 5)

`evidence/claims_audit.md` keys rows to §numbers (§4.1...§8.3, §10, §3, "§5 H2", "§6 H1/H2/H3/H6"), plus a few float numbers ("Fig 1/9/11/13", "Figs 4–5", "Table 1/2"). Verified by grep against the audit (59 table lines): **no rows key §7.6, §8.4, §9, §11, §12, H7, or §6 H8.**

Per-edit numbering impact of THIS proposal:

- **E-1 through E-8, E-13, E-14:** no §/subsection numbering changes; no audit updates.
- **E-9 (§8.4 → new §6.9):** §6 gains a ninth subsection (audit uses "§6 Hk" keys, never §6.x — unaffected); §8.1–§8.3 keep their numbers (§8.4 was last — rows C1–C7 unaffected); `sec:setaside` label travels with the block, so the file's one prose `\ref{sec:setaside}`-style pointer (A3-4's new one) resolves. **Zero audit updates required.**
- **E-10/E-11/E-12 (float moves):** figure numbers swap: dose 16→15, tuda 15→16 (absence stays 17). Audit row **C1** (line 55) says "compare Fig 13 scatter" — already stale in v1.9 (the dose scatter is currently Fig 16); **update C1 to "Fig 15"** once the move lands. Pre-existing staleness found in passing, unrelated to any E edit: row **B4** (line 39) says "eyeball Fig 11 left panel" but the waiver figure is currently Fig 12 — **update B4 to "Fig 12"** regardless of this proposal. Row A14's "§5 H2" is also stale under current numbering (H2 is §6.2) — fix to "§6 H2" (or leave, if the reconciler adopts the merge I reject).
- **Contingency (only if the reconciler overrides Part 1a and merges §5 into §6):** all top-level numbers from §6 down shift by −1, requiring these audit location updates: B1 (§7.1→§6.1); B2, B3 (§7.2→§6.2); B4, B5 (§7.3→§6.3); B6 (§6 H3→§5 H3; §7.3→§6.3); B7 (§7.3→§6.3; §3 unchanged); B8, B9 (§7.4→§6.4); B10, B11 (§6 H1→§5 H1); B12, B13 (§6 H6→§5 H6); B14 (§6 H2→§5 H2); C1, C2 (§8.1→§7.1); C3, C4, C5 (§8.2→§7.2); C6, C7 (§8.3→§7.3); C8 (§10→§9); D1–D4 (§6 H2→§5 H2); A14's "§5 H2" becomes coincidentally correct. 26 row edits — the cost that motivates the rejection.

---

# Part 5 — Edits (document order)

### EDIT E-structure-1 [insert-after]
ANCHOR: The analysis is descriptive and abductive rather than causal in the experimental sense
SECTION: Introduction (new final paragraph: roadmap, D9(d))
PROPOSED: The report proceeds as follows. Section~\ref{sec:related} places the contribution in the existing literature, and Section~\ref{sec:data} describes the data. Section~\ref{sec:verify} verifies the decline directly and distills it into eight facts (F1--F8) that any explanation must fit. Section~\ref{sec:candidates} lists the eight candidate explanations, and Section~\ref{sec:testing} assesses each against those facts, hypothesis by hypothesis. Section~\ref{sec:sharper} then reports five sharper tests built from cohort structure, school sector, and policy and rollout timing; Section~\ref{sec:mechanism} checks the phase-two channels (schooling mode, attendance) and asks whether falling test-taking effort could account for the measured decline. Section~\ref{sec:synthesis} assembles the scorecard and states the resulting ranking. Limitations, the verification record (Section~\ref{sec:verification}), and a short conclusion close the report.
WHY: D9(d) — roadmap at the end of the introduction; counts ("eight", "five") verified against the file's own structure; no argumentative content (symmetry contract stated once, in A2-1, per A1 rec 3).
RISK: collides:A1 — MUST be applied BEFORE A1-2, which replaces the anchor paragraph (insert-after preserves the anchor for A1-2's later replace); cross-ref — depends on E-2/E-4/E-6 labels landing.

### EDIT E-structure-2 [replace]
ANCHOR: \section{Data}
SECTION: Data (section heading; adds label)
PROPOSED: \section{Data}\label{sec:data}
WHY: D9(d) infrastructure — lets the roadmap reference the section without a hard-coded number.
RISK: none

### EDIT E-structure-3 [replace]
ANCHOR: \subsection{The Long-Term Trend assessment confirms the timing}
SECTION: §4.2 heading (label sec:ltt on next line, untouched)
PROPOSED: \subsection{The Long-Term Trend assessment: the same timing on unchanged content}
WHY: Part 3 parallelism — the only §4 evidence heading without the paper's topic-colon-finding form; claim content identical (A1 judged it T1-licensed; this is form only).
RISK: collides:P2 (style zone) — droppable without consequence.

### EDIT E-structure-4 [replace]
ANCHOR: \section{Candidate Explanations}
SECTION: Candidate Explanations (section heading; adds label)
PROPOSED: \section{Candidate Explanations}\label{sec:candidates}
WHY: D9(a) — section kept (merge rejected); label enables roadmap and future cross-refs.
RISK: none

### EDIT E-structure-5 [insert-after]
ANCHOR: \end{enumerate}
SECTION: Candidate Explanations (new closing paragraph after the H1–H8 list)
PROPOSED: Two notes bound this list. It is drawn from the explanations prominent in research and public debate, and it makes no claim to exhaust the possible causes: the elimination logic used below is only as strong as the candidate set itself. And it is not closed. Candidates proposed by readers of earlier drafts (rising immigration, political polarization, school-discipline reform, and deteriorating adolescent mental health) are taken up with the other hypothesis assessments in Section~\ref{sec:h8}, and further avenues examined and set aside are recorded in Section~\ref{sec:setaside}.
WHY: D9(a) — de-orphans §5 at zero renumbering cost and gives the critique-reader a landing page; pure signposting, no substance (dispatch content is A3-4/A3-5's, in H8).
RISK: cross-ref — depends on A3-3 (`\label{sec:h8}`); if A3-3 is cut, replace "Section~\ref{sec:h8}" with "the closing block of the next section (H8)". collides:A3 (light; wording of the candidate list should track A3-4's).

### EDIT E-structure-6 [replace]
ANCHOR: \section{Testing the Hypotheses}
SECTION: Testing the Hypotheses (section heading; adds label)
PROPOSED: \section{Testing the Hypotheses}\label{sec:testing}
WHY: D9(d) infrastructure for the roadmap.
RISK: none

### EDIT E-structure-7 [replace]
ANCHOR: \section{Sharper Tests: Cohorts, Sectors, and Policy Variation}
SECTION: §7 section heading (label sec:sharper on next line, untouched)
PROPOSED: \section{Sharper Tests: Cohorts, Sectors, and Policy and Rollout Variation}
WHY: D9(e) companion — the current title omits the 4G rollout design, understating that the digital-media side also faces a timing test (the asymmetry critique point 2 names); matches A2-1's "policy and rollout variation" phrasing.
RISK: cross-ref — E-9's destination anchor is this heading's CURRENT text, so E-9 must be applied before E-7.

### EDIT E-structure-8 [replace]
ANCHOR: \subsection{Could it be test-taking effort rather than skill?}
SECTION: §8.3 heading (label sec:effort on next line, untouched)
PROPOSED: \subsection{Test-taking effort: a real wedge in levels, too small to explain the decline}
WHY: Part 3 parallelism — the paper's only question-form heading; replacement states the subsection's own computed bound in the house topic-colon-finding form.
RISK: collides:P5 (style zone) — droppable.

### EDIT E-structure-9 [move]
ANCHOR: \subsection{Avenues examined and set aside}
SECTION: §8.4 → end of §6 (new §6.9). Move the three-line block: the `\subsection{Avenues examined and set aside}` heading line, its `\label{sec:setaside}` line, and the paragraph beginning "Several further hypotheses were tested or scoped". DESTINATION: insert immediately BEFORE the line `\section{Sharper Tests: Cohorts, Sectors, and Policy Variation}` (current text; apply before E-7). If A3-5's mental-health block has already been inserted at the end of H8, the destination is unchanged (the section boundary), so the moved block lands after it, as intended.
PROPOSED: (block moved verbatim; no text changes)
WHY: D9 — set-asides are rival-candidate triage and belong at the end of the hypothesis-testing section, completing the sequence H8 dispatches → mental-health rival → set-asides; makes A3-4's `\ref{sec:setaside}` near-adjacent; verified zero claims-audit rows key §8.4 or §6.x. RIDER: if this lands, amend A4-8's proposed intro by deleting its final clause ", and the section closes with the avenues examined and set aside" (ending that sentence at "...falling test-taking effort.").
RISK: collides:A4 (the A4-8 rider); collides:P5 (owns §8 signposting). Label `sec:setaside` travels with the block; all refs resolve.

### EDIT E-structure-10 [move]
ANCHOR: \includegraphics[width=.95\textwidth]{fig_tuda.pdf}
SECTION: `fig:tuda` float block (the full `\begin{figure}[tbp]`...`\end{figure}` containing this anchor) → §8.1, immediately after the paragraph ending "blur a gradient that longitudinal growth data resolve." DESTINATION ANCHOR: blur a gradient that longitudinal growth data resolve
PROPOSED: (block moved verbatim)
WHY: Part 2 — float currently defined after §8.4, two subsections downstream of its only reference; with E-11 this also repairs the inverted figure-number/reference order in §8.1.
RISK: none (claims-audit impact of the resulting renumbering is recorded in Part 4: update C1 to "Fig 15").

### EDIT E-structure-11 [move]
ANCHOR: \includegraphics[width=.95\textwidth]{fig_doseresponse.pdf}
SECTION: `fig:dose` float block → §8.1, immediately after the paragraph ending "between-state variation in score declines." DESTINATION ANCHOR: between-state variation in score declines
PROPOSED: (block moved verbatim)
WHY: Part 2 — first-referenced float in §8.1 should be first in source order (becomes Figure 15, restoring reference-order numbering).
RISK: none

### EDIT E-structure-12 [move]
ANCHOR: \includegraphics[width=.95\textwidth]{fig_absence.pdf}
SECTION: `fig:absence` float block → §8.2, immediately after the paragraph ending "phase one was not an attendance phenomenon." DESTINATION ANCHOR: phase one was not an attendance phenomenon
PROPOSED: (block moved verbatim)
WHY: Part 2 — float defined after §8.4 cannot typeset near its §8.2 discussion.
RISK: none

### EDIT E-structure-13 [delete]
ANCHOR: Three implications follow
SECTION: §9 Synthesis, final paragraph (moved into the Conclusion by E-14, not lost)
PROPOSED: (delete the full paragraph line beginning "Three implications follow." — its entire content, with every number, citation, and the Mississippi sentence, reappears verbatim in E-14 ¶2, with only A4-9's terminology substitution applied)
WHY: D9(c) — Synthesis owns the ranking and ends on the phase-two paragraph; implications are the Conclusion's job. Non-negotiable 1(a) satisfied: nothing is deleted that E-14 does not restate.
RISK: collides:A4 (A4-9 global-substitute targets this line; satisfied-by-incorporation in E-14 — mark A4-9 moot if E-13/E-14 land); number-adjacent (numbers move, unchanged). Apply AFTER E-14.

### EDIT E-structure-14 [replace]
ANCHOR: The decline in American student achievement is real, large, and verifiable
SECTION: §12 Conclusion (full replacement: two paragraphs; supersedes A1-28 by incorporating its calibration sentence verbatim)
PROPOSED: The decline in American student achievement is real, large, and verifiable from primary data: roughly one grade level of learning lost at grade 8 since 2013, the lowest grade 8 reading scores ever recorded, and the widest achievement gaps in NAEP's history. It happened in two phases with different causes. For the pre-pandemic erosion, nearly invisible in averages because it was confined to the bottom of the distribution, the best-supported remaining candidate is the post-2012 saturation of adolescent life by smartphones and digital media; the evidence behind that ranking is assembled in Sections~\ref{sec:sharper} and \ref{sec:synthesis}. That conclusion is a ranking by consistency with the evidence, not a causal estimate; the pre-registered state phone-ban test against NAEP 2026 is the next opportunity to corroborate or overturn it, and adolescent mental-health deterioration remains an entangled rival these data cannot separate. The retreat from test-based accountability likely contributed at the margins, most visibly at the public-school grade 4 bottom decile, but failed the direct tests this report could put to it. The pandemic then imposed the largest schooling shock in modern history, whose effects, far from fading, have been locked in by chronic absenteeism that remains half again its pre-pandemic level. Funding cuts, demographic change, and teacher shortages are, on the evidence, second-order.

Three implications follow. First, ``COVID recovery'' framing understates the problem: grade 8 reading was already down 4.4 points before the pandemic, and the forces behind that slide are still operating. Second, because losses are concentrated at the bottom, average-score targets understate the equity emergency; the 90--10 gap is the widest ever measured. Third, with the policy-side explanations weakened by the tests of Section~\ref{sec:sharper}, the empirical frontier shifts to the digital-media hypothesis and its pathways, where causal evidence is accumulating: existing ban studies \citep{belandmurphy2016,abrahamsson2024,beneito2022,figlio2025} consistently find gains concentrated among low achievers, and the staggered adoption of U.S. state bans (roughly thirty states by 2025--26) against NAEP 2026 offers exactly the kind of test that waiver timing provided here---this project's repository pre-specifies the design and treatment coding. Mississippi's literacy reform remains the strongest evidence that aggressive instructional policy can buck the trend even if policy retreat did not cause it. The policy conclusion is uncomfortable but clear: returning to 2019 practices would only return the country to a trajectory that was already pointing down.
WHY: D9(c) — cuts the Conclusion's five-fact ranking re-argument (the triple-redundancy harvest; every cut clause is stated in §7.6/§9), keeps A1-28's calibration sentence verbatim, and receives §9's implications paragraph (E-13) with A4-9's substitution applied. ¶1 is A1-28 minus the re-argument; ¶2 is the moved paragraph plus the existing closer.
WHY-NOTE: the two NAEP-2026 mentions (¶1 epistemics, ¶2 policy frontier) serve different functions; P6 may trim one clause if it grates.
RISK: collides:A1 (supersedes A1-28 with A1's own blessing per their rec 2); collides:A3 (mental-health clause presumes D5 lands — strip the clause if D5 is cut); collides:P6 (styles the remainder); number-adjacent (all numbers carried verbatim from A1-28 and the moved paragraph).

---

# Part 6 — Sequenced move plan for the applier

Apply within this proposal in the following order (anchors are all verified unique in the CURRENT file; the order below keeps every anchor valid at its moment of use):

1. **E-10** — cut the `fig:tuda` block (6 lines around its `\includegraphics` anchor); reinsert after the paragraph ending "blur a gradient that longitudinal growth data resolve."
2. **E-11** — cut the `fig:dose` block; reinsert after the paragraph ending "between-state variation in score declines." (Resulting §8.1 source order: ¶1, dose block, ¶2, tuda block — reference order = numbering order.)
3. **E-12** — cut the `fig:absence` block; reinsert after the paragraph ending "phase one was not an attendance phenomenon."
4. **E-9** — cut the §8.4 block (heading + `\label{sec:setaside}` + "Several further hypotheses..." paragraph); reinsert immediately before `\section{Sharper Tests: Cohorts, Sectors, and Policy Variation}` (heading still carries its current text at this point). Apply the A4-8 rider (drop its final clause) whenever A4-8 lands.
5. **E-7** — retitle the §7 heading (only now, so step 4's destination anchor was valid).
6. **E-3, E-8** — subsection retitles (independent).
7. **E-2, E-4, E-6** — label additions (independent).
8. **E-1** — roadmap insert. MUST precede A1-2 (which replaces the anchor paragraph). If A1-2 has already been applied, insert the roadmap immediately after A1-2's replacement paragraph instead (same slot).
9. **E-5** — §5 closing paragraph insert (after `\end{enumerate}`; independent of A3-1's item replace on an earlier line; its `\ref{sec:h8}` requires A3-3 by compile time).
10. **E-14** — Conclusion replacement (before E-13, so the implications content is never absent from the file).
11. **E-13** — delete the §9 "Three implications follow." paragraph.

Cross-agent adjudications for the reconciler (restated): A2-1 wins the §7-intro three-way (A1-22 subsumed; P4 layers style only); A2-2+A2-7 win the null-heading pair (A1-24, A4-6 withdrawn); A4-4+A4-5 win H7 (A1-17, A1-18 superseded; A1 harmonizes the Assessment line); E-14 supersedes A1-28; A4-9 moot after E-13/E-14; A4-7 endorsed with the abstract-mirror flag for A1-1; A4-8 endorsed with the E-9 rider. Claims-audit updates required by this proposal: C1 "Fig 13"→"Fig 15" (after step 2); recommended regardless: B4 "Fig 11"→"Fig 12", A14 "§5 H2"→"§6 H2". Verify with `cd report && tectonic report.tex` after application; all moved labels (`sec:setaside`, `fig:tuda`, `fig:dose`, `fig:absence`) travel with their blocks, and every existing `\label{}` survives.
