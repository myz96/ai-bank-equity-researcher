# 32 — Component bake-off round: parser, embeddings, vision-vs-text paths

Type: task
Status: claimed

## PRIORITY ARM (user, 2026-08-29): research-loop reasoning tier

Anchor failure: the judge's 1/43 narrative-checklist sweep (page starvation of
the why-layer). Question: is the bottleneck the REASONING tier or the OPEN-LOOP
context assembly? Four arms on four fixed dev cases spanning metric shapes
(CBA nim FY26 = walk; cash_earnings FY26 = bridge; impairment FY26 = note;
nim FY21 = era walk):

1. Cheap pipeline (baseline — artifacts exist)
2. Pipeline + normal author (glm-5.3): same open-loop context, stronger
   reasoner. If the checklist rate stays low, reasoning was not the bottleneck.
3. Agentic closed-loop research on Sonnet (benchmark-template prompt, fresh
   agent per case)
4. Agentic closed-loop research on Fable (ceiling; 3 of 4 case outputs already
   exist from the benchmark)

Scoring: identical for all arms — movement/driver match vs gold, the judge's
stated-AND-entailed checklist rate (the discriminator), cost, wall time.
Prompts for arms 3-4 are the UNCHANGED benchmark template (no checklist
leakage into prompts). Decision output: which tier owns the research loop,
or whether deterministic reference-following (ticket 22) closes the gap at
cheap-tier cost — that engineered arm joins round 2 once built.

## RESULTS (2026-08-29, run complete; five arms + codex added per user)

All five arms ran all four anchor cases. The judge protocol is one script,
scripts/bakeoff_judge.py, over both artifact formats; detail JSON in
evals/results/20260829-2140-bakeoff-judge.json (merged master). The cheap row
is the POST-ticket-27 code (commit 9a9d13d), so the numbers-fix round is
already priced in.

| arm | loop | nim FY26 | cash-earn FY26 | impair FY26 | nim FY21 | checklist | flagged | movement | cost/case | time/case |
|---|---|---|---|---|---|---|---|---|---|---|
| cheap pipeline | open | 0/4 | 0/3 | 0/3 | 0/5 | **0/15** | 1 | 4/4 | $0.002-0.005 | 1-3 min |
| glm-5.3 author, same context | open | 0/4 | 0/3 | 1/3 | 0/5 | **1/15** | 2 | 4/4 | $0.22-0.86 | 4-31 min |
| Sonnet agentic | closed | 4/4 | 0/3 | 0/3 | 2/5 | **6/15** | 3 | 4/4 | 27-55k out-tok (sub) | 7-11 min |
| Fable agentic | closed | 3/4 | 0/3 | 0/3 | 0/5 | **3/15** | 4 | 4/4 | 15-35k out-tok (sub) | 4-10 min |
| Codex agentic | closed | 1/4 | 0/3 | 0/3 | 0/5 | **1/15** | 5 | 4/4 | OpenAI sub quota | 4-8 min |

Answer to the anchor question — REASONING TIER IS NOT THE BOTTLENECK:

- Movements: every arm 4/4. Numbers are tier-independent AND loop-independent.
- The glm control is the clean experiment: same open-loop context, an author
  ~100x the cheap price, ~10x the wall time — and it gained ONE checklist item
  (the impairment divisional deltas). Open-loop tops out near zero insight no
  matter who reasons over the starved context.
- The closed-loop arms all beat open-loop; the spread inside closed-loop
  (Sonnet 6 > Fable 3 > Codex 1) is NOT a capability ranking — see caveats.

Caveats that bound the reading:

1. The checklist ceiling is compressed: the impairment list has two half-year
   facts a FY-vs-FY report legitimately skips (Sonnet's report skips them BY
   NAME as out of scope), and nim FY21 has one document-meta fact quotes can
   never entail. Realistic ceiling is ~10-12/15, not 15/15.
2. Codex's 1/15 carries 5 flags and a citation-style interaction: it cites
   terse chart labels ("Liquids (0.03%)"), which fail strict entailment where
   Sonnet's sentence-length quotes pass. Its numbers and decompositions match
   gold 4/4 with zero residual.
3. All five arms scored 0/3 on cash-earnings insight: those three facts live
   in the presentation's slide-24 framing (+6.2% income, operating performance
   $16,469m +6.5%) and every arm answered from the PA instead. Even a closed
   loop does not surface an alternative document's framing unprompted — worth
   its own checklist note in round 2.
