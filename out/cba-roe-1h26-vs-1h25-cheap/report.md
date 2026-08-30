# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bps to 13.8% in 1H26 vs 1H25. The increase was driven by higher cash NPAT (+$313m), partially offset by a larger average net asset base.

> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-15] CBA/1H26/results_presentation, printed p53: "ROE (cash) 13.8% +10bpts"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.09 ppt | 80 | 1 (single_source) | ev-2, ev-6 |
| `equity_effect` | — | +0.01 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.09 ppt | confidence 80/100*

Derived: prior ROE (13.7%) multiplied by earnings growth rate (6%). Cash NPAT increased $313m or 6% to $5,445m (ev-2). This contribution is derived, not disclosed.
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*+0.01 ppt | confidence 80/100*

Residual: total delta (0.1 ppt) minus earnings effect (0.09 ppt). Driven by higher average net assets ($78,004m vs $74,176m; ev-3), consistent with retained earnings and capital generation.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

## Limitations
- Earnings and equity effects are quantified via arithmetic derivation rather than bank disclosure.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T18:42:02+00:00
- seconds: 37.5
- cost_usd: 0.0017
- tokens: 35505 in / 4744 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
