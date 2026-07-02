# Revision v2.0 Charter — editorial direction for the critique-response revision

*Orchestrator: main session, 2026-07-02. Every swarm agent reads this document in full before touching anything. It is the single source of alignment. If an instruction here conflicts with your own judgment about a local passage, propose your alternative and flag it — do not silently deviate.*

## Mission

Revise `report/report.tex` so that it (1) resolves an external written critique where that critique is correct, (2) makes the paper's existing answers impossible to miss where the critique is factually wrong about the paper, and (3) substantially upgrades organization and line-level clarity throughout. The revision changes what the paper **claims** and how it **reads** — never what it **found**.

## Non-negotiables (binding on every agent)

1. **NUMBERS FROZEN.** No numeric value in the paper (estimate, SE, p-value, percentage, count, year, MDE) may be altered. Numbers may only be (a) deleted as part of removing a passage that repeats them verbatim elsewhere, or (b) added from Agent A3's web-verified list (each with URL). If your rewrite touches a sentence containing a number, carry the number through unchanged.
2. **FINDINGS FROZEN.** Calibration changes strength-of-claim language, not results. No analysis is reversed, no estimate reinterpreted as its opposite.
3. **CITATIONS.** Never invent a citation. Existing `\citep`/`\citet` keys stay attached to the claims they support. New references come only from A3's verified list (URL + access date), added to `refs.bib`.
4. **LABELS.** Every existing `\label{}` survives. All `\ref`/`\autoref` must resolve after any move. Cross-references are checked at verify time.
5. **SECTION NUMBERING.** `evidence/claims_audit.md` keys 42 rows to section numbers (§4.1, §5.2, ...). Do not change the top-level section count or order without a compelling reason; if any structural move shifts §/subsection numbers, the edit plan MUST include the corresponding claims-audit location-column updates.
6. **LENGTH.** Net growth ≤ ~2 compiled pages. New content (mental health, mechanism taxonomy, inferential strategy) is paid for by cutting redundancy (the verdicts/synthesis/conclusion triple-statement is the main harvest).
7. **GENRE.** This remains a research report with a hypothesis scorecard and per-hypothesis assessments, written for skeptical academic readers. Keep the device; fix the register.
8. **DO NOT CAPITULATE** to critique points the adjudication below marks as factually wrong. The fix for those is signposting and explicitness, not deletion or hedging of correct material.
9. **COMPILE.** `cd report && tectonic report.tex` must pass. No new packages.
10. **PHASE 1 IS READ-ONLY.** Diagnostic agents write proposals to `docs/revision_v2/proposals/`; nobody edits `report.tex` until the reconciled plan is approved.
11. The tex file uses one physical line per paragraph. Prefer whole-paragraph rewrites: one edit = one full paragraph (or heading) replaced. Anchors are verbatim substrings of the current line, ≤120 chars, unique in the file.

## The critique (paraphrased)

*The review is presented here in paraphrase; the reviewer's text is not reproduced verbatim in this public repository. The substance is preserved point for point, in the review's order and emphasis, and agents treated this section as the authoritative statement of what must be answered.*

The review identifies two major problems.

**First, inferential overreach.** The paper, it argues, conflates consistency with causation and misapplies core research concepts, overinterpreting its analyses. Describing the smartphone hypothesis as the explanation most consistent with the evidence would be acceptable as a worth-investigating-further inference, but the paper treats it as the most likely causal explanation. Many social changes accelerated over the 2010s (deteriorating adolescent mental health, rising political polarization, rising immigration, shifts in school discipline), and the paper establishes only that smartphones are compatible with several observed patterns, not that they outperform every alternative. A related conceptual error: a smartphone is a technology, not a mechanism. If devices depress achievement they do so through some pathway (reduced attention; attention effects that changed classroom practice, such as less homework assigned; degraded self-regulation; or something else), and for a paper about mechanisms, the paper never engages the question.

**Second, asymmetric standards of evidence.** The elimination procedure applies a stronger standard to rival explanations than to the preferred one. The accountability hypothesis is heavily discounted on the strength of a null waiver-timing test, while the paper's own null 4G-rollout test is excused on the ground that the smartphone effect may run through national adoption rather than local rollout timing: the rival faces direct policy-variation tests while the favored hypothesis survives its null. The international evidence shares the flaw: synchronized declines across countries are compatible with many globally shared phenomena, not distinctively with smartphones. The residual explanation ends up held with confidence the analysis does not warrant, which the reviewer identified as the sharpest divergence between AI-produced and researcher-driven inference.

