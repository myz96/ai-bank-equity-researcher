# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column FY25 -> column FY26*

CBA's cash ROE rose 50 bps to 14.0% in FY26, driven by a 7% increase in cash NPAT ($10,982m) which lifted ROE at constant equity, partially offset by higher average net assets ($78,238m vs $75,710m). The earnings effect contributed approximately +0.95 ppt, while the equity effect reduced ROE by approximately -0.45 ppt.

> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-4] CBA/FY26/profit_announcement, printed p3: "Return on equity (ROE) (%) Cash basis 14.0 13.5 50 bpts 14.3 13.8 50 bpts"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-13] CBA/FY26/profit_announcement, PDF p146: "ROE – cash basis (%) 14.0 13.5 14.3 13.8"
> [ev-18] CBA/FY26/results_presentation, printed p54: "ROE (cash) 14.0% +50bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.95 ppt | 80 | 1 (single_source) | ev-1, ev-8, ev-13 |
| `equity_effect` | — | -0.45 ppt | 80 | 1 (single_source) | ev-1, ev-7, ev-13 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.95 ppt | confidence 80/100*

Derived: Prior-period ROE (13.5%) multiplied by cash NPAT growth rate (7.0%, ev-8). Cash NPAT increased $730m to $10,982m (ev-8), lifting ROE at constant equity. This is an arithmetic derivation, not a disclosed figure.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-13] CBA/FY26/profit_announcement, PDF p146: "ROE – cash basis (%) 14.0 13.5 14.3 13.8"

### equity_effect
*-0.45 ppt | confidence 80/100*

Derived: Total delta (0.5 ppt) minus earnings effect (+0.95 ppt). Average net assets rose to $78,238m from $75,710m (ev-1), diluting returns. This is an arithmetic derivation, not a disclosed figure.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-13] CBA/FY26/profit_announcement, PDF p146: "ROE – cash basis (%) 14.0 13.5 14.3 13.8"

## Limitations
- Earnings and equity effects are derived via identity decomposition, not explicitly quantified by the bank as separate drivers in the provided text.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T18:53:12+00:00
- seconds: 30.5
- cost_usd: 0.0016
- tokens: 35305 in / 3824 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
