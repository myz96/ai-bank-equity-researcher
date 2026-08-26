# ANZ — nim — 1H26 vs 1H25

**Movement (cash basis):** 156bps → 153bps (-3bps) | **Attribution confidence:** 40/100

ANZ's cash NIM declined by 3 bps to 153 bps in 1H26 vs 1H25. The decline was driven by asset pricing (-4 bps) and deposit pricing (-3 bps), partially offset by capital/replicating portfolio (+4 bps), group centre liquids (+3 bps), and mix (+2 bps). Markets activities contributed a headwind of -5 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `asset_pricing` | Assets pricing | -4 bps | 85 | 1 (single_source) | ev-1, ev-12 |
| `funding.deposits` | Deposits pricing | -3 bps | 85 | 1 (single_source) | ev-1, ev-13 |
| `capital_replicating` | Capital & replicating portfolio | +4 bps | 85 | 1 (single_source) | ev-1, ev-15 |
| `mix` | Assets & funding mix | +2 bps | 85 | 1 (single_source) | ev-1, ev-16 |
| `liquids` | Group Centre liquids | +3 bps | 85 | 1 (single_source) | ev-1 |
| `markets_treasury` | Markets activities | -5 bps | 85 | 1 (single_source) | ev-1 |
| `funding.wholesale` | Wholesale funding | +0 bps | 85 | 1 (single_source) | ev-1, ev-14 |

### asset_pricing — "Assets pricing"
*-4 bps | confidence 85/100*

Driven by ongoing competition across most divisions and timing impact of RBA rate changes.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"
> [ev-12] ANZ/1H26/results_announcement, printed p18: "Assets pricing (-4 bps): driven by ongoing competition across most divisions and timing impact of RBA rate changes."

### funding.deposits — "Deposits pricing"
*-3 bps | confidence 85/100*

Driven by lower cash rates in New Zealand and international geographies and pricing competition.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"
> [ev-13] ANZ/1H26/results_announcement, printed p18: "Deposits pricing (-3 bps): driven by lower cash rates in New Zealand and international geographies and pricing competition."

### capital_replicating — "Capital & replicating portfolio"
*+4 bps | confidence 85/100*

Driven by higher volumes and average hedge rates.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"
> [ev-15] ANZ/1H26/results_announcement, printed p18: "Capital and replicating portfolio (+4 bps): driven by higher volumes and average hedge rates."

### mix — "Assets & funding mix"
*+2 bps | confidence 85/100*

Favourable funding mix primarily from stronger growth in at-call deposits, and overall deposit growth outpacing lending growth.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"
> [ev-16] ANZ/1H26/results_announcement, printed p18: "Assets and funding mix (+2 bps): favourable funding mix primarily from stronger growth in at-call deposits, and overall deposit growth outpacing lending growth."

### liquids — "Group Centre liquids"
*+3 bps | confidence 85/100*

Positive contribution from Group Centre liquid assets.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"

### markets_treasury — "Markets activities"
*-5 bps | confidence 85/100*

Negative contribution from markets activities.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"

### funding.wholesale — "Wholesale funding"
*+0 bps | confidence 85/100*

Largely flat with increased funding volume and lower average spread.
> [ev-1] ANZ/1H26/results_announcement, printed p18: "[walk chart] Net interest margin - March 2026 Half Year v March 2025 Half Year: 1H25 Cash net interest margin 156.0 -> 1H26 Cash net interest margin 153.0"
> [ev-14] ANZ/1H26/results_announcement, printed p18: "Wholesale funding (0 bps): largely flat with increased funding volume and lower average spread."

## Limitations
- Failed check: walk_extraction_error p19: float() argument must be a string or a real number, not 'NoneType'

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: ANZ/1H26/results_announcement (29d777ef9536), ANZ/1H26/results_book (8b6238fd9365), ANZ/1H26/investor_presentation (90ae6d66d158), ANZ/1H25/results_announcement (b3915a58b7cc), ANZ/1H25/results_book (0c7eb69a1062), ANZ/1H25/investor_presentation (b9d8962fe8b0)
- generated: 2026-08-26T05:27:06+00:00
- seconds: 93.5
- cost_usd: 0.0015
- tokens: 26332 in / 5623 out
- orchestration: pipeline
