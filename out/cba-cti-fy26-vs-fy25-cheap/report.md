# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio (cash basis) improved by 20 basis points from 45.7% in FY25 to 45.5% in FY26. This improvement was driven by operating income growth of 6.2% outpacing underlying operating expense growth of 5.6%. The bank also reported an underlying cost-to-income ratio of 44.9%, a 30 basis point improvement from 45.2%.

> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-18] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-1] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income (%) 44.9 45.2 (30)bpts 45.2 44.7 50 bpts"
> [ev-5] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income ratio decreased 30 basis points from 45.2% to 44.9%."
> [ev-23] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-24] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | -0.1 ppt | 80 | 2 () | ev-23, ev-8 |
| `expense_growth` | — | +0.1 ppt | 80 | 2 () | ev-24, ev-9 |
| *residual (unexplained)* | — | -0.2 ppt | — | — |

### income_growth
*-0.1 ppt | confidence 80/100*

Income grew 6.2% ($28,465m to $30,224m), outpacing expense growth and lowering the ratio.
> [ev-23] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-8] CBA/FY26/profit_announcement, printed p2: "Total operating income"

### expense_growth
*+0.1 ppt | confidence 80/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m), partially offsetting income gains.
> [ev-24] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-9] CBA/FY26/profit_announcement, printed p2: "Underlying operating expenses"

## Source disagreements
- **Basis of Headline Ratio** (definitional): 45.5% (Cash) vs 45.2% (Underlying)
  Preferred: 45.5% (Cash). The bank reports both cash and underlying ratios. Cash is the primary statutory measure.

## Limitations
- No walk chart provided for driver attribution; contributions are estimated based on jaws arithmetic.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T16:28:42+00:00
- seconds: 39.8
- cost_usd: 0.0018
- tokens: 36498 in / 5575 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
