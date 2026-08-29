# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROE - cash basis', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE increased 10 basis points to 13.8% in 1H26 (ev-1). This movement is driven by a positive earnings effect from higher cash NPAT growth of 6%, partially offset by a negative equity effect due to the increase in average net assets.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.82 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-6 |
| `equity_effect` | — | -0.72 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3, ev-6 |
| *residual (unexplained)* | — | -0 ppt | — | — |

### earnings_effect
*+0.82 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) multiplied by cash NPAT growth (6.0%, ev-2). Represents the lift at constant equity. Cited from KPI table and profit announcement.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*-0.72 ppt | confidence 80/100*

Derived: total delta (0.1 ppt) minus earnings effect (0.82 ppt). Reflects dilution from higher average net assets ($78,004m vs $74,176m, ev-3), likely from retained earnings.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

## Source disagreements
- **Statutory ROE definition** (definitional): 13.6% (ev-8) vs 13.8% (ev-9)
  Preferred: 13.6%. The results book summary (ev-8) reports statutory ROE as 13.6%, while the detailed reconciliation table (ev-9) lists it as 13.8%. The summary figure is preferred for consistency with the primary narrative.

## Limitations
- Earnings and equity effects are derived arithmetic contributions, not explicitly disclosed by the bank.
- Residual is negligible but non-zero due to rounding of inputs.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T03:30:15+00:00
- seconds: 81.8
- cost_usd: 0.0016
- tokens: 31624 in / 4766 out
- orchestration: pipeline
