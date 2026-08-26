# 24 — Defect: cross-source view pools walks of different comparisons

Type: task
Status: open

## Question

`cross_source_view` pools every extracted walk for a metric, so half-on-half bars leak into full-year disagreement lists (CBA run: "funding +2 (HoH) vs +0 (FY)" surfaced as a rounding disagreement — but they are different comparisons, not conflicting sources). Fix: group walks by comparison first (match walk endpoint labels/values against the case's period and comparator); corroboration and disagreement only compare walks of the SAME comparison; other-comparison walks are context, marked as such.
