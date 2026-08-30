# Round 2 — reviewer B (Claude), read-only @ 2177917

I read `round1-claude.md`, `round1-codex.md` and the round log first. I skip every fixed and known item. Every finding below carries an executed repro. The code did **not** stabilise: I found 9 new real issues, two of them in round-1 fresh code itself.

---

## 1. HIGH — `_quote_numbers` mis-parses any number with a glued unit suffix

`validate.py:902` (`_QUOTE_NUMBER_RE`), used by `cap_weakly_cited_claims` at `validate.py:950-953`.

**Claim.** The pattern ends with `(?![\w])`. A digit run followed by a letter fails that lookahead, so the regex backtracks and returns a **prefix** of the number. This is round-1 fresh code.

**Repro (executed).**
```
'cash NPAT of $10,982m'  -> [10.0, 7.0]      # not 10982
'fell 5bps'              -> []               # the number vanishes
'$2.5bn buyback'         -> [2.0]            # not 2.5
```
Both directions fire at once on one record:
```
quote: "Cash net profit after tax was $10,982m, up 7% on the prior year."
  nii            +10     $m  conf 95 -> KEPT   (falsely grounded by the prefix "10")
  tax_and_other  +10982  $m  conf 95 -> CAPPED (the quote literally prints it)
```

**Live scale.** 163 of 2042 shipped quotes (8.0%) carry a digit glued to a letter. Real examples from the saved set: `"(-3bps)"` → `[]`; `"(CET1 impact of -13bpts)"` → `13` lost while `[2.0, 2025.0, 643.0]` enters (a footnote index and a bare year).

**Failure scenario.** A driver that cites the record that prints its number is capped to 80. A neighbouring driver with a small round value is certified at 95 by a digit prefix. The cap is exactly inverted.

**Fix.** Allow a unit suffix after the number and consume it: `(?<![\w.])-?\d[\d,]*(?:\.\d+)?(?:\s*(?:bps|bpts|bp|ppt|ppts|m|bn|b|%))?(?![\w])`, and read the suffix as the number's unit (it feeds finding 3). Also drop a bare four-digit year token, as `FY25` already is.

**Verification.** `uv run python -c` over `_quote_numbers` and `cap_weakly_cited_claims`; corpus-wide count over `out/*/attribution.json`.

---

## 2. HIGH — a fatal check caps the attribution and never the drivers

`pipeline.py:558-561`, `research_agent.py:1401-1402`.

**Claim.** When `fatal` holds, only `attribution.attribution_confidence` drops to 40. Per-driver `confidence` is untouched for every method except `walk_extraction`. The scorer's Brier and confidently-wrong rate read **driver** confidence (`evals.py:907-919` over `_score_one_framing`'s `claim.confidence`), so the calibration metric is blind to every failed check.

**Live scale.** 22 saved artifacts carry a `Failed check:` limitation and still ship drivers at 80-90. Example: `cba-cash_earnings-1h26-vs-1h25-cheap` sits at `attr_conf 40` with six drivers at 80-85.

**Failure scenario.** This is the direct cause of the suite's one confidently-wrong claim (see finding 5). The bridge failed `drivers_reconcile`, the answer declared 40, and the offending driver kept 85.

**Fix.** When `drivers_reconcile` fails, cap every quantified driver at `CLAIM_CITATION_CAP` (80), which is below `CONFIDENT_THRESHOLD` (85). A bridge that does not close proves that one contribution is wrong, but not which one, so cap all of them. Add the same rule to both shells at the `if fatal:` branch. This only lowers confidence, so it loosens nothing.

**Verification.** Sweep of `out/*/attribution.json` comparing `attribution_confidence` against per-driver `confidence`.

---

## 3. PRE-SEEDED (a) — `cap_weakly_cited_claims` matches magnitude only

`validate.py:943-954`.

**Root cause.** The NumberFact branch compares `abs(number.value)` with `abs(driver.contribution.value)` and never reads `number.unit`. The quote branch has no unit at all.

**Live case, confirmed exactly.** `cba-cti-1h26-vs-1h25-cheap`, driver `notable_items +0.0 ppt` at confidence 90, cites `ev-16`:
```
quote:   "Restructuring and notable items ¹"
numbers: -170.0 $m (31 Dec 25) | -130.0 $m (30 Jun 25) | 0.0 $m (31 Dec 24)
```
The `0.0 $m` cell of a **dollar** row grounds a **percentage-point** claim. Repro also shows a `-5.0 bps` NumberFact grounding a `-5.0 $m` claim at confidence 95.

