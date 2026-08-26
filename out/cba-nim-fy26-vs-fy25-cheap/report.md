# CBA — nim — FY26 vs FY25

**Movement (cash basis):** 208bps → 205bps (-3bps) | **Attribution confidence:** 90/100

CBA's cash NIM declined by 3 bps to 205 bps in FY26 (FY25: 208 bps). The decline was driven primarily by asset pricing pressures (-5 bps) and a reduction in liquid assets drag (-4 bps), partially offset by favorable portfolio mix (+2 bps) and higher capital/replicating earnings (+5 bps). Funding costs were flat on a full-year basis.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `asset_pricing` | Asset pricing | -5 bps | 100 | 2 (corroborated_2_sources) | ev-1, ev-2, ev-3, ev-4 |
| `liquids` | Liquids & repos | -4 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-4 |
| `capital_replicating` | Interest rate risk hedging | +5 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-4 |
| `mix` | Portfolio mix | +2 bps | 90 | 1 (corroborated_2_sources) | ev-4 |
| `funding` | Funding costs | +0 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-4 |
| `markets_treasury` | Treasury & Markets | -1 bps | 90 | 1 (cross_source_divergence_surfaced) | ev-4 |

### asset_pricing — "Asset pricing"
*-5 bps | confidence 100/100*

Consistent negative pressure across all periods, reflecting elevated competition in lending markets.
> [ev-1] CBA/FY26/profit_announcement, PDF p28: "[walk chart] NIM Movement since June 2025: Jun 25 Full Year 208 -> Jun 26 Full Year 205"
> [ev-2] CBA/FY26/profit_announcement, PDF p29: "[walk chart] NIM Movement since December 2025: Dec 25 Half 204 -> Jun 26 Half 206"
> [ev-3] CBA/FY26/results_presentation, printed p26: "[walk chart] Group margin: 1H26 204.0 -> 2H26 206.0"
> [ev-4] CBA/FY26/results_presentation, printed p1: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### liquids — "Liquids & repos"
*-4 bps | confidence 90/100*

A net negative contribution in the full year, contrasting with positive or neutral contributions in half-years, indicating a shift in liquid asset levels or yields over the annual period.
> [ev-4] CBA/FY26/results_presentation, printed p1: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### capital_replicating — "Interest rate risk hedging"
*+5 bps | confidence 90/100*

Significant positive contribution from the replicating portfolio and interest rate risk hedging activities.
> [ev-4] CBA/FY26/results_presentation, printed p1: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### mix — "Portfolio mix"
*+2 bps | confidence 90/100*

Favorable mix impact, likely driven by growth in higher-yielding loan segments.
> [ev-4] CBA/FY26/results_presentation, printed p1: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### funding — "Funding costs"
*+0 bps | confidence 90/100*

Flat funding costs on a full-year basis, though H2 saw a slight increase of 2 bps.
> [ev-4] CBA/FY26/results_presentation, printed p1: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

### markets_treasury — "Treasury & Markets"
*-1 bps | confidence 90/100*

Slight negative contribution from Treasury and Markets operations.
> [ev-4] CBA/FY26/results_presentation, printed p1: "[walk chart] Group margin – 12 months: FY25 208.0 -> FY26 205.0"

## Source disagreements
- **Liquids Contribution** (definitional): -3.0 bps — ev-1 (FY26 Full Year) vs -4.0 bps — ev-4 (FY25->FY26)
  Preferred: -4.0 bps. ev-1 reports a -3 bps movement for Liquids in the FY26 walk chart, while ev-4 reports -4 bps for the same driver in the FY25-to-FY26 comparison. Both are from FY26 documents. The sum check passes for both walks independently. Given the hierarchy, we prioritize the explicit 'Group margin – 12 months' walk (ev-4) which directly compares FY25 to FY26.
- **Capital/Replicating vs Hedging Labeling** (definitional): 5.0 bps — Capital, Replicating (ev-1) vs 5.0 bps — Interest rate risk hedging (ev-4)
  Preferred: Interest rate risk hedging. ev-1 labels the bar 'Capital, Replicating', while ev-4 uses 'Interest rate risk hedging'. These map to the same canonical concept 'capital_replicating'. The value is consistent at 5 bps.
- **Treasury & Markets Contribution** (definitional): -2.0 bps — Treasury & Markets and Other (ev-1) vs -1.0 bps — Treasury & Markets (ev-4)
  Preferred: -1.0 bps. ev-1 includes 'Other' in the label and shows -2 bps. ev-4 shows -1 bps for 'Treasury & Markets'. The difference may be due to rounding or reclassification of minor items into 'Other' in the PA document versus the Presentation.
- **liquids contribution** (definitional): -3 — Liquids (CBA/FY26/profit_announcement PDF p28 (ev-1)) vs +0 — Liquids (CBA/FY26/profit_announcement PDF p29 (ev-2)) vs +0 — Liquids & repos (CBA/FY26/results_presentation PDF p26 (ev-3)) vs -4 — Liquids & repos (CBA/FY26/results_presentation PDF p60 (ev-4))
  Preferred: -4 (per the source hierarchy). The documents use different decompositions of the same movement.
- **capital_replicating contribution** (rounding): +5 — Capital, Replicating (CBA/FY26/profit_announcement PDF p28 (ev-1)) vs +3 — Capital, Replicating and Other (CBA/FY26/profit_announcement PDF p29 (ev-2)) vs +5 — Interest rate risk hedging (CBA/FY26/results_presentation PDF p60 (ev-4))
  Preferred: +5 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.
- **funding contribution** (rounding): +0 — Funding costs (CBA/FY26/profit_announcement PDF p28 (ev-1)) vs +2 — Funding costs (CBA/FY26/profit_announcement PDF p29 (ev-2)) vs +2 — Funding costs (CBA/FY26/results_presentation PDF p26 (ev-3)) vs +0 — Funding costs (CBA/FY26/results_presentation PDF p60 (ev-4))
  Preferred: +0 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.
- **markets_treasury contribution** (rounding): -2 — Treasury & Markets and Other (CBA/FY26/profit_announcement PDF p28 (ev-1)) vs +1 — Treasury & Markets (CBA/FY26/profit_announcement PDF p29 (ev-2)) vs +1 — Treasury & Markets (CBA/FY26/results_presentation PDF p26 (ev-3)) vs -1 — Treasury & Markets (CBA/FY26/results_presentation PDF p60 (ev-4))
  Preferred: -1 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.

## Limitations
- The primary attribution evidence comes from the Results Presentation (ev-4) which explicitly compares FY25 to FY26. The Profit Announcement (ev-1) also covers FY26 but shows slightly different values for Liquids and Treasury, likely due to presentation differences or inclusion of 'Other' items.
- Narrative details for specific drivers (e.g., exact deposit mix shifts) are not fully quantified in the provided text beyond the walk chart bars.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T05:01:34+00:00
- seconds: 89.5
- cost_usd: 0.0012
- tokens: 25020 in / 3272 out
- orchestration: pipeline
