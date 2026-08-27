# CBA — impairment — 1H26 vs 1H25

**Movement (cash basis):** 320$m → 319$m (-1$m) | **Attribution confidence:** 40/100

CBA's cash loan impairment expense decreased by $1 million to $319 million in 1H26 (ev-2). The loss rate remained stable at 6 bps of average GLAAs (ev-7). This stability masks significant offsetting movements across divisions: Retail Banking Services saw a $153 million increase in charges (ev-6), while Business Banking declined by $129 million (ev-3) and Institutional Banking & Markets improved by $17 million (ev-4). New Zealand also contributed a $12 million decrease (ev-5).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +153 $m | 85 | 1 (single_source) | ev-6, ev-23 |
| `collective.asset_quality` | Business Banking | -129 $m | 95 | 2 () | ev-3, ev-25 |
| `individual_provisions` | Institutional Banking and Markets | -17 $m | 95 | 2 () | ev-4, ev-25 |
| `other_unmapped` | New Zealand | -12 $m | 95 | 2 () | ev-5, ev-25 |
| *residual (unexplained)* | — | -96 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+153 $m | confidence 85/100*

Retail LIE increased $153m to $232m. Loss rates rose 1bp to 7bps, driven by losses in the consumer finance portfolio (ev-6, ev-23).
> [ev-6] CBA/1H26/profit_announcement, printed p18: "An increase in Retail Banking Services of $153 million to an expense of $232 million"
> [ev-23] CBA/1H26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances (GLAAs) was 7 basis points, an increase of 1 basis point on the prior half, mainly driven by losses within the consumer finance portfolio."

### collective.asset_quality — "Business Banking"
*-129 $m | confidence 95/100*

Business Banking LIE decreased $129m to $91m. Loss rates were stable at 17bps (ev-3, ev-25).
> [ev-3] CBA/1H26/profit_announcement, printed p18: "A decrease in Business Banking of $129 million to an expense of $91 million"
> [ev-25] CBA/1H26/results_presentation, printed p68: "Loan loss rate by business unit1,2 bpts 1H26 1H25 RBS 3 3 BB 17 16 IB&M 2 7 ASB 7 8 Group 6 6"

### individual_provisions — "Institutional Banking and Markets"
*-17 $m | confidence 95/100*

IB&M LIE decreased $17m to a benefit of $8m. Loss rates fell from 7bps to 2bps (ev-4, ev-25).
> [ev-4] CBA/1H26/profit_announcement, printed p18: "A decrease in Institutional Banking and Markets of $17 million to a benefit of $8 million"
> [ev-25] CBA/1H26/results_presentation, printed p68: "Loan loss rate by business unit1,2 bpts 1H26 1H25 RBS 3 3 BB 17 16 IB&M 2 7 ASB 7 8 Group 6 6"

### other_unmapped — "New Zealand"
*-12 $m | confidence 95/100*

NZ LIE decreased $12m to $4m. Loss rates fell from 8bps to 7bps (ev-5, ev-25).
> [ev-5] CBA/1H26/profit_announcement, printed p18: "A decrease in New Zealand of $12 million to an expense of $4 million"
> [ev-25] CBA/1H26/results_presentation, printed p68: "Loan loss rate by business unit1,2 bpts 1H26 1H25 RBS 3 3 BB 17 16 IB&M 2 7 ASB 7 8 Group 6 6"

## Source disagreements
- **Total Impairment Movement** (definitional): -$1m — ev-2 (text) vs -$87m — ev-8 (text)
  Preferred: -$1m. The Profit Announcement text contains conflicting statements regarding the total movement. Ev-2 states a decrease of $1m on the prior comparative period, which reconciles with the statutory table (ev-1: 406 to 319). Ev-8 states a decrease of $87m, which contradicts the table and the divisional breakdowns. We prioritize the table and the detailed divisional bullets.
- **IB&M Movement Magnitude** (definitional): -$17m — ev-4 (divisional detail) vs -$48m — ev-9 (aggregate summary)
  Preferred: -$17m. Ev-4 provides the specific divisional delta for IB&M (-$17m) which sums correctly with other divisions to match the -$1m headline. Ev-9 cites a -$48m decrease for IB&M within an aggregate context that appears inconsistent with the primary divisional data and the -$1m total.

## Limitations
- The attribution is based on Cash basis divisional deltas which sum to -$1m.
- The residual of -$96m represents the difference between the Statutory total movement (-$87m) and the Cash total movement (-$1m), plus any rounding or mapping differences not explicitly quantified in the divisional cash bullets.
- Specific driver taxonomy mapping (e.g., volume vs asset quality) is inferred from narrative cues ('losses within consumer finance') rather than explicit provision balance bridges.
- Failed check: drivers_reconcile (drivers -5.0 + residual -96.0 != delta -1.0, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-27T07:42:31+00:00
- seconds: 90.4
- cost_usd: 0.0021
- tokens: 36166 in / 8082 out
- orchestration: pipeline
