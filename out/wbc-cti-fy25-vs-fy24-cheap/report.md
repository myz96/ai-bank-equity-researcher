# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 40/100

*Read from: row 'Cost-to-income ratio (ex-notables)', column Full Year Sept 2024 -> column Full Year Sept 2025*

WBC's cost-to-income ratio (ex-notables) widened by 270 bps to 53.0% in FY25 from 50.3% in FY24. This deterioration was driven by operating expenses growing faster than operating income.

### expense_growth — "Operating expense growth"
*unquantified | confidence 80/100*


> [ev-1] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Total operating expenses
(11,916)
(10,944)
9"

### income_growth — "Operating income growth"
*unquantified | confidence 80/100*

Net operating income grew from $10,947m to $11,471m, an increase of approximately 4.8% (ev-7). Income growth lagged expense growth, contributing to the higher ratio.
> [ev-7] WBC/FY25/investor_discussion_pack, printed p119: "Net operating income 10,947 10,993 11,471"

## Source disagreements
- **Headline vs Ex-Notable Ratio** (definitional): 53.0% (ex-notables basis, ev-2) vs 44.0% (headline implied, ev-5)
  Preferred: 53.0% (ex-notables). The task requires the headline measure. However, the provided evidence for the headline 'Expense to income' (ev-5) shows 44.0%, while the ex-notable measure (ev-2) shows 53.0%. The validation history flagged that reading the ex-notable row as the headline was a failure. Without explicit FY24/FY25 headline numbers in the text, I cannot compute the headline movement accurately. I have reported the ex-notable movement as it is the only fully quantified period-over-period comparison available in the evidence records (ev-2), but this represents a deviation from the strict 'headline' instruction due to missing data.

## Limitations
- The requested 'headline' cost-to-income ratio endpoints were not explicitly provided in the evidence records for both FY24 and FY25. The evidence contains the 'ex-notables' ratio (ev-2) and half-year headline ratios (ev-5). To avoid guessing, I reported the movement for the 'ex-notables' ratio, which is clearly defined in the bank vocabulary as a distinct measure. The headline ratio movement cannot be calculated with certainty from the provided snippets.
- Failed check: movement_from_variant (the row you read is a 'ex-notable' variant: row 'Cost-to-income ratio (ex-notables)', column Full Year Sept 2024 -> column Full Year Sept 2025. Read the headline measure instead, and report the variant as context or as a disagreement)
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T13:51:07+00:00
- seconds: 85.7
- cost_usd: 0.0012
- tokens: 30280 in / 2435 out
- orchestration: pipeline
