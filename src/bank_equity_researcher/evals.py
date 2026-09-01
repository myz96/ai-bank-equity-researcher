"""The eval harness (ticket 05): runs gold cases through the pipeline and
produces a scorecard — driver precision/recall, calibration, per-stage
extraction accuracy — never one blended number.

Scoring semantics (ticket 28, Codex findings 1, 4, 5, 6):

- A claim carries one of three labels: correct, incorrect, or unscored. A claim
  is unscored when the gold has no verified value for it. Unscored claims stay
  out of precision and calibration; a coverage stat counts them.
- The answer is scored against ONE eligible gold framing, never a mixture of
  framings. Canonical claims must be unique.
- A parent slot accepts a parent claim, or a set of child claims whose values
  sum to the parent value.
- Extraction matches bars one to one by canonical label AND value, inside ONE
  walk record whose endpoints are the case's movement.
- One typed tolerance serves every numeric comparison here.

tests/test_scoring.py is the executable specification of these rules.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .config import COMBOS, OUT_DIR, REGISTRY_DIR, REPO_ROOT
from .judge import answer_prose, cited_quotes, judge_facts
from .schema import Attribution, DriverClaim
from .validate import (
    MONEY_ABS_TOL_M,
    MONEY_REL_TOL,
    RATIO_TOL_PPT,
    WALK_BAR_TOL_PA,
    cross_source_view,
    normalize_unit,
)

GOLD_DIR = REPO_ROOT / "evals" / "gold"
RESULTS_DIR = REPO_ROOT / "evals" / "results"

CONFIDENT_THRESHOLD = 85  # claims at/above this count for the confidently-wrong rate
RELIABILITY_BUCKETS = [(0, 50), (50, 70), (70, 85), (85, 95), (95, 101)]

# The three claim labels (finding 1). "unscored" is not a soft "incorrect": it
# means the gold cannot decide the claim, so the claim must not reach precision
# or calibration.
CORRECT = "correct"
INCORRECT = "incorrect"
UNSCORED = "unscored"

# A catch-all bucket is not an economic concept: it can legitimately repeat, it
# satisfies no gold slot, and no gold value verifies it.
BUCKET_CANONICALS = {"other_unmapped"}

# The CET1 ratio is a regulatory capital measure with no cash / statutory /
# ex-notables basis, so the gold file's basis does not apply to it. Every other
# metric here is basis-sensitive (Westpac publishes NIM ex Notable Items).
BASIS_NOT_APPLICABLE = {"cet1"}


def load_gold(suite: str, bank: str | None = None) -> list[dict]:
    cases = []
    for path in sorted(GOLD_DIR.glob("*.json")):
        gold_file = json.loads(path.read_text())
        for case in gold_file["cases"]:
            if case.get("split", "dev") != suite:
                continue
            if bank and gold_file["bank"].upper() != bank.upper():
                continue
            if "movement" not in case:
                # Cross-reference consolidation cases (ticket 26) run through
                # the ask entry point, not the metric pipeline; skip here.
                continue
            cases.append({**case, "bank": gold_file["bank"], "period": gold_file["period"],
                          "comparator": gold_file["comparator"], "basis": gold_file["basis"]})
    return cases


def load_crossref_gold(bank: str | None = None) -> list[dict]:
    """Cross-reference consolidation cases (ticket 26): cases carrying
    required_locations instead of a movement. HOLDOUT: run only at milestones."""
    cases = []
    for path in sorted(GOLD_DIR.glob("*.json")):
        gold_file = json.loads(path.read_text())
        if gold_file.get("case_class") != "crossref_consolidation":
            continue
        if bank and gold_file["bank"].upper() != bank.upper():
            continue
        for case in gold_file["cases"]:
            cases.append({**case, "bank": gold_file["bank"], "period": gold_file["period"],
                          "comparator": gold_file["comparator"]})
    return cases


def load_question_gold(split: str = "dev", bank: str | None = None) -> list[dict]:
    """Free-form researcher questions: a case with a question and required
    locations, in a gold file that fixes no single bank or period.

    A question names its own banks and periods, so the case carries neither and
    the runner resolves the scope from the question itself. `bank` filters on
    the banks the question names, which is the only sense a bank filter has
    when one case can span three of them.
    """
    from .corpus import banks_named

    cases = []
    for path in sorted(GOLD_DIR.glob("*.json")):
        gold_file = json.loads(path.read_text())
        if gold_file.get("case_class") == "crossref_consolidation":
            continue
        for case in gold_file["cases"]:
            if "question" not in case or "movement" in case:
                continue
            if case.get("split", "dev") != split:
                continue
            if bank and bank.upper() not in banks_named(case["question"]):
                continue
            cases.append(dict(case))
    return cases


def _same_document(gold_doc: str, record_doc_id: str, index: dict[str, str] | None) -> bool:
    """Whether a gold location's document name is the record's document."""
    from .corpus import resolve_doc_name

    resolved = resolve_doc_name(gold_doc, index) if index else None
    if resolved is not None:
        return record_doc_id == resolved
    return str(gold_doc) in str(record_doc_id)


def crossref_answer_prose(ask_output: dict) -> str:
    """The answer's own words: the prose plus its key-fact sentences.

    The evidence quotes are deliberately left out. A note that pastes a quote
    saying the fact has not stated the fact itself (judge.answer_prose).
    """
    facts = "\n".join(f"- {f.get('fact', '')}" for f in ask_output.get("key_facts", []))
    return f"{ask_output.get('answer', '')}\n\nKey facts:\n{facts}".strip()


def score_crossref(
    gold_case: dict,
    ask_output: dict,
    llm=None,
    judges: tuple[str, ...] | None = None,
    doc_index: dict[str, str] | None = None,
    max_quotes: int | None = None,
) -> dict:
    """Location coverage AND judged fact accuracy — two populations, never one.

    Location coverage is the fraction of gold required_locations whose
    (doc, pdf_page) appears among the evidence records cited by the answer's
    key_facts. It measures retrieval, not correctness (finding 7).

    A gold author writes a document's name as a person does — "NAB/FY25/
    investor-presentation", "WBC/FY25/presentation-and-IDP" — and the corpus
    knows it by its doc_id. `doc_index` (corpus.doc_alias_index) maps one onto
    the other, so a spelling difference can never read as a missed page.
    Without it the name is matched as a substring, as it always was.

    Fact accuracy is the fraction of gold_answer_facts that the judges rule
    BOTH stated by the answer AND entailed by its cited quotes. Pass `llm` and
    `judges` to run it; without them the fact check is reported as not run,
    and the case cannot be called a pass.
    """
    cited_ids = {e for fact in ask_output.get("key_facts", []) for e in fact.get("evidence", [])}
    cited = [r for r in ask_output.get("evidence_records", []) if r["id"] in cited_ids]

    locations = []
    hits = 0
    for loc in gold_case.get("required_locations", []):
        hit_ids = [r["id"] for r in cited
                   if _same_document(loc["doc"], r["doc_id"], doc_index)
                   and r["pdf_page"] == loc["pdf_page"]]
        hits += bool(hit_ids)
        locations.append({"doc": loc["doc"], "pdf_page": loc["pdf_page"],
                          "holds": loc.get("holds", ""), "hit": bool(hit_ids),
                          "cited_by": hit_ids})
    total = len(locations)
    gold_facts = gold_case.get("gold_answer_facts", []) or []
    if llm is None or not judges:
        fact_check = {
            "status": "not_run (no judge client)",
            "gold_answer_facts": gold_facts,
            "fact_accuracy": None,
            "accuracy_fraction": None,
        }
    else:
        fact_check = judge_facts(
            llm,
            gold_facts,
            crossref_answer_prose(ask_output),
            [r.get("quote", "") for r in cited],
            tuple(judges),
            max_quotes=max_quotes,
        )

    coverage_fraction = round(hits / total, 3) if total else None
    row = {
        "case": gold_case["id"],
        "location_coverage": f"{hits}/{total}",
        "coverage_fraction": coverage_fraction,
        "locations": locations,
        "cited_evidence_ids": sorted(cited_ids),
        "confidence": ask_output.get("confidence"),
        "limitations": len(ask_output.get("limitations", [])),
        "fact_check": fact_check,
        "fact_accuracy": fact_check.get("fact_accuracy"),
        "cost_usd": ask_output.get("provenance", {}).get("cost_usd"),
        "seconds": ask_output.get("provenance", {}).get("seconds"),
    }
    row["passes"] = crossref_passes(coverage_fraction, fact_check)
    return row


# A crossref case passes only when the answer reached every required location
# AND the judges confirmed the gold facts (finding 7). Coverage is a necessary
# condition, never a sufficient one: the mortgage-offset answer scored 1/1
# coverage while omitting the required balances and adding an unsupported
# causal reading.
#
# Coverage must be complete. The gold names the locations that CARRY the
# answer; missing one means part of the answer was never sighted.
CROSSREF_COVERAGE_PASS = 1.0
# Fact accuracy allows one flagged or judge-split fact in a four-fact case
# without failing the whole case, and no more. The allowance covers a fact the
# judges could not settle — a split, or a judge that could not be read. It has
# never covered a fact the judges SETTLED AGAINST the answer.
CROSSREF_FACT_PASS = 0.75


def crossref_passes(coverage_fraction: float | None, fact_check: dict | None) -> bool | None:
    """None means "not decidable": an unjudged case is not a passing case.

    Three states, not two. A flagged fact is neither a pass nor a fail
    (judge.judge_facts), and the 0.75 allowance is what "neither" costs. A
    FAILED fact is the answer stating something the judges ruled absent or
    unentailed, and no allowance covers that.

    The rule used to read `accuracy_fraction` alone, which collapses all three
    states into passed/total. A case with three passes and one unanimous FAIL
    scored 0.75 and passed, though nothing about it was uncertain.
    """
    if coverage_fraction is None or not fact_check:
        return None
    total = fact_check.get("total") or 0
    if not total or fact_check.get("accuracy_fraction") is None:
        return None
    flagged = fact_check.get("flagged") or 0
    failed = fact_check.get("failed")
    if failed is None:
        failed = total - (fact_check.get("passed") or 0) - flagged
    return (
        coverage_fraction >= CROSSREF_COVERAGE_PASS
        and failed == 0
        and (total - flagged) / total >= CROSSREF_FACT_PASS
    )


def run_answer_suite(kind: str, gold_cases: list[dict], combo: str) -> Path:
    """Run free-form question cases through the COMBO'S OWN shell and score them.

    One runner serves both answer suites — the crossref holdout and the
    researcher questions — because they differ only in which gold they load
    (finding 8: the run/write loops belong behind one helper). The shell comes
    from config.question_runner_for and from nowhere else (finding 1), so a
    suite can never measure one shell under the other's label. Since ticket 33
    wave 3 that seam has one shell behind it, the closed loop.
    """
    from .config import question_runner_for
    from .corpus import doc_alias_index
    from .llm import LLM

    run_question = question_runner_for(combo)
    judges = COMBOS[combo].judges
    judge_llm = LLM()
    doc_index = doc_alias_index()
    rows = []
    for gold in gold_cases:
        label = f"{gold.get('bank') or 'multi-bank'} {gold['id']}"
        try:
            # A case that fixes its bank and periods passes them as hints; a
            # question that names its own is scoped from the question itself.
            periods = [p for p in (gold.get("period"), gold.get("comparator")) if p]
            output, _ = run_question(
                gold.get("bank"), gold["question"], combo, periods or None
            )
            # Researcher-question answers legitimately cite ~40 records; the
            # frozen 24-quote window dropped grounding they actually had
            # (measured 2026-08-30: 15 of 39 cited records never reached the
            # entailment judge). The wider window applies to every arm of the
            # questions suite equally; the crossref holdout keeps the frozen
            # default for comparability with its earlier runs.
            row = score_crossref(
                gold, output, judge_llm, judges, doc_index,
                max_quotes=48 if kind == "questions" else None,
            )
        except Exception as exc:  # noqa: BLE001 - a crashed case is a scored failure
            row = {"case": label, "error": str(exc)[:300]}
        print(f"scored {label}: {json.dumps({k: v for k, v in row.items() if k not in ('locations', 'fact_check')})[:250]}")
        rows.append(row)

    stamp = run_stamp()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RESULTS_DIR / f"{stamp}-{combo}-{kind}.jsonl"
    raw_path.write_text("\n".join(json.dumps(r) for r in rows))

    lines = [f"# {kind.capitalize()} scorecard — combo {combo}, {stamp}", ""]
    lines += scorecard_meta(stamp, f"judges: {', '.join(judges)}")
    lines += [
        "",
        (
            "Two populations, reported apart. **Location coverage** measures the "
            "retriever: did the answer cite the pages that carry the answer? "
            "**Fully-grounded facts** measures citation discipline, not analysis "
            "quality: did the judges rule each gold fact both STATED by the answer "
            "and ENTAILED by its cited quotes, with EVERY load-bearing number "
            "present in those quotes? An answer whose analysis is right but whose "
            "quotes omit a number it used scores a fail here by design "
            "(measured 2026-08-31: frontier agents state nearly every gold fact "
            "and lose this column on quote completeness). A "
            f"case PASSES only when coverage is {CROSSREF_COVERAGE_PASS:.0%}, NO "
            "fact failed, and the facts the judges could not settle stay inside "
            f"{1 - CROSSREF_FACT_PASS:.0%} of the case. A flagged fact is neither "
            "a pass nor a fail; a failed fact is the answer getting it wrong, and "
            "no allowance covers that. Coverage alone is not correctness "
            "(ticket 29, finding 7)."
        ),
        "",
    ]
    lines.append("| Case | Pass | Location coverage | Fully-grounded facts | Flagged | Missed locations | Conf | Cost |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in rows:
        if "error" in r:
            lines.append(f"| {r['case']} | ERROR: {r['error'][:60]} | | | | | | |")
            continue
        missed = "; ".join(
            f"{loc['doc']} p{loc['pdf_page']}" for loc in r["locations"] if not loc["hit"]
        ) or "—"
        passes = {True: "PASS", False: "FAIL", None: "—"}[r.get("passes")]
        fact_check = r.get("fact_check", {})
        lines.append(
            f"| {r['case']} | {passes} | {r['location_coverage']} "
            f"| {fact_check.get('fact_accuracy', '—')} | {fact_check.get('flagged', '—')} "
            f"| {missed} | {r['confidence']} | ${r.get('cost_usd', 0)} |"
        )
    lines += ["", "## Judged facts", ""]
    for r in rows:
        if "error" in r:
            continue
        lines.append(f"### {r['case']}")
        for fact in r.get("fact_check", {}).get("facts", []):
            lines.append(f"- **{fact['verdict']}** — {fact['fact']}")
            lines.append(f"  - {fact['reason']}")
        lines.append("")
    lines.append(
        f"Judge cost: ${round(judge_llm.usage.cost_usd, 4)} over "
        f"{judge_llm.usage.calls} calls (on top of the per-case answer cost)."
    )
    card_path = RESULTS_DIR / f"{stamp}-{combo}-{kind}.md"
    card_path.write_text("\n".join(lines) + "\n")
    return card_path


def run_crossref_suite(combo: str, bank: str | None = None) -> Path:
    """Run every crossref HOLDOUT case, then report location coverage AND
    judged fact accuracy. Discipline: run at most once per milestone; never
    iterate on it."""
    return run_answer_suite("crossref", load_crossref_gold(bank), combo)


def run_question_suite(combo: str, bank: str | None = None, split: str = "dev",
                       only: str | None = None) -> Path:
    """Run the free-form researcher questions, scored like the crossref cases.

    `only` filters case ids for fast loops, exactly as it does for the metric
    suite: a comma-separated list of fragments matched against the case id.
    """
    cases = load_question_gold(split, bank)
    if only:
        wanted = [w.strip().lower() for w in only.split(",") if w.strip()]
        cases = [c for c in cases if any(w in c["id"].lower() for w in wanted)]
    return run_answer_suite("questions", cases, combo)


# ---------------------------------------------------------------------------
# One typed tolerance (finding 6). The constants live in validate.py with the
# reason they have their value; this is the single place that applies them to
# a comparison, so the harness and the deterministic checks cannot disagree.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Tolerance:
    """A unit-typed match tolerance: max(absolute, relative x |target|)."""

    unit: str
    absolute: float
    relative: float = 0.0

    def for_target(self, target: float) -> float:
        return max(self.absolute, self.relative * abs(float(target)))


def tolerance_for(unit: str | None) -> Tolerance:
    canonical = normalize_unit(unit)
    if canonical == "$m":
        # Banks round to $m; 1% or $10m (whichever is larger) absorbs
        # re-presented comparatives without letting real errors through.
        return Tolerance("$m", MONEY_ABS_TOL_M, MONEY_REL_TOL)
    if canonical in ("ppt", "%"):
        return Tolerance(canonical, RATIO_TOL_PPT)
    if canonical == "bps":
        return Tolerance("bps", WALK_BAR_TOL_PA)
    return Tolerance(canonical, WALK_BAR_TOL_PA)


def values_match(value: float, target: float, unit: str | None) -> bool:
    """A sign flip is never a rounding difference, so it never matches.

    The sign rule used to be gated on `abs(target) > tol`, which made it dead
    code: opposite signs put the two numbers at least `|value| + |target|`
    apart, so wherever the gate was open the distance check below had already
    returned False. Inside the gate — a target smaller than its own tolerance,
    which the $10m money floor makes common — a claim of the OPPOSITE
    DIRECTION scored correct. Two live dev gold targets sit there: CBA 1H26
    impairment moved -1 $m, and an answer of +9 $m was graded a match, so a
    charge that fell was credited to an answer that said it rose.
    """
    tol = tolerance_for(unit).for_target(target)
    if value * target < 0:
        return False
    return abs(value - target) <= tol


# ---------------------------------------------------------------------------
# Gold framings (finding 4)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Framing:
    """One coherent gold decomposition of a movement.

    slots           canonical -> verified value (the scored population)
    unscored_slots  canonicals the gold names but does not verify
    known_children  child canonical -> verified value, where the gold splits a
                    parent slot further
    exhaustive      True when the gold covers the whole movement, so a claim
                    outside it is wrong rather than unknown. A published walk
                    is exhaustive; component and arithmetic gold is not
                    (evals/gold/README.md: reconciliation is never force-fitted).
    """

    name: str
    slots: dict[str, float]
    unscored_slots: frozenset[str] = frozenset()
    known_children: dict[str, float] = field(default_factory=dict)
    exhaustive: bool = False


def _numeric(value) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _verified_value(entry) -> float | None:
    """Gold entries come as a bare number or {value, provenance, ...}. A missing
    or null value, a direction-only entry, or an UNVERIFIED provenance means the
    gold does not verify this driver (evals/gold/README.md)."""
    if isinstance(entry, dict):
        if "UNVERIFIED" in str(entry.get("provenance", "")).upper():
            return None
        return _numeric(entry.get("value"))
    return _numeric(entry)


def gold_framings(gold: dict) -> list[Framing]:
    """The primary framing first, then each accepted alternate framing."""
    gold_drivers = gold.get("gold_drivers", {}) or {}
    slots: dict[str, float] = {}
    unscored: set[str] = set()
    for canonical, entry in (gold_drivers.get("drivers", {}) or {}).items():
        value = _verified_value(entry)
        if value is None:
            unscored.add(canonical)
        else:
            slots[canonical] = value
    # A "<parent>_children" block verifies the split of a parent slot (the CET1
    # rwa case): those children are scored on their own values.
    known_children: dict[str, float] = {}
    for key, block in gold_drivers.items():
        if not key.endswith("_children") or not isinstance(block, dict):
            continue
        for child, entry in block.items():
            value = _verified_value(entry)
            if value is not None:
                known_children[child] = value
    exhaustive = bool(gold_drivers.get("exhaustive", gold_drivers.get("tier") == "walk"))
    framings = [Framing("primary", slots, frozenset(unscored), known_children, exhaustive)]
    for alt in gold.get("alt_framings", []) or []:
        alt_slots = {}
        for canonical, entry in (alt.get("drivers", {}) or {}).items():
            value = _verified_value(entry)
            if value is not None:
                alt_slots[canonical] = value
        framings.append(
            Framing(f"alt:{alt.get('source', '?')}", alt_slots, frozenset(), {}, exhaustive)
        )
    return framings


def gold_comparison_mismatch(gold: dict) -> bool:
    """True when the gold decomposition describes a different comparison from
    the case (the FY26 CET1 gold holds a half-on-half walk)."""
    declared = (gold.get("gold_drivers", {}) or {}).get("comparison")
    if not declared:
        return False
    wanted = f"{gold['period']}vs{gold['comparator']}".lower()
    return declared.lower().replace(" ", "") != wanted


def _ancestors(canonical: str) -> list[str]:
    """'rwa.credit.corporate' -> ['rwa.credit', 'rwa'] (closest first)."""
    parts = canonical.split(".")
    return [".".join(parts[:i]) for i in range(len(parts) - 1, 0, -1)]


def _slot_ancestor(canonical: str, slots: dict[str, float]) -> str | None:
    return next((parent for parent in _ancestors(canonical) if parent in slots), None)


# ---------------------------------------------------------------------------
# Driver scoring (findings 1 and 4)
# ---------------------------------------------------------------------------


def _score_one_framing(framing: Framing, claims: list[DriverClaim], unit: str) -> dict:
    entries: list[dict] = []
    first_seen: set[str] = set()
    deferred: dict[str, list[int]] = {}
    invalid_parents: set[str] = set()
    matched: set[str] = set()
    duplicates = 0

    def label(entry: dict, state: str, reason: str) -> None:
        entry["label"], entry["reason"] = state, reason

    for index, claim in enumerate(claims):
        canonical = claim.canonical
        entry = {
            "canonical": canonical,
            "value": claim.contribution.value,
            "confidence": claim.confidence,
            "label": None,
            "reason": "",
        }
        entries.append(entry)
        value = entry["value"]

        # The gold states its values in ONE unit, and the harness used to apply
        # that unit to every claim whatever the claim said its own unit was: a
        # "+3 bps" contribution was scored against a "+3 $m" gold slot and
        # graded correct by tolerance. A claim in another unit is a claim about
        # something else, so it is wrong, not right.
        claimed_unit = normalize_unit(claim.contribution.unit)
        if claimed_unit and claimed_unit != normalize_unit(unit):
            label(
                entry,
                INCORRECT,
                f"claimed in {claim.contribution.unit}, and this movement is stated in {unit}",
            )
            continue
        if canonical in BUCKET_CANONICALS:
            label(entry, UNSCORED, "catch-all bucket: no canonical gold slot verifies it")
            continue
        if canonical in first_seen:
            duplicates += 1
            verified = canonical in framing.slots or canonical in framing.known_children
            label(
                entry,
                INCORRECT if verified else UNSCORED,
                "duplicate canonical claim: one canonical concept has one contribution",
            )
            continue
        first_seen.add(canonical)

        if canonical in framing.slots:
            target = framing.slots[canonical]
            if values_match(value, target, unit):
                label(entry, CORRECT, f"matches gold {target:+g}")
                matched.add(canonical)
            else:
                label(entry, INCORRECT, f"gold {target:+g}")
            continue

        parent = _slot_ancestor(canonical, framing.slots)
        if canonical in framing.known_children:
            target = framing.known_children[canonical]
            if values_match(value, target, unit):
                label(entry, CORRECT, f"matches gold child {target:+g}")
            else:
                label(entry, INCORRECT, f"gold child {target:+g}")
                if parent:
                    invalid_parents.add(parent)
            if parent:
                deferred.setdefault(parent, []).append(index)
            continue

        if parent:
            deferred.setdefault(parent, []).append(index)
            continue
        if canonical in framing.unscored_slots:
            label(entry, UNSCORED, "gold names this driver but verifies no value")
            continue
        children = [slot for slot in framing.slots if _slot_ancestor(slot, {canonical: 0.0})]
        if children:
            label(
                entry,
                INCORRECT,
                f"gold decomposes this into {', '.join(sorted(children))}; "
                "a parent claim satisfies a parent slot only",
            )
            continue
        if framing.exhaustive:
            label(entry, INCORRECT, "not a driver of this gold framing")
        else:
            label(entry, UNSCORED, "gold does not cover this driver")

    # Parent slots may be satisfied by a set of child claims that sums to them.
    for parent, indexes in deferred.items():
        target = framing.slots[parent]
        total = sum(entries[i]["value"] for i in indexes)
        taken = parent in matched  # a parent claim already holds the slot
        sums = not taken and parent not in invalid_parents and values_match(total, target, unit)
        if sums:
            matched.add(parent)
        reason = (
            f"the {parent} slot is already claimed as a whole; children double-count it"
            if taken
            else f"children of {parent} sum {total:+g} vs gold {target:+g}"
        )
        for i in indexes:
            if entries[i]["label"] is None:
                label(entries[i], CORRECT if sums else INCORRECT, reason)

    correct = sum(1 for e in entries if e["label"] == CORRECT)
    incorrect = sum(1 for e in entries if e["label"] == INCORRECT)
    return {
        "framing": framing.name,
        "claims": entries,
        "correct": correct,
        "incorrect": incorrect,
        "unscored": sum(1 for e in entries if e["label"] == UNSCORED),
        "duplicate_canonicals": duplicates,
        "recall_matched": len(matched),
        "recall_total": len(framing.slots),
        "recall": (
            f"{len(matched)}/{len(framing.slots)}"
            if framing.slots
            else "n/a (no verified numeric gold)"
        ),
        "precision": (
            f"{correct}/{correct + incorrect}"
            if framing.slots
            else "n/a (no verified numeric gold)"
        ),
        "unscored_gold_slots": len(framing.unscored_slots),
    }


def score_drivers(framings: list[Framing], claims: list[DriverClaim], unit: str) -> dict:
    """Score the quantified claims one-to-one against ONE eligible framing.

    An alternate framing is taken as a whole or not at all: precision and recall
    always come from the same framing, so a mixture of decompositions cannot
    collect credit no published source supports.
    """
    quantified = [c for c in claims if c.contribution is not None]
    scored = [_score_one_framing(f, quantified, unit) for f in framings]
    ranked = sorted(
        enumerate(scored),
        key=lambda pair: (
            pair[1]["recall_matched"],
            pair[1]["correct"],
            -pair[1]["incorrect"],
            -pair[0],  # ties go to the primary framing
        ),
        reverse=True,
    )
    return ranked[0][1]


# ---------------------------------------------------------------------------
# Extraction scoring (finding 5)
# ---------------------------------------------------------------------------

_NUMBER = re.compile(r"-?\d+(?:\.\d+)?")


def walk_endpoints(record) -> tuple[float, float] | None:
    """Read (start, end) from a walk record's code-stamped quote:
    '[walk chart] <title>: <start label> <start> -> <end label> <end>'.
    Endpoint labels carry their own digits ('Jun 26 Full Year 205'), so each
    endpoint is the LAST number on its side of the arrow."""
    quote = record.quote or ""
    if "->" not in quote:
        return None
    left, _, right = quote.rpartition("->")
    starts, ends = _NUMBER.findall(left), _NUMBER.findall(right)
    if not starts or not ends:
        return None
    return float(starts[-1]), float(ends[-1])


def _record_canonicals(record, label_map: dict[str, str]) -> list[tuple[str, float]]:
    """Bar labels mapped to canonical ids with the registry's verbatim label map
    (the same mapping the pipeline shows the author)."""
    walk = {
        "source": record.id,
        "bars": [{"label": n.label, "bps": n.value} for n in record.numbers],
    }
    view = cross_source_view([walk], label_map or {})
    return [(canonical, bar["value"]) for canonical, bars in view.items() for bar in bars]


def _match_bars(slots: dict[str, float], bars: list[tuple[str, float]], unit: str) -> int:
    """One-to-one: each extracted bar satisfies at most one gold bar, and only
    when its canonical label AND its value agree."""
    available = list(bars)
    hits = 0
    for slot, target in slots.items():
        for i, (canonical, value) in enumerate(available):
            same_slot = canonical == slot or _slot_ancestor(canonical, {slot: 0.0}) == slot
            if same_slot and values_match(value, target, unit):
                available.pop(i)
                hits += 1
                break
    return hits


def score_extraction(
    gold: dict, attribution: Attribution, unit: str, label_map: dict[str, str] | None = None
) -> dict:
    """Per-stage read accuracy of the case's walk: the gold bars found, by label
    and value, inside ONE walk record whose endpoints are the case's movement."""
    gold_drivers = gold.get("gold_drivers", {}) or {}
    if gold_drivers.get("tier") != "walk":
        return {"extraction": None, "status": "no walk-tier gold for this case"}
    if gold_comparison_mismatch(gold):
        return {
            "extraction": "n/a (gold walk is not the case comparison)",
            "status": "gold holds a walk for another comparison",
        }
    framings = [f for f in gold_framings(gold) if f.slots]
    if not framings:
        return {"extraction": None, "status": "no verified gold bars"}

    movement = gold["movement"]
    records = [r for r in attribution.evidence_records if r.kind == "walk_vision"]
    eligible = []
    for record in records:
        endpoints = walk_endpoints(record)
        if endpoints and values_match(endpoints[0], movement["from"], unit) and values_match(
            endpoints[1], movement["to"], unit
        ):
            eligible.append(record)
    if not eligible:
        return {
            "extraction": f"0/{len(framings[0].slots)}",
            "status": f"no extracted walk runs {movement['from']:g} -> {movement['to']:g} "
            f"({len(records)} walk records read)",
            "walk": None,
        }

    best = (0, framings[0], eligible[0])
    for framing in framings:
        for record in eligible:
            hits = _match_bars(framing.slots, _record_canonicals(record, label_map or {}), unit)
            if hits > best[0]:
                best = (hits, framing, record)
    hits, framing, record = best
    return {
        "extraction": f"{hits}/{len(framing.slots)}",
        "status": "ok",
        "walk": f"{record.id} {record.doc_id} p{record.pdf_page}",
        "framing": framing.name,
    }


