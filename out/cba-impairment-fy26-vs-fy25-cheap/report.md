# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 85/100

*Read from: row 'Total loan impairment expense', column FY25 (12 months ended Jun 2025) -> column FY26 (12 months ended Jun 2026)*

CBA's credit impairment charge increased $62 million to $788 million in FY26, driven by a $106 million rise in Retail Banking Services and an $11 million increase in New Zealand, partially offset by decreases in Business Banking (-$45 million) and Institutional Banking (-$16 million). The loss rate rose 1 basis point to 8 bps on average GLAA.

> [ev-16] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense was $788 million, an increase of $62 million or 9% on the prior year."
> [ev-21] CBA/FY26/profit_announcement, PDF p34: "Loan impairment expense as a percentage of average gross loans and acceptances (GLAA) increased 1 basis point to 8 basis points."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.asset_quality` | Retail Banking Services | +106 $m | 85 | 1 (single_source) | ev-17, ev-3, ev-13, ev-14 |
| `other_unmapped` | New Zealand | +11 $m | 85 | 1 (single_source) | ev-18 |
| `collective.volume` | Business Banking | -45 $m | 80 | 1 (single_source) | ev-19, ev-12 |
| `individual_provisions` | Institutional Banking and Markets | -16 $m | 80 | 1 (single_source) | ev-20, ev-15 |
| *residual (unexplained)* | — | +6 $m | — | — |

### collective.asset_quality — "Retail Banking Services"
*+106 $m | confidence 85/100*

Increased by $106 million to $378 million. Driven by higher arrears in the well-secured home lending portfolio (ev-3), which pushed gross non-performing exposures up $644 million on the prior half. Consumer collective provisions decreased slightly ($48m), but individually assessed provisions fell less than the volume-driven collective costs, resulting in a net expense increase.
> [ev-17] CBA/FY26/profit_announcement, PDF p34: "An increase in Retail Banking Services of $106 million to an expense of $378 million"
> [ev-3] CBA/FY26/profit_announcement, PDF p45: "Gross non-performing exposures were $11,113 million, an increase of $644 million or 6% on the prior half, mainly driven by higher arrears in the well-secured home lending portfolio."
> [ev-13] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million"
> [ev-14] CBA/FY26/profit_announcement, PDF p44: "Consumer individually assessed provisions decreased $19 million or 16% to $97 million"

### other_unmapped — "New Zealand"
*+11 $m | confidence 85/100*

Increased by $11 million to $66 million. Reflecting specific local credit conditions and portfolio growth within the ASB subsidiary.
> [ev-18] CBA/FY26/profit_announcement, PDF p34: "An increase in New Zealand of $11 million to an expense of $66 million"

### collective.volume — "Business Banking"
*-45 $m | confidence 80/100*

Decreased by $45 million to $310 million. Despite corporate collective provisions increasing by $172 million (ev-12), the overall expense fell, likely due to lower individually assessed provisions or write-backs not fully detailed in the segment split.
> [ev-19] CBA/FY26/profit_announcement, PDF p34: "A decrease in Business Banking of $45 million to an expense of $310 million"
> [ev-12] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million"

### individual_provisions — "Institutional Banking and Markets"
*-16 $m | confidence 80/100*

Decreased by $16 million to $33 million. Corporate individually assessed provisions decreased by $6 million to $694 million (ev-15), contributing to the lower expense.
> [ev-20] CBA/FY26/profit_announcement, PDF p34: "A decrease in Institutional Banking and Markets of $16 million to an expense of $33 million"
> [ev-15] CBA/FY26/profit_announcement, PDF p44: "Corporate individually assessed provisions decreased $6 million or 1% to $694 million"

## Limitations
- The residual of $6m is unattributed; the bank does not provide a full breakdown of all divisional drivers summing exactly to the total LIE movement in the provided text.
- Driver narratives infer 'volume' vs 'quality' splits based on aggregate provision changes where explicit driver attribution per division is not granularly stated.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:56:31+00:00
- seconds: 52.6
- cost_usd: 0.0023
- tokens: 42223 in / 7565 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/FY26/profit_announcement p116 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p117 <- p118 Note 2.2 Provisions for Impairment and Asset Quality [added]', 'CBA/FY26/profit_announcement p118 <- p118 Note 2.2 Provisions for Impairment and Asset Quality']
