# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 60/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio (cash basis) improved by 20 basis points to 45.5% in FY26 from 45.7% in FY25. This improvement was driven by operating income growth of 6.2% outpacing underlying operating expense growth of 5.6%, resulting in a net positive jaws effect.

> [ev-2] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"
> [ev-12] CBA/FY26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | -0.1 ppt | 60 | 2 () | ev-12, ev-29 |
| `expense_growth` | — | -0.1 ppt | 60 | 1 (single_source) | ev-30, ev-37 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*-0.1 ppt | confidence 60/100*


> [ev-12] CBA/FY26/profit_announcement, printed p2: "Group Performance Summary"
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"

### expense_growth
*-0.1 ppt | confidence 60/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m). Slower expense growth relative to income supported the ratio improvement.
> [ev-30] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-37] CBA/FY26/results_presentation, printed p24: "Underlying operating expenses 13,585 5.6% 2.2%"

## Source disagreements
- **Underlying vs Total CTI** (definitional): 44.9% (Underlying), ev-1 vs 45.5% (Total/Cash), ev-2
  Preferred: 45.5% (Total/Cash). The task requires the headline measure 'Operating expenses to total operating income'. The bank reports this as 45.5% on a cash/total basis. The underlying ratio (44.9%) is a different measure excluding notable items.

## Limitations
- No walk chart provided for FY25->FY26 CTI decomposition. Contributions are inferred from aggregate income and expense growth rates rather than a published driver bridge.
- Confidence is capped at 60 due to lack of explicit bank-stated driver attribution for the specific ppt split.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T18:55:43+00:00
- seconds: 46.2
- cost_usd: 0.0021
- tokens: 37429 in / 7553 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
