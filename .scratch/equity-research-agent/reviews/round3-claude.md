I have completed the review. All repros below were executed on commit d84a2f7 with `uv run python`; the suite is green (369 passed).

# Round 3 — reviewer C, read-only @ d84a2f7

I read all four archived reports and the round log first. I skip every fixed item and the five known-open items in the brief. **The code has not stabilised.** I found 6 new issues. Four of them sit inside round-2 fresh code, and two of those four are regressions the round-2 fix introduced.

---

## 1. HIGH — `_mint_record` verifies a NumberFact's VALUE and never its UNIT, so a model-supplied unit defeats the whole round-2 unit binding

`research_agent.py:1064` calls `quote_prints`; `validate.py:1108-1126`.

**Claim.** Codex round-1 item 1 asked for value **and** unit validation. The fix validates the value only — `quote_prints`'s first branch compares magnitudes with no unit at all, by design (`validate.py:1120-1122`). The unit therefore still arrives from the model. Every downstream check that B3 taught to bind units (`_states`, `validate.py:1129-1141`) then binds a unit the page never printed.

**Repro (executed).**
```
q = 'Net interest margin decreased 5 basis points to 2.03 per cent.'
quote_prints(q, 5, '$m')            -> True     # _mint_record KEEPS {"value":5,"unit":"$m"}
_states(5, '$m', 5, '$m', 0.5)      -> True
cap_weakly_cited_claims -> capped: []  driver +5 $m stays at confidence 95
```
The agent cites a real, verbatim, basis-point sentence, attaches `{"value": 5, "unit": "$m"}`, and a `+5 $m` driver keeps 95. This is Codex-1's own scenario with one field changed.

**Why it matters.** B3's conversion table is the round's headline tightening, and it reads `number.unit`. In the agent shell that field is still unverified, so the table binds a fiction.

**Fix.** In `quote_prints`, keep the bare-number branch but reject a number whose GLUED unit conflicts: when `quoted_unit` is present, accept only through `convert_unit`, and `continue` otherwise. That alone does not close this case, because "5 basis points" reads as bare — so it needs finding 5's suffix table too. The two fixes are one change.

**Verification.** Executed `quote_prints`, `_states` and `cap_weakly_cited_claims` on a constructed attribution.

---

## 2. HIGH — `settle_ratio_scale` reverses the percent-to-bps lift, and every check then passes

`validate.py:1273-1304`, against the lift at `research_agent.py:1262-1279` and `author.py:425-450`. Call sites: `research_agent.py:1407`, `pipeline.py:409`.

**Claim.** The lift keys on the METRIC's unit (`taxonomy["unit"] == "bps"`). `settle_ratio_scale` keys on `movement.unit`, which is a string the model wrote. When a model labels a bps metric's movement `"%"` — the exact condition the lift exists to repair — the lift multiplies the endpoints by 100 and `settle_ratio_scale` divides them straight back.

**Repro (executed).** CET1, taxonomy unit `bps`, evidence printing 12.20% and 12.30%:
```
model movement : 12.20 -> 12.30, delta 0.10, unit '%'
after bps lift : 1220.0 -> 1230.0, delta 10.0, unit '%'
settle_ratio_scale -> FIRED
after settle   : 12.2 -> 12.3, delta 0.1, unit '%'
check_movement    : passed ['movement_arithmetic']
check_ratio_level : passed ['movement_level_is_ratio_sized']
```
No check fires. The artifact ships a CET1 movement of `+0.1 %` against a gold of `+10 bps`, and carries two limitations that contradict each other: "converted from percent to bps", then "converted from basis points to %". The scorer marks `unit_ok` False, so the case scores WRONG.

**Reach.** The agent shell has no retry, so this ships. The pipeline gets one retry from `ratio_note`. Live: 0 of 76 saved artifacts hold a movement unit that differs from its taxonomy unit, so this is latent — but the trigger is the condition the lift was built for.

**Fix.** Give `settle_ratio_scale` the metric's unit, exactly as the lift has it. Return `None` unless the METRIC's unit is a ratio unit. Both call sites already hold `metric_cfg["unit"]`.

**Verification.** Executed the lift and the corrector in sequence, then both checks.

---

## 3. MED-HIGH — the narrowed `strip_markers` still deletes real table data; round 2 measured the least-affected documents

`research_agent.py:733` (`_MARKER_RE`).

**Both directions, as the brief asks.**

- The round-1 footnote repro still passes. `match_quote("Revenue from ordinary activities 30,153", CBA/FY26 PA p2)` returns `(True, markers_stripped)`. ✅
- It can still delete data. ❌

**Claim.** The shape rule requires a letter, a one- or two-digit run, then a value of three or more characters. A bank table row whose FIRST data column holds a small value and whose second holds a large one has exactly that shape. The rule cannot tell that row from a footnote marker.

