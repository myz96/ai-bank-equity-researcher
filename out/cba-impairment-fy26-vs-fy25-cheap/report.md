# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 80/100

*Read from: row 'Total loan impairment expense', column FY25 (12 months ended Jun 2025) -> column FY26 (12 months ended Jun 2026)*

CBA's credit impairment charge increased $62 million to $788 million in FY26, driven by higher Retail Banking Services expenses ($378m vs $272m) and New Zealand ($66m vs $55m), partially offset by Business Banking ($310m vs $355m) and Institutional Banking ($33m vs $49m). The loss rate rose 1 basis point to 8 bps on average GLAA.

> [ev-17] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-22] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "An increase in New Zealand of $11 million to an expense of $66 million"
> [ev-20] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-21] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Net collective provision funding | +150 $m | 80 | 1 (single_source) | ev-6, ev-13, ev-14 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 80 | 1 (single_source) | ev-7, ev-15, ev-16 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -71 $m | 80 | 1 (single_source) | ev-8 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.volume — "Net collective provision funding"
*+150 $m | confidence 80/100*

Collective provisions increased $150 million ($606m vs $456m) due to portfolio growth. Corporate collective provisions rose $172 million to $2,797 million, while Consumer collective provisions decreased $48 million to $2,888 million.
> [ev-6] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456 388 218"
> [ev-13] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million"
> [ev-14] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million"

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 80/100*

New and increased individual provisions decreased $17 million ($422m vs $439m). Consumer individually assessed provisions fell $19 million to $97 million, and Corporate individually assessed provisions decreased $6 million to $694 million.
> [ev-7] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439 177 245"
> [ev-15] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million"
> [ev-16] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million"

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-71 $m | confidence 80/100*

Larger write-backs reduced the net charge by $71 million. Write-backs were $240 million in FY26 compared to $169 million in FY25, reflecting improved outcomes on specific names.
> [ev-8] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169) (96) (144)"

## Limitations
- The bank does not explicitly map the divisional P&L movements to the specific provision types (collective vs individual) in the text; the bridge is constructed from the aggregate provision type tables which sum to the total movement.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T12:37:05+00:00
- seconds: 55.6
- cost_usd: 0.0024
- tokens: 44021 in / 8568 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
