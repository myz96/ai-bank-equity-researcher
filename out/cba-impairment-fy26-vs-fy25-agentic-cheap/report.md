# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 90/100

*Read from: row 'Loan impairment expense/(benefit)', column 30 Jun 25 $M -> column 30 Jun 26 $M*

CBA's loan impairment charge rose $62 million (9%) to $788 million in FY26 from $726 million in FY25, driven by a $150 million increase in net collective provision funding that reflected portfolio growth, cost-of-living pressures, and heightened geopolitical risk and macroeconomic uncertainty. This was partially offset by a $71 million acceleration in individually assessed write-backs and a modest $17 million reduction in net new individual provisioning. The loan loss rate increased 1 basis point to 8 bps on average gross loans and acceptances.

> [ev-1] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense/(benefit) 788 726 9 469 319 47"
> [ev-22] CBA/FY26/profit_announcement, PDF p9: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Net collective provision funding | +150 $m | 80 | 1 (single_source) | ev-7, ev-22 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 80 | 1 (single_source) | ev-8 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -71 $m | 80 | 1 (single_source) | ev-9 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.volume — "Net collective provision funding"
*+150 $m | confidence 80/100*

Net collective provision funding rose $150 million to $606 million (FY25: $456 million), driven by portfolio growth across home lending and commercial books, cost-of-living pressures lifting consumer arrears (home loan 90+ days to 0.73%, personal loans to 1.72%), and increased geopolitical risk and macroeconomic uncertainty. In New Zealand, deterioration in the unemployment outlook also lifted collective provisions. The bank states impairment expense was 'higher reflecting portfolio growth and increased global macroeconomic uncertainty.'
> [ev-7] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456 388 218"
> [ev-22] CBA/FY26/profit_announcement, PDF p9: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 80/100*

Net new and increased individual provisioning fell $17 million to $422 million (FY25: $439 million). In Business Banking, lower individually assessed provision charges included an increase in write-backs. In IB&M, the release of individually assessed provisions drove the decrease. These reductions were partly offset by higher individual provisions in New Zealand.
> [ev-8] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439 177 245"

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-71 $m | confidence 80/100*

Write-backs of individually assessed provisions increased to $240 million (FY25: $169 million), a $71 million swing that reduced the overall charge. The bank notes that in Business Banking, lower individually assessed provision charges included 'an increase in write-backs,' and in IB&M, the 'release of individually assessed provisions' contributed to the divisional decrease.
> [ev-9] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169) (96) (144)"

## Limitations
- No walk/bridge chart found in the results presentation for the FY26 vs FY25 comparison; the provision-type split table on page 118 is used as the primary decomposition instead.
- The provision-type rows do not separately decompose collective provisions into volume vs asset-quality sub-drivers; the narrative attributes the collective increase to both portfolio growth and risk migration factors but no printed numbers split these sub-components.
- Corporate Centre and Other shows a $6 million movement from a ($5)m benefit to $1m expense; this small item is included in the divisional sum but has no separate driver narrative.
- Capped at 80: collective.volume +150 $m, individual_provisions -17 $m, write_backs_recoveries -71 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T15:15:12+00:00
- seconds: 112.2
- cost_usd: 0.0115
- tokens: 566412 in / 4972 out
- orchestration: agent
- tool_calls: 30
- pages_read: 14
- charts_read: 0
- budget_exhausted: no