**Finally, register.** The reviewer would reject a working paper that combined the problems above with the paper's confidence-bearing language: the verdict framing, "best explained by," the claim that smartphones are the explanation most consistent with the full pattern, and the "almost by construction" construction (all of these are the paper's own v1.9 phrases).

## Adjudication (orchestrator's editorial direction — this is what we act on)

**Lands — fix it:**
- The headline/assessment register outruns what an observational elimination exercise can license. The hedges exist but live in Limitations while the abstract, assessment lines, synthesis, and conclusion carry more confidence. Fix globally with the claim ladder (D2) and by moving the epistemic framework up front (D3).
- The two nulls (waiver vs. 4G) receive visibly different rhetoric even though the underlying logic is parallel. Fix with symmetric construction (D4).
- Adolescent mental health is a genuine unaddressed rival that plausibly clears the paper's own dual-criterion test. Add it honestly (D5).
- "Smartphones" names a technology, not a pathway. The paper has pathway evidence scattered through it but never assembles a taxonomy or says plainly that it does not adjudicate among pathways. Fix (D6).
- Tone: "Verdict," "best explained by," assertive subsection titles. Recalibrate (D1, D2, D8).

**Does not land — surface the existing answer, don't delete substance:**
- On the charge that the paper misunderstands research inference: the paper already states its observational status precisely (Limitations opening). The fix is placement and voice — own the inferential strategy in the introduction — not concession.
- On the charge that the smartphone hypothesis is permitted to survive its null: the 4G null was self-administered adversarial evidence, run by this project against its own leading candidate, and reported prominently. Frame it that way. And the direct policy-variation test on the smartphone side is the quasi-experimental ban literature plus the pre-registered NAEP-2026 state-ban test — the exact analog of the waiver test. Say this where the reviewer looked for it.
- On the summary of the waiver logic (no effect found, therefore accountability minor): incomplete reading — the waiver section already concedes the national-channel escape hatch in nearly the same words the 4G section uses. Make the parallelism typographically impossible to miss (D4).
- Immigration is handled by the within-group results and the composition bound; school discipline is explicitly set aside as untested. Make both findable via signposting (D5 dispatch).

**Bonus fix the reviewer missed:**
- The paper leans on adolescent-specificity while also citing the adult PIAAC decline as confirmation. Resolve explicitly: the age profile is a dose/development gradient, not a cliff; the fertility literature's adults-null concerns births, not skills (D7).

## Global decisions

**D1 — Rename the assessment device.** "**Verdict.**" → "**Assessment.**" in every hypothesis block, and replace running-prose uses of "verdict" (abstract, related work, synthesis, README-facing text is out of scope) with calibrated alternatives. Subsection titles that assert conclusions ("--- the best fit to...") are in scope for recalibration: keep informative headings, but they must describe the evidence examined, not pre-announce the winner (e.g., "H2: Smartphones and digital media --- timing, breadth, and the ban literature").

**D2 — Claim-strength ladder.** Use these verb families; the tier is set by the evidence behind the sentence:
- T1 verified data description: "shows," "is," "fell," "the widest on record."
- T2 external causal literature: "causal evidence indicates/finds."
- T3 this report's quasi-experimental nulls: "we find no detectable effect; the design rules out effects larger than [MDE] on this margin" — never "rules out the hypothesis."
- T4 associations (PISA gradients, dose-response): "is associated with," "consistent with," "cannot bear causal weight alone."
- T5 synthesis ranking: "the leading candidate," "the best-supported remaining candidate," "the explanation the discriminating tests consistently favor, pending the pre-registered 2026 test."
- BANNED at T5: "best explained by," "the verdict," "confirms/establishes" (for H2-level claims), "uniquely predicts" (soften to "is the only candidate examined here that predicts").

