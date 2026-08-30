# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income', column 31 Dec 24 -> column 31 Dec 25*

CBA's statutory cost-to-income ratio rose 70 basis points from 45.2% in 1H25 to 45.9% in 1H26. The movement was driven by a negative JAWS effect: operating expenses grew faster (8%) than operating income (6%), partially offset by the impact of notable items which increased costs in 1H26 but were absent in 1H25.

> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-10] CBA/1H26/profit_announcement, printed p2: "Total operating income"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | -0.3 ppt | 80 | 2 () | ev-10, ev-18, ev-24 |
| `expense_growth` | — | +0.6 ppt | 80 | 2 () | ev-3, ev-13, ev-19 |
| `notable_items` | Restructuring and notable items | +0.4 ppt | 80 | 2 () | ev-12, ev-26 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*-0.3 ppt | confidence 80/100*

Income growth of 6.6% exerted a negative contribution to the ratio, lowering it by approximately 30 basis points relative to the prior period.
> [ev-10] CBA/1H26/profit_announcement, printed p2: "Total operating income"
> [ev-18] CBA/1H26/results_presentation, printed p8: "Operating income $m 14,097 14,368 15,021 1H25 2H25 1H26"
> [ev-24] CBA/1H26/results_presentation, printed p24: "Operating income 15,021 6.6% 4.5%"

### expense_growth
*+0.6 ppt | confidence 80/100*

Expense growth of 8.2% exerted a positive contribution to the ratio, raising it by approximately 60 basis points as costs outpaced income growth.
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-13] CBA/1H26/profit_announcement, printed p2: "Total operating expenses"
> [ev-19] CBA/1H26/results_presentation, printed p8: "Operating expenses $m 6,372 6,494 6,720 1H25 2H25 1H26"

### notable_items — "Restructuring and notable items"
*+0.4 ppt | confidence 80/100*

Notable items of $170m in 1H26 (vs $0m in 1H25) added to expenses, contributing positively to the ratio increase.
> [ev-12] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹"
> [ev-26] CBA/1H26/results_presentation, printed p24: "Restructuring and notable items2 170"

## Notable items
- Restructuring and notable items of $170 million in 1H26 compared to nil in 1H25.

## Source disagreements
- **Headline Ratio Basis** (definitional): 45.9% (Profit Announcement) vs 39.9% (Results Presentation)
  Preferred: 45.9%. The Profit Announcement table explicitly labels the row 'Operating expenses to total operating income' with values 45.9%, matching the statutory block. The Results Presentation slide shows 39.9%, likely an underlying or different basis measure not matching the statutory headline definition.

## Limitations
- Contributions are estimated based on disclosed levels rather than a published walk chart for the statutory basis.
- The bank's narrative attributes the movement to higher income partly offset by higher expenses, consistent with the calculated JAWS effect.
- Basis normalised from 'statutory' to 'cash': no page in evidence prints 'statutory' beside the movement, and the registry names cash as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T18:44:40+00:00
- seconds: 46.0
- cost_usd: 0.0023
- tokens: 45782 in / 6785 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
