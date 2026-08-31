# WBC — roe — FY25 vs FY24

**Movement (ex_notables basis):** 11.21ppt → 10.97ppt (-0.24ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROTE ex Notable Items', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's ROTE ex Notable Items fell 24 basis points (from 11.21% to 10.97%) in FY25 vs FY24. The decline was driven almost entirely by a ~2% fall in net profit excluding Notable Items ($7,106m to $6,966m), which at constant equity would have lowered ROTE by approximately 22 ppt. Average tangible ordinary equity was essentially unchanged ($63,415m to $63,476m, +$61m or 0.1%), contributing a further ~2 ppt headwind as the small equity increase interacted with lower earnings. The near-flat equity reflected high dividend payout (75% ex Notable Items) and on-market share buybacks that offset retained earnings.

> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-4] WBC/FY25/investor_discussion_pack, printed p6: "11.0% ROTE ex Notable Items1 24bps to FY24"
> [ev-29] WBC/FY25/investor_discussion_pack, printed p37: "Return on tangible equity ex Notable Items, down 24 bps"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Movement in cash earnings at constant equity | -0.221 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-22, ev-23 |
| `equity_effect` | Movement in average equity at constant earnings | -0.019 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-9, ev-11, ev-26 |
| *residual (unexplained)* | — | -0.02 ppt | — | — |

### earnings_effect — "Movement in cash earnings at constant equity"
*-0.221 ppt | confidence 80/100*

Derived contribution: prior-period ROTE (11.21%) multiplied by the earnings growth rate of -1.97% ((6,966−7,106)/7,106). Net profit excluding Notable Items fell 2% to $6,972m (statutory basis, incl NCI) or $6,966m (ex NCI, adj RSP), as higher operating income (+3% revenue) and lower impairment charges (5bps vs 7bps of avg loans) were more than offset by 9% higher expenses including a $273m restructuring charge under the Fit for Growth program.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-2] WBC/FY25/results_announcement, PDF p58: "Net profit attributable to owners of WBC (adjusted for RSP dividends) excluding Notable Items 6,966 7,106"
> [ev-22] WBC/FY25/results_announcement, PDF p9: "Net profit excluding Notable Items 6,972 7,113 (2)"
> [ev-23] WBC/FY25/results_announcement, PDF p9: "Net profit excluding Notable Items was $6,972 million, a decrease of 2%, with higher operating income and lower credit impairment charges more than offset by higher expenses."

### equity_effect — "Movement in average equity at constant earnings"
*-0.019 ppt | confidence 80/100*

Derived contribution: total delta (−24 ppt) minus earnings effect (−22.1 ppt). Average tangible ordinary equity rose only $61m (0.1%) from $63,415m to $63,476m, as intangible assets amortised ($10,758m→$10,586m) partially offset by software capitalisation. Ordinary equity was flat ($71,493m→$71,544m). Weighted average shares fell 2% (3,476m→3,422m) due to on-market buybacks. The 75% dividend payout ratio ex Notable Items limited retained earnings accumulation, and the final dividend DRP was satisfied via market purchases rather than new issuance, preventing dilutive equity growth.
> [ev-1] WBC/FY25/results_announcement, PDF p10: "ROTE 10.97% 11.21% (24 bps)"
> [ev-3] WBC/FY25/results_announcement, PDF p58: "Average tangible ordinary equity 63,476 63,415"
> [ev-9] WBC/FY25/results_announcement, PDF p31: "Total ordinary dividend (cents per share) 153 151 1"
> [ev-11] WBC/FY25/results_announcement, PDF p29: "Capital return: 2 basis points reduction due to the on market share buyback."
> [ev-26] WBC/FY25/results_announcement, PDF p10: "Weighted average ordinary shares (millions) 3,422 3,476"

## Limitations
- The earnings_effect and equity_effect are arithmetic derivations, not disclosed by the bank. No walk chart decomposing the ROTE movement exists in either document.
- The residual of -0.02 ppt is rounding noise from the derivation.
- No primary-period ROTE bridge/walk chart was found; the driver table relies on the identity decomposition method specified in the task.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Movement endpoints converted from basis points (1121, 1097) to ppt: the evidence prints this ratio as 11.21% and 10.97%, and the unit for this metric is ppt. A change column printed in basis points is divided by 100 to enter a movement stated in points.
- Identity contributions restated from -24.00 to -0.2400 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-31T00:37:41+00:00
- seconds: 174.8
- cost_usd: 0.0502
- tokens: 1329158 in / 10676 out
- orchestration: agent
- tool_calls: 52
- pages_read: 15
- charts_read: 2
- budget_exhausted: no
