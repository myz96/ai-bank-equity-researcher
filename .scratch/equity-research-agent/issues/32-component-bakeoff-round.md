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

## Question

Time-permitting robustness round (user, 2026-08-28): the current component choices are tested but not comprehensively compared — make each a measured decision rather than an assumption. Reuse the prototype-13/14 harnesses; every arm scores against existing gold.

1. **Extraction paths**: text-layer vs vision-rendered per page TYPE (clean tables, dense tables, era pages with text-layer artifacts like FY21's "47. 0", chart pages). Decides whether vision-for-tables earns its cost anywhere.
2. **Embedding models**: bge-small (current) vs a bigger local model (bge-m3 class) vs BM25-only, on the bake-off target set EXTENDED with NAB/WBC and longitudinal-case queries — CBA-shaped documents flattered the current choice.
3. **Parser**: pymupdf vs one alternative (pdfplumber or a vision-first read) on the known trap pages (decimal-space era pages, hidden-text slides, the chart page that breaks the vision reader).

Trigger earlier than "time permitting" if: a retrieval miss appears on NAB/WBC/longitudinal cases, or an extraction-stage regression traces to the text layer. Success = a table per component, and either a documented switch or a documented keep.
