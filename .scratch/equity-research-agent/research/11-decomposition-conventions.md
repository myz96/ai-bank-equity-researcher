# Driver decomposition conventions for Australian bank headline metrics

Research date: 2026-08-25. All claims come from primary sources: big-four results materials, APRA prudential standards, RBA publications, and AASB 9. Labels in quotes are verbatim from the cited documents. Items I could not confirm are marked UNVERIFIED.

Primary documents used (text extracted and read in full or in targeted sections):

- NAB 2025 Full Year Results Investor Presentation (6 Nov 2025): <https://www.nab.com.au/content/dam/nab/documents/reports/corporate/2025-full-year-results-investor-presentation.pdf>
- NAB 2025 Full Year Results Management Discussion and Analysis: <https://www.nab.com.au/content/dam/nab/documents/reports/corporate/2025-full-year-results-management-discussion-and-analysis.pdf>
- Westpac 2025 Full Year Results Presentation & Investor Discussion Pack: <https://www.westpac.com.au/content/dam/public/wbc/documents/pdf/aw/ic/wbc-full-year-presentation-and-IDP-2025.pdf>
- CBA Profit Announcement, full year ended 30 June 2025: <https://www.commbank.com.au/content/dam/commbank-assets/investors/docs/results/fy25/full-year-profit-announcement.pdf>
- CBA Profit Announcement FY18 (for the "jaws" definition): <https://www.commbank.com.au/content/dam/commbank/about-us/shareholders/pdfs/results/fy18/fy2018-profit-announcement.pdf>
- ANZ 1H26 Results Announcement (half year to 31 March 2026): <https://www.anz.com/content/dam/anzcom/shareholder/1H26-results-announcement/1H26-ANZGHL-Results-Announcement.pdf>
- RBA Bulletin, "Developments in Banks' Funding Costs and Lending Rates" (May 2026): <https://www.rba.gov.au/publications/bulletin/2026/may/developments-in-banks-funding-costs-and-lending-rates.html> (also the March 2023 edition: <https://www.rba.gov.au/publications/bulletin/2023/mar/developments-in-banks-funding-costs-and-lending-rates.html>)
- RBA Financial Stability Review Oct 2016, Box C, "Recent Developments in Australian Banks' Capital Position and Return on Equity": <https://www.rba.gov.au/publications/fsr/2016/oct/box-c.html>
- RBA Bulletin March 2017, "Returns on Equity, Cost of Equity and the Implications for Banks": <https://www.rba.gov.au/publications/bulletin/2017/mar/6.html>
- APRA APS 110 Capital Adequacy: <https://www.apra.gov.au/standards/aps-110>; APS 111 Measurement of Capital: <https://www.apra.gov.au/standards/aps-111-final-not-force>; APS 112 Standardised Approach to Credit Risk: <https://www.apra.gov.au/standards/aps-112>; APS 113 IRB Approach to Credit Risk: <https://www.apra.gov.au/standards/aps-113>; APS 115 Standardised Measurement Approach to Operational Risk: <https://www.apra.gov.au/system/files/2022-07/Prudential%20Standard%20APS%20115%20Capital%20Adequacy%20-%20Standardised%20Approach%20to%20Op%20Risk.pdf>; APS 117 Interest Rate Risk in the Banking Book: <https://www.apra.gov.au/sites/default/files/2022-11/Prudential%20Standard%20APS%20117%20Capital%20Adequacy%20-%20Interest%20Rate%20Risk%20in%20the%20Banking%20Book%20-%20clean.pdf>; APG 110 practice guide (capital floor mechanics): <https://www.apra.gov.au/practice-guides/apg-110>
- AASB 9 Financial Instruments (compiled standard): <https://www.aasb.gov.au/admin/file/content105/c9/AASB9_12-14_COMPdec17_01-19.pdf>

---

## 1. Net interest margin (NIM)

### The standard walk

