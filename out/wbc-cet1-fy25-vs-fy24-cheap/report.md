# WBC — cet1 — FY25 vs FY24

**Movement (ex_notables basis):** 1249bps → 1253bps (+4bps) | **Attribution confidence:** 40/100

*Read from: row 'Level 2 common equity Tier 1 capital ratio', column Sep-24 -> column Sep-25*

WBC's Level 2 CET1 ratio increased by 4 bps to 12.53% in FY25 (ev-16). The movement was driven by net profit (+4 bps) and other reserve movements (+4 bps), which were largely offset by dividends (-8 bps total), higher Total RWA (-4 bps), lower capitalised software balances (-4 bps), and on-market share buybacks (-4 bps) (ev-1, ev-20). A residual of +16 bps exists due to a reconciliation failure in the primary walk chart.

> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"
> [ev-16] WBC/FY25/results_announcement, PDF p10: "Level 2 common equity Tier 1 capital ratio: - Australian Prudential Regulation Authority (APRA)"
> [ev-20] WBC/FY25/results_announcement, PDF p28: "The Level 2 CET1 capital ratio was 12.53% at 30 September 2025, 4 basis points higher than 30 September 2024."

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_generation` | Net profit | +4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2024 final ordinary dividend | -4 bps | 85 | 1 (single_source) | ev-1 |
| `dividend_net_drp` | 2025 interim ordinary dividend | -4 bps | 85 | 1 (single_source) | ev-1 |
| `deductions_other` | Other reserve movements | +4 bps | 85 | 1 (single_source) | ev-1 |
| `deductions_other` | Lower capitalised software balances | -4 bps | 85 | 1 (single_source) | ev-1 |
| `rwa` | Higher Total RWA | -4 bps | 85 | 1 (single_source) | ev-1, ev-22 |
| `capital_returns` | On market share buybacks | -4 bps | 85 | 1 (single_source) | ev-1 |
| *residual (unexplained)* | — | +16 bps | — | — |

### earnings_generation — "Net profit"
*+4 bps | confidence 85/100*

Capital generated from earnings contributed +4 bps to the ratio (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2024 final ordinary dividend"
*-4 bps | confidence 85/100*

The payment of the 2024 final ordinary dividend reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### dividend_net_drp — "2025 interim ordinary dividend"
*-4 bps | confidence 85/100*

The payment of the 2025 interim ordinary dividend reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### deductions_other — "Other reserve movements"
*+4 bps | confidence 85/100*

Other reserve movements contributed +4 bps to the ratio (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### deductions_other — "Lower capitalised software balances"
*-4 bps | confidence 85/100*

Lower capitalised software balances reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

### rwa — "Higher Total RWA"
*-4 bps | confidence 85/100*

Higher Total RWA reduced the ratio by 4 bps (ev-1). Total RWA increased by $12.6 billion, mainly from higher IRRBB RWA (ev-22).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"
> [ev-22] WBC/FY25/results_announcement, PDF p28: "Total RWA increased by $12.6 billion mainly from higher Interest Rate Risk in the banking book (IRRBB) RWA."

### capital_returns — "On market share buybacks"
*-4 bps | confidence 85/100*

On-market share buybacks reduced the ratio by 4 bps (ev-1).
> [ev-1] WBC/FY25/results_announcement, PDF p28: "[walk chart] Full Year 2025 - Full Year 2024 Level 2 CET1 capital ratio movement: 30 Sept 2024 1249 -> 30 Sept 2025 1253"

## Source disagreements
- **Walk Reconciliation** (error): Sum of bars: -12.0 bps (Source: ev-1) vs Stated Delta: +4.0 bps (Source: ev-20)
  Preferred: Stated Delta. The primary walk chart (ev-1) fails its sum check (start 1249 + bars -12 = 1237 != end 1253). The bank explicitly states the delta is +4 bps (ev-20). The residual of +16 bps captures this discrepancy.

## Limitations
- The primary walk chart (ev-1) contains a significant arithmetic error where the sum of drivers (-12 bps) does not reconcile with the stated movement (+4 bps). This results in an unexplained residual of +16 bps.
- Half-on-half data (ev-2, ev-3) was excluded from driver attribution as it covers a different period (Mar-25 to Sep-25).
- Specific sub-components of 'Total RWA' for the full year are not quantified in the primary walk; only the aggregate impact is provided.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- Failed check: walk_sum (start 1249 + bars -12.0 = 1237.0 != end 1253, tol 1.0) [WBC/FY25/results_announcement PDF p28 (ev-1)]

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T12:46:53+00:00
- seconds: 89.6
- cost_usd: 0.003
- tokens: 72643 in / 6693 out
- orchestration: pipeline
- pages_extracted: 18
- reference_follow: ['WBC/FY25/investor_discussion_pack p125 <- p78 page 125 [added]']
