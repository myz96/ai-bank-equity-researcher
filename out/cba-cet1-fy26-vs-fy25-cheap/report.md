# CBA — cet1 — FY26 vs FY25

**Movement (cash basis):** 1230bps → 1200bps (-30bps) | **Attribution confidence:** 60/100

*Read from: row 'Common Equity Tier 1 (CET1)', column 31 Dec 25 -> column 30 Jun 26*

CBA's Level 2 CET1 ratio decreased by 30 bps to 12.0% in FY26 from 12.3% in FY25. The decline was driven by dividends and RWA growth, partially offset by earnings generation.

### earnings_generation — "Cash NPAT"
*unquantified | confidence 70/100*

Organic capital generation from earnings supported the ratio. The half-on-half walk shows +106 bps for Cash NPAT (ev-1). No specific FY25-FY26 quantification is provided.
> [ev-6] CBA/FY26/profit_announcement, PDF p48: "Key drivers of the change in CET1 for the 6 months ended 30 June 2026 were: • Capital generated from earnings; partly offset by • Payment of the 1H26 dividend;"

### dividend_net_drp — "Dividend"
*unquantified | confidence 70/100*

The payment of the 1H26 dividend reduced the ratio. The half-on-half walk shows a -76 bps impact for the 1H26 dividend (DRP neutralised) (ev-1).
> [ev-6] CBA/FY26/profit_announcement, PDF p48: "Key drivers of the change in CET1 for the 6 months ended 30 June 2026 were: • Capital generated from earnings; partly offset by • Payment of the 1H26 dividend;"
> [ev-8] CBA/FY26/profit_announcement, PDF p48: "Dividend (76)"

### rwa — "RWA"
*unquantified | confidence 70/100*


> [ev-9] CBA/FY26/profit_announcement, PDF p48: "Credit (38)"
> [ev-10] CBA/FY26/profit_announcement, PDF p48: "IRRBB (16)"
> [ev-16] CBA/FY26/results_presentation, printed p32: "Movements in bpts Credit Risk4 (38) IRRBB (16) Market Risk 8 Operational Risk - 3 Underlying movement Jun 26 vs Jun 25"

### deductions_other — "Other"
*unquantified | confidence 70/100*

Other regulatory adjustments had an impact. The half-on-half walk shows -8 bps for Other (ev-1).
> [ev-11] CBA/FY26/profit_announcement, PDF p48: "Other 8"

## Source disagreements
- **Comparison Span Mismatch** (definitional): Context: Half-on-half walk (Dec 25 -> Jun 26) used for driver context only vs Task: Full-year comparison (Jun 25 -> Jun 26)
  Preferred: Full-year comparison. The bank published a capital walk for the half-on-half period (Dec 25 -> Jun 26) but did not provide a quantified full-year (FY25 -> FY26) walk. The half-on-half bars cannot be attributed to the full-year delta.

## Limitations
- No full-year (FY25 vs FY26) capital walk was published. Driver contributions are unquantified for the task period.
- The residual (-30 bps) represents the total delta as no primary walk drivers were available to decompose it.
- Failed check: no_quantified_drivers
- No published walk covers FY26 vs FY25: the bank's walk for this metric describes another comparison, so the driver split is not walk-verified for this comparison. Confidence is capped at 85.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T13:23:14+00:00
- seconds: 153.5
- cost_usd: 0.0024
- tokens: 56582 in / 5777 out
- orchestration: pipeline
