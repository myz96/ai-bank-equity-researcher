# CBA — cash_earnings — FY26 vs FY25

**Movement (cash basis):** 10252$m → 10982$m (+730$m) | **Attribution confidence:** 40/100

CBA's cash NPAT from continuing operations increased $730 million (7%) to $10,982 million in FY26 compared to FY25 ($10,252 million). This growth was driven by lending volume expansion and a 3 basis point improvement in Net Interest Margin (NIM) to 2.05%. These positives were partially offset by higher operating expenses ($13,755 million, +6%) due to inflation and technology investments, as well as an increase in loan impairment expense ($788 million, +9%). Pre-provision profit grew 6% to $16.5 billion.

## Drivers

| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |
|---|---|---|---|---|---|
| `operating_expenses` | Operating expenses | -784 $m | 85 | 1 (single_source) | ev-11, ev-13 |
| `credit_impairment_charge` | Loan impairment expense | -64 $m | 85 | 1 (single_source) | ev-12, ev-3 |
| *residual (unexplained)* | — | +1578 $m | — | — |

### nii.volume
*unquantified | confidence 60/100*

Narrative confirms lending volume growth in core businesses supported earnings. No specific dollar contribution provided in source.
> [ev-3] CBA/FY26/asx_announcement, PDF p1: "Net profit after tax (NPAT) was supported by lending volume growth in our core businesses... This was partly offset by higher operating expenses primarily due to inflation and technology investments, and a higher loan impairment expense"

### nii.margin — "Net interest margin"
*unquantified | confidence 60/100*

NIM improved by 3 basis points to 2.05% in FY26. While positive for income, the specific dollar impact is not isolated from volume effects in the provided text.
> [ev-10] CBA/FY26/asx_announcement, PDF p2: "Net interest margin 2.05% 3bpts on FY25"

### operating_expenses — "Operating expenses"
*-784 $m | confidence 85/100*

Operating expenses increased by $784 million (6%) to $13,755 million, primarily due to inflation and technology investments. This negatively impacted cash earnings.
> [ev-11] CBA/FY26/asx_announcement, PDF p2: "Operating expenses $13,755m 6% on FY25"
> [ev-13] CBA/FY26/asx_announcement, PDF p2: "Investment spend of $2,428 million was up 6% on FY25"

### credit_impairment_charge — "Loan impairment expense"
*-64 $m | confidence 85/100*

Loan impairment expense increased by $64 million (9%) to $788 million, reducing net profit. This was cited as a headwind against volume and margin growth.
> [ev-12] CBA/FY26/asx_announcement, PDF p2: "Credit quality – loan impairment expense $788m 9% on FY25"
> [ev-3] CBA/FY26/asx_announcement, PDF p1: "Net profit after tax (NPAT) was supported by lending volume growth in our core businesses... This was partly offset by higher operating expenses primarily due to inflation and technology investments, and a higher loan impairment expense"

## Notable items
- Transaction costs and gains/(losses) on disposals: $15.5m (positive)
- Hedging and IFRS volatility: -$10.7m (negative)

## Source disagreements
- **Walk Chart Summation** (error): Start 1,025,200 bps + Bars (+4,800 bps) = 1,030,000 bps != End 1,098,200 bps vs Source: CBA/FY26/results_presentation PDF p23 (ev-1)
  Preferred: Profit Announcement Table (ev-14/ev-21). The walk chart extracted from the results presentation fails the sum check significantly. The bars provided (Transaction costs + Hedging) only account for a small fraction of the total movement. The Profit Announcement table provides the definitive absolute values for Cash NPAT.

## Limitations
- No quantified breakdown of NII volume vs margin contributions is available in the evidence records; attribution relies on narrative confirmation of volume growth and margin improvement.
- The residual of $1,578m represents the unquantified portion of the $730m delta after accounting for known expense and impairment increases. This likely includes the positive impact of NII growth (volume + margin) and other operating income, but these are not explicitly separated in dollars.
- Confidence is capped at 60 for drivers lacking explicit dollar quantification in the source documents.
- Failed check: walk_sum (start 1025200 + bars +4800.0 = 1030000.0 != end 1098200, tol 10.0)

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY25/profit_announcement (e2e911ab4fed)
- generated: 2026-08-26T06:17:55+00:00
- seconds: 75.0
- cost_usd: 0.0011
- tokens: 18269 in / 3958 out
- orchestration: pipeline
