# 18 — Acquire the NAB and Westpac corpus

Type: task
Status: resolved

## Question

Extend the manifest machinery to NAB and Westpac for the eval periods (NAB FY25 + 1H26; WBC FY25 + 1H26): results books / announcements, investor presentations / IDP, and Westpac's Key Financial Information Excel. URLs come from research tickets 09 and 10; scrape landing pages where direct links are missing (both banks' filenames drift). AFK. The answer records files, sizes, checksums.

## Answer

Resolved 2026-08-25. I wrote `manifest/nab.json` and `manifest/wbc.json` in the schema of `manifest/cba.json`. All URLs came from research files 09, 10, and 11. I verified each URL with a HEAD request before the fetch. Each request returned HTTP 200 with content type application/pdf or the xlsx type. The fetch script downloaded all ten documents and recorded the sha256 checksums in the manifests with `--record`. The files sit under `data/raw/NAB/` and `data/raw/WBC/`.

Files fetched (period, name, size, pages or sheets):

| Period | File | Size (bytes) | Pages / sheets |
|---|---|---|---|
| NAB FY25 | NAB-FY25-results-book.pdf (Management Discussion and Analysis) | 4,432,351 | 84 pages |
| NAB FY25 | NAB-FY25-investor-presentation.pdf | 3,223,914 | 134 pages |
| NAB 1H26 | NAB-1H26-results-book.pdf (Half Year Results book) | 5,703,606 | 108 pages |
| NAB 1H26 | NAB-1H26-investor-presentation.pdf | 2,947,103 | 129 pages |
| WBC FY25 | WBC-FY25-results-announcement.pdf | 962,235 | 67 pages |
| WBC FY25 | WBC-FY25-presentation-and-IDP.pdf | 2,974,258 | 125 pages |
| WBC FY25 | WBC-FY25-key-financial-information.xlsx | 212,774 | 32 sheets |
| WBC 1H26 | WBC-1H26-results-announcement.pdf | 3,167,310 | 114 pages |
| WBC 1H26 | WBC-1H26-presentation-and-IDP.pdf | 2,057,685 | 125 pages |
| WBC 1H26 | WBC-1H26-key-financial-information.xlsx | 188,534 | 29 sheets |

Checksums (sha256, recorded in the manifests):

- NAB-FY25-results-book.pdf: df0445a6cd5413b6e778cd347537d3008bf74a99fc1fa19c85b263e71b32cf7c
- NAB-FY25-investor-presentation.pdf: de3a394e6e1aeadd21e8347d4f67faf77ab39e1f3edbdaaf0d5253177d562d96
- NAB-1H26-results-book.pdf: 4b4984ec002dbef1035fdadb94dd64674c43d141099d68e18602d8aaf0cb3302
- NAB-1H26-investor-presentation.pdf: 520f2a59967e397910a60c9c539d591fb2c567ae26743730397636eb414a8db8
- WBC-FY25-results-announcement.pdf: a4cd05cf44f4fb45bb28998ef5c856a1cf7b0d13859acf49132cd41272110d64
- WBC-FY25-presentation-and-IDP.pdf: 61645f94df8560b87b9128142ab28de4802a5be3e95314f675ff1e2d1c83e13f
- WBC-FY25-key-financial-information.xlsx: 36745596356b76d320b9353367e02b72628584adf4bd159f67f6d30c4afce2b5
- WBC-1H26-results-announcement.pdf: 5d0e7d301d0efcac92723b67b82bfb15025927dbb48c6731e94d838e84317118
- WBC-1H26-presentation-and-IDP.pdf: 7af34e986c7f978fcc3216fdb4dcea29d525d78e9f76c3401785cc36ff7a6ae7
- WBC-1H26-key-financial-information.xlsx: 82294efe914dcc41da0f4cce3022382ac199812ed653961288915cf8984c5084

Cross-checks against the research inventories: the NAB 1H26 book has 108 pages (matches research 09), the WBC 1H26 announcement has 114 pages, the WBC IDPs have 125 pages, and the WBC 1H26 workbook has 29 sheets (all match research 10). Both xlsx files open as valid zip archives.

No documents were left out. There are no UNVERIFIED items for this ticket.
