# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column FY25 -> column FY26*

CBA's cash ROE increased by 50 basis points to 14.0% in FY26, up from 13.5% in FY25. This improvement was primarily driven by a 7% increase in cash NPAT ($10,982m), which lifted ROE at constant equity. This positive earnings effect was partially offset by an increase in average net assets (equity) from $75,710m to $78,238m, which diluted the return.

> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-4] CBA/FY26/profit_announcement, printed p3: "Return on equity (ROE) (%) Cash basis 14.0 13.5 50 bpts 14.3 13.8 50 bpts"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-13] CBA/FY26/results_presentation, printed p54: "ROE (cash) 14.0% +50bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.9 ppt | 80 | 1 (single_source) | ev-1, ev-8 |
| `equity_effect` | — | -0.4 ppt | 80 | 1 (single_source) | ev-1, ev-7 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.9 ppt | confidence 80/100*

Derived: Prior-period ROE (13.5%) multiplied by cash NPAT growth rate (7.0%, ev-8). Represents the lift in ROE assuming constant equity. Cash NPAT rose $730m to $10,982m (ev-8).
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect
*-0.4 ppt | confidence 80/100*

Derived: Total delta (0.5 ppt) minus earnings effect (0.9 ppt). Reflects dilution from higher average net assets ($78,238m vs $75,710m, ev-1), likely due to retained earnings and capital generation outpacing buybacks/DRP.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."

## Limitations
- Earnings and equity effects are derived calculations based on reported levels and growth rates, not explicitly quantified as such by the bank in a bridge table.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T16:25:56+00:00
- seconds: 52.2
- cost_usd: 0.0015
- tokens: 34952 in / 3677 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