**Where the unit must bind.** At the NumberFact branch only (`validate.py:946-949`). The quote branch cannot read a unit today; after finding 1 it can, so bind it there too, and until then require the quote to contain a unit word of the claim's family.

**Convertible unit pairs.**

| claim unit | grounding unit | rule |
|---|---|---|
| `ppt` | `%`, `ppt`, `ratio` | same family, factor 1 |
| `ppt` / `%` | `bps` | factor 1/100 — a `-20 bps` fact grounds `-0.2 ppt`, never `-20 ppt` |
| `bps` | `%`, `ppt` | factor 100 |
| `$m` | `$m` | factor 1 |
| `$m` | `$bn`, `$b` | factor 1000 |
| anything | absent or empty unit | **no evidence either way — do not ground** |
| `$m` | any ratio unit | never |

**Fix.** Move `evals.UNIT_ALIASES` and `normalize_unit` into `validate.py` and import them from `evals` instead (the reverse import makes a cycle). Add `bpts`, `$bn`, `$b`, `cents` and `ratio` to the table — the saved set uses all five. Convert the NumberFact into the claim's unit, then compare with `CITATION_TOL` of the **claim's** unit. Add a test with the `ev-16` shape; no current test pins unit agreement.

**Verification.** Executed repro on `cap_weakly_cited_claims`; the `ev-16` record read from the shipped artifact; unit census over all saved records.

---

## 4. PRE-SEEDED (b) + PRIORITY 3 — nothing validates that a ratio's level is ratio-sized

`validate.py:275` (`check_movement`), `validate.py:838-870` (`settle_identity_scale`), `author.py:394-415` and `research_agent.py:1180-1195` (the percent-to-bps lift).

**Root cause.** A percent-to-bps lift exists for a `bps` metric. Its mirror does not exist. A `ppt` metric whose endpoints arrive in basis points passes every check: `check_movement` is self-consistent (1350 + 50 = 1400), `check_drivers_reconcile` closes at the same wrong scale, and `settle_identity_scale`'s guard needs a contribution larger than the level (1400), so it can never fire.

**This is the answer to priority 3.** `nab-roe-fy25-vs-fy24-agentic-cheap` is the **same defect**, not a wrong-row read:

- The agent read the **right** row. `movement_source` = `row 'Cash return on equity row'`, and `ev-1` is `NAB/FY25/results_book p10`: `"Cash return on equity 11.4% 11.6% (20 bps)"` with NumberFacts `11.4 %` and `11.6 %`. The gold cites that exact row and page.
- It then submitted `1160.0 -> 1140.0` unit `ppt`. It scaled the levels to match the printed `(20 bps)` change column and kept the metric's declared unit string.
- **The registry's headline-row label would not have prevented it.** The row was already correct.
- It is not a missing instruction either: `research_agent.py:262-266` says *"quote ratio metrics in points when the unit is ppt (45.7% -> 45.7, a 20 bpts improvement is delta -0.2)"*. The model ignored it. The pipeline prompt carries one extra anti-pattern sentence (`author.py:193-195`) that the agent prompt lacks, and the pipeline got **both** ROE cases right where the agent got both wrong.

So the failure is **tool-output-shaped and check-shaped, not prompt-shaped**. The fix is code.

**Minimal check design, measured over all 65 saved artifacts.** I replayed three candidates:

| candidate | fires | false fires |
|---|---|---|
| A: `ppt`/`%` level > 200 | 2 | **0** |
| B: both endpoints printed in the evidence | 7 | 5 (CET1 in bps against `12.20%` quotes) |
| C: mirror lift — endpoints/100 evidenced as `%` | 1 | 0 |

Candidate B is too noisy. Use **C as the corrector and A as the check**:

1. `settle_ratio_scale(attribution, records)` — mirror of the percent lift. When the unit is `ppt` or `%` and both `from_value / 100` and `to_value / 100` are evidenced as `%`/`ppt`/`ratio` (reuse `_percent_evidenced`), divide both endpoints and the delta by 100 and record the note. This auto-corrects the NAB case.
2. `check_ratio_level(movement)` — fail `movement_level_not_ratio_sized` when the unit is `ppt` or `%` and `max(|from|, |to|) > RATIO_LEVEL_CEILING`. Set `RATIO_LEVEL_CEILING = 200.0` with its reason: the largest ratio these banks print is an LCR near 130% or an NSFR near 115%, and the largest legitimate level in the saved set is a WBC CTI of 53.04. That gives 3.8x headroom above real data and 5.8x below the smallest defect.

