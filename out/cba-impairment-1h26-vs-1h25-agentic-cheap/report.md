# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Loan impairment expense/(benefit)', column 31 Dec 24 $M -> column 31 Dec 25 $M*

CBA's loan impairment expense (LIE) was $319 million in 1H26, a decrease of $1 million from $320 million in 1H25. The annualised loss rate fell 1 bps to 6 bps on average gross loans and acceptances. The movement was driven by a $76 million increase in net individual provisioning (from $169m to $245m), partially offset by a $74 million increase in write-backs (from $70m to $144m) and a $3 million decrease in net collective provision funding (from $221m to $218m). Divisionally, Retail Banking Services drove the increase (+$153m to $232m) while Business Banking (-$129m to $91m), IB&M (-$17m to a benefit of $8m), and New Zealand (-$12m to $4m) all decreased.

> [ev-1] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense/(benefit) 319 406 320 (21) -"
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Net collective provision funding | -3 $m | 80 | 2 () | ev-10, ev-14, ev-17 |
| `individual_provisions` | Net new and increased individual provisioning | +76 $m | 80 | 2 () | ev-11, ev-15 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -74 $m | 80 | 2 () | ev-12, ev-14, ev-16 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Net collective provision funding"
*-3 $m | confidence 80/100*

Net collective provision funding decreased $3 million to $218 million (from $221 million in 1H25). The bank states this reflects elevated geopolitical tensions and global macroeconomic uncertainty driving higher collective provisions, partly offset by improvements in underlying credit quality including lower arrears and lower corporate TNPE.
> [ev-10] CBA/1H26/profit_announcement, PDF p109: "Net collective provision funding 218 235 221"
> [ev-14] CBA/1H26/results_presentation, printed p70: "LIE Lower collective and specific provision charges due to improvements in underlying credit quality and an increase in write backs."
> [ev-17] CBA/1H26/results_presentation, printed p70: "LIE Higher collective provisions due to elevated geopolitical tensions and macroeconomic uncertainty."

### individual_provisions — "Net new and increased individual provisioning"
*+76 $m | confidence 80/100*

Net new and increased individual provisioning rose $76 million to $245 million (from $169 million in 1H25). The bank attributes this to release of individually assessed provisions in IB&M (partly offset by higher collective provisions reflecting elevated global macroeconomic uncertainty) and lower collective and individually assessed provision charges in Business Banking due to improvements in credit quality.
> [ev-11] CBA/1H26/profit_announcement, PDF p109: "Net new and increased individual provisioning 245 270 169"
> [ev-15] CBA/1H26/results_presentation, printed p70: "LIE Release of individually assessed provisions, partly offset by higher collective provisions reflecting elevated global macroeconomic uncertainty."

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-74 $m | confidence 80/100*

Write-backs of individually assessed provisions increased to $144 million (from $70 million in 1H25), a $74 million swing that reduced the overall charge. The bank cites an increase in write-backs as a driver of the Business Banking decrease ($129m to $91m) and notes lower consumer finance write-offs and lower home lending provisions in New Zealand reflecting improved credit quality.
> [ev-12] CBA/1H26/profit_announcement, PDF p109: "Write-back of individually assessed provisions (144) (99) (70)"
> [ev-14] CBA/1H26/results_presentation, printed p70: "LIE Lower collective and specific provision charges due to improvements in underlying credit quality and an increase in write backs."
> [ev-16] CBA/1H26/results_presentation, printed p70: "LIE Lower write-offs and lower home lending provisions reflecting improved credit quality, partly offset by lower forecast house price growth."

## Limitations
- No walk/bridge chart of the dollar-level impairment movement was found in either document; the provision-type split is from a table on p109 of the profit announcement, not a chart. The delta is computed by subtraction of two period levels rather than read from a primary walk chart whose sum check passed.
- The results presentation page 29 contains a chart labeled 'Loan impairment expense' but its bars do not reconcile to the task comparison endpoints.
- Divisional commentary provides qualitative reasons but no sub-component numbers for each division's provision-type breakdown.
- Capped at 80: collective.asset_quality -3 $m, individual_provisions +76 $m, write_backs_recoveries -74 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: walk_sum (start 7 + bars -12.0 = -5.0 != end 6, tol 1.0 $m) [CBA/1H26/results_presentation PDF p68 (ev-19)]
- Failed check: walk_sum (start 320 + bars +86.0 = 406.0 != end 319, tol 1.0 $m) [CBA/1H26/results_presentation PDF p29 (ev-20)]

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T23:59:08+00:00
- seconds: 156.1
- cost_usd: 0.0176
- tokens: 623500 in / 6943 out
- orchestration: agent
- tool_calls: 32
- pages_read: 14
- charts_read: 2
- budget_exhausted: no
