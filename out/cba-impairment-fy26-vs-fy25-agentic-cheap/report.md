# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 85/100

*Read from: row 'Loan impairment expense/(benefit)', column Full Year Ended 30 Jun 25 $M -> column Full Year Ended 30 Jun 26 $M*

CBA's credit impairment charge (loan impairment expense) rose $62 million or 9% to $788 million in FY26 from $726 million in FY25, driven by a $150 million increase in net collective provision funding that was partially offset by a $71 million larger write-back of individually assessed provisions and a $17 million decrease in net new and increased individual provisioning. The loss rate as a percentage of average gross loans and acceptances increased 1 basis point to 8 basis points. The increase was concentrated in Retail Banking Services (+$106m) and New Zealand (+$11m), partly offset by decreases in Business Banking (-$45m) and Institutional Banking and Markets (-$16m).

> [ev-2] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-3] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."
> [ev-7] CBA/FY26/profit_announcement, PDF p118: "Total loan impairment expense 788 726"
> [ev-18] CBA/FY26/results_presentation, printed p29: "802 726 788"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Net collective provision funding | +150 $m | 80 | 1 (single_source) | ev-4, ev-14, ev-16 |
| `individual_provisions` | Net new and increased individual provisioning | -17 $m | 80 | 1 (single_source) | ev-5 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -71 $m | 80 | 1 (single_source) | ev-6, ev-16 |

### collective.asset_quality — "Net collective provision funding"
*+150 $m | confidence 80/100*

Net collective provision funding rose $150 million to $606 million (FY25: $456 million), reflecting higher collective provisions driven by increased geopolitical risk, macroeconomic uncertainty, and portfolio growth across retail and business banking segments, as stated by the bank.
> [ev-4] CBA/FY26/profit_announcement, PDF p118: "Net collective provision funding 606 456"
> [ev-14] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million, primarily driven by increased geopolitical risk, macroeconomic uncertainty, and rising cost-of-living pressures"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million, primarily driven by lower individually assessed provision charges, including an increase in write-backs, partly offset by higher collective provisions reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty"

### individual_provisions — "Net new and increased individual provisioning"
*-17 $m | confidence 80/100*

Net new and increased individual provisioning decreased $17 million to $422 million (FY25: $439 million), with lower charges in Business Banking partly offset by increases in other segments.
> [ev-5] CBA/FY26/profit_announcement, PDF p118: "Net new and increased individual provisioning 422 439"

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-71 $m | confidence 80/100*

Write-backs of individually assessed provisions increased to ($240) million from ($169) million, a $71 million larger write-back that reduced the overall charge. This was driven by an increase in write-backs in Business Banking, as noted by the bank.
> [ev-6] CBA/FY26/profit_announcement, PDF p118: "Write-back of individually assessed provisions (240) (169)"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million, primarily driven by lower individually assessed provision charges, including an increase in write-backs, partly offset by higher collective provisions reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty"

## Limitations
- No walk/bridge chart with individual bars was found for the FY26 vs FY25 comparison; the results presentation page 29 shows only endpoint values without decomposition bars.
- The provision-type bridge sums exactly to the total movement ($150m - $17m - $71m = $62m), so no residual is needed.
- Divisional drivers are narrative-only (no quantified sub-components per division within each provision type); the bank does not disclose how much of the $150m collective increase came from volume vs asset quality within each division.
- Corporate Centre and Other contributed +$6m (from benefit of $5m to expense of $1m) but is not separately decomposed into provision types.
- Capped at 80: collective.asset_quality +150 $m, individual_provisions -17 $m, write_backs_recoveries -71 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T01:03:32+00:00
- seconds: 105.2
- cost_usd: 0.0085
- tokens: 465530 in / 5632 out
- orchestration: agent
- tool_calls: 28
- pages_read: 9
- charts_read: 1
- budget_exhausted: no
