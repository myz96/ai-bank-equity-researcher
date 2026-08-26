# CBA — roe — FY26 vs FY25

**Movement (cash basis):** 13.6ppt → 13.5ppt (-0.1ppt) | **Attribution confidence:** 40/100

CBA's cash ROE declined by 10 basis points to 13.5% in FY25 (vs FY24). The statutory ROE rose by 30 bps to 13.4%. Due to the absence of a validated walk chart for FY25 vs FY24, specific driver attribution is not possible; the movement reflects the net result of earnings and equity changes.

### other_unmapped
*unquantified | confidence 40/100*

No validated walk chart exists for the FY25 vs FY24 period. Therefore, quantified drivers cannot be attributed. The decline in cash ROE implies either lower core profit or higher average equity relative to the prior year, but exact contributions are unknown.
> [ev-2] CBA/FY25/profit_announcement, printed p3: "Return on equity (ROE) (%) Cash basis 13.5 13.6 (10)bpts"

## Source disagreements
- **ROE Basis Movement** (definitional): Cash: -10 bps (ev-2) vs Statutory: +30 bps (ev-1)
  Preferred: Cash. Cash and statutory ROE moved in opposite directions. Cash basis is preferred for operational performance analysis as it excludes non-cash items.

## Limitations
- The task requests FY26 vs FY25 analysis, but evidence records only cover FY25 vs FY24. Analysis performed on available data (FY25 vs FY24).
- No walk charts were provided for the relevant period, preventing quantified driver attribution per validation rules.
- Confidence is capped due to lack of granular driver data.
- Failed check: no_quantified_drivers

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:00:16+00:00
- seconds: 31.7
- cost_usd: 0.0006
- tokens: 12746 in / 1685 out
- orchestration: pipeline
