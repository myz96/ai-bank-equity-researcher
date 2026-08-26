# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+50ppt) | **Attribution confidence:** 40/100

CBA's cash ROE increased by 50 bps to 14.0% in FY26 (FY25: 13.5%). The improvement was driven primarily by a 7% increase in cash NPAT ($11bn), supported by lending volume growth and stable underlying NIM. While pre-provision profit grew 6%, the earnings effect is partially offset by an equity effect from balance sheet expansion. No detailed walk chart is available to quantify the specific split between earnings and equity effects.

### earnings_effect — "core_profit"
*unquantified | confidence 80/100*

Cash NPAT increased 7% to $11bn, providing a positive contribution to ROE. This was supported by lending volume growth and broadly stable underlying net interest margin.
> [ev-2] CBA/FY26/asx_announcement, PDF p1: "Cash net profit after tax increased 7% to $11bn"
> [ev-5] CBA/FY26/asx_announcement, PDF p1: "Net profit after tax (NPAT) was supported by lending volume growth in our core businesses, with underlying net interest margin broadly stable."

### equity_effect
*unquantified | confidence 60/100*

Average equity likely increased due to retained earnings and loan growth, exerting a downward pressure on ROE. Without average equity figures, the magnitude cannot be quantified.
> [ev-3] CBA/FY26/asx_announcement, PDF p1: "pre-provision profit increased 6% to $16.5bn"
> [ev-9] CBA/FY26/profit_announcement, printed p3: "Cash basis 14.0 13.5 50 bpts"

## Limitations
- No validated walk chart is provided to decompose the ROE movement into precise earnings and equity contributions.
- Average equity balances for FY25 and FY26 are not explicitly stated in the evidence records, preventing calculation of the equity effect.
- Confidence is capped at 60 because key quantitative drivers (equity levels) are missing.
- Failed check: movement_arithmetic (13.5 + 50.0 != 14.0)
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:18:27+00:00
- seconds: 32.5
- cost_usd: 0.0007
- tokens: 15569 in / 2002 out
- orchestration: pipeline