4. One run per arm per case; no repeat sampling. Flags are judge
   disagreements, human-resolved by design, listed beside the rate.
5. Operational finding: glm-5.3 exhausted a 24000-token budget reasoning on
   the densest bridge prompt and returned empty five times; author_max_tokens
   for the normal combo is now 40000 (config.py comment records it).

DECISION (recommended; user ratifies):

1. The research loop is loop-bound, so the fix is loop shape, not model size.
   Build ticket 22 deterministic reference-following as round 2's engineered
   arm — the impairment case is the acceptance test (Note 2.2, PDF p118, is
   reachable by following "refer Note 2.2" from the income statement).
2. If the engineered arm lands at or above Sonnet's 6/15 on the anchors at
   cheap-tier cost, the cheap pipeline keeps the research loop.
3. If it half-works, hybrid: cheap pipeline owns numbers (now Brier 0.035,
   36/36 at 85+), and a Sonnet-tier closed-loop pass owns the why-layer.
   Sonnet is the priced midpoint: it matched Fable's insight quality on these
   cases at lower cost, and its p118 find is the exemplar of what the pass
   buys. Fable/Codex tiers buy nothing extra here.

## ROUND 2 RESULT (2026-08-30, ticket 22 engineered arm; commit 78448fb)

The reference-following arm scored **3/15** on the anchors (one earlier
sample of the same code: 4/15), against the pre-registered bar of Sonnet's
6/15. Suite stayed green everywhere and improved: 15/15 CBA movements,
brier 0.032, confidently-wrong 0.0, 34/34 at 85+; worst anchor cost
$0.0048 (envelope $0.010). Full detail in ticket 22's progress note.

By the pre-registered rule this is the "half-works" branch -> hybrid. But
the residual 12-item gap decomposes before that conclusion follows:

- 3 items (cash-earnings): the judge's entailment path reads only quotes a
  DRIVER cites, so headline-level facts (operating-performance frame,
  statutory-vs-cash frame) can never entail in the pipeline's report shape,
  however well sourced. Both judges already answer "stated" on one of them.
  This is a report-shape/protocol interaction, not a research failure —
  and Sonnet also scored 0/3 here.
- 5 items (nim FY21): slide-63 annotation layer separates numbers from
  labels in the text layer; text extraction cannot pair them. Identified
  mechanical fix: a vision read of walk-page annotations. Sonnet got 2/5
  by reading the same page visually.
- 2 items (impairment): half-year facts a FY-vs-FY note legitimately
  skips (caveat 1 above; every arm scored 0 on them).
- Meanwhile the arm now delivers the p118 Note 2.2 bridge (+150/-17/-71,
  zero residual) INSIDE the attribution — the exact find that made the
  Sonnet arm the exemplar — but no checklist item credits it.

Reading: the remaining gap to the Sonnet bar is two mechanical fixes
(headline citations in the report shape; vision annotation pairing), not a
loop-shape deficit. RECOMMENDATION UPDATE: run one more cheap-tier
iteration on those two fixes before paying for a hybrid pass; adopt the
hybrid only if the anchors still sit below ~6/15 after it. User ratifies.

## Question

Time-permitting robustness round (user, 2026-08-28): the current component choices are tested but not comprehensively compared — make each a measured decision rather than an assumption. Reuse the prototype-13/14 harnesses; every arm scores against existing gold.

1. **Extraction paths**: text-layer vs vision-rendered per page TYPE (clean tables, dense tables, era pages with text-layer artifacts like FY21's "47. 0", chart pages). Decides whether vision-for-tables earns its cost anywhere.
2. **Embedding models**: bge-small (current) vs a bigger local model (bge-m3 class) vs BM25-only, on the bake-off target set EXTENDED with NAB/WBC and longitudinal-case queries — CBA-shaped documents flattered the current choice.
3. **Parser**: pymupdf vs one alternative (pdfplumber or a vision-first read) on the known trap pages (decimal-space era pages, hidden-text slides, the chart page that breaks the vision reader).

Trigger earlier than "time permitting" if: a retrieval miss appears on NAB/WBC/longitudinal cases, or an extraction-stage regression traces to the text layer. Success = a table per component, and either a documented switch or a documented keep.
