# 24 — Defect: cross-source view pools walks of different comparisons

Type: task
Status: open

## Question

`cross_source_view` pools every extracted walk for a metric, so half-on-half bars leak into full-year disagreement lists (CBA run: "funding +2 (HoH) vs +0 (FY)" surfaced as a rounding disagreement — but they are different comparisons, not conflicting sources). Fix: group walks by comparison first (match walk endpoint labels/values against the case's period and comparator); corroboration and disagreement only compare walks of the SAME comparison; other-comparison walks are context, marked as such.

## Progress note — 2026-08-28 (comparison classification landed)

Root cause confirmed. The pipeline had no idea which comparison a walk
described. It pooled every walk into one `cross_source_view`, and the author
took whichever bar it read first. The four wrong movements came from this, in
two shapes.

1. Wrong walk. CET1 FY21 read the Dec 20 -> Jun 21 half-on-half walk and
   reported +50bps at confidence 100. The task movement is Jun 20 -> Jun 21.
2. Wrong table column. Half-year books print THREE period columns (current
   half, prior half, same half a year earlier). ROE 1H26 and CTI 1H26 took
   from_value from the middle column, which is the prior half, not the
   comparator. CET1 1H26 went further and took a slide's Level-1-style ratio
   instead of the APRA Level 2 row.

### The classifier (validate.py)

`period_end_date` resolves a period label to a balance date through the bank's
registry calendar: CBA's year ends in June, so 1H26 is the half ended December
2025; NAB, WBC and ANZ end in September, so their 1H26 is the half ended March
2026. `label_end_date` resolves a walk's printed endpoint labels the same way
("Dec 24 Half", "Jun 25 Level 2", "FY24", "2H25 Cash net interest margin").
`annotate_walks` compares the pair against the case's two dates and stamps
`comparison` = primary | context | unclassified, with the span in words.

Two decisions worth recording.

- Chart TITLES are ignored. The vision reader receives the case description
  and echoes it into the title: "CBA CET1 ratio in FY21 vs FY20" sat on the
  half-on-half chart. Only the endpoint labels are evidence of the comparison,
  so the walk prompt now demands them verbatim and forbids the task's periods.
- A PRO-FORMA endpoint makes a walk context whatever its dates say. CBA's FY21
  slide bridges Jun 20 to a Jun 21 pro-forma that already subtracts a buy-back
  announced after balance date, so its bars sum to a figure the bank never
  reported.

Classification was checked offline against every walk in `out/` before any
model ran: 17 walks over 4 banks and 7 cases, each one as hand-verified.

### What the classification changes

- `cross_source_view` receives walks of ONE comparison, so corroboration and
  disagreement compare like with like. Where the bank published no walk for
  the case comparison, the largest single other-comparison group is used
  instead: two half-on-half walks still corroborate each other.
- The author prompt labels every walk. Rule 6 forbids a context bar from
  becoming a `contribution`; its numbers belong in the narrative with the span
  named.
- Rule 10 (movement column) is mechanical. The pipeline computes both balance
  dates AND the prior-half date from the registry calendar and prints them as
  PERIOD DEFINITIONS. The author returns movement_row, movement_from_column
  and movement_to_column, capped at 12 words each; code composes them into the
  new `movement_source` field, which the report prints under the movement.
- Rule 11 (ratio variant): use the headline reported measure from the results
  book's KPI table. Level 1, internationally comparable, pro-forma, underlying
  and ex-notable are different measures, reported as context or disagreement.
- The extraction prompt demands one number per period column, all of them,
  each labelled with its own printed period. The old prompt dropped the third
  column and relabelled the prior half as the prior year.

### New deterministic checks

- `check_comparison_leak` fires on the exact symptom: a quantified
  contribution repeats a bar from a walk of a different comparison and no bar
  of the task's own walk gives that value. Output-level, so it drives the
  author retry with the offending label and source, and it is fatal.
- `check_movement_columns` reads the extracted evidence, not the model's note.
  It groups every extracted number by the balance date its label names, then
  fires only when from_value is a prior-half figure and is not a comparator
  figure. Replayed offline over 16 saved artifacts it fired on exactly one —
  the impairment 1H26 case that was wrong — and stayed silent or passed on the
  other 15.
- Evidence-ladder cap: a walk metric with no walk for the case comparison caps
  at confidence 85, with the reason in limitations. Prompt rule 4 already
  reserved >=90 for a bar backed by a walk of this comparison; the cap makes it
  mechanical, so a mis-sourced CET1 claim can no longer certify itself at 100.
  `no_quantified_drivers` becomes non-fatal in that state, because leaving the
  drivers unquantified is then the correct answer.
- The canonical label mapper gained a token pass that ignores filler words, so
  "Capital, Replicating & Other" and "Capital, Replicating and Other" map to
  the same driver. The miss was costing that bar its corroboration.

### Result

CBA-nim-1H26 precision 4/7 -> 7/7; the three leaked half-on-half bars are
gone. CET1 1H26 1530->1510 became 1220->1230. ROE 1H26 13.4->13.8 became
13.7->13.8. CTI 1H26 45.2->44.7 became 45.2->45.9. CET1 FY21 1260->1310 at
confidence 100 became 1160->1310 at 65.

### Suggested registry patch (not applied; ADR-0003)

`registry/cba.json` `cet1_walk_labels` has no entry for the FY21-era bars
("Divestments", "Off-market buy-back", "APRA Overlay Release", "Organic").
`check_comparison_leak` cannot see bars it cannot map, so CET1 FY21 still
claims a buy-back bar off the pro-forma walk (absorbed by a declared residual,
confidence 65). Adding those labels would close it.

### Round 2 (same day): three more mechanisms the first pass exposed

- `movement_source` as one free-text field became a scratchpad. On CBA
  impairment 1H26 the model wrote 120 words of reasoning into it, reached the
  right delta, and still left the half-on-half numbers in `movement`. It is now
  three capped fields — movement_row, movement_from_column, movement_to_column,
  12 words each — which code composes into the citation.
- `check_movement_columns` is the deterministic backstop for the same trap. It
  groups every extracted number by the balance date its label names and fires
  when from_value is a prior-half figure that is not also a comparator figure.
- `check_movement_variant` makes rule 11 mechanical. It reads the row the
  author says it used and fires on a variant word — underlying, ex-notable,
  pro-forma, internationally comparable, level 1 — that the bank's OWN headline
  label (from the registry) does not contain. Replayed over 19 saved artifacts
  it fired on exactly one, the CTI 1H26 run that had taken "Underlying
  operating expenses to underlying operating income" instead of the KPI row.

Both checks were replayed offline against every saved artifact before being
switched on, so their false-positive rate on this corpus is measured, not
assumed.

### Scorecard — 20260828-1220 (19 dev cases, cheap combo)

17 of 19 movements OK, against 12 of 17 scored on the same scorer for the 0801
artifacts. All four defect-24 movements are fixed: CET1 1H26, ROE 1H26, CTI
1H26 and CET1 FY21. NIM precision is 7/7 on 1H26, FY21 and FY25 (FY26 claimed
6 of its 6 slide-framing bars). Brier 0.061, confidently-wrong rate 0.0, from
0.265 on the 0801 run.

Status: the machinery is done and measured. What remains on this ticket is
the CBA registry label patch above, which only affects how much
`check_comparison_leak` can see on FY21-era CET1 bars.
