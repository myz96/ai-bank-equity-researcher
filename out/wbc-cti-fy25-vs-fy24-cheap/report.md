# WBC — cti — FY25 vs FY24

**Movement (ex_notables basis):** 50.3ppt → 53ppt (+2.7ppt) | **Attribution confidence:** 60/100

*Read from: row 'Cost-to-income ratio (ex Notable Items)', column Full Year Sept 2024 -> column Full Year Sept 2025*

WBC's headline cost-to-income ratio (ex Notable Items) widened by 270 bps to 53.0% in FY25 from 50.3% in FY24. This deterioration was driven by operating expenses growing faster than operating income. Total operating expenses rose 9% ($11,916m vs $10,944m), while net operating income grew only ~4.8% ($11,471m vs $10,947m). The expense growth outpaced the income growth, resulting in a negative jaws effect.

### expense_growth — "Operating expense growth"
*unquantified | confidence 80/100*

Total operating expenses increased 9% to $11,916 million (ev-1, ev-3). This growth rate exceeded the income growth rate, exerting negative pressure on the ratio.
> [ev-1] WBC/FY25/results_announcement, PDF p18: "Total operating expenses increased 9% to $11,916 million."
> [ev-3] WBC/FY25/results_announcement, PDF p18: "Total operating expenses
(11,916)
(10,944)
9"

### income_growth — "Operating income growth"
*unquantified | confidence 80/100*

Net operating income grew approximately 4.8% to $11,471 million from $10,947 million (ev-7). This slower growth relative to expenses contributed to the ratio widening.
> [ev-7] WBC/FY25/investor_discussion_pack, printed p119: "Net operating income 10,947 10,993 11,471"

## Source disagreements
- **Expense to income ratio ex Notable Items** (definitional): 53.0% - WBC/FY25/results_announcement (ev-2) vs 45.7% - WBC/FY25/investor_discussion_pack (ev-5)
  Preferred: 53.0%. The results announcement (ev-2) reports the 'expense to income ratio excluding Notable Items' as 53.0%. The investor discussion pack (ev-5) reports 'Expense to income (%)' as 45.7% for FY25. Given the source hierarchy and the explicit label match with the task's required measure ('ex Notable Items'), the 53.0% figure is preferred. The 45.7% figure likely represents a different basis or definition not explicitly labeled 'ex Notable Items' in the same manner, or potentially includes/not includes specific items differently.

## Limitations
- The bank does not provide a quantified JAWS bridge (ppt contribution of income vs expense growth) in the provided evidence. Contributions are inferred from growth rates rather than stated ppt splits.
- There is a definitional disagreement between the results announcement (53.0%) and the investor discussion pack (45.7%) for the 'ex Notable Items' ratio. The analysis uses the results announcement figure based on source hierarchy and label matching.
- No walk charts were extracted, so driver contributions are not derived from a validated primary walk.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-29T18:13:03+00:00
- seconds: 54.6
- cost_usd: 0.0014
- tokens: 33491 in / 2756 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p26 page 125 [added]']
