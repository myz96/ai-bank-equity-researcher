# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 75/100

*Read from: row 'ROTE row, Shareholder value - excluding Notable Items block', column Full Year Sept 2024 column -> column Full Year Sept 2025 column*

Westpac's return on average tangible equity excluding Notable Items (ROTE ex Notable Items) fell 24 basis points to 10.97% in FY25 from 11.21% in FY24. The decline was almost entirely driven by a 2% fall in net profit excluding Notable Items ($6,966m vs $7,106m), which reduced ROTE by approximately 22 ppt at constant equity. Average tangible ordinary equity rose marginally by $61m (0.1%) to $63,476m, contributing roughly 2 ppt of headwind as the interaction term. Higher operating expenses (+9%, including a $273m restructuring charge) more than offset higher net interest income (+3%) and lower impairment charges, driving the earnings decline.

> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-12] WBC/FY25/results_announcement, PDF p58: "Return on average tangible ordinary equity (excluding Notable Items) 10.97% 11.21%"
> [ev-6] WBC/FY25/investor_discussion_pack, printed p6: "11.0% ROTE ex Notable Items1 24bps to FY24"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Net profit excluding Notable Items movement | -0.22 ppt | 80 | 1 (single_source) | ev-1, ev-12, ev-13, ev-5 |
| `equity_effect` | Average tangible ordinary equity movement | -0.02 ppt | 75 | 1 (single_source) | ev-8, ev-9 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "Net profit excluding Notable Items movement"
*-0.22 ppt | confidence 80/100*

Derived: prior-period ROTE (11.21%) multiplied by earnings growth rate (-1.97%, from $7,106m to $6,966m). Net profit excl. Notable Items fell 2% as higher operating expenses (+9%, incl. $273m restructuring under Fit for Growth) more than offset higher NII (+3%) and lower impairment charges (5bps vs 7bps of avg loans). Bank does not disclose a separate ROTE walk.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-12] WBC/FY25/results_announcement, PDF p58: "Return on average tangible ordinary equity (excluding Notable Items) 10.97% 11.21%"
> [ev-13] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106"
> [ev-5] WBC/FY25/results_announcement, PDF p9: "Net profit excluding Notable Items was $6,972 million, a decrease of 2%, with higher operating income and lower credit impairment charges more than offset by higher expenses."

### equity_effect — "Average tangible ordinary equity movement"
*-0.02 ppt | confidence 75/100*

Derived: total delta (-24 ppt) minus earnings effect (-22 ppt). Average tangible ordinary equity rose $61m to $63,476m (+0.1%), nearly flat YoY. The DRP for the final dividend was satisfied via third-party market purchase (neutralising share count), while the bank continued its ongoing share buyback program. Retained earnings from $6,966m profit less $153m dividends provided limited equity accretion.
> [ev-8] WBC/FY25/results_announcement, PDF p58: "Average tangible ordinary equity 63,476 63,415 64,429 62,519"
> [ev-9] WBC/FY25/results_announcement, PDF p31: "The Board has determined to satisfy the DRP for the 2025 final ordinary dividend by arranging for the purchase of shares in the market by a third party."

## Limitations
- No dedicated ROTE bridge/walk chart published by Westpac; both driver contributions are arithmetic derivations per the task method, not bank-disclosed decompositions.
- The equity_effect captures both the pure equity effect and the interaction residual between earnings and equity movements.
- The bank discusses expense growth and NIM drivers narratively but does not attribute specific ROTE components to individual business segments.
- Movement delta normalised from -24 to -0.24 (unit slip against the endpoints).
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Identity contributions restated from -24.00 to -0.2400 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T14:47:14+00:00
- seconds: 192.1
- cost_usd: 0.0497
- tokens: 1722831 in / 9304 out
- orchestration: agent
- tool_calls: 64
- pages_read: 31
- charts_read: 0
- budget_exhausted: no
