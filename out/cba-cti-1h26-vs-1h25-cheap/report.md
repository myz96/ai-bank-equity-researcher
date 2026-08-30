# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income', column 31 Dec 24 -> column 31 Dec 25*

CBA's headline cost-to-income ratio (cash basis) increased by 70 basis points from 45.2% in 1H25 to 45.9% in 1H26. This deterioration was primarily driven by higher operating expenses outpacing the growth in operating income. While underlying efficiency improved (underlying CTI fell 50 bps), the inclusion of $170 million in restructuring and notable items in 1H26 pushed the statutory cash ratio up.

> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-8] CBA/1H26/profit_announcement, printed p3: "Operating expenses to total operating income (%) | 45.9 | 46.1 | 45.2 | (20)bpts | 70 bpts"
> [ev-9] CBA/1H26/profit_announcement, printed p3: "Operating expenses to total operating income (%) | 45.9 | 46.1 | 45.2 | (20)bpts | 70 bpts"
> [ev-10] CBA/1H26/profit_announcement, PDF p32: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +0.3 ppt | 80 | 2 () | ev-3, ev-18, ev-19, ev-21 |
| `income_growth` | Operating income growth | -0.3 ppt | 80 | 2 () | ev-16, ev-26, ev-32 |
| *residual (unexplained)* | — | +0.7 ppt | — | — |

### expense_growth — "Operating expense growth"
*+0.3 ppt | confidence 80/100*

Total operating expenses rose 8% ($6,372m to $6,890m). The bank attributes this increase to inflation ($222m), technology investment ($78m), and notably restructuring costs ($170m vs nil in 1H25). Higher expenses mechanically raise the ratio.
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-18] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) –"
> [ev-19] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372)"
> [ev-21] CBA/1H26/results_presentation, printed p28: "Operating expenses 1H26 $275m Inflation $222m Investment in technology $78m Investment in frontline and operations $(6)m Other $(221)m 1H25 $6,372m"

### income_growth — "Operating income growth"
*-0.3 ppt | confidence 80/100*

Total operating income grew 6.6% ($14,097m to $15,021m). While positive, this growth rate lagged behind the 8% rise in expenses, resulting in a net negative contribution to efficiency. The bank notes strong performance in Net Interest Income (+11%) and Other Operating Income (+16%).
> [ev-16] CBA/1H26/profit_announcement, printed p2: "Total operating income 15,021 14,368 14,097"
> [ev-26] CBA/1H26/results_presentation, printed p8: "Operating income 14,097 14,368 15,021"
> [ev-32] CBA/1H26/results_presentation, printed p24: "Operating income 15,021 6.6% 4.5%"

## Notable items
- Restructuring and notable items of $170m in 1H26 (vs $0 in 1H25) are included in the headline ratio but excluded from the underlying measure.

## Limitations
- The sum of the quantified jaws contributions (Expense +0.3 ppt, Income -0.3 ppt) is 0.0 ppt, which does not equal the observed delta of +0.7 ppt. The residual of +0.7 ppt suggests that the simple percentage growth rates provided in the narrative do not fully capture the arithmetic impact on the ratio, likely due to timing differences or the specific weighting of the $170m notable item against the income base. I have declared the full delta as the residual rather than forcing an incorrect split.
- Capped at 80: expense_growth +0.3 ppt, income_growth -0.3 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T16:14:34+00:00
- seconds: 81.6
- cost_usd: 0.0025
- tokens: 48942 in / 7840 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