**D3 — Inferential-strategy paragraph** (new, introduction, ~150 words; A1 drafts). States the method in our own voice: enumerate candidates → derive discriminating predictions → test them against the variation that exists → run or pre-register direct tests where possible. States plainly: the output is a *ranking of candidate explanations by consistency with evidence*, not a causal estimate; consistency is a screen, not proof; the candidate set is open; and the report's strongest claims are therefore about which explanations the evidence *rejects*. This is where "we know consistency ≠ causation" lives, up front.

**D4 — Symmetry template.** §sec:waiver and §sec:fourg each get the same five-beat structure, in the same order, with matched sentence frames: (i) what varies and why it identifies anything; (ii) what margin the design identifies; (iii) result with MDE against the relevant benchmark; (iv) which FORM of the hypothesis the null rejects ("the strong form, in which..."); (v) which channel survives by construction (national/anticipated channels absorbed by year effects — same clause structure in both sections). "What the tests jointly imply" is rewritten symmetric: both strong local forms are rejected by timing tests; H2's remaining advantage rests on its positive evidence (timing, exposure gradients, international + adult synchrony, ban studies), not on surviving elimination; explicit sentence that elimination arguments are only as strong as the candidate list, which stays open. Note in H2 or §jointly that the ban literature (and the pre-registered 2026 test) is the smartphone-side direct policy-variation test, and that the 4G design was this project's own adversarial test of its leading candidate.

**D5 — Mental-health rival + dispatch of other proposed candidates** (A3 owns content; web-verify everything).
- New block in H8 (~200 words): adolescent mental-health deterioration as an independent rival. Expected facts to verify (do NOT trust these from memory; fetch and confirm exact values + URLs): CDC YRBS persistent sadness/hopelessness trend 2011→2021; Mojtabai/Olfson/Han (2016, *Pediatrics*) adolescent MDE prevalence rise. Honest assessment: right timing; international; adolescent-specific; clears the dual-criterion screen; plausibly entangled with H2 in both directions (the rollout literature already links the same shock to teen mental health — abrahamsson2024, hudsonmoscoso2026); not separable with this report's data; the strongest unresolved rival. Scorecard gains one row. Synthesis dual-criterion paragraph acknowledges it as the other candidate that clears both bars, distinct from H2 mainly in whether devices are cause or covariate. Limitations gains one sentence.
- Dispatch sentences (one or two each, placed where a reader landing from the critique would look — likely the candidate-list section or H8 intro): rising immigration (addressed by within-every-group declines + 1–2 point composition bound + Catholic/international/adult breadth); political polarization (no articulated pathway to a bottom-concentrated, adolescent-specific, internationally synchronized decline extending to adults; US-centric in intensity). Respectful, one clause acknowledging these were proposed by readers of a draft.