Add it to the `output_failures` list in `pipeline.py:399-409` and to `finalise`, so the retry sees it and the fatal cap catches what the corrector cannot.

**Verification.** Replay script over 65 artifacts; the NAB gold read from `evals/gold/nab-fy25.json` (`11.6 -> 11.4, -0.2 ppt`); the agent's own evidence records.

---

## 5. PRE-SEEDED (c) — the `credit_impairment_charge -1.0` sign flip

`out/cba-cash_earnings-1h26-vs-1h25-cheap`, CBA 1H26 Profit Announcement p34.

**The path is none of the three you named.** It is not `settle_charge_sign` (`author.py:272-302`), which only touches the movement and only re-signs a pair of negative endpoints. It is not the bracket-negative rule; the page prints no bracket. It is not the delta harmoniser, which only compares the movement against its own endpoints.

**What happened.** The page text and the evidence say:
```
ev-21  "Loan impairment expense/(benefit) 319 406 320"
         319 (31 Dec 25) | 406 (30 Jun 25) | 320 (31 Dec 24)
ev-22  "Loan impairment expense was $319 million, a decrease of $1 million
        on the prior comparative period."   NumberFact: -1.0 $m
```
The charge **fell** by $1m, from 320 to 319. In a cash-earnings bridge a falling charge **adds** $1m to earnings, so the contribution is `+1` and the gold says `+1`. The model copied the change in the charge (`-1`) straight into the contribution field. Nothing converts a cost component's sign into its effect on earnings, and `_component_delta_pools` (`validate.py:571`) says so out loud: *"Magnitudes, because the author signs a cost component the other way up."*

**The bridge identity already found it.** `761 + 163 - 348 - 170 - 1 - 94 = 311` against a delta of `313`. The gap is `+2.00`, which is exactly twice the offending contribution. With `+1` the sum is `313` exactly. `drivers_reconcile` **failed** and is in the artifact's limitations. The claim still shipped at confidence 85 — because of finding 2.

**Fix, in two parts.**
1. Finding 2's cap. It removes the confidently-wrong claim on this case and on every other non-closing bridge.
2. A retry hint, not an auto-correction. When `drivers_reconcile` fails and the gap equals `-2 x c` for exactly **one** quantified contribution `c` (within `RECONCILE_TOL`), add to `author_validation`: *"the gap is exactly twice your `<canonical>` contribution; check its sign against the bridge's direction."* I replayed this probe over the 10 non-reconciling artifacts: it names `credit_impairment_charge -1.0` **uniquely** on this case, gives two candidates on `cba-cti-fy26` (so it reports ambiguity rather than a correction), and stays silent on the other eight. It names no gold value.

Optionally add a sign rule to the taxonomy: a `cash_earnings` component whose canonical is a cost or a charge takes its contribution as the negative of the change in that line. I did not verify that against every bank's framing, so I do not recommend it blind.

**Verification.** Artifact, evidence records and page text read directly; arithmetic checked; the twice-a-contribution probe replayed over every saved artifact.

---

## 6. MED-HIGH — `strip_markers` removes far more than footnote markers

`research_agent.py:690` (`_MARKER_RE`), `693-695`, `704-723`.

**Claim.** `(?<!\S)\d{1,2}(?!\S)` cannot tell a footnote marker from real data. On real pages the great majority of what it removes is data.

**Measured (executed).** Across the 607 pages of CBA FY26 and 1H26 it removes **10,158 tokens, 16.7 per page**. 324 pages (53%) lose 10 or more. What it removes on `CBA/1H26/profit_announcement` p34 and p54: the day and the two-digit year of every column header (`31 Dec 25`), bps values (`decreased 1 basis point to 6 basis points`), and capital tiers.

