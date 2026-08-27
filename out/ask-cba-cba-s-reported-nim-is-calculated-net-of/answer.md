# Q: CBA's reported NIM is calculated net of mortgage offset account balances. Quantify those balances for FY26 and FY25 and explain how they affect average interest earning assets and NIM.

*CBA, periods FY26, FY25 — confidence 90/100*

CBA's average mortgage offset balances were $94,892 million in FY26 and $84,123 million in FY25 (ev-1). These balances are netted against interest-earning assets for NIM calculation purposes, despite being grossed up under accounting standards (ev-2). This netting reduces the reported average interest-earning asset base, thereby inflating the reported Net Interest Margin compared to a gross basis. While spot offset balances were $94 billion in FY26 and $97 billion in FY25 (ev-3), the relevant metric for NIM impact is the annual average figure provided in the Profit Announcement.

## Key facts

- Average mortgage offset balances were $94,892m in FY26 and $84,123m in FY25.
  > [ev-1] CBA/FY26/profit_announcement, PDF p28: "Net of average mortgage offset balances of $94,892 million for the full year ended 30 June 2026 ($84,123 million for the full year ended 30 June 2025)"
- Offset balances are netted for NIM calculation but grossed up for accounting standards.
  > [ev-2] CBA/FY26/profit_announcement, PDF p28: "While these balances are required to be grossed up under accounting standards, they are netted down for the calculation of customer interest payments and the Group’s net interest margin."

## Limitations
- The evidence provides average balances for NIM context but does not explicitly quantify the exact dollar impact on the NIM percentage or the specific reduction in average earning assets beyond stating they are netted. Spot balances from the results presentation differ slightly from the annual averages used for NIM.

## Provenance
- combo: cheap
- models: extract=qwen/qwen3.7-flash, author=qwen/qwen3.7-flash
- documents: CBA/FY26/profit_announcement (438d5975baad), CBA/FY26/results_presentation (289f03457584), CBA/FY26/asx_announcement (83622c320171), CBA/FY26/pre_results_note (fa67eb945987), CBA/FY25/profit_announcement (e2e911ab4fed)
- queries: ["CBA's reported NIM is calculated net of mortgage offset account balances. Quantify those balances for FY26 and FY25 and explain how they affect average interest earning assets and NIM.", 'CBA net interest margin mortgage offset account balance FY25 FY26', '"average interest earning assets" "offset accounts" CBA results presentation', 'note: impact of mortgage offset balances on NIM calculation Commonwealth Bank']
- pages_read: ['CBA/FY26/profit_announcement p29', 'CBA/FY26/profit_announcement p8', 'CBA/FY26/profit_announcement p9', 'CBA/FY26/profit_announcement p11', 'CBA/FY26/profit_announcement p28', 'CBA/FY26/profit_announcement p151', 'CBA/FY26/results_presentation p63', 'CBA/FY26/results_presentation p130', 'CBA/FY26/results_presentation p75', 'CBA/FY26/results_presentation p9', 'CBA/FY26/results_presentation p80', 'CBA/FY26/results_presentation p135']
- generated: 2026-08-27T07:19:27+00:00
- seconds: 38.0
- cost_usd: 0.0005
- tokens: 14701 in / 769 out
