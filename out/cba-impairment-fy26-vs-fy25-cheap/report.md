# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 85/100

*Read from: row 'Total loan impairment expense', column FY25 (12 months ended Jun 2025) -> column FY26 (12 months ended Jun 2026)*

CBA's credit impairment charge increased $62 million to $788 million in FY26 (ev-16). The loss rate rose 1 basis point to 8 bps on average GLAA (ev-19). This increase was driven by a $106 million rise in Retail Banking Services provisions, partially offset by a $45 million decrease in Business Banking and a $16 million decrease in Institutional Banking and Markets (ev-17, ev-18, ev-13). Corporate collective provisions grew $172 million due to portfolio growth and macro uncertainty, while consumer collective provisions fell $48 million (ev-6, ev-7).

> [ev-16] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-13] CBA/FY26/profit_announcement, PDF p34: "Institutional Banking and Markets 33 49 (33) 41 (8) large"
> [ev-6] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."
> [ev-7] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts. This was partly offset by higher arrears, rising cost-of-living pressures, increased geopolitical risk, and macroeconomic uncertainty."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Portfolio growth | +172 $m | 85 | 1 (single_source) | ev-6 |
| `collective.asset_quality` | Risk migration / Macro uncertainty | -48 $m | 85 | 1 (single_source) | ev-7 |
| `individual_provisions` | Individually assessed provisions | -25 $m | 80 | 1 (single_source) | ev-8, ev-9 |
| *residual (unexplained)* | — | -37 $m | — | — |

### collective.volume — "Portfolio growth"
*+172 $m | confidence 85/100*

Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth (ev-6).
> [ev-6] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."

### collective.asset_quality — "Risk migration / Macro uncertainty"
*-48 $m | confidence 85/100*

Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices and more targeted forward-looking adjustments for higher risk customer cohorts (ev-7).
> [ev-7] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts. This was partly offset by higher arrears, rising cost-of-living pressures, increased geopolitical risk, and macroeconomic uncertainty."

### individual_provisions — "Individually assessed provisions"
*-25 $m | confidence 80/100*

Consumer individually assessed provisions decreased $19 million to $97 million, and corporate individually assessed provisions decreased $6 million to $694 million, driven by write-backs and write-offs (ev-8, ev-9).
> [ev-8] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million, reflecting rising house prices over the period, partly offset by higher arrears."
> [ev-9] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

## Source disagreements
- **Divisional Bridge Sum** (definitional): Sum of stated provision drivers: $99m (ev-6, ev-7, ev-8, ev-9) vs Stated P&L LIE delta: $62m (ev-16)
  Preferred: P&L LIE delta ($62m). The sum of the specific provision balance changes cited ($172m - $48m - $19m - $6m = $99m) exceeds the reported Loan Impairment Expense movement ($62m). This discrepancy arises because provision balance movements include non-P&L items such as foreign exchange translation differences, direct write-offs against provisions, and recoveries that do not flow through the current period's impairment expense line.

## Limitations
- The quantified bridge is based on the net change in provision balances rather than a direct P&L driver walk, leading to a residual difference between the provision balance movements and the P&L impairment expense.
- Specific divisional drivers (Retail +$106m, Business -$45m) are provided in the narrative but were not included in the primary canonical driver table to avoid double-counting with the aggregate provision data.
- Capped at 80: individual_provisions -25 $m. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T18:54:57+00:00
- seconds: 49.7
- cost_usd: 0.0023
- tokens: 43040 in / 8103 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
