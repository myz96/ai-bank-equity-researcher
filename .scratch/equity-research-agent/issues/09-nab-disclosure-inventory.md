# 09 — NAB disclosure inventory

Type: research
Status: resolved

## Question

Same inventory as ticket 08, for NAB: the document suite per results event with names and URL patterns, machine-readable packs, location of the NIM walk and cash earnings bridge in the most recent results, format drift against a period around FY2020–21, cash-vs-statutory presentation, and where the other four metrics' evidence lives. Note: NAB's financial year ends 30 September.

## Answer

Full findings, with citations: [research/09-nab-disclosures.md](../research/09-nab-disclosures.md)

1. **The half-year results book is the master document.** The 1H26 "Half Year Results" PDF (108 pages) contains Appendix 4D, the MD&A, the reviewed interim financial report, and supplementary tables. The NIM movement walk (bps waterfall) is on printed p22 (PDF p26), Section 2 "Net interest income". The cash-earnings-to-statutory reconciliation is on printed pp100–101 (PDF pp104–105), Section 5. The Investor Presentation repeats both: slide 25 (NIM HoH) and slide 39 (reconciliation).
2. **Full-year format changed at FY21.** FY20's results book contained the statutory financial report and Appendix 4E. From FY21 the full-year document became an MD&A without financial statements; the audited report moved to the Annual Report suite, published the same day. A single combined Annual Report started at FY22.
3. **No results Excel pack exists today.** NAB stopped the "Key Performance Measures" workbook after FY20. Recurring machine-readable files are only the quarterly Pillar 3 XLSX (from 2025), a sustainability data pack, and a remuneration CSV. P&L data must come from PDFs.
4. **Cash earnings is the primary basis.** The definition sits at printed p12 of each results book, with three exclusion categories plus a separate "large notable items" layer (1H26: $949m post-tax software amortisation).
5. **URL naming drifts.** Pre-2021 files live under `/content/dam/nabrwd/...`, later under `/content/dam/nab/...`, with inconsistent names — scrape the financial-results landing page rather than construct URLs.

UNVERIFIED items (ASX lodgement titles, transcript archive, pre-2025 Pillar 3 XLSX) are flagged in the research file.
