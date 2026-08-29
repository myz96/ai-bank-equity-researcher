# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 90/100

*Read from: row 'Loan impairment expense', column FY25 -> column FY26*

CBA's loan impairment expense increased $62 million (9%) to $788 million in FY26 from $726 million in FY25. The annualised loss rate rose to 8 bps of average gross loans and acceptances (GLAA) from 7 bps. The increase was driven by higher collective provisions ($150m), partially offset by a reduction in individually assessed net charges ($17m). Divisionally, Retail Banking Services drove the rise (+$106m), while Business Banking (-$45m) and Institutional Banking (-$16m) provided offsets.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Net collective provision funding | +150 $m | 85 | 1 (single_source) | ev-3, ev-4, ev-14, ev-15 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 85 | 1 (single_source) | ev-3, ev-5, ev-16, ev-17 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -71 $m | 85 | 1 (single_source) | ev-3, ev-6, ev-17 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Net collective provision funding"
*+150 $m | confidence 85/100*

Collective provisions increased $150 million to $606 million (ev-3, ev-4). Corporate collective provisions rose $172 million to $2,797 million due to portfolio growth and macroeconomic uncertainty (ev-14). Consumer collective provisions fell $48 million to $2,888 million as rising house prices offset cost-of-living pressures (ev-15).
> [ev-3] CBA/FY26/profit_announcement, PDF p118: "Total loan impairment expense 788 726 469 319"
> [ev-4] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456 388 218"
> [ev-14] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."
> [ev-15] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts. This was partly offset by higher arrears, rising cost-of-living pressures, increased geopolitical risk, and macroeconomic uncertainty."

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 85/100*

Net new/increased individual provisions decreased $17 million to $422 million (ev-3, ev-5). Corporate individually assessed provisions fell $6 million to $694 million (ev-17). Consumer individually assessed provisions fell $19 million to $97 million (ev-16).
> [ev-3] CBA/FY26/profit_announcement, PDF p118: "Total loan impairment expense 788 726 469 319"
> [ev-5] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439 177 245"
> [ev-16] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million, reflecting rising house prices over the period, partly offset by higher arrears."
> [ev-17] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-71 $m | confidence 85/100*


> [ev-3] CBA/FY26/profit_announcement, PDF p118: "Total loan impairment expense 788 726 469 319"
> [ev-6] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169) (96) (144)"
> [ev-17] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

## Limitations
- The bank does not explicitly split collective provisions into 'volume' vs 'asset quality' drivers in the quantified bridge; the narrative attributes movements to both factors.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T18:04:18+00:00
- seconds: 59.9
- cost_usd: 0.0029
- tokens: 54803 in / 9903 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
