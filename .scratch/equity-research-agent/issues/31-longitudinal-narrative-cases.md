# 31 — Longitudinal narrative holdout cases (multi-year, multi-document)

Type: task
Status: open

## Progress 2026-08-28

Corpus extended (FY22-FY24 fetched, FY20-FY26 continuous) and the NIM
longitudinal case is authored and hand-verified: `evals/gold/cba-longitudinal.json`
(holdout). Every year's walk read from the rendered page and summing exactly.
Bonus trap discovered during verification: the FY22 deck RESTATES the FY21
comparative NIM to 208 vs the 203 published in FY21's own documents — the
spine's basis shifts across eras, and the gold requires the narrative to
acknowledge it. Remaining: the impairment credit-cycle arc as a second case;
6-period-width testing of the ask entry point.

## Question

User requirement (2026-08-28, eval review): the existing crossref cases test consolidation within one results event; the harder — and more realistic — analyst task spans YEARS: "how did CBA's NIM evolve from FY21 to FY26 and what drove each phase?" That demands pulling the right evidence from every era's documents (five-plus PDFs, three disclosure-format eras), holding it together, and constructing a coherent narrative — not finding one fact in one file.

Build 1–2 such cases as HOLDOUT:

1. **Corpus extension first**: fetch CBA FY22, FY23, FY24 Profit Announcements (+ presentations where the era's walk lives there) from the results archive, manifest-pinned like FY21.
2. **Gold spine**: the year-by-year movement path with each year's published walk/driver set, each value with provenance (FY21 −4bps and FY25 +9bps and FY26 −3bps walks are already gold; FY22–24 need hand-verification).
3. **Narrative checklist**: the era phases a good multi-year note must name (COVID overlay build and unwind; the low-rate margin squeeze and TFF era; the rate-cycle margin expansion; the competition/liquids compression thereafter) — citation-graded.
4. **Required locations** across all era documents; location coverage plus fact accuracy scoring, as in ticket 26.
5. Candidate second case: the credit-cycle arc via impairment (FY20 COVID build $2,518m → FY21 unwind $554m → normalisation to FY26 $788m; loss rate 33 → 7 → 8bps).

The `ask` entry point already accepts multiple periods; it needs testing at 6-period width (evidence budget per document across ~10 PDFs).
