# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's headline cost-to-income ratio (cash basis) increased by 70 bpts from 45.2% in 1H25 to 45.9% in 1H26. The movement was driven by a negative Jaws effect: operating expenses grew faster than operating income.

### expense_growth — "Operating expense growth"
*unquantified | confidence 80/100*

Total operating expenses increased 8% year-on-year ($6,372m to $6,890m), outpacing the 4.5% growth in total operating income ($14,097m to $15,021m). This positive expense growth contributed to the ratio deterioration.
> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-11] CBA/1H26/profit_announcement, PDF p75: "Total operating income 1,805 1,619 1,664 11 8"
> [ev-16] CBA/1H26/profit_announcement, printed p2: "Group Performance Summary"

### income_growth — "Operating income growth"
*unquantified | confidence 80/100*

Total operating income grew 4.5% year-on-year. While positive, this growth rate was lower than the 8% expense growth, resulting in a net negative impact on the cost-to-income ratio.
> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-11] CBA/1H26/profit_announcement, PDF p75: "Total operating income 1,805 1,619 1,664 11 8"
> [ev-16] CBA/1H26/profit_announcement, printed p2: "Group Performance Summary"

### notable_items — "Restructuring and notable items"
*unquantified | confidence 90/100*

Notable items of $170m were recorded in 1H26 compared to nil in 1H25. These are included in the headline total operating expenses figure used for the ratio calculation.
> [ev-2] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-18] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items (170) (130) – 31 n/a"
> [ev-19] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372) 4 8"

## Notable items
- Restructuring and notable items of $170m in 1H26 vs $0m in 1H25.

## Source disagreements
- **Underlying vs Headline Ratio** (definitional): 44.7% (Underlying, ev-1) vs 45.9% (Headline, ev-2)
  Preferred: 45.9%. The task requires the headline measure. The underlying ratio (44.7%) excludes notable items and uses an underlying income base, representing a different metric.

## Limitations
- No primary walk chart extracted for the 1H25-1H26 comparison. Driver contributions are inferred from disclosed growth rates rather than a quantified additive decomposition.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T03:33:15+00:00
- seconds: 61.5
- cost_usd: 0.0022
- tokens: 42134 in / 7492 out
- orchestration: pipeline
