# CBA — impairment — FY26 vs FY25

**Movement (statutory basis):** 802$m → 726$m (-76$m) | **Attribution confidence:** 40/100

CBA's statutory loan impairment expense decreased by $76 million (9%) to $726 million in FY25 (note: source data covers FY25 vs FY24; FY26 specific data is not provided in the evidence set). The decline was driven by lower provisions across both Retail and Business Banking segments, with Business Banking contributing the largest absolute reduction.

### collective.asset_quality
*unquantified | confidence 60/100*

Aggregate impairment declined significantly. Business Banking saw a $84 million drop (from $437m to $353m) and Retail Banking fell $45 million (from $319m to $274m), suggesting improved risk migration or reduced collective provisioning requirements relative to the prior year.
> [ev-5] CBA/FY25/profit_announcement, printed p18: "Retail Banking Services | 274 | 319 | (14)"
> [ev-6] CBA/FY25/profit_announcement, printed p18: "Business Banking | 353 | 437 | (19)"

## Limitations
- The task requests FY26 vs FY25 analysis, but the provided evidence records (ev-1 through ev-9) exclusively contain FY25 full-year results compared against FY24 comparatives. No FY26 data exists in the source hierarchy.
- A residual of $53 million remains unexplained because segment-level deltas ($84m + $45m = $129m decrease) do not sum to the total headline decrease ($76m). This discrepancy likely arises from other segments (e.g., Corporate/Institutional) increasing provisions or unmapped components, which are not detailed in the provided evidence.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:02:11+00:00
- seconds: 29.2
- cost_usd: 0.0008
- tokens: 16725 in / 2068 out
- orchestration: pipeline
