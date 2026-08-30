# WBC — impairment — FY25 vs FY24

**Movement (ex_notables basis):** 537$m → 424$m (-113$m) | **Attribution confidence:** 40/100

*Read from: row 'Impairment (charges)/benefits', column Full Year Sept 2024 -> column Full Year Sept 2025*

Westpac's credit impairment charge fell $113 million to $424 million in FY25 from $537 million in FY24, a 21% reduction. The loss rate on average loans declined from 7 bps to 5 bps. The improvement was driven mainly by a $174 million swing in individually assessed provisions (IAPs) — from a $140 million net charge to a $34 million net benefit — due to higher write-backs (+$102m) and recoveries (+$57m), partly offset by a $61 million increase in collectively assessed provision (CAP) charges, primarily from higher write-offs (+$75m). Divisionally, Institutional swung from a $120 million charge to a $1 million benefit (+$121m) and New Zealand from a $25 million charge to a $41 million benefit (+$66m), while Business & Wealth saw its charge rise $103 million to $245 million.

> [ev-2] WBC/FY25/results_announcement, PDF p9: "Impairment (charges)/benefits (424) (537)"
> [ev-3] WBC/FY25/results_announcement, PDF p9: "Credit impairment charges of $424 million represented 5 basis points of average gross loans compared to 7 basis points of average gross loans in the prior year."
> [ev-11] WBC/FY25/results_announcement, PDF p21: "Total impairment (charges)/benefits (424) (537)"
> [ev-12] WBC/FY25/results_announcement, PDF p21: "The credit impairment charge of $424 million represented 5 basis points of average loans, down from 7 basis points in the prior year. The lower impairment charge was mainly due to an increase in write-backs and recoveries partly offset by a higher CAP charge."

## Limitations
- The investor discussion pack chart on page 49 has a failed walk sum check and is not used as the primary decomposition.
- The divisional table does not map one-to-one to the provision-type bridge; the provision-type drivers (IAPs, write-backs, recoveries, write-offs, other CAP changes) are the canonical quantified bridge per the bank's own disclosure on page 21, and they sum exactly to the $113m movement.
- The 'other changes in CAPs' row is a composite of multiple sub-drivers (economic outlook improvements, delinquency reductions, downside scenario weight increase, overlay increases) that the bank does not separately quantify in dollar terms beyond the aggregate $103m benefit.
- Basis normalised from 'cash' to 'ex_notables': no page in evidence prints 'cash' beside the movement, and the registry names ex_notables as the bank's headline basis.
- driver dropped as malformed (1 validation error for DriverClaim)
- driver dropped as malformed (1 validation error for DriverClaim)
- driver dropped as malformed (1 validation error for DriverClaim)
- driver dropped as malformed (1 validation error for DriverClaim)
- driver dropped as malformed (1 validation error for DriverClaim)
- Failed check: no_quantified_drivers
- Failed check: walk_sum (start 175 + bars +268.0 = 443.0 != end 174, tol 10.0) [WBC/FY25/investor_discussion_pack PDF p49 (ev-1)]

## Provenance
- combo: agentic-cheap
- models: agent=qwen/qwen3.7-flash, vision=qwen/qwen3.7-flash
- documents: WBC/FY25/results_announcement (a4cd05cf44f4), WBC/FY25/investor_discussion_pack (61645f94df85)
- generated: 2026-08-30T14:56:00+00:00
- seconds: 175.1
- cost_usd: 0.0416
- tokens: 1035527 in / 11002 out
- orchestration: agent
- tool_calls: 40
- pages_read: 16
- charts_read: 1
- budget_exhausted: no