# ---------------------------------------------------------------------------
# Case scoring
# ---------------------------------------------------------------------------


def walk_label_map(bank: str, metric: str) -> dict[str, str]:
    path = REGISTRY_DIR / f"{bank.lower()}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text()).get(f"{metric}_walk_labels", {})


def score_movement(gold: dict, attribution: Attribution, unit: str) -> dict:
    """Numbers, unit, basis and comparator all have to agree (finding 6)."""
    movement, gold_movement = attribution.movement, gold["movement"]
    numbers_ok = bool(
        movement
        and values_match(movement.from_value, gold_movement["from"], unit)
        and values_match(movement.to_value, gold_movement["to"], unit)
        and values_match(movement.delta, gold_movement["delta"], unit)
    )
    unit_ok = bool(movement and normalize_unit(movement.unit) == unit)
    if gold["metric"] in BASIS_NOT_APPLICABLE or not gold.get("basis"):
        basis_ok = None
    else:
        basis_ok = (attribution.basis or "").strip().lower() == gold["basis"].strip().lower()
    comparison_ok = (
        attribution.period.upper() == gold["period"].upper()
        and attribution.comparator.upper() == gold["comparator"].upper()
    )
    return {
        "numbers_ok": numbers_ok,
        "unit_ok": unit_ok,
        "basis_ok": basis_ok,
        "comparison_ok": comparison_ok,
        "answer_basis": attribution.basis,
        "gold_basis": gold.get("basis"),
        "answer_unit": movement.unit if movement else None,
    }


