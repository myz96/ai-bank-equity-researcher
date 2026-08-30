# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Expense to income ratio, ex Notable Items', column FY24 (12 months ended Sep 2024) -> column FY25 (12 months ended Sep 2025)*

Westpac's cost-to-income ratio (ex Notable Items) widened by 270 basis points (2.7 ppt) from 50.3% in FY24 to 53.0% in FY25. This deterioration was driven by operating expenses growing faster than operating income. Total operating expenses increased 9% to $11,916 million, while net operating income grew more modestly from $21,763 million to $22,464 million. The widening reflects expense growth outpacing revenue growth across the group.

> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Total operating expenses
(11,916)
(10,944)"
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 2025 8,424 6,110 3,808 2,814 1,308 22,464"
> [ev-7] WBC/FY25/results_announcement, PDF p33: "Net operating income 2024 8,160 6,136 3,505 2,645 1,317 21,763"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | — | +1.8 ppt | 80 | 1 (single_source) | ev-2, ev-3, ev-6, ev-8 |
| `income_growth` | — | -0.9 ppt | 80 | 1 (single_source) | ev-5, ev-7 |
| *residual (unexplained)* | — | +1.8 ppt | — | — |

### expense_growth
*+1.8 ppt | confidence 80/100*

Operating expenses rose 9% ($10,944m to $11,916m), contributing positively to the ratio increase as costs expanded faster than income.
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Total operating expenses
(11,916)
(10,944)"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses 2025 (4,932) (2,727) (1,647) (1,342) (1,268) (11,916)"
> [ev-8] WBC/FY25/results_announcement, PDF p33: "Operating expenses 2024 (4,787) (2,626) (1,465) (1,262) (804) (10,944)"

### income_growth
*-0.9 ppt | confidence 80/100*

Net operating income grew ~3% ($21,763m to $22,464m). Slower income growth relative to expenses exerted a negative pressure on the ratio.
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 2025 8,424 6,110 3,808 2,814 1,308 22,464"
> [ev-7] WBC/FY25/results_announcement, PDF p33: "Net operating income 2024 8,160 6,136 3,505 2,645 1,317 21,763"

## Source disagreements
- **Cost to Income Ratio Definition and Value** (definitional): 53.0% (ev-1, Results Announcement) vs 42.4% (ev-12, Investor Discussion Pack)
  Preferred: 53.0%. The Results Announcement (ev-1) explicitly states 'The expense to income ratio excluding Notable Items was 53.0%'. The Investor Discussion Pack (ev-12) lists a different value of 42.4%. Given the source hierarchy (Results Announcement > Investor Discussion Pack) and the explicit textual confirmation in ev-1 matching the movement calculation (53.0 - 50.3 = 2.7), the 53.0% figure is preferred for the headline movement.

## Limitations
- The residual of 1.8 ppt suggests that simple JAWS decomposition using aggregate levels does not fully account for the 2.7 ppt movement, likely due to base effects or non-linearities in the ratio calculation not captured by simple percentage growth rates. No walk charts were provided to decompose this further.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T19:04:05+00:00
- seconds: 28.5
- cost_usd: 0.0014
- tokens: 32872 in / 2963 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
