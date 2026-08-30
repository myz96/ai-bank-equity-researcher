# NAB — roe — FY25 vs FY24

**Movement (cash basis):** 11.6ppt → 11.4ppt (-0.2ppt) | **Attribution confidence:** 80/100

*Read from: row 'Cash return on equity', column FY24 -> column FY25*

NAB's Cash ROE declined by 20 bps to 11.4% in FY25 (ev-8). Earnings fell $11m to $7,091m against a flat equity base of ~$62.4bn (ev-4, ev-5), driving a negative earnings effect. Equity growth provided a small offsetting positive contribution.

> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `earnings_effect` | — | -0.03 ppt | 80 | 1 (single_source) | ev-4, ev-6, ev-8 |
| `equity_effect` | — | -0.17 ppt | 80 | 1 (single_source) | ev-5, ev-8 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### earnings_effect
*-0.03 ppt | confidence 80/100*

Derived: Prior ROE (11.6%) x Earnings Growth (-0.15%). Earnings fell $11m to $7,091m (ev-4). Contribution is derived, not disclosed.
> [ev-4] NAB/FY25/results_book, PDF p71: "Cash earnings 7,091 7,102"
> [ev-6] NAB/FY25/results_book, PDF p71: "Cash return on equity 11.4% 11.6%"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"

### equity_effect
*-0.17 ppt | confidence 80/100*

Derived: Total delta (-0.2 ppt) minus earnings effect (-0.03 ppt). Equity grew from $61,039m to $62,355m (ev-5). Higher average equity reduced the ratio. Contribution is derived, not disclosed.
> [ev-5] NAB/FY25/results_book, PDF p71: "Total average equity (attributable to owners of the Company) ($m) 62,355 61,039"
> [ev-8] NAB/FY25/results_book, printed p8: "Cash return on equity 11.4% 11.6% (20 bps) 11.0% 11.7% (70 bps)"

## Source disagreements
- **Cash ROE FY25 Level** (definitional): 11.4% (Results Book) vs 10.7% (Investor Presentation)
  Preferred: 11.4%. The Results Book (audited source hierarchy) reports 11.4%. The IP likely uses a different denominator or basis.

## Limitations
- Drivers are mathematically derived using the identity ROE = Earnings/Equity. The bank does not explicitly split the movement into these two canonical components in the provided text.
- Confidence capped at 80 due to derivation and disagreement on the FY25 level between sources.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: NAB/FY25/results_book (df0445a6cd54), NAB/FY25/investor_presentation (de3a394e6e1a)
- generated: 2026-08-30T14:59:36+00:00
- seconds: 34.1
- cost_usd: 0.0016
- tokens: 33504 in / 4433 out
- orchestration: pipeline
- pages_extracted: 15
- reference_follow: ['NAB/FY25/investor_presentation p39 <- p5 page 39', 'NAB/FY25/investor_presentation p10 <- p39 page 10 [added]']
