# CBA — cti — FY21 vs FY20

**Movement (cash basis):** 46.3ppt → 47ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column FY20 -> column FY21*

CBA's headline cost-to-income ratio (cash basis) increased by 70 basis points from 46.3% in FY20 to 47.0% in FY21. This deterioration was driven by operating expense growth of 3.3% outpacing operating income growth of 1.7%. The movement includes higher remediation costs.

### expense_growth — "Operating expenses Cash basis"
*unquantified | confidence 80/100*

Operating expenses grew 3.3% ($10,996m to $11,359m), driven by higher remediation costs and other items, which weighed on the ratio as it exceeded income growth.
> [ev-3] CBA/FY21/profit_announcement, PDF p11: "Operating expenses Cash basis $11,359m FY20 $10,996m ▲3.3%"
> [ev-6] CBA/FY21/profit_announcement, printed p16: "Operating expenses including remediation costs and other - "cash basis" 11,359 10,996 3"

### income_growth — "Operating income Cash basis"
*unquantified | confidence 80/100*

Operating income grew 1.7% ($23,761m to $24,156m). Income growth lagged expense growth, contributing positively to the ratio increase.
> [ev-2] CBA/FY21/profit_announcement, PDF p11: "Operating income Cash basis $24,156m FY20 $23,761m ▲1.7%"
> [ev-14] CBA/FY21/profit_announcement, PDF p31: "Group Performance Summary"

### notable_items — "Remediation costs"
*unquantified | confidence 85/100*

Remediation costs increased from $461m in FY20 to $575m in FY21. Excluding these, the ratio improved by 10 basis points (44.7% to 44.6%), indicating the headline deterioration is largely attributable to this notable item.
> [ev-1] CBA/FY21/profit_announcement, PDF p37: "Operating expenses to total operating income ratio excluding remediation costs and other decreased 10 basis points from 44.7% to 44.6%."
> [ev-7] CBA/FY21/profit_announcement, printed p16: "Operating expenses to total operating income ratio excluding remediation costs and other increased 30 basis points from 44.3% to 44.6%."
> [ev-17] CBA/FY21/results_presentation, printed p9: "Operating Expenses Ex-Remediation FY20 10,535 FY21 10,784 Remediation FY20 461 FY21 575"

## Notable items
- Remediation costs increased by $114m year-on-year.

## Source disagreements
- **Ratio Definition (Headline vs Ex-Notable)** (definitional): 47.0% (Headline cash basis, ev-4) vs 44.6% (Ex-remediation cash basis, ev-1)
  Preferred: 47.0%. The task requires the headline measure. The bank reports a headline cash-basis ratio of 47.0% and an ex-remediation ratio of 44.6%. We report the headline movement.

## Limitations
- Quantified ppt contributions for individual drivers are not provided because the bank does not publish a JAWS walk chart for the headline ratio. Contributions are derived narratively from the disclosed income and expense growth rates.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-28T12:10:36+00:00
- seconds: 94.7
- cost_usd: 0.0025
- tokens: 53899 in / 7090 out
- orchestration: pipeline
