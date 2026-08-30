# CBA — impairment — FY26 vs FY25

**Movement (cash basis):** 726$m → 788$m (+62$m) | **Attribution confidence:** 75/100

*Read from: row 'Total loan impairment expense', column Full Year Ended 30 Jun 25 $M -> column Full Year Ended 30 Jun 26 $M*

CBA’s credit impairment charge (loan impairment expense) rose to $788 million in FY26 from $726 million in FY25, an increase of $62 million (9%). The loss rate against average gross loans and acceptances increased 1 bps to 8 bps. The movement was driven by higher net collective provision funding (+$150m), partially offset by lower write-backs of individually assessed provisions (more negative by $71m) and roughly flat net new/individual provisioning (-$17m). Divisionally, Retail Banking Services drove the increase (+$106m to $378m), partly offset by decreases in Business Banking (-$45m to $310m) and Institutional Banking & Markets (-$16m to $33m), with a smaller increase in New Zealand (+$11m to $66m).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `collective.volume` | — | +150 $m | 85 | 1 (single_source) | ev-1, ev-2 |
| `individual_provisions` | — | -17 $m | 85 | 1 (single_source) | ev-1, ev-2 |
| `write_backs_recoveries` | — | -71 $m | 85 | 1 (single_source) | ev-1 |

### collective.volume
*+150 $m | confidence 85/100*

Net collective provision funding increased $150 million to $606 million (from $456 million in FY25). The bank attributes higher collective provisions to portfolio growth, increased geopolitical risk, and macroeconomic uncertainty across both consumer and corporate segments. Corporate collective provisions grew $172 million to $2,797 million, while consumer collective provisions fell $48 million to $2,888 million due to rising house prices and more targeted FLAs for higher-risk cohorts, partly offset by higher arrears and cost-of-living pressures.
> [ev-1] CBA/FY26/results_presentation, printed p29: "[walk chart] Loan impairment expense: FY25 72.60000000000001 -> FY26 78.80000000000001"
> [ev-2] CBA/FY26/results_presentation, printed p24: "[walk chart] CBA credit impairment charge in FY26 vs FY25: FY25 0.0 -> FY26 0.071"

### individual_provisions
*-17 $m | confidence 85/100*

Net new and increased individual provisioning decreased $17 million to $422 million (from $439 million in FY25). Consumer individually assessed provisions decreased $19 million to $97 million, and corporate individually assessed provisions decreased $6 million to $694 million, driven by write-backs and write-offs.
> [ev-1] CBA/FY26/results_presentation, printed p29: "[walk chart] Loan impairment expense: FY25 72.60000000000001 -> FY26 78.80000000000001"
> [ev-2] CBA/FY26/results_presentation, printed p24: "[walk chart] CBA credit impairment charge in FY26 vs FY25: FY25 0.0 -> FY26 0.071"

### write_backs_recoveries
*-71 $m | confidence 85/100*


> [ev-1] CBA/FY26/results_presentation, printed p29: "[walk chart] Loan impairment expense: FY25 72.60000000000001 -> FY26 78.80000000000001"

### other_unmapped
*unquantified | confidence 70/100*

Divisional movements not fully explained by provision-type drivers: Retail +$106m to $378m (driven by geopolitical risk, macro uncertainty, cost-of-living); NZ +$11m to $66m (higher collective provisions from unemployment outlook deterioration); Business Banking -$45m to $310m (lower individual charges, higher collective from growth/geopolitical); IB&M -$16m to $33m (release of individual provisions, higher collective). Corporate Centre showed a benefit of $1m vs $(5)m prior year. These divisional deltas sum to $62m total movement.
> [ev-2] CBA/FY26/results_presentation, printed p24: "[walk chart] CBA credit impairment charge in FY26 vs FY25: FY25 0.0 -> FY26 0.071"

## Limitations
- No walk/bridge chart with quantified bars for the FY26 vs FY25 impairment movement was found in the results presentation; the bridge is built from the provision-type table on page 118 of the profit announcement.
- The provision-type components (net collective funding +$150m, net individual +$422m, write-backs -$240m) sum to $332m, which does not equal the $62m total movement. This is because the table includes all components but the 'Total loan impairment expense' line also implicitly captures other items like discount unwind, write-offs, recoveries, and other adjustments that are part of the provision rollforward but not separately listed in the LIE table. The $62m movement is the stated figure.
- Divisional breakdown provides the where-layer but the provision-type bridge does not decompose by division, so there is no direct mapping between provision-type drivers and divisional movements.
- Confidence is limited by the absence of a primary walk chart with summed bars; the driver contributions are derived from the provision-type table deltas rather than a published bridge.
- Research stopped early: the tool-call budget (40 calls) was reached, so the evidence behind this answer is less complete than a full run's.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T12:59:56+00:00
- seconds: 142.2
- cost_usd: 0.0318
- tokens: 987865 in / 4671 out
- orchestration: agent
- tool_calls: 40
- pages_read: 23
- charts_read: 3
- budget_exhausted: the tool-call budget (40 calls)
