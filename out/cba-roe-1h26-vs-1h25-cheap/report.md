# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bps to 13.8% in 1H26 vs 1H25. The increase is driven by a positive earnings effect from 6% growth in cash NPAT, partially offset by a negative equity effect as average net assets expanded.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.82 ppt | 80 | 1 (single_source) | ev-2, ev-3 |
| `equity_effect` | — | -0.72 ppt | 80 | 1 (single_source) | ev-3 |
| *residual (unexplained)* | — | -0 ppt | — | — |

### earnings_effect
*+0.82 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) multiplied by the stated cash NPAT growth rate of 6% (ev-2). This represents the lift at constant equity.
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*-0.72 ppt | confidence 80/100*

Derived: total delta (0.1 ppt) minus earnings effect (0.82 ppt). Reflects the drag from higher average net assets ($78,004m vs $74,176m), consistent with retained earnings growth.
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 Less: Average non-controlling interests – – – Net average equity 78,004 77,020 74,176 Net profit after tax - "cash basis" 5,445 5,120 5,133 ROE - "cash basis" (%) 13.8 13.4 13.7"

## Source disagreements
- **ROE Statutory Basis Values** (restatement): 13.6% (ev-4, ev-9 table) vs 13.8% (ev-5, ev-9 text)
  Preferred: 13.6%. The detailed ROE table (ev-4) and its summary (ev-9) show 13.6%, while the KPI slide (ev-5) shows 13.8%. The detailed table is preferred per source hierarchy.

## Limitations
- Earnings and equity effects are derived calculations, not disclosed by the bank.
- Residual is negligible but non-zero due to rounding of inputs.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T20:43:33+00:00
- seconds: 42.0
- cost_usd: 0.0017
- tokens: 35053 in / 4857 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: []
