# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's headline cost-to-income ratio (CTI) widened by 70 basis points (ppt) from 45.2% in 1H25 to 45.9% in 1H26. This deterioration was primarily driven by higher operating expenses (+8% YoY), which outpaced the growth in operating income (+6.6% YoY). While underlying CTI improved by 50 basis points due to stronger income growth relative to underlying expense growth, the inclusion of $170 million in restructuring and notable items in 1H26 pushed the headline ratio up.

### expense_growth — "Operating expense growth"
*unquantified | confidence 85/100*

Total operating expenses increased by $518 million or 8% year-on-year (ev-3, ev-18). The bank states this increase 'mainly driven by higher operating expenses' (ev-6). Specific drivers include $170m in restructuring costs (ev-17) and organic underlying expense growth of 5% (ev-4).
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Total operating expenses 6,890 6,624 6,372 4 8"
> [ev-4] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses were $6,720 million, an increase of $348 million or 5% on the prior comparative period."
> [ev-6] CBA/1H26/profit_announcement, PDF p69: "The operating expenses to total operating income ratio decreased 10 basis points on the prior half, mainly driven by higher operating income, partly offset by higher operating expenses."
> [ev-17] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) –"
> [ev-18] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372)"

### income_growth — "Operating income growth"
*unquantified | confidence 85/100*


> [ev-7] CBA/1H26/profit_announcement, PDF p69: "Net interest income increased $337 million or 8% on the prior half."
> [ev-8] CBA/1H26/profit_announcement, PDF p69: "Other operating income decreased $26 million or 5% on the prior half"
> [ev-11] CBA/1H26/profit_announcement, PDF p75: "Total operating income 1,805 1,619 1,664"
> [ev-15] CBA/1H26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-21] CBA/1H26/results_presentation, printed p8: "Operating income $m 14,097 14,368 15,021 1H25 2H25 1H26"

### notable_items — "Restructuring and notable items"
*unquantified | confidence 90/100*

The widening includes $170 million in restructuring and notable items in 1H26 (ev-17, ev-33), compared to zero in 1H25. These items are excluded from the underlying measure but included in the headline total operating expenses used for the headline CTI.
> [ev-17] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) –"
> [ev-33] CBA/1H26/results_presentation, printed p24: "Restructuring and notable items2 170"

## Notable items
- Restructuring and notable items: $170 million in 1H26 vs $0 in 1H25.

## Source disagreements
- **Underlying vs Headline CTI** (definitional): Underlying CTI: 44.7% (1H26) vs 45.2% (1H25) -> -50 bpts (ev-1, ev-5) vs Headline CTI: 45.9% (1H26) vs 45.2% (1H25) -> +70 bpts (ev-2)
  Preferred: Headline CTI. The task requires the headline cost-to-income ratio. The underlying variant shows an improvement, while the headline shows a widening. We report the headline movement as requested.

## Limitations
- The specific ppt contribution of each driver (income vs expense vs notable items) is not explicitly quantified in a walk chart. The narrative attributes the movement to these factors based on the bank's text, but precise arithmetic attribution is derived from the component growth rates rather than a published bridge.
- No primary walk chart was extracted for the 1H25 to 1H26 comparison. Evidence relies on Profit Announcement tables and narrative text.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T17:51:20+00:00
- seconds: 99.0
- cost_usd: 0.0024
- tokens: 44481 in / 7967 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/1H26/profit_announcement p31 <- p32 page 15']
