# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 60/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's total loan impairment expense decreased by $1 million to $319 million in 1H26 (vs $320 million in 1H25), a decrease of 0.3%. The annualised loss rate against average gross loans and acceptances (GLAAs) fell 1 basis point to 6 bps. This net stability masks significant offsetting movements: Retail Banking Services saw a $153 million increase in expense, while Business Banking recorded a $129 million decrease.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `individual_provisions` | Individually assessed provisions | +58 $m | 85 | 1 (single_source) | ev-13, ev-14 |
| `collective.asset_quality` | Collective provisions: risk migration | -7 $m | 85 | 1 (single_source) | ev-11, ev-12 |
| *residual (unexplained)* | — | -52 $m | — | — |

### individual_provisions — "Individually assessed provisions"
*+58 $m | confidence 85/100*

Corporate individually assessed provisions increased $56 million to $694 million, driven by downgrades for a small number of single-name customers. Consumer individually assessed provisions rose $2 million to $99 million.
> [ev-13] CBA/1H26/profit_announcement, printed p24: "Corporate individually assessed provisions increased $56 million or 9% to $694 million, mainly driven by downgrades for a small number of single name customers."
> [ev-14] CBA/1H26/profit_announcement, printed p24: "Consumer individually assessed provisions increased $2 million or 2% to $99 million."

### collective.asset_quality — "Collective provisions: risk migration"
*-7 $m | confidence 85/100*

Corporate collective provisions decreased $5 million to $2,581 million, reflecting improvements in credit quality. Consumer collective provisions increased $55 million to $2,961 million due to elevated geopolitical tensions and global macroeconomic uncertainty.
> [ev-11] CBA/1H26/profit_announcement, printed p24: "Consumer collective provisions increased $55 million or 2% to $2,961 million, reflecting elevated geopolitical tensions and global macroeconomic uncertainty. This was partly offset by the positive impact on households of rising house prices and lower interest rates."
> [ev-12] CBA/1H26/profit_announcement, printed p24: "Corporate collective provisions decreased $5 million to $2,581 million, reflecting improvements in credit quality. This was offset by portfolio growth, elevated geopolitical tensions and global macroeconomic uncertainty."

### other_unmapped — "Residual / Unmapped"
*unquantified | confidence 60/100*

The sum of the quantified provision drivers ($58m + -$7m = $51m) does not match the total impairment charge movement (-$1m). The remaining -$52m is attributed to unmapped components such as write-backs, recoveries, or volume effects not explicitly split in the provided text.
> [ev-1] CBA/1H26/profit_announcement, PDF p109: "Total loan impairment expense 319 406 320"
> [ev-2] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-11] CBA/1H26/profit_announcement, printed p24: "Consumer collective provisions increased $55 million or 2% to $2,961 million, reflecting elevated geopolitical tensions and global macroeconomic uncertainty. This was partly offset by the positive impact on households of rising house prices and lower interest rates."
> [ev-12] CBA/1H26/profit_announcement, printed p24: "Corporate collective provisions decreased $5 million to $2,581 million, reflecting improvements in credit quality. This was offset by portfolio growth, elevated geopolitical tensions and global macroeconomic uncertainty."
> [ev-13] CBA/1H26/profit_announcement, printed p24: "Corporate individually assessed provisions increased $56 million or 9% to $694 million, mainly driven by downgrades for a small number of single name customers."
> [ev-14] CBA/1H26/profit_announcement, printed p24: "Consumer individually assessed provisions increased $2 million or 2% to $99 million."

## Limitations
- The bank's narrative provides specific dollar movements for individual and collective provisions but does not provide a full bridge reconciling these provision changes to the P&L Loan Impairment Expense line. Consequently, a residual of $52 million exists between the sum of disclosed provision drivers and the total charge movement.
- Divisional expense movements are known (Retail +$153m, Business -$129m, etc.) but cannot be mapped to the canonical provision taxonomy without further disclosure.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T17:49:41+00:00
- seconds: 59.3
- cost_usd: 0.0018
- tokens: 33021 in / 6312 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
