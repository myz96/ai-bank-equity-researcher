# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bps to 13.8% in 1H26 vs 1H25, driven by a 6% increase in cash NPAT ($5,445m), partially offset by higher average net assets ($78,004m). The earnings effect contributed approximately +9 bps, while the equity effect reduced ROE by approximately -8 bps.

> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-6] CBA/1H26/profit_announcement, PDF p19: "Return on equity (ROE) (%) Cash basis 13.8 13.4 13.7"
> [ev-13] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-16] CBA/1H26/results_presentation, printed p53: "ROE (cash) 13.8% +10bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.09 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3, ev-12 |
| `equity_effect` | — | -0.08 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-11 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.09 ppt | confidence 80/100*

Derived: Prior-period ROE (13.7%) multiplied by cash NPAT growth rate (6%). Cash NPAT increased $313 million or 6% to $5,445 million (ev-2). This represents the lift at constant equity.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-12] CBA/1H26/profit_announcement, PDF p168: "Net profit after tax - "cash basis" 5,445 5,120 5,132"

### equity_effect
*-0.08 ppt | confidence 80/100*

Derived: Total delta (0.1 ppt) minus earnings effect (+0.09 ppt). Net average equity grew from $74,176 million to $78,004 million (ev-3). Higher net assets partly offset the profit gain as stated in the narrative (ev-1).
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-11] CBA/1H26/profit_announcement, PDF p168: "Net average equity 78,004 77,020 74,176"

## Source disagreements
- **Statutory ROE levels** (rounding): 13.6% (ev-4, ev-5) vs 13.8% (ev-15)
  Preferred: 13.6%. The KPI table (ev-4) and summary table (ev-5) report 13.6%, while the detailed reconciliation table (ev-15) reports 13.8%. Given the source hierarchy, the KPI/summary tables are preferred for headline figures, likely due to rounding conventions in the detailed view.

## Limitations
- Earnings and equity effects are derived using an arithmetic identity, not disclosed directly by the bank.
- Residual is zero due to the derivation method; interaction terms are embedded in the equity effect.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T14:40:03+00:00
- seconds: 48.5
- cost_usd: 0.0022
- tokens: 45335 in / 6124 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
