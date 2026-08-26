# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 40/100

CBA's cash ROE increased by 50 bps to 14.0% in FY26 (FY25: 13.5%). This improvement was driven primarily by a 7% increase in cash NPAT to $11bn, partially offset by an expansion in average equity. The statutory ROE also rose by 50 bps to 13.9%. No specific driver walk is available for this period.

### earnings_effect — "core_profit"
*unquantified | confidence 80/100*

Cash NPAT grew 7% to $11bn. While the exact equity base is not provided to calculate the precise earnings contribution, rising profits at constant equity would positively drive ROE.
> [ev-2] CBA/FY26/asx_announcement, PDF p1: "Cash net profit after tax increased 7% to $11bn"
> [ev-5] CBA/FY26/profit_announcement, printed p3: "Cash basis 14.0 13.5 50 bpts"

### equity_effect
*unquantified | confidence 60/100*

Average equity likely expanded, exerting a negative pressure on ROE. Without the specific average equity figures for FY25 and FY26, the magnitude of this drag cannot be quantified from the provided evidence.
> [ev-5] CBA/FY26/profit_announcement, printed p3: "Cash basis 14.0 13.5 50 bpts"

## Limitations
- No walk chart or detailed driver table was provided for FY26 vs FY25. Consequently, I cannot decompose the 50 bps ROE movement into specific earnings and equity contributions with precision. The residual equals the total delta because the drivers are unquantified.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:32:37+00:00
- seconds: 26.7
- cost_usd: 0.0006
- tokens: 14670 in / 1544 out
- orchestration: pipeline
