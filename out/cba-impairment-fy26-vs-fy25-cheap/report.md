# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 90/100

*Read from: row 'Total loan impairment expense', column FY25 (12 months ended Jun 2025) -> column FY26 (12 months ended Jun 2026)*

CBA's credit impairment charge increased $62 million to $788 million in FY26 (vs $726 million in FY25), a 9% rise. The loss rate against average gross loans and acceptances (GLAA) rose 1 basis point to 8 bps. The increase was driven by higher collective provisions ($150m), partially offset by improved individual write-backs ($71m). Retail Banking Services drove the bulk of the expense growth (+$106m), while Business Banking and Institutional Banking & Markets saw declines.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Net collective provision funding | +150 $m | 85 | 1 (single_source) | ev-6, ev-10, ev-11 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 85 | 1 (single_source) | ev-7, ev-12, ev-13 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -71 $m | 85 | 1 (single_source) | ev-8 |
| `other_unmapped` | Divisional Residual | +0 $m | 80 | 1 (single_source) | ev-17, ev-18, ev-19, ev-20, ev-21 |

### collective.volume — "Net collective provision funding"
*+150 $m | confidence 85/100*

Collective provisions rose $150 million to $606 million. Corporate collective provisions increased $172 million to $2,797 million, reflecting portfolio growth and macroeconomic uncertainty. Consumer collective provisions decreased $48 million to $2,888 million due to rising house prices and targeted forward-looking adjustments.
> [ev-6] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456 388 218"
> [ev-10] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."
> [ev-11] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts. This was partly offset by higher arrears, rising cost-of-living pressures, increased geopolitical risk, and macroeconomic uncertainty."

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 85/100*

New and increased individual provisions fell $17 million to $422 million. Corporate individually assessed provisions decreased $6 million to $694 million, driven by write-backs and write-offs. Consumer individually assessed provisions decreased $19 million to $97 million, supported by rising house prices.
> [ev-7] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439 177 245"
> [ev-12] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million, reflecting rising house prices over the period, partly offset by higher arrears."
> [ev-13] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-71 $m | confidence 85/100*

Write-backs of individually assessed provisions increased (reducing the net charge) by $71 million to $240 million (vs $169 million in FY25). This improvement partially offset the rise in collective and new individual provisions.
> [ev-8] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169) (96) (144)"

### other_unmapped — "Divisional Residual"
*+0 $m | confidence 80/100*

The sum of quantified provision drivers (Collective +150, Individual New -17, Write-backs -71) equals the total movement of $62 million. No residual is required. Divisional movements: Retail +$106m, Business -$45m, IB&M -$16m, NZ +$11m, Corp Centre +$6m.
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "Retail Banking Services 378 272 39"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Business Banking 310 355 (13)"
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "Institutional Banking and Markets 33 49 (33)"
> [ev-20] CBA/FY26/profit_announcement, PDF p34: "New Zealand 66 55 20"
> [ev-21] CBA/FY26/profit_announcement, PDF p34: "Corporate Centre and Other 1 (5) large"

## Source disagreements
- **Loss Rate Denominator/Labeling** (definitional): 8 bps (Profit Announcement ev-1, ev-16) vs 9 bpts (Results Presentation ev-23, ev-29)
  Preferred: 8 bps. The Profit Announcement (primary source) explicitly states the Loan Impairment Expense as a percentage of average GLAA is 8 bps (ev-1, ev-16). The Results Presentation slide (ev-23) labels a table 'Full Year Loan Impairment Expense as a percentage of average GLAA' but lists 9 bps for FY26. Given the source hierarchy, the PA narrative/table is preferred. The discrepancy may stem from different averaging periods or rounding conventions not fully explained.

## Limitations
- The bridge relies on the explicit provision type splits provided in Note 2.2. Divisional movements are reported but not broken down into provision types in the evidence, so the divisional attribution is based on the aggregate P&L line items rather than a detailed provision-type bridge per division.
- The 'Other changes' in NPE rollforward (ev-40) are not mapped to specific impairment drivers.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T20:56:40+00:00
- seconds: 66.9
- cost_usd: 0.0025
- tokens: 44053 in / 9095 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
