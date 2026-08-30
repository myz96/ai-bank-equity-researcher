# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Expense to income ratio, ex Notable Items', column FY24 -> column FY25*

Westpac's cost-to-income ratio (ex Notable Items) widened by 270 basis points to 53.0% in FY25 from 50.3% in FY24. This deterioration was driven by operating expenses growing faster than operating income. Total operating expenses rose 9% to $11,916 million, while net operating income grew approximately 3% to $22,464 million.

> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 2025 8,424 6,110 3,808 2,814 1,308 22,464"
> [ev-7] WBC/FY25/results_announcement, PDF p33: "Net operating income 2024 8,160 6,136 3,505 2,645 1,317 21,763"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +4.8 ppt | 80 | 1 (single_source) | ev-2, ev-3 |
| `income_growth` | Operating income growth | -2.1 ppt | 80 | 1 (single_source) | ev-5, ev-7 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expense growth"
*+4.8 ppt | confidence 80/100*

Total operating expenses increased 9% ($972m) to $11,916m (ev-2, ev-3). This outpaced income growth, raising the ratio. The bank does not provide a specific ppt attribution for this driver in the narrative.
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"

### income_growth — "Operating income growth"
*-2.1 ppt | confidence 80/100*

Net operating income grew ~3% to $22,464m (ev-5, ev-7), lagging behind expense growth. This slower income growth contributed to the ratio widening.
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 2025 8,424 6,110 3,808 2,814 1,308 22,464"
> [ev-7] WBC/FY25/results_announcement, PDF p33: "Net operating income 2024 8,160 6,136 3,505 2,645 1,317 21,763"

## Limitations
- The bank does not publish a formal JAWS bridge or walk chart for the cost-to-income ratio movement. Contributions are derived mechanically from headline income and expense levels rather than stated driver attributions.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T15:04:36+00:00
- seconds: 26.8
- cost_usd: 0.0013
- tokens: 32773 in / 2679 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
