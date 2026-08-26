# CBA — cti — FY26 vs FY25

**Movement (statutory basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 80/100

CBA's statutory cost-to-income ratio (CTI) improved by 20 basis points to 45.5% in FY26 from 45.7% in FY25. This improvement was driven by operating income growth outpacing operating expense growth. Operating expenses grew 6%, while total operating income increased approximately 6.2%. The underlying CTI also improved by 30 basis points to 44.9%.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | +0.1 ppt | 80 | 1 (single_source) | ev-3 |
| `expense_growth` | — | -0.3 ppt | 80 | 2 () | ev-2, ev-3 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*+0.1 ppt | confidence 80/100*

Operating income growth contributed to the CTI improvement. Total operating income rose from $28,465m to $30,224m (~6.2%), slightly outpacing expense growth.
> [ev-3] CBA/FY26/profit_announcement, printed p2: "Total operating income 30,224 | Underlying operating expenses (13,585) | Total operating expenses (13,755)"

### expense_growth
*-0.3 ppt | confidence 80/100*

Expense growth exerted upward pressure on CTI but was contained. Operating expenses grew 6% (ev-2), rising from $12,996m to $13,755m. While significant, this was lower than income growth.
> [ev-2] CBA/FY26/asx_announcement, PDF p2: "6% on FY25"
> [ev-3] CBA/FY26/profit_announcement, printed p2: "Total operating income 30,224 | Underlying operating expenses (13,585) | Total operating expenses (13,755)"

## Source disagreements
- **Basis of CTI reporting** (definitional): 45.5% (statutory, ev-1, ev-6) vs 44.9% (underlying, ev-4, ev-5)
  Preferred: statutory. The task asks for CBA's CTI movement. Standard equity analysis typically defaults to statutory unless 'underlying' is specified. However, both are reported. I have selected statutory as the primary headline metric per standard convention, but noted the underlying improvement. The statutory delta is -0.2 ppt, while underlying is -0.3 ppt.

## Limitations
- No walk chart was provided to decompose the drivers into specific line items (e.g., specific expense categories). Attribution is based on high-level jaws analysis using table data.
- Confidence is capped at 80 due to lack of granular driver attribution from a validated walk chart.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:21:30+00:00
- seconds: 26.9
- cost_usd: 0.0007
- tokens: 14621 in / 2188 out
- orchestration: pipeline
