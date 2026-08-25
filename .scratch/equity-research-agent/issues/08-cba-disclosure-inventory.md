# 08 — CBA disclosure inventory

Type: research
Status: resolved

## Question

What does CBA publish at each results event, and where does the evidence live? Inventory: (1) the document suite per half/full-year (profit announcement, results presentation, investor pack, data pack or Excel, Pillar 3, annual report) with exact names and URL patterns; (2) whether machine-readable packs exist; (3) where the NIM walk and the cash earnings bridge appear in the most recent results; (4) format drift against a period around FY2020–21; (5) how cash vs statutory profit is presented; (6) where ROE, CET1, impairment, and cost-to-income evidence lives. Note: CBA's financial year ends 30 June.

## Answer

Full findings, with citations: [research/08-cba-disclosures.md](../research/08-cba-disclosures.md)

1. **FY2026 full-year results are out** (published 12 August 2026). The suite per event: ASX Announcement (4 pp), Profit Announcement (152 pp), Results Presentation and Investor Discussion Pack (139 pp), Basel III Pillar 3 PDF (137 pp) plus quantitative XLSX, Annual Report (207 pp, full-year only), webcast transcript, and a pre-results "Items impacting CBA's financial reporting" note. Landing page: `commbank.com.au/about-us/investors/results.html`; archive back to 1998.
2. **No Excel pack exists for P&L data.** The only machine-readable file is the quarterly Pillar 3 XLSX (47 APS 330 sheets, from March 2025). P&L, NIM, and divisional data require PDF parsing. The in-PDF "Analysis Template" appendix (6.4) exposes ratio inputs.
3. **FY26 NIM walk:** Profit Announcement printed p12 ("NIM Movement since June 2025" waterfall) and Presentation slides 26 (half-on-half) and 60 (12-month). **Cash earnings analysis:** Presentation slides 23–25; PA Group Performance Summary printed p2 and Appendix 6.3 "Profit Reconciliation" printed p113. Cash basis defined printed p3; glossary p121. Printed page = PDF page − 16.
4. **Format drift since FY20:** Appendix 4E moved; divisions changed (time-series break); income lines re-presented; the CDN URL pattern changed three times — scrape links, never template URLs.
5. **Parsing traps:** FY20/FY21 PDFs are AES-encrypted (pypdf needs `cryptography`); the FY26 deck's title page contains leftover hidden "Strawman" notes.

Two items are marked UNVERIFIED in the research file.
