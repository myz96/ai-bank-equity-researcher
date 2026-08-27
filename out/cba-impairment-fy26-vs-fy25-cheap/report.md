# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 95/100

CBA's Loan Impairment Expense (LIE) increased $62 million to $788 million in FY26 (ev-22). The loss rate rose 1 basis point to 8 bps of average GLAA (ev-25). This increase was primarily driven by Retail Banking Services (+$106m), partially offset by Business Banking (-$45m) and Institutional Banking & Markets (-$16m). While the P&L charge increased, total provision balances grew modestly ($99m), with corporate collective provisions rising due to growth and macro uncertainty, while consumer provisions declined on improved housing prices.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +106 $m | 85 | 1 (single_source) | ev-23, ev-17, ev-8, ev-9 |
| `collective.volume` | Business Banking | -45 $m | 85 | 1 (single_source) | ev-24, ev-18 |
| `individual_provisions` | Institutional Banking and Markets | -16 $m | 85 | 1 (single_source) | ev-19, ev-10 |
| `other_unmapped` | New Zealand | +11 $m | 95 | 2 () | ev-20, ev-27 |
| `other_unmapped` | Corporate Centre and Other | +6 $m | 85 | 1 (single_source) | ev-21 |
| *residual (unexplained)* | — | +0 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+106 $m | confidence 85/100*

RBS LIE increased $106 million to $378 million (ev-23). Although consumer collective provisions decreased, the net expense rise suggests higher individual assessments or write-offs within the retail portfolio, as collective provisions fell (ev-8, ev-9).
> [ev-23] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "Retail Banking Services 378 272 39"
> [ev-8] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts."
> [ev-9] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million, reflecting rising house prices over the period, partly offset by higher arrears."

### collective.volume — "Business Banking"
*-45 $m | confidence 85/100*


> [ev-24] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Business Banking 310 355 (13)"

### individual_provisions — "Institutional Banking and Markets"
*-16 $m | confidence 85/100*

IBM LIE decreased from $49 million to $33 million, a delta of -$16 million (ev-19, ev-21 calculation: 33-49=-16). Corporate individually assessed provisions also decreased $6 million (ev-10), consistent with this segment.
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "Institutional Banking and Markets 33 49 (33)"
> [ev-10] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

### other_unmapped — "New Zealand"
*+11 $m | confidence 95/100*

NZ LIE increased $11 million to $66 million (ev-20). ASB loss rates rose significantly from 11 bps to 20 bps (ev-27), driving the expense increase.
> [ev-20] CBA/FY26/profit_announcement, PDF p34: "New Zealand 66 55 20"
> [ev-27] CBA/FY26/results_presentation, printed p69: "Loan loss rate by business unit1,2 FY26 RBS 7 BB 4 IB&M 4 ASB 20 Group 6 FY25 RBS 9 BB 6 IB&M 9 ASB 11 Group 3 bpts"

### other_unmapped — "Corporate Centre and Other"
*+6 $m | confidence 85/100*

CCO LIE moved from a benefit of $5 million to an expense of $1 million, a positive contribution of $6 million to the total delta (ev-21).
> [ev-21] CBA/FY26/profit_announcement, PDF p34: "Corporate Centre and Other 1 (5) large"

## Source disagreements
- **Loan Impairment Expense Basis** (definitional): 788 / 726 — cash (ev-16, ev-22) vs 788 / 726 — statutory (ev-5)
  Preferred: cash. The values are identical for both bases in FY26/FY25, but the primary driver table (ev-17 to ev-21) is explicitly labeled 'cash'. The narrative (ev-22) aligns with the cash basis. No material disagreement exists in magnitude.

## Limitations
- The attribution relies on divisional P&L deltas rather than a direct walk chart of impairment drivers. Individual drivers like 'collective.volume' vs 'collective.asset_quality' within divisions are inferred from balance sheet provision movements (ev-7, ev-8) and narrative context, not explicitly quantified as separate bars in the P&L bridge.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-27T07:59:42+00:00
- seconds: 73.2
- cost_usd: 0.0016
- tokens: 26389 in / 6224 out
- orchestration: pipeline