**D6 — Mechanism taxonomy** (A4 owns; ~180 words in H2). Technology ≠ pathway. Name the candidate pathways: (i) time displacement (reading, homework, sleep); (ii) attention fragmentation (in-class distraction); (iii) social displacement (the fertility literature's in-person-interaction channel); (iv) degraded self-regulation. Map which existing evidence in the paper speaks to which pathway (reading-for-fun collapse → i; PISA distraction and notification items → ii; time-diary evidence → iii; ban-study heterogeneity → ii/iv). State plainly: the report establishes (at most) a reduced-form candidate and does not adjudicate among pathways; the policy conclusions (binding school-hours restrictions, attendance) do not require pathway adjudication, but the scientific account does, and that is where the empirical frontier is. Terminology discipline paper-wide: "smartphones/digital media" = the exposure; "pathway/channel" = how it would work; reserve "mechanism" accordingly (audit every occurrence; the section currently titled "Mechanism Checks" is about schooling mode and attendance — retitle if warranted, keeping labels).

**D7 — Age-profile gradient paragraph** (A3 owns, H2 and/or synthesis). Reconcile adolescent-specificity with the adult PIAAC decline: exposure hits all ages; adolescence combines peak dose with developmental sensitivity, so effects concentrate there without vanishing for adults; the fertility literature's adults-null concerns births, not skills. Soften any "strikes whoever is an adolescent" phrasing to acknowledge the adult margin explicitly.

**D8 — Style rules (all part editors):**
- Cut em-dash usage by at least two-thirds; at most ~1 per paragraph. Replace with periods, commas, colons, or parentheses as sense dictates.
- Split sentences over ~40 words unless the length is doing real work. The abstract's mega-sentences are the worst offenders.
- Abstract: restructure to ≤300 words (currently ~430), same facts, calibrated conclusion (T5 language), readable in one pass.
- Intensifiers ("critically," "strikingly," "dramatic," "remarkably") only where earned; cut most.
- Prefer active voice; keep the report's plain-spoken register; no new jargon.
- Topic sentences: each paragraph's first sentence states what the paragraph establishes.

**D9 — Organization appetite (E owns proposals; reconciler adjudicates):**
- Reorder/merge freely within sections; subsection moves allowed if clearly better; top-level section list stays recognizable (see non-negotiable 5).
- Flagged candidates to evaluate (not mandates): (a) merge the one-paragraph "Candidate Explanations" section into the opening of "Testing the Hypotheses"; (b) H7 (reading practice) explicitly repositioned as H2's displacement pathway — the paper already says this; decide whether to fold or keep with a re-headed pointer; (c) verdicts/synthesis/conclusion triple-redundancy: synthesis owns the ranking; conclusion shrinks to implications; (d) a one-paragraph roadmap at the end of the introduction; (e) "Sharper Tests" section intro promising the symmetric treatment (D4) so readers know the design standard applies to both sides.

**D10 — Version stamp and disclosure.** `\date` → v2.0, July 2, 2026. Add one sentence to the "How this report was produced" disclosure: v2.0 responds to a written external review with claim-strength calibration, symmetric treatment of the two null designs, an added rival-hypothesis analysis (adolescent mental health), and a full organizational and line-level edit; no analyses, estimates, or data changed.

## Ownership map (who owns substance where — style editors flag rather than duplicate)

| Passage | Substance owner | Notes |
|---|---|---|
| Abstract | A1 | full rewrite, ≤300 words |
| Intro inferential-strategy para | A1 | new (D3) |
| All Assessment lines + assertive headings | A1 | D1, D2 |
| §sec:waiver, §sec:fourg, "What the tests jointly imply" | A2 | D4 |
| Synthesis phase-one + dual-criterion paras | A1+A2+A3 | reconciler merges |
| H2 mechanism taxonomy | A4 | D6 |
| H2/synthesis age-gradient | A3 | D7 |
| H8 mental health + dispatches, scorecard row | A3 | D5 |
| H7 placement, section architecture | E | D9 |
| Everything else, line-level | P1–P6 | D8 |

## Part assignments (current line numbers of report/report.tex, 499 lines)

- **P1** lines 1–70: preamble, title/date (D10), introduction, Related Work, Data. Abstract content is A1's; P1 may flag but not rewrite it.
- **P2** lines 71–197: Verifying the Decline (7 subsections + summary-of-facts list).
- **P3** lines 198–297: Candidate Explanations + Testing the Hypotheses (H1–H8). Assessment lines and H2/H8 new content are owned above; style the rest.
- **P4** lines 298–384: Sharper Tests. §waiver/§fourg substance is A2's; style cohort/sector/Common Core + captions.
- **P5** lines 385–473: Mechanism Checks, set-asides, Synthesis. Signpost H8→set-asides; scorecard table notes.
- **P6** lines 474–499: Limitations (restructure the monolithic paragraph into thematic paragraphs), Verification (light touch), Conclusion (tighten; calibration is A1's).
- **E** whole file: structure only (D9), no line-level style edits.

## Output spec (Phase-1 agents)

Write your full proposal to `docs/revision_v2/proposals/<agent-id>.md`. For each proposed edit:

```
### EDIT <agent-id>-<n> [<type: replace | insert-after | delete | move | global-substitute>]
ANCHOR: <verbatim substring of the current line being targeted, ≤120 chars, unique in file>
SECTION: <section/subsection name>
PROPOSED: <complete final text, LaTeX-valid — the full new paragraph/heading, not a diff>
WHY: <one line, tied to a charter decision (Dn) or critique point>
RISK: <none | number-adjacent | cross-ref | collides:<agent-id>>
```

Front matter of the proposal: 3-sentence summary; top-3 structural recommendations; anything you deliberately left alone and why (if notable). Then the edits in document order. Return a short JSON summary as your final message (the harness enforces the schema).
