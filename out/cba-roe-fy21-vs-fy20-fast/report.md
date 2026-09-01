# CBA — roe — FY21 vs FY20

**Movement (cash basis):** 10.2ppt → 11.5ppt (+1.3ppt) | **Attribution confidence:** 90/100

*Read from: row 'ROE - cash basis (%)', column 30 Jun 20 column, continuing operations -> column 30 Jun 21 column, continuing operations*

CBA's cash-basis return on equity (continuing operations) rose 1.3 ppt in FY21, from 10.2% in FY20 to 11.5% in FY21 (ev-3, ev-6). The bank states ROE "increased 130 basis points to 11.5% due to the impact of higher profit (approximately 200 basis points), partly offset by an increase in capital levels (approximately 70 basis points)" (ev-2). Cash NPAT from continuing operations rose $1,428m or 19.8% to $8,653m (ev-1). Applying the task's identity: earnings_effect = 10.2% × 0.198 ≈ +2.0 ppt; equity_effect = 1.3 − 2.0 ≈ −0.7 ppt. These derived contributions match the bank's own stated split. The statutory-basis ROE also rose, from 10.4% to 11.8% (ev-3).

> [ev-3] CBA/FY21/profit_announcement, PDF p155: "ROE - "cash basis" (%) 11. 5 10. 2 12. 6 10. 5"
> [ev-6] CBA/FY21/results_presentation, printed p57: "10.2% 11.5% FY20 FY21 (4)bpts +130bpts"
> [ev-2] CBA/FY21/profit_announcement, PDF p30: "Return on equity ("cash basis") increased 130 basis points to 11.5% due to the impact of higher profit (approximately 200 basis points), partly offset by an increase in capital levels (approximately 70 basis points)."
> [ev-1] CBA/FY21/profit_announcement, PDF p30: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $1,428 million or 19.8% on the prior year to $8,653 million."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | Higher profit | +2 ppt | 90 | 1 (single_source) | ev-2, ev-1, ev-3, ev-4 |
| `equity_effect` | Increase in capital levels | -0.7 ppt | 90 | 1 (single_source) | ev-2, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — | — |

### earnings_effect — "Higher profit"
*+2 ppt | confidence 90/100*

Derived, not disclosed: earnings_effect = prior-period ROE (10.2%) × cash NPAT growth (19.8% as fraction 0.198) ≈ +2.0 ppt. The bank states ROE rose due to "the impact of higher profit (approximately 200 basis points)" (ev-2). Cash NPAT from continuing operations increased $1,428m or 19.8% to $8,653m (ev-1), driven by a 1.7% rise in operating income, a 3.3% rise in operating expenses and a $1,964m decrease in loan impairment expense (ev-1).
> [ev-2] CBA/FY21/profit_announcement, PDF p30: "Return on equity ("cash basis") increased 130 basis points to 11.5% due to the impact of higher profit (approximately 200 basis points), partly offset by an increase in capital levels (approximately 70 basis points)."
> [ev-1] CBA/FY21/profit_announcement, PDF p30: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $1,428 million or 19.8% on the prior year to $8,653 million."
> [ev-3] CBA/FY21/profit_announcement, PDF p155: "ROE - "cash basis" (%) 11. 5 10. 2 12. 6 10. 5"
> [ev-4] CBA/FY21/profit_announcement, PDF p155: "Net profit after tax - "cash basis" 8,653 7,225 4,785 3,868"

### equity_effect — "Increase in capital levels"
*-0.7 ppt | confidence 90/100*

Derived, not disclosed: equity_effect = total delta (1.3 ppt) − earnings_effect (2.0 ppt) ≈ −0.7 ppt. The bank states ROE was "partly offset by an increase in capital levels (approximately 70 basis points)" (ev-2). Net average equity rose from $70,833m to $75,187m (ev-5), so higher equity at constant earnings dilutes ROE, consistent with the negative contribution.
> [ev-2] CBA/FY21/profit_announcement, PDF p30: "Return on equity ("cash basis") increased 130 basis points to 11.5% due to the impact of higher profit (approximately 200 basis points), partly offset by an increase in capital levels (approximately 70 basis points)."
> [ev-5] CBA/FY21/profit_announcement, PDF p155: "Net average equity 75,187 70,833 76,814 73,424"

## Notable items
- ROE cash basis (continuing operations) is the headline measure; statutory-basis ROE rose from 10.4% to 11.8% (ev-3)

## Source disagreements
- **FY20 cash ROE and cash NPAT comparatives** (restatement): FY20 ROE 10.3% / cash NPAT $7,296m (FY20 profit announcement, ev-8) vs FY20 ROE 10.2% / cash NPAT $7,225m (FY21 profit announcement, ev-3, ev-4)
  Preferred: FY21 document restated figures (10.2% / $7,225m). The FY21 profit announcement restated FY20 comparatives to conform to current-period presentation (page 155 note: 'Comparative information has been restated to conform to presentation in the current period'). Per source hierarchy, the newer document's restated comparatives win.

## Limitations
- No dedicated ROE walk/bridge chart exists in either document; the bank's decomposition is stated in narrative on profit announcement page 30 (ev-2). The two driver contributions are derived via the task's identity and match the bank's stated split (+200bps profit, -70bps capital).
- The equity_effect direction is supported by the increase in net average equity (ev-5) and the bank's own 'increase in capital levels' wording (ev-2); the bank does not separately quantify retained earnings, buyback or DRP effects on average equity.
- The FY20 document's originally-reported ROE (10.3%) and cash NPAT ($7,296m) differ from the FY21 restated comparatives (10.2% / $7,225m); the restated figures are used.

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-09-01T18:05:05+00:00
- seconds: 88.9
- cost_usd: 0.0053
- tokens: 277169 in / 14440 out
- latency: 16 calls, 88s in requests (slowest 16s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 25
- pages_read: 8
- charts_read: 0
- budget_exhausted: no
