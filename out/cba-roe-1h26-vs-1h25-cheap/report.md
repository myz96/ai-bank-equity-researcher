# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.4ppt → 13.8ppt (+0.4ppt) | **Attribution confidence:** 95/100

CBA's cash ROE increased by 40 basis points to 13.8% in 1H26 (ev-1). This movement is driven by a positive earnings effect of approximately 35 basis points, derived from 6% growth in cash NPAT (ev-2), partially offset by a negative equity effect of approximately 5 basis points due to the increase in average net assets (ev-3). The bank confirms higher cash NPAT was partly offset by higher net assets.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.35 ppt | 85 | 1 (single_source) | ev-1, ev-2, ev-6 |
| `equity_effect` | — | +0.05 ppt | 85 | 1 (single_source) | ev-1, ev-3, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.35 ppt | confidence 85/100*

Derived contribution: Prior-period ROE (13.4%) multiplied by cash NPAT growth rate (6%, ev-2). Represents the lift at constant equity. Value is derived, not disclosed.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*+0.05 ppt | confidence 85/100*

Residual contribution: Total delta (0.4 ppt) minus earnings effect (0.35 ppt). Reflects the drag from higher average equity (78,004 vs 77,020, ev-3), likely driven by retained earnings and capital buffers.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

## Limitations
- The split between earnings and equity effects is an arithmetic derivation based on the canonical taxonomy, not a direct disclosure from the bank.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-27T07:39:57+00:00
- seconds: 55.9
- cost_usd: 0.0012
- tokens: 24353 in / 3367 out
- orchestration: pipeline
