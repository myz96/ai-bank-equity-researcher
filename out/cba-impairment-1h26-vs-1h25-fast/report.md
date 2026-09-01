# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 85/100

*Read from: row 'Loan impairment expense/(benefit)', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's loan impairment expense (LIE) fell $1m from $320m in 1H25 to $319m in 1H26 (continuing operations basis). The annualised loss rate (LIE as % of average gross loans and acceptances) decreased 1 basis point to 6 basis points. The provision-type bridge: net collective provision funding -$3m, net new and increased individual provisioning +$76m, write-back of individually assessed provisions -$74m (sums to -$1m). Where it arose: Retail Banking Services +$153m (79 to 232), Business Banking -$129m (220 to 91), Institutional Banking and Markets -$17m (9 to -8), New Zealand -$12m (16 to 4), Corporate Centre +$4m (-4 to 0).

> [ev-1] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense/(benefit) 319 406 320 (21) -"
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-12] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."
> [ev-17] CBA/1H26/results_presentation, printed p29: "$m 320 406 319 1H25 2H25 1H26"
> [ev-22] CBA/1H26/results_presentation, printed p29: "Total 7 8 6"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective` | Net collective provision funding | -3 $m | 80 | 1 (single_source) | ev-13, ev-2, ev-3, ev-11, ev-8 |
| `individual_provisions` | Net new and increased individual provisioning | +76 $m | 80 | 1 (single_source) | ev-14, ev-4, ev-9 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -74 $m | 80 | 1 (single_source) | ev-15, ev-5, ev-10 |
| *residual (unexplained)* | — | +0 $m | — | — | — |

### collective — "Net collective provision funding"
*-3 $m | confidence 80/100*

Net collective provision funding fell $3m from $221m (1H25) to $218m (1H26). Where it arose: Retail Banking Services rose $153m from $79m to $232m, reflecting higher collective provisions due to elevated geopolitical tensions and global macroeconomic uncertainty; Business Banking fell $129m from $220m to $91m, partly lower collective provision charges due to improvements in credit quality; IB&M higher collective provisions partly offset the release of individually assessed provisions; New Zealand lower home lending provisions.
> [ev-13] CBA/1H26/profit_announcement, PDF p109: "Net collective provision funding 218 235 221"
> [ev-2] CBA/1H26/profit_announcement, printed p18: "Retail Banking Services 232 193 79 20 large"
> [ev-3] CBA/1H26/profit_announcement, printed p18: "Business Banking 91 135 220 (33) (59)"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million, reflecting higher collective provisions due to elevated geopolitical tensions and global macroeconomic uncertainty."
> [ev-8] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million, primarily driven by lower collective and individually assessed provision charges due to improvements in credit quality and an increase in write backs;"

### individual_provisions — "Net new and increased individual provisioning"
*+76 $m | confidence 80/100*

Net new and increased individual provisioning rose $76m from $169m (1H25) to $245m (1H26). Where it arose: Business Banking lower individually assessed provision charges; Institutional Banking and Markets fell $17m from an expense of $9m to a benefit of $8m, primarily driven by the release of individually assessed provisions, partly offset by higher collective provisions.
> [ev-14] CBA/1H26/profit_announcement, PDF p109: "Net new and increased individual provisioning 245 270 169"
> [ev-4] CBA/1H26/profit_announcement, printed p18: "Institutional Banking and Markets (8) 40 9 (large) (large)"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million, primarily driven by the release of individually assessed provisions, partly offset by higher collective provisions reflecting elevated geopolitical tensions and global macroeconomic uncertainty;"

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-74 $m | confidence 80/100*

Write-back of individually assessed provisions rose $74m from $70m (1H25) to $144m (1H26). Where it arose: Business Banking increase in write-backs; New Zealand fell $12m from $16m to $4m, primarily driven by lower consumer finance write-offs and lower home lending provisions reflecting improved credit quality.
> [ev-15] CBA/1H26/profit_announcement, PDF p109: "Write-back of individually assessed provisions (144) (99) (70)"
> [ev-5] CBA/1H26/profit_announcement, printed p18: "New Zealand 4 39 16 (90) (75)"
> [ev-10] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million, primarily driven by lower consumer finance write-offs and lower home lending provisions reflecting improved credit quality, partly offset by lower forecast house price growth;"

## Notable items
- Corporate Centre and Other division moved +$4m (from -$4m to 0) with no bank narrative

## Source disagreements
- **New Zealand impairment expense decrease** (definitional): results book: $12m decrease (AUD) vs presentation: ($14m) decrease (NZD)
  Preferred: results book $12m (AUD). The results book reports NZ impairment expense in AUD ($12m decrease), while the presentation reports it in NZD ($14m decrease); the difference reflects currency translation.

## Limitations
- The bank provides no narrative for the Corporate Centre and Other division's +$4m movement (from -$4m to 0); it is part of the where-layer and is not separately explained.
- The provision-type bridge (net collective -3, net new and increased individual +76, write-backs -74) sums exactly to the -$1m total, so residual is 0.
- The presentation reports New Zealand's impairment expense decrease as ($14m) in NZD terms (ev-21), versus the results book's $12m in AUD (ev-10); the difference is a currency/definitional matter.
- No dedicated walk/bridge chart for the LIE movement exists; the decomposition is built from the provision-type split table (p109) and the divisional table (p34).
- Driver contributions are deltas computed from printed period levels (capped at 80 confidence); the total movement is stated by the bank in words.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-09-01T17:16:33+00:00
- seconds: 96.5
- cost_usd: 0.0052
- tokens: 220421 in / 17251 out
- latency: 14 calls, 96s in requests (slowest 39s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 22
- pages_read: 7
- charts_read: 0
- budget_exhausted: no