def score_case(gold: dict, attribution: Attribution, label_map: dict[str, str] | None = None) -> dict:
    unit = normalize_unit(gold["movement"]["unit"])
    result: dict = {"case": f"{gold['bank']}-{gold['metric']}-{gold['period']}", "metric": gold["metric"]}

    # 1. Movement: numbers, unit, basis and comparator.
    detail = score_movement(gold, attribution, unit)
    result["movement_detail"] = detail
    result["movement_ok"] = bool(
        detail["numbers_ok"]
        and detail["unit_ok"]
        and detail["comparison_ok"]
        and detail["basis_ok"] is not False
    )

    # 2. Drivers: one framing, unique claims, three-state labels.
    quantified = [d for d in attribution.drivers if d.contribution is not None]
    if gold_comparison_mismatch(gold):
        reason = "gold decomposes a different comparison"
        result["driver_recall"] = f"n/a ({reason})"
        result["driver_precision"] = f"n/a ({reason})"
        result["framing"] = None
        result["claims"] = [
            {"canonical": d.canonical, "value": d.contribution.value, "confidence": d.confidence,
             "label": UNSCORED, "reason": reason}
            for d in quantified
        ]
        coverage = {"correct": 0, "incorrect": 0, "unscored": len(quantified),
                    "duplicate_canonicals": 0, "unscored_gold_slots": 0}
    else:
        scored = score_drivers(gold_framings(gold), attribution.drivers, unit)
        result["driver_recall"] = scored["recall"]
        result["driver_precision"] = scored["precision"]
        result["framing"] = scored["framing"]
        result["claims"] = scored["claims"]
        coverage = {key: scored[key] for key in
                    ("correct", "incorrect", "unscored", "duplicate_canonicals", "unscored_gold_slots")}
    coverage["quantified_claims"] = len(quantified)
    coverage["unquantified_drivers"] = len(attribution.drivers) - len(quantified)
    result["coverage"] = coverage

    # 3. Per-stage extraction accuracy.
    if label_map is None:
        label_map = walk_label_map(gold["bank"], gold["metric"])
    extraction = score_extraction(gold, attribution, unit, label_map)
    if extraction["extraction"] is not None:
        result["extraction"] = extraction["extraction"]
        result["extraction_detail"] = extraction

    # 4. Honesty signals.
    result["failed_checks"] = sum(1 for item in attribution.limitations if item.startswith("Failed check:"))
    result["attribution_confidence"] = attribution.attribution_confidence
    result["cost_usd"] = attribution.provenance.get("cost_usd")
    result["seconds"] = attribution.provenance.get("seconds")
    return result


