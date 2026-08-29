# CBA — cti — FY26 vs FY25

**Movement (cash basis):** 45.7ppt → 45.5ppt (-0.2ppt) | **Attribution confidence:** 90/100

*Read from: row 'Operating expenses to total operating income (%)', column FY25 -> column FY26*

CBA's headline cost-to-income ratio improved by 20 basis points (45.7% to 45.5%) in FY26. This improvement was driven by a positive Jaws effect where operating income growth (+6.2%) outpaced underlying operating expense growth (+5.6%). The movement is consistent with the bank's narrative of efficiency gains and income growth.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `income_growth` | — | +0.1 ppt | 90 | 2 () | ev-28, ev-3 |
| `expense_growth` | — | -0.3 ppt | 90 | 2 () | ev-29, ev-7, ev-5, ev-6, ev-3 |
| *residual (unexplained)* | — | +0 ppt | — | — |

### income_growth
*+0.1 ppt | confidence 90/100*

Operating income grew 6.2% ($28,465m to $30,224m), providing a positive Jaws contribution that offset expense growth.
> [ev-28] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
> [ev-3] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"

### expense_growth
*-0.3 ppt | confidence 90/100*

Underlying operating expenses grew 5.6% ($12,866m to $13,585m). Key drivers included IT services (+$393m/16%) and staff costs (+$288m/4%), partially offset by lower occupancy (-$19m/2%).
> [ev-29] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"
> [ev-7] CBA/FY26/profit_announcement, PDF p31: "Information technology services expenses increased by $393 million or 16% to $2,782 million"
> [ev-5] CBA/FY26/profit_announcement, PDF p31: "Staff expenses increased by $288 million or 4% to $8,258 million"
> [ev-6] CBA/FY26/profit_announcement, PDF p31: "Occupancy and equipment expenses decreased by $19 million or 2% to $938 million"
> [ev-3] CBA/FY26/profit_announcement, PDF p31: "Operating expenses to total operating income (%) 45.5 45.7 (20)bpts 45.2 45.9 (70)bpts"

## Source disagreements
- **Underlying CTI Definition** (definitional): 44.9% (ev-2) vs 45.2% (ev-10)
  Preferred: 44.9%. ev-2 reports the Underlying CTI as 44.9% for FY26. ev-10 reports it as 45.2%. The table in ev-2 is the primary KPI source; ev-10 appears to be a text summary error or refers to a different period.

## Limitations
- The bank does not provide a formal bridge walk chart for the headline CTI. Contributions are derived from the disclosed Jaws components (Income and Expense growth rates) rather than a published driver table.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-29T18:05:01+00:00
- seconds: 43.8
- cost_usd: 0.0019
- tokens: 34676 in / 6750 out
- orchestration: pipeline
- pages_extracted: 14
- reference_follow: ['CBA/FY26/profit_announcement p31 <- p32 page 15']