**Repro (executed), ANZ 1H26 results announcement p59.**
```
page   : 'Credit and Capital Markets \n \n80 \n102 \n114  \n-22% \n-30%'
strip  : 'Credit and Capital Markets  \n102 \n114  \n-22% \n-30%'
match_quote('Credit and Capital Markets 102 114', page) -> (True, 'markers_stripped')
```
The quote is accepted as verbatim. It drops the current-period value 80 and presents 102 as the first column. A reader of the record reads the wrong period.

**Measured (executed) over all 30 corpus documents, 3546 pages.**

| window | pages | tokens removed |
|---|---|---|
| CBA FY26 + 1H26 only (round 2's window) | 607 | **198** |
| whole corpus | 3546 | **1670** |
| of which the newline-separated column class | | **734** |

The worst documents are the ones round 2 did not measure: `CBA/FY20/profit_announcement` 174, `CBA/FY22/profit_announcement` 169, `WBC/1H26/results_announcement` 60 (48 of them the dangerous class). Other real deletions: `ANZ Capital Notes 6/7/8/9` all become `ANZ Capital Notes` (four different instruments, the same defect as "Tier 1 / Tier 2"), `included in stage 2` becomes `included in stage`, and `Mar 26\n100\n101` in the presentations loses the column date.

**Fix.** Two steps.
1. Cheap and safe: require the run to sit on the LABEL's own line — `(?<=[A-Za-z])((?:[ \t]+\d{1,2})+)(?=\s+\(?[\d,]{3,})`. Measured: 1670 tokens fall to 779, and it kills the newline-column class outright, which is the class that deletes a data column. The round-1 repro still passes under it.
2. The remaining 779 are digits inside a LABEL ("Capital Notes 6", "Table 1", "ABN 16", "stage 2"), which no shape rule separates from a marker. Bound that by reading the page's own numbered footnote block and stripping only an index the page defines.

**Verification.** Corpus-wide token census with both patterns; `match_quote` executed against the real page texts; the round-1 repro re-executed.

---

## 4. MED-HIGH — an off-unit RESIDUAL is named as a mismatch and then added to the sum anyway

`validate.py:1211-1213` and `validate.py:1225-1226`.

**Claim.** B7 made the reconciliation sum unit-typed for CONTRIBUTIONS (`quantified` filters on the movement's unit at line 1214). The residual is put in `off_unit` at line 1213 and is then added to the total unfiltered at line 1225. The defect B7 closed stays open in the same function, for the other addend.

**Repro (executed).**
```
movement 5132 -> 5445, delta 313 $m
drivers  nii +310 $m
residual +3 bps
check_drivers_reconcile ->
  passed ['drivers_reconcile']
  failed ['drivers_unit_mismatch (+3 bps is not stated in the movement's unit ($m) ...)']
```
Three basis points closed a dollar bridge. `drivers_reconcile` PASSES.

**Compound effect.** A false `drivers_reconcile` pass also makes a failing walk non-load-bearing (`pipeline.py:559-561`, `research_agent.py:1457-1459`), and it keeps `cap_unreconciled_drivers` silent, because `drivers_unit_mismatch` is not in `WHOLE_TABLE_FAILURES` (see finding 6).

**Reach.** `drop_off_unit_contributions` iterates `drivers` only (`author.py:284`). Both shells take the residual raw from the model (`author.py:497`, `research_agent.py:1359`). Live: 0 off-unit residuals in the saved set, so this is latent.

**Fix.** Add the residual to the total only when its unit is empty or equal to the movement's unit. One condition.

**Verification.** Executed `check_drivers_reconcile` on a constructed attribution.

---

## 5. MED — `_FAMILY_WORDS["ppt"]` holds `"pt"`, which matches `"bpts"`, so the citation cap inverts by a factor of 100

`validate.py:1047-1055` (`_FAMILY_WORDS`) and `validate.py:1022-1042` (`_SUFFIX_UNITS`).

**Two joined defects.**
1. `_SUFFIX_UNITS` reads spelled-out MONEY ("million", "billion") and no spelled-out RATIO unit. `_quote_numbers("decreased 5 basis points")` returns `[(5.0, '')]`, so the number never reaches the `bps -> ppt` conversion B3 built.
2. The family test is a raw substring test on a two-letter token. `"pt"` is inside `"bpts"`, and inside ordinary English ("September", "accepted", "adopted", "except"). `_FAMILY_WORDS["cents"]` holds `"cent"`, which is inside "per cent" and "recent".

**Repro (executed) on two real shipped quotes.**
```
'Movements in bpts Credit Risk (34)'
   _quote_numbers -> [(34.0, '')]
   quote_states(34.0,  'ppt') -> True      # 34 ppt is 100x wrong
   quote_states(0.34, 'ppt')  -> False     # the CORRECT claim is refused
'RBS1 bpts 209 227 2H20 1H21 2H21'
   quote_states(209.0, 'ppt') -> True
```
The cap is exactly inverted, which is the same shape as round-2 finding B1, now in B1's own replacement.

**Live scale.** 203 of 2034 shipped quotes name only the bps family and still pass the ppt family test. I replayed the loose test against a strict one over all 729 shipped (driver, cited record) pairs: **0 verdicts differ today.** So this is a latent hole, not a shipped defect. I state that plainly.

**Fix.** Add the spelled-out ratio units to `_SUFFIX_UNITS`: `basis point(s)`, `bpt(s)`, `per cent`, `percentage point(s)`. Then drop `"pt"` and `"pct"`-style short tokens from `_FAMILY_WORDS` and match family words on word boundaries, not on substrings. This fix also closes finding 1's remaining half.

**Verification.** Executed `_quote_numbers` and `quote_states` on 18 real quote shapes; loose-versus-strict replay over every shipped driver/record pair; substring census over all 2034 shipped quotes.

---

## 6. MED — `cap_unreconciled_drivers` covers two failure names out of eight, and `comparison_leak` names its offender and never caps it

`validate.py:1312` (`WHOLE_TABLE_FAILURES`), against `validate.py:516-520` (`check_comparison_leak`).

**Claim.** B2's argument is that a failed check must reach the DRIVERS, because the calibration metrics read driver confidence. The implementation carries two names: `drivers_reconcile` and `movement_level_not_ratio_sized`. Six other fatal names cap the attribution to 40 and leave every driver untouched: `movement_arithmetic`, `comparison_leak`, `drivers_unit_mismatch`, `movement_columns`, `movement_variant`, `movement_basis`, plus `component_columns` and `walk_sum`.

`comparison_leak` is the strongest case, because it is the one check that names the offending driver: *"dividend_net_drp claims -91, which is the 'Dividends paid' bar of ... a walk for a different comparison"*. B2's stated reason for capping the whole table is that code cannot name the offender. Here code CAN name it, and it caps nobody.

**Live scale.** `comparison_leak` fires on 4 saved artifacts and `walk_sum` on 4. Three artifacts carry a fatal check with no whole-table name and still ship drivers at 85-90:
```
anz-nim-1h26-vs-1h25-cheap        walk_extraction_error   attr 40  4 drivers at 85
cba-nim-fy26-vs-fy25-agentic-cheap walk_sum               attr 85  2 drivers at 90
wbc-cet1-fy25-vs-fy24-cheap        walk_sum               attr 40  4 drivers at 85
```
The one `comparison_leak` artifact I inspected has its drivers at 80 already, capped by another rule, so the leak case is reachable rather than shipped.

**Fix.** Two parts. Cap the NAMED driver in `check_comparison_leak` itself, at `CLAIM_CITATION_CAP`, and record `comparison_leak_cap_80` on it. Add `movement_arithmetic` and `drivers_unit_mismatch` to `WHOLE_TABLE_FAILURES`, because a broken movement is the movement the whole table was written against — B2's own argument.

**Verification.** Failure-name census across every saved artifact; per-driver confidence read beside each artifact's fatal checks.

---

## Cap-stack trace (priority 2) — clean

I traced every cap in both shells. **No cap raises a confidence, none double-applies, and the order is identical in the two shells.**

| order | cap | pipeline | agent | direction |
|---|---|---|---|---|
| 1 | `settle_ratio_scale`, `settle_identity_scale` | 409-410 | 1407-1408 | corrects values |
| 2 | `corroborate` single_source 85 | 495 | 1409 | `min()` |
| 3 | `cap_weakly_cited_claims` 80 | 502 | 1413 | guarded, only lowers |
| 4 | bridge split framing 80 | 517 | 1423 | `min()` |
| 5 | fatal 40, then `cap_unreconciled_drivers` 80 | 596-600 | 1477-1481 | guarded, only lowers |
| 6 | no-primary-walk 85 | 613-615, 629 | 1488-1490, 1495 | `min()` |

Both cap functions start with `if driver.confidence <= CLAIM_CITATION_CAP: continue`, so a driver already at 70 keeps 70. `corroborate` runs before the citation cap in both shells. `finalise` runs once per case. The only ordering defect I found is finding 2, where a corrector reverses a corrector.

## Checked and found clean

`_quote_numbers` against 18 real quote shapes: glued units, spelled-out money, thousands separators, brackets, `FY25`/`1H26`/`p12` exclusion — all correct. The four-digit year drop removes 0 real NumberFacts across the whole saved set. `sign_flip_hint`'s arithmetic and its uniqueness guard are both correct (`gap == -2c` is the right signature). `extract_walk_annotations` cannot raise, so the annotation-on-failed-walk path is safe. The per-call budget ladder now binds cost, tool calls and the hard wall clock. `period_note` reaches both question prompts. `values_match`'s sign rule, `score_drivers`'s unit rule, `judge_facts`'s `quotes_used`, `_fit_quotes`, and post-submit atomicity are all correct. `RATIO_LEVEL_CEILING = 200` is safe: only `roe` and `cti` are ppt metrics, and both print levels between 10 and 55. `uv run python -m pytest tests/ -q` — **369 passed**.