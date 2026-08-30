# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 80/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's headline cost-to-income ratio (Operating expenses to total operating income) rose 70 basis points to 45.9% in 1H26 from 45.2% in 1H25, driven by two offsetting forces. Underlying operations delivered a 50-bpt improvement as income growth of 6.6% outpaced underlying expense growth of 5%, lowering the underlying ratio to 44.7%. However, $170 million of restructuring and notable items in 1H26 (vs nil in 1H25) pushed total expense growth to 8.1%, well above income growth, creating negative jaws that overwhelmed the underlying improvement and lifted the headline ratio by 70 bpts.

> [ev-16] CBA/1H26/profit_announcement, printed p3: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"
> [ev-22] CBA/1H26/results_presentation, printed p53: "Cost to income 45.9% +70bpts"
> [ev-31] CBA/1H26/results_presentation, printed p53: "Cost to income 45.9% +70bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expenses | +0.7 ppt | 80 | 1 (single_source) | ev-25, ev-26, ev-27, ev-28, ev-29, ev-18 |

### expense_growth — "Operating expenses"
*+0.7 ppt | confidence 80/100*

Total operating expenses grew 8.1% ($6,890m vs $6,372m), driven by underlying expense growth of 5% ($348m increase) plus $170m of restructuring and notable items. Underlying components: staff expenses up $169m or 4% (wage inflation, investment in lenders and technology resources); IT services up $134m or 11% (cloud computing volumes, software licensing, vendor inflation, infrastructure and AI investment); other expenses up $40m or 5% (higher marketing spend); occupancy and equipment up $5m or 1%. Productivity initiatives partially offset these increases.
> [ev-25] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses were $6,720 million, an increase of $348 million or 5% on the prior comparative period."
> [ev-26] CBA/1H26/profit_announcement, PDF p31: "Staff expenses increased by $169 million or 4% to $4,139 million, mainly driven by wage inflation, and increased investment in lenders and technology resources, partly offset by productivity initiatives."
> [ev-27] CBA/1H26/profit_announcement, PDF p31: "Occupancy and equipment expenses increased by $5 million or 1% to $465 million."
> [ev-28] CBA/1H26/profit_announcement, PDF p31: "Information technology services expenses increased by $134 million or 11% to $1,321 million, primarily due to increased cloud computing volumes and software licensing, higher software and IT vendor inflation, higher amortisation and investment in infrastructure, resilience and AI capabilities, partly offset by productivity initiatives including reduction in the use of third party service providers."
> [ev-29] CBA/1H26/profit_announcement, PDF p31: "Other expenses increased by $40 million or 5% to $795 million, primarily driven by higher marketing spend."
> [ev-18] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372) 4 8"

### income_growth — "Operating income"
*unquantified | confidence 85/100*

Operating income grew 6.6% ($15,021m vs $14,097m), providing a positive jaws effect against underlying expense growth of 5%. This outpacing of underlying expenses by income drove the 50-bpt improvement in the underlying cost-to-income ratio from 45.2% to 44.7%. However, total expense growth of 8.1% including notable items exceeded income growth, resulting in net negative jaws on the headline ratio.
> [ev-17] CBA/1H26/profit_announcement, printed p2: "Total operating income 15,021 14,368 14,097 5 7"
> [ev-23] CBA/1H26/results_presentation, printed p53: "Operating income ($m) 15,021 +6.6%"

### notable_items — "Restructuring and notable items"
*unquantified | confidence 85/100*

Restructuring and notable items of $170m in 1H26 (vs nil in 1H25) widened the headline CTI by approximately 120 bpts relative to the underlying CTI. Items include provisions for NZ legal proceedings settlement, an additional goodwill payment to customers from ASIC's Better Banking review, and domestic customer remediation.
> [ev-21] CBA/1H26/profit_announcement, PDF p31: "Restructuring and notable items 170 130 – 31 n/a"
> [ev-20] CBA/1H26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.9 46.1 45.2 (20)bpts 70 bpts"

## Limitations
- No dedicated CTI walk chart published by CBA; driver contributions are inferred from separate income, expense, and notable items data rather than a single bridge.
- The ppt contribution of each driver to the headline CTI movement is computed rather than directly stated by the bank.
- The results presentation corroborates the headline figures but does not provide an independent CTI decomposition.
- Capped at 80: expense_growth +0.7 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T19:32:24+00:00
- seconds: 153.8
- cost_usd: 0.036
- tokens: 1027562 in / 9231 out
- orchestration: agent
- tool_calls: 42
- pages_read: 22
- charts_read: 3
- budget_exhausted: no
