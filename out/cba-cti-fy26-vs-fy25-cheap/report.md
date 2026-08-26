# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45ppt → 45.7ppt (+70ppt) | **Attribution confidence:** 40/100

CBA's statutory cost-to-income ratio (CTI) increased by 70 basis points to 45.7% in FY25 (vs FY24). This deterioration was driven by operating expense growth outpacing income growth. The underlying CTI also rose by 60 basis points to 45.2%, indicating a structural shift in efficiency metrics despite the exclusion of notable items.

### expense_growth — "Operating expenses growth vs FY24"
*unquantified | confidence 80/100*

Operating expenses grew 6% year-on-year, contributing to the ratio increase as income growth did not fully offset this expense expansion.
> [ev-2] CBA/FY25/profit_announcement, PDF p9: "6% on FY24"

### notable_items — "Underlying vs Total CTI"
*unquantified | confidence 90/100*

The total CTI (45.7%) exceeded the underlying CTI (45.2%) by 50 basis points, implying that notable items negatively impacted the headline ratio relative to the core business performance.
> [ev-1] CBA/FY25/profit_announcement, PDF p9: "$12,996m (45.7% cost-to-income)"
> [ev-4] CBA/FY25/profit_announcement, PDF p31: "Underlying operating expenses to underlying operating income (%)"
> [ev-5] CBA/FY25/profit_announcement, PDF p31: "Operating expenses to total operating income (%)"

## Notable items
- Notable items contributed to the spread between total and underlying CTI.

## Source disagreements
- **CTI Value Definition** (definitional): 45.7% - ev-1 (Total) vs 39.1% - ev-7 (Operating exp to Operating Income)
  Preferred: 45.7%. ev-1 and ev-5 define CTI as 'Operating expenses to total operating income' yielding 45.7%. ev-7 defines it as 'Operating expenses to operating income' yielding 39.1%. The task asks for the standard banking CTI which typically uses Total Operating Income; furthermore, the delta in ev-7 (60 bpts) matches the underlying delta in ev-6, suggesting ev-7 might be referencing the underlying metric or a different denominator scope. We prioritize the explicit 'Total' label in ev-1/ev-5 for the headline movement.

## Limitations
- The task requests FY26 vs FY25 analysis, but all provided evidence records (ev-1 through ev-8) pertain to FY25 vs FY24 comparisons. No FY26 data is available in the source hierarchy.
- Quantified driver contributions (Jaws split) are not explicitly provided in the evidence; only aggregate expense growth (6%) is cited. Therefore, specific contribution values for income vs expense drivers cannot be calculated with certainty.
- Confidence is capped at 80 due to the period mismatch (FY24/FY25 data used for FY25/FY26 query) and lack of granular Jaws decomposition.
- Failed check: movement_arithmetic (45.0 + 70.0 != 45.7)
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:02:42+00:00
- seconds: 31.1
- cost_usd: 0.0008
- tokens: 14668 in / 2456 out
- orchestration: pipeline
