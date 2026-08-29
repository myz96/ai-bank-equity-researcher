# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROE - cash basis (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bps to 13.8% in 1H26 vs 1H25. The increase is driven by higher cash NPAT (+$313m, +6%), partially offset by a larger average equity base ($78.0bn vs $74.2bn). Earnings effect contributed ~+0.8 ppt; equity effect reduced ROE by ~-0.7 ppt.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.8 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-5, ev-6 |
| `equity_effect` | — | -0.7 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-4, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.8 ppt | confidence 80/100*


> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-5] CBA/1H26/profit_announcement, PDF p169: "Net profit after tax - "cash basis" 5,445 5,120 5,133"
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*-0.7 ppt | confidence 80/100*

Derived: Total delta (0.1 ppt) minus earnings effect (0.8 ppt). Evidence: ev-1, ev-3, ev-4. Higher average net assets/equity ($78.0bn vs $74.2bn) diluted returns, consistent with retained earnings accumulation.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"
> [ev-4] CBA/1H26/profit_announcement, PDF p169: "Net average equity 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

## Limitations
- Drivers are derived via arithmetic decomposition (Level 1), not explicitly disclosed as such by the bank.
- Interaction term between earnings and equity growth is embedded in the equity_effect calculation.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T17:47:41+00:00
- seconds: 77.9
- cost_usd: 0.0014
- tokens: 31521 in / 3845 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
