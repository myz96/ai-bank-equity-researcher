# CBA — cet1 — FY26 vs FY25




## Limitations
- The research loop ended without a submitted attribution (the model stopped calling tools).
- Failed check: movement_missing
- Failed check: walk_sum (start 1230 + bars -24.0 = 1206.0 != end 1200, tol 1.0 bps) [CBA/FY26/profit_announcement PDF p48 (ev-1)]

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-09-01T05:39:03+00:00
- seconds: 295.0
- cost_usd: 0.0149
- tokens: 373497 in / 36291 out
- orchestration: agent
- tool_calls: 25
- pages_read: 13
- charts_read: 2
- budget_exhausted: no