def calibration(rows: list[dict]) -> dict:
    """Calibration runs over scored claims only: a claim the gold cannot decide
    is not evidence either way, so it is reported as coverage instead."""
    claims = [c for r in rows for c in r.get("claims", [])]
    scored = [c for c in claims if c.get("label") in (CORRECT, INCORRECT)]
    coverage = {
        "scored_claims": len(scored),
        "unscored_claims": len(claims) - len(scored),
        "cases_scored": sum(1 for r in rows if any(
            c.get("label") in (CORRECT, INCORRECT) for c in r.get("claims", []))),
        "cases": len(rows),
    }
    if not scored:
        return {**coverage, "brier": None, "confidently_wrong_rate": None, "reliability": []}
    def hit(claim: dict) -> float:
        return 1.0 if claim["label"] == CORRECT else 0.0

    brier = sum((c["confidence"] / 100 - hit(c)) ** 2 for c in scored) / len(scored)
    confident = [c for c in scored if c["confidence"] >= CONFIDENT_THRESHOLD]
    table = []
    for lo, hi in RELIABILITY_BUCKETS:
        bucket = [c for c in scored if lo <= c["confidence"] < hi]
        if bucket:
            accuracy = sum(hit(c) for c in bucket) / len(bucket)
            table.append(f"{lo}-{hi - 1}: {len(bucket)} claims, {accuracy:.0%} correct")
    return {
        **coverage,
        "brier": round(brier, 3),
        "confidently_wrong_rate": (
            round(sum(1 for c in confident if c["label"] == INCORRECT) / len(confident), 3)
            if confident else None
        ),
        "reliability": table,
    }


