# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 90/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's statutory cost-to-income ratio rose 70 basis points from 45.2% in 1H25 to 45.9% in 1H26. The movement was driven by higher operating expenses (expense growth) partially offset by higher operating income (income growth). Underlying metrics improved by 50 basis points.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +0.8 ppt | 85 | 1 (single_source) | ev-3, ev-17 |
| `income_growth` | Operating income growth | -0.1 ppt | 90 | 2 () | ev-14, ev-23 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expense growth"
*+0.8 ppt | confidence 85/100*

Total operating expenses increased $518 million or 8% on the prior comparative period, rising from $6,372 million to $6,890 million. This expense growth exerted a positive pressure on the ratio.
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses"
> [ev-17] CBA/1H26/profit_announcement, printed p2: "Total operating expenses"

### income_growth — "Operating income growth"
*-0.1 ppt | confidence 90/100*

Total operating income increased $924 million or 7% on the prior comparative period, rising from $14,097 million to $15,021 million. This income growth exerted a negative pressure on the ratio.
> [ev-14] CBA/1H26/profit_announcement, printed p2: "Total operating income"
> [ev-23] CBA/1H26/results_presentation, printed p8: "Operating income $m 14,097 14,368 15,021 1H25 2H25 1H26"

## Notable items
- Restructuring and notable items of $170 million were incurred in 1H26, compared to nil in 1H25.

## Source disagreements
- **Underlying vs Statutory Movement** (definitional): Statutory: +70 bpts (45.2% to 45.9%) vs Underlying: -50 bpts (45.2% to 44.7%)
  Preferred: Statutory. The task requires the headline measure 'Operating expenses to total operating income'. The bank reports this as 45.9% for 1H26 and 45.2% for 1H25. The underlying ratio is a different measure excluding notable items.

## Limitations
- The narrative attributes the movement to JAWS drivers based on the arithmetic of the statutory endpoints. The bank's narrative explicitly discusses half-on-half movements (Jun 25 to Dec 25), which differ from the year-on-year comparison requested here.
- Basis normalised from 'statutory' to 'cash': no page in evidence prints 'statutory' beside the movement, and the registry names cash as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T20:46:33+00:00
- seconds: 54.4
- cost_usd: 0.0023
- tokens: 46252 in / 6963 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
