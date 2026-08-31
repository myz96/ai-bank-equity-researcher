# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 80/100

*Read from: row 'Loan impairment expense', column FY25 -> column FY26*

CBA's credit impairment charge (LIE) increased $62 million (+9%) to $788 million in FY26 from $726 million in FY25. The loss rate rose 1 basis point to 8 bps on average GLAA. Growth was driven by a $106 million increase in Retail Banking Services, partially offset by decreases in Business Banking and Institutional Banking.

> [ev-12] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense/(benefit) 788 726 9 469 319 47"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-21] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."
> [ev-26] CBA/FY26/results_presentation, printed p29: "Loan impairment expense $m"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | Retail Banking Services | +106 $m | 80 | 2 () | ev-13, ev-19, ev-25 |
| `collective.asset_quality` | Business Banking | -45 $m | 80 | 1 (single_source) | ev-14, ev-20 |
| `individual_provisions` | Institutional Banking and Markets | -16 $m | 80 | 1 (single_source) | ev-15, ev-18 |
| `other_unmapped` | New Zealand | +11 $m | 80 | 1 (single_source) | ev-16, ev-18 |
| `other_unmapped` | Corporate Centre and Other | +6 $m | 80 | 1 (single_source) | ev-17, ev-18 |

### collective.volume — "Retail Banking Services"
*+106 $m | confidence 80/100*

Retail LIE increased $106 million to $378 million. This rise reflects portfolio growth and increased global macroeconomic uncertainty, as stated in the results presentation.
> [ev-13] CBA/FY26/profit_announcement, PDF p34: "Retail Banking Services 378 272 39 146 232 (37)"
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-25] CBA/FY26/results_presentation, printed p29: "Impairment expense higher reflecting portfolio growth and increased global macroeconomic uncertainty"

### collective.asset_quality — "Business Banking"
*-45 $m | confidence 80/100*

Business Banking LIE decreased $45 million to $310 million. The improvement is attributed to lower collective provision charges and improved asset quality relative to the prior year.
> [ev-14] CBA/FY26/profit_announcement, PDF p34: "Business Banking 310 355 (13) 219 91 large"
> [ev-20] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"

### individual_provisions — "Institutional Banking and Markets"
*-16 $m | confidence 80/100*

IB&M LIE decreased $16 million to $33 million from $49 million in FY25, reflecting lower individually assessed provisions and write-backs.
> [ev-15] CBA/FY26/profit_announcement, PDF p34: "Institutional Banking and Markets 33 49 (33) 41 (8) large"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."

### other_unmapped — "New Zealand"
*+11 $m | confidence 80/100*

New Zealand LIE increased $11 million to $66 million from $55 million in FY25, driven by higher arrears and cost-of-living pressures.
> [ev-16] CBA/FY26/profit_announcement, PDF p34: "New Zealand 66 55 20 62 4 large"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."

### other_unmapped — "Corporate Centre and Other"
*+6 $m | confidence 80/100*

Corporate Centre and Other LIE increased $6 million to $1 million from a benefit of $5 million in FY25.
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "Corporate Centre and Other 1 (5) large 1 – n/a"
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."

## Limitations
- The bank does not explicitly map divisional LIE movements to specific canonical drivers (e.g., volume vs. quality). Contributions are inferred from narrative context.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T00:50:50+00:00
- seconds: 57.7
- cost_usd: 0.0024
- tokens: 43126 in / 8715 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
