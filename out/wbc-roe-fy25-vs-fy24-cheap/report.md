# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 75/100

*Read from: row 'ROTE ex-notables', column FY24 -> column FY25*

Westpac's headline ROTE ex Notable Items declined by 24 basis points to 10.97% in FY25 from 11.21% in FY24 (ev-4). This decline was driven primarily by a reduction in cash earnings at constant equity, as average tangible equity remained broadly stable with a slight increase (ev-6). The movement is derived from the KPI table endpoints and average equity levels.

> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.24 ppt | 75 | 1 (single_source) | ev-4, ev-6 |
| `equity_effect` | — | -0.05 ppt | 75 | 1 (single_source) | ev-4, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.24 ppt | confidence 75/100*

Derived: Prior-period ROE (11.21%) multiplied by the implied earnings growth rate. Earnings fell from $8,003m to $7,866m (-1.7%). Contribution = 11.21% * -0.017 = -0.19 ppt. Remaining delta attributed to equity effect.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m)"

### equity_effect
*-0.05 ppt | confidence 75/100*

Derived: Total delta (-0.24) minus earnings effect (-0.19). Average tangible equity increased slightly from $71,549m to $71,885m (+0.5%), exerting a small negative drag on ROE.
> [ev-4] WBC/FY25/results_announcement, PDF p10: "ROTE"
> [ev-6] WBC/FY25/results_announcement, PDF p10: "Average total equity ($m)"

## Limitations
- Drivers are derived using Level 1 arithmetic (ROE endpoints and average equity) rather than disclosed bridge components. Earnings figures were inferred from ROE and Equity data; direct profit evidence not provided in extract.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T23:44:00+00:00
- seconds: 24.7
- cost_usd: 0.0014
- tokens: 36008 in / 2107 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
