# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 85/100

*Read from: row 'Loan impairment expense/(benefit) total row', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's loan impairment expense was $319 million in 1H26, down $1 million (flat) from $320 million in 1H25. The annualised loss rate as a percentage of average gross loans and acceptances decreased 1 basis point to 6 bps. The near-flat movement masked offsetting forces: higher individually assessed provisioning (+$76m) and larger write-backs ($74m more), largely cancelling each other, while collective provision funding was broadly stable ($3m lower). Divisionally, Retail Banking Services surged +$153m to $232m, driven by higher collective provisions for geopolitical and macro uncertainty; this was offset by Business Banking (-$129m to $91m), IB&M (-$17m to a $8m benefit), and New Zealand (-$12m to $4m), all reflecting improved credit quality and/or larger write-backs.

> [ev-1] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense/(benefit) 319 406 320"
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."
> [ev-12] CBA/1H26/results_presentation, printed p24: "Loan impairment expense 319 (0.3%) (21.4%)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Net collective provision funding | -3 $m | 80 | 2 () | ev-9, ev-18, ev-19, ev-21 |
| `individual_provisions` | Net new and increased individual provisioning | +76 $m | 80 | 2 () | ev-9, ev-18, ev-20 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -74 $m | 80 | 2 () | ev-9, ev-7, ev-19, ev-20, ev-21 |

### collective.volume — "Net collective provision funding"
*-3 $m | confidence 80/100*

Net collective provision funding was $218 million in 1H26 versus $221 million in 1H25, a decrease of $3 million. The bank attributes higher collective provisions across divisions to 'elevated geopolitical tensions and global macroeconomic uncertainty' (ev-18, ev-19, ev-21). In Retail Banking Services, collective provisions rose sharply (+$153m to $232m) due to these headwinds (ev-18). In Business Banking, collective provisions fell as credit quality improved (ev-19). The net effect across portfolios was roughly flat.
> [ev-9] CBA/1H26/profit_announcement, PDF p109: "Loan impairment expense Net collective provision funding 218 235 221 Net new and increased individual provisioning 245 270 169 Write-back of individually assessed provisions (144) (99) (70) Total loan impairment expense 319 406 320"
> [ev-18] CBA/1H26/results_presentation, printed p70: "LIE Higher collective provisions due to elevated geopolitical tensions and macroeconomic uncertainty."
> [ev-19] CBA/1H26/results_presentation, printed p70: "LIE Release of individually assessed provisions, partly offset by higher collective provisions reflecting elevated global macroeconomic uncertainty."
> [ev-21] CBA/1H26/results_presentation, printed p70: "LIE Lower write-offs and lower home lending provisions reflecting improved credit quality, partly offset by lower forecast house price growth."

### individual_provisions — "Net new and increased individual provisioning"
*+76 $m | confidence 80/100*

Net new and increased individual provisioning was $245 million in 1H26 versus $169 million in 1H25, an increase of $76 million. This reflected higher individually assessed provision charges, particularly in Retail Banking Services where the overall impairment surge to $232m included elevated specific provisions (ev-18). In IB&M, the release of individually assessed provisions drove a $17m improvement to a benefit of $8m (ev-19, ev-20).
> [ev-9] CBA/1H26/profit_announcement, PDF p109: "Loan impairment expense Net collective provision funding 218 235 221 Net new and increased individual provisioning 245 270 169 Write-back of individually assessed provisions (144) (99) (70) Total loan impairment expense 319 406 320"
> [ev-18] CBA/1H26/results_presentation, printed p70: "LIE Higher collective provisions due to elevated geopolitical tensions and macroeconomic uncertainty."
> [ev-20] CBA/1H26/results_presentation, printed p70: "LIE Lower collective and specific provision charges due to improvements in underlying credit quality and an increase in write backs."

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-74 $m | confidence 80/100*

Write-backs of individually assessed provisions were $144 million in 1H26 versus $70 million in 1H25, an increase in write-backs of $74 million (reducing the net charge). The bank notes 'an increase in write backs' as a driver of the Business Banking improvement (ev-7, ev-19), and 'release of individually assessed provisions' in IB&M (ev-19, ev-20). In New Zealand, lower individual provisions in the business portfolio contributed to the $12m decline (ev-21).
> [ev-9] CBA/1H26/profit_announcement, PDF p109: "Loan impairment expense Net collective provision funding 218 235 221 Net new and increased individual provisioning 245 270 169 Write-back of individually assessed provisions (144) (99) (70) Total loan impairment expense 319 406 320"
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-19] CBA/1H26/results_presentation, printed p70: "LIE Release of individually assessed provisions, partly offset by higher collective provisions reflecting elevated global macroeconomic uncertainty."
> [ev-20] CBA/1H26/results_presentation, printed p70: "LIE Lower collective and specific provision charges due to improvements in underlying credit quality and an increase in write backs."
> [ev-21] CBA/1H26/results_presentation, printed p70: "LIE Lower write-offs and lower home lending provisions reflecting improved credit quality, partly offset by lower forecast house price growth."

## Limitations
- No walk/bridge chart published for the 1H25-to-1H26 comparison; the provision-type bridge is derived from the table on p.109 of the profit announcement, with deltas computed by subtracting period columns (capped at 80 confidence per rules).
- The bank does not separately disclose collective provisions split into volume vs asset-quality drivers; the narrative references 'elevated geopolitical tensions and global macroeconomic uncertainty' as the stated reason but does not quantify the sub-components.
- Corporate Centre and Other moved from a ($4)m benefit in 1H25 to break-even in 1H26 (+$4m); this small remainder is absorbed within the provision-type drivers rather than attributed separately.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T13:50:22+00:00
- seconds: 128.0
- cost_usd: 0.0204
- tokens: 703512 in / 7589 out
- orchestration: agent
- tool_calls: 35
- pages_read: 14
- charts_read: 0
- budget_exhausted: no
