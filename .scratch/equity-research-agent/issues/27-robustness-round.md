# 27 — Robustness round: parse retry, load-bearing caps, FY25 chart, residual assist

Type: task
Status: open

## Question

Four precise defects from the 19-case suite (ticket 25's report, 2026-08-27):

1. **Author JSON parse retry**: two cases crashed on "Expecting ':' delimiter" — `author_attribution` has no parse-failure retry; `extract_walk` does. Mirror it.
2. **Load-bearing cap grading**: nim FY26 scored 7/7 recall and precision but a SECONDARY misread walk failed walk_sum and the fatal cap dropped confidence to 40. A walk_sum failure should be fatal only when the failing walk is the one the drivers rest on (another walk for the same comparison passed and the claims reconcile → peripheral).
3. **FY25 PA NIM chart vision failure**: the page breaks the vision reader with "Unterminated string" on both attempts (nim FY25 fell to 2/7). Diagnose the page (render size? label density?) and fix the read path.
4. **Residual assist in the author retry**: when drivers_reconcile fails, the retry message should include the code-computed implied residual (delta minus claimed sum) so the model corrects arithmetic instead of guessing again.

These plus defect 24 (comparison-aware machinery) are the remaining blockers on the CBA exit gate.
