# CBA — cet1 — 1H26 vs 1H25

**Movement (cash basis):** 1220bps → 1230bps (+10bps) | **Attribution confidence:** 40/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 24 -> column 31 Dec 25*

CBA's Level 2 CET1 ratio increased by 10 bps to 12.3% in 1H26 (vs 12.2% in 1H25). The bank does not publish a capital walk for this specific year-on-year comparison; the available half-on-half walk (Jun 25 -> Dec 25) shows a net -10 bps movement driven by dividends and RWA changes. Quantified drivers for 1H26 vs 1H25 are unavailable.

> [ev-17] CBA/1H26/profit_announcement, printed p28: "Summary Group Capital Adequacy Ratios Common Equity Tier 1 (CET1) 12.3 12.3 12.2 – 10 bpts"
> [ev-19] CBA/1H26/profit_announcement, PDF p157: "Common Equity Tier 1 12.3 12.3 12.2"
> [ev-40] CBA/1H26/results_presentation, printed p103: "Key capital ratios (%) Dec 24 Jun 25 Dec 25 CET1 capital ratio 12.2 12.3 12.3"

## Limitations
- The bank published no capital walk for the 1H25 -> 1H26 comparison. Only the Jun 2025 -> Dec 2025 (half-on-half) walk is available (ev-1, ev-9), which cannot be used as driver contributions for the requested period.
- Quantified driver values (e.g., Cash NPAT +107 bps, Dividend -87 bps) belong to the half-on-half period and are excluded from the driver table per instructions.
- Attribution confidence is low because the primary evidence (the walk) is missing for the target period.
- Failed check: no_quantified_drivers
- No published walk covers 1H26 vs 1H25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-30T14:41:26+00:00
- seconds: 83.6
- cost_usd: 0.0026
- tokens: 63364 in / 5118 out
- orchestration: pipeline
- pages_extracted: 16
- reference_follow: ['CBA/1H26/profit_announcement p49 <- p48 page 29']