All four banks present a NIM "walk" (waterfall) from the prior period NIM to the current period NIM. Each bar is one driver. Each bar carries a basis-point (bp) contribution. The bars sum to the total NIM change.

Verbatim walk labels by bank:

| Driver concept | NAB (FY25 pres, p.24) | Westpac (FY25 IDP, p.24) | CBA (FY25 PA, pp.12–13) | ANZ (1H26 RA, pp.18–19) |
|---|---|---|---|---|
| Asset pricing / competition | "Lending Margin" | "Loans" | "Asset pricing" | "Assets pricing" |
| Deposit pricing and mix | "Deposits" | "Deposits" | inside "Funding costs" | "Deposits pricing" |
| Wholesale funding | "Funding Costs" | "Wholesale funding" | inside "Funding costs" | "Wholesale funding" |
| Liquid assets drag | "Liquid Assets" | "Liquid assets" | "Liquids & Pooled Facilities" | "Group Centre liquids" |
| Capital + replicating portfolio | "Replicating Portfolios" | "Capital & Other" | "Capital, Replicating and Other" | "Capital and replicating portfolio" |
| Mix | (inside other bars) | (inside other bars) | "Portfolio mix" | "Assets and funding mix" |
| Basis risk | (not separate) | (not separate) | "Basis risk" | (not separate) |
| Markets / Treasury | "M&T" | "Treasury & Markets" | "Treasury and Markets" | "Markets activities" |

Examples with signs, verbatim:

- NAB 2H25 half-on-half walk: Mar 25 1.70% + "Lending Margin 0.00%" + "Funding Costs 0.01%" + "Deposits (0.01%)" + "Replicating Portfolios 0.02%" + "Liquid Assets 0.02%" + "M&T 0.04%" = Sep 25 1.78%; "HoH increase 8bps". Side annotations split bars further: "Aust HL -1bp, Aust BL -1bp, NZ +1bp, Other +1bp" for lending, and "Deposits +3bps, Capital +1bp" for the replicating portfolios. The liquid assets bar is noted "Largely revenue neutral". (NAB FY25 Investor Presentation, p.24.)
- CBA FY25 year-on-year walk: Jun 24 1.99% + "Liquids & Pooled Facilities" +0.07% + "Asset pricing" flat + "Funding costs" (0.07%) + "Portfolio mix" flat + "Basis risk" (0.01%) + "Capital, Replicating and Other" +0.09% + "Treasury and Markets" +0.01% = Jun 25 2.08%. CBA also splits "Capital, Replicating and Other" in text: replicating portfolio rate and volume "up 5 basis points" and "higher earnings on capital hedges (up 4 basis points)". CBA defines basis risk as the spread between the 3-month bank bill swap rate and the 3-month overnight index swap rate. (CBA FY25 Profit Announcement, pp.12–13.)
- ANZ 1H26 vs 1H25: "Assets pricing (-4 bps)", "Deposits pricing (-3 bps)", "Wholesale funding (0 bps)", "Capital and replicating portfolio (+4 bps)", "Assets and funding mix (+2 bps)", "Group Centre liquids (+3 bps)", "Markets activities (-5 bps)". Each bar has a one-line cause, e.g. deposits pricing was "driven by lower cash rates in New Zealand and international geographies and pricing competition". (ANZ 1H26 Results Announcement, p.18.)
- Westpac annotates bars rather than sub-labelling them, e.g. under "Deposits": "Consumer savings reprice 3bps", "RBA rate changes (2bps)", "Spread & mix (3bps)"; under "Capital & Other": "Replicating portfolio 1bp", "Non hedged capital & other (2bps)". (Westpac FY25 IDP, p.24.)

### "Core"/"underlying" NIM variants

Each bank strips volatile items, but the name differs:

