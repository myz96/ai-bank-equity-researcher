# CBA — roe — FY21 vs FY20

**Movement (cash basis):** 10.2ppt → 11.5ppt (+1.3ppt) | **Attribution confidence:** 40/100

*Read from: row 'Return on equity (ROE) (%) Cash basis', column Jun 20 -> column Jun 21*

CBA's cash ROE rose 130 bpts to 11.5% in FY21 from 10.2% in FY20. This improvement was driven by a ~146 ppt lift from earnings growth at constant equity, partially offset by a ~16 ppt drag from equity expansion.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +146 ppt | 80 | 1 (single_source) | ev-2, ev-4 |
| `equity_effect` | — | -16 ppt | 80 | 1 (single_source) | ev-4 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+146 ppt | confidence 80/100*

Derived: Prior ROE (10.2%) x Earnings Growth (~14.7%). Cash NPAT rose $1,428m ($7,225m to $8,653m), a 19.8% increase. At constant equity, this lifts ROE by ~146 ppt. Value is derived, not disclosed.
> [ev-2] CBA/FY21/profit_announcement, PDF p23: "Return on equity (ROE) (%) Cash basis 11.5 10.2 130 bpts 12.6 10.5 210 bpts"
> [ev-4] CBA/FY21/profit_announcement, PDF p155: "Return on Equity - "cash basis" Average net assets 75,192 70,842 76,819 73,429 Less: Average non-controlling interests (5) (37) (5) (5) Average equity 75,187 70,805 76,814 73,424 Add average treasury shares – 28 – – Net average equity 75,187 70,833 76,814 73,424 Net profit after tax - "cash basis" 8,653 7,225 4,785 3,868 ROE - "cash basis" (%) 11. 5 10. 2 12. 6 10. 5"

### equity_effect
*-16 ppt | confidence 80/100*

Derived: Delta (130 ppt) minus Earnings Effect (146 ppt). Net average equity grew ~6.1% ($70,833m to $75,187m) due to retained earnings and reduced treasury share deductions. Equity expansion dilutes ROE. Value is derived, not disclosed.
> [ev-4] CBA/FY21/profit_announcement, PDF p155: "Return on Equity - "cash basis" Average net assets 75,192 70,842 76,819 73,429 Less: Average non-controlling interests (5) (37) (5) (5) Average equity 75,187 70,805 76,814 73,424 Add average treasury shares – 28 – – Net average equity 75,187 70,833 76,814 73,424 Net profit after tax - "cash basis" 8,653 7,225 4,785 3,868 ROE - "cash basis" (%) 11. 5 10. 2 12. 6 10. 5"

## Source disagreements
- **Statutory vs Cash ROE** (definitional): 11.8% — statutory vs 11.5% — cash
  Preferred: cash. Cash basis is the primary reporting measure per bank vocabulary. Statutory ROE moved 140 bpts.

## Limitations
- Earnings and equity effects are quantified via arithmetic derivation from KPI table data, not explicitly split by the bank in a driver walk.
- Movement delta normalised from 130.0 to 1.3 (unit slip against the endpoints).
- Failed check: drivers_reconcile (drivers +130.0 + residual +0.0 != delta +1.3, tol 1.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-28T12:06:13+00:00
- seconds: 68.4
- cost_usd: 0.0015
- tokens: 31907 in / 4172 out
- orchestration: pipeline
