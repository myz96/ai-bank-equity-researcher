# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 40/100

CBA's Loan Impairment Expense (LIE) increased $62 million to $788 million in FY26 (FY25: $726 million), a 9% rise. The impairment ratio rose 1 basis point to 8 bps of average GLAA. Management attributes the increase primarily to portfolio growth and macroeconomic headwinds (cost-of-living, geopolitical risk). While corporate collective provisions grew significantly (+$172m) reflecting these risks, consumer collective provisions decreased (-$48m) due to rising house prices, partially offsetting the corporate increase.

### collective.volume
*unquantified | confidence 60/100*

Management explicitly cites 'portfolio growth' as a main driver for the LIE increase (ev-1). This is corroborated by the significant growth in Corporate Collective Provisions (+$172m, ev-11), which are typically driven by volume expansion alongside risk factors.
> [ev-1] CBA/FY26/asx_announcement, PDF p2: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."
> [ev-11] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."

### overlays_fla
*unquantified | confidence 60/100*

The narrative highlights 'increased geopolitical risk and macroeconomic uncertainty' (ev-1, ev-11) and 'more targeted forward-looking adjustments' (ev-12). These represent forward-looking overlays or FLA components adjusting for expected future losses beyond current historical trends.
> [ev-1] CBA/FY26/asx_announcement, PDF p2: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."
> [ev-11] CBA/FY26/profit_announcement, PDF p44: "Corporate collective provisions increased $172 million or 7% to $2,797 million, mainly reflecting portfolio growth, increased geopolitical risk and macroeconomic uncertainty."
> [ev-12] CBA/FY26/profit_announcement, PDF p44: "Consumer collective provisions decreased $48 million or 2% to $2,888 million, reflecting rising house prices over the period and more targeted forward-looking adjustments for higher risk customer cohorts."

### collective.asset_quality
*unquantified | confidence 60/100*

Cost-of-living pressures (ev-1) and rising arrears in credit cards (+7bps) and personal loans (+31bps) (ev-23) indicate deteriorating asset quality in specific retail segments, contributing to higher provisions despite falling home loan arrears.
> [ev-1] CBA/FY26/asx_announcement, PDF p2: "Loan impairment expense increased mainly reflecting portfolio growth, cost-of-living pressures and increased geopolitical risk and macroeconomic uncertainty."
> [ev-23] CBA/FY26/profit_announcement, PDF p46: "Credit card and personal loan 90+ days arrears were 0.73% and 1.72% respectively, an increase of 7 basis points and 31 basis points on the prior half"

## Limitations
- No quantitative walk chart was provided to decompose the $62m movement into specific driver contributions.
- The bank's narrative attributes the increase to multiple factors (growth, macro, geopolitics) without providing a precise numerical split between them.
- Confidence is capped at 60 for individual drivers because they rely on narrative attribution rather than quantified data points.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:34:11+00:00
- seconds: 46.9
- cost_usd: 0.0014
- tokens: 24445 in / 5084 out
- orchestration: pipeline
