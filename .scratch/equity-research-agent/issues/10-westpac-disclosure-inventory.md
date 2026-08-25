# 10 — Westpac disclosure inventory

Type: research
Status: resolved

## Question

Same inventory as ticket 08, for Westpac: the document suite per results event with names and URL patterns, machine-readable packs, location of the NIM walk and cash earnings bridge in the most recent results, format drift against a period around FY2020–21, cash-vs-statutory presentation, and where the other four metrics' evidence lives. Note: Westpac's financial year ends 30 September.

## Answer

Full findings, with citations: [research/10-westpac-disclosures.md](../research/10-westpac-disclosures.md)

1. **The headline measure changed at 1H23.** The "1H23 Reporting Changes Update" (24 March 2023) made net profit the single performance measure and removed cash earnings. FY22 was the last cash-earnings result. Westpac now shows statutory net profit first, with "Net profit excluding Notable Items" (non-AAS) beside it; FY25 calls the ex-Notables basis "comparable to a 'cash earnings' basis".
2. **A machine-readable pack exists since 1H23.** The "Key Financial Information" Excel workbook ships with each result (1H26: 29 sheets mirroring the announcement sections). A quarterly Pillar 3 quantitative Excel exists since the APS 330 change on 1 January 2025.
3. **In the 1H26 result (5 May 2026)** the NIM movement walk appears twice: Investor Discussion Pack slide 24 and Results Announcement "Review of earnings" printed p7. Net profit bridges: IDP slides 37–38; statutory reconciliation slide 39.
4. **Format breaks for parsers:** 1H23 (measure change; annual report absorbed the FY financial report; FY announcement shrank to a 67-page performance review) and 1H25 (new Pillar 3 format). The half-year announcement still contains the Interim Financial Report (Appendix 4D).
5. **URL patterns:** documents sit under `westpac.com.au/content/dam/public/wbc/documents/pdf/aw/ic/`; period landing pages follow `/about-westpac/investor-centre/events-and-presentations/YYYY-...`. Filenames drift, so scrape the landing pages.

UNVERIFIED: stable ASX deep link; pre-2025 Pillar 3 Excel coverage; first period ROTE appeared.
