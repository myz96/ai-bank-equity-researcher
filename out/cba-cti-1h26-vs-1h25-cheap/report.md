# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's statutory cost-to-income ratio rose 70 basis points from 45.2% in 1H25 to 45.9% in 1H26 (ev-2). The movement was driven by higher operating expenses partially offset by higher operating income. Underlying metrics improved by 50 basis points to 44.7% as the bank excluded $170 million of restructuring and notable items.

> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%)"
> [ev-5] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."
> [ev-11] CBA/1H26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-13] CBA/1H26/profit_announcement, PDF p32: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | — | +0.8 ppt | 80 | 1 (single_source) | ev-3, ev-16 |
| `income_growth` | — | -0.1 ppt | 80 | 2 () | ev-14, ev-28 |
| `notable_items` | — | +0 ppt | 90 | 2 () | ev-16, ev-30 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth
*+0.8 ppt | confidence 80/100*

Operating expenses grew 8.2% ($6,372m to $6,890m), outpacing income growth and raising the ratio. This includes $170m of restructuring costs (ev-3, ev-16).
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses"
> [ev-16] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹"

### income_growth
*-0.1 ppt | confidence 80/100*

Total operating income grew 6.6% ($14,097m to $15,021m), which lowered the ratio. Growth was led by an 8% increase in net interest income (ev-14, ev-28).
> [ev-14] CBA/1H26/profit_announcement, printed p2: "Total operating income"
> [ev-28] CBA/1H26/results_presentation, printed p24: "Operating income 15,021 6.6% 4.5%"

### notable_items
*+0 ppt | confidence 90/100*

The statutory ratio includes $170m of restructuring and notable items in 1H26, compared to zero in 1H25. These items are a primary driver of the expense growth.
> [ev-16] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹"
> [ev-30] CBA/1H26/results_presentation, printed p24: "Restructuring and notable items2 170"

## Notable items
- Restructuring and notable items: $170m in 1H26 vs $0m in 1H25.

## Source disagreements
- **Underlying vs Statutory Ratio Movement** (definitional): Statutory +70 bpts (ev-2) vs Underlying -50 bpts (ev-5)
  Preferred: Statutory +70 bpts. The task requires the headline statutory measure. The underlying ratio is a different measure that excludes notable items.

## Limitations
- Quantified contributions for income and expense growth are computed deltas rather than explicit walk bars provided by the bank.
- Basis normalised from 'statutory' to 'cash': no page in evidence prints 'statutory' beside the movement, and the registry names cash as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T14:43:21+00:00
- seconds: 60.6
- cost_usd: 0.002
- tokens: 36045 in / 7098 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
