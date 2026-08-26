# 26 — Cross-reference consolidation cases (holdout)

Type: task
Status: claimed

## Question

User requirement (2026-08-26): before we can claim the system done, it must face cases where the answer only exists by consolidating footnotes, notes, and tables scattered across a report — the thing humans do well and LLMs notoriously do not. Each case: a question, a gold answer, and the **gold set of locations** (document, page) that must all be consolidated; held out from iteration. Scoring adds a location-coverage metric: how many of the required locations appear in the agent's cited evidence. The user personally reviews these cases (HITL); some may be authored by the user directly.

Progress 2026-08-26: three cases drafted and location-verified in `evals/gold/cba-fy26-crossref.json` (holdout from birth). Remaining: (a) the restatement web case (needs the pre-results note fetched); (b) an `ask` CLI entry point so free-form questions run through the same tool layer, plus location-coverage scoring in the harness; (c) the user's personal review, and any cases the user authors directly.

Seed webs identified during gold verification:
1. **The dividend/DRP web**: CBA slide 32's −76bpts dividend bar + its footnote ($530m on-market purchase, −10bpts) + PA p48's DRP text (satisfied in full on-market, participation rates).
2. **The mortgage-offset footnote**: CBA's NIM is calculated net of ~$95bn of offset balances, disclosed only in a table footnote.
3. **The notable-items web**: the $170m value on slide 24, the item list in its footnote, the underlying-vs-headline expense framing on slide 27's footnote, and the KPI CTI table.
4. **The restatement web** (pending): the pre-results "Items impacting CBA's financial reporting" note vs restated comparatives inside the PA.
