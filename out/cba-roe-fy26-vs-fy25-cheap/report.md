# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column FY25 -> column FY26*

CBA's cash ROE rose 50 bps to 14.0% in FY26, driven by a 7% increase in cash NPAT ($10,982m) which lifted ROE by approximately 94 bpts at constant equity. This was partially offset by a higher average net asset base ($78,238m vs $75,710m), contributing a negative drag of approximately 44 bpts.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Higher cash NPAT | +0.94 ppt | 80 | 1 (single_source) | ev-1, ev-7, ev-8 |
| `equity_effect` | Higher net assets | -0.44 ppt | 80 | 1 (single_source) | ev-1, ev-7 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "Higher cash NPAT"
*+0.94 ppt | confidence 80/100*

Derived: Prior ROE (13.5%) x Cash NPAT growth (7%). Ev-8 cites $730m (+7%) cash NPAT growth. Narrative states this drove the increase.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-8] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."

### equity_effect — "Higher net assets"
*-0.44 ppt | confidence 80/100*

Derived: Total delta (0.5 ppt) minus earnings effect (0.94 ppt). Ev-1 shows avg net assets grew from $75,710m to $78,238m (+3.3%), diluting ROE.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."

## Limitations
- Earnings and equity effects are derived arithmetic contributions, not explicitly quantified splits in the bank's disclosure.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T20:54:35+00:00
- seconds: 37.9
- cost_usd: 0.0015
- tokens: 34584 in / 3607 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
