# 25 — Iterate the cash-earnings bridge path to the benchmark spec

Type: task
Status: open

## Question

The pipeline scores 1/4 components at confidence 40 on CBA cash earnings FY26 while the Fable benchmark reconciled the full bridge with zero residual (docs/design/benchmarks.md). Close the gap using the benchmark's working as the spec: (1) extraction must capture the FY25 comparative LEVELS (tax expense, notable items) so deltas are computable, plus the presentation's income waterfall (slide 25) and the statutory-vs-cash reconciliation (slide 23); (2) the author must distinguish underlying vs headline expenses and claim the underlying bridge (−719) with the notable delta separate; (3) claim the `tax_and_other` component instead of dumping it into residual; (4) state the statutory divergence with its reason. Target: 4/4 gold components within tolerance, confidence earned above 80. Verify against the harness (CBA-only suite).