**Failure scenario.** These quotes are all accepted as verbatim under the relaxation:
```
"Additional Tier and Tier Capital."                    (page: "Additional Tier 1 and Tier 2 Capital.")
"decreased basis point to basis points"                (page: "decreased 1 basis point to 6 basis points")
"months at December 2025 was 5.2 years."               (page: "12 months at 31 December 2025 was 5.2 years.")
```
Tier 1 and Tier 2 are different instruments. The record then shows the author and the grounding judge a sentence with its load-bearing numbers removed, and the judge is asked whether the quotes entail the fact. The docstring's guarantee ("a quote may OMIT a marker but never STATE a number the page lacks") holds, but omitting the `1` from `Tier 1` changes the claim.

**Under-tested.** `tests/test_research_agent.py:1396` pins only the wrong-number direction. No test pins the drop direction.

**Fix.** Narrow the pattern so it only strips a marker in the shape a marker takes. Require the token to sit **between a letter and a digit run of three or more, or at the end of a label before a value**: e.g. `(?<=[A-Za-z])\s+\d{1,2}(?=\s+[\d(])` plus superscript characters. Then re-verify the round-1 repro (`"Revenue from ordinary activities 2 3 30,153"`). Add a red test for `"Additional Tier and Tier Capital."`.

**Verification.** Corpus-wide token count and per-page listing; `match_quote` run against the real page texts.

---

## 7. MED — `check_drivers_reconcile` still sums mixed units; the scorer still uses the gold unit

`validate.py:976-982`, `evals.py:674` and `evals.py:863`.

**Claim.** Round 1 made the reconciliation **tolerance** unit-typed. It did not make the **sum** unit-typed. `check_drivers_reconcile` adds `d.contribution.value` for every driver and never reads `d.contribution.unit`. `score_drivers` takes one `unit` from the gold movement and applies it to every claim. This is Codex round-1 finding #1's second half.

**Repro (executed).**
```python
movement 5132 -> 5445 delta 313 $m
drivers: nii +310 $m, mix +3 bps
check_drivers_reconcile -> (['drivers_reconcile'], [])
```
A `+3 bps` bar reconciles a `$m` bridge.

**Asymmetry.** The agent shell already guards this at `research_agent.py:1248-1262`: an off-unit contribution becomes narrative and the driver drops to 60. The pipeline's `author.py` has no equivalent.

**Honest limit.** This is latent, not shipped: **0** off-unit contributions across all 65 saved artifacts. A unit-typed tolerance over a unit-blind sum is still a hole.

**Fix.** Lift `research_agent.py:1248-1262` into `author.py` so both shells share it. Have `score_drivers` compare `claim.contribution.unit` against the gold unit and label a mismatch `INCORRECT`, not `CORRECT` by tolerance.

**Verification.** Executed repro; off-unit census over all saved artifacts.

---

## 8. MED — the delta harmoniser keeps a flat 0.51 that `check_movement` no longer uses

`author.py:424-430`, `research_agent.py:1199-1205`.

**Claim.** Round 1 gave `check_movement` a unit-typed table (`MOVEMENT_ARITHMETIC_TOL`, 0.1 for `ppt`). The two normalisers that **repair** the delta still test against a hard-coded `0.51`. The two now disagree for every ratio metric.

**Repro (executed).**
```
movement 45.0 -> 46.0 ppt, delta 1.5
harmoniser fires? False   (gap 0.5, threshold 0.51)
check_movement:  ['movement_arithmetic (45.0 + 1.5 != 46.0, tol 0.1 ppt)']
```
A repairable one-line slip now sinks the answer to confidence 40 instead of being corrected. The direction is safe, but the round left the fix half applied.

**Fix.** Import `MOVEMENT_ARITHMETIC_TOL` in both places and index it by `movement["unit"]`. Same constant, one source.

**Verification.** Executed repro against both functions.

---

## 9. MED — the agent's `cite` tool makes `numbers` optional, and the column checks go silent

`research_agent.py:473-475` (the `cite` schema, `"required": ["quote"]`), and the agent prompt, which never mentions `numbers`.

**Claim.** The pipeline's `extract_text_evidence` always emits NumberFacts. The agent's `cite` does not, and the prompt never asks for them. Every deterministic check that reads `record.numbers` therefore runs on an empty pool in the closed loop.

**Measured (executed).**

| shell | records | NumberFacts | per record |
|---|---|---|---|
| pipeline (`cheap`) | 1391 | 3467 | 2.49 |
| agent (`agentic-cheap`) | 651 | 485 | **0.75** |

Replaying `check_component_columns` and `check_movement_columns` over the bridge and note artifacts:

