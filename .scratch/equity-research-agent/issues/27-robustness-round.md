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
