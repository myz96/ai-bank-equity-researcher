# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROE - "cash basis" (%)', column 31 Dec 24 -> column 31 Dec 25*

CBA's return on equity (cash basis) from continuing operations rose 10 basis points (0.1 ppt) to 13.8% in 1H26 from 13.7% in 1H25. The increase was driven by a 6% rise in cash NPAT ($5,445m, up $313m or 6% on 1H25's $5,132m), which at constant equity would have lifted ROE by approximately 0.8 ppt. However, average equity also grew from $74,176m to $78,004m (+5%), partially offsetting the earnings gain and reducing ROE by approximately 0.7 ppt, yielding a net improvement of 0.1 ppt. The bank stated: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."

> [ev-1] CBA/1H26/profit_announcement, PDF p19: "Cash basis 13.8 13.4 13.7 40 bpts 10 bpts"
> [ev-4] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-5] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-14] CBA/1H26/profit_announcement, PDF p168: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-16] CBA/1H26/profit_announcement, PDF p9: "The Bank's ROE remained peer leading and increased 10bpts to 13.8%."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | higher cash NPAT | +0.8 ppt | 80 | 1 (single_source) | ev-3, ev-5, ev-13 |
| `equity_effect` | higher net assets | -0.7 ppt | 80 | 1 (single_source) | ev-2, ev-12, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect — "higher cash NPAT"
*+0.8 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) multiplied by earnings growth rate (6.1%, from $313m/$5,132m). At constant equity, the 6% cash NPAT increase would have lifted ROE by approximately 0.8 ppt. The bank attributes part of the ROE improvement to 'higher cash NPAT' (ev-6).
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Net profit after tax - "cash basis" 5,445 5,120 5,133"
> [ev-5] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax ("cash NPAT" or "cash profit") from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-13] CBA/1H26/profit_announcement, PDF p168: "Net profit after tax - "cash basis" 5,445 5,120 5,132"

### equity_effect — "higher net assets"
*-0.7 ppt | confidence 80/100*

Derived: residual of total delta (0.1 ppt) minus earnings effect (0.8 ppt). Average equity grew from $74,176m to $78,004m (+$3,828m or +5.2%), reflecting retained earnings from the $5,445m profit less dividends of $3,933m (payout ratio 72%). The bank states the ROE increase was 'partly offset by higher net assets' (ev-6).
> [ev-2] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"
> [ev-12] CBA/1H26/profit_announcement, PDF p168: "Average net assets 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, printed p2: "Return on equity ("cash basis") increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."

## Limitations
- No walk/bridge chart for ROE decomposition was found in either document; both driver contributions are arithmetic derivations, not bank-disclosed components.
- The earnings growth rate of 6% is rounded by the bank; the precise rate is 6.1% ($313m/$5,132m).
- Average equity includes discontinued operations in the ratios table on page 169 but excludes them on page 168 (continuing operations); the continuing operations figures were used.

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T13:44:13+00:00
- seconds: 114.6
- cost_usd: 0.0128
- tokens: 629728 in / 6248 out
- orchestration: agent
- tool_calls: 34
- pages_read: 11
- charts_read: 0
- budget_exhausted: no
