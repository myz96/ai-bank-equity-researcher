# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (ROE) (%) Cash basis', column 31 Dec 24 column -> column 31 Dec 25 column*

CBA's return on equity (cash basis) increased 10 bpts to 13.8% in 1H26 vs 13.7% in 1H25. The movement was driven by a positive earnings effect from 6% growth in cash NPAT ($5,445m, up $313m on $5,132m), which lifted ROE at constant equity. This was partially offset by a negative equity effect as average net assets grew 5% to $78.0bn from $74.2bn, diluting the return. The bank stated: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets" (p26).

> [ev-2] CBA/1H26/profit_announcement, PDF p19: "Cash basis 13.8 13.4 13.7 40 bpts 10 bpts"
> [ev-5] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-17] CBA/1H26/results_presentation, printed p53: "ROE (cash) 13.8% +10bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | higher cash NPAT | +0.8 ppt | 80 | 1 (single_source) | ev-2, ev-5, ev-6, ev-7 |
| `equity_effect` | higher net assets | -0.7 ppt | 80 | 1 (single_source) | ev-2, ev-6, ev-9, ev-10, ev-11, ev-12, ev-13, ev-14 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "higher cash NPAT"
*+0.8 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) × earnings growth fraction (6.1%, from $313m/$5,132m cash NPAT increase per ev-5 and ev-7). At constant equity, the 6% profit lift would have added ~0.8 ppt to ROE. The bank attributes the ROE increase to 'higher cash NPAT' (ev-6).
> [ev-2] CBA/1H26/profit_announcement, PDF p19: "Cash basis 13.8 13.4 13.7 40 bpts 10 bpts"
> [ev-5] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-7] CBA/1H26/profit_announcement, PDF p166: "Net profit after tax - "cash basis" 5,445 5,120 5,132"

### equity_effect — "higher net assets"
*-0.7 ppt | confidence 80/100*

Derived: total delta (0.1 ppt) minus earnings effect (0.8 ppt) = -0.7 ppt. Average net assets grew from $74,176m to $78,004m (+5.2%), diluting ROE. Driven by retained earnings ($5,367m net profit to retained profits per ev-10) partly distributed via dividends ($3,708m cash + $643m DRP per ev-11, ev-12), with no share buybacks in 1H26 (ev-9). The bank notes the increase was 'partly offset by higher net assets' (ev-6).
> [ev-2] CBA/1H26/profit_announcement, PDF p19: "Cash basis 13.8 13.4 13.7 40 bpts 10 bpts"
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-9] CBA/1H26/profit_announcement, PDF p121: "Retained profits Opening balance 43,974 42,578 41,600"
> [ev-10] CBA/1H26/profit_announcement, PDF p121: "Net profit attributable to equity holders of the Bank 5,367 4,982 5,134"
> [ev-11] CBA/1H26/profit_announcement, PDF p121: "Final dividend - cash component (3,708) – (3,426)"
> [ev-12] CBA/1H26/profit_announcement, PDF p121: "Final dividend - dividend reinvestment plan (643) – (758)"
> [ev-13] CBA/1H26/profit_announcement, PDF p168: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176"
> [ev-14] CBA/1H26/profit_announcement, PDF p168: "Net profit after tax - "cash basis" 5,445 5,120 5,132"

## Limitations
- The earnings_effect and equity_effect are derived arithmetic decompositions, not disclosed by the bank. The bank does not provide a walk chart or bridge table for ROE movement.
- No primary-period ROE walk chart exists in either document; the results presentation (pp35-36, 40, 53) shows ROE levels and peer comparisons but no decomposition of the period-over-period movement.
- The interaction term between earnings and equity effects is embedded in the equity_effect residual rather than reported separately.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T19:26:35+00:00
- seconds: 108.8
- cost_usd: 0.0362
- tokens: 845587 in / 8146 out
- orchestration: agent
- tool_calls: 38
- pages_read: 15
- charts_read: 0
- budget_exhausted: no
