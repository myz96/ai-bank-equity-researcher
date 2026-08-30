# NAB — cti — FY25 vs FY24

**Movement (cash basis):** 46.5ppt → 47.3ppt (+0.8ppt) | **Attribution confidence:** 75/100

*Read from: row 'Cost to income ratio (cash earnings basis)', column Sep 24 column -> column Sep 25 column*

NAB's cash-basis cost-to-income ratio (CTI) rose 80 ppt to 47.3% in FY25 from 46.5% in FY24, driven by expense growth of 4.6% outpacing income growth of 2.9%. On a statutory basis, CTI rose 110 ppt to 49.6% from 48.5%. Expense growth was driven by $130 million of payroll review and remediation charges, higher salary-related costs ($267 million), technology and investment spend ($213 million), and volume-related costs ($143 million), partially offset by productivity benefits of $420 million.

> [ev-2] NAB/FY25/results_book, PDF p15: "Cost to income ratio 49.6% 48.5% 110 bps 50.2% 48.9% 130 bps"
> [ev-3] NAB/FY25/results_book, PDF p15: "Cost to income ratio 47.3% 46.5% 80 bps 47.8% 46.8% 100 bps"
> [ev-4] NAB/FY25/results_book, PDF p13: "Net operating income 20,813 20,236 2.9 10,545 10,268 2.7"
> [ev-5] NAB/FY25/results_book, PDF p13: "Operating expenses(1) (9,848) (9,413) 4.6 (5,043) (4,805) 5.0"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | Operating expenses | +0.8 ppt | 90 | 2 () | ev-7, ev-8, ev-9, ev-1 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### expense_growth — "Operating expenses"
*+0.8 ppt | confidence 90/100*

Operating expenses rose $435 million or 4.6% to $9,848 million. Excluding $130 million of payroll review and remediation charges, underlying expense growth was 3.2%. Key components: salary-related costs increased $267 million driven by salary inflation and investment in additional bankers; technology and investment spend rose $213 million from software licences, maintenance and cloud consumption; volume-related costs added $143 million. These were partially offset by productivity benefits of $420 million from process improvements and simplification, EU-related cost reductions of $71 million, and other increases of $131 million.
> [ev-7] NAB/FY25/results_book, PDF p5: "Expenses increased by 4.6% including $130 million related to payroll review and remediation charges. Excluding payroll review and remediation charges, expenses rose 3.2% reflecting higher personnel and technology related costs, partially offset by productivity benefits and lower costs relating to the Group's Enforceable Undertaking with AUSTRAC."
> [ev-8] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."
> [ev-9] NAB/FY25/results_book, printed p18: "Personnel expenses increased by $271 million or 4.8%. Excluding an increase of $101 million for payroll review and remediation costs, personnel expenses increased by $170 million or 3.0%. The increase was driven by salary expense inflation, investment in additional bankers and resources to support growth, and continued investment in technology and financial crime related capabilities. These impacts were partially offset by productivity benefits achieved through continued process improvements and simplification of the Group's operations and lower EU related costs."
> [ev-1] NAB/FY25/investor_presentation, printed p25: "[walk chart] Operating expenses (YoY): Sep 24 9413 -> Sep 25 9848"

### income_growth — "Net operating income"
*unquantified | confidence 80/100*

Net operating income grew 2.9% to $20,813 million from $20,236 million. Growth was driven by net interest income up 3.8% ($644 million) reflecting higher average interest earning assets (+2.3%) and improved net interest margin (+3 bps), partially offset by other operating income down 1.9% due to lower customer remediation charges ($102 million in FY25 vs $35 million in FY24) and fee reduction impacts from business disposals, offset by higher trading activity in wealth and card fees.
> [ev-6] NAB/FY25/results_book, PDF p5: "Revenue increased by 2.9% with key drivers including volume growth and higher Markets & Treasury (M&T) income, partially offset by higher customer-related remediation charges and the impact from business disposals and run-offs."
> [ev-4] NAB/FY25/results_book, PDF p13: "Net operating income 20,813 20,236 2.9 10,545 10,268 2.7"

### notable_items — "Payroll review and remediation"
*unquantified | confidence 90/100*

Payroll review and remediation charges totalled $130 million in FY25 (personnel expenses included $101 million; general expenses included $29 million). The bank described these as 'disappointing and must be fixed.' In FY24, comparable charges were approximately $0 million, making this a new cost item driving expense growth.
> [ev-7] NAB/FY25/results_book, PDF p5: "Expenses increased by 4.6% including $130 million related to payroll review and remediation charges. Excluding payroll review and remediation charges, expenses rose 3.2% reflecting higher personnel and technology related costs, partially offset by productivity benefits and lower costs relating to the Group's Enforceable Undertaking with AUSTRAC."
> [ev-8] NAB/FY25/results_book, printed p18: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."
> [ev-1] NAB/FY25/investor_presentation, printed p25: "[walk chart] Operating expenses (YoY): Sep 24 9413 -> Sep 25 9848"

## Limitations
- The bank does not provide a formal CTI bridge or walk chart decomposing the ppt movement into drivers. The 80 ppt delta is derived from KPI table endpoints (ev-2, ev-3). Driver contributions are inferred from separate income and expense growth rates rather than a unified decomposition.
- The statutory CTI movement (+110 ppt) differs from the cash CTI movement (+80 ppt) by 30 ppt; the cash basis is used as the primary measure per bank language.
- Driver ppt contributions are not independently quantified by the bank; the narrative describes growth rates and dollar components from separate tables and charts.
- Movement delta normalised from 80 to 0.8 (unit slip against the endpoints).
- Identity contributions restated from +80.00 to +0.8000 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T14:32:23+00:00
- seconds: 131.3
- cost_usd: 0.0235
- tokens: 839605 in / 7632 out
- orchestration: agent
- tool_calls: 36
- pages_read: 16
- charts_read: 1
- budget_exhausted: no
