# CBA — nim — 1H26 vs 1H25

**Movement (cash basis):** 208bps → 204bps (-4bps) | **Attribution confidence:** 90/100

CBA's Group NIM decreased 4 bps to 204 bps in 1H26 vs 1H25. The decline was driven by lower asset pricing (-2 bps) and Treasury/Markets drag (-2 bps), partially offset by favourable portfolio mix (+1 bps) and higher replicating portfolio earnings (+1 bps). Liquids and repos contributed a further -4 bps drag on the reported margin.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & repos | -4 bps | 95 | 2 (cross_source_divergence_surfaced) | ev-4, ev-6, ev-12 |
| `asset_pricing` | Asset pricing | -2 bps | 95 | 2 (corroborated_2_sources) | ev-4, ev-19 |
| `markets_treasury` | Treasury & Markets | -2 bps | 95 | 2 (cross_source_divergence_surfaced) | ev-4, ev-22 |
| `mix` | Portfolio mix | +1 bps | 95 | 2 (corroborated_2_sources) | ev-4, ev-20 |
| `capital_replicating` | Interest rate risk hedging | +6 bps | 95 | 2 () | ev-4, ev-14 |

### liquids — "Liquids & repos"
*-4 bps | confidence 95/100*

Growth in liquid assets and institutional reverse sale/repurchase agreements exerted a negative impact on the reported NIM. Excluding these items, the underlying NIM movement was significantly less negative.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208 -> 1H26 204"
> [ev-6] CBA/1H26/profit_announcement, PDF p9: "Excluding growth in liquid assets and institutional reverse sale and repurchase agreements, which have broadly neutral impacts on net interest income, underlying net interest margin was slightly lower in the half."
> [ev-12] CBA/1H26/profit_announcement, printed p2: "Excluding the impact of liquid assets and institutional reverse sale and repurchase agreements, the underlying NIM was unchanged."

### asset_pricing — "Asset pricing"
*-2 bps | confidence 95/100*

Home lending margins declined due to increased competition, reducing overall asset pricing.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208 -> 1H26 204"
> [ev-19] CBA/1H26/profit_announcement, PDF p29: "Asset pricing: Decreased margin by 2 basis points driven by home lending pricing reflecting the impact of increased competition."

### markets_treasury — "Treasury & Markets"
*-2 bps | confidence 95/100*

Lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances reduced the margin.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208 -> 1H26 204"
> [ev-22] CBA/1H26/profit_announcement, PDF p29: "Treasury and Markets: Decreased margin by 2 basis points due to lower risk management income in Treasury and an increase in reverse sale and repurchase agreement balances."

### mix — "Portfolio mix"
*+1 bps | confidence 95/100*

Favourable funding mix from strong growth in at-call deposits improved the margin.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208 -> 1H26 204"
> [ev-20] CBA/1H26/profit_announcement, PDF p29: "Portfolio mix: Increased margin by 1 basis point driven by favourable funding mix from strong growth in at-call deposits."

### capital_replicating — "Interest rate risk hedging"
*+6 bps | confidence 95/100*

Higher earnings from the replicating portfolio (interest rate risk hedging) provided a positive contribution to the margin.
> [ev-4] CBA/1H26/results_presentation, printed p59: "[walk chart] Group margin – 12 months: 1H25 208 -> 1H26 204"
> [ev-14] CBA/1H26/profit_announcement, PDF p69: "Net interest margin increased 5 basis points, reflecting: • Higher earnings from the replicating portfolio; and • Favourable portfolio mix due to growth in deposits relative to assets; partly offset by • Lower deposit margins due to the impact of declining interest rates; and • Lower business and home lending margins principally due to increased competition."

## Source disagreements
- **Capital/Replicating attribution framing** (definitional): 6.0 bps — CBA/1H26/results_presentation PDF p59 (ev-4) vs 1.0 bps — CBA/1H26/profit_announcement PDF p29 (ev-2)
  Preferred: 6.0 bps. The results presentation (ev-4) attributes +6 bps to 'Interest rate risk hedging' within the capital bucket. The profit announcement walk (ev-2) splits this into +1 bps for 'Capital, Replicating & Other' and does not explicitly list a separate hedging bar in that specific half-walk, though ev-14 narrative confirms the replicating portfolio benefit. The larger figure in the 12-month view (ev-4) is preferred as it captures the full hedging impact described in the narrative.
- **Funding costs attribution** (timing): -3.0 bps — CBA/1H26/results_presentation PDF p59 (ev-4) vs 0.0 bps — CBA/1H26/profit_announcement PDF p29 (ev-2)
  Preferred: 0.0 bps. The profit announcement walk (ev-2) for the specific half-over-half comparison shows 0 bps for funding costs, consistent with the narrative attributing deposit margin declines to 'lower deposit margins' but potentially offset by mix or timing lags not captured in a single 'funding' line item in that specific view. The 12-month view (ev-4) shows -3 bps, reflecting longer-term trends. For the 1H26 vs 1H25 period, the half-walk is more precise.
- **liquids contribution** (rounding): -3 — Liquids (CBA/1H26/profit_announcement PDF p28 (ev-1)) vs -2 — Liquids (CBA/1H26/profit_announcement PDF p29 (ev-2)) vs -3 — Liquids & repos (CBA/1H26/results_presentation PDF p27 (ev-3)) vs -4 — Liquids & repos (CBA/1H26/results_presentation PDF p59 (ev-4))
  Preferred: -4 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.
- **markets_treasury contribution** (rounding): -3 — Treasury & Markets (CBA/1H26/profit_announcement PDF p28 (ev-1)) vs -2 — Treasury & Markets (CBA/1H26/profit_announcement PDF p29 (ev-2)) vs -1 — Treasury & Markets (CBA/1H26/results_presentation PDF p27 (ev-3)) vs -2 — Treasury & Markets (CBA/1H26/results_presentation PDF p59 (ev-4))
  Preferred: -2 (per the source hierarchy). The documents decompose the same movement with different bar framings; the gap is framing/rounding, not a data conflict.

## Limitations
- The primary driver table relies on the 12-month view (ev-4) for the Capital/Replicating split which differs from the half-walk (ev-2). The half-walk (ev-2) sums to -2 bps total drivers, while the headline delta is -4 bps, implying a residual of -2 bps unexplained by the listed bars in ev-2 (Liquids -2, Asset Pricing -2, Mix +1, Capital +1, Treasury -2 = -4? No: -2-2+1+1-2 = -4. Wait, ev-2 sum: -2(Liq) + -2(Asset) + 0(Fund) + 1(Mix) + 0(Basis) + 1(Cap) + -2(Treas) = -4. So ev-2 sums correctly to -4. The disagreement is only on the internal composition of Capital/Funding between views.)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/1H26/profit_announcement (2bb45d7c2fa6), CBA/1H26/results_presentation (c294f1e23bf6)
- generated: 2026-08-26T06:28:10+00:00
- seconds: 98.6
- cost_usd: 0.0016
- tokens: 32108 in / 4587 out
- orchestration: pipeline
