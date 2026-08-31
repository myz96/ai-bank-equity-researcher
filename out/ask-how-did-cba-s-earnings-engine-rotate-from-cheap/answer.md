# Q: How did CBA's earnings engine rotate from FY25 to FY26, and was FY26's faster cash-NPAT growth higher quality despite reported NIM compression and a higher loan-loss rate? Reconcile the two years' income/expense/impairment mix with CBA's own FY26 margin bridge.

*CBA, periods FY26, FY25 — confidence 95/100*

CBA's earnings engine rotated from volume-driven growth to a mix of volume, pricing, and expense discipline. FY26 Cash NPAT grew 7% ($10.98bn) [ev-1], outpacing the 6% Pre-Provision Profit (PPP) growth [ev-2]. This acceleration occurred despite reported NIM compression in specific segments (e.g., IB&M ex Markets fell to 188bps) [ev-52] and higher loan impairment expense (+$62m) [ev-24]. The quality is high because underlying NIM remained broadly stable due to an 8% AIEA increase [ev-25], while operating expenses grew only 5.6%, lagging income growth [ev-47]. Reconciliation: Operating Income rose 6.2% ($30.2bn) [ev-46], offsetting 5.6% OpEx growth ($13.6bn) [ev-47] and $788m LIE [ev-41]. The 'reported' NIM compression reflects segmental mix/competition, but aggregate underlying NIM was stable, allowing PPP to support faster bottom-line growth.

## Key facts

- FY26 Cash NPAT grew 7% to $10.98bn, driven by 6% Op Income growth.
  > [ev-1] CBA/FY26/profit_announcement, PDF p8: "Cash net profit after tax increased 7% to $11bn"
  > [ev-46] CBA/FY26/results_presentation, printed p7: "Operating income FY25 28,465 FY26 30,224 +6.2%"
- Underlying NIM was broadly stable despite segmental pressure; AIEA grew 8%.
  > [ev-4] CBA/FY26/profit_announcement, PDF p8: "underlying net interest margin broadly stable"
  > [ev-25] CBA/FY26/profit_announcement, printed p3: "Net interest income increased 7%, primarily driven by an 8% or $92 billion increase in Average Interest Earning Assets (AIEA). Excluding the impact of liquid assets, underlying Net Interest Margin (NIM) was stable."
- Loan Impairment Expense increased $62m to $788m, reflecting portfolio growth.
  > [ev-24] CBA/FY26/profit_announcement, printed p3: "The result was driven by a 6% increase in operating income and a 6% increase in operating expenses 2, as well as a $62 million increase in loan impairment expense."
  > [ev-41] CBA/FY26/results_presentation, printed p24: "Loan impairment expense 788 8.5% 47.0%"
- Operating Expenses grew 5.6% to $13.6bn, lagging Op Income growth.
  > [ev-47] CBA/FY26/results_presentation, printed p7: "Operating expenses FY25 12,866 FY26 13,585 +5.6%"

## Limitations
- The prompt asks for a 'margin bridge' reconciliation which typically requires a detailed waterfall chart not fully provided in text form; I have reconstructed it using narrative drivers and segmental NIM data.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- queries: ["How did CBA's earnings engine rotate from FY25 to FY26, and was FY26's faster cash-NPAT growth higher quality despite reported NIM compression and a higher loan-loss rate? Reconcile the two years' income/expense/impairment mix with CBA's own FY26 margin bridge.", 'CBA FY26 margin bridge NIM compression NPAT growth', '"earnings engine" rotation CBA annual report FY25 FY26', 'CBA loan loss provisions impairment expense quality FY26']
- pages_read: ['CBA/FY26/profit_announcement p11', 'CBA/FY26/profit_announcement p8', 'CBA/FY26/profit_announcement p29', 'CBA/FY26/profit_announcement p118', 'CBA/FY26/profit_announcement p26', 'CBA/FY26/profit_announcement p45', 'CBA/FY26/results_presentation p69', 'CBA/FY26/results_presentation p24', 'CBA/FY26/results_presentation p7', 'CBA/FY26/results_presentation p9', 'CBA/FY26/results_presentation p28', 'CBA/FY26/results_presentation p63']
- generated: 2026-08-31T01:09:37+00:00
- seconds: 81.7
- cost_usd: 0.0022
- tokens: 32166 in / 9222 out
