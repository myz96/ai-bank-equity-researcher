# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Expense to income ratio, ex Notable Items', column FY24 (12 months ended Sep 2024) -> column FY25 (12 months ended Sep 2025)*

Westpac's cost-to-income ratio (ex Notable Items) widened by 270 bps to 53.0% in FY25 from 50.3% in FY24. This deterioration was driven by operating expenses growing faster than operating income. Total operating expenses rose 9% to $11,916 million, while total operating income grew only 3% to $22,464 million.

> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"
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

Operating expenses increased 9% ($11,916m vs $10,944m), contributing positively to the ratio widening as costs outpaced income growth.
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses 2025 (4,932) (2,727) (1,647) (1,342) (1,268) (11,916)"
> [ev-8] WBC/FY25/results_announcement, PDF p33: "Operating expenses 2024 (4,787) (2,626) (1,465) (1,262) (804) (10,944)"

### income_growth
*-0.9 ppt | confidence 80/100*

Operating income grew 3% ($22,464m vs $21,763m). Slower income growth relative to expenses exerted a negative pressure on the ratio.
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 2025 8,424 6,110 3,808 2,814 1,308 22,464"
> [ev-7] WBC/FY25/results_announcement, PDF p33: "Net operating income 2024 8,160 6,136 3,505 2,645 1,317 21,763"

## Source disagreements
- **Headline Ratio Definition** (definitional): 53.0% (Results Announcement ev-1) vs 42.4% (Investor Discussion Pack ev-13)
  Preferred: 53.0%. The Results Announcement explicitly states 'The expense to income ratio excluding Notable Items was 53.0%'. The IDP table at ev-13 lists 42.4% but lacks the explicit 'ex Notable Items' label in the row header shown in the extract, and the magnitude difference suggests it may be a statutory or different basis measure. Per source hierarchy, the Results Announcement text is preferred.

## Limitations
- The residual of 1.8 ppt indicates that the simple JAWS decomposition (based on aggregate growth rates) does not fully account for the 2.7 ppt movement, likely due to timing differences in revenue/expense recognition or base effects not captured by simple period-over-period growth rates. No walk charts were provided to decompose this further.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T16:36:35+00:00
- seconds: 27.4
- cost_usd: 0.0013
- tokens: 32285 in / 2354 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