- Westpac: "Core net interest margin — Calculated by dividing net interest income excluding Notable Items and Treasury & Markets by average interest-earning assets (annualised where applicable)" (FY25 IDP glossary, p.121). Westpac stacks reported NIM = Core NIM + a "Treasury & Markets" band (e.g. 1.82 + 0.13 = 1.95 in 2H25).
- NAB: "Net interest margin ex M&T" (FY25 pres, p.75 area) and commentary "Excluding a 3 bps increase from M&T, NIM declined 3 bps" (2025 Half Year materials: <https://www.nab.com.au/content/dam/nab/documents/reports/corporate/2025-half-year-results-investor-presentation.pdf>).
- ANZ: "Net interest margin (excl. Markets)" reported next to headline NIM (1H26 RA, p.9). ANZ's headline NIM (1.53%) is much lower than peers because Markets average interest-earning assets sit in the denominator.
- CBA: no named core NIM. CBA writes the exclusion out: "Excluding a 7 basis point increase in margin from a reduction in lower yielding liquid assets and institutional pooled facilities, which have a broadly neutral impact on net interest income, net interest margin increased 2 basis points" (FY25 PA, p.12).

### Presentation and sign conventions

- Contributions are in basis points. Charts label bars in per cent with two decimals ("0.01%" = 1bp) at NAB and CBA; Westpac and ANZ label in bps.
- Negative contributions sit in parentheses: "(0.01%)", "(-3 bps)", "(2bps)".
- Banks publish both half-on-half and prior-corresponding-period walks.
- Standard sensitivities accompany the walk: NAB "7bps move in 3 month Bills/OIS equivalent to ~1bp of annualised NIM" and a 25bp cash-rate cut on unhedged low-rate deposits "~1bp annualised" (FY25 pres, p.24); Westpac gives the same two sensitivities (FY25 IDP, p.24).

### RBA framing (system level)

The RBA's recurring Bulletin series "Developments in Banks' Funding Costs and Lending Rates" decomposes funding costs into deposits, wholesale debt, and equity. The May 2026 edition states that deposits are about two-thirds, debt almost one-third, and equity less than one-tenth of major bank funding; that banks hedge low-rate deposits and capital so cash-rate declines do not fully hit NIM (the replicating-portfolio mechanism); and that "competition in deposit and lending markets weighed on NIMs and lending spreads in 2025". URLs above.

---

## 2. Cash earnings

### The measure and its names

- NAB: "cash earnings". Non-IFRS. "NAB uses cash earnings … for its internal management reporting purposes and considers it a better reflection of the Group's underlying performance." Not audited or reviewed. Defined on p.10 of the FY25 MD&A, with a full reconciliation on pp.72–74. (NAB FY25 pres, p.39; MD&A.)
- ANZ: "cash profit". "Cash profit, a non-IFRS measure, represents the Group's preferred measure of the result of its core business activities … the Group excludes non-core items from statutory profit." Cash profit itself is not reviewed by the external auditor, but the adjustments sit inside reviewed statutory profit. (ANZ 1H26 RA, p.10.)
- CBA: "cash NPAT" / "cash profit" / net profit after tax ("cash basis"). "The cash basis is used by management to present a clear view of the Bank's operating results. It is not a measure based on cash accounting or cash flows." (CBA FY25 PA, statutory-to-cash section and glossary.)
- Westpac: no cash measure. Westpac reports statutory net profit and "Net profit excluding Notable Items", "a non-AAS financial performance measure used by Westpac for internal management reporting, as it provides a clearer view of the Group's underlying operational performance" (FY25 IDP, p.42). UNVERIFIED: Westpac retired "cash earnings" as its primary measure around FY22; I did not verify the exact date from a primary source.

### The cash-to-statutory reconciliation items

- NAB non-cash earnings items (after tax): "Hedging and fair value volatility", "Amortisation of acquired intangible assets", "Acquisition, disposals and business closures", plus discontinued operations. (FY25 pres, p.39.)
- CBA non-cash items: "Loss on acquisition, disposal, closure and demerger of businesses", "Hedging and IFRS volatility". (FY25 PA, statutory-to-cash table.)
- ANZ non-core items: "Economic hedges", "Revenue and expense hedges", and amortisation of intangible assets recognised in a business combination. (1H26 RA, pp.69–71 and note 2 on p.2.)
- Westpac Notable Items categories (after tax): "Asset sales and revaluations", "Provisions for remediation, litigation, fines and penalties", "Restructuring costs", "Asset write-downs", "Hedging items". In FY25 only "Hedging items" was populated. (FY25 IDP, p.42.)

### The standard earnings bridge

The conventional bridge runs: net interest income (split volume vs margin) → other operating income → operating expenses → pre-provision profit → credit impairment charge → tax → cash earnings.

- Volume vs margin convention: NII = average interest-earning assets (AIEA) x NIM. CBA: "Net Interest Income (NII) increased 5%, primarily driven by a 9 basis point increase in Net Interest Margin (NIM) and a $9 billion increase [in AIEA]" (FY25 PA, p.6). Westpac defines AIEA in its glossary and calculates NIM on it (FY25 IDP, p.121).
- Pre-provision subtotal names differ: Westpac "Pre-provision profit — Net operating income less operating expenses" (FY25 IDP glossary, p.121); CBA "Operating performance" (FY25 PA, key financials table); ANZ "Cash profit before credit impairment and income tax" (1H26 RA, p.9). NAB uses "underlying profit" for this subtotal in its MD&A — UNVERIFIED here (I confirmed the term is standard NAB usage in prior years but did not sight it in the FY25 documents I extracted).

### Separating "core" from notable items

- Westpac shows every headline metric twice: reported and "ex Notable Items" ("Net profit ex Notable Items, ROTE ex Notable Items and cost to income ex Notable Items are used for internal management reporting", FY25 IDP, p.3).
- ANZ calls them "significant items" and shows "Cash Profit ex-Sig. Items". The Sep 2025 half items were: PT Panin impairment, staff redundancies, ASIC settlement, Suncorp Bank migration, Cashrewards closure. (1H26 RA, p.12.)
- CBA nets "Restructuring and notable items" out of expenses to show "underlying operating expenses" (FY25 PA, expenses section; the FY25 items were remediation provisions and a Bankwest restructuring provision).
- NAB guides "excluding any large notable items" (FY25 pres, p.25).

---

## 3. Return on equity (ROE)

### Metric names

- CBA: "Return on equity ('cash basis') — Based on net profit after tax ('cash basis') divided by average shareholders' equity" (FY25 PA glossary).
- NAB: "Cash ROE" / "Cash return on equity" (FY25 pres, pp.3, 14).
- ANZ reports a suite: "Return on average ordinary shareholders' equity", "Return on average tangible equity", "Return on average assets", "Return on average RWA" (1H26 RA, p.9).
- Westpac leads with "ROTE" (return on tangible equity) and "ROTE ex Notable Items" (FY25 IDP, pp.3–4).

### Conventional decomposition

Analyst convention splits an ROE move into a numerator effect (cash earnings movement, see section 2) and a denominator effect (average equity movement from retained earnings, dividends, buybacks, and capital raisings). The DuPont-style framing for banks is ROE = return on assets x leverage (assets / equity). The RBA states the mechanism: "Higher capital levels directly reduce ROE because the share of equity funding is greater for a given return on assets" (RBA FSR Oct 2016, Box C). The RBA Bulletin March 2017 article "Returns on Equity, Cost of Equity and the Implications for Banks" extends this framing. Buybacks lower the share count and average equity, and so support ROE and EPS; capital raisings do the reverse (same RBA Box C mechanism; each bank's buyback appears in its CET1 walk, see section 4).

Divisional convention: banks imply divisional ROE from allocated capital at the target CET1 ratio. NAB: divisional ROE is "implied by reported cash earnings on average RWA using 11.25% CET1 ratio" (FY25 pres, footnotes). CBA uses "Profit After Capital Charge (PACC) … a risk-adjusted measure" as its internal performance measure (FY25 PA glossary).

---

## 4. CET1 ratio

### Regulatory scaffolding (APRA)

- APS 110 sets the capital ratios (CET1, Tier 1, Total), the 4.5% CET1 minimum prudential capital requirement, buffers, and Attachment A on RWA calculation. <https://www.apra.gov.au/standards/aps-110>
- APS 111 defines what counts as CET1/AT1/Tier 2 capital and the regulatory adjustments (deductions). <https://www.apra.gov.au/standards/aps-111-final-not-force>
- RWA components: credit risk under APS 112 (standardised) and APS 113 (IRB); operational risk under APS 115; traded market risk under APS 116; interest rate risk in the banking book (IRRBB) under APS 117 for advanced ADIs. APRA's inclusion of IRRBB in RWA makes it a recurring walk item for the majors (all four cite IRRBB RWA moves; see below).
- Capital floor: an IRB ADI's total RWA cannot fall below 72.5% of RWA calculated under the standardised approach, applied at the aggregate level (APS 110 Attachment A; mechanics in APG 110: <https://www.apra.gov.au/practice-guides/apg-110>). ANZ and NAB both report a "capital floor adjustment" line; Westpac notes "Standardised floor met".
- Ratios are reported at "Level 1" (the ADI) and "Level 2" (the consolidated banking group); banks quote Level 2 as the headline and Level 1 alongside (NAB FY25 pres, p.29; Westpac FY25 IDP, p.77).

### The standard capital walk

Verbatim walk items:

- NAB (FY25 pres, p.29), Mar 25 12.01% to Sep 25 11.70%: "Cash earnings +0.82", "Dividend (0.61)", "Credit RWA (0.45)", "Other RWA 0.01", "Other (0.08)", plus a "Pro forma" bar for an announced divestment (MLC Life sale). Credit RWA is decomposed in a companion chart: "Volume", "Asset quality", "Models & methodology", "Derivatives & repurchase agreements", "Translation FX".
- Westpac (FY25 IDP, p.77): "Net profit", "1H25 dividend", "RWA", "IRRBB", "Other", "Capital return", with annotations "Share buyback (23bps)", "IRRBB standard changes 39bps", "Operational risk overlay removal 17bps".
- ANZ (1H26 RA, p.40), in bps: "Cash profit … +81 bps"; "Reinvestment of NOHC surplus capital, including the remaining $0.8 billion of the share buy-back … +22 bps"; "Payment of the 2025 final dividend (net of DRP discount and BOP) … -33 bps"; "Underlying RWA (excluding IRRBB) growth … -19 bps"; "Capital deductions and others … +7 bps"; "IRRBB RWA growth … -24 bps"; "A decrease in the capital floor adjustment … +2 bps".
- CBA (FY25 PA, p.28) lists drivers in text: "Capital generated from earnings"; completion of divestments; "The payment of the 1H25 dividend"; "Higher Credit Risk and Traded Market Risk RWA, partly offset by lower IRRBB RWA"; "Other regulatory adjustments and movement in reserves". CBA's RWA section separates Credit Risk RWA, Traded Market Risk RWA, IRRBB RWA, and Operational Risk RWA ("As required by APS 115 …").

### Vocabulary notes

- "Organic capital generation" is CBA's named concept: "cash net profit after tax less the …" (divisional capital pages, FY25 PA). The generic phrase "capital generated from earnings" also appears.
- Dividends enter the walk "net of DRP" where the DRP issues shares (ANZ wording above). CBA's DRP was "satisfied in full by the on-market purchase of shares", so it did not add capital (FY25 PA, p.28).
- Model and regulatory changes are a standard bar: NAB "Models & methodology" (with RWA overlays), Westpac "IRRBB standard changes" and "Operational risk overlay removal", ANZ "advanced Internal-Rating Based (IRB) model enhancement benefits" and "risk migration" (credit-quality-driven RWA change).
- Banks also publish an "Internationally comparable CET1 ratio" reconciliation (NAB FY25 pres, p.121-area; Westpac FY25 IDP, p.77), which removes APRA conservatism including the capital floor adjustment.

---

## 5. Credit impairment charge

### Accounting scaffolding (AASB 9)

AASB 9 section 5.5 sets the expected credit loss (ECL) model: Stage 1 assets carry a 12-month ECL allowance; a significant increase in credit risk (SICR) moves an asset to Stage 2 with lifetime ECL; credit-impaired assets are Stage 3 with lifetime ECL. ECL must be "an unbiased and probability-weighted amount" that reflects "reasonable and supportable information … about past events, current conditions and forecasts of future economic conditions" — the hook for forward-looking economic scenarios and probability weights. (AASB 9 compiled standard, paras 5.5.3, 5.5.5, 5.5.9, 5.5.17: <https://www.aasb.gov.au/admin/file/content105/c9/AASB9_12-14_COMPdec17_01-19.pdf>.)

### The line item name differs by bank

- NAB: "Credit impairment charge (CIC)" — also "credit impairment charge / (write-back)" (FY25 pres, p.26 and glossary).
- ANZ: "Credit impairment (charge)/release", split into "Individually assessed credit impairment charge/(release)" and "Collectively assessed credit impairment charge/(release)" (1H26 RA, p.9).
- Westpac: "Impairment charges" (an "impairment benefit" when negative) (FY25 IDP, pp.3, 49).
- CBA: "Loan impairment expense (LIE)" / "Loan impairment expense/(benefit)" (FY25 PA, p.18).

### Conventional driver decomposition

- Collective vs individual: NAB charts the CIC as "Individually assessed charge" + "Underlying CP charge/(write-back)" + "Forward looking provisions" (FY25 pres, p.26; CP = collective provision). Westpac decomposes into "New IAPs", "Write-backs & recoveries", "Write-offs direct", "Other movements in CAP" (FY25 IDP, p.49; IAP = individually assessed provisions, CAP = collectively assessed provisions). CBA narrates by division through "collective provision charges" and "individual provisions for single name exposures" (FY25 PA, p.18). ANZ uses "individually assessed" / "collectively assessed" splits (1H26 RA, p.9).
- Forward-looking overlays: NAB's glossary defines "EA — Economic Adjustment" and "FLA — Forward-Looking Adjustments"; its provision stack is "Forward Looking Collective Provision" vs "Underlying Collective Provision" (FY25 pres, pp.26–28, 132). Westpac shows "Overlays" as a provision component next to "Stage 1 CAP / Stage 2 CAP / Stage 3 CAP / Stage 3 IAP", and attributes moves to "Improvement in economics, partly offset by overlays" (FY25 IDP, pp.48–49). CBA cites "the reduction of some forward looking adjustments, mainly in Commercial Property" and links collective provisions to "an improving base case economic outlook" (FY25 PA, pp.6, 18).
- Portfolio growth: NAB "No underlying collective provisioning charge — volume growth and reducing impact from asset quality, offset by transfers to individual provisions" (FY25 pres, p.26).
- Specific exposures: "single name" is the standard phrase — NAB "Business lending single names impacting … individually assessed charges"; CBA "higher individual provisions for single name exposures".

### Loss-rate convention

The charge is normalised to basis points of gross loans, annualised for half years. The denominators differ in name: NAB "CIC as a % of GLAs (HY annualised)" (GLAs = gross loans and acceptances); CBA "Loan impairment expense as a percentage of average gross loans and acceptances (GLAAs) … 7 basis points"; ANZ "Total credit impairment charge/(release) as a % of average gross loans and advances"; Westpac "Impairment charge to average loans annualised". Coverage ratios also differ: NAB "Collective provisions/CRWAs"; Westpac "CAP to credit RWA"; Westpac tracks portfolio stress as "stressed exposures to TCE" (total committed exposure); CBA uses "Troublesome and Non-Performing Exposures (TNPE)". Default and 90+ days-past-due categories align to APS 220 Credit Risk Management (NAB FY25 pres, p.26 footnotes).

---

## 6. Cost-to-income ratio (CTI)

### Names and definitions

- CBA glossary: "Operating expenses to total operating income — Represents operating expenses as a percentage of total operating income. The ratio is a key efficiency measure." CBA quotes it with the result ("45.7% cost-to-income", FY25 PA, p.2).
- ANZ: "Operating expenses to operating income" (1H26 RA, p.9).
- Westpac: "Cost to income ratio", reported and "ex Notable Items" (FY25 IDP, pp.3–4).
- NAB: "CTI — Cost to income ratio" (FY25 pres glossary, p.132).

### "Jaws"

Jaws is the gap between income growth and expense growth. CBA's profit announcements define "Jaws" as the difference between total operating income growth and operating expense growth versus the prior comparative period, and CBA has used "positive jaws" as a headline claim since at least FY17 (CBA FY18 Profit Announcement: <https://www.commbank.com.au/content/dam/commbank/about-us/shareholders/pdfs/results/fy18/fy2018-profit-announcement.pdf>; FY17 media release: <https://www.commbank.com.au/content/dam/commbank/about-us/shareholders/pdfs/results/fy17/media-release.pdf>). The other three majors use the term in commentary and briefings rather than as a defined statistic — UNVERIFIED whether any of NAB/WBC/ANZ currently defines "jaws" in a glossary.

### Conventional expense drivers (the cost bridge)

- NAB FY25 expense bridge labels: "Salary related", "Volume related", "Technology & Investment", "Depreciation & Amortisation", "Productivity" (a negative bar, -$420m), "Payroll review and remediation", "EU" (AUSTRAC Enforceable Undertaking costs), "Other". Growth is quoted with and without the notable-like item: "YoY increase 4.6% (ex payroll review +3.2%)"; productivity target ">$450m"; investment spend "~$1.8bn". (FY25 pres, p.25.)
- Westpac FY25 expense bridge labels: "Staff costs", "Technology", "Volume and other", "Productivity", "Investments", "Restructuring charge"; "6% increase ex restructuring". Wage inflation appears as "Salary and EBA increases" (enterprise bargaining agreement) and technology spend through the "UNITE" simplification program. (FY25 IDP, p.27.)
- CBA expense lines: "Staff expenses" (up 7% on wage inflation and hours), "Occupancy and equipment expenses", "Information technology services expenses", plus "Restructuring and notable items" netted out of "underlying operating expenses". (FY25 PA, pp.15, expenses tables.)
- The CTI narrative convention: positive jaws lowers CTI; restructuring and remediation items are quoted separately so that the "underlying" CTI trend is visible (all four banks, documents above).

---

## 7. Terminology: adopt, avoid, and cross-bank differences

### Adopt (default vocabulary for the agent)

- "Credit impairment charge" for the P&L line, with "(write-back)"/"(release)" for the negative case. Map to each bank's label when quoting them (see table below).
- "Notable items" as the generic term for separately disclosed large items; say "significant items" when writing about ANZ.
- "Cash earnings" as the generic core-profit concept, but name the bank's own measure when quoting: NAB "cash earnings", ANZ "cash profit", CBA "cash NPAT", Westpac "net profit excluding Notable Items".
- "Basis points (bps)" for NIM, CET1, and loss-rate moves; parentheses for negatives.
- "Collective provision (CP)" and "individual/individually assessed provision (IP/IAP)"; "overlay" or "forward-looking adjustment" for post-model economic adjustments.
- "Replicating portfolio" and "capital benefit" for the deposit/capital hedge earnings; "Markets & Treasury contribution" for the volatile NIM component.
- "Loss rate" as credit impairment charge in bps of average gross loans (state the bank's denominator).
- "Positive/negative jaws" for income growth minus expense growth.
- "Organic capital generation" for earnings-less-dividend capital build; "dividend net of DRP".

### Avoid

- "Bad and doubtful debts" / "BDD": legacy pre-AASB 9 label. None of the four banks' current results materials reviewed here use it.
- "One-offs": use "notable items" (or the bank's own label); Westpac and ANZ define these categories formally.
- "Provision for bad debts": use "provision for expected credit losses" / "collective provision".
- "Cash profit" when writing about Westpac (it has no cash measure).
- "Loan loss provision expense" and other US-style terms ("net charge-offs", "allowance for loan losses"): use the Australian labels above.
- Mixing "NIM ex Markets" concepts across banks without care: NAB excludes M&T, Westpac excludes Treasury & Markets and Notable Items ("Core NIM"), ANZ excludes Markets, CBA excludes liquids/pooled facilities. These are not the same adjustment.

### Where the big four differ (quick reference)

| Concept | NAB | Westpac | CBA | ANZ |
|---|---|---|---|---|
| Core profit measure | "cash earnings" | "net profit excluding Notable Items" (no cash measure) | "cash NPAT" / cash basis | "cash profit" |
| Large-item label | "large notable items" (guidance wording) | "Notable Items" (5 defined categories) | "notable items" + "restructuring" (inside expenses) | "significant items" |
| Impairment P&L line | "credit impairment charge (CIC)" | "impairment charges" | "loan impairment expense (LIE)" | "credit impairment (charge)/release" |
| Provision split | CP / individually assessed; "EA" + "FLAs" | "CAP" / "IAP" by Stage 1/2/3 + "Overlays" | collective / individual provisions + "forward looking adjustments" | collectively assessed / individually assessed |
| Loss-rate denominator | GLAs (gross loans and acceptances) | average loans | GLAAs (gross loans and acceptances) | average gross loans and advances |
| Ex-volatile NIM | "NIM ex M&T" | "Core NIM" | "underlying" NIM excl. liquids & pooled facilities | "NIM (excl. Markets)" |
| Markets bar in NIM walk | "M&T" | "Treasury & Markets" | "Treasury and Markets" | "Markets activities" |
| Headline return metric | "Cash ROE" | "ROTE" (and ex Notable Items) | ROE "cash basis" | ROE + "Return on average tangible equity" |
| CTI label | "CTI — cost to income ratio" | "Cost to income ratio" (ex Notable Items) | "Operating expenses to total operating income" | "Operating expenses to operating income" |
| Pre-provision subtotal | "underlying profit" (UNVERIFIED for FY25) | "Pre-provision profit" | "Operating performance" | "Cash profit before credit impairment and income tax" |
| Asset-quality stress metric | "watch loans", NPEs as % of GLAs | "stressed exposures to TCE" | "TNPE" (troublesome + non-performing exposures) | (not sighted in extracts) UNVERIFIED |
| Balance date / period | 30 Sep FY; halves Mar/Sep | 30 Sep FY; halves Mar/Sep | 30 Jun FY; halves Dec/Jun | 30 Sep FY; halves Mar/Sep |

### UNVERIFIED items (collected)

1. Westpac's formal retirement date of "cash earnings" (believed FY22; not confirmed from a primary source here).
2. NAB's use of "underlying profit" as the pre-provision subtotal in FY25 documents (confirmed in prior-year usage patterns only; the FY25 MD&A likely defines it on p.10 but I did not extract that page).
3. Whether NAB/Westpac/ANZ currently define "jaws" in a glossary (CBA definition verified from FY18 PA).
4. ANZ's current named stress-watch metric equivalent to Westpac's "stressed exposures" (not sighted in the 1H26 extract).
5. ANZ's historical use of "large/notable items" naming before "significant items" (not verified from a primary source).
