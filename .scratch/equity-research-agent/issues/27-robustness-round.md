# 27 — Robustness round: parse retry, load-bearing caps, FY25 chart, residual assist

Type: task
Status: open

## Question

Four precise defects from the 19-case suite (ticket 25's report, 2026-08-27):

1. **Author JSON parse retry**: two cases crashed on "Expecting ':' delimiter" — `author_attribution` has no parse-failure retry; `extract_walk` does. Mirror it.
2. **Load-bearing cap grading**: nim FY26 scored 7/7 recall and precision but a SECONDARY misread walk failed walk_sum and the fatal cap dropped confidence to 40. A walk_sum failure should be fatal only when the failing walk is the one the drivers rest on (another walk for the same comparison passed and the claims reconcile → peripheral).
3. **FY25 PA NIM chart vision failure**: the page breaks the vision reader with "Unterminated string" on both attempts (nim FY25 fell to 2/7). Diagnose the page (render size? label density?) and fix the read path.
4. **Residual assist in the author retry**: when drivers_reconcile fails, the retry message should include the code-computed implied residual (delta minus claimed sum) so the model corrects arithmetic instead of guessing again.

These plus defect 24 (comparison-aware machinery) are the remaining blockers on the CBA exit gate.

## Progress note — 2026-08-28 (all four items closed)

### 1. Author JSON parse retry

Mirroring the retry into `author_attribution` would have left the same hole in
`extract_text_evidence`, so the retry moved one level down into
`LLM.chat_json`: parse the reply, and on a parse failure re-issue the WHOLE
request (up to `json_retries=2`), asking for complete terminated JSON.
Re-issuing matters, because the failure is a truncated reply from a flaky
provider route: re-parsing the same text can never succeed, while a fresh
request usually lands on a healthy route. `extract_walk`'s own retry was
deleted as a duplicate. `Usage.json_retries` counts them.

The retry alone did not save both crashed cases. The CTI cases failed on a
different cause: the model wrote a row label in nested double quotes inside a
JSON string, which no retry can cure at temperature 0. The fix was to remove
the long free-text field that invited the quoting (see item 5) and to forbid
double quotes inside string values. `parse_json_block` now also reports the
90 characters either side of the error, so the next such break costs a log
line instead of a rerun.

### 2. Load-bearing grading of walk_sum failures

Rule, documented in `pipeline.py` beside the code: a walk_sum failure is fatal
only when the drivers rest on the walk that failed. The failing walk is
load-bearing when BOTH hold:

1. it is classified `primary` for the case comparison — a walk of a different
   comparison never supplies the driver table (defect 24), so its misread bars
   cannot corrupt the answer; and
2. no sibling primary walk passed its own sum check, OR the author's claims do
   not reconcile with the movement — either means no validated decomposition
   of this comparison survived.

Otherwise the failure is a peripheral secondary read: still listed in
limitations, no confidence cap. The older escalation ("when nothing at all
passed walk_sum, every peripheral failure becomes fatal") was also scoped to
walk failures only. It had been cancelling the two_level_arithmetic exemption
for `no_quantified_drivers` on ROE and CTI, which publish no walk at all, so
those cases were capped at 40 for being honest.

The nim FY26 case that motivated the ticket also had a fixable cause. The
vision reader had repeated the chart's END column as a final bar ("Jun 26 Full
Year: 205"), so the bars summed +202 instead of -3. `extract_walk` now drops a
bar whose LABEL matches an endpoint label, and the walk prompt says the bars
list holds only the columns between the endpoints. Matching on the label, not
the value, keeps a real bar that happens to equal an endpoint.

### 3. FY25 Profit Announcement NIM chart

Diagnosis: NOT a rendering problem. The page renders to a 304KB PNG at zoom 2,
and a direct API call returned the complete seven-bar walk first try. The
failing calls came back as '```json\n{\n  "title": "NIM Movement' — 34
characters, `finish_reason: "stop"`, 249 completion tokens billed. The provider
truncated the completion. The old code retried once at temperature 0 and hit
the same route, which is why both attempts failed identically.

Fix: the chat_json retry above (three attempts, a fresh request each time),
plus a last-resort re-render at zoom 3.0 in `extract_walk` once those are
spent — a second axis of variation, kept because the ticket asked for it, not
because the diagnosis blames the render.

Result: nim FY25 read all seven bars, 7/7 recall and precision at confidence
95, up from 2/7.

### 4. Residual assist in the author retry

`implied_residual` (validate.py) returns the movement delta minus the sum of
the claimed contributions. When `drivers_reconcile` fails, the retry message
carries `code_computed_implied_residual` with that number and the instruction
to declare exactly it or correct the contributions, and not to invent a third
number.

### 5. Two defects this round exposed

- `movement_source` as one free-text field became a scratchpad. On CBA
  impairment 1H26 the model wrote 120 words of reasoning into it, reached the
  right delta, and left the wrong numbers in `movement`. Three capped fields
  (row, from-column, to-column) leave no room to think, and their short values
  no longer carry the nested double quotes that broke both CTI cases.
- `basis` was being set from the discussion rather than from the row read.
  Rule 2 now says the field names the basis of the numbers inside `movement`,
  that an unlabelled row takes the bank's primary basis, and that "statutory"
  is never a default. The nim method hint adds the group-versus-division trap:
  a divisional table repeats a margin row for one business unit and must not
  supply the Group movement.

### Confidence ladder made explicit

Author rule 4 now grades each driver by how the number reached it, per
ADR-0001's evidence ladder: a walk bar of this comparison whose sum check
passed may reach 90-95; a movement the bank states in words or in a change
column may reach 90; a delta the model computed itself by subtracting two
period levels caps at 80; an unquantified narrative driver caps at 60. Computed
bridge deltas scored about 60% correct over the 0801 run, so 85 was
overconfident.

### 6. Wall-clock deadline on every request (found during the final suite)

A dev-suite run stalled for 30 minutes with zero completed cases. A stack
sample showed the process hot in `bytes_join`, assembling
`httpx` `response.content`, while a fresh completion returned in under two
seconds. Cause: `httpx`'s `timeout` bounds the gap BETWEEN chunks, never the
whole call, so a provider route that drips a body keeps the socket alive
indefinitely and the run never advances.

`LLM._post` now streams the response and checks two budgets per chunk: an
absolute wall-clock deadline and a maximum body size. A breach closes the
response and raises `ResponseDeadline`, which the existing retry loop treats
like any other failure, so the next attempt usually lands on a healthy route.
The deadline scales with the output the caller asked for — a floor of 120
seconds plus 0.02 seconds per requested token — so a 4k-token extraction gets
the floor while a 24k-token reasoning author still has room. `Usage` counts the
aborts as `deadline_aborts`.

### Status at handover

Items 1-4 are done and measured on the 20260828-1220 scorecard: no walk
extraction errors, NIM FY25 at 7/7 recall and precision, no spurious walk_sum
cap on NIM FY26, and the residual assist in place.

Two defects were diagnosed AFTER that scorecard and fixed but NOT yet
re-confirmed by a full suite run:

- The two CTI cases still crashed on it. The improved parse error named the
  cause: the model dropped a key's colon and wrote
  `"narrative "Operating expenses grew 5.8%",`. `parse_json_block` now tries
  two targeted repairs after a strict parse fails, and keeps a repair only if
  the patched text parses. Both CTI cases then completed
  (CTI 1H26 45.2 -> 45.9 and 45.2 -> 44.7 across two runs, CTI FY26
  45.7 -> 45.5).
- NIM FY25 scored WRONG on basis alone. The extractor had invented
  `statutory` for CBA's unlabelled Group NIM row, and the author repeated it.
  The extraction prompt now fills `basis` only when the page prints the word,
  and `_settle_basis` falls back to the registry's headline basis when the
  claimed basis appears in no cited quote. NIM FY25 then reported cash.

Both fixes were verified case by case; the confirming suite run was stopped
part way at the coordinator's instruction.

## Progress note — 2026-08-29 (component-column discipline, bridge completeness, per-driver walk cap)

Three defects from the 20260829 dev baseline, worked in priority order.

### 1. Component-column trap on cash_earnings 1H26 (was 0/3)

The movement machinery (rule 10, `check_movement_columns`) guarded the
headline only. The 1H26 case had the movement right and every component wrong:
the author took its component numbers from the prior-half column or from
half-on-half framings, because the pages that state the PCP movements were
never in evidence. Four changes, one per layer:

- **Retrieval**: the NII query was phrased for growth prose and ranked the NII
  section's CONTINUATION page above its table page, so the author never saw
  the stated PCP movement. Rephrased for the table page. A `extract_focus`
  was added for cash_earnings so the extractor covers every P&L line of the
  performance tables with one number per period column — before it, pages 27,
  34 and 35 of the 1H26 PA returned zero to six records; after, ten each with
  per-column labels.
- **Author prompt**: rule 10 now binds every COMPONENT of a bridge to the same
  column discipline as the movement, and each quantified driver returns a
  `columns` citation field (<=12 words), mirroring the three movement fields.
  The method hint names the mandatory components, the column subtraction rule,
  the prior-half-level trap, and the sign convention (an expense increase is a
  negative contribution).
- **Deterministic check**: `check_component_columns` (validate.py) mirrors
  `check_movement_columns` one level down, for bridge metrics only. It groups
  every extracted number by the period column its label names, strips the
  period out of the label to pair the same row's columns, and forms each row's
  three deltas. It fires when a claimed contribution matches a prior-half
  delta OR a prior-half level and matches no period-versus-comparator delta
  anywhere in evidence. Tolerance is `COMPONENT_TOL` = $2m, not the movement's
  $10m: component deltas subtract integer cells, and at $10m one component's
  half-on-half delta hid behind a neighbouring component's PCP delta.
  Replayed over the saved non-holdout artifacts before switch-on: zero fires
  (scoped to bridge metrics after it false-fired on two NIM/impairment
  artifacts in an unscoped replay). Synthetic 1H26-shaped fixtures live in
  `tests/test_component_columns.py`.
- **Result**: 1H26 movement OK, recall 2/3 with correct values (nii and
  impairment exact; the bridge sums to the delta exactly with no residual).
  The one miss is a framing gap, not a column error: the answer claims the
  underlying/notable expense split while this case's gold verifies the
  headline expense row. The FY26 gold verifies the underlying row, so the two
  golds disagree on framing; see the cap below.

### 2. FY26 completeness variance (was 3/4 to 4/4 across runs)

`unclaimed_components` (validate.py) reads a per-metric `component_labels`
map (taxonomy) and lists bridge components the evidence quantifies but the
answer leaves unclaimed — canonical id and evidence ids only, never a value.
A non-empty list drives the one author retry as a nudge; it is not a failed
check and never caps confidence. With the method hint's CLAIM EVERY COMPONENT
sentence, FY26 now claims all six components and reconciles exactly (4/4
recall and precision, no residual).

### 3. Per-driver cap under total walk failure

The evidence-ladder cap (defect 24) sat in an `elif` behind the fatal branch,
so the outage run shipped derived drivers at 90 under an attribution capped at
40. A standalone block now caps every driver at 85 whenever a walk metric has
no primary walk — context walks present or no walk extracted at all.
Unclassified-only walks stay exempt (the cold path for an unseen bank).

### Two calibration caps the rework exposed

- **Computed-delta cap made mechanical**: prompt rule 4 caps a self-computed
  delta at 80, and the model does not always obey. For bridge components the
  pipeline now checks whether any cited record PRINTS the claimed delta; if
  none does, the arithmetic is the model's own and confidence drops to 80
  (`computed_delta_cap_80`).
- **Framing-uncertainty cap**: when the answer claims the underlying/notable
  expense split, both claims cap at 80 — the bank equally publishes the
  combined headline framing, so a framing-relative claim cannot reach
  near-certainty. This is what keeps the 1H26 framing gap out of the
  confidently-wrong band honestly.

### 4. Mid-band overconfidence (note only)

On the frozen baseline, claims in the 70-84 band scored 0% correct (2 claims)
while 85+ scored 31/31: the model used 80 as its "probably right" default, so
the band under the confidently-wrong threshold was where its wrong guesses
pooled. The band was too small to read much into.

The final run changes the picture. The band now holds 8 claims at 88%
correct, because the mechanical caps move honest claims into it: the WBC
bridge scores 5/5 with every claim at 80. So the band is no longer a
wrong-way signal, but it is now a MIXED one — it holds both self-computed
correct claims and the round's two wrong claims. The next calibration round
should ask whether a self-computed delta that reconciles to the movement
deserves more than 80.

### 5. Extraction budget: a lost page crashed the case

The first verification suite crashed the NAB and WBC FY25 cash-earnings cases
with `Unterminated string` from `chat_json`. The cause was mine: the new
`extract_focus` asks for one record per P&L row per period column, and on a
dense performance-summary page that reply passed the 3000-token budget, so it
truncated mid-string and the whole PAGE was unparseable. Two fixes:

- The text-extraction budget is now 6000 tokens. One record per row per column
  is the point of the stage, so the budget must cover the densest page.
- A page that still fails no longer crashes the case. `run_case` catches the
  failure, keeps the pages that did read, and appends the lost page to
  `limitations`, so the gap is visible instead of silent.

Both cases then ran. Cold first-run scores (these ten NAB/WBC cases are new to
the suite, so they are a starting point, not a regression): NAB movement OK
with 2/3 recall; WBC 3/5 recall with the movement taken on the statutory
basis where the gold wants ex-Notables. Every wrong claim in both sits at 80,
under the confidently-wrong threshold, because the computed-delta cap fired on
each self-computed delta.

### Verification

Two baseline cases went red in the first suite and BOTH recovered on a
re-run with the same code, so they are run-to-run variance, not a regression:

- `CBA-cet1-1H26` recall 1/1 -> 0/1 -> 1/1. Both red and green runs sit at
  the same capped confidence. The baseline's green also carried a
  `comparison_leak` failure that the recovered run does not.
- `CBA-cti-1H26` movement OK -> variant row -> OK. This case picks between two
  adjacent ratio rows and was already failing one check at baseline.

Neither metric is a bridge, so none of the component-column work touches them.

### Final dev suite — `evals/results/20260829-1354-cheap-dev.md`

All 25 dev cases ran with the final code. No baseline case went red.

| Measure | Frozen baseline (15 CBA) | Final run (25 cases) |
|---|---|---|
| movements OK | 15/15 | 15/15 CBA, 22/25 overall |
| CBA cash_earnings 1H26 recall | 0/3 | 2/3 |
| CBA cash_earnings FY26 recall | 3/4 | 4/4 |
| CBA nim FY26 recall | 6/6 | 7/7 |
| NAB cash_earnings FY25 recall | crashed | 3/3 |
| WBC cash_earnings FY25 recall | crashed | 5/5 |
| Brier | 0.058 | 0.035 |
| confidently-wrong rate | 0.0 | 0.0 |
| 85+ claims correct | 31/31 | 36/36 |

The one remaining CBA 1H26 miss is a gold-framing question, not a wrong
number: the answer claims underlying expenses -348 plus notable items -170,
which sums to -518 — exactly the value this case's gold verifies on the
combined headline row. The FY26 gold verifies the underlying row instead, so
the two golds frame the same component differently. The framing cap holds
both claims at 80, so the split never reads as confidently wrong. A gold
decision is needed: either accept a split that sums to a verified parent, or
settle one framing per bank.

Three NAB/WBC cases report a wrong movement (NAB cti, WBC roe, WBC
impairment). All three are first runs of new cases and none is in scope here.
