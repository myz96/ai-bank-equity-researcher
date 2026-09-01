# NAB — nim — FY25 vs FY24




## Limitations
- The research loop ended without a submitted attribution (the model stopped calling tools).
- Failed check: movement_missing
- Failed check: walk_sum (start 170 + bars +60.0 = 230.0 != end 178, tol 0.1 %) [NAB/FY25/investor_presentation PDF p24 (ev-2)]

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-09-01T07:42:35+00:00
- seconds: 303.1
- cost_usd: 0.0187
- tokens: 323266 in / 39366 out
- orchestration: agent
- tool_calls: 18
- pages_read: 2
- charts_read: 2
- budget_exhausted: no
