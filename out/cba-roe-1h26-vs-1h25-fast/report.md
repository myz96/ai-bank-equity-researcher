# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROE - "cash basis" (%)', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's cash-basis return on equity rose 10 basis points to 13.8% in 1H26 from 13.7% in 1H25 (ev-2, ev-7, ev-3, ev-8). The bank states the increase was "due to higher cash NPAT being partly offset by higher net assets" (ev-2). Cash NPAT from continuing operations rose $313m or 6% to $5,445m (ev-1, ev-4), while net average equity grew from $74,176m to $78,004m (ev-5). On the statutory basis ROE was flat at 13.8% in both halves (page 168), a definitional difference from the cash-basis +10bps. The +0.1ppt movement decomposes into a +0.83ppt earnings effect (higher cash profit at constant equity) and a -0.73ppt equity effect (higher net assets), both derived arithmetically rather than disclosed.

> [ev-1] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/results_presentation, printed p53: "ROE (cash) 13.8% +10bpts"
> [ev-4] CBA/1H26/results_presentation, printed p53: "Cash NPAT ($m) 5,445 +6.1%"
> [ev-5] CBA/1H26/profit_announcement, PDF p168: "Net average equity 78,004 77,020 74,176"
> [ev-7] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-8] CBA/1H26/results_presentation, printed p54: "13.7% 13.4% 13.8% 1H25 2H25 1H26"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | higher cash NPAT | +0.83 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-7 |
| `equity_effect` | higher net assets | -0.73 ppt | 80 | 1 (single_source) | ev-2, ev-5 |
| *residual (unexplained)* | — | +0 ppt | — | — | — |

### earnings_effect — "higher cash NPAT"
*+0.83 ppt | confidence 80/100*

Derived, not disclosed: prior-period ROE (13.7%) x cash NPAT growth (6.08% as a fraction, from $5,133m to $5,445m) = +0.83ppt at constant equity. The bank confirms the direction: ROE rose "due to higher cash NPAT" (ev-2). Cash NPAT from continuing operations increased $313m or 6% to $5,445m (ev-1).
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-7] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect — "higher net assets"
*-0.73 ppt | confidence 80/100*

Derived, not disclosed: total delta (+0.1ppt) minus earnings effect (+0.83ppt) = -0.73ppt. Direction supported by the bank's statement that higher cash NPAT was "partly offset by higher net assets" (ev-2) and by net average equity rising from $74,176m to $78,004m, +5.16% (ev-5).
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-5] CBA/1H26/profit_announcement, PDF p168: "Net average equity 78,004 77,020 74,176"

## Source disagreements
- **ROE movement by basis** (definitional): cash +10bps (13.7 to 13.8) vs statutory flat (13.8 to 13.8)
  Preferred: cash basis +10bps. The task's headline measure is cash-basis ROE, which rose 10bps. The statutory-basis ROE (continuing operations) was flat at 13.8% in both 1H25 and 1H26 (page 168). The difference reflects the cash/statutory NPAT reconciliation.

## Limitations
- The earnings and equity effects are arithmetic derivations from the disclosed ROE endpoints and the disclosed cash NPAT growth rate; the bank does not publish a quantified ROE bridge. The bank's own narrative (ev-2) confirms only the direction of each effect, not its magnitude.
- The equity effect is computed as the residual (total delta minus earnings effect) and includes the interaction term; its direction is supported by the disclosed net average equity growth and the bank's 'partly offset by higher net assets' statement, but the bank does not separately quantify retained earnings, buybacks or DRP treatment.
- The earnings growth rate used (6.08%) is computed from the disclosed $5,133m and $5,445m cash NPAT levels; the bank's rounded stated growth is 6% (ev-1) and 6.1% (ev-4).

## Provenance
- combo: fast
- models: agent=deepseek/deepseek-v4-flash-0731, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-09-01T17:12:42+00:00
- seconds: 52.5
- cost_usd: 0.0035
- tokens: 175537 in / 7759 out
- latency: 12 calls, 52s in requests (slowest 10s), 0 retries, 0 grace waits, 0s slept
- orchestration: agent
- tool_calls: 21
- pages_read: 5
- charts_read: 0
- budget_exhausted: no
