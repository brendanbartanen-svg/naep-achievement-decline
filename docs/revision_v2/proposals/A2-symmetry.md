# A2-symmetry — Proposal: symmetric treatment of the two null designs (D4, D9e)

## Summary

This proposal rebuilds §`sec:waiver` and §`sec:fourg` on the identical five-beat template of D4 — (i) what varies, (ii) the margin identified, (iii) result with MDE against the relevant benchmark, (iv) the strong local form the null rejects, (v) the national channel that survives by construction — with the beat-(iv) and beat-(v) sentences using verbatim-matched clause structures in both sections, plus matched headings, matched openers, and mirrored closing sentences and cross-pointers. "What the tests jointly imply" is rewritten per D4 into three paragraphs: both strong local forms rejected; H2's advantage resting on positive evidence rather than survival of elimination; the ban literature plus the pre-registered NAEP-2026 state-ban test named as the smartphone-side direct policy-variation analog of the waiver test; the 4G design framed as this project's self-administered adversarial test; and an explicit candidate-set-openness sentence. It also supplies the D9e symmetric-standard promise in the Sharper Tests section intro (fixing the stale "three tests" count — the section has five test subsections) and a shared-ownership rewrite of the Synthesis phase-one paragraph whose only A2 substance is the two-null treatment.

Every estimate, SE, p-value, MDE, date, and count in the affected passages carries through verbatim (anchors and frozen numbers verified by `grep -F` against the current file; all cross-referenced labels exist). Estimated net length impact of all twelve edits: roughly +520 words (~0.6 compiled page), of which ~270 is the jointly-imply rewrite; a compression option is offered below if the reconciler needs to claw back length.

## Top-3 structural recommendations

1. **Adopt the matched five-beat template as a locked pair.** Edits A2-2 through A2-10 make §waiver and §fourg structurally identical: matched headings ("no detectable effect on the release-timing / arrival-timing margin"), matched conditional openers ("If X drove the decline, ... supplies a test..."), the shared frame "The test is informative, not merely underpowered," verbatim-matched beat-(iv)/(v) clause structures, mirrored "Whatever X did to American students'/adolescents' learning..." closers, and reciprocal cross-pointers (waiver → fourg, fourg → waiver). If A1's heading scheme differs, the pair must still be changed *together* — the typographic parallelism is the fix the adjudication demands.
2. **Make "What the tests jointly imply" the single home of the symmetric-elimination statement and the candidate-openness sentence (A2-11); let Synthesis carry the ranking.** If the reconciler needs length back for D5/D6 content, compress my jointly paragraph 2 (the positive-evidence enumeration) to two sentences with cross-refs and keep the fuller enumeration only in the Synthesis phase-one paragraph (A2-12) — not the reverse, since D4 requires the "positive evidence, not survival of elimination" statement to live in jointly.
3. **Fix the Sharper Tests intro count while adding the D9e promise (A2-1).** The current intro says the section "reports three tests"; it contains five test subsections (cohort, sector, waiver, Common Core, 4G) plus the joint-implications summary. This is a stale structural count, not a data value; if E moves any subsection, re-verify the count at reconciliation.

## Deliberately left alone (and why)

- **H2 body, line 239 closing clause** ("a discipline on the hypothesis's mechanics ... rather than on its substance, since the national, adoption-driven channel ... is invisible to that design by construction"): substance overlaps my D4 remit but the paragraph is inside H2, where A4 (D6 taxonomy) and P3 (style) operate. Flagged below instead of edited; the fix is to recast in the two-form language.
- **Related Work, line 49 fourg sentence**: already symmetric ("returns a precise null on the arrival-timing margin while leaving the national and adoption margins open"). P1 may style; no substance change needed.
- **§`sec:commoncore` closing frame** ("what the test rules out is the strong claim that..."): already echoes the template; P4 styles. My jointly rewrite references it so the three nulls read as one standard.
- **Synthesis dual-criterion paragraph (line 466)**: A3 owns (mental-health rival amends "the only candidate examined here that clears both").
- **H1/H2/H3 Assessment lines, abstract, conclusion**: A1 owns; substance points supplied as flags below.
- **Limitations sentence on the waiver/4G caveats**: P6 owns the restructure; content is already parallel.

