# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 85/100

*Read from: row 'Operating expenses to total operating income', column 31 Dec 24 -> column 31 Dec 25*

CBA's statutory cost-to-income ratio rose 70 basis points from 45.2% in 1H25 to 45.9% in 1H26 (ev-2). The movement was driven by higher operating expenses partly offset by higher operating income. Underlying costs improved by 50 basis points to 44.7%, but statutory notable items of $170m widened the headline ratio.

> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-5] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."
> [ev-11] CBA/1H26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-12] CBA/1H26/profit_announcement, PDF p32: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `notable_items` | Restructuring and notable items | +0.7 ppt | 85 | 1 (single_source) | ev-2, ev-5, ev-15 |

### expense_growth — "Higher operating expenses"
*unquantified | confidence 80/100*

Total operating expenses increased 8% year-on-year from $6,372m to $6,890m (ev-3). This expense growth exerted upward pressure on the ratio, partially offsetting the benefit from income growth.
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"

### income_growth — "Higher operating income"
*unquantified | confidence 80/100*

Total operating income grew 6.6% year-on-year from $14,097m to $15,021m (ev-13, ev-23). This income growth provided a downward contribution to the ratio, mitigating the impact of rising expenses.
> [ev-13] CBA/1H26/profit_announcement, printed p2: "Total operating income"
> [ev-23] CBA/1H26/results_presentation, printed p8: "Operating income 14,097 14,368 15,021"

### notable_items — "Restructuring and notable items"
*+0.7 ppt | confidence 85/100*

The widening of the statutory ratio versus the underlying ratio is fully explained by restructuring and notable items. These items were nil in 1H25 but totaled $170m in 1H26 (ev-15), pushing the statutory ratio up while the underlying ratio fell 50 basis points (ev-5).
> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-5] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."
> [ev-15] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹"

## Notable items
- Restructuring and notable items: $170m in 1H26 vs $0m in 1H25.

## Limitations
- The bank does not provide a quantitative JAWS split for the statutory ratio; contributions are inferred from the delta between statutory and underlying movements.
- Basis normalised from 'statutory' to 'cash': no page in evidence prints 'statutory' beside the movement, and the registry names cash as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T12:25:35+00:00
- seconds: 46.2
- cost_usd: 0.0019
- tokens: 35595 in / 6689 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
