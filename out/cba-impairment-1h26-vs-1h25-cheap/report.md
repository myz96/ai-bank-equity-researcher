# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

*Read from: row 'Total loan impairment expense', column 31 Dec 24 -> column 31 Dec 25*

CBA's credit impairment charge was broadly flat at $319 million in 1H26 (vs $320 million in 1H25), a decrease of $1 million. The loss rate decreased by 1 basis point to 6 bps on average gross loans and acceptances. This stability masked significant offsetting movements across divisions: Retail Banking Services saw a large increase in charges (+$153 million) driven by consumer finance losses, while Business Banking charges fell sharply (-$129 million). Institutional Banking and Markets swung from a small charge to a benefit (-$17 million), and New Zealand expenses also declined (-$12 million).

> [ev-1] CBA/1H26/profit_announcement, PDF p109: "Total loan impairment expense"
> [ev-2] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense was $319 million, a decrease of $1 million on the prior comparative period."
> [ev-7] CBA/1H26/profit_announcement, printed p18: "Loan impairment expense annualised as a percentage of average gross loans and acceptances (GLAAs) decreased 1 basis point to 6 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +153 $m | 80 | 1 (single_source) | ev-6, ev-8, ev-19 |
| `individual_provisions` | Business Banking | -129 $m | 80 | 1 (single_source) | ev-3, ev-9 |
| `write_backs_recoveries` | Institutional Banking and Markets | -17 $m | 80 | 1 (single_source) | ev-4, ev-10 |
| `other_unmapped` | New Zealand | -12 $m | 80 | 1 (single_source) | ev-5, ev-11 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+153 $m | confidence 80/100*

Retail charges increased by $153 million to $232 million. The bank attributes this mainly to losses within the consumer finance portfolio, driving the consumer loss rate up 1 basis point to 7 bps.
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-8] CBA/1H26/profit_announcement, printed p18: "Retail Banking Services 232 193 79"
> [ev-19] CBA/1H26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances (GLAAs) was 7 basis points, an increase of 1 basis point on the prior half, mainly driven by losses within the consumer finance portfolio."

### individual_provisions — "Business Banking"
*-129 $m | confidence 80/100*

Business Banking charges decreased by $129 million to $91 million. While the text does not explicitly split this into individual vs collective drivers for the delta, the sharp decline is attributed to the divisional performance.
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"
> [ev-9] CBA/1H26/profit_announcement, printed p18: "Business Banking 91 135 220"

### write_backs_recoveries — "Institutional Banking and Markets"
*-17 $m | confidence 80/100*

Institutional Banking and Markets swung from a $9 million charge to an $8 million benefit, a total decrease in expense of $17 million.
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"
> [ev-10] CBA/1H26/profit_announcement, printed p18: "Institutional Banking and Markets (8) 40 9"

### other_unmapped — "New Zealand"
*-12 $m | confidence 80/100*

New Zealand impairment expense decreased by $12 million to $4 million.
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"
> [ev-11] CBA/1H26/profit_announcement, printed p18: "New Zealand 4 39 16"

## Limitations
- The bank does not provide a quantified bridge splitting the movement into canonical provision types (e.g., volume vs asset quality vs overlays) for the full group or specific divisions. Contributions are derived from divisional deltas.
- Failed check: drivers_reconcile (drivers -5.0 + residual +0.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T14:42:20+00:00
- seconds: 54.1
- cost_usd: 0.0025
- tokens: 48309 in / 7903 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
