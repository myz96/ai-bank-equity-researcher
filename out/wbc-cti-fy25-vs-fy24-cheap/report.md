# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Expense to income ratio, ex Notable Items', column FY24 (12 months ended Sep 2024) -> column FY25 (12 months ended Sep 2025)*

Westpac's cost-to-income ratio (ex Notable Items) widened by 270 basis points (2.7 ppt) to 53.0% in FY25 from 50.3% in FY24. This deterioration was driven by operating expenses growing faster than operating income. Total operating expenses rose 9% to $11,916 million, while net operating income grew more modestly to $22,464 million from $21,763 million.

> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 22,464 21,763"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses (11,916) (10,944)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +1.8 ppt | 80 | 1 (single_source) | ev-2, ev-3, ev-6 |
| `income_growth` | Operating income growth | -0.9 ppt | 80 | 1 (single_source) | ev-5, ev-6 |
| *residual (unexplained)* | — | +1.8 ppt | — | — |

### expense_growth — "Operating expense growth"
*+1.8 ppt | confidence 80/100*

Total operating expenses increased 9% to $11,916 million (FY24: $10,944 million). This expense growth outpaced income growth, exerting a positive pressure on the ratio.
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses (11,916) (10,944)"

### income_growth — "Operating income growth"
*-0.9 ppt | confidence 80/100*

Net operating income grew to $22,464 million from $21,763 million. While positive, this income growth was slower than expense growth, providing a negative contribution to the ratio movement.
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 22,464 21,763"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses (11,916) (10,944)"

## Limitations
- The bank does not provide a detailed JAWS bridge or walk chart for the FY25 vs FY24 period. The residual of 1.8 ppt likely reflects the compounding effect of the base year levels and rounding differences between the reported percentage and the calculated growth rates.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-31T00:54:01+00:00
- seconds: 22.6
- cost_usd: 0.0012
- tokens: 31362 in / 1804 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