def run_suite(suite: str, combo: str, bank: str | None = None, only: str | None = None) -> Path:
    """`only` filters cases for fast iteration loops: a comma-separated list of
    metric names and/or bank-metric-period fragments, matched case-insensitively
    against "BANK-metric-PERIOD" (e.g. "cash_earnings", "nim-1H26",
    "NAB,WBC-cti"). Full suites remain the gate at the end of a round."""
    from .config import runner_for

    run_case = runner_for(combo)

    gold_cases = load_gold(suite, bank)
    if only:
        wanted = [w.strip().lower() for w in only.split(",") if w.strip()]
        gold_cases = [
            g for g in gold_cases
            if any(w in f"{g['bank']}-{g['metric']}-{g['period']}".lower() for w in wanted)
        ]
    rows = []
    for gold in gold_cases:
        label = f"{gold['bank']} {gold['metric']} {gold['period']}"
        try:
            attribution, _ = run_case(gold["bank"], gold["metric"], gold["period"], gold["comparator"], combo)
            row = score_case(gold, attribution)
        except Exception as exc:  # noqa: BLE001 - a crashed case is a scored failure
            row = {"case": label, "metric": gold["metric"], "error": str(exc)[:300]}
        print(f"scored {label}: {json.dumps({k: v for k, v in row.items() if k != 'claims'})[:200]}")
        rows.append(row)

    stamp = run_stamp()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RESULTS_DIR / f"{stamp}-{combo}-{suite}.jsonl"
    raw_path.write_text("\n".join(json.dumps(r) for r in rows))

    card_path = RESULTS_DIR / f"{stamp}-{combo}-{suite}.md"
    card_path.write_text(
        "\n".join(scorecard_lines(f"Scorecard — suite {suite}, combo {combo}, {stamp}", rows)) + "\n"
    )
    return card_path


