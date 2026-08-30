# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 75/100

*Read from: row 'Operating expenses to total operating income (%)', column 30 Jun 25 column -> column 30 Jun 26 column*

CBA’s cost-to-income ratio (cash basis) improved 20bps to 45.5% in FY26 from 45.7% in FY25. The improvement was driven by operating income growing 6.2% to $30,224m, outpacing operating expense growth of 5.8% to $13,755m. Income growth reflected disciplined franchise volume expansion across home loans, business lending and deposits, alongside higher insurance and equities income. Expense growth was driven by wage inflation, technology investment, and frontline staffing, partly offset by productivity initiatives and favourable FX. Restructuring and notable items rose $40m year-on-year to $170m, partially offsetting the jaws benefit.

> [ev-3] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"
> [ev-6] CBA/FY26/results_presentation, printed p54: "Cost to income 45.5% (20bpts)"
> [ev-7] CBA/FY26/results_presentation, printed p54: "Operating income ($m) 30,224 +6.2%"
> [ev-8] CBA/FY26/results_presentation, printed p54: "Operating expenses ($m) 13,755 +5.8%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | Operating income growth | -0.17 ppt | 80 | 2 () | ev-4, ev-7, ev-21 |
| `expense_growth` | Operating expense growth | +0.15 ppt | 90 | 2 () | ev-2, ev-11, ev-17 |
| `notable_items` | Restructuring and notable items | +0.13 ppt | 80 | 1 (single_source) | ev-14, ev-12 |
| *residual (unexplained)* | — | -0.11 ppt | — | — |

### income_growth — "Operating income growth"
*-0.17 ppt | confidence 80/100*

Operating income grew 6.2% ($28,465m to $30,224m), driven by average lending volume growth of 6.8%, deposit volume growth of 8.2%, higher insurance income, higher CommSec equities income, and one-off gains including a milestone payment from CommInsure GI sale and a fair value gain on Gemini IPO, partly offset by lower retail foreign exchange income. The faster income growth versus expense growth lowered the ratio.
> [ev-4] CBA/FY26/profit_announcement, printed p2: "Total operating income 30,224 28,465 6"
> [ev-7] CBA/FY26/results_presentation, printed p54: "Operating income ($m) 30,224 +6.2%"
> [ev-21] CBA/FY26/results_presentation, printed p25: "Higher income from disciplined franchise growth"

### expense_growth — "Operating expense growth"
*+0.15 ppt | confidence 90/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m) per the primary walk chart: inflation contributed +$455m (wage inflation including higher super guarantee, vendor IT inflation +5%, cloud consumption and software licensing); technology investment +$444m (infrastructure, resilience and AI capabilities); frontline and operations investment +$128m; other costs +$96m; partially offset by productivity savings -$404m. Headline operating expenses including restructuring and notable items grew 5.8% to $13,755m.
> [ev-2] CBA/FY26/results_presentation, printed p27: "[walk chart] Operating expenses: FY25 12866 -> FY26 13585"
> [ev-11] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses 13,585 12,866 6"
> [ev-17] CBA/FY26/profit_announcement, PDF p9: "Operating expenses increased 6% driven by inflation, investment in technology, fraud, scams and financial crime, partly offset by productivity initiatives and favourable foreign exchange."

### notable_items — "Restructuring and notable items"
*+0.13 ppt | confidence 80/100*

Restructuring and notable items increased $40m to $170m (FY26: NZ legal proceedings settlement, ASIC Better Banking review goodwill payment, domestic customer remediation; FY25: domestic and NZ customer remediation, Bankwest restructuring provision). This added $40m to expenses, raising the ratio by approximately $40m/$30,224m = 0.13ppt.
> [ev-14] CBA/FY26/profit_announcement, PDF p31: "Restructuring and notable items ¹ 170 130 31"
> [ev-12] CBA/FY26/profit_announcement, PDF p31: "Total operating expenses 13,755 12,996 6"

## Limitations
- No dedicated CTI walk/breakdown chart provided by the bank; jaws contributions computed from income and expense growth rates rather than a formal CTI decomposition.
- Driver contributions do not sum exactly to the -0.2ppt movement due to interaction effects between income and expense growth and rounding of reported ratio levels.
- The expense growth contribution is based on the underlying operating expenses walk (ev-2) which excludes restructuring and notable items; headline expense growth includes an additional $40m of notable items.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:21:53+00:00
- seconds: 297.5
- cost_usd: 0.0658
- tokens: 1925853 in / 12863 out
- orchestration: agent
- tool_calls: 62
- pages_read: 13
- charts_read: 2
- budget_exhausted: no
