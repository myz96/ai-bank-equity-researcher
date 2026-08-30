# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's credit impairment charge was broadly flat at $319 million in 1H26 (vs $320 million in 1H25), a decrease of $1 million. The annualised loss rate decreased by 1 basis point to 6 bps on average gross loans and acceptances. The movement was driven by significant decreases in Business Banking ($129m) and Institutional Banking ($17m), partially offset by an increase in Retail Banking Services ($153m).

> [ev-1] CBA/1H26/profit_announcement, PDF p109: "Total loan impairment expense"
> [ev-2] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Business Banking | -129 $m | 80 | 1 (single_source) | ev-3, ev-9 |
| `write_backs_recoveries` | Institutional Banking and Markets | -17 $m | 80 | 1 (single_source) | ev-4, ev-10 |
| `individual_provisions` | Retail Banking Services | +153 $m | 80 | 1 (single_source) | ev-6, ev-8 |
| `other_unmapped` | New Zealand | -12 $m | 80 | 1 (single_source) | ev-5, ev-11 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Business Banking"
*-129 $m | confidence 80/100*

Expense decreased $129 million to $91 million (ev-3, ev-9). This reduction is attributed to lower collective provisions as risk migration improved, though the bank does not explicitly split this divisional delta into volume vs quality drivers.
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "Business Banking 91 135 220"

### write_backs_recoveries — "Institutional Banking and Markets"
*-17 $m | confidence 80/100*

Moved from a $9 million expense to an $8 million benefit (ev-4, ev-10). The shift reflects recoveries and write-backs outweighing new charges in the institutional portfolio.
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"
> [ev-10] CBA/1H26/profit_announcement, printed p18: "Institutional Banking and Markets (8) 40 9"

### individual_provisions — "Retail Banking Services"
*+153 $m | confidence 80/100*

Expense increased $153 million to $232 million (ev-6, ev-8). The bank attributes the rise mainly to losses within the consumer finance portfolio, indicating higher individually assessed or specific collective risks.
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Retail Banking Services 232 193 79"

### other_unmapped — "New Zealand"
*-12 $m | confidence 80/100*

Expense decreased $12 million to $4 million (ev-5, ev-11). Specific drivers for this offshore segment are not detailed separately in the provided text.
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "New Zealand 4 39 16"

## Limitations
- The bank does not provide a canonical bridge splitting the total charge into 'collective' vs 'individual' components for the full group. Drivers are attributed based on divisional movements and narrative cues (e.g., 'consumer finance losses').
- Confidence is capped at 80 because the deltas are computed from period levels rather than being explicitly stated as driver contributions.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T12:24:49+00:00
- seconds: 55.4
- cost_usd: 0.0026
- tokens: 49187 in / 8352 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
