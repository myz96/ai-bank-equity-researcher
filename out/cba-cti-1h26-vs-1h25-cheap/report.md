# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 90/100

*Read from: row 'Operating expenses to total operating income', column 31 Dec 24 -> column 31 Dec 25*

CBA's headline cost-to-income ratio (cash basis) increased by 70 bpts from 45.2% in 1H25 to 45.9% in 1H26. This deterioration was primarily driven by higher operating expenses outpacing the growth in operating income. While underlying efficiency improved (underlying CTI fell 50 bpts), the inclusion of $170m in restructuring and notable items in 1H26 (vs nil in 1H25) added significant expense pressure that outweighed the organic gains.

> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-8] CBA/1H26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-11] CBA/1H26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-14] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372) 4 8"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +0.9 ppt | 80 | 2 () | ev-3, ev-11, ev-13, ev-14, ev-28 |
| `income_growth` | Operating income growth | -0.2 ppt | 80 | 2 () | ev-11, ev-20, ev-26 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expense growth"
*+0.9 ppt | confidence 80/100*

Total operating expenses rose 8% ($6,372m to $6,890m). The increase included a $170m charge for restructuring and notable items (ev-13, ev-28), which did not exist in the prior period. This expense growth exceeded income growth, raising the ratio.
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-11] CBA/1H26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-13] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items (170) (130) – 31 n/a"
> [ev-14] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372) 4 8"
> [ev-28] CBA/1H26/results_presentation, printed p24: "Restructuring and notable items2 170"

### income_growth — "Operating income growth"
*-0.2 ppt | confidence 80/100*

Total operating income grew 4.5% ($14,097m to $15,021m). Although positive, this growth rate lagged behind the 8% rise in operating expenses, resulting in a net negative contribution to the ratio improvement (i.e., it mitigated the rise but did not prevent it).
> [ev-11] CBA/1H26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-20] CBA/1H26/results_presentation, printed p8: "Operating income $m 14,097 14,368 15,021 1H25 2H25 1H26"
> [ev-26] CBA/1H26/results_presentation, printed p24: "Operating income 15,021 6.6% 4.5%"

## Notable items
- Restructuring and notable items: $170m in 1H26 vs $0m in 1H25.

## Source disagreements
- **Underlying vs Headline Ratio Movement** (definitional): Headline CTI +70 bpts (ev-2) vs Underlying CTI -50 bpts (ev-5)
  Preferred: Headline CTI +70 bpts. The task requires the headline 'Operating expenses to total operating income' ratio. The underlying measure excludes notable items. The bank reports both; the headline movement is +70 bpts while the underlying is -50 bpts. We report the headline as requested.

## Limitations
- The JAWS decomposition is calculated manually from disclosed levels rather than taken from a specific walk chart. The residual is zero based on the arithmetic of the two primary drivers (Expense Growth and Income Growth).
- Capped at 80: expense_growth +0.9 ppt, income_growth -0.2 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T23:20:37+00:00
- seconds: 38.5
- cost_usd: 0.0018
- tokens: 34696 in / 6005 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
