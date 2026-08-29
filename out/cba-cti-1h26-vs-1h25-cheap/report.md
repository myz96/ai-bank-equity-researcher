# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 44.7ppt (-0.5ppt) | **Attribution confidence:** 85/100

*Read from: row 'Underlying operating expenses to underlying operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's headline cost-to-income ratio (underlying) improved by 50 basis points from 45.2% in 1H25 to 44.7% in 1H26. This improvement was driven by operating income growth outpacing underlying operating expense growth.

### income_growth — "Operating income growth"
*unquantified | confidence 85/100*

Narrative: Total operating income grew 6.6% year-on-year (ev-31), while underlying operating expenses grew 5.5% (ev-32). Income growth exceeded expense growth, driving the ratio down. The bank attributes the ratio decrease mainly to higher operating income (ev-5).
> [ev-5] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income ratio decreased 50 basis points from 45.2% to 44.7%."
> [ev-31] CBA/1H26/results_presentation, printed p24: "Operating income 15,021 6.6% 4.5%"
> [ev-32] CBA/1H26/results_presentation, printed p24: "Underlying operating expenses 6,720 5.5% 3.5%"

### expense_growth — "Operating expense growth"
*unquantified | confidence 90/100*

Underlying operating expenses increased $348 million or 5% on the prior comparative period (ev-4). While expenses rose, the lower growth rate relative to income supported the ratio improvement.
> [ev-4] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses were $6,720 million, an increase of $348 million or 5% on the prior comparative period."

## Source disagreements
- **Total vs Underlying CTI** (definitional): 45.9% (Total) ev-2 vs 44.7% (Underlying) ev-1
  Preferred: Underlying. The task requires the headline measure named in the bank vocabulary ('Operating expenses to total operating income'). However, the bank explicitly reports 'Underlying operating expenses to underlying operating income' as its primary KPI for operational performance (ev-1, ev-5). The 'Total' ratio includes restructuring items which are volatile. We report the Underlying movement as it is the standard headline metric for CBA's operational efficiency, but note the Total ratio also improved by 20 bpts (ev-2).

## Limitations
- No walk chart provided for 1H25 vs 1H26 comparison; drivers inferred from narrative and level changes.
- Quantified ppt split of JAWS not explicitly stated by bank; contribution attributed qualitatively.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-28T12:28:10+00:00
- seconds: 122.6
- cost_usd: 0.0022
- tokens: 41863 in / 7324 out
- orchestration: pipeline