# ---------------------------------------------------------------------------
# Scorecards and the offline rescore (ticket 28 verification)
# ---------------------------------------------------------------------------


def _git_commit() -> str:
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT,
                              capture_output=True, text=True, timeout=10, check=False)
        status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT,
                                capture_output=True, text=True, timeout=10, check=False)
    except Exception:  # noqa: BLE001 - metadata is best-effort, never fatal
        return "unknown"
    return head.stdout.strip() + (" (working tree dirty)" if status.stdout.strip() else "")


def _gold_sha() -> str:
    """One hash over the whole gold set, so a scorecard names the gold it used."""
    digest = hashlib.sha256()
    for path in sorted(GOLD_DIR.glob("*.json")):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()[:16]


def run_stamp() -> str:
    """One UTC clock reading per run, shared by the file names and the header."""
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")


def scorecard_meta(stamp: str, *extra: str) -> list[str]:
    """The header that makes two runs comparable experiments (finding 10)."""
    lines = [
        "## Run metadata",
        "",
        f"- run: {stamp} (UTC)",
        f"- commit: {_git_commit()}",
        f"- gold sha256 (evals/gold/*.json, first 16): {_gold_sha()}",
    ]
    lines += [f"- {item}" for item in extra if item]
    return lines


def artifact_dir(gold: dict, combo: str) -> Path:
    """The saved out/<slug>/ directory for one gold case and one combo."""
    slug = f"{gold['bank']}-{gold['metric']}-{gold['period']}-vs-{gold['comparator']}-{combo}".lower()
    return OUT_DIR / slug


