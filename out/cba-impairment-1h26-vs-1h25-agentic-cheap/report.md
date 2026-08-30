# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 88/100

*Read from: row 'Loan impairment expense/(benefit)', column Half Year Ended 31 Dec 24 -> column Half Year Ended 31 Dec 25*

CBA's loan impairment expense (LIE) was essentially flat at $319 million in 1H26 versus $320 million in 1H25, a decrease of $1 million (0.3%). The annualised loss rate on average gross loans and acceptances fell 1 basis point to 6 bps. The near-flat result masks large offsetting movements: higher collective provision funding (+$3m net) and significantly larger individually assessed provision charges (+$76m) were more than offset by a much larger write-back of individually assessed provisions (+$74m benefit). Divisionally, Retail Banking Services saw its charge surge $153m to $232m driven by elevated geopolitical tensions and global macroeconomic uncertainty, while Business Banking fell $129m to $91m on improved credit quality and higher write-backs, IB&M swung $17m to a $8m benefit from release of individually assessed provisions, and New Zealand declined $12m to $4m on lower write-offs and improved home lending quality.

> [ev-1] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense/(benefit) 319 406 320"
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-12] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."
> [ev-18] CBA/1H26/results_presentation, printed p24: "Loan impairment expense 319 (0.3%) (21.4%)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Net collective provision funding | -3 $m | 80 | 1 (single_source) | ev-14, ev-11, ev-8 |
| `individual_provisions` | Net new and increased individual provisioning | +76 $m | 80 | 1 (single_source) | ev-15, ev-8, ev-9 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -74 $m | 80 | 1 (single_source) | ev-16, ev-8 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.volume — "Net collective provision funding"
*-3 $m | confidence 80/100*

Net collective provision funding decreased $3 million to $218 million from $221 million in 1H25. The bank attributes this broadly stable level to elevated geopolitical tensions and global macroeconomic uncertainty being partly offset by improvements in credit quality across portfolios.
> [ev-14] CBA/1H26/profit_announcement, PDF p109: "Net collective provision funding 218 235 221"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million, reflecting higher collective provisions due to elevated geopolitical tensions and global macroeconomic uncertainty"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million, primarily driven by lower collective and individually assessed provision charges due to improvements in credit quality and an increase in write backs"

### individual_provisions — "Net new and increased individual provisioning"
*+76 $m | confidence 80/100*

Net new and increased individual provisioning rose $76 million to $245 million from $169 million in 1H25. Higher charges reflect elevated geopolitical tensions and global macroeconomic uncertainty, particularly in Business Banking where individually assessed provision charges fell due to improvements in credit quality (the prior period had higher charges). In IB&M, the release of individually assessed provisions drove a $17 million swing to a benefit of $8 million.
> [ev-15] CBA/1H26/profit_announcement, PDF p109: "Net new and increased individual provisioning 245 270 169"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million, primarily driven by lower collective and individually assessed provision charges due to improvements in credit quality and an increase in write backs"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million, primarily driven by the release of individually assessed provisions, partly offset by higher collective provisions reflecting elevated geopolitical tensions and global macroeconomic uncertainty"

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-74 $m | confidence 80/100*

Write-back of individually assessed provisions increased to ($144) million from ($70) million in 1H25, a $74 million larger write-back that reduced the overall charge. This contributed to the $129 million decrease in Business Banking expense to $91 million, as the bank notes 'an increase in write backs' alongside lower collective and individually assessed provision charges due to improvements in credit quality.
> [ev-16] CBA/1H26/profit_announcement, PDF p109: "Write-back of individually assessed provisions (144) (99) (70)"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million, primarily driven by lower collective and individually assessed provision charges due to improvements in credit quality and an increase in write backs"

## Notable items
- Retail Banking Services charge surged $153m to $232m (from $79m), reflecting higher collective provisions due to elevated geopolitical tensions and global macroeconomic uncertainty
- Business Banking charge fell $129m to $91m (from $220m), driven by lower collective and individually assessed provision charges and an increase in write-backs
- IB&M swung $17m to a benefit of $8m (from $9m expense), primarily from release of individually assessed provisions
- New Zealand charge declined $12m to $4m (from $16m), driven by lower consumer finance write-offs and lower home lending provisions
- Corporate Centre and Other moved from ($4)m to $0

## Limitations
- The provision-type bridge (collective + individual + write-backs) sums exactly to the $1m movement, confirming completeness of the canonical decomposition
- No walk chart was found in either document for the 1H25-to-1H26 comparison; the provision-type table on page 109 serves as the primary decomposition
- The bank does not separately quantify the split between collective volume-driven and asset-quality-driven components within the net collective provision line
- Divisional detail confirms the aggregate movement but the provision-type breakdown is at group level only, not by division
- Capped at 80: collective.volume -3 $m, individual_provisions +76 $m, write_backs_recoveries -74 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T19:29:51+00:00
- seconds: 47.9
- cost_usd: 0.0042
- tokens: 261059 in / 5049 out
- orchestration: agent
- tool_calls: 18
- pages_read: 9
- charts_read: 0
- budget_exhausted: no
