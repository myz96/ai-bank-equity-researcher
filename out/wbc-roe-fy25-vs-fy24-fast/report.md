# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROTE (return on average tangible equity) excluding Notable Items', column Full Year Sept 2024 column -> column Full Year Sept 2025 column*

WBC's headline ROE measure, ROTE ex Notable Items (return on average tangible equity, excluding Notable Items), fell 24 bps to 10.97% in FY25 from 11.21% in FY24 (ev-1, ev-4, ev-6). The decline was driven almost entirely by lower cash earnings: net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items fell to $6,966m from $7,106m, a 1.97% decline (ev-3). Average tangible ordinary equity rose slightly to $63,476m from $63,415m (ev-2, ev-5), a small negative equity effect. The bank attributes the earnings fall to higher operating expenses (9% higher, including $273m restructuring costs) more than offsetting higher operating income and lower credit impairment charges (ev-9). Statutory ROTE fell 12 bps to 10.89% and statutory ROE fell 11 bps to 9.66% (ev-1).

> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps) 10.87% 11.08% (21 bps)"
> [ev-4] WBC/FY25/results_announcement, PDF p58: "Return on average tangible ordinary equity (excluding Notable Items) 10.97% 11.21% 10.87% 11.08%"
> [ev-6] WBC/FY25/investor_discussion_pack, printed p6: "11.0% ROTE ex Notable Items1 24bps to FY24"
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106 3,511 3,454"
> [ev-2] WBC/FY25/results_announcement, PDF p10: "Average tangible ordinary equity ($m) 63,476 63,415 - 64,429 62,519 3"
> [ev-5] WBC/FY25/results_announcement, PDF p58: "Average tangible ordinary equity 63,476 63,415 64,429 62,519"
> [ev-9] WBC/FY25/results_announcement, PDF p9: "Operating expenses were 9% higher. The increase included restructuring costs of $273 million to support targeted productivity initiatives under our Fit for Growth program."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Movement in cash earnings at constant equity | -0.22 ppt | 80 | 1 (single_source) | ev-3, ev-8, ev-9 |
| `equity_effect` | Movement in average equity at constant earnings | -0.02 ppt | 75 | 1 (single_source) | ev-2, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "Movement in cash earnings at constant equity"
*-0.22 ppt | confidence 80/100*

Derived, not disclosed: prior-period ROTE (11.21%) x earnings growth (-1.97% as a fraction) = -0.22 ppt. Earnings (net profit attributable to owners of WBC adjusted for RSP dividends ex Notable Items) fell to $6,966m from $7,106m (ev-3). Bank states net profit ex Notable Items fell 2% as higher operating income and lower credit impairment charges were more than offset by higher expenses (ev-8, ev-9).
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106 3,511 3,454"
> [ev-8] WBC/FY25/results_announcement, PDF p9: "Net profit excluding Notable Items 6,972 7,113 (2)"
> [ev-9] WBC/FY25/results_announcement, PDF p9: "Operating expenses were 9% higher. The increase included restructuring costs of $273 million to support targeted productivity initiatives under our Fit for Growth program."

### equity_effect — "Movement in average equity at constant earnings"
*-0.02 ppt | confidence 75/100*

Derived, not disclosed: total delta (-0.24 ppt) minus earnings_effect (-0.22 ppt) = -0.02 ppt. Average tangible ordinary equity rose slightly to $63,476m from $63,415m (+0.1%) (ev-2, ev-5); at constant earnings, higher equity reduces ROE. On-market share buyback reduced equity but was more than offset by retained earnings (ev-2, ev-5).
> [ev-2] WBC/FY25/results_announcement, PDF p10: "Average tangible ordinary equity ($m) 63,476 63,415 - 64,429 62,519 3"
> [ev-5] WBC/FY25/results_announcement, PDF p58: "Average tangible ordinary equity 63,476 63,415 64,429 62,519"

## Notable items
- Hedging items Notable Items: -$56m FY25 vs -$123m FY24 (ev-12)

## Limitations
- The bank does not disclose a ROTE bridge/walk chart decomposing the movement; the earnings_effect and equity_effect are arithmetic derivations per the task method, not bank-disclosed figures.
- The earnings growth rate (-1.97%) is computed from the ROTE-relevant earnings measure (net profit attributable to owners of WBC adjusted for RSP dividends ex Notable Items, $6,966m vs $7,106m), which differs slightly from the group net profit ex Notable Items ($6,972m vs $7,113m, -2%) shown in the performance summary and investor pack.
- The equity_effect direction is inferred from the small rise in average tangible ordinary equity (+$61m) and the on-market share buyback context; the bank does not quantify the equity contribution to ROTE.
- Statutory ROTE (10.89% vs 11.01%, -12 bps) and statutory ROE (9.66% vs 9.77%, -11 bps) are named variants and are reported as context only, not as the headline movement.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-09-01T06:23:30+00:00
- seconds: 653.9
- cost_usd: 0.0084
- tokens: 194618 in / 8958 out
- orchestration: agent
- tool_calls: 23
- pages_read: 8
- charts_read: 0
- budget_exhausted: no
