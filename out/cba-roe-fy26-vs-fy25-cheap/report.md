# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column FY25 -> column FY26*

CBA's cash ROE rose 50 bps to 14.0% in FY26, driven by a 7% increase in cash NPAT ($10,982m) which lifted ROE at constant equity, partially offset by higher average net assets ($78,238m). The earnings effect contributed approximately 0.95 ppt, while the equity effect reduced ROE by approximately 0.45 ppt.

> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-5] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-6] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-10] CBA/FY26/profit_announcement, PDF p146: "ROE – cash basis (%) 14.0 13.5 14.3 13.8"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.95 ppt | 80 | 2 () | ev-1, ev-6, ev-14 |
| `equity_effect` | — | -0.45 ppt | 80 | 1 (single_source) | ev-1, ev-8 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.95 ppt | confidence 80/100*

Derived: Prior ROE (13.5%) x Cash NPAT growth (7.1%). Higher cash NPAT of $10,982m (+$730m) drove this lift. Cited ev-1, ev-6, ev-14.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-6] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-14] CBA/FY26/results_presentation, printed p54: "Cash NPAT ($m) 10,982 +7.1%"

### equity_effect
*-0.45 ppt | confidence 80/100*

Derived: Total delta (0.5 ppt) minus earnings effect (0.95 ppt). Reflects dilution from higher average net assets ($78,238m vs $75,710m), likely due to retained earnings or capital actions. Cited ev-1, ev-8.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "Return on Equity – cash basis"
> [ev-8] CBA/FY26/profit_announcement, PDF p146: "Net average equity 78,238 75,710 77,968 78,004"

## Limitations
- Earnings and equity effects are derived arithmetic contributions, not disclosed bank splits. Confidence capped at 80 due to derivation.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:54:25+00:00
- seconds: 46.8
- cost_usd: 0.0015
- tokens: 34780 in / 3559 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
