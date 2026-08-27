# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 95/100

CBA's cash ROE increased by 50 basis points to 14.0% in FY26 (FY25: 13.5%). This improvement was driven primarily by a 7% increase in cash earnings, which contributed approximately 94 bps at constant equity. This positive earnings effect was partially offset by the impact of higher average net assets, resulting in a negative equity effect of approximately -44 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.94 ppt | 85 | 1 (single_source) | ev-3, ev-4, ev-11 |
| `equity_effect` | — | -0.44 ppt | 85 | 1 (single_source) | ev-2, ev-3, ev-4, ev-11 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.94 ppt | confidence 85/100*

Derived contribution: Prior-period ROE (13.5%) multiplied by cash NPAT growth rate (7.0%, from ev-11). Value is derived, not disclosed. Supported by ev-11 ($730m / $10,253m growth) and ev-3.
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net profit after tax – cash basis"
> [ev-4] CBA/FY26/profit_announcement, PDF p147: "ROE – cash basis (%)"
> [ev-11] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect
*-0.44 ppt | confidence 85/100*

Residual contribution: Total delta (0.5 ppt) minus earnings effect (0.94 ppt). Value is derived, not disclosed. Direction supported by ev-2 showing average net equity growth from $75,710m to $78,238m (+3.3%), reflecting retained earnings.
> [ev-2] CBA/FY26/profit_announcement, PDF p147: "Net average equity"
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net profit after tax – cash basis"
> [ev-4] CBA/FY26/profit_announcement, PDF p147: "ROE – cash basis (%)"
> [ev-11] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

## Source disagreements
- **Cash Profit Numerical Consistency** (rounding): 10,253.0 - ev-3 vs 10,252.0 - ev-15
  Preferred: 10,253.0. ev-3 lists FY25 Cash Profit as 10,253.0, while ev-15 lists it as 10,252.0. The difference is 1 unit ($1m), likely due to rounding or restatement differences between tables. ev-3 is used for calculation consistency with the stated 7% growth in ev-11.

## Limitations
- The split between earnings and equity effects is an arithmetic derivation based on the canonical taxonomy, not a direct disclosure from CBA.
- The specific drivers of the equity increase (e.g., DRP vs retained earnings) are inferred from the balance sheet movement rather than explicitly quantified in the provided evidence.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-27T07:57:10+00:00
- seconds: 45.8
- cost_usd: 0.0012
- tokens: 25104 in / 3803 out
- orchestration: pipeline
