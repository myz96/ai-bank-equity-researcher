# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE increased by 10 basis points to 13.8% in 1H26, driven by a 6% growth in cash NPAT which was partially offset by an increase in average net assets.

> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-6] CBA/1H26/profit_announcement, PDF p19: "Return on equity (ROE) (%) Cash basis 13.8 13.4 13.7"
> [ev-11] CBA/1H26/results_presentation, printed p53: "ROE (cash) 13.8% +10bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.08 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3 |
| `equity_effect` | — | +0.02 ppt | 80 | 1 (single_source) | ev-1, ev-3 |

### earnings_effect
*+0.08 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) multiplied by the stated cash NPAT growth rate (6%). This reflects the lift at constant equity from higher earnings.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*+0.02 ppt | confidence 80/100*

Residual: total delta minus earnings effect. Driven by higher average net assets ($78,004m vs $74,176m), likely due to retained earnings and capital generation outpacing distributions.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"

## Source disagreements
- **Statutory ROE Definition** (definitional): 13.6% - ev-4 vs 13.8% - ev-5
  Preferred: 13.6%. The KPI table (ev-4) reports statutory ROE as 13.6%, while the summary table (ev-5) lists it as 13.8%. The KPI table is the primary source for detailed metrics.

## Limitations
- Earnings and equity effects are derived using a multiplicative identity rather than disclosed additive drivers.
- Confidence capped at 80 because the split is computed from reported levels and growth rates, not explicitly quantified by the bank.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T16:11:18+00:00
- seconds: 75.3
- cost_usd: 0.0021
- tokens: 44927 in / 5796 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
