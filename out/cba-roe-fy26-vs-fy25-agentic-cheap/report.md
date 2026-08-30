# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column Full Year Ended 30 Jun 25 -> column Full Year Ended 30 Jun 26*

CBA's return on equity (cash basis) rose 50 bpts to 14.0% in FY26 from 13.5% in FY25, driven primarily by a 7.1% increase in cash NPAT ($10,982m vs $10,253m) which lifted ROE by approximately 0.96 ppt at constant equity. This was partially offset by a −0.46 ppt equity effect as average shareholders' equity grew to $78,238m from $75,710m (+3.3%), diluting the earnings gain. The bank states: "The Bank's ROE increased 50bpts to 14.0% and remains peer leading." Cash NPAT grew 7% supported by lending volume growth and broadly stable underlying NIM, partly offset by higher operating expenses and loan impairment expense.

> [ev-6] CBA/FY26/profit_announcement, PDF p9: "The Bank's ROE increased 50bpts to 14.0% and remains peer leading."
> [ev-7] CBA/FY26/profit_announcement, printed p3: "Cash basis 14.0 13.5 50 bpts 14.3 13.8 50 bpts"
> [ev-16] CBA/FY26/asx_announcement, PDF p1: "Cash net profit after tax increased 7% to $11bn"
> [ev-21] CBA/FY26/results_presentation, printed p54: "ROE (cash) 14.0% +50bpts"

## Limitations
- The ROE movement decomposition (earnings_effect and equity_effect) is an arithmetic derivation, not a bank-disclosed walk. CBA does not publish a bridge/walk chart decomposing the ROE movement into earnings and equity components.
- No primary-period ROE walk chart was found in either the results presentation or profit announcement; the bank only states the headline movement of +50bpts.
- The residual is zero by construction since only two drivers sum to the total delta.
- Failed check: no_quantified_drivers

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-30T19:47:46+00:00
- seconds: 195.3
- cost_usd: 0.0497
- tokens: 1157289 in / 9840 out
- orchestration: agent
- tool_calls: 44
- pages_read: 18
- charts_read: 0
- budget_exhausted: no
