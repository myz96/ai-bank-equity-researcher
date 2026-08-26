# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 13590$m (+3338$m) | **Attribution confidence:** 40/100

CBA cash earnings grew $3,338m (+32.6%) to $13,590m in FY26 vs FY25 ($10,252m). The results presentation walk chart attributes a +$210m movement to core drivers (NII, PCL, OOI, OpEx, Tax), implying a significant unquantified residual of ~$3,128m. While the Profit Announcement cites 7% growth (implying ~$11,000m), this contradicts the detailed walk chart endpoint of $13,590m. We prioritize the walk chart's explicit dollar endpoints for the delta calculation but flag the severe discrepancy with the PA narrative.

### nii.volume
*unquantified | confidence 80/100*

Net Interest Revenue contributed +450bps per the walk chart (ev-3). This is an unallocated mix of volume and margin effects; specific volume attribution is not provided in the evidence.
> [ev-3] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA cash earnings in FY26 vs FY25: FY25 Cash Earnings 13800.0 -> FY26 Cash Earnings 13590.0"

### credit_impairment_charge — "Provision for Credit Losses"
*unquantified | confidence 80/100*

PCL contributed -280bps per the walk chart (ev-3). No absolute dollar value or GLAA denominator is provided to convert bps to $m.
> [ev-3] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA cash earnings in FY26 vs FY25: FY25 Cash Earnings 13800.0 -> FY26 Cash Earnings 13590.0"

### other_operating_income — "Other Operating Income"
*unquantified | confidence 80/100*

OOI contributed +120bps per the walk chart (ev-3). Specific fee/trading/insurance breakdowns are not quantified in the evidence.
> [ev-3] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA cash earnings in FY26 vs FY25: FY25 Cash Earnings 13800.0 -> FY26 Cash Earnings 13590.0"

### operating_expenses — "Operating Expenses"
*unquantified | confidence 80/100*

OpEx contributed -310bps per the walk chart (ev-3). No absolute dollar value is provided.
> [ev-3] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA cash earnings in FY26 vs FY25: FY25 Cash Earnings 13800.0 -> FY26 Cash Earnings 13590.0"

### tax_and_other — "Tax Expense"
*unquantified | confidence 80/100*

Tax contributed -190bps per the walk chart (ev-3). No effective tax rate or absolute dollar value is provided.
> [ev-3] CBA/FY26/results_presentation, printed p2: "[walk chart] CBA cash earnings in FY26 vs FY25: FY25 Cash Earnings 13800.0 -> FY26 Cash Earnings 13590.0"

## Source disagreements
- **FY26 Cash Earnings Absolute Value** (definitional): 13590.0 — CBA/FY26/results_presentation PDF p2 (ev-3) vs ~11000.0 — CBA/FY26/profit_announcement PDF p2 (ev-12, ev-13)
  Preferred: 13590.0. The Walk Chart (ev-3) explicitly states FY26 Cash Earnings as $13,590m. However, the Profit Announcement (ev-12, ev-13) states profit growth was 7%. Applying 7% growth to the FY25 base of $10,252m yields ~$10,970m. The $13,590m figure implies ~32.6% growth. The PA narrative (ev-11) also cites 7% revenue growth. There is a material conflict between the detailed walk chart numbers and the high-level PA percentages.
- **Walk Chart Summation** (rounding): +210.0 bps sum of bars — CBA/FY26/results_presentation PDF p2 (ev-3) vs -210.0 bps implied by start/end if interpreted differently — Validation Error
  Preferred: +210.0 bps. The validation error noted 'walk_extraction_error'. The bars sum to +450 - 280 + 120 - 310 - 190 = -210 bps. The start point is 13,800 bps (likely $13,800m mislabeled as bps or a scaling error in the extraction). If the start is $13,800m and end is $13,590m, the delta is -$210m. However, the task requires comparing FY26 ($13,590m) to FY25 ($10,252m). The walk chart appears to be a reconciliation from a *different* starting point (perhaps FY26 prior year adjusted or a different metric) rather than a direct FY25-to-FY26 bridge. The 'start_bps' of 13800 matches the FY26 end label of the previous period? No, FY25 is 10252. The walk chart source (ev-3) has start_label 'FY25 Cash Earnings' but value 13800. This is a definitional mismatch: the label says FY25, the number says 13800. 13800 does not match FY25 Cash Earnings (10252). Thus, the walk chart does not actually bridge FY25 to FY26 as labeled.

## Limitations
- The primary walk chart (ev-3) contains a critical data integrity error: it labels the start point as 'FY25 Cash Earnings' but assigns it a value of 13,800, whereas FY25 Cash Earnings is confirmed as 10,252 (ev-4, ev-6, ev-9). Consequently, the bars in ev-3 do not reconcile the actual FY25 to FY26 movement.
- The Profit Announcement (ev-12, ev-13) claims 7% growth, which contradicts the $13,590m figure in the walk chart. Without a reconciled table showing the full bridge from $10,252m to the final FY26 number, we cannot attribute the $3,338m delta to specific canonical drivers with high confidence.
- Driver contributions are only available in basis points (ev-3) and cannot be converted to dollars without the correct average balance sheet denominators (GLAAs) and tax rates, which are not provided in the evidence records.
- Failed check: no_quantified_drivers
- Failed check: walk_extraction_error p2: walk endpoints unreadable on CBA/FY26/profit_announcement p2

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T05:59:44+00:00
- seconds: 76.4
- cost_usd: 0.0015
- tokens: 29255 in / 4578 out
- orchestration: pipeline
