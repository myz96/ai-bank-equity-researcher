# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 80/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's credit impairment charge was essentially flat at $319 million in 1H26 (ended Dec 2025), a decrease of $1 million from the $320 million reported in 1H25 (ended Dec 2024). The annualised loss rate decreased by 1 basis point to 6 bps on average gross loans and acceptances. This stability masked significant offsetting movements: Retail Banking Services saw a $153 million increase in charges driven by consumer finance losses, while Business Banking reduced its charge by $129 million.

> [ev-1] CBA/1H26/profit_announcement, PDF p109: "Total loan impairment expense"
> [ev-5] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-10] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."
> [ev-9] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-6] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Net new and increased individual provisioning | +76 $m | 80 | 1 (single_source) | ev-3, ev-16, ev-17 |
| `collective.asset_quality` | Net collective provision funding | -3 $m | 80 | 1 (single_source) | ev-2, ev-14, ev-15 |
| `write_backs_recoveries` | Write-back of individually assessed provisions | -74 $m | 80 | 1 (single_source) | ev-4 |
| *residual (unexplained)* | — | +0 $m | — | — |

### individual_provisions — "Net new and increased individual provisioning"
*+76 $m | confidence 80/100*

Increased by $76 million to $245 million (from $169 million). Driven by downgrades for a small number of single-name customers in Corporate banking, where individually assessed provisions rose $56 million to $694 million (ev-16). Consumer individually assessed provisions also rose slightly by $2 million to $99 million (ev-17).
> [ev-3] CBA/1H26/profit_announcement, PDF p109: "Net new and increased individual provisioning"
> [ev-16] CBA/1H26/profit_announcement, printed p24: "Corporate individually assessed provisions increased $56 million or 9% to $694 million, mainly driven by downgrades for a small number of single name customers."
> [ev-17] CBA/1H26/profit_announcement, printed p24: "Consumer individually assessed provisions increased $2 million or 2% to $99 million."

### collective.asset_quality — "Net collective provision funding"
*-3 $m | confidence 80/100*

Decreased by $3 million to $218 million (from $221 million). In Consumer banking, collective provisions increased $55 million to $2,961 million due to elevated geopolitical tensions and global macroeconomic uncertainty, partly offset by rising house prices and lower interest rates (ev-14). In Corporate banking, collective provisions decreased $5 million to $2,581 million reflecting improvements in credit quality, offset by portfolio growth and macro uncertainty (ev-15).
> [ev-2] CBA/1H26/profit_announcement, PDF p109: "Net collective provision funding"
> [ev-14] CBA/1H26/profit_announcement, printed p24: "Consumer collective provisions increased $55 million or 2% to $2,961 million, reflecting elevated geopolitical tensions and global macroeconomic uncertainty. This was partly offset by the positive impact on households of rising house prices and lower interest rates."
> [ev-15] CBA/1H26/profit_announcement, printed p24: "Corporate collective provisions decreased $5 million to $2,581 million, reflecting improvements in credit quality. This was offset by portfolio growth, elevated geopolitical tensions and global macroeconomic uncertainty."

### write_backs_recoveries — "Write-back of individually assessed provisions"
*-74 $m | confidence 80/100*

The write-back benefit increased by $74 million to $(144) million (from $(70) million). This larger reduction in expense partially offset the increases in new individual and collective provisions.
> [ev-4] CBA/1H26/profit_announcement, PDF p109: "Write-back of individually assessed provisions"

## Limitations
- Confidence is capped at 80 because the quantified driver contributions were computed by subtracting period-end levels found in separate table rows rather than reading a pre-calculated bridge or movement column directly provided by the bank.
- The narrative does not explicitly map the divisional movements (Retail +$153m, Business -$129m) to specific provision types (individual vs collective) within the provided evidence records.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T16:13:13+00:00
- seconds: 47.0
- cost_usd: 0.0021
- tokens: 37495 in / 7580 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
