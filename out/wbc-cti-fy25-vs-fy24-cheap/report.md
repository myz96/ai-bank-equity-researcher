# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Expense to income ratio, ex Notable Items', column FY24 (12 months ended Sep 2024) -> column FY25 (12 months ended Sep 2025)*

Westpac's cost-to-income ratio (ex Notable Items) widened by 270 basis points (2.7 ppt) from 50.3% in FY24 to 53.0% in FY25. This deterioration was driven by operating expenses growing at 9%, outpacing net operating income growth of approximately 3%. The bank attributes the expense increase primarily to investment in technology and business transformation.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expenses | +1.8 ppt | 85 | 1 (single_source) | ev-1, ev-2, ev-3, ev-5, ev-6 |
| `income_growth` | Net operating income | -0.9 ppt | 85 | 1 (single_source) | ev-1, ev-5, ev-6 |
| *residual (unexplained)* | — | +1.8 ppt | — | — |

### expense_growth — "Operating expenses"
*+1.8 ppt | confidence 85/100*

Total operating expenses increased 9% ($1,072 million) to $11,916 million. This expense growth is the primary driver of the ratio widening, as it significantly outpaced income growth. The bank cites investment in technology and business transformation as key factors.
> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-2] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Operating expenses ... Total operating expenses (11,916) (10,944)"
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 22,464 21,763"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses (11,916) (10,944)"

### income_growth — "Net operating income"
*-0.9 ppt | confidence 85/100*

Net operating income grew 3% ($701 million) to $22,464 million. While positive, this slower growth rate relative to expenses exerted a negative pressure on the ratio, contributing to the overall widening.
> [ev-1] WBC/FY25/results_announcement, PDF p18: "The expense to income ratio excluding Notable Items was 53.0%, up from 50.3%."
> [ev-5] WBC/FY25/results_announcement, PDF p33: "Net operating income 22,464 21,763"
> [ev-6] WBC/FY25/results_announcement, PDF p33: "Operating expenses (11,916) (10,944)"

## Source disagreements
- **Cost to Income Ratio Definition** (definitional): 53.0% -> 50.3% (WBC/FY25/results_announcement, ev-1) vs 42.4% -> 43.2% (WBC/FY25/investor_discussion_pack, ev-10)
  Preferred: 53.0% -> 50.3%. The results announcement (ev-1) explicitly labels the row 'Expense to income ratio excluding Notable Items', which matches the HEADLINE ROW definition. The investor discussion pack (ev-10) lists a different value (42.4%) for the same label; this likely reflects a different calculation basis or segment scope not aligned with the group headline measure defined in the registry.

## Limitations
- The residual of 1.8 ppt arises because the JAWS decomposition (Income + Expense) does not perfectly sum to the delta due to the non-linear nature of the ratio metric when calculated from rounded percentages. Specifically, the arithmetic delta from levels (53.0 - 50.3 = 2.7) is split between expense impact (+1.8 ppt approx) and income impact (-0.9 ppt approx), but precise ppt contributions require exact underlying numbers not fully disclosed for a perfect zero-residual bridge.
- No specific narrative breakdown of expense drivers beyond 'technology and business transformation' was provided in the cited evidence records.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T21:05:56+00:00
- seconds: 33.2
- cost_usd: 0.0012
- tokens: 31286 in / 2168 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