## Coordination flags (substance points for other agents; not rewrites)

- **A1 — H3 Assessment line must contain:** the waiver test finds no detectable effect on the release-timing margin (if numbers are quoted: MDE ~3.2 points / 0.35 SD pooled, less than half the Dee–Jacob NCLB-adoption gain, carried verbatim); it rejects the *strong local form* (formal release from NCLB consequences driving a state's low performers down); the *national* climate-shift channel culminating in ESSA survives by construction. Use the same clause structure as the H2 Assessment's 4G-null sentence so the symmetry extends to the assessment device itself.
- **A1 — H2 Assessment line must contain:** this project's own adversarial 4G test returns no detectable effect on the arrival-timing margin (MDEs 0.013/0.016 SD), rejecting the strong local form (harm riding on local infrastructure timing) while the national adoption channel survives by construction; H2's standing rests on positive evidence (timing, exposure gradients, international and adult synchrony, the reading collapse, ban studies), not on surviving elimination; the ban literature plus the pre-registered NAEP-2026 state-ban test is H2's direct policy-variation evidence, the analog of the waiver test; T5 ranking language ("the leading candidate ... pending the pre-registered 2026 test").
- **A1 — Abstract:** the current abstract reports the waiver null but omits the 4G null entirely — the reviewer's asymmetry complaint is visible from the abstract alone. The ≤300-word rewrite should carry both nulls in parallel language (one clause each suffices).
- **A1/P6 — Conclusion (line 495):** "is best explained by" is D2-banned at T5; the evidence list there cites only H3-adverse facts ("show no relationship to when states were released from NCLB") — either add the 4G self-test clause or rest the ranking explicitly on positive evidence.
- **A4/P3 — line 239:** recast "a discipline on the hypothesis's mechanics ... rather than on its substance" into the two-form language ("rejects the strong local-arrival form; the national adoption channel is invisible to that design by construction") so H2's own body does not read as excusing the null.
- **Optional:** add `\label{sec:jointly}` to the "What the tests jointly imply" heading if A1's Assessment lines want to cite it directly; nothing currently requires it.

---

## Edits (document order)

### EDIT A2-1 [replace]
ANCHOR: The verdicts above lean on timing and incidence.
SECTION: Sharper Tests (`sec:sharper`) — section intro
PROPOSED:

```latex
The assessments above lean on timing and incidence. This section reports five sharper tests, each exploiting a dimension of the data that the candidate explanations treat differently: a cohort-matched decomposition separating period effects from cohort effects, a sector comparison against Catholic schools that federal accountability never governed, and three timing designs built from policy and rollout variation (release from NCLB, Common Core adoption, and the arrival of high-speed mobile internet). The standard is symmetric by design. Each of the two leading phase-one hypotheses (H2 digital media, H3 accountability) faces a timing test built from its own variation and reported the same way: the margin the design identifies, the result with its minimum detectable effect, the form of the hypothesis the null rejects, and the channel that survives by construction.
```

WHY: D9e — the final two sentences are the promised symmetric-standard addition; also fixes the stale "three tests" count (the section has five test subsections) and anticipates D1 ("verdicts" → "assessments").
RISK: collides:P4 (style owner of this span) | number-adjacent ("three" → "five" is a count of the paper's own subsections, not a data value; verified against the current file)

### EDIT A2-2 [replace]
ANCHOR: \subsection{NCLB waiver timing: no state-level accountability effect}
SECTION: §5.3 heading (`sec:waiver`)
PROPOSED:

```latex
\subsection{NCLB waiver timing: no detectable effect on the release-timing margin}
```

WHY: D4 matched headings (pairs verbatim-parallel with A2-7) in D2-T3 language ("no detectable effect ... on this margin"); keep `\label{sec:waiver}` on its existing line untouched.
RISK: collides:A1 (owns assertive headings; the pair must move together)

### EDIT A2-3 [replace]
ANCHOR: The accountability hypothesis has a directly testable state-level implication
SECTION: `sec:waiver`, paragraph 1 — beats (i)–(ii)
PROPOSED:

```latex
If dismantling test-based accountability drove the decline, the dismantling itself supplies a test: states were released from NCLB's consequences at different times, and bottom-decile scores should have begun falling where and when the pressure came off. \citet{dewey2026} observe descriptively that post-2013 declines look similar in waiver and non-waiver states and note that the sustained-accountability counterfactual ``has never been tested''; this section provides the test. States received ESEA flexibility waivers in waves: eleven in early 2012, twenty-three more (plus DC) later in 2012, and eight in 2013--2014. Seven states (CA, IA, MT, NE, ND, VT, WY) never received one and remained formally under NCLB until ESSA took effect in 2017--18.\footnote{Approval dates compiled from the Department of Education's per-state ESEA flexibility pages, CRS Report R42328, and EdWeek's state-by-state tracking. Washington's waiver was revoked in April 2014; it is dropped from the panel after 2013.} The design identifies one margin: whether a state's formal release from NCLB consequences moved its scores, relative to states not yet or never released. It is the direct policy-variation test the accountability hypothesis invites.
```

WHY: D4 beats (i)–(ii); the conditional opener, the "The design identifies one margin:" frame, and the closing "It is the direct ...-variation test the ... hypothesis invites" are verbatim-matched to A2-8.
RISK: number-adjacent (wave counts, state list, dates, and footnote carried verbatim)

### EDIT A2-4 [replace]
ANCHOR: Figure~\ref{fig:waiver} shows the test using the state-percentile panel
SECTION: `sec:waiver`, paragraph 2 — beat (iii), point estimates
PROPOSED:

```latex
The result is a null on the release-timing margin (Figure~\ref{fig:waiver}, using the state-percentile panel, 2003--2019, ending before the pandemic). Left panel: 10th-percentile grade 8 mathematics scores in early-waiver, late-waiver, and never-waiver states move essentially in lockstep; never-waiver states' bottom decile fell as much as waiver states' after 2012. Right panel: an event-study regression (early-waiver vs.\ never-waiver states, all four grade--subject cells pooled in within-cell SD units, state and year fixed effects, clustered by state) finds post-2012 coefficients near zero. A two-way fixed-effects estimate of the post-waiver effect on 10th-percentile scores is $+0.09$ SD with $p=0.50$ pooled, and is small and insignificant in every cell separately; effects at the 25th and 90th percentiles are likewise null. The one prior quasi-experimental estimate, \citet{bleiberg2020}'s binary waiver difference-in-differences on mean student-level NAEP scores through 2013, also found no average effect; the percentile results here extend that null to the part of the distribution where the decline actually occurred and through 2019.
```

WHY: D4 beat (iii) with the "The result is a null on the [X]-timing margin" opener matched to A2-9; D8 dash reduction; all estimates verbatim.
RISK: number-adjacent

### EDIT A2-5 [replace]
ANCHOR: Because the comparison group is only seven states
SECTION: `sec:waiver`, paragraph 3 — beat (iii), inference and MDE benchmark
PROPOSED:

```latex
Because the comparison group is only seven states, conventional cluster asymptotics are unreliable, so inference is re-done by randomization: permuting the waiver-timing assignment across states 2{,}000 times yields $p=0.46$ for the pooled estimate ($p=0.86$ for grade 8 mathematics in points). The test is informative, not merely underpowered. The randomization distribution implies an 80\%-power minimum detectable effect of about \emph{3.2 points} on grade 8 mathematics 10th-percentile scores (0.35 SD pooled across cells), less than half the $\sim$7-point gain \citet{deejacob2011} attribute to NCLB's adoption, which was concentrated among exactly these students. If withdrawing accountability had undone even half of what imposing it achieved, this design would very likely have detected it. One caveat: a joint test of pre-2011 event-study coefficients gives $p=0.08$, and early-waiver states were converging upward toward never-waiver states before treatment (visible in Figure~\ref{fig:waiver}). The pre-trend cuts both ways but does not rescue the hypothesis, since the post-2012 point estimates are wrong-signed for H3.
```

WHY: D4 beat (iii) MDE-against-benchmark; "The test is informative, not merely underpowered." becomes the shared sentence frame with A2-9; D8 (drops "Crucially," removes em-dashes, splits long sentences); every number verbatim.
RISK: number-adjacent

### EDIT A2-6 [replace]
ANCHOR: One scope limitation remains: a waiver is one notch of deregulation.
SECTION: `sec:waiver`, paragraph 4 — beats (iv)–(v)
PROPOSED:

```latex
What the null rejects is the strong local form of the hypothesis, in which the formal release from NCLB consequences drove a state's low performers downward. What survives by construction is the national form: if the operative change was a nationwide shift in expectations and stakes, culminating in ESSA, it hit all states in the same years, is absorbed by the year fixed effects, and is invisible to this design. A waiver is one notch of deregulation, and this test prices only that notch. Whatever the accountability retreat did to American students' learning, it did not travel through the timing of a state's own release. Section~\ref{sec:fourg} holds this report's leading candidate to the same standard.
```

WHY: D4 beats (iv)–(v); the "What the null rejects is the strong local form of the hypothesis, in which ..." and "What survives by construction is the national form: if the operative ... it hit all [units] in the same years, is absorbed by the year fixed effects, and is invisible to this design" clause structures are verbatim-matched to A2-10; mirrored closer and forward pointer make the symmetry typographically impossible to miss.
RISK: cross-ref (adds `\ref{sec:fourg}`; label exists and resolves)

### EDIT A2-7 [replace]
ANCHOR: \subsection{4G rollout timing: a first within-U.S.\ test of the digital-media channel}
SECTION: §5.5 heading (`sec:fourg`)
PROPOSED:

```latex
\subsection{4G rollout timing: no detectable effect on the arrival-timing margin}
```

WHY: D4 matched headings (pairs verbatim-parallel with A2-2); the "first within-U.S." novelty claim survives in the body and in Related Work; keep `\label{sec:fourg}` on its existing line untouched.
RISK: collides:A1 (owns assertive headings; the pair must move together)

### EDIT A2-8 [replace]
ANCHOR: identification strategy can be pointed at test scores
SECTION: `sec:fourg`, paragraph 1 — beats (i)–(ii)
PROPOSED:

```latex
If the saturation of adolescent life by smartphones and digital media drove the decline, the infrastructure rollout that carried it supplies a test of the same kind: counties crossed into high-speed mobile coverage at different times, and scores should have begun falling where and when 4G arrived. This section runs that test as an adversarial check on the report's own leading candidate, pointing the fertility literature's identification strategy (Section~\ref{sec:h2}) at test scores. Using the archived National Broadband Map (block~$\times$~provider mobile coverage, nine semiannual waves spanning the entire 2010--2014 LTE rollout, validated against FCC benchmarks, Verizon's December 2010 launch markets, and the later Form 477 data), we construct each county's high-speed-mobile coverage history and define treatment as the first wave in which coverage passes half the county's population. Matched to SEDA~5.0 county means (grades 3--8, mathematics and reading, 2009--2019; 99.9\% of counties merge), this is, to our knowledge, the first within-U.S. mobile-rollout design run against student achievement. The identifying variation is the rural lag: metro counties typically crossed the threshold around 2011--2012, nonmetro counties one to three years later. The design identifies one margin: whether a county's local 4G arrival timing moved its students' scores, relative to counties not yet or never covered. It is the direct rollout-variation test the digital-media hypothesis invites.
```

WHY: D4 beats (i)–(ii) with opener, margin frame, and closer verbatim-matched to A2-3; states the adversarial self-test framing where the reviewer looked for it (adjudication: surface the existing answer, don't concede).
RISK: number-adjacent (all data-construction details verbatim) | cross-ref (adds `\ref{sec:h2}`; label exists)

### EDIT A2-9 [replace]
ANCHOR: The result is a precise null on every margin the design can identify
SECTION: `sec:fourg`, paragraph 2 — beat (iii), results with MDE benchmark
PROPOSED:

```latex
The result is a precise null on the arrival-timing margin, in both the contemporaneous-dose and exposure-year designs (Figure~\ref{fig:fourg}). The contemporaneous dose coefficient, moving a county from zero to full LTE coverage, is $-0.002$ SD (cluster SE $0.004$; permutation $p=0.66$); a within-county-year design identifying from cross-grade differences in adolescent exposure yields $+0.011$ SD per exposed year (permutation $p=0.12$). A ten-specification robustness grid (alternative speed-tier codings, Verizon-only coverage, 25\%/75\% thresholds, dropping five states with known coverage-coding artifacts, unweighted) keeps every coefficient within $\pm0.003$ SD, with signs that flip across specifications. The test is informative, not merely underpowered. The 80\%-power minimum detectable effects are $0.013$ SD on the dose margin and $0.016$ on the exposure-year margin, several times smaller than the $0.04$--$0.08$ SD effects \citet{jainstemper2024} estimate on the cross-country 3G margin. The only nominally significant patterns (a small \emph{positive} drift for early-treated counties, reading-only, growing with time since treatment) are continuations of a visible pre-trend, carry the wrong sign for the harm hypothesis, and disappear when the artifact states are dropped: the signature of mildly diverging urban--rural trends, the design's flagged first-order threat, not of a treatment effect.
```

WHY: D4 beat (iii) with the shared "informative, not merely underpowered" frame and an explicit MDE-against-benchmark sentence matched to A2-5; the jainstemper2024 benchmark moves up from the old limits paragraph so both sections benchmark their MDE at the same beat; every number verbatim.
RISK: number-adjacent (jainstemper2024 stays attached to its 0.04--0.08 SD claim)

### EDIT A2-10 [replace]
ANCHOR: Three limits keep this null from being a refutation
SECTION: `sec:fourg`, paragraph 3 — beats (iv)–(v)
PROPOSED:

```latex
What the null rejects is the strong local form of the hypothesis, in which the arrival of high-speed mobile infrastructure in a county drove its students' scores downward. What survives by construction is the national form: if the operative exposure was the device's saturation of adolescent social life, spreading on existing networks and synchronized nationally, it hit all counties in the same years, is absorbed by the year fixed effects, and is invisible to this design. Two further limits narrow what the null prices. Smartphone adoption ran substantially on existing 3G networks (teen ownership was already 37\% in 2012), so coverage timing is a noisy and partly anticipated instrument for exposure. And controls are exhausted by 2015 (the never-treated remainder is 117 deep-rural counties, half a percent of population), so slowly accumulating effects materializing four or more years after arrival are outside the design's reach. This is the same two-form reading the waiver test imposes on the accountability hypothesis (Section~\ref{sec:waiver}); neither leading candidate is exempted from it. What the null establishes is still informative on its own terms: the decline did not propagate through differences in when high-speed mobile infrastructure arrived, in instructive contrast to teen fertility, where the same variation produces large effects \citep{hudsonmoscoso2026}. Whatever digital media did to American adolescents' learning, it arrived with the device and its saturation of social life, not with the local cell tower upgrade.
```

WHY: D4 beats (iv)–(v) with clause structures verbatim-matched to A2-6; all three original limits preserved (national channel becomes beat (v); 3G anticipation and exhausted controls become scope limits); backward pointer mirrors A2-6's forward pointer; mirrored "Whatever X did..." closer.
RISK: number-adjacent | cross-ref (adds `\ref{sec:waiver}`; label exists)

### EDIT A2-11 [replace]
ANCHOR: These tests were designed so the leading phase-one hypotheses predict different outcomes
SECTION: "What the tests jointly imply" (subsection body; replaces the single existing paragraph with three)
PROPOSED:

```latex
The five tests hold the two leading hypotheses to one standard, and the two timing designs return the same kind of result. The waiver test rejects the strong local form of the accountability hypothesis: a state's formal release from NCLB consequences did not move its bottom decile, in a design powered to detect well under half the effect size accountability is credited with creating (Section~\ref{sec:waiver}). The 4G test, which this project ran as an adversarial check on its own leading candidate, rejects the strong local form of the digital-media hypothesis: a county's high-speed-mobile arrival did not move its students' scores, with minimum detectable effects several times below the cross-country 3G estimates (Section~\ref{sec:fourg}). The Common Core test does the same to a third policy candidate: states that never adopted the standards declined as much as adopters (Section~\ref{sec:commoncore}). In each case what survives, by construction, is a nationally synchronized channel that year effects absorb. Neither leading hypothesis leaves this section with a demonstrated local channel.

What still separates the two is positive evidence, not survival of elimination. The pre-pandemic decline strikes whoever is an adolescent after $\sim$2012, regardless of how the cohort looked at age 9 (Section~\ref{sec:cohort}). It appears, in reading, the subject where the decline was earliest and largest, inside Catholic schools that accountability policy never governed (Section~\ref{sec:sector}). It recurs across rich countries with divergent school policies and, in PIAAC, among adults no school policy touches (Section~\ref{sec:adults}). And it coincides with the collapse of voluntary reading and with device-engagement gradients concentrated exactly where the losses are (Section~\ref{sec:h2}). Each of these facts is one the digital-media hypothesis predicts and the school-policy hypotheses do not, and each stands independently of any elimination argument. The accountability retreat survives in a weaker form: a national climate change contributing through channels common to all states, with its clearest remaining footprint at the public-school grade 4 bottom decile.

Two boundaries keep this conclusion honest. First, the digital-media hypothesis faces direct policy variation of its own: the quasi-experimental ban literature \citep{belandmurphy2016,abrahamsson2024,beneito2022,figlio2025}, whose test-score gains concentrate among previously low-achieving students, and the pre-registered test of staggered U.S. state phone bans against NAEP 2026, specified in this project's repository in advance of the data. That pairing is the smartphone-side analog of the waiver test: the same design logic pointed at the other leading hypothesis. Second, elimination arguments are only as strong as the candidate list, and the list stays open. The hypotheses examined here are the ones prominent in research and public debate, not a partition of all possible causes, and a rival not on the list is untouched by the failures of those on it. The strongest claims in this report are accordingly its rejections; the ranking among the surviving candidates is stated in Section~\ref{sec:synthesis} in those calibrated terms.
```

WHY: D4 jointly-imply rewrite in full — both strong local forms rejected; H2's advantage rests on positive evidence, not surviving elimination; the ban literature plus the pre-registered 2026 state-ban test named as the smartphone-side direct policy-variation analog of the waiver test; the 4G design named as this project's adversarial self-test; explicit candidate-set-openness sentence.
RISK: collides:A1 ("strongest claims are its rejections" deliberately echoes A1's D3 inferential-strategy paragraph and the last sentence presumes A1's calibrated Synthesis; reconciler may dedupe) | number-adjacent (no numerals quoted; relations "well under half" / "several times below" match the frozen section values)

### EDIT A2-12 [replace]
ANCHOR: \textbf{Phase one (2013--2019): erosion at the bottom.}
SECTION: Synthesis (`sec:synthesis`), phase-one paragraph — SHARED with A1+A3; my substance is confined to the two-null treatment and the "positive evidence, not survival of elimination" frame; reconciler merges
PROPOSED:

```latex
\textbf{Phase one (2013--2019): erosion at the bottom.} Slow national decline, concentrated almost entirely among the lowest-performing students, present in most states and many countries, alongside collapsing voluntary reading. Two hypotheses fit these basic facts: the accountability retreat (which predicts the bottom-concentration and the U.S. policy timing, and is corroborated in mirror image by Mississippi) and digital-media displacement (which predicts the international synchrony and the reading-practice collapse). The timing tests of Section~\ref{sec:sharper} reject the strong local form of each, using each hypothesis's own variation: release from NCLB did not move a state's bottom decile, and 4G arrival did not move a county's scores. What ranks digital media ahead, pending the pre-registered 2026 state-ban test, is positive evidence rather than survival of elimination: the losses accrue during adolescence to cohorts that arrived at grade 4 at record levels, they appear equally inside Catholic schools that accountability never governed and in states that never adopted the Common Core, and, in the widest version of the same test, they reappear among adults across nineteen OECD countries (Section~\ref{sec:adults}), a population no school policy touches. The accountability retreat retains a plausible supporting role, as a national climate shift and at the public-school grade 4 bottom decile, where the sector contrast does point its way, but it no longer claims a demonstrated state-level channel. Funding, demographics, and teacher supply fail on timing, distribution, or magnitude.
```

WHY: D4 — the Synthesis phase-one ranking must treat the two nulls symmetrically ("break the tie in favor of" replaced by T5 ranking resting on positive evidence, with both strong local forms rejected first); all facts, the Mississippi mirror, the grade-4 footprint, and "nineteen OECD countries" carried verbatim.
RISK: collides:A1 | collides:A3 (shared paragraph per ownership map; if A1/A3 versions prevail, the two sentences to preserve from mine are the reject-both-strong-forms sentence and the "positive evidence rather than survival of elimination" ranking frame)