# ---------------------------------------------------------------------------
# Narrative checklist grading (ticket 29 finding 7; gold README: "checklist
# items are never value-scored; they are graded by citation-grounding").
# ---------------------------------------------------------------------------


def judge_case_checklist(llm, gold: dict, combo: str, judges: tuple[str, ...]) -> dict:
    """Grade one case's narrative_checklist against its SAVED artifact.

    No pipeline stage runs and no document is fetched. The report's own prose
    answers "does the note say it"; the quotes its drivers cite answer "does
    the source support it".
    """
    case = f"{gold['bank']}-{gold['metric']}-{gold['period']}"
    row = {"case": case, "metric": gold["metric"], "period": gold["period"]}
    checklist = [str(item) for item in (gold.get("narrative_checklist") or [])]
    out = artifact_dir(gold, combo)
    row["artifact"] = f"out/{out.name}"
    if not checklist:
        return {**row, "status": "no narrative_checklist in gold", "note": "", "total": 0}
    if not (out / "report.md").exists() or not (out / "attribution.json").exists():
        return {**row, "status": "no saved artifact", "note": f"out/{out.name}",
                "total": len(checklist)}

    attribution = json.loads((out / "attribution.json").read_text())
    row["artifact_generated"] = attribution.get("provenance", {}).get("generated", "")
    graded = judge_facts(
        llm,
        checklist,
        answer_prose((out / "report.md").read_text()),
        cited_quotes(attribution),
        judges,
    )
    return {**row, **graded}


JUDGE_COMBO = "agentic"


def run_judge_suite(suite: str = "dev", combo: str = "agentic", bank: str | None = None) -> Path:
    """Judge every case's narrative checklist and write a coverage scorecard.

    `combo` is a SLUG SELECTOR, exactly as `rescore` treats it: it names which
    saved `out/<slug>/` artifacts to grade and never which shell to run,
    because this action runs no shell. It therefore accepts a retired combo
    name, and the frozen `-cheap` baseline stays gradable. Reading
    `COMBOS[combo].judges` here made a retired name raise a bare `KeyError`,
    and the default was itself a retired name, so the call crashed on its own
    defaults. The judges come from the one live combo instead: they grade the
    artifact, so they have nothing to do with the arm that produced it.
    """
    from .llm import LLM

    judges = COMBOS[JUDGE_COMBO].judges
    llm = LLM()
    rows = []
    for gold in load_gold(suite, bank):
        row = judge_case_checklist(llm, gold, combo, judges)
        print(f"judged {row['case']}: {row.get('fact_accuracy', row.get('status'))} "
              f"flagged={row.get('flagged', '—')} spend=${round(llm.usage.cost_usd, 4)}")
        rows.append(row)

    stamp = run_stamp()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    (RESULTS_DIR / f"{stamp}-{combo}-{suite}-judge.jsonl").write_text(
        "\n".join(json.dumps(r) for r in rows)
    )
    card_path = RESULTS_DIR / f"{stamp}-{combo}-{suite}-judge.md"
    card_path.write_text(
        "\n".join(judge_scorecard_lines(stamp, suite, combo, judges, rows, llm)) + "\n"
    )
    return card_path


