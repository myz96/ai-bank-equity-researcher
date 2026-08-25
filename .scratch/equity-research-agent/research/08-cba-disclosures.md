# CBA disclosure inventory

Research date: 2026-08-25. All sources are primary: commbank.com.au investor pages and published result documents. CBA's financial year ends 30 June. CBA reports full-year results in August and half-year results in February.

Most recent results as of today: **FY2026 full-year results, published 12 August 2026** (year ended 30 June 2026). Date verified on page 1 of the ASX Announcement PDF ("12 August 2026 | Media Release 215/2026").
Source: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-ASX-Announcement.pdf

---

## 1. Document suite at each results event

### Landing pages

| Page | URL |
|---|---|
| Results hub (current + ~2 prior years, grouped by period) | https://www.commbank.com.au/about-us/investors/results.html |
| Results archive (2024 back to 1998, full-year and half-year) | https://www.commbank.com.au/about-us/investors/results/results-archive.html |
| Investor centre | https://www.commbank.com.au/about-us/investors.html |
| Annual reports | https://www.commbank.com.au/about-us/investors/annual-reports.html |
| ASX announcements | https://www.commbank.com.au/about-us/investors/asx-announcements.html |
| Pillar 3 capital disclosures (quarterly, incl. Excel) | https://www.commbank.com.au/about-us/investors/regulatory-disclosure/pillar-3-capital-disclosures.html |

The results hub lists each period as a card with the same document set. Source: https://www.commbank.com.au/about-us/investors/results.html

### Standard suite per results event (FY26 full-year example, all links verified)

| Document | Pages (FY26 FY) | Direct URL |
|---|---|---|
| Full Year Results ASX Announcement (media release) | 4 | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-ASX-Announcement.pdf |
| Profit Announcement (the detailed results book) | 152 PDF pages (124 numbered + preamble) | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Profit-Announcement.pdf |
| Results Presentation and Investor Discussion Pack | 139 | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf |
| Basel III Pillar 3 Disclosure (PDF) | 137 | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/2026-Full-Year-Basel-III-Pillar-3-Disclosure.pdf |
| Basel III Pillar 3 quantitative information (Excel) | 47 sheets | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/Commonwealth-Bank-Basel-III-Pillar-3-quantitative-information-as-at-30-June-2026-(Excel).xlsx |
| Annual Report (full-year events only) | 207 | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Annual-Report.pdf |
| "Items impacting CBA's financial reporting" (pre-results restatement note, ~1 week before results) | 3 | https://www.commbank.com.au/content/dam/commbank-assets/about-us/docs/FY26-Items-impacting-CBA%27s-financial-reporting.pdf |
| Webcast transcript | n/a | https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Transcript.pdf |

Page counts come from local inspection of the downloaded PDFs (pypdf). Suite composition per period comes from the results hub: https://www.commbank.com.au/about-us/investors/results.html

Half-year events publish the same set without the Annual Report. Example 1H26 (11 February 2026):
- Profit Announcement: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA%202026%20Half%20Year%20Results%20Profit%20Announcement.pdf
- Presentation: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA%202026%20Half%20Year%20Results%20Presentation.pdf
- ASX Announcement: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA%202026%20Half%20Year%20Results%20ASX%20Announcement.pdf
- Pillar 3: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA%202026%20Half%20Year%20Basel%20III%20Pillar%203%20Disclosure.pdf
The 11 February 2026 date comes from the Pillar 3 disclosures page (2Q26 row): https://www.commbank.com.au/about-us/investors/regulatory-disclosure/pillar-3-capital-disclosures.html

Extra document: a US-format Profit Announcement exists for US investors, e.g. https://www.commbank.com.au/content/dam/commbank-assets/about-us/us-investors/2025-Full-Year-US-Profit-Announcement.pdf (verified HTTP 200).

### URL patterns (they drift across years)

- FY20 and earlier: `/content/dam/commbank/about-us/shareholders/pdfs/results/{fy20|1h20}/<file>.pdf`
- FY21–FY25: `/content/dam/commbank-assets/investors/docs/results/{fy21...fy25|1h21...1h25}/<file>.pdf`
- FY26 onward: `/content/dam/commbank-assets/investors/2026/<file>.pdf` (flat calendar-year folder; file names contain spaces for 1H26, hyphens for FY26)

Sources: results hub and archive pages listed above. Warning: do not template these URLs. File-name style changes between periods. Scrape the landing page instead.

---

## 2. Machine-readable packs (Excel/CSV)

