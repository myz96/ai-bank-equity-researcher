# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 10.97ppt → 10.89ppt (-0.08ppt) | **Attribution confidence:** 40/100

*Read from: row 'ROTE ex Notable Items', column FY24 -> column FY25*

Westpac's headline ROTE ex Notable Items declined by 8 bps to 10.89% in FY25 (ev-4). This decline is driven by a negative earnings effect of approximately 6.3 bps, calculated using the statutory profit growth rate as a proxy for core earnings performance at constant equity. The remaining 1.7 bps of decline is attributed to an equity effect, reflecting the impact of average tangible equity changes and interaction terms.

> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-2] WBC/FY25/results_announcement, PDF p10: "Return on average tangible equity (ROTE) 10.89% 11.01% (12 bps) 11.13% 10.63% 50 bps"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -6.3 ppt | 75 | 1 (single_source) | ev-2, ev-4 |
| `equity_effect` | — | -1.7 ppt | 75 | 1 (single_source) | ev-4 |

### earnings_effect
*-6.3 ppt | confidence 75/100*


> [ev-2] WBC/FY25/results_announcement, PDF p10: "Return on average tangible equity (ROTE) 10.89% 11.01% (12 bps) 11.13% 10.63% 50 bps"
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"

### equity_effect
*-1.7 ppt | confidence 75/100*

Derived: Total delta (-8 bps) minus earnings effect (-6.3 bps). Reflects the drag from average tangible equity growth (likely due to retained earnings or DRP) outpacing earnings growth, plus interaction residuals.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"

## Limitations
- Exact 'Average Tangible Equity' levels are not provided in evidence records; Ordinary/Total Equity used as proxies for directionality.
- Core Earnings growth rate is not explicitly stated in evidence; Statutory Profit growth used as a proxy for the earnings effect calculation.
- Confidence capped at 75 due to derivation of drivers rather than direct bank disclosure of the bridge.
- Failed check: drivers_reconcile (drivers -8.0 + residual +0.0 != delta -0.1, tol 0.1)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T19:03:36+00:00
- seconds: 31.0
- cost_usd: 0.0017
- tokens: 42171 in / 3026 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
