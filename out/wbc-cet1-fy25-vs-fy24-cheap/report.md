# WBC — cet1 — FY25 vs FY24

**Movement (ex_notables basis):** 1249bps → 1253bps (+4bps) | **Attribution confidence:** 60/100

*Read from: row 'Level 2 common equity Tier 1 capital ratio', column As at 30 Sept 2024 -> column As at 30 Sept 2025*

Westpac's Level 2 CET1 ratio increased by 4 basis points to 12.53% in FY25 (ev-1, ev-19). The movement was driven by net profit largely offset by dividend payments and higher Risk Weighted Assets (RWA) (ev-14, ev-20). While the bank's primary walk aggregates these into a single 'Net profit etc' bar of +4 bps and a zero 'Higher Total RWA and buybacks' bar, narrative evidence confirms that earnings generation was counterbalanced by dividends and capital returns against rising RWA (ev-20, ev-21).

> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: As at 30 Sept 2024 1249 -> As at 30 Sept 2025 1253"
> [ev-13] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio of 12.5% is above our target ratio of 11.25% in normal operating conditions."
> [ev-14] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio increased 4 basis points as net profit was largely offset by the payment of dividends and increases in Risk Weighted Assets (RWA)."
> [ev-18] WBC/FY25/investor_discussion_pack, printed p31: "CET1 capital ratio %"
> [ev-19] WBC/FY25/results_announcement, PDF p28: "The Level 2 CET1 capital ratio was 12.53% at 30 September 2025, 4 basis points higher than 30 September 2024."
> [ev-20] WBC/FY25/results_announcement, PDF p28: "The increase from net profit less the payment of 2024 final ordinary dividend and 2025 interim ordinary dividend, other reserve movements and lower capitalised software balances was offset by higher Total RWA and on market share buybacks."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Net profit etc (implied) | +4 bps | 60 | 1 (single_source) | ev-1, ev-14, ev-20 |
| `rwa` | Higher Total RWA and buybacks (implied) | +0 bps | 60 | 1 (single_source) | ev-1, ev-21 |

### earnings_generation — "Net profit etc (implied)"
*+4 bps | confidence 60/100*

The results announcement presents this as a net implied bar of +4 bps (ev-1). Narrative text states net profit was 'largely offset' by dividends and RWA increases (ev-14, ev-20), implying earnings were the sole positive contributor.
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: As at 30 Sept 2024 1249 -> As at 30 Sept 2025 1253"
> [ev-14] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio increased 4 basis points as net profit was largely offset by the payment of dividends and increases in Risk Weighted Assets (RWA)."
> [ev-20] WBC/FY25/results_announcement, PDF p28: "The increase from net profit less the payment of 2024 final ordinary dividend and 2025 interim ordinary dividend, other reserve movements and lower capitalised software balances was offset by higher Total RWA and on market share buybacks."

### dividend_net_drp — "Dividends"
*unquantified | confidence 40/100*

The bank states dividends offset earnings (ev-14, ev-20). The half-on-half walk quantifies dividends at -58 bps (ev-2, ev-24), but this is for H2 only. No specific FY24-FY25 dividend impact is provided in the primary walk or text.
> [ev-14] WBC/FY25/results_announcement, PDF p6: "The CET1 capital ratio increased 4 basis points as net profit was largely offset by the payment of dividends and increases in Risk Weighted Assets (RWA)."
> [ev-20] WBC/FY25/results_announcement, PDF p28: "The increase from net profit less the payment of 2024 final ordinary dividend and 2025 interim ordinary dividend, other reserve movements and lower capitalised software balances was offset by higher Total RWA and on market share buybacks."
> [ev-24] WBC/FY25/results_announcement, PDF p29: "Payment of the 2025 interim ordinary dividend: 58 basis points reduction;"

### rwa — "Higher Total RWA and buybacks (implied)"
*+0 bps | confidence 60/100*

The primary walk lists this combined bar at 0 bps (ev-1). Text notes RWA increased $12.6bn mainly from IRRBB (ev-21). The half-on-half walk shows RWA at -7 bps (ev-2), but this is not the FY comparison.
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: As at 30 Sept 2024 1249 -> As at 30 Sept 2025 1253"
> [ev-21] WBC/FY25/results_announcement, PDF p28: "Total RWA increased by $12.6 billion mainly from higher Interest Rate Risk in the banking book (IRRBB) RWA."

### capital_returns — "Higher Total RWA and buybacks (implied)"
*unquantified | confidence 40/100*

Buybacks are included in the zero-bps combined bar (ev-1). The half-on-half walk quantifies capital return at -2 bps (ev-2, ev-27), but no FY-specific value is disclosed.
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: As at 30 Sept 2024 1249 -> As at 30 Sept 2025 1253"
> [ev-27] WBC/FY25/results_announcement, PDF p29: "Capital return: 2 basis points reduction due to the on market share buyback."

## Source disagreements
- **Primary Walk Aggregation vs Half-on-Half Detail** (timing): Primary walk: Net profit +4 bps, RWA/Buybacks 0 bps (ev-1) vs Half-on-Half walk: Net profit +80 bps, Dividends -58 bps, RWA -7 bps, Capital Return -2 bps (ev-2)
  Preferred: Primary walk values. The task requires the FY24-FY25 movement. The detailed driver bars (+80, -58, -7, -2) belong to the Mar-25 to Sep-25 period (ev-2, ev-3). They cannot be attributed to the full-year window.

## Limitations
- The primary walk (ev-1) aggregates drivers into two high-level bars ('Net profit etc' and 'Higher Total RWA and buybacks'), preventing granular attribution of the FY24-FY25 movement.
- Detailed driver contributions (e.g., dividends, RWA sub-components) are only available for the half-on-half period (Mar-25 to Sep-25) in the results announcement (ev-2) and investor pack (ev-3). These cannot be used for the FY comparison.
- Confidence is limited because the specific FY24-FY25 impacts of dividends and RWA are not explicitly quantified in the primary source, relying on narrative descriptions of offsets.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T19:05:27+00:00
- seconds: 82.6
- cost_usd: 0.0024
- tokens: 59462 in / 4691 out
- orchestration: pipeline
- pages_extracted: 18
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p78 page 125 [added]']
