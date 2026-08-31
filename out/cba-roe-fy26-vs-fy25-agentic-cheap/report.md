# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 75/100

*Read from: row 'ROE – cash basis (%)', column Full Year Ended 30 Jun 25 -> column Full Year Ended 30 Jun 26*

CBA's return on equity (cash basis) increased 50 bpts to 14.0% in FY26 from 13.5% in FY25. The improvement was driven by a +96 ppt earnings effect (cash NPAT grew 7% to $10,982m from $10,253m at constant average equity of $75,710m), partially offset by a −46 ppt equity effect as average equity expanded 3% to $78,238m from retained earnings funding franchise growth without share buybacks. Both contributions are derived, not disclosed by the bank. The statutory ROE also rose 50 bpts (13.4% to 13.9%).

> [ev-1] CBA/FY26/profit_announcement, PDF p147: "ROE – cash basis (%) 14.0 13.5 14.3 13.8"
> [ev-5] CBA/FY26/profit_announcement, PDF p9: "The Bank's ROE increased 50bpts to 14.0% and remains peer leading."
> [ev-8] CBA/FY26/results_presentation, printed p55: "Overview – FY26 result Key financial outcomes"
> [ev-9] CBA/FY26/results_presentation, printed p55: "Cash ROE1"
> [ev-10] CBA/FY26/results_presentation, printed p55: "13.5% 14.0%"
> [ev-11] CBA/FY26/results_presentation, printed p55: "Cash NPAT1 ($m)"
> [ev-12] CBA/FY26/results_presentation, printed p55: "10,252 10,982"
> [ev-16] CBA/FY25/profit_announcement, PDF p146: "ROE – "cash basis" (%) 13.5 13.6"
> [ev-17] CBA/FY25/profit_announcement, PDF p146: "Net profit after tax – "cash basis" 10,253 9,847"
> [ev-19] CBA/FY25/profit_announcement, PDF p9: "The Bank's ROE remained peer leading and broadly stable at 13.5%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Return on equity (cash basis) | +0.96 ppt | 80 | 2 () | ev-1, ev-2, ev-3, ev-5, ev-16, ev-17, ev-18 |
| `equity_effect` | Return on equity (cash basis) | -0.46 ppt | 80 | 2 () | ev-3, ev-13, ev-14, ev-15, ev-18 |

### earnings_effect — "Return on equity (cash basis)"
*+0.96 ppt | confidence 80/100*

Derived: cash NPAT grew 7% ($10,982m vs $10,253m, ev-2, ev-17) at constant FY25 average equity ($75,710m, ev-3, ev-18), lifting ROE by approximately 96 ppt. The bank states ROE increased 50bpts to 14.0% (ev-5, ev-7). No explicit decomposition is provided.
> [ev-1] CBA/FY26/profit_announcement, PDF p147: "ROE – cash basis (%) 14.0 13.5 14.3 13.8"
> [ev-2] CBA/FY26/profit_announcement, PDF p147: "Net profit after tax – cash basis 10,982 10,253 5,537 5,445"
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net average equity 78,238 75,710 77,968 78,004"
> [ev-5] CBA/FY26/profit_announcement, PDF p9: "The Bank's ROE increased 50bpts to 14.0% and remains peer leading."
> [ev-16] CBA/FY25/profit_announcement, PDF p146: "ROE – "cash basis" (%) 13.5 13.6"
> [ev-17] CBA/FY25/profit_announcement, PDF p146: "Net profit after tax – "cash basis" 10,253 9,847"
> [ev-18] CBA/FY25/profit_announcement, PDF p146: "Net average equity 75,710 72,517"

### equity_effect — "Return on equity (cash basis)"
*-0.46 ppt | confidence 80/100*

Derived: average equity grew 3% ($78,238m vs $75,710m, ev-3, ev-18) due to retained earnings ($10,866m net profit attributable to equity holders, ev-13) partially distributed as dividends ($7,111m total cash dividends per ev-14: interim $3,403m + final $3,708m). No share buyback occurred in FY26 (ev-14). DRP participation rates were modest (13.5%-18.1%, ev-15), adding shares but mostly neutralised via on-market purchases. This equity expansion reduced ROE by approximately 46 ppt.
> [ev-3] CBA/FY26/profit_announcement, PDF p147: "Net average equity 78,238 75,710 77,968 78,004"
> [ev-13] CBA/FY26/profit_announcement, PDF p123: "Net profit attributable to equity holders of the Bank 10,866 10,116"
> [ev-14] CBA/FY26/profit_announcement, PDF p123: "No share buy-back activity was undertaken during the year ended 30 June 2026."
> [ev-15] CBA/FY26/profit_announcement, PDF p126: "The DRP for the 2026 interim, 2025 final and 2025 interim dividends were satisfied in full by the on-market purchase and transfer of shares, and had participation rates of 13.5%, 14.8% and 18.1% respectively."
> [ev-18] CBA/FY25/profit_announcement, PDF p146: "Net average equity 75,710 72,517"

## Limitations
- No walk chart or bridge table for ROE decomposition exists in either document; both earnings_effect (+96 ppt) and equity_effect (-46 ppt) are arithmetic derivations, not disclosed by the bank.
- The bank only states the headline movement: 'ROE increased 50bpts to 14.0%' (ev-5, ev-7).
- The residual interaction term between earnings and equity effects is absorbed into the derived figures and not separately quantified.
- Identity contributions restated from +50.00 to +0.5000 ppt: the identity closes on the movement delta at the ratio's own scale and not at the scale they were written on, and a contribution larger than the ratio itself cannot be a movement of that ratio. A growth rate enters a ratio identity as a fraction, and a dollar movement enters it divided by the identity's denominator.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-31T00:58:52+00:00
- seconds: 169.4
- cost_usd: 0.0359
- tokens: 1099403 in / 9531 out
- orchestration: agent
- tool_calls: 50
- pages_read: 18
- charts_read: 0
- budget_exhausted: no
