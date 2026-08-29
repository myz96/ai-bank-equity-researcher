# CBA — roe — 1H26 vs 1H25

**Movement (cash basis):** 13.7ppt → 13.8ppt (+0.1ppt) | **Attribution confidence:** 80/100

*Read from: row 'ROE - cash basis', column 31 Dec 24 -> column 31 Dec 25*

CBA's cash ROE rose 10 bps to 13.8% in 1H26 vs 1H25, driven by a 6% increase in cash NPAT ($5,445m), partially offset by higher average net assets ($78,004m). The earnings effect contributed +0.8 ppt, while the equity effect reduced ROE by -0.7 ppt.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +0.8 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-6 |
| `equity_effect` | — | -0.7 ppt | 80 | 1 (single_source) | ev-1, ev-2, ev-3, ev-6 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+0.8 ppt | confidence 80/100*

Derived: Prior ROE (13.7%) x Earnings Growth (6%). Cash NPAT rose $313m (+6%) to $5,445m (ev-2). This lift at constant equity is quantified as +0.8 ppt.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

### equity_effect
*-0.7 ppt | confidence 80/100*

Residual: Total delta (0.1 ppt) minus earnings effect (+0.8 ppt). Average net assets grew from $74,176m to $78,004m (ev-3), diluting returns. Driven by retained earnings and capital accumulation.
> [ev-1] CBA/1H26/profit_announcement, printed p2: "Return on equity (“cash basis”) increased 10 basis points to 13.8% due to higher cash NPAT being partly offset by higher net assets."
> [ev-2] CBA/1H26/profit_announcement, printed p2: "Cash net profit after tax (“cash NPAT” or “cash profit”) from continuing operations increased $313 million or 6% on the prior comparative period to $5,445 million."
> [ev-3] CBA/1H26/profit_announcement, PDF p169: "Average net assets 78,004 77,020 74,176"
> [ev-6] CBA/1H26/profit_announcement, PDF p169: "ROE - "cash basis" (%) 13.8 13.4 13.7"

## Source disagreements
- **Statutory ROE Definition** (definitional): 13.6% - ev-10 vs 13.8% - ev-11
  Preferred: 13.6%. ev-10 (KPI table) reports statutory ROE as 13.6%, while ev-11 (summary table) reports 13.8%. The KPI table is preferred per source hierarchy.

## Limitations
- Earnings and equity effects are derived arithmetic contributions, not disclosed bank splits.
- Interaction term between earnings and equity growth is embedded in the equity residual.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-28T12:37:21+00:00
- seconds: 65.9
- cost_usd: 0.0017
- tokens: 32250 in / 5273 out
- orchestration: pipeline
