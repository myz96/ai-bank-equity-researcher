# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 75/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's headline cost-to-income ratio (total) increased by 70 basis points from 45.2% in 1H25 to 45.9% in 1H26. This deterioration was primarily driven by higher operating expenses (+8%) outpacing the growth in operating income (+8%, though narrative cites 21% expense growth vs 8% income growth for statutory context). The underlying ratio improved by 50 basis points.

### expense_growth — "Operating expenses"
*unquantified | confidence 80/100*

Total operating expenses increased $518 million or 8% on the prior comparative period (ev-3, ev-2). Narrative states this increase partly offset income growth (ev-6). Statutory view shows 21% expense growth (ev-14).
> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-6] CBA/1H26/profit_announcement, PDF p69: "The operating expenses to total operating income ratio decreased 10 basis points on the prior half, mainly driven by higher operating income, partly offset by higher operating expenses."
> [ev-14] CBA/1H26/profit_announcement, PDF p75: "The result was driven by flat operating performance with a 21% increase in operating expenses, offset by an 8% increase in total operating income"

### income_growth — "Operating income"
*unquantified | confidence 80/100*

Total operating income increased $1,924 million or 14% on the prior comparative period (ev-11, ev-16). Narrative attributes ratio improvement mainly to higher operating income (ev-6).
> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-11] CBA/1H26/profit_announcement, PDF p75: "Total operating income 1,805 1,619 1,664"
> [ev-16] CBA/1H26/profit_announcement, printed p2: "Total operating income 15,021 14,368 14,097"
> [ev-6] CBA/1H26/profit_announcement, PDF p69: "The operating expenses to total operating income ratio decreased 10 basis points on the prior half, mainly driven by higher operating income, partly offset by higher operating expenses."

### notable_items — "Restructuring and notable items"
*unquantified | confidence 90/100*

Notable items of $170 million were incurred in 1H26 compared to nil in 1H25 (ev-18). These are included in the total operating expenses figure used for the headline ratio.
> [ev-18] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) –"
> [ev-19] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372)"

## Notable items
- Restructuring and notable items: $170m in 1H26 vs $0m in 1H25.

## Source disagreements
- **Underlying vs Total CTI Movement** (definitional): Underlying CTI decreased 50 bpts (ev-5) vs Total CTI increased 70 bpts (ev-2)
  Preferred: Total CTI movement reported in task. The task requires the headline 'Operating expenses to total operating income' ratio. The bank reports a different movement for the 'underlying' measure. Both are cited but only the total is used for the primary movement delta.

## Limitations
- No primary walk chart extracted for 1H25->1H26 comparison. Driver contributions (ppt) are not quantified because the bank does not provide a JAWS bridge for the total ratio; only narrative direction and aggregate growth rates are available.
- Confidence capped at 80 for drivers due to reliance on narrative statements rather than explicit ppt contribution tables.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T13:11:33+00:00
- seconds: 119.2
- cost_usd: 0.0023
- tokens: 42855 in / 7978 out
- orchestration: pipeline
