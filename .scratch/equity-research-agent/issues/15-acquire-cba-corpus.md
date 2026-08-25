# 15 — Acquire the CBA corpus

Type: task
Status: resolved

## Question

Stand up the corpus machinery and fetch the CBA POC documents. Commit `manifest/cba.json` with the verified URLs from ticket 08 (FY26 Profit Announcement, FY26 Results Presentation, FY26 ASX Announcement, FY25 Profit Announcement). Write `scripts/fetch_corpus.py`: reads the manifest, downloads into gitignored `data/raw/<bank>/<period>/`, verifies sha256 when recorded, records checksums on first fetch (`--record`), skips verified files. Run it. AFK. The answer records file sizes and checksums.

## Answer

Done. `manifest/cba.json` (committed, checksums pinned) + `scripts/fetch_corpus.py` (stdlib only, idempotent, PDF-magic-byte check, trust-on-first-use `--record`). Fetched into `data/raw/CBA/`:

- FY26 Profit Announcement — 4.1 MiB, 152 pages
- FY26 Results Presentation — 5.7 MiB, 139 pages
- FY26 ASX Announcement — 0.4 MiB
- FY25 Profit Announcement — 2.8 MiB, 151 pages

Sanity check passed: page counts match ticket 08's inventory, and printed p12 = PDF page 28 contains the "Net Interest Income (continuing operations basis)" section — the +16 printed-page offset holds. `pymupdf` added as the PDF library.
