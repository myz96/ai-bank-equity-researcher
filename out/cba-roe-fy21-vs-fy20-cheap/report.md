# CBA — roe — FY21 vs FY20

**Movement (cash basis):** 10.2ppt → 11.5ppt (+1.3ppt) | **Attribution confidence:** 90/100

CBA's cash ROE improved by 130 bps to 11.5% in FY21 (vs 10.2% in FY20). This movement is driven primarily by earnings growth (earnings effect), with a smaller contribution from equity expansion (equity effect). The earnings effect is derived as prior-period ROE multiplied by the cash NPAT growth rate of 19.8%. The equity effect captures the residual impact of average equity increasing from $70,833m to $75,187m.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | +2.02 ppt | 95 | 2 () | ev-2, ev-10 |
| `equity_effect` | — | -0.72 ppt | 90 | 2 () | ev-4, ev-13 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*+2.02 ppt | confidence 95/100*

Derived: Prior-period ROE (10.2%) x Cash NPAT growth (19.8%). Represents the lift at constant equity. Evidence: ev-2 (ROE endpoints), ev-10 (NPAT growth).
> [ev-2] CBA/FY21/profit_announcement, PDF p23: "Return on equity (ROE) (%) Cash basis 11.5 10.2 130 bpts 12.6 10.5 210 bpts"
> [ev-10] CBA/FY21/results_presentation, printed p8: "Cash NPAT ($m) 8,653 19.8%"

### equity_effect
*-0.72 ppt | confidence 90/100*

Derived: Total delta (1.3 ppt) minus earnings effect (2.02 ppt). Reflects dilution from higher average equity ($75,187m vs $70,833m), likely due to retained earnings exceeding dividends/buybacks. Evidence: ev-4 (Equity levels), ev-13 (Dividends).
> [ev-4] CBA/FY21/profit_announcement, PDF p155: "Return on Equity - "cash basis" Average net assets 75,192 70,842 Average non-controlling interests (5) (37) Average equity 75,187 70,805 Add average treasury shares – 28 Net average equity 75,187 70,833 Net profit after tax - "cash basis" 8,653 7,225 ROE - "cash basis" (%) 11. 5 10. 2"
> [ev-13] CBA/FY21/results_presentation, printed p8: "Dividend per share ($) 3.50 52c"

## Source disagreements
- **ROE Basis Definition** (definitional): 11.5% (Cash basis, ev-2) vs 11.8% (Statutory basis, ev-1)
  Preferred: Cash basis. The task asks for CBA's ROE movement. While both statutory and cash are reported, cash basis is the primary performance metric for Australian banks. The analysis uses cash basis (10.2% to 11.5%) as it aligns with the core profit narrative and EPS data provided.

## Limitations
- The 'earnings_effect' and 'equity_effect' are arithmetic derivations based on the canonical taxonomy, not explicit disclosures by CBA. CBA does not publish this specific decomposition.
- The equity effect includes an interaction term (growth in earnings on new equity) which is bundled into the residual calculation here as per the method instructions (Total Delta - Earnings Effect).
- Confidence is high for the derivation but relies on the assumption that the canonical split is the appropriate analytical lens.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY21/profit_announcement (ffdff75173e7), CBA/FY21/results_presentation (b1bbbd626803), CBA/FY20/profit_announcement (2c2179a200a3)
- generated: 2026-08-27T07:47:07+00:00
- seconds: 64.6
- cost_usd: 0.0014
- tokens: 26656 in / 4539 out
- orchestration: pipeline
