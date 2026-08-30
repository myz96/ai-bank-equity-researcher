# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's credit impairment charge was broadly flat at $319 million in 1H26 (Dec 2025), a decrease of $1 million from $320 million in 1H25 (Dec 2024). The loss rate remained stable at 6 basis points on average gross loans and acceptances. The movement was driven by offsetting divisional shifts: Retail Banking Services saw a significant increase in expense (+$153 million) due to losses in the consumer finance portfolio, while Business Banking experienced a substantial decrease (-$129 million). Institutional Banking and Markets also decreased (-$17 million) to a benefit, and New Zealand decreased (-$12 million).

> [ev-1] CBA/1H26/profit_announcement, PDF p109: "Total loan impairment expense"
> [ev-2] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +153 $m | 80 | 1 (single_source) | ev-6, ev-19 |
| `individual_provisions` | Business Banking | -129 $m | 80 | 1 (single_source) | ev-3 |
| `write_backs_recoveries` | Institutional Banking and Markets | -17 $m | 80 | 1 (single_source) | ev-4 |
| `other_unmapped` | New Zealand | -12 $m | 80 | 1 (single_source) | ev-5 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+153 $m | confidence 80/100*

Expense increased $153 million to $232 million. This was mainly driven by losses within the consumer finance portfolio.
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-19] CBA/1H26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances (GLAAs) was 7 basis points, an increase of 1 basis point on the prior half, mainly driven by losses within the consumer finance portfolio."

### individual_provisions — "Business Banking"
*-129 $m | confidence 80/100*

Expense decreased $129 million to $91 million. While the bank does not explicitly attribute this specific delta to individual vs collective drivers in the text, the sharp reduction is consistent with improved asset quality or lower individual provisions compared to the prior period.
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"

### write_backs_recoveries — "Institutional Banking and Markets"
*-17 $m | confidence 80/100*

Moved to a benefit of $8 million (expense of -$8 million), a decrease of $17 million. This likely reflects recoveries or write-backs outweighing new charges.
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"

### other_unmapped — "New Zealand"
*-12 $m | confidence 80/100*

Expense decreased $12 million to $4 million. No specific driver breakdown provided for this division in the text.
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"

## Limitations
- The bank does not provide a granular split of the Business Banking, IB&M, and NZ movements into canonical provision types (e.g., volume vs asset quality). Drivers are attributed based on the most likely component given the direction and magnitude, but exact attribution is inferred.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)
- Capped at 80: collective.asset_quality +153 $m. drivers_reconcile failed, so the parts and the whole disagree. That proves one of these claims is wrong without saying which, so none of them may claim near-certainty.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T18:43:54+00:00
- seconds: 51.5
- cost_usd: 0.0025
- tokens: 49351 in / 8186 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
