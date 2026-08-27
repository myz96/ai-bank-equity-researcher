# CBA — cti — FY21 vs FY20

**Movement (cash basis):** 46.3ppt → 47ppt (+0.7ppt) | **Attribution confidence:** 90/100

CBA's headline cost-to-income ratio (CTI) on a cash basis increased by 70 basis points to 47.0% in FY21 from 46.3% in FY20. This deterioration was driven primarily by operating expense growth (3.3%) outpacing operating income growth (1.7%). However, the underlying operational efficiency improved; the CTI excluding remediation costs and other items decreased by 10 basis points to 44.6%, indicating that the headline increase was largely attributable to higher remediation costs.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expenses | -0.5 ppt | 85 | 2 () | ev-2, ev-3, ev-22, ev-23 |
| `notable_items` | Remediation costs and other | +1.2 ppt | 85 | 1 (single_source) | ev-1, ev-6, ev-7, ev-8, ev-14 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expenses"
*-0.5 ppt | confidence 85/100*

Operating expenses grew 3.3% ($10,996m to $11,359m), significantly outpacing income growth. This negative jaws effect is the primary driver of the CTI deterioration. The impact is calculated as the difference between the expense growth rate and income growth rate applied to the base ratio.
> [ev-2] CBA/FY21/profit_announcement, PDF p11: "Operating expenses Cash basis $11,359m FY20 $10,996m ▲3.3%"
> [ev-3] CBA/FY21/profit_announcement, PDF p11: "Operating income Cash basis $24,156m FY20 $23,761m ▲1.7%"
> [ev-22] CBA/FY21/results_presentation, printed p27: "Operating Income 24,156 1.7% 2.0%"
> [ev-23] CBA/FY21/results_presentation, printed p27: "Operating Expenses 11,359 3.3% 3.2%"

### notable_items — "Remediation costs and other"
*+1.2 ppt | confidence 85/100*

Remediation costs increased from $461m to $575m (+25%). Excluding these items, the CTI actually improved by 10bps (44.3% to 44.6%). The inclusion of these higher notable items accounts for the majority of the headline deterioration.
> [ev-1] CBA/FY21/profit_announcement, PDF p37: "Operating expenses to total operating income ratio excluding remediation costs and other decreased 10 basis points from 44.7% to 44.6%."
> [ev-6] CBA/FY21/profit_announcement, printed p16: "Operating expenses to total operating income excluding remediation costs and other (%)"
> [ev-7] CBA/FY21/profit_announcement, printed p16: "Operating expenses to total operating income (%)"
> [ev-8] CBA/FY21/profit_announcement, printed p16: "Operating expenses to total operating income ratio excluding remediation costs and other increased 30 basis points from 44.3% to 44.6%."
> [ev-14] CBA/FY21/profit_announcement, PDF p31: "Remediation costs and other 2 (575) (461) 25"

## Notable items
- Remediation costs and other

## Source disagreements
- **Headline vs Underlying CTI Movement** (definitional): 47.0% (incl-remediation) vs 44.6% (ex-remediation)
  Preferred: 47.0%. The bank reports two distinct CTI metrics. The headline 'Cash basis' CTI includes remediation costs, while the 'ex-remediation' metric excludes them. Both are valid but measure different things. The analysis prioritizes the headline figure for the movement delta but uses the ex-remediation figure to isolate the structural driver.

## Limitations
- The attribution relies on a JAWS decomposition which assumes linear interaction effects. The residual is zero because the narrative explicitly attributes the change to expense growth relative to income growth and the specific volume of remediation costs.
- No detailed walk chart was provided in the evidence records to validate the exact split between organic expense growth and one-off items within the 'other' category.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-27T07:50:52+00:00
- seconds: 48.4
- cost_usd: 0.0013
- tokens: 23289 in / 4396 out
- orchestration: pipeline
