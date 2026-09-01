"""The metric scorer's pure rules: the grader's own tolerances, the three claim
labels, the gold framings, and the driver and extraction scoring that turns one
attribution into labelled claims. Nothing here calls a model or reads a file.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..validation.schema import Attribution, DriverClaim
from ..validation.validate import cross_source_view, normalize_unit

# The GRADER'S OWN tolerances, deliberately not imported from the product's
# validation constants although the values agree today: a loosened product
# tolerance must show up as eval failures, and a grader that inherits the
# loosening cannot see it.
SCORER_MONEY_ABS_TOL_M = 10.0
SCORER_MONEY_REL_TOL = 0.01
SCORER_RATIO_TOL_PPT = 0.1
SCORER_BPS_TOL = 0.5

# The three claim labels. "unscored" is not a soft "incorrect": it
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


# ---------------------------------------------------------------------------
# One typed tolerance, applied here to every comparison. The SCORER_*
# constants above are the grader's own — see their block for why they are
# deliberately not shared with validate.py.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Tolerance:
    """A match tolerance: max(absolute, relative x |target|)."""

    absolute: float
    relative: float = 0.0

    def for_target(self, target: float) -> float:
        return max(self.absolute, self.relative * abs(float(target)))


def tolerance_for(unit: str | None) -> Tolerance:
    canonical = normalize_unit(unit)
    if canonical == "$m":
        # Banks round to $m; 1% or $10m (whichever is larger) absorbs
        # re-presented comparatives without letting real errors through.
        return Tolerance(SCORER_MONEY_ABS_TOL_M, SCORER_MONEY_REL_TOL)
    if canonical in ("ppt", "%"):
        return Tolerance(SCORER_RATIO_TOL_PPT)
    return Tolerance(SCORER_BPS_TOL)


def values_match(value: float, target: float, unit: str | None) -> bool:
    """A sign flip is never a rounding difference, so it never matches.

    The sign rule carries the cases where the target is smaller than its own
    tolerance, which the $10m money floor makes common: CBA 1H26 impairment
    moved -1 $m, and the distance check alone graded an answer of +9 $m a
    match, so a charge that fell was credited to an answer that said it rose.
    """
    tol = tolerance_for(unit).for_target(target)
    if value * target < 0:
        return False
    return abs(value - target) <= tol


# ---------------------------------------------------------------------------
# Gold framings
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


def _gold_number(value) -> float | None:
    """A gold value must BE a number — a string in gold is an authoring
    error, never coerced (the agent-side _numeric parses strings; this one
    deliberately does not: opposite contracts, different names)."""
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
        return _gold_number(entry.get("value"))
    return _gold_number(entry)


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
# Driver scoring
# ---------------------------------------------------------------------------


def _score_one_framing(framing: Framing, claims: list[DriverClaim], unit: str,
                       known_canonicals: frozenset | None) -> dict:
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

        # The gold states its values in ONE unit. A claim in another unit is a
        # claim about something else, so it is wrong, not right: without this
        # check a "+3 bps" contribution matched a "+3 $m" gold slot by
        # tolerance alone.
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
            if known_canonicals is not None and canonical not in known_canonicals:
                label(entry, UNSCORED,
                      f"{canonical} is not a taxonomy driver; an invented child "
                      "cannot fill a parent slot")
            else:
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


def score_drivers(framings: list[Framing], claims: list[DriverClaim], unit: str,
                  known_canonicals: frozenset | None = None) -> dict:
    """Score the quantified claims one-to-one against ONE eligible framing.

    An alternate framing is taken as a whole or not at all: precision and recall
    always come from the same framing, so a mixture of decompositions cannot
    collect credit no published source supports.

    `known_canonicals` is the metric's taxonomy vocabulary: a dotted child
    OUTSIDE it cannot fill a parent slot (two invented rwa.* children summing
    to the parent scored 2/2 at confidence 99, executed repro).
    """
    quantified = [c for c in claims if c.contribution is not None]
    scored = [_score_one_framing(f, quantified, unit, known_canonicals) for f in framings]
    ranked = sorted(
        enumerate(scored),
        key=lambda pair: (
            # The FRACTION ranks first: a complete alternate (2/2) must beat
            # a fuller-but-incomplete primary (2/3); the raw matched count
            # alone handed the primary the tie (executed repro).
            pair[1]["recall_matched"] / max(1, pair[1]["recall_total"]),
            pair[1]["recall_matched"],
            pair[1]["correct"],
            -pair[1]["incorrect"],
            -pair[0],  # ties go to the primary framing
        ),
        reverse=True,
    )
    return ranked[0][1]


# ---------------------------------------------------------------------------
# Extraction scoring
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
    """Bar labels mapped to canonical ids with the registry's verbatim label map."""
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
