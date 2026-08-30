# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 10982$m (+730$m) | **Attribution confidence:** 40/100

*Read from: row 'Net profit after tax from continuing operations – cash basis', column Full Year Ended 30 Jun 25 $M -> column Full Year Ended 30 Jun 26 $M*

CBA's cash NPAT from continuing operations increased $730 million or 7% to $10,982 million in FY26 (vs $10,252 million in FY25). Statutory NPAT rose $778 million or 8% to $10,911 million. The movement was driven by a $1,759 million increase in total operating income (NII up $1,563 million on 8% AIEA growth and stable underlying NIM; other operating income up $196 million), partly offset by higher underlying operating expenses ($719 million increase driven by inflation, technology investment including cloud and AI, and staff costs), a $62 million increase in loan impairment expense (retail banking +$106 million, NZ +$11 million, partially offset by Business Banking -$45 million and IB&M -$16 million), a $40 million increase in restructuring and notable items, and a $208 million increase in corporate tax expense. Total non-cash items were $116 million (FY25: $137 million), comprising hedging/IFRS volatility of $54 million and disposal/acquisition losses of $17 million.

> [ev-3] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-19] CBA/FY26/profit_announcement, printed p2: "Net profit after tax from continuing operations – cash basis 10,982 10,252 7 5,537 5,445 2"
> [ev-21] CBA/FY26/profit_announcement, printed p2: "Net profit after tax from continuing operations – statutory basis 10,911 10,133 8 5,499 5,412 2"
> [ev-23] CBA/FY26/results_presentation, printed p23: "Statutory NPAT – continuing operations 10,133 10,911"
> [ev-24] CBA/FY26/results_presentation, printed p23: "Cash NPAT – continuing operations 10,252 10,982"

## Notable items
- FY26 notable items ($170m): NZ legal proceedings settlement, ASIC Better Banking goodwill payment, domestic customer remediation
- FY25 notable items ($130m): domestic and NZ customer remediation, Bankwest restructuring provision
- Non-cash items (statutory-to-cash reconciliation): hedging/IFRS volatility ($54m loss in FY26 vs $53m gain in FY25); disposal/acquisition losses ($17m in FY26 vs $172m in FY25)

## Source disagreements
- **Statutory vs Cash NPAT movement** (definitional): Statutory NPAT increased $778m (8%) to $10,911m vs Cash NPAT increased $730m (7%) to $10,982m
  Preferred: Both movements reported: statutory +$778m and cash +$730m. The task asks for cash earnings movement. Both statutory and cash movements are material and differ by $48m due to non-cash items. Both are shown in the headline.

## Limitations
- No single walk chart decomposing the full cash NPAT movement into all six components was found; the bridge is constructed from individual component movements stated in the results tables and narrative
- The operating expenses bridge chart (page 31) sums correctly and provides sub-component detail (inflation +$455m, technology investment +$444m, frontline/operations +$128m, other +$96m, productivity -$404m)
- Tax movement computed as delta between two period columns rather than bank-stated driver contribution
- Failed check: no_quantified_drivers
- Failed check: walk_sum (start 0.0 + bars -790.0 = -790.0 != end 710.0, tol 10.0) [CBA/FY26/results_presentation PDF p24 (ev-1)]

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T14:09:06+00:00
- seconds: 187.8
- cost_usd: 0.0397
- tokens: 1234812 in / 7692 out
- orchestration: agent
- tool_calls: 45
- pages_read: 21
- charts_read: 2
- budget_exhausted: no
