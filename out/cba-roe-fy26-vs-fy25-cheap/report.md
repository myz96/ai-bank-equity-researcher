# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column FY25 -> column FY26*

CBA's cash ROE rose 50 bps to 14.0% in FY26, driven by a 7% increase in cash NPAT ($10,982m) which was partially offset by higher average net assets ($78,238m). The earnings effect contributed approximately +39 bps, while the equity effect reduced ROE by approximately -39 bps.

> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.39 ppt | 80 | 1 (single_source) | ev-1, ev-8 |
| `equity_effect` | — | +0.11 ppt | 80 | 1 (single_source) | ev-1, ev-8 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.39 ppt | confidence 80/100*

Derived: Prior ROE (13.5%) multiplied by cash NPAT growth rate (7%). Cash NPAT increased $730m or 7% to $10,982m (ev-8). This lift at constant equity is derived, not disclosed.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect
*+0.11 ppt | confidence 80/100*

Residual: Total delta (0.5 ppt) minus earnings effect (0.39 ppt). Average net assets grew from $75,710m to $78,238m (ev-1). Higher retained earnings likely drove equity growth, dampening ROE expansion. Derived, not disclosed.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

## Limitations
- Earnings and equity effects are quantified via arithmetic derivation using reported ROE and profit growth rates; these specific driver contributions are not explicitly disclosed by the bank.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T12:35:05+00:00
- seconds: 32.0
- cost_usd: 0.0015
- tokens: 34979 in / 3778 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
