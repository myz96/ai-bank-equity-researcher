# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 85/100

*Read from: row 'Loan impairment expense/(benefit)', column Full Year Ended 30 Jun 25 $M -> column Full Year Ended 30 Jun 26 $M*

CBA's loan impairment charge (LIE) rose to $788 million in FY26 from $726 million in FY25, an increase of $62 million (9%). The loan loss rate increased 1 basis point to 8 bps of average gross loans and acceptances. The movement was driven by higher collective provisions (+$150m) reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty, partially offset by lower net individual provisioning (-$17m) and a larger write-back of individually assessed provisions (-$71m). Retail Banking Services contributed the largest divisional increase (+$106m to $378m), while Business Banking (-$45m to $310m) and IB&M (-$16m to $33m) declined.

> [ev-6] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense/(benefit) 788 726"
> [ev-12] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Net collective provision funding | +150 $m | 80 | 1 (single_source) | ev-7, ev-13, ev-14, ev-15, ev-16 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 80 | 1 (single_source) | ev-8, ev-15, ev-16 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -71 $m | 80 | 1 (single_source) | ev-9, ev-15, ev-16 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.volume — "Net collective provision funding"
*+150 $m | confidence 80/100*

Net collective provision funding rose $150 million (456 to 606), driven by portfolio growth across home lending ($41.4b, 8%), business lending ($20.8b, 13%), and consumer finance, plus increased geopolitical risk and macroeconomic uncertainty. In New Zealand, deterioration in the unemployment outlook also pushed collective provisions higher.
> [ev-7] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456"
> [ev-13] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million, primarily driven by increased geopolitical risk, macroeconomic uncertainty, and rising cost-of-living pressures"
> [ev-14] CBA/FY26/profit_announcement, PDF p34: "An increase in New Zealand of $11 million to an expense of $66 million, primarily driven by higher collective provisions reflecting deterioration in the unemployment outlook, and increased geopolitical risk and macroeconomic uncertainty, partly offset by lower individually assessed provisions and lower consumer finance write-offs"
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million, primarily driven by lower individually assessed provision charges, including an increase in write-backs, partly offset by higher collective provisions reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million, primarily driven by release of individually assessed provisions, partly offset by higher collective provisions reflecting increased geopolitical risk, macroeconomic uncertainty, and portfolio growth"

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 80/100*

Net new and increased individual provisioning fell $17 million (439 to 422), broadly flat year-on-year. Business Banking saw lower individually assessed provision charges, and IB&M had a release of individually assessed provisions, partly offsetting the decline.
> [ev-8] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439"
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million, primarily driven by lower individually assessed provision charges, including an increase in write-backs, partly offset by higher collective provisions reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million, primarily driven by release of individually assessed provisions, partly offset by higher collective provisions reflecting increased geopolitical risk, macroeconomic uncertainty, and portfolio growth"

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-71 $m | confidence 80/100*

Write-backs of individually assessed provisions grew from $(169)m to $(240)m, a $71m larger write-back. Business Banking noted an increase in write-backs, and IB&M reported a release of individually assessed provisions, reducing the overall charge.
> [ev-9] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169)"
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million, primarily driven by lower individually assessed provision charges, including an increase in write-backs, partly offset by higher collective provisions reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million, primarily driven by release of individually assessed provisions, partly offset by higher collective provisions reflecting increased geopolitical risk, macroeconomic uncertainty, and portfolio growth"

## Source disagreements
- **New Zealand divisional impairment movement** (timing): +$18m (NZD) vs +$11m (A$M)
  Preferred: +$11m (A$M). Results presentation page 56 reports NZ impairment movement as +$18m (in NZD), while the profit announcement page 34 shows +$11m (in A$M). The A$M figure is the consolidated group-level number and is used in the attribution.

## Limitations
- No walk/bridge chart published by CBA for the FY26 vs FY26 impairment movement; the quantified bridge is built from the provision-type table on page 118 which sums correctly to the total movement.
- The bank does not separately quantify collective provisions into volume-driven vs asset-quality-driven components; the $150m collective increase is attributed to collective.volume as the closest canonical category.
- New Zealand divisional impairment in the results presentation (page 56) states +$18m vs FY25 in NZD, while the profit announcement shows +$11m in A$M — a currency conversion difference; the A$M figure is used throughout.
- Corporate Centre and Other shows a small reversal from $(5)m benefit in FY25 to $1m expense in FY26 (+$6m delta), included in the divisional sum but not separately explained in the provision-type table.
- Capped at 80: collective.volume +150 $m, individual_provisions -17 $m, write_backs_recoveries -71 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T19:54:50+00:00
- seconds: 144.4
- cost_usd: 0.0448
- tokens: 835708 in / 6350 out
- orchestration: agent
- tool_calls: 36
- pages_read: 19
- charts_read: 1
- budget_exhausted: no
