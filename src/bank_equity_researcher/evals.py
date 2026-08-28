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

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .config import OUT_DIR, REGISTRY_DIR, REPO_ROOT
from .schema import Attribution, DriverClaim
from .validate import (
    MONEY_ABS_TOL_M,
    MONEY_REL_TOL,
    RATIO_TOL_PPT,
    WALK_BAR_TOL_PA,
    cross_source_view,
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


def score_crossref(gold_case: dict, ask_output: dict) -> dict:
    """Location coverage: the fraction of gold required_locations whose
    (doc substring, pdf_page) appears among the evidence records cited by
    the answer's key_facts."""
    cited_ids = {e for fact in ask_output.get("key_facts", []) for e in fact.get("evidence", [])}
    cited = [r for r in ask_output.get("evidence_records", []) if r["id"] in cited_ids]

    locations = []
    hits = 0
    for loc in gold_case.get("required_locations", []):
        hit_ids = [r["id"] for r in cited
                   if loc["doc"] in r["doc_id"] and r["pdf_page"] == loc["pdf_page"]]
        hits += bool(hit_ids)
        locations.append({"doc": loc["doc"], "pdf_page": loc["pdf_page"],
                          "holds": loc.get("holds", ""), "hit": bool(hit_ids),
                          "cited_by": hit_ids})
    total = len(locations)
    return {
        "case": gold_case["id"],
        "location_coverage": f"{hits}/{total}",
        "coverage_fraction": round(hits / total, 3) if total else None,
        "locations": locations,
        "cited_evidence_ids": sorted(cited_ids),
        "confidence": ask_output.get("confidence"),
        "limitations": len(ask_output.get("limitations", [])),
        # Stub for judge-based fact checking (not yet implemented): the gold
        # facts a judge must verify against the answer text.
        "fact_check": {
            "status": "not_implemented",
            "gold_answer_facts": gold_case.get("gold_answer_facts", []),
            "answer": ask_output.get("answer", ""),
        },
        "cost_usd": ask_output.get("provenance", {}).get("cost_usd"),
        "seconds": ask_output.get("provenance", {}).get("seconds"),
    }


def run_crossref_suite(combo: str, bank: str | None = None) -> Path:
    """Run every crossref HOLDOUT case through ask and report location
    coverage. Discipline: run at most once per milestone; never iterate on it."""
    from .ask import run_ask

    rows = []
    for gold in load_crossref_gold(bank):
        label = f"{gold['bank']} {gold['id']}"
        try:
            output, _ = run_ask(
                gold["bank"], [gold["period"], gold["comparator"]], gold["question"], combo
            )
            row = score_crossref(gold, output)
        except Exception as exc:  # noqa: BLE001 - a crashed case is a scored failure
            row = {"case": label, "error": str(exc)[:300]}
        print(f"scored {label}: {json.dumps({k: v for k, v in row.items() if k not in ('locations', 'fact_check')})[:250]}")
        rows.append(row)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RESULTS_DIR / f"{stamp}-{combo}-crossref.jsonl"
    raw_path.write_text("\n".join(json.dumps(r) for r in rows))

    lines = [f"# Crossref scorecard — combo {combo}, {stamp}", ""]
    lines.append("| Case | Location coverage | Missed locations | Conf | Cost |")
    lines.append("|---|---|---|---|---|")
    for r in rows:
        if "error" in r:
            lines.append(f"| {r['case']} | ERROR: {r['error'][:80]} | | | |")
            continue
        missed = "; ".join(
            f"{loc['doc']} p{loc['pdf_page']}" for loc in r["locations"] if not loc["hit"]
        ) or "—"
        lines.append(
            f"| {r['case']} | {r['location_coverage']} | {missed} "
            f"| {r['confidence']} | ${r.get('cost_usd', 0)} |"
        )
    lines += ["", "Judge-based fact checking against gold_answer_facts: not implemented",
              "(the gold facts are recorded per case in the .jsonl for a later judge)."]
    card_path = RESULTS_DIR / f"{stamp}-{combo}-crossref.md"
    card_path.write_text("\n".join(lines) + "\n")
    return card_path


# ---------------------------------------------------------------------------
# One typed tolerance (finding 6). The constants live in validate.py with the
# reason they have their value; this is the single place that applies them to
# a comparison, so the harness and the deterministic checks cannot disagree.
# ---------------------------------------------------------------------------

UNIT_ALIASES = {
    "bps": "bps", "bp": "bps", "bpt": "bps", "bpts": "bps", "basis": "bps",
    "$m": "$m", "$": "$m", "m": "$m", "$millions": "$m", "aud$m": "$m",
    "ppt": "ppt", "ppts": "ppt", "pp": "ppt",
    "%": "%", "pct": "%", "percent": "%",
}


@dataclass(frozen=True)
class Tolerance:
    """A unit-typed match tolerance: max(absolute, relative x |target|)."""

    unit: str
    absolute: float
    relative: float = 0.0

    def for_target(self, target: float) -> float:
        return max(self.absolute, self.relative * abs(float(target)))


def normalize_unit(unit: str | None) -> str:
    """'bps of average GLAA' -> 'bps'; '$ m' -> '$m'; None -> ''."""
    if not unit:
        return ""
    token = str(unit).strip().lower().split(" ")[0]
    return UNIT_ALIASES.get(token, token)


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
    """A sign flip is never a rounding difference, so it never matches."""
    tol = tolerance_for(unit).for_target(target)
    if abs(target) > tol and value * target < 0:
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


def run_suite(suite: str, combo: str, bank: str | None = None) -> Path:
    from .pipeline import run_case

    gold_cases = load_gold(suite, bank)
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

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
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
    combo: str = "cheap",
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
        slug = f"{gold['bank']}-{gold['metric']}-{gold['period']}-vs-{gold['comparator']}-{combo}".lower()
        case = f"{gold['bank']}-{gold['metric']}-{gold['period']}"
        path = OUT_DIR / slug / "attribution.json"
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

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
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