1. **Basel III Pillar 3 quantitative information (XLSX)** — exists each quarter from March 2025 onward. The FY26 file has 47 sheets with the APS 330 standard tables: Cover, Table of Contents, OV1 (RWA overview), EAD & CRWA, CMS1, CMS2, CR1–CR10 (credit risk), CCR1–CCR8 (counterparty), SEC1–SEC4 (securitisation), TMR, IRRBB1, OR1–OR3 (operational risk), LIQ1 (LCR), LIQ2 (NSFR), KM1 (key metrics incl. CET1), CC1/CC2 (capital composition), CCyB1, LR1/LR2 (leverage), ENC, LI1/LI2. Sheet list verified by opening the file.
   Landing page: https://www.commbank.com.au/about-us/investors/regulatory-disclosure/pillar-3-capital-disclosures.html
   FY26 file: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/Commonwealth-Bank-Basel-III-Pillar-3-quantitative-information-as-at-30-June-2026-(Excel).xlsx
   Quarters before 3Q25 have PDF only (verified on the same landing page).

2. **No Excel data pack for the P&L results.** The results hub lists no XLSX for any results period (verified on https://www.commbank.com.au/about-us/investors/results.html). The substitute is the **"Analysis Template" appendix inside the Profit Announcement PDF** (FY26: Appendix 6.4, printed pages 116–119). It shows the exact inputs and outputs for EPS, ROE, and other ratios. A legacy file "full-year-results-excel-tables.xls" exists at https://www.commbank.com.au/content/dam/commbank/about-us/shareholders/pdfs/results/full-year-results-excel-tables.xls but its metadata shows a last-save date of 13 August 2013. It covers FY2013. CBA stopped this series. UNVERIFIED: whether Excel results tables exist for any year between FY2014 and FY2024; I found none on the results or archive pages.

3. Consequence for the agent: the P&L, NIM, and divisional data must come from PDF parsing of the Profit Announcement. Capital and liquidity data can come from the Pillar 3 XLSX for periods after March 2025.

---

## 3. FY26 (most recent): NIM walk and cash earnings bridge

### NIM walk (net interest margin movement)

- **Profit Announcement, section "Group Performance Analysis" → "Net Interest Income"**, printed page 12 (PDF page 28). It contains the table "Net Interest Income (continuing operations basis)", the chart **"NIM Movement since June 2025"** (waterfall: FY25 2.08% → liquids −0.02%, asset pricing −0.05%, → FY26 2.05%), and driver text (asset pricing −5 bpts, funding costs flat, portfolio mix +2 bpts, basis risk flat). Half-on-half version follows on printed page 13 (PDF page 29). Appendix 1.2 "Net Interest Margin" (printed page 72) gives the history table.
  Source: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Profit-Announcement.pdf
- **Results Presentation**: slide 26 (CFO section) is the half-on-half Group margin walk (1H26 204 bpts → 2H26 206 bpts). Slide 60 (Investor Discussion Pack, "Financial overview" section) is the 12-month walk: FY25 208 bpts → FY26 205 bpts with components Liquids & repos (−4), Asset pricing (−5), Funding costs (0), Portfolio mix (+2), Interest rate risk hedging (+5), Treasury & Markets (−1). Slide 61 covers the replicating portfolio and equity hedge. Slide 63 covers margins by division.
  Source: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf

### Cash earnings bridge / analysis

- **Results Presentation**: slide 24 "FY26 result" is the cash NPAT analysis table (operating income $30,224m, underlying expenses $13,585m, restructuring/notable items $170m, operating performance $16,469m, LIE $788m, cash NPAT $10,982m, with FY26-vs-FY25 and 2H26-vs-1H26 percentages). Slide 25 is the operating income waterfall ($28,465m → $30,224m). Slide 23 "Statutory vs cash NPAT" is the reconciliation. Slide 56 shows cash NPAT by division.
  Source: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf
- **Profit Announcement**: the "Group Performance Summary" table (printed page 2, PDF 16) shows the statutory and cash P&L side by side down to NPAT, plus cash NPAT by division. The narrative bridge is "Financial Performance and Business Review" (printed pages 10–11, PDF 26–27).
  Source: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Profit-Announcement.pdf

### FY26 Profit Announcement structure (from its contents pages)

1. Highlights (printed 2–7): Group Performance Summary; Non-Cash Items Included in Statutory Profit; Key Performance Indicators; Market Share; Credit Ratings.
2. Group Performance Analysis (10–22): Financial Performance and Business Review; Net Interest Income; Other Operating Income; Operating Expenses; Investment Spend; Capitalised Software; Loan Impairment Expense; Taxation Expense; Group Assets and Liabilities.
3. Group Operations and Business Settings (24–35): Loan Impairment Provisions and Credit Quality; Capital; Leverage Ratio; Dividends; Liquidity; Funding; NSFR.
4. Divisional Performance (38–60): Retail Banking Services; Business Banking; Institutional Banking and Markets; New Zealand; Corporate Centre and Other.
5. Financial Statements (62–67): Income Statement; Comprehensive Income; Balance Sheet; Changes in Equity; Cash Flows.
6. Appendices (70–124): 1.1 Net Interest Income; 1.2 Net Interest Margin; 1.3 Average Balances and Related Interest; 1.4 Interest Rate and Volume Analysis; 1.5 Other Operating Income; 1.6 Operating Expenses; 1.7 Income Tax Expense; 2.1 Loans and Other Receivables; 2.2 Provisions for Impairment and Asset Quality; 3.1 Deposits; 4.1 Capital; 4.2 Shareholders' Equity; 4.3 Share Capital; 5.1 Integrated Risk Management; 5.2 Counterparty and Other Credit Risk Exposures; 6.1 Intangible Assets; 6.2 ASX Appendix 4E (p.106); 6.3 Profit Reconciliation (p.113); 6.4 Analysis Template (p.116); 6.5 Foreign Exchange Rates; 6.6 Definitions (p.121).
The PDF also front-loads the 4-page ASX Announcement and the media release before printed page 1.
Source: contents pages of https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Profit-Announcement.pdf

### FY26 Presentation structure (139 slides)

CEO section (slides 4–20, Matt Comyn); CFO section (slides 21–36, Alan Docherty); Investor Discussion Pack: Overview & strategy (37); Financial overview (53); Home & consumer lending (73); Business & corporate lending (86); Funding, liquidity & capital (97); Economic overview (119); Sources, glossary & notes (129).
Source: divider slides of https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf

Parsing warning: page 1 of the FY26 presentation PDF contains leftover hidden text ("Strawman – CEO section" planning notes). Text extraction picks it up. Filter the title page.

---

## 4. Format drift: FY20/FY21 vs FY26

Suite composition and top-level architecture are stable. Details drifted:

1. **Document names are stable.** Every period from FY20 to FY26 has: Profit Announcement, Results ASX Announcement, Results Presentation (titled "Results Presentation and Investor Discussion Pack" on the cover in FY20, FY21, and FY26), Basel III Pillar 3 Disclosure, webcast + transcript. Sources: results archive https://www.commbank.com.au/about-us/investors/results/results-archive.html and the PDF covers.
2. **ASX Appendix 4E moved.** FY20 Profit Announcement opens with the Appendix 4E ("Results for announcement to the market", PDF page 2). FY26 places it at Appendix 6.2 (printed page 106) and opens with the media release instead. Sources: https://www.commbank.com.au/content/dam/commbank/about-us/shareholders/pdfs/results/fy20/cba-fy20-profit-announcement.pdf and the FY26 Profit Announcement.
3. **Divisional structure changed.** FY20 divisions: Retail Banking Services; Business and Private Banking; Institutional Banking and Markets; IFS and New Zealand; Corporate Centre; plus Wealth Management in discontinued operations. FY26 divisions: Retail Banking Services; Business Banking; Institutional Banking and Markets; New Zealand; Corporate Centre and Other. Divestments (CFS, life insurance, IFS units) drove the change. Time-series joins across divisions break at these points.
4. **Income line presentation changed.** The FY20 divisional summary splits income into "Total banking income", "Funds management income", and "Insurance income". FY26 shows "Net interest income" and "Other operating income" only.
5. **NIM walk chart in the Profit Announcement is newer.** FY26 has a labelled waterfall "NIM Movement since June 2025". FY20 and FY21 Profit Announcements describe margin drivers in prose and tables; text extraction finds no "NIM movement" chart label. UNVERIFIED: the exact period that introduced the labelled waterfall. The presentation deck carried a Group margin walk in every year checked (FY20 slide 23; FY26 slides 26 and 60).
6. **Presentation section merge.** FY20 Investor Discussion Pack had separate "Deposits, Funding and Liquidity" (slide 115) and "Capital" (slide 122) sections. FY21 merged them into "Funding, Liquidity and Capital" (slide 102); FY26 keeps the merged form (slide 97). Deck length: FY20 155 slides, FY21 138, FY26 139.
7. **New artifacts since FY25/FY26:** the pre-results "Items impacting CBA's financial reporting" note (FY26 edition dated 4 August 2026, covers restatements such as home-loan arrears methodology alignment) and the Pillar 3 quantitative XLSX (from March 2025). FY21 had an ad-hoc equivalent restatement note ("Update on financial reporting changes", https://www.commbank.com.au/content/dam/commbank-assets/investors/docs/results/fy21/update-on-financial-reporting-changes-impacting-comparative-financial-information.pdf).
8. **Analysis Template continuity.** The ratio input/output appendix exists in both eras (FY20: "Ratios - Output Summary" at printed page 132; FY26: Appendix 6.4 "Analysis Template" at printed page 116). FY20 writes `"cash basis"` in quotation marks; FY26 drops the quotation marks.
9. **CDN path migration** (see URL patterns in section 1). Old FY20 links still resolve.

---

## 5. Cash NPAT vs statutory NPAT

- **Definition and policy statement**: Profit Announcement, Highlights section, "Non-Cash Items Included in Statutory Profit", printed page 3 (PDF 17). Text: statutory basis follows the Corporations Act and Australian Accounting Standards (IFRS-compliant); "The cash basis is used by management to present a clear view of the Bank's operating results. It is not a measure based on cash accounting or cash flows." Excluded items: hedging and IFRS volatility; gains/losses on acquisition, disposal, closure, capital repatriation, and demerger of businesses (discontinued operations).
- **Reconciliations**:
  - Group Performance Summary table, printed page 2: statutory and cash columns side by side, then non-cash items to bridge cash NPAT ($10,982m FY26) to statutory NPAT ($10,866m incl. discontinued; $10,911m continuing).
  - Non-cash items tables, printed page 3 (split by continuing/discontinued).
  - Appendix 6.3 "Profit Reconciliation", printed pages 113–115: line-by-line P&L reconciliation between statutory and cash.
  - Presentation slide 23 "Statutory vs cash NPAT": FY25/FY26 two-line reconciliation (transaction costs and gains/losses on disposals; hedging and IFRS volatility).
- **Glossary entries**: Appendix 6.6 Definitions, printed pages 121–123, defines NPAT (statutory basis), NPAT (cash basis), ROE (cash and statutory), payout ratios (cash and statutory).
- Both bases appear together in the Key Performance Indicators table (printed pages 4–6) and in EPS/ROE lines.
Sources: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Profit-Announcement.pdf and https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/CBA-2026-Full-Year-Results-Presentation.pdf

---

## 6. Evidence map for other metrics (FY26 references)

| Metric | Profit Announcement | Presentation | Other |
|---|---|---|---|
| ROE (cash 14.0%, statutory 13.9%) | Key Performance Indicators, printed p.5 (PDF 19); definition in Appendix 6.6 ("net profit after tax (cash basis) divided by average shareholders' equity") | Slides 5, 54, 55 | Annual Report |
| CET1 (12.0% APRA Level 2; 18.3% international) | Group Operations → "Capital", printed p.28 (PDF 48): Summary Group Capital Adequacy Ratios + movement analysis; Appendix 4.1 Capital, printed p.92 | Slide 32: CET1 waterfall (Dec 25 12.3% → Jun 26 12.0%: +106 bpts cash NPAT, −76 dividend, −46 RWA, −8 other); slides 5, 54, 55 | Pillar 3 PDF + XLSX sheets KM1, CC1, CC2: https://www.commbank.com.au/content/dam/commbank-assets/investors/2026/Commonwealth-Bank-Basel-III-Pillar-3-quantitative-information-as-at-30-June-2026-(Excel).xlsx |
| Loan impairment expense ($788m; 8 bpts of GLAA) | Group Performance Analysis → "Loan Impairment Expense", printed p.18 (PDF 34), by division; provisions and credit quality, printed pp.24–27; Appendix 2.2 | Slide 29 (LIE + arrears), slide 30 (provisioning), slide 24 (in cash NPAT table) | Pillar 3 CR tables |
| Cost-to-income (45.5%) / operating expenses ($13,755m) | "Operating Expenses", printed p.15; ratio "Operating expenses to total operating income" in Key Performance Indicators, printed p.4 (PDF 18); Appendix 1.6 | Slide 27: expense waterfall (FY25 $12,866m → FY26 $13,585m underlying: inflation +455, technology +444, frontline +128, other +96, productivity −404); slides 54–55 | — |
| NIM (2.05%) | See section 3 | See section 3 | — |

All Profit Announcement printed page numbers map to PDF pages with offset +16 (printed p.2 = PDF 16).

---

## Notes and open items

- UNVERIFIED: the first period with the labelled "NIM Movement" waterfall in the Profit Announcement (present FY26; absent from FY20/FY21 text layers).
- UNVERIFIED: Excel results tables for FY2014–FY2024; none found on the results hub, archive, or via site search.
- The FY20/FY21 documents are AES-encrypted PDFs (owner encryption only). pypdf needs the `cryptography` package to read them. Plan for this in the ingestion pipeline.
- File names for 1H26 contain URL-encoded spaces (`%20`); FY26 full-year names use hyphens. Scrape links from the landing page; do not construct them.
- The results hub keeps roughly the two most recent years; older periods move to the results archive page.
