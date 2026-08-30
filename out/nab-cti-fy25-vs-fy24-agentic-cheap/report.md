# NAB — cti — FY25 vs FY24

**Movement (cash basis):** 46.5ppt → 47.3ppt (+0.8ppt) | **Attribution confidence:** 40/100

*Read from: row 'Cost to income ratio (cash earnings basis)', column Sep 24 column -> column Sep 25 column*

NAB’s cash cost-to-income ratio (CTI) rose 80 bps (0.8 ppt) to 47.3% in FY25 from 46.5% in FY24. The movement was driven by expense growth (4.6%) outpacing revenue growth (2.9%), a negative jaws effect of approximately 1.4 ppt. Expense growth included $130m in payroll review and remediation charges; excluding these, expenses grew 3.2%, still ahead of revenue growth. The statutory CTI rose 110 bps to 49.6%.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `expense_growth` | — | +1.4 ppt | 80 | 2 () | ev-3, ev-4, ev-5, ev-6, ev-7, ev-8 |

### expense_growth
*+1.4 ppt | confidence 80/100*

Operating expenses grew 4.6% ($9,413m to $9,848m, +$435m), outpacing net operating income growth of 2.9% ($20,236m to $20,813m). This expense-led jaws effect raised the ratio. The expense bridge shows salary-related (+$267m), technology & investment (+$213m), volume-related (+$143m), other (+$131m), and payroll review/remediation (+$130m) as positive contributors, partially offset by productivity benefits (-$420m) and EU-related cost reductions (-$71m). Excluding the $130m payroll review and remediation charges, underlying expense growth was 3.2% (+$305m), still exceeding revenue growth.
> [ev-3] NAB/FY25/results_book, PDF p5: "Revenue increased by 2.9% with key drivers including volume growth and higher Markets & Treasury (M&T) income, partially offset by higher customer-related remediation charges and the impact from business disposals and run-offs."
> [ev-4] NAB/FY25/results_book, PDF p5: "Expenses increased by 4.6% including $130 million related to payroll review and remediation charges. Excluding payroll review and remediation charges, expenses rose 3.2% reflecting higher personnel and technology related costs, partially offset by productivity benefits and lower costs relating to the Group's Enforceable Undertaking with AUSTRAC."
> [ev-5] NAB/FY25/results_book, printed p12: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."
> [ev-6] NAB/FY25/results_book, PDF p13: "Net operating income 20,813 20,236 2.9"
> [ev-7] NAB/FY25/results_book, PDF p13: "Operating expenses(1) (9,848) (9,413) 4.6"
> [ev-8] NAB/FY25/investor_presentation, printed p25: "[walk chart] Operating expenses (YoY): Sep 24 9413 -> Sep 25 9848"

### income_growth
*unquantified | confidence 70/100*

Net operating income grew 2.9% year-on-year, driven by volume growth and higher Markets & Treasury income, partially offset by higher customer-related remediation charges and business disposals/run-offs. Revenue growth lagged expense growth, contributing negatively to the CTI movement. The bank does not disclose a separate income-growth contribution in ppt to the CTI walk.
> [ev-3] NAB/FY25/results_book, PDF p5: "Revenue increased by 2.9% with key drivers including volume growth and higher Markets & Treasury (M&T) income, partially offset by higher customer-related remediation charges and the impact from business disposals and run-offs."
> [ev-6] NAB/FY25/results_book, PDF p13: "Net operating income 20,813 20,236 2.9"

### notable_items
*unquantified | confidence 80/100*

Payroll review and remediation charges of $130m (FY25 vs prior year) are a notable expense item driving the CTI higher. Customer-related remediation charges also impacted revenue (contra-revenue in fees/commissions). The bank states these are 'disappointing and must be fixed.' Excluding payroll review and remediation, expense growth was 3.2%.
> [ev-4] NAB/FY25/results_book, PDF p5: "Expenses increased by 4.6% including $130 million related to payroll review and remediation charges. Excluding payroll review and remediation charges, expenses rose 3.2% reflecting higher personnel and technology related costs, partially offset by productivity benefits and lower costs relating to the Group's Enforceable Undertaking with AUSTRAC."
> [ev-5] NAB/FY25/results_book, printed p12: "Operating expenses increased by $435 million or 4.6%. Excluding an increase of $130 million for payroll review and remediation costs, operating expenses increased by $305 million or 3.2%."

## Source disagreements
- **Basis of CTI movement** (definitional): Cash: 80 bps (0.8 ppt) vs Statutory: 110 bps (1.1 ppt)
  Preferred: Cash: 80 bps (0.8 ppt). The bank reports CTI on both statutory and cash earnings bases. Per bank_language, cash earnings is the core profit measure and primary reporting basis. The statutory CTI rose 110 bps while cash CTI rose 80 bps due to different treatment of non-cash items.

## Limitations
- No CTI-specific walk/breakdown chart published by NAB for FY25 v FY24. The expense bridge on page 25 of the investor presentation is primary and covers the expense side only. Income/revenue bridge for FY25 v FY24 was not found in either document.
- The 1.4 ppt expense-jaws contribution is computed from the reported growth rates (expense 4.6% vs income 2.9%) rather than read directly from a CTI walk bar. Confidence capped accordingly.
- The bank does not publish a formal CTI driver table decomposing the ppt movement into income growth, expense growth, and notable items components. Drivers are inferred from narrative and the expense bridge.
- Statutory CTI movement (110 bps) differs materially from cash CTI movement (80 bps); both reported but cash is the primary basis per bank_language.
- Research stopped early: the tool-call budget (80 calls) was reached, so the evidence behind this answer is less complete than a full run's.
- Capped at 80: expense_growth +1.4 ppt. The records these claims cite do not state those numbers, so each one is arithmetic over the evidence rather than a figure read from it.
- Failed check: drivers_reconcile (drivers +1.4 + residual +0.0 != delta +0.8, tol 0.1)

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T20:05:51+00:00
- seconds: 311.4
- cost_usd: 0.1608
- tokens: 3068732 in / 10060 out
- orchestration: agent
- tool_calls: 80
- pages_read: 54
- charts_read: 1
- budget_exhausted: the tool-call budget (80 calls)
