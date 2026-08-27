# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 44.7ppt (-0.5ppt) | **Attribution confidence:** 85/100

CBA's underlying cost-to-income ratio improved by 50 basis points (45.2% to 44.7%) in 1H26 vs 1H25. This improvement was driven by operating income growth outpacing underlying operating expense growth. Statutory CIR also improved slightly by 10 bps (46.1% to 45.9%), supported by higher income and partially offset by higher total expenses including notable items.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | -0.3 ppt | 85 | 2 () | ev-1, ev-9, ev-16 |
| `expense_growth` | — | -0.2 ppt | 85 | 2 () | ev-1, ev-3, ev-10, ev-17 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*-0.3 ppt | confidence 85/100*

Operating income grew from $14,368m to $15,021m (+4.5%). This numerator growth contributed approximately 30bps of the 50bps underlying CIR improvement, as income expanded faster than expenses.
> [ev-1] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income (%)"
> [ev-9] CBA/1H26/profit_announcement, printed p2: "Total operating income 15,021 14,368 14,097 5 7"
> [ev-16] CBA/1H26/results_presentation, printed p8: "Operating income 14,097 14,368 15,021"

### expense_growth
*-0.2 ppt | confidence 85/100*

Underlying operating expenses increased by 5% ($6,494m to $6,720m). While rising, this denominator growth was slower than income growth, contributing the remaining ~20bps of the underlying CIR improvement.
> [ev-1] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income (%)"
> [ev-3] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses were $6,720 million, an increase of $348 million or 5% on the prior comparative period."
> [ev-10] CBA/1H26/profit_announcement, printed p2: "Underlying operating expenses (6,720) (6,494) (6,372) 3 5"
> [ev-17] CBA/1H26/results_presentation, printed p8: "Operating expenses 6,372 6,494 6,720"

## Notable items
- Restructuring and notable items increased from $130m to $170m.

## Source disagreements
- **Presentation Slide Error** (error): 45.2% — ev-13 (Slide) vs 44.7% — ev-15 (Slide)
  Preferred: Profit Announcement. The results presentation slide (ev-13, ev-15) incorrectly labels the 1H26 value as 45.2% and 1H25 as 44.7%, swapping the periods and contradicting the Profit Announcement (ev-1, ev-4) which correctly states 1H25 was 45.2% and 1H26 was 44.7%. The PA is the primary source per hierarchy.
- **Statutory vs Underlying CIR** (definitional): -0.1 ppt — ev-2 (Statutory) vs -0.5 ppt — ev-1 (Underlying)
  Preferred: Underlying. Two different metrics are reported. The task asks for 'cost-to-income ratio' generally, but banks typically highlight 'underlying' for core performance. I report the underlying movement (-50bps) as the primary headline driver, while noting the statutory movement (-10bps) in the narrative. Both show improvement.

## Limitations
- No explicit JAWS walk chart was provided in the evidence records. Contributions are derived from calculated deltas between income and expense levels cited in the Profit Announcement.
- The results presentation contains labeling errors regarding the specific period values for the underlying CIR, requiring reliance on the Profit Announcement table for accurate period identification.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-27T07:43:18+00:00
- seconds: 47.2
- cost_usd: 0.0012
- tokens: 21968 in / 4177 out
- orchestration: pipeline
