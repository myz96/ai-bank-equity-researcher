# CBA — cti — FY26 vs FY25

**Movement (statutory basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 95/100

CBA's statutory cost-to-income ratio (CTI) improved by 20 basis points to 45.5% in FY26 from 45.7% in FY25 (ev-1, ev-7). This improvement was driven by operating income growth outpacing underlying operating expense growth. Operating expenses grew 6% (ev-2), while total operating income increased from $28,465m to $30,224m, a growth rate of approximately 6.2%. The faster income growth compressed the ratio despite rising costs.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | +0.2 ppt | 95 | 2 () | ev-2, ev-4 |

### income_growth
*+0.2 ppt | confidence 95/100*

Operating income growth (~6.2%) exceeded expense growth (6%), mechanically improving the CTI. Calculated from ev-4 ($28,465m to $30,224m) and ev-2 (6% expense growth).
> [ev-2] CBA/FY26/asx_announcement, PDF p2: "6% on FY25"
> [ev-4] CBA/FY26/profit_announcement, printed p2: "Group Performance Summary"

## Source disagreements
- **Basis of CTI reporting** (definitional): 45.5% (statutory, ev-1, ev-7) vs 44.9% (underlying, ev-5, ev-6)
  Preferred: statutory. The task asks for CBA's CTI movement. Standard equity analysis typically uses the headline statutory or cash-basis CTI unless 'underlying' is specified. Ev-1 and Ev-7 provide the statutory view (45.5%, -20bps). Ev-5/6 provide the underlying view (44.9%, -30bps). These are different metrics due to exclusion of notable items. I have selected the statutory basis as it is the primary reported headline figure in the ASX announcement table (ev-1).

## Limitations
- No walk chart provided to decompose drivers further than jaws effect.
- Underlying vs Statutory basis disagreement noted; statutory chosen as primary.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:34:49+00:00
- seconds: 37.6
- cost_usd: 0.0007
- tokens: 14593 in / 1962 out
- orchestration: pipeline
