# CBA — nim — FY25 vs FY24

**Movement (cash basis):** 199bps → 208bps (+9bps) | **Attribution confidence:** 95/100

CBA's reported Net Interest Margin (NIM) increased by 9 basis points to 208 bps in FY25 compared to 199 bps in FY24. This headline increase was primarily driven by a 7 bps reduction in the drag from liquid assets and pooled facilities, alongside a 9 bps contribution from capital replicating portfolio earnings. Underlying NIM, excluding these volatile items, increased by only 2 bps, reflecting offsetting headwinds from funding costs (-7 bps) and basis risk (-1 bps).

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-15 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1, ev-5 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-5 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1, ev-5 |
| `markets_treasury` | Treasury and Markets | +1 bps | 85 | 1 (single_source) | ev-1 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

A positive 7 bps contribution resulting from a reduction in lower-yielding liquid assets and institutional pooled facilities.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-15] CBA/FY25/profit_announcement, printed p12: "The Bank’s net interest margin increased 9 basis points on the prior year to 2.08%. Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities... net interest margin increased 2 basis points."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

A positive 9 bps contribution driven by higher earnings on the replicating portfolio.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-5] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### funding — "Funding costs"
*-7 bps | confidence 85/100*

A negative 7 bps impact from funding costs, mainly due to competition, unfavorable mix shift to higher-yielding deposits, and declining interest rates.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-5] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

A negative 1 bps impact arising from an increase in the spread between the 3-month bank bill swap rate and the 3-month overnight index swap rate.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-5] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### markets_treasury — "Treasury and Markets"
*+1 bps | confidence 85/100*

A small positive 1 bps contribution from Treasury and Markets activities.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"

## Notable items
- Reduction in liquid assets and institutional pooled facilities

## Source disagreements
- **Cash vs Reported NIM Movement** (definitional): -3 bps — CBA Australia segment cash basis (ev-4, ev-5, ev-7) vs +9 bps — Total Group reported cash basis (ev-3, ev-14, ev-16)
  Preferred: +9 bps. The task asks for CBA's net interest margin. The evidence contains two distinct metrics: the 'Australia' segment cash NIM (which decreased 3 bps) and the 'Total Group' reported NIM (which increased 9 bps). The walk chart (ev-1) and primary narrative (ev-14, ev-15) explicitly attribute the +9 bps movement to specific drivers summing to that delta. The -3 bps figure refers specifically to the domestic Australia segment cash basis, which excludes international operations and other group entities included in the total group reported NIM. Given the detailed driver breakdown aligns with the +9 bps figure, this is the correct attribution for the consolidated entity.

## Limitations
- The analysis focuses on the Total Group reported NIM (+9 bps) as it is the only metric supported by a complete, validated walk chart attribution. The Australia segment cash NIM decrease (-3 bps) lacks a corresponding detailed driver walk in the provided evidence.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:29:58+00:00
- seconds: 51.4
- cost_usd: 0.0012
- tokens: 24670 in / 3620 out
- orchestration: pipeline
