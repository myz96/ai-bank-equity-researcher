# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's CET1 ratio increased by 10 bps to 12.3% in 1H26 vs 1H25. The bank did not publish a capital walk for this specific comparison; the published Jun-Dec walk shows offsetting drivers. Quantified contributions are limited to footnoted items.

> [ev-15] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-17] CBA/1H26/profit_announcement, printed p28: "Dec 25 vs Dec 24 % 10 bpts"
> [ev-19] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"
> [ev-39] CBA/1H26/results_presentation, printed p103: "Level 2 CET1 capital ratio of 12.3%"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `dividend_net_drp` | Dividends net of DRP | -33 bps | 85 | 1 (single_source) | ev-37 |
| *residual (unexplained)* | — | +43 bps | — | — |

### dividend_net_drp — "Dividends net of DRP"
*-33 bps | confidence 85/100*

The bank states a 33 bps negative impact from dividends net of DRP in the 1H26 results presentation text (ev-37). This is distinct from the 87 bps bar in the half-on-half walk.
> [ev-37] CBA/1H26/results_presentation, printed p33: "2H25 dividend (DRP neutralised) (33)"

### earnings_generation — "Cash NPAT"
*unquantified | confidence 0/100*

No quantified contribution for earnings generation was disclosed for the 1H25-to-1H26 window. The published Cash NPAT bar (+107 bps) applies to the Jun-Dec period (ev-1, ev-7).

### rwa — "RWA"
*unquantified | confidence 0/100*

No quantified RWA contribution was disclosed for the 1H25-to-1H26 window. The published RWA bar (-33 bps) applies to the Jun-Dec period (ev-1, ev-7).

### deductions_other — "Other"
*unquantified | confidence 0/100*

No quantified 'Other' contribution was disclosed for the 1H25-to-1H26 window. The published Other bar (+9 bps) applies to the Jun-Dec period (ev-1, ev-7).

## Limitations
- The bank only published a capital walk for the half-on-half period (Jun 2025 -> Dec 2025), not for the requested 1H25 -> 1H26 comparison.
- Quantified drivers are restricted to the single footnoted dividend impact (-33 bps); the remaining 43 bpts of movement is unquantified residual.
- Confidence is lowered due to the lack of explicit driver attribution for the year-on-year movement.
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T12:51:55+00:00
- seconds: 81.7
- cost_usd: 0.0025
- tokens: 61904 in / 5324 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
