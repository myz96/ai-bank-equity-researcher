# CBA — cti — 1H26 vs 1H25

**Movement (cash basis):** 45.2ppt → 45.9ppt (+0.7ppt) | **Attribution confidence:** 40/100

*Read from: row 'Operating expenses to total operating income (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA’s cost-to-income ratio (operating expenses to total operating income) rose 70 basis points to 45.9% in 1H26 from 45.2% in 1H25, on cash basis. Operating income grew 6.6% year-on-year to $15,021 million, while operating expenses grew 8.1% to $6,890 million. Expense growth outpaced income growth, driven by wage inflation, increased technology spend, and $170 million in restructuring and notable items (absent in 1H25). Underlying cost-to-income (excluding notable items) improved 50 basis points to 44.7%, reflecting strong cumulative cost savings of $1,207 million over seven years.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expense growth | +5.9 ppt | 90 | 2 () | ev-20, ev-21, ev-22, ev-23, ev-24, ev-25, ev-26, ev-27, ev-28, ev-29 |
| `income_growth` | Operating income growth | -1 ppt | 80 | 2 () | ev-4, ev-30 |
| `notable_items` | Restructuring and notable items | +1.1 ppt | 85 | 1 (single_source) | ev-6, ev-7 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expense growth"
*+5.9 ppt | confidence 90/100*

Operating expenses grew 8.1% YoY ($6,372M to $6,890M), driven by inflation (+$275M, mainly wage inflation including higher super guarantee and vendor IT inflation of +5%), investment in technology (+$222M, for cloud consumption, software licensing, infrastructure, resilience and AI capabilities), and investment in frontline and operations (+$78M). Partially offset by productivity savings (-$221M) and other (-$6M). The bank states: "Inflation, investment in technology and proprietary distribution driving higher expense growth" (p28).
> [ev-20] CBA/1H26/results_presentation, printed p28: "Inflation, investment in technology and proprietary distribution driving higher expense growth"
> [ev-21] CBA/1H26/results_presentation, printed p28: "Inflation, investment in technology and proprietary distribution driving higher expense growth"
> [ev-22] CBA/1H26/results_presentation, printed p28: "Inflation, investment in technology and proprietary distribution driving higher expense growth"
> [ev-23] CBA/1H26/results_presentation, printed p28: "Underlying cost to income: 45.2%"
> [ev-24] CBA/1H26/results_presentation, printed p28: "Contribution to mvt:"
> [ev-25] CBA/1H26/results_presentation, printed p28: "(3.4%) +4.3% +3.5% +1.2%"
> [ev-26] CBA/1H26/profit_announcement, PDF p31: "Underlying operating expenses were $6,720 million, an increase of $348 million or 5% on the prior comparative period."
> [ev-27] CBA/1H26/profit_announcement, PDF p31: "Staff expenses increased by $169 million or 4% to $4,139 million, mainly driven by wage inflation, and increased investment in lenders and technology resources"
> [ev-28] CBA/1H26/profit_announcement, PDF p31: "Information technology services expenses increased by $134 million or 11% to $1,321 million, primarily due to increased cloud computing volumes and software licensing, higher software and IT vendor inflation, higher amortisation and investment in infrastructure, resilience and AI capabilities"
> [ev-29] CBA/1H26/profit_announcement, PDF p31: "Other expenses increased by $40 million or 5% to $795 million, primarily driven by higher marketing spend."

### income_growth — "Operating income growth"
*-1 ppt | confidence 80/100*

Operating income grew 6.6% YoY ($14,097M to $15,021M), providing a partial offset to expense growth. Net interest income benefited from average lending volume growth of +7.0% and average deposit volume growth of +8.4%, partly offset by margin compression. Other operating income grew 8% driven by higher commissions (+6%), trading income (+16%), and lending fees (+4%).
> [ev-4] CBA/1H26/profit_announcement, printed p2: "Total operating income 15,021 14,368 14,097 5 7"
> [ev-30] CBA/1H26/results_presentation, printed p24: "Operating income 15,021 6.6% 4.5%"

### notable_items — "Restructuring and notable items"
*+1.1 ppt | confidence 85/100*

Restructuring and notable items of $170M in 1H26 versus $0 in 1H25, adding to operating expenses. Items include provisions for NZ legal proceedings settlement, additional goodwill payment to customers from ASIC's Better Banking review, and domestic customer remediation.
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Restructuring and notable items ¹ (170) (130) – 31 n/a"
> [ev-7] CBA/1H26/profit_announcement, printed p2: "Total operating expenses (6,890) (6,624) (6,372) 4 8"

## Limitations
- Movement delta normalised from 7.0 to 0.7 (unit slip against the endpoints).
- Failed check: drivers_reconcile (drivers +6.0 + residual +0.0 != delta +0.7, tol 1.0)

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T13:54:06+00:00
- seconds: 224.7
- cost_usd: 0.0633
- tokens: 1919519 in / 12047 out
- orchestration: agent
- tool_calls: 67
- pages_read: 33
- charts_read: 2
- budget_exhausted: no
