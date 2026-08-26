# NAB — nim — FY25 vs FY24

**Movement (statutory basis):** 171bps → 174bps (+3bps) | **Attribution confidence:** 95/100

NAB's statutory Net Interest Margin (NIM) increased by 3 basis points in FY25 compared to FY24, rising from 171 bps to 174 bps. This improvement was primarily driven by a positive benefit from net free liabilities, provisions, and equity (+5 bps), which more than offset a decline in the net interest spread (-2 bps). While cash NIM declined slightly due to different accounting treatments of volatile items, the statutory view highlights the core operational resilience.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `other_unmapped` | Benefit of net free liabilities, provisions and equity | +5 bps | 85 | 1 (single_source) | ev-2 |
| `other_unmapped` | Net interest spread | -2 bps | 85 | 1 (single_source) | ev-2 |

### other_unmapped — "Benefit of net free liabilities, provisions and equity"
*+5 bps | confidence 85/100*

A positive contribution of 5 bps attributed to the benefit of net free liabilities, provisions, and equity. This is a residual category in the statutory walk that captures non-core or structural benefits not classified as pure lending or funding margins.
> [ev-2] NAB/FY25/results_book, printed p64: "[walk chart] NAB net interest margin in FY25 vs FY24: Sep 24 171.0 -> Sep 25 174.0"

### other_unmapped — "Net interest spread"
*-2 bps | confidence 85/100*

A negative contribution of 2 bps from the net interest spread. This reflects the difference between asset yields and funding costs before specific mix or pricing adjustments captured elsewhere.
> [ev-2] NAB/FY25/results_book, printed p64: "[walk chart] NAB net interest margin in FY25 vs FY24: Sep 24 171.0 -> Sep 25 174.0"

## Source disagreements
- **Cash vs Statutory NIM Movement** (definitional): Statutory: +3 bps (171 -> 174) - ev-6, ev-7 vs Cash: -4 bps (311 -> 307) - ev-3
  Preferred: Statutory. The task asks for NAB's NIM movement. The statutory basis (+3 bps) is the primary reported metric in the Profit Announcement results book (ev-6, ev-7) and aligns with the detailed statutory walk chart (ev-2). The cash basis (-4 bps) excludes certain volatile items (Markets & Treasury) and represents a different performance view. We prioritize the statutory basis as it is the headline statutory profit driver.

## Limitations
- The primary attribution evidence (ev-2) uses a simplified two-bar walk ('Net interest spread' and 'Benefit of net free liabilities...') rather than the granular canonical drivers (Lending margin, Funding, etc.) found in the H1 walk (ev-1). Therefore, we cannot attribute the movement to specific canonical IDs like 'asset_pricing' or 'funding.deposits' with high confidence for the full year.
- The H1 walk (ev-1) provides granular canonical drivers but covers Mar 25 to Sep 25, not the full FY24 vs FY25 comparison required. It is used only for context if needed, but the FY25 vs FY24 statutory delta is strictly defined by ev-2.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-26T06:22:22+00:00
- seconds: 52.0
- cost_usd: 0.0009
- tokens: 18699 in / 2589 out
- orchestration: pipeline
