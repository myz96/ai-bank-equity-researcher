# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'Return on equity (cash basis)', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE increased 10 bpts to 13.8% in 1H26 vs 1H25, driven by a 6% rise in cash NPAT partially offset by higher average net assets.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.8 ppt | 80 | 1 (single_source) | ev-1, ev-2 |
| `equity_effect` | — | -0.7 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3 |

### earnings_effect
*+0.8 ppt | confidence 80/100*

Derived: prior-period ROE (13.7%) multiplied by stated cash NPAT growth (6.0%). This represents the lift at constant equity. Derived from ev-1 and ev-2.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."

### equity_effect
*-0.7 ppt | confidence 80/100*

Residual: total delta (0.1 ppt) minus earnings effect (0.8 ppt). Reflects dilution from higher average net assets ($78,004m vs $74,176m), likely due to retained earnings. Derived from ev-1, ev-2, ev-3.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"

## Source disagreements
- **Statutory ROE values** (definitional): 13.6% (ev-8) vs 13.8% (ev-9)
  Preferred: 13.6%. ev-8 is the primary KPI table for statutory ROE; ev-9 appears to be a summary or slide with a discrepancy.

## Limitations
- Earnings and equity effects are derived arithmetic contributions, not disclosed by the bank.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-29T13:07:09+00:00
- seconds: 56.5
- cost_usd: 0.0016
- tokens: 32158 in / 4982 out
- orchestration: pipeline
