
## Fable probes on the crossref failures (2026-09-01)

The frozen crossref run failed all 5 hard consolidation cases. Diagnosis in
two parts:

1. HARNESS: the worst case (nim-longitudinal-fy21-fy26, 2/6 coverage) was a
   scope bug — "from FY21 to FY26" parsed as two years, so the agent never
   received the FY22-FY25 documents and said so itself at confidence 58.
   Fixed and pinned (range questions now load every year inside the range).

2. CAPABILITY: three Fable subagent probes ran the genuinely-missed
   questions under the benchmark protocol (question text + the four FY26
   PDFs; no gold, no hints; marked against required_locations afterwards):
   - dividend-drp-web: Fable 2/2 coverage (the loop missed presentation
     p32); every fact quote-carried.
   - notables-cti-web: Fable 2/3, same coverage as the loop, but its
     "missing" page has a same-figures substitute (profit p31 prints both
     CTI ratios verbatim) — partly a gold-authoring nit; Fable's facts all
     quote-complete vs the loop's 2/4.
   - restatement-web: Fable 3/3 coverage (the loop had 2/3) with the causal
     mechanism (fee inclusion, threshold removal) and the
     no-credit-deterioration ruling fully quoted.

Reading: the loop's remaining crossref gap is mostly retrieval DEPTH — the
frontier model keeps sweeping both documents after a first satisfying
answer; glm-flash stops earlier and quotes less completely. This matches
the bake-off's tier-bound hard-search finding (Opus 11 / Fable 10 /
glm-flash lower on coverage) and prices the ceiling: a frontier arm would
lift crossref coverage at roughly 100x the per-case cost.
