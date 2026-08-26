# CBA — nim — FY26 vs FY25

**Movement (cash basis):** 208bps → 205bps (-3bps) | **Attribution confidence:** 90/100

CBA's statutory Net Interest Margin (NIM) decreased by 3 basis points to 2.05% in FY26 compared to FY25 (2.08%). This decline was primarily driven by competitive pressure on asset pricing (-5 bps) and the dilutive impact of growth in liquid assets and institutional repos (-4 bps). These headwinds were partially offset by a favorable portfolio mix (+2 bps) and higher earnings from interest rate risk hedging (+5 bps). Funding costs remained flat year-on-year.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & repos | -4 bps | 95 | 1 (cross_source_divergence_surfaced) | ev-3, ev-18, ev-19, ev-21 |
| `asset_pricing` | Asset pricing | -5 bps | 95 | 2 (corroborated_2_sources) | ev-3, ev-14, ev-21 |
| `capital_replicating` | Interest rate risk hedging | +5 bps | 90 | 2 (cross_source_divergence_surfaced) | ev-3, ev-9, ev-21 |
| `mix` | Portfolio mix | +2 bps | 95 | 2 (corroborated_2_sources) | ev-3, ev-15, ev-21 |
| `funding` | Funding costs | +0 bps | 90 | 2 (cross_source_divergence_surfaced) | ev-3, ev-16, ev-21 |

### liquids — "Liquids & repos"
*-4 bps | confidence 95/100*

Growth in average liquid assets ($15bn) and institutional reverse sale/repurchase agreements ($11bn) exerted a negative drag on margin. The bank noted these have broadly neutral impacts on NII but dilute the margin percentage.
> [ev-3] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208 -> FY26 205"
> [ev-18] CBA/FY26/results_presentation, printed p60: "Lower margin largely due to growth in liquids and repos – competition offset by hedge earnings"
> [ev-19] CBA/FY26/results_presentation, printed p60: "+$15bn increase in average liquid assets and +$11bn increase in average institutional repos in FY26 vs FY25."
> [ev-21] CBA/FY26/results_presentation, printed p60: "None"

### asset_pricing — "Asset pricing"
*-5 bps | confidence 95/100*

Margin decreased due to lower home lending pricing (-4 bps) driven by competition, and lower business/institutional lending pricing (-1 bps). This is consistent across all period comparisons.
> [ev-3] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208 -> FY26 205"
> [ev-14] CBA/FY26/profit_announcement, PDF p28: "Asset pricing: Decreased margin by 5 basis points driven by home lending pricing (down 4 basis points) and business and institutional lending pricing (down 1 basis point)"
> [ev-21] CBA/FY26/results_presentation, printed p60: "None"

### capital_replicating — "Interest rate risk hedging"
*+5 bps | confidence 90/100*

Higher earnings on the replicating portfolio and interest rate risk hedging provided a significant positive offset to the margin decline. Note: The Profit Announcement aggregates this into 'Capital, Replicating and Other' at +3 bps for H2, while the Results Presentation isolates it at +5 bps for FY.
> [ev-3] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208 -> FY26 205"
> [ev-9] CBA/FY26/profit_announcement, PDF p64: "Net interest margin decreased by 1 basis point on the prior year, reflecting: • Lower home lending margins primarily due to competition; and • Lower deposit margins mainly due to competition and mix shift to higher yielding savings deposits; partly offset by • Higher earnings on the replicating portfolio; and • Favourable portfolio mix primarily due to the benefit of strong growth in average deposits relative to assets."
> [ev-21] CBA/FY26/results_presentation, printed p60: "None"

### mix — "Portfolio mix"
*+2 bps | confidence 95/100*

Favorable mix contributed positively, driven by strong growth in business lending (asset side) and strong growth in average deposits relative to assets (funding side).
> [ev-3] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208 -> FY26 205"
> [ev-15] CBA/FY26/profit_announcement, PDF p28: "Portfolio mix: Increased margin by 2 basis points driven by favourable asset mix from strong growth in business lending and favourable funding mix from strong growth in deposits."
> [ev-21] CBA/FY26/results_presentation, printed p60: "None"

### funding — "Funding costs"
*+0 bps | confidence 90/100*

Funding costs were flat year-on-year. While the H2 walk chart shows a +2 bps contribution, the FY comparison explicitly states funding costs were flat.
> [ev-3] CBA/FY26/results_presentation, printed p60: "[walk chart] Group margin – 12 months: FY25 208 -> FY26 205"
> [ev-16] CBA/FY26/profit_announcement, PDF p28: "Funding costs: Flat."
> [ev-21] CBA/FY26/results_presentation, printed p60: "None"

## Source disagreements
- **Hedging/Replicating Portfolio Attribution** (definitional): +5 bps — CBA/FY26/results_presentation PDF p60 (ev-3) vs +3 bps — CBA/FY26/profit_announcement PDF p29 (ev-1)
  Preferred: +5 bps. The Results Presentation (FY view) isolates 'Interest rate risk hedging' as a distinct +5 bps driver. The Profit Announcement (H2 view) groups this into 'Capital, Replicating and Other' at +3 bps. For the full FY attribution requested, the isolated FY figure is more precise.
- **Funding Costs Contribution** (timing): 0 bps — CBA/FY26/results_presentation PDF p60 (ev-3) vs +2 bps — CBA/FY26/profit_announcement PDF p29 (ev-1)
  Preferred: 0 bps. The FY comparison explicitly states funding costs were flat (0 bps). The +2 bps figure appears in the Half 2 walk chart, reflecting different timing or compounding effects within the half rather than the full year delta.
- **liquids contribution** (definitional): +0 — Liquids (CBA/FY26/profit_announcement PDF p29 (ev-1)) vs +0 — Liquids & repos (CBA/FY26/results_presentation PDF p26 (ev-2)) vs -4 — Liquids & repos (CBA/FY26/results_presentation PDF p60 (ev-3))
  Preferred: -4 (per the source hierarchy). The documents use different decompositions of the same movement.
- **capital_replicating contribution** (rounding): +3 — Capital, Replicating and Other (CBA/FY26/profit_announcement PDF p29 (ev-1)) vs +5 — Interest rate risk hedging (CBA/FY26/results_presentation PDF p60 (ev-3))
  Preferred: +5 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.
- **funding contribution** (rounding): +2 — Funding costs (CBA/FY26/profit_announcement PDF p29 (ev-1)) vs +2 — Funding costs (CBA/FY26/results_presentation PDF p26 (ev-2)) vs +0 — Funding costs (CBA/FY26/results_presentation PDF p60 (ev-3))
  Preferred: +0 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.

## Limitations
- The primary FY attribution relies on the Results Presentation walk chart (ev-3) which sums correctly to -3 bps. The Profit Announcement text confirms the drivers qualitatively but provides less granular quantitative breakdown for the full year in the narrative sections compared to the slide deck.
- Cash NIM declined by only 1 bps (2.51% to 2.50%), significantly less than the statutory decline. The analysis above focuses on statutory NIM as per the primary movement data (ev-4, ev-6, ev-20).
- Failed check: walk_extraction_error p28: Unterminated string starting at: line 2 column 12 (char 13)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:31:18+00:00
- seconds: 80.0
- cost_usd: 0.0016
- tokens: 32985 in / 4335 out
- orchestration: pipeline
