# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 85/100

*Read from: row 'Total loan impairment expense', column FY25 (30 Jun 2025) -> column FY26 (30 Jun 2026)*

CBA's credit impairment charge increased $62 million to $788 million in FY26 (ev-14). The loss rate rose 1 basis point to 8 bps on average GLAA (ev-19). This increase was primarily driven by higher expenses in Retail Banking Services (+$106m) and New Zealand (+$11m), partially offset by decreases in Business Banking (-$45m) and Institutional Banking (-$16m). The movement reflects portfolio growth and macroeconomic uncertainty.

> [ev-14] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "An increase in New Zealand of $11 million to an expense of $66 million"
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Retail Banking Services | +106 $m | 85 | 1 (single_source) | ev-15, ev-3, ev-5 |
| `individual_provisions` | New Zealand | +11 $m | 85 | 2 () | ev-16, ev-27 |
| `collective.asset_quality` | Business Banking | -45 $m | 80 | 1 (single_source) | ev-17, ev-10 |
| `write_backs_recoveries` | Institutional Banking and Markets | -16 $m | 80 | 1 (single_source) | ev-18, ev-12 |
| *residual (unexplained)* | — | +6 $m | — | — |

### collective.volume — "Retail Banking Services"
*+106 $m | confidence 85/100*

Retail Banking Services LIE increased $106 million to $378 million (ev-15). This rise is attributed to portfolio growth and rising arrears in the well-secured home lending portfolio (ev-3, ev-5).
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-3] CBA/FY26/profit_announcement, PDF p45: "Gross non-performing exposures were $11,113 million, an increase of $644 million or 6% on the prior half, mainly driven by higher arrears in the well-secured home lending portfolio."
> [ev-5] CBA/FY26/profit_announcement, PDF p45: "Consumer loan impairment expense (LIE) as a percentage of average gross loans and acceptances was 4 basis points, a decrease of 3 basis points on the prior half, driven by lower collective provision charges."

### individual_provisions — "New Zealand"
*+11 $m | confidence 85/100*

New Zealand LIE increased $11 million to $66 million (ev-16). The bank attributes this to increased global macroeconomic uncertainty affecting its offshore operations (ev-27).
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "An increase in New Zealand of $11 million to an expense of $66 million"
> [ev-27] CBA/FY26/results_presentation, printed p29: "Impairment expense higher reflecting portfolio growth and increased global macroeconomic uncertainty"

### collective.asset_quality — "Business Banking"
*-45 $m | confidence 80/100*

Business Banking LIE decreased $45 million to $310 million (ev-17). This reduction reflects lower collective provision charges as house prices rose, partly offsetting risk migration (ev-10).
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-10] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts."

### write_backs_recoveries — "Institutional Banking and Markets"
*-16 $m | confidence 80/100*

Institutional Banking and Markets LIE decreased $16 million to $33 million (ev-18). Corporate individually assessed provisions decreased $6 million due to write-backs and write-offs (ev-12).
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million"
> [ev-12] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million, driven by write-backs and write-offs."

## Limitations
- The sum of quantified divisional drivers ($106m + $11m - $45m - $16m = $56m) leaves a residual of $6m against the total delta of $62m. This residual likely represents the Corporate Centre or other unallocated items not explicitly broken out in the divisional table.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T16:28:02+00:00
- seconds: 66.1
- cost_usd: 0.0031
- tokens: 58600 in / 10461 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
