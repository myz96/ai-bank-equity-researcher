# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bps to 13.8% in 1H26 vs 1H25, driven by a 6% increase in cash NPAT ($5,445m), partially offset by higher average net assets ($78.0bn). The earnings effect lifted ROE by ~81 bps, while the equity effect reduced it by ~80 bps.

> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-4] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.81 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3 |
| `equity_effect` | — | -0.71 ppt | 80 | 1 (single_source) | ev-1, ev-3, ev-4 |
| *residual (unexplained)* | — | -0 ppt | — | — |

### earnings_effect
*+0.81 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) x earnings growth (6%). Cash NPAT grew $313m to $5,445m (ev-2). This contribution is derived from arithmetic, not disclosed directly.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*-0.71 ppt | confidence 80/100*

Derived: total delta (0.1 ppt) minus earnings effect (0.81 ppt). Higher average net assets ($78.0bn vs $74.2bn) diluted returns (ev-4). This contribution is derived from arithmetic.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"
> [ev-4] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176"

## Limitations
- Earnings and equity effects are quantified via arithmetic derivation rather than bank disclosure.
- Residual is negligible but non-zero due to rounding of inputs.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T12:22:41+00:00
- seconds: 35.3
- cost_usd: 0.0017
- tokens: 35602 in / 4849 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
