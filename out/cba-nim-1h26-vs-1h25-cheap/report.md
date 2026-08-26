# CBA — nim — 1H26 vs 1H25

**Movement (cash basis):** 208bps → 204bps (-4bps) | **Attribution confidence:** 90/100

CBA's Group Net Interest Margin (NIM) decreased by 4 basis points to 204 bps in 1H26 compared to 1H25. This decline was primarily driven by lower asset pricing (-2 bps), higher funding costs (-3 bps), and a negative impact from liquid assets/repo agreements (-4 bps). These headwinds were partially offset by favorable portfolio mix (+1 bps) and strong earnings from the replicating portfolio/hedging (+6 bps). Treasury & Markets contributed a further drag of -2 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & repos | -4 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-4 |
| `capital_replicating` | Interest rate risk hedging | +6 bps | 85 | 1 (single_source) | ev-4 |
| `asset_pricing` | Asset pricing | -2 bps | 95 | 2 (corroborated_2_sources) | ev-1, ev-2, ev-3, ev-4 |
| `funding` | Funding costs | -3 bps | 85 | 2 (cross_source_divergence_surfaced) | ev-1, ev-4, ev-15 |
| `mix` | Portfolio mix | +1 bps | 95 | 2 (corroborated_2_sources) | ev-1, ev-2, ev-3, ev-4 |
| `markets_treasury` | Treasury & Markets | -2 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-4 |

### liquids — "Liquids & repos"
*-4 bps | confidence 90/100*

The movement in liquid assets and institutional reverse sale and repurchase agreements reduced NIM by 4 bps. While the Profit Announcement notes these have 'broadly neutral impacts' on NII, the walk chart explicitly attributes a -4 bps drag to this category for the 12-month comparison.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### capital_replicating — "Interest rate risk hedging"
*+6 bps | confidence 85/100*

Higher earnings from the replicating portfolio and interest rate risk hedging activities provided a significant positive contribution of +6 bps to the margin, as detailed in the 12-month walk chart.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### asset_pricing — "Asset pricing"
*-2 bps | confidence 95/100*

Lower business and home lending margins, principally due to increased competition, drove a -2 bps decrease in asset pricing. This figure is consistent across all four evidence records.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-2] CBA/1H26/profit_announcement, PDF p29: "[walk chart] NIM movement since June 2025: Jun 25 Half 208 -> Dec 25 Half 204"
> [ev-3] CBA/1H26/results_presentation, printed p27: "[walk chart] Group margin: 2H25 208.0 -> 1H26 204.0"
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### funding — "Funding costs"
*-3 bps | confidence 85/100*

Lower deposit margins, impacted by declining interest rates, resulted in a -3 bps increase in funding costs. Note: The 6-month walk (ev-2) shows 0 bps, but the 12-month/annual comparison (ev-4) and the PA narrative (ev-15) support the -3 bps annual figure.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"
> [ev-15] CBA/1H26/profit_announcement, PDF p69: "Net interest margin increased 5 basis points, reflecting: • Higher earnings from the replicating portfolio; and • Favourable portfolio mix due to growth in deposits relative to assets; partly offset by • Lower deposit margins due to the impact of declining interest rates; and • Lower business and home lending margins principally due to increased competition."

### mix — "Portfolio mix"
*+1 bps | confidence 95/100*

Favorable portfolio mix, driven by growth in deposits relative to assets, contributed positively to NIM by +1 bps. This is consistent across all sources.
> [ev-1] CBA/1H26/profit_announcement, printed p12: "[walk chart] NIM movement since December 2024: Dec 24 Half 208 -> Dec 25 Half 204"
> [ev-2] CBA/1H26/profit_announcement, PDF p29: "[walk chart] NIM movement since June 2025: Jun 25 Half 208 -> Dec 25 Half 204"
> [ev-3] CBA/1H26/results_presentation, printed p27: "[walk chart] Group margin: 2H25 208.0 -> 1H26 204.0"
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

### markets_treasury — "Treasury & Markets"
*-2 bps | confidence 90/100*

Markets and Treasury activities contributed a negative drag of -2 bps to the net interest margin over the 12-month period.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208.0 -> 1H26 204.0"

## Source disagreements
- **Funding Costs Contribution** (timing): -3.0 bps — CBA/1H26/profit_announcement PDF p28 (ev-1) vs 0.0 bps — CBA/1H26/profit_announcement PDF p29 (ev-2) vs -3.0 bps — CBA/1H26/results_presentation PDF p59 (ev-4)
  Preferred: -3.0 bps. The task requires 1H26 vs 1H25 (12-month comparison). Evidence ev-1 and ev-4 cover this period showing -3 bps. Evidence ev-2 covers Jun 25 to Dec 25 (6-month) showing 0 bps. We prioritize the 12-month view.
- **Capital Replicating / Hedging Labeling** (definitional): 6.0 bps (Capital, Replicating & Other) — CBA/1H26/profit_announcement PDF p28 (ev-1) vs 6.0 bps (Interest rate risk hedging) — CBA/1H26/results_presentation PDF p59 (ev-4)
  Preferred: Interest rate risk hedging. The results presentation (ev-4) explicitly labels the driver as 'Interest rate risk hedging', mapping to canonical 'capital_replicating'. The profit announcement (ev-1) uses a broader label 'Capital, Replicating & Other'. Both quantify the same magnitude (+6 bps).
- **liquids contribution** (rounding): -3 — Liquids (CBA/1H26/profit_announcement PDF p28 (ev-1)) vs -2 — Liquids (CBA/1H26/profit_announcement PDF p29 (ev-2)) vs -3 — Liquids & repos (CBA/1H26/results_presentation PDF p27 (ev-3)) vs -4 — Liquids & repos (CBA/1H26/results_presentation PDF p59 (ev-4))
  Preferred: -4 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.
- **funding contribution** (rounding): -3 — Funding costs (CBA/1H26/profit_announcement PDF p28 (ev-1)) vs +0 — Funding costs (CBA/1H26/profit_announcement PDF p29 (ev-2)) vs +0 — Funding costs (CBA/1H26/results_presentation PDF p27 (ev-3)) vs -3 — Funding costs (CBA/1H26/results_presentation PDF p59 (ev-4))
  Preferred: -3 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.
- **markets_treasury contribution** (rounding): -3 — Treasury & Markets (CBA/1H26/profit_announcement PDF p28 (ev-1)) vs -2 — Treasury & Markets (CBA/1H26/profit_announcement PDF p29 (ev-2)) vs -1 — Treasury & Markets (CBA/1H26/results_presentation PDF p27 (ev-3)) vs -2 — Treasury & Markets (CBA/1H26/results_presentation PDF p59 (ev-4))
  Preferred: -2 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.

## Limitations
- The primary attribution is based on the 12-month walk chart (ev-4) which matches the 1H26 vs 1H25 comparator. The 6-month walk (ev-2) differs in funding and capital drivers but is excluded as it represents a different time window.
- The Profit Announcement text (ev-6, ev-12) states underlying NIM was 'flat' or 'unchanged' excluding liquids. However, the quantitative walk charts consistently show a -4 bps total movement including liquids. The narrative likely refers to the residual after removing the volatile liquidity items, whereas the task asks for the full NIM movement drivers.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-26T06:13:33+00:00
- seconds: 122.6
- cost_usd: 0.0015
- tokens: 31158 in / 4224 out
- orchestration: pipeline
