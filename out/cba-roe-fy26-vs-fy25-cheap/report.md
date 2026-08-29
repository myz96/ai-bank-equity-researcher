# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on Equity – cash basis', column FY25 -> column FY26*

CBA's cash ROE increased by 50 bps to 14.0% in FY26 (ev-1). This improvement was driven by a 7% growth in cash NPAT ($10,982m), which lifted ROE at constant equity, partially offset by the dilutive effect of higher average net assets ($78,238m) as retained earnings accumulated.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Higher cash NPAT | +0.945 ppt | 80 | 1 (single_source) | ev-1, ev-9 |
| `equity_effect` | Higher net assets | -0.445 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-9 |

### earnings_effect — "Higher cash NPAT"
*+0.945 ppt | confidence 80/100*

Derived: Prior ROE (13.5%) x Cash NPAT growth (7.0%). Ev-9 cites $730m increase. At constant equity, this lift is ~95 bps.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-9] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect — "Higher net assets"
*-0.445 ppt | confidence 80/100*

Derived: Total delta (0.5 ppt) minus earnings effect (0.945 ppt). Driven by avg equity rising from $75,710m to $78,238m (ev-3), absorbing retained earnings.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net average equity (under Return on Equity – cash basis)"
> [ev-9] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

## Limitations
- Earnings and equity effects are derived arithmetic contributions, not disclosed bank splits.
- Residual interaction term is embedded in the equity effect.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T18:02:12+00:00
- seconds: 27.3
- cost_usd: 0.0013
- tokens: 31266 in / 3117 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
