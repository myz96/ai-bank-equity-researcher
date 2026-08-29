# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 75/100

*Read from: row 'Total loan impairment expense', column FY25 (12 months ended Jun 2025) -> column FY26 (12 months ended Jun 2026)*

CBA's Loan Impairment Expense increased $62 million to $788 million in FY26, up from $726 million in FY25. The annualised loss rate rose 1 basis point to 8 bps on average GLAA. Growth was driven by Retail Banking Services (+$106m) and New Zealand (+$11m), partially offset by Business Banking (-$45m) and Institutional Banking (-$16m).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Retail Banking Services collective provisions | +106 $m | 80 | 2 () | ev-17, ev-27 |
| `individual_provisions` | Corporate individually assessed provisions | -6 $m | 80 | 1 (single_source) | ev-12 |
| `collective.asset_quality` | Consumer collective provisions | -48 $m | 80 | 1 (single_source) | ev-10 |
| `individual_provisions` | Consumer individually assessed provisions | -19 $m | 80 | 1 (single_source) | ev-11 |
| *residual (unexplained)* | — | +29 $m | — | — |

### collective.volume — "Retail Banking Services collective provisions"
*+106 $m | confidence 80/100*

Retail LIE increased $106m ($378m vs $272m). Narrative attributes this to portfolio growth and macroeconomic uncertainty.
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "Retail Banking Services 378 272 39 146 232 (37)"
> [ev-27] CBA/FY26/results_presentation, printed p29: "Impairment expense higher reflecting portfolio growth and increased global macroeconomic uncertainty"

### individual_provisions — "Corporate individually assessed provisions"
*-6 $m | confidence 80/100*

Corporate IAP decreased $6m ($694m vs $700m implied), driven by write-backs and write-offs.
> [ev-12] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

### collective.asset_quality — "Consumer collective provisions"
*-48 $m | confidence 80/100*

Consumer CP decreased $48m ($2,888m vs $2,936m implied), reflecting rising house prices and targeted forward-looking adjustments.
> [ev-10] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts. This was partly offset by higher arrears, rising cost-of-living pressures, increased geopolitical risk, and macroeconomic uncertainty."

### individual_provisions — "Consumer individually assessed provisions"
*-19 $m | confidence 80/100*

Consumer IAP decreased $19m ($97m vs $116m implied), reflecting rising house prices.
> [ev-11] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million, reflecting rising house prices over the period, partly offset by higher arrears."

## Source disagreements
- **Loss Rate Definition** (definitional): 8 bps (Profit Announcement ev-1, ev-14) vs 1.02% (Results Presentation ev-26)
  Preferred: 8 bps. The Profit Announcement reports the headline annualised loss rate as 8 bps of average GLAA. The Results Presentation table shows a different metric (likely statutory or non-annualised) at 1.02%. Per source hierarchy, the PA narrative is preferred for the primary movement analysis.

## Limitations
- The provided evidence does not contain a full walk chart reconciling the $62m P&L charge to specific driver bars. Contributions are derived from divisional P&L deltas and provision balance changes. A residual of $29m exists, likely representing IB&M, NZ, and Corporate Centre movements not fully detailed in the text.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T13:27:27+00:00
- seconds: 253.0
- cost_usd: 0.0025
- tokens: 45704 in / 8654 out
- orchestration: pipeline
