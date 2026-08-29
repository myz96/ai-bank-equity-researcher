# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on Equity – cash basis', column FY25 -> column FY26*

CBA's cash ROE increased by 50 bps to 14.0% in FY26 (ev-1). This improvement was driven by a 7% growth in cash NPAT, which lifted ROE at constant equity, partially offset by the dilutive effect of higher average net assets.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Higher cash NPAT | +0.945 ppt | 80 | 1 (single_source) | ev-1, ev-7 |
| `equity_effect` | Higher net assets | -0.445 ppt | 80 | 1 (single_source) | ev-1, ev-6 |

### earnings_effect — "Higher cash NPAT"
*+0.945 ppt | confidence 80/100*

Derived: FY25 ROE (13.5%) x Cash NPAT growth (7.0%, ev-7) = +0.945 ppt. Earnings rose $730m to $10,982m (ev-7). Value is derived, not disclosed.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect — "Higher net assets"
*-0.445 ppt | confidence 80/100*

Derived: Total delta (0.5 ppt) minus earnings effect (+0.945 ppt) = -0.445 ppt. Reflects average equity rising from $75,710m to $78,238m (ev-1), likely due to retained earnings exceeding capital returns.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-6] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."

## Limitations
- Earnings and equity effects are mathematically derived contributions, not bank-disclosed bridge components.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-28T12:16:34+00:00
- seconds: 51.4
- cost_usd: 0.0014
- tokens: 29667 in / 3572 out
- orchestration: pipeline
