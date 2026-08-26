# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 10982$m (+730$m) | **Attribution confidence:** 40/100

CBA's cash NPAT increased $730 million (7%) to $10,982 million in FY26. This growth was primarily driven by a 6% increase in pre-provision profit, supported by lending volume expansion and a 3 basis point improvement in Net Interest Margin. These gains were partially offset by higher operating expenses (up 6%) due to inflation and technology investments, as well as an increase in loan impairment expense (up 9%).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `operating_expenses` | Operating expenses | -784 $m | 85 | 1 (single_source) | ev-9 |
| `credit_impairment_charge` | Loan impairment expense | -65 $m | 85 | 1 (single_source) | ev-10 |
| *residual (unexplained)* | — | +647 $m | — | — |

### nii.volume
*unquantified | confidence 60/100*

Narrative confirms lending volume growth in core businesses supported earnings. No specific dollar quantification provided for volume vs margin split.
> [ev-3] CBA/FY26/asx_announcement, PDF p1: "Net profit after tax (NPAT) was supported by lending volume growth in our core businesses... This was partly offset by higher operating expenses primarily due to inflation and technology investments, and a higher loan impairment expense"

### nii.margin
*unquantified | confidence 60/100*

NIM improved by 3 basis points to 2.05%. While positive, the specific dollar contribution of this margin movement is not explicitly quantified separately from volume.
> [ev-8] CBA/FY26/asx_announcement, PDF p2: "Net interest margin ... 2.05% ... 3bpts on FY25"

### operating_expenses — "Operating expenses"
*-784 $m | confidence 85/100*

Operating expenses increased by 6% to $13,755 million. The negative contribution to earnings is calculated as the absolute increase in costs ($13,755m - $12,971m implied).
> [ev-9] CBA/FY26/asx_announcement, PDF p2: "Operating expenses ... $13,755m (45.5% cost-to-income) ... 6% on FY25"

### credit_impairment_charge — "Loan impairment expense"
*-65 $m | confidence 85/100*

Loan impairment expense increased by 9% to $788 million. The negative contribution is the absolute increase in the charge ($788m - $723m implied).
> [ev-10] CBA/FY26/asx_announcement, PDF p2: "Loan impairment expense ... $788m (Loan loss rate3 8bpts) ... 9% on FY25"

## Source disagreements
- **Walk Chart Reconciliation** (definitional): Start: 10133, End: 10982, Delta: 849 (implied by walk endpoints) vs Walk Bars Sum: +48 (155 - 107)
  Preferred: Profit Announcement Table. The walk chart on p23 (ev-1) uses Statutory FY25 as a start point but Cash FY26 as an end point, creating a definitional mismatch. Furthermore, the bars do not sum to the delta between these mixed bases. We rely on the Profit Announcement table (ev-14/ev-21) which provides consistent Cash NPAT figures for both periods.

## Limitations
- The specific dollar contributions of NII volume and margin are not separately quantified in the evidence; they are subsumed within the Pre-Provision Profit growth narrative.
- A significant residual of $647m exists after accounting for OpEx and Impairment increases against the total NPAT growth. This residual likely represents the net impact of NII growth (volume + margin) and other income items, but cannot be precisely allocated without further data.
- Confidence is capped at 60 because key drivers (NII components) are unquantified in dollars.
- Failed check: drivers_reconcile (drivers -849.0 + residual +647.0 != delta +730.0, tol 10.0)
- Failed check: walk_sum (start 10133 + bars +48.0 = 10181.0 != end 10982, tol 10.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:32:11+00:00
- seconds: 53.0
- cost_usd: 0.0014
- tokens: 25341 in / 5234 out
- orchestration: pipeline