```
nab-cash_earnings-fy25-vs-fy24-agentic-cheap    0 nums   SILENT  SILENT   0 stems
nab-cash_earnings-fy25-vs-fy24-cheap          265 nums   SILENT  PASS    73 stems
cba-cash_earnings-1h26-vs-1h25-agentic-cheap   39 nums   PASS    PASS    11 stems
cba-cash_earnings-1h26-vs-1h25-cheap          317 nums   PASS    FAIL    99 stems
```
Four agentic bridge artifacts hold **zero** NumberFacts. `check_component_columns`, `check_movement_columns` and `_percent_evidenced` are all inert there. Defect 24's whole check family is switched off in the shell that is supposed to be compared against the pipeline — the same non-comparability that round-1 item 8 fixed for the annotation layer.

**Fix.** Add `numbers` to the `cite` item's `required` list, and add one line to the agent prompt: *"Every quote that carries a figure must list that figure in `numbers`, with its label, its period and its unit."* Then confirm that `_mint_record` still tolerates an empty list for a prose quote.

**Verification.** NumberFact census over all artifacts; replay of both column checks with real calendars from the registry.

---

## 10. MED-LOW — the period-substitution note reaches the reader and never the model

`ask.py:147-148` and `239`; `research_agent.py:1816-1817` and `1860`.

**Claim.** Round-1 item 14 records the substitution in `limitations`. Both shells add it **after** the answer exists. Neither prompt carries it. The model is asked about FY26, is handed FY25 documents, and is told nothing.

**Failure scenario.** The model hunts for FY26 pages that do not exist, spends budget, and can report an FY25 figure under an FY26 label. The reader sees the note; the answerer never did.

**Fix.** Pass `scope_notes` into `ANSWER_PROMPT` and `QUESTION_PROMPT` as a `period_note` field, the way the metric shell already passes `period_note` (`author.py:349`). One line in each shell.

**Verification.** Read of both call sites; no prompt format string takes the notes.

---

## 11. LOW — `extract_walk`'s endpoint scale harmoniser is still bps-calibrated

`extract.py:342-349`.

**Claim.** Round 1 gave the walk record its true unit (item 5) but left this threshold at a flat `10`. It is a basis-point quantity applied to every unit.

**Effect.** For a `ppt` walk the trigger `> 10` can never be reached, so the harmoniser is dead code there. For a `$m` walk it accepts a residual of up to 10 dollars-million as "the walk sums", which is ten times `RECONCILE_TOL["$m"]`, and it can rescale endpoints onto a wrong factor and then pass `check_walk`'s new 1.0.

**Fix.** Replace the two `10` literals with `walk_sum_tolerance(doc.doc_type, unit)`. `extract_walk` already takes `unit`.

**Verification.** Read of the arithmetic against the ppt and $m movement ranges in the saved set.

---

## 12. LOW — the per-call budget binds tool calls and time, but not cost

`research_agent.py:1552-1573`.

**Claim.** Round-1 item 11 binds `max_tool_calls` and the hard wall clock before every dispatched call. `cost_ceiling_usd` is still read once per turn (`research_agent.py:1491`). One `read_chart` now costs **two** vision calls (`extract_walk` plus `extract_walk_annotations`, added by round-1 item 8) and counts as one tool call.

**Failure scenario.** One turn that carries five `read_chart` calls issues ten vision calls with no cost check between them.

**Fix.** Add `elif llm.usage.cost_usd >= combo.cost_ceiling_usd:` to the per-call `stop` ladder, with the same message.

**Verification.** Read of the loop; the second vision call confirmed at `research_agent.py:894`.

---

## Checked and found clean

`_fit_quotes` (`judge.py:169`) — the block-length arithmetic is right, whole quotes only, and `quotes_used` is the true count. The one hole (a first quote longer than the whole budget escapes the cut) is unreachable: `EvidenceRecord.quote` is capped at 600 and `char_limit` is at least 4000. Post-submit atomicity (`research_agent.py:1544-1551`) is correct in both orders. `fetch_more`'s retry carry is correct in `pipeline.py:334` and was never broken in `ask.py:223`. `banks_named`'s phrase pass and `crossref_passes`'s `failed == 0` rule are both correct. `values_match`'s sign rule is correct. All 308 tests pass.

**Not re-reported** (known from round 1 and still open by the log's own account): the content-hash cache key, `ask.py`'s per-period page quota, the judge's character budget against a 48-quote window, and the LLM-side retry deadline.