def judge_scorecard_lines(
    stamp: str, suite: str, combo: str, judges, rows: list[dict], llm
) -> list[str]:
    """Coverage first (finding 2), then the rate, then every judged item."""
    judged = [r for r in rows if r.get("status") == "judged"]
    items = sum(r["total"] for r in judged)
    passed = sum(r["passed"] for r in judged)
    flagged = sum(r["flagged"] for r in judged)
    flagged_split = sum(r["flagged_split"] for r in judged)
    flagged_unreadable = sum(r["flagged_unreadable"] for r in judged)

    lines = [f"# Narrative checklist scorecard — suite {suite}, combo {combo}", ""]
    lines += scorecard_meta(stamp, f"judges: {', '.join(judges)}",
                            "input: saved out/*/report.md + attribution.json (no pipeline calls)")
    lines += [
        "",
        "## Coverage",
        "",
        f"- cases in the {suite} suite: {len(rows)}",
        f"- cases judged: {len(judged)}",
        f"- cases not judged: {len(rows) - len(judged)}"
        + (f" ({'; '.join(sorted({r['status'] for r in rows if r.get('status') != 'judged'}))})"
           if len(rows) - len(judged) else ""),
        f"- checklist items judged: {items}",
        (
            f"- items flagged: {flagged} — {flagged_split} judge split (a human must read "
            f"the fact), {flagged_unreadable} unreadable or unreachable judge (repeat the run)"
        ),
        "",
        "## What a column means",
        "",
        (
            "A checklist item PASSES only when both judges rule it STATED by the "
            "report's own prose AND ENTAILED by the quotes the report cites. "
            "`stated, not entailed` is the ungrounded-narrative failure: the note "
            "asserts the reason but the cited source does not carry it. "
            "`not stated` means the note left the reason out. Flagged items count "
            "as neither a pass nor a fail."
        ),
        "",
        "| Case | Checklist pass | Rate | Stated, not entailed | Not stated | Flagged |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        if row.get("status") != "judged":
            note = f" ({row['note']})" if row.get("note") else ""
            lines.append(f"| {row['case']} | not judged: {row.get('status')}{note} | — | — | — | — |")
            continue
        rate = f"{row['accuracy_fraction']:.0%}" if row["accuracy_fraction"] is not None else "—"
        lines.append(
            f"| {row['case']} | {row['fact_accuracy']} | {rate} "
            f"| {row['stated_not_entailed']} | {row['not_stated']} | {row['flagged']} |"
        )
    rate = f"{passed / items:.0%}" if items else "n/a"
    lines.append(f"| **TOTAL** | **{passed}/{items}** | **{rate}** | "
                 f"**{sum(r['stated_not_entailed'] for r in judged)}** | "
                 f"**{sum(r['not_stated'] for r in judged)}** | **{flagged}** |")
    lines += [
        "",
        (
            "Descriptive for this run only: one run, one combo, no repeat sampling "
            "and no case-cluster bootstrap (finding 9). Do not quote the rate as a "
            "calibration claim."
        ),
        "",
        "## Judged items",
        "",
    ]
    for row in rows:
        if row.get("status") != "judged":
            continue
        lines.append(f"### {row['case']} ({row['fact_accuracy']})")
        for fact in row["facts"]:
            lines.append(f"- **{fact['verdict']}** — {fact['fact']}")
            lines.append(f"  - {fact['reason']}")
        lines.append("")
    lines.append(f"Judge spend: ${round(llm.usage.cost_usd, 4)} over {llm.usage.calls} calls.")
    return lines


def _movement_label(row: dict) -> str:
    if row["movement_ok"]:
        return "OK"
    detail = row.get("movement_detail", {})
    reasons = [name.removesuffix("_ok") for name in ("numbers_ok", "unit_ok", "basis_ok", "comparison_ok")
               if detail.get(name) is False]
    return f"WRONG ({', '.join(reasons)})" if reasons else "WRONG"


def scorecard_lines(title: str, rows: list[dict]) -> list[str]:
    cal = calibration(rows)
    lines = [f"# {title}", ""]
    lines.append("| Case | Movement | Driver recall | Precision | Extraction | Scored claims "
                 "| Unscored | Failed checks | Conf | Cost |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for row in rows:
        if "error" in row:
            lines.append(f"| {row['case']} | ERROR: {row['error'][:60]} | | | | | | | | |")
            continue
        coverage = row.get("coverage", {})
        scored = coverage.get("correct", 0) + coverage.get("incorrect", 0)
        lines.append(
            f"| {row['case']} | {_movement_label(row)} | {row['driver_recall']} "
            f"| {row['driver_precision']} | {row.get('extraction', '—')} "
            f"| {scored}/{coverage.get('quantified_claims', 0)} | {coverage.get('unscored', 0)} "
            f"| {row['failed_checks']} | {row['attribution_confidence']} | ${row.get('cost_usd', 0)} |"
        )
    lines += ["", "## Calibration (scored quantified driver claims only)", ""]
    lines += [
        (
            "Disclosure: confidently_wrong counts wrong claims at confidence 85+. "
            "The validation caps write 80 — one notch below that line — so a claim "
            "a cap touches is excluded from the metric by construction. The caps-off "
            "ablation (evals/results/audits/capsoff-*) measured the raw self-report "
            "rates; read this number alongside it, never alone."
        ),
        "",
    ]
    for key, value in cal.items():
        if key == "reliability":
            lines += [f"- {item}" for item in value]
        else:
            lines.append(f"- {key}: {value}")
    return lines


def _case_key(name: str) -> str:
    return name.replace(" ", "-").upper()


def _cell(row: dict, key: str) -> str:
    if "error" in row:
        return "ERROR"
    if key == "movement":
        return _movement_label(row)
    return str(row.get(key, "—"))


def delta_table_lines(old_rows: list[dict], new_rows: list[dict]) -> list[str]:
    """Per-case old-vs-new comparison. A drop where the old scorer was generous
    is the point of the exercise, never a regression to tune away."""
    old_by_case = {_case_key(r.get("case", "")): r for r in old_rows}
    lines = ["| Case | Movement | Driver recall | Precision | Extraction |", "|---|---|---|---|---|"]
    for row in new_rows:
        old = old_by_case.get(_case_key(row.get("case", "")))
        cells = []
        for key in ("movement", "driver_recall", "driver_precision", "extraction"):
            new_value = _cell(row, key)
            old_value = _cell(old, key) if old else "—"
            cells.append(new_value if old_value == new_value else f"{old_value} -> **{new_value}**")
        lines.append(f"| {row.get('case')} | " + " | ".join(cells) + " |")
    return lines


def rescore(
    suite: str = "dev",
    combo: str = "agentic",
    bank: str | None = None,
    since: str | None = None,
    until: str | None = None,
    baseline: str | None = None,
    label: str | None = None,
) -> Path:
    """Score saved out/<slug>/attribution.json artifacts again, with NO model
    calls: the scorer changes, the artifacts do not. `since` and `until` bound
    the artifact generation timestamps, so one run's artifacts are scored on
    their own even after a later run overwrites some of them. `baseline` is a
    previous run's .jsonl to compare against."""
    rows = []
    for gold in load_gold(suite, bank):
        out = artifact_dir(gold, combo)
        slug = out.name
        case = f"{gold['bank']}-{gold['metric']}-{gold['period']}"
        path = out / "attribution.json"
        if not path.exists():
            rows.append({"case": case, "metric": gold["metric"], "error": f"no artifact at out/{slug}"})
            continue
        attribution = Attribution.model_validate_json(path.read_text())
        generated = attribution.provenance.get("generated", "")
        if since and generated < since:
            rows.append({"case": case, "metric": gold["metric"],
                         "error": f"artifact predates {since} (generated {generated})"})
            continue
        if until and generated > until:
            rows.append({"case": case, "metric": gold["metric"],
                         "error": f"artifact postdates {until} (generated {generated}): "
                                  "a later run overwrote this artifact"})
            continue
        row = score_case(gold, attribution)
        row["artifact"] = f"out/{slug}"
        row["artifact_generated"] = generated
        rows.append(row)
        print(f"rescored {case}: movement={_movement_label(row)} recall={row['driver_recall']} "
              f"precision={row['driver_precision']} extraction={row.get('extraction', '—')}")

    stamp = run_stamp()
    stem = label or f"rescore-{stamp}-{combo}-{suite}"
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    (RESULTS_DIR / f"{stem}.jsonl").write_text("\n".join(json.dumps(r) for r in rows))

    lines = scorecard_lines(f"Rescore — suite {suite}, combo {combo}, saved artifacts, {stamp}", rows)
    lines += ["", "Scored offline from saved out/*/attribution.json artifacts. No model calls."]
    if baseline:
        old_rows = [json.loads(line) for line in Path(baseline).read_text().splitlines() if line.strip()]
        lines += ["", f"## Old vs new scorer (baseline {Path(baseline).name})", ""]
        lines += delta_table_lines(old_rows, rows)
    card_path = RESULTS_DIR / f"{stem}.md"
    card_path.write_text("\n".join(lines) + "\n")
    return card_path
