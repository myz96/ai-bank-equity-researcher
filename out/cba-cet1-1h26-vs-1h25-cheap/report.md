# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1260bps → 1230bps (-30bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's CET1 ratio declined by 30 bps to 12.3% in 1H26 (vs 12.6% in 1H25). The bank does not publish a capital walk for this specific period; the available Jun-Dec walk shows offsetting earnings and RWA movements.

> [ev-11] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-15] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"
> [ev-22] CBA/1H26/results_presentation, printed p101: "CET1 1H26 12.3%"
> [ev-23] CBA/1H26/results_presentation, printed p101: "CET1 1H25 12.6%"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 40/100*

The bank does not disclose the specific Cash NPAT contribution to the CET1 ratio for the 1H25-to-1H26 comparison. Narrative evidence is limited to the headline ratio levels.
> [ev-11] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-15] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"

### dividend_net_drp — "Dividends"
*unquantified | confidence 40/100*

The bank does not disclose the specific dividend impact on the CET1 ratio for the 1H25-to-1H26 comparison. Narrative evidence is limited to the headline ratio levels.
> [ev-11] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-15] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"

### rwa — "RWA"
*unquantified | confidence 40/100*

The bank does not disclose the specific RWA movement contribution to the CET1 ratio for the 1H25-to-1H26 comparison. Narrative evidence is limited to the headline ratio levels.
> [ev-11] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-15] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"

## Limitations
- No capital walk published for the 1H25-to-1H26 comparison. Quantified drivers are unavailable; the residual captures the full -30 bpts movement.
- Failed check: no_quantified_drivers
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T18:43:03+00:00
- seconds: 60.1
- cost_usd: 0.0026
- tokens: 62140 in / 5543 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
