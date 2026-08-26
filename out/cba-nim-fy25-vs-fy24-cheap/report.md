# CBA — nim — FY25 vs FY24

**Movement (statutory basis):** 1.99bps → 2.08bps (+9bps) | **Attribution confidence:** 40/100

CBA's statutory NIM increased 9 bps to 2.08% in FY25 (FY24: 1.99%). This was driven by a 7 bps benefit from reduced liquid assets/pooled facilities drag and 9 bps from capital/replicating earnings, partially offset by 7 bps of higher funding costs and 1 bp of basis risk. Underlying NIM improved only 2 bps.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `liquids` | Liquids & Pooled Facilities | +7 bps | 85 | 1 (single_source) | ev-1, ev-3, ev-4, ev-16 |
| `capital_replicating` | Capital, Replicating and Other | +9 bps | 85 | 1 (single_source) | ev-1, ev-10, ev-16 |
| `funding` | Funding costs | -7 bps | 85 | 1 (single_source) | ev-1, ev-10 |
| `basis_risk` | Basis risk | -1 bps | 85 | 1 (single_source) | ev-1, ev-10 |

### liquids — "Liquids & Pooled Facilities"
*+7 bps | confidence 85/100*

Reduction in lower-yielding liquid assets and institutional pooled facilities provided a 7 bps margin benefit compared to FY24.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-3] CBA/FY25/profit_announcement, PDF p9: "Net interest margin 2.08% ... 9bpts on FY24 (+2bpts underlying basis)"
> [ev-4] CBA/FY25/profit_announcement, PDF p9: "Excluding the mix effect of lower liquid assets and institutional pooled facilities, margins improved by 2bpts."
> [ev-16] CBA/FY25/profit_announcement, printed p12: "The Bank’s net interest margin increased 9 basis points on the prior year to 2.08%. Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities... net interest margin increased 2 basis points."

### capital_replicating — "Capital, Replicating and Other"
*+9 bps | confidence 85/100*

Higher earnings on the replicating portfolio contributed 9 bps to the margin expansion.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-10] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"
> [ev-16] CBA/FY25/profit_announcement, printed p12: "The Bank’s net interest margin increased 9 basis points on the prior year to 2.08%. Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities... net interest margin increased 2 basis points."

### funding — "Funding costs"
*-7 bps | confidence 85/100*

Lower deposit margins due to competition, unfavorable mix shift to higher-yielding deposits, and declining interest rates resulted in a 7 bps headwind.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-10] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

### basis_risk — "Basis risk"
*-1 bps | confidence 85/100*

Higher basis risk arising from an increase in the spread between the 3-month bank bill swap rate and the 3-month overnight index swap rate caused a 1 bps drag.
> [ev-1] CBA/FY25/profit_announcement, printed p12: "[walk chart] NIM Movement since June 2024: Jun 24 Full Year 199 -> Jun 25 Full Year 208"
> [ev-10] CBA/FY25/profit_announcement, printed p42: "Net interest margin decreased by 3 basis points on the prior year, reflecting: • Lower deposit margins mainly due to competition, unfavourable mix as customers shift to higher yielding deposits and the impact of declining interest rates; • Lower home lending margins principally reflecting elevated competition; and • The impact of higher basis risk arising from an increase in the spread between the 3 month bank bill swap rate and the 3 month overnight index swap rate; partly offset by • Higher earnings on the replicating portfolio; • Favourable portfolio mix primarily due to the benefit of stro"

## Notable items
- Liquids & Pooled Facilities reduction (7 bps)

## Source disagreements
- **NIM Basis Definition** (definitional): 9 bps increase (Statutory) — ev-3, ev-15, ev-16, ev-17 vs -3 bps decrease (Cash) — ev-5, ev-6, ev-10, ev-11, ev-12
  Preferred: Statutory. The statutory walk (ev-1) sums exactly to the reported statutory movement (+9 bps). The cash basis shows a decline (-3 bps) but lacks a corresponding validated driver walk in the evidence set for attribution. Per source hierarchy, the Profit Announcement narrative and tables prioritize the statutory view for the primary NIM discussion.

## Limitations
- Asset pricing and Portfolio mix are reported as 0 bps in the statutory walk; however, narrative mentions 'elevated competition' affecting home lending margins (ev-10), which may be netted within other categories or immaterial at this aggregation level.
- Cash basis NIM drivers are not fully quantified in the provided evidence records.
- Failed check: movement_arithmetic (1.99 + 9.0 != 2.08)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T05:55:54+00:00
- seconds: 130.7
- cost_usd: 0.0015
- tokens: 28961 in / 4907 out
- orchestration: pipeline
