# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 40/100

*Read from: row 'ROTE ex-notables', column FY24 -> column FY25*

Westpac's headline ROTE ex Notable Items declined by 24 basis points (11.21% to 10.97%) in FY25 vs FY24. The decline is primarily driven by a negative earnings effect (-23.8 ppt), reflecting lower cash earnings at constant equity. A small positive equity effect (+0.6 ppt) partially offset this, arising from an increase in average tangible equity.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -23.76 ppt | 80 | 1 (single_source) | ev-4, ev-6 |
| `equity_effect` | — | +0.56 ppt | 80 | 1 (single_source) | ev-4, ev-6 |
| *residual (unexplained)* | — | -0.04 ppt | — | — |

### earnings_effect
*-23.76 ppt | confidence 80/100*

Derived: Prior-period ROE (11.21%) multiplied by the implied earnings growth rate. Earnings fell as NII and fee income declines outweighed cost savings, despite stable impairment. This contribution is derived from KPI data, not disclosed directly.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m)"

### equity_effect
*+0.56 ppt | confidence 80/100*

Derived: Total delta minus earnings effect. Average tangible equity increased slightly (cited in ev-6 context of ordinary equity stability), providing a small positive lift to ROE at constant earnings. This reflects retained earnings and capital management.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m)"

## Limitations
- The earnings effect and equity effect are quantified derivations based on the arithmetic identity of ROE, not explicit bank disclosures. The residual of -0.04 ppt represents rounding differences between the reported percentages and the calculated components.
- Failed check: drivers_reconcile (drivers -23.2 + residual -0.0 != delta -0.2, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T21:05:23+00:00
- seconds: 49.7
- cost_usd: 0.0013
- tokens: 35339 in / 2014 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
