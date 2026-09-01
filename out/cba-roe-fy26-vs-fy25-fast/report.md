# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.5ppt → 14ppt (+0.5ppt) | **Attribution confidence:** 85/100

*Read from: row 'Return on equity (ROE) cash basis', column Full Year Ended 30 Jun 25 -> column Full Year Ended 30 Jun 26*

CBA's cash-basis return on equity rose 50 basis points to 14.0% in FY26 from 13.5% in FY25 (continuing operations). The bank states the increase was driven by higher cash NPAT, partly offset by higher net assets. Cash NPAT from continuing operations rose $730m or 7% to $10,982m, while average net equity grew from $75,710m to $78,238m. The statutory-basis ROE also rose 50 bpts to 13.9% from 13.4%. The FY25 profit announcement corroborates the FY25 cash ROE of 13.5%, and the results presentation shows CBA's FY26 cash ROE of 14.0%.

> [ev-1] CBA/FY26/profit_announcement, printed p3: "Return on equity (ROE) (%) ¹ Statutory basis 13.9 13.4 50 bpts 14.2 13.8 40 bpts Cash basis 14.0 13.5 50 bpts 14.3 13.8 50 bpts"
> [ev-2] CBA/FY26/profit_announcement, PDF p146: "Net average equity 78,238 75,710 77,968 78,004 Net profit after tax – cash basis 10,982 10,252 5,537 5,445 ROE – cash basis (%) 14.0 13.5 14.3 13.8"
> [ev-3] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-4] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-6] CBA/FY25/profit_announcement, printed p3: "Return on equity (ROE) (%) ¹ Statutory basis 13.4 13.1 30 bpts 13.1 13.8 (70)bpts Cash basis 13.5 13.6 (10)bpts 13.4 13.7 (30)bpts"
> [ev-8] CBA/FY26/results_presentation, printed p38: "14.0% 9.8% 10.6% 8.5% CBA Peer 3 Peer 1 Peer 2"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Higher cash NPAT | +0.95 ppt | 80 | 2 () | ev-3, ev-5, ev-2 |
| `equity_effect` | Higher net assets | -0.45 ppt | 80 | 1 (single_source) | ev-4, ev-2 |
| *residual (unexplained)* | — | +0 ppt | — | — | — |

### earnings_effect — "Higher cash NPAT"
*+0.95 ppt | confidence 80/100*

Derived, not disclosed: prior-period ROE (13.5%) x cash NPAT growth (7%) = +0.95 ppt at constant equity. Cash NPAT from continuing operations rose $730m or 7% to $10,982m, driven by a 6% increase in operating income and a 6% increase in operating expenses, plus a $62m increase in loan impairment expense.
> [ev-3] CBA/FY26/profit_announcement, printed p3: "Cash net profit after tax (cash NPAT or cash profit) from continuing operations increased $730 million or 7% on the prior year to $10,982 million."
> [ev-5] CBA/FY26/results_presentation, printed p24: "Cash NPAT 10,982 7.1% 1.7%"
> [ev-2] CBA/FY26/profit_announcement, PDF p146: "Net average equity 78,238 75,710 77,968 78,004 Net profit after tax – cash basis 10,982 10,252 5,537 5,445 ROE – cash basis (%) 14.0 13.5 14.3 13.8"

### equity_effect — "Higher net assets"
*-0.45 ppt | confidence 80/100*

Derived, not disclosed: total delta (+0.5 ppt) minus earnings effect (+0.95 ppt) = -0.45 ppt. Direction confirmed by the bank: 'higher cash NPAT being partly offset by higher net assets.' Average net equity grew from $75,710m to $78,238m, consistent with retained earnings (cash NPAT ~$11bn less ~$8.5bn dividends).
> [ev-4] CBA/FY26/profit_announcement, printed p3: "Return on equity (cash basis) increased 50 basis points to 14.0% with higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/FY26/profit_announcement, PDF p146: "Net average equity 78,238 75,710 77,968 78,004 Net profit after tax – cash basis 10,982 10,252 5,537 5,445 ROE – cash basis (%) 14.0 13.5 14.3 13.8"

## Notable items
- Statutory-basis ROE also rose 50 bpts to 13.9% from 13.4% (ev-1)

## Limitations
- The earnings_effect and equity_effect contributions are arithmetic derivations (prior-period ROE x earnings growth; total delta minus earnings effect), not figures the bank discloses as a split. The bank discloses only the total +50 bpts movement and its qualitative attribution ('higher cash NPAT being partly offset by higher net assets').
- The earnings growth rate used (7%) is the bank's stated rounded figure from the profit announcement; the results presentation prints 7.1%. Using 7.1% would give earnings_effect of +0.96 ppt and equity_effect of -0.46 ppt, immaterially different.
- No waterfall/bridge chart of the ROE movement was found in either document; the split is derived from the disclosed ROE endpoints and earnings growth rather than read from a bank-published walk.
- The equity_effect direction is supported by the bank's own statement and the disclosed average equity growth, but the bank does not quantify the split between retained earnings, buybacks and DRP treatment.
- The results presentation does not print a full KPI table with the FY26 vs FY25 ROE columns; page 38 corroborates only the FY26 level of 14.0% (ev-8). The FY26 vs FY25 ROE movement is read from the profit announcement KPI table (ev-1).

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-09-01T17:33:25+00:00
- seconds: 64.2
- cost_usd: 0.0043
- tokens: 228451 in / 10437 out
- latency: 13 calls, 64s in requests (slowest 13s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 22
- pages_read: 7
- charts_read: 0
- budget_exhausted: no
