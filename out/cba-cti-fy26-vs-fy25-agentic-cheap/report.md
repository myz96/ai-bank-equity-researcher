# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 75/100

*Read from: row 'Operating expenses to total operating income (%)', column 30 Jun 25 column -> column 30 Jun 26 column*

CBA's cost-to-income ratio (Operating expenses to total operating income, cash basis) improved 20 basis points to 45.5% in FY26 from 45.7% in FY25. The improvement was driven by operating income growing 6.2% ($28,465m to $30,224m), outpacing operating expense growth of 5.8% ($12,996m to $13,755m). Underlying cost-to-income improved 30 basis points to 44.9% from 45.2%, partly offset by a $40m increase in restructuring and notable items ($130m to $170m).

> [ev-5] CBA/FY26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"
> [ev-7] CBA/FY26/profit_announcement, printed p2: "Total operating income 30,224 28,465 6"
> [ev-8] CBA/FY26/profit_announcement, printed p2: "Total operating expenses (13,755) (12,996) 6"
> [ev-9] CBA/FY26/results_presentation, printed p54: "Cost to income 45.5% (20bpts)"
> [ev-10] CBA/FY26/results_presentation, printed p54: "Operating income ($m) 30,224 +6.2%"
> [ev-11] CBA/FY26/results_presentation, printed p54: "Operating expenses ($m) 13,755 +5.8%"

### income_growth — "Operating income growth"
*unquantified | confidence 80/100*

Operating income grew 6.2% from $28,465m to $30,224m, driven by lending and deposit volume growth, higher earnings on replicating portfolio and capital hedges, favourable portfolio mix from growth in business lending, higher insurance income, higher CommSec equities income, and one-off gains including a milestone payment from the sale of CommInsure General Insurance and a fair value gain on Gemini IPO, partly offset by lower retail foreign exchange income.
> [ev-7] CBA/FY26/profit_announcement, printed p2: "Total operating income 30,224 28,465 6"
> [ev-10] CBA/FY26/results_presentation, printed p54: "Operating income ($m) 30,224 +6.2%"

### expense_growth — "Operating expense growth"
*unquantified | confidence 80/100*

Total operating expenses grew 5.8% from $12,996m to $13,755m. Underlying operating expenses grew 5.6% from $12,866m to $13,585m, driven by wage inflation including higher super guarantee, vendor IT inflation of 5%, higher cloud consumption and software licensing, investment in infrastructure resilience and AI capabilities, and investment in frontline and operations resources, partly offset by productivity initiatives and favourable FX. Staff expenses rose 4% to $8,258m, IT services expenses rose 16% to $2,782m, occupancy and equipment decreased 2% to $938m, and other expenses rose 4% to $1,607m.
> [ev-8] CBA/FY26/profit_announcement, printed p2: "Total operating expenses (13,755) (12,996) 6"
> [ev-15] CBA/FY26/profit_announcement, PDF p31: "Underlying operating expenses 13,585 12,866 6"
> [ev-16] CBA/FY26/profit_announcement, PDF p31: "Staff expenses 8,258 7,970 4"
> [ev-17] CBA/FY26/profit_announcement, PDF p31: "Information technology services expenses 2,782 2,389 16"
> [ev-18] CBA/FY26/profit_announcement, PDF p31: "Restructuring and notable items 170 130 31"

### notable_items — "Restructuring and notable items"
*unquantified | confidence 80/100*

Restructuring and notable items increased $40m or 31% from $130m to $170m. FY26 related to provisions for the settlement of legal proceedings in NZ, an additional goodwill payment made to certain customers as a result of ASIC's Better Banking review, and domestic customer remediation. FY25 related to domestic and NZ customer remediation as well as a Bankwest restructuring provision. This increase partially offset the improvement in underlying cost-to-income.
> [ev-18] CBA/FY26/profit_announcement, PDF p31: "Restructuring and notable items 170 130 31"
> [ev-14] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts"

## Limitations
- No explicit CTI ratio walk chart published by the bank; ppt contributions of individual drivers are unquantified and reported as null. Growth rates are taken from the bank's disclosed figures.
- The jaws effect (income growth vs expense growth) is computed from disclosed levels rather than from a bank-published CTI bridge.
- Confidence capped at 80 for quantified drivers since deltas were computed from period levels rather than read directly from a walk chart.
- Failed check: no_quantified_drivers

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T19:57:10+00:00
- seconds: 140.1
- cost_usd: 0.0479
- tokens: 1244194 in / 12051 out
- orchestration: agent
- tool_calls: 47
- pages_read: 16
- charts_read: 1
- budget_exhausted: no
