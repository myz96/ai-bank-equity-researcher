# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 75/100

*Read from: row 'Expense to income ratio, ex Notable Items', column FY24 (12 months ended Sep 2024) -> column FY25 (12 months ended Sep 2025)*

Westpac's cost-to-income ratio (ex Notable Items) widened by 270 basis points to 53.0% in FY25 from 50.3% in FY24. This deterioration was driven by operating expenses growing faster than net operating income. Expenses rose 9% overall and 6% excluding restructuring charges, while net operating income grew only 3%. The bank attributes the expense growth primarily to restructuring costs and inflationary pressures.

> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Excluding this charge, operating expenses increased by 6%"
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Excluding Notable Items, $m ... Net operating income ... Group ... 2025 22,464 ... 2024 21,763"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Excluding Notable Items, $m ... Operating expenses ... Group ... 2025 (11,916) ... 2024 (10,944)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +2 ppt | 85 | 1 (single_source) | ev-2, ev-3, ev-4, ev-6 |
| `income_growth` | Net operating income growth | -0.7 ppt | 85 | 1 (single_source) | ev-5 |
| *residual (unexplained)* | — | +1.4 ppt | — | — |

### expense_growth — "Operating expense growth"
*+2 ppt | confidence 85/100*


> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Excluding this charge, operating expenses increased by 6%"
> [ev-4] WBC/FY25/results_announcement, PDF p18: "Total operating expenses (11,916) (10,944)"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Excluding Notable Items, $m ... Operating expenses ... Group ... 2025 (11,916) ... 2024 (10,944)"

### income_growth — "Net operating income growth"
*-0.7 ppt | confidence 85/100*

Net operating income (ex Notable Items) grew 3% ($22,464m vs $21,763m). Slower income growth relative to expenses contributed negatively to the ratio improvement.
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Excluding Notable Items, $m ... Net operating income ... Group ... 2025 22,464 ... 2024 21,763"

## Source disagreements
- **Cost to Income Ratio Value** (definitional): 53.0% (Results Announcement ev-1) vs 42.4% (Investor Discussion Pack ev-10)
  Preferred: 53.0%. The Results Announcement (ev-1) explicitly states the 'expense to income ratio excluding Notable Items' was 53.0%. The Investor Discussion Pack (ev-10) lists a different value of 42.4% for the same label. Given the source hierarchy (Profit Announcement > Presentation), the 53.0% figure is preferred. The 42.4% figure may refer to a different period or basis not fully clarified in the snippet, or represents a discrepancy.

## Limitations
- The JAWS decomposition is approximate. The residual of 1.4 ppt suggests that the simple percentage growth rates provided (9% exp, 3% inc) do not perfectly map to the ppt movement due to base effects or other minor components not detailed in the text snippets.
- The evidence record ev-10 presents a conflicting ratio value (42.4%) which is significantly lower than the headline 53.0%. This disagreement is noted but the higher value from the primary announcement is used.
- Detailed breakdown of expense drivers (e.g., specific cost categories) beyond 'restructuring' is not available in the provided evidence records.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T12:45:23+00:00
- seconds: 33.2
- cost_usd: 0.0013
- tokens: 31761 in / 2429 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
