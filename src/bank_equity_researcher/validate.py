"""Deterministic validation checks and their tolerances (tickets 01, 05).

Every constant carries the reason it has that value.
"""

from __future__ import annotations

# Profit Announcement walks label bars to two decimals of a percent (0.01% =
# 1bp), so extraction should be exact; +-0.5bp absorbs float noise only.
WALK_BAR_TOL_PA = 0.5
# PA walk bars are exact, so their sum should reconcile within rounding of the
# endpoints (each endpoint rounded to 1bp): 1bp.
WALK_SUM_TOL_PA = 1.0
# Presentation walks round endpoints coarsely (CET1 slides round to 0.1% =
# 10bps; CBA FY26 slide 32 bars sum to -24 vs a -30 headline and the slide
# footnotes the rounding). Tolerance = one endpoint rounding step.
WALK_SUM_TOL_PRESENTATION = 10.0
# Money figures: banks round to $m; 1% or $10m (whichever larger) absorbs
# re-presented comparatives without letting real errors through.
MONEY_REL_TOL = 0.01
MONEY_ABS_TOL_M = 10.0
# Ratio metrics quoted to one decimal of a percent.
RATIO_TOL_PPT = 0.1
# Two documents quoting the same driver agree if within this (covers 1bp
# rounding on each side, e.g. PA "Liquids -3" vs slide "Liquids & repos (4)"
# is a framing gap, not agreement). Beyond it, the gap is surfaced as a
# disagreement, never averaged away.
CORROBORATION_TOL = 1.5


def walk_sum_tolerance(doc_type: str) -> float:
    if doc_type in ("results_presentation", "investor_discussion_pack", "investor_presentation"):
        return WALK_SUM_TOL_PRESENTATION
    return WALK_SUM_TOL_PA


def check_walk(walk: dict, doc_type: str) -> tuple[list[str], list[str]]:
    """walk: {start_bps, bars: [{label, bps}], end_bps}. Returns (passed, failed)."""
    passed, failed = [], []
    total = walk["start_bps"] + sum(b["bps"] for b in walk["bars"])
    if abs(total - walk["end_bps"]) <= walk_sum_tolerance(doc_type):
        passed.append("walk_sum")
    else:
        failed.append(
            f"walk_sum (start {walk['start_bps']} + bars {sum(b['bps'] for b in walk['bars']):+.1f} "
            f"= {total:.1f} != end {walk['end_bps']}, tol {walk_sum_tolerance(doc_type)})"
        )
    return passed, failed


def check_movement(movement) -> tuple[list[str], list[str]]:
    passed, failed = [], []
    if movement is None:
        return passed, ["movement_missing"]
    if abs(movement.from_value + movement.delta - movement.to_value) <= 0.51:
        passed.append("movement_arithmetic")
    else:
        failed.append(
            f"movement_arithmetic ({movement.from_value} + {movement.delta} != {movement.to_value})"
        )
    return passed, failed


def _normalize_label(label: str) -> str:
    return "".join(ch for ch in label.lower() if ch.isalnum())


def cross_source_view(walks: list[dict], label_map: dict[str, str]) -> dict[str, list[dict]]:
    """canonical driver -> [{source, label, value}] across all extracted walks.
    Labels map to canonical ids via the registry's verbatim label map."""
    normalized_map = {_normalize_label(k): v for k, v in label_map.items()}
    view: dict[str, list[dict]] = {}
    for walk in walks:
        for bar in walk.get("bars", []):
            norm = _normalize_label(str(bar.get("label", "")))
            canonical = normalized_map.get(norm)
            if canonical is None:  # fallback: containment either way
                canonical = next(
                    (c for k, c in normalized_map.items() if k and (k in norm or norm in k)),
                    "other_unmapped",
                )
            view.setdefault(canonical, []).append(
                {"source": walk.get("source", "?"), "label": bar.get("label"), "value": float(bar.get("bps", 0))}
            )
    return view


def corroborate(attribution, cross_source: dict[str, list[dict]]) -> None:
    """Annotate each quantified driver with its corroboration status; surface
    cross-source divergence as a disagreement; cap single-source confidence.
    Mutates the attribution in place."""
    from .schema import Disagreement, DisagreementReason

    for driver in attribution.drivers:
        if driver.contribution is None:
            continue
        entries = cross_source.get(driver.canonical, [])
        cited_docs = {
            r.doc_id for r in attribution.evidence_records if r.id in driver.evidence
        }
        walk_docs = {e["source"].split(" PDF")[0] for e in entries}
        n_sources = len(cited_docs | walk_docs)
        if len(entries) >= 2 and len(walk_docs) >= 2:
            values = [e["value"] for e in entries]
            if max(values) - min(values) <= CORROBORATION_TOL:
                driver.checks_passed.append(f"corroborated_{len(walk_docs)}_sources")
            else:
                driver.checks_passed.append("cross_source_divergence_surfaced")
                gap = max(values) - min(values)
                attribution.disagreements.append(
                    Disagreement(
                        topic=f"{driver.canonical} contribution",
                        values=[f"{e['value']:+g} — {e['label']} ({e['source']})" for e in entries],
                        preferred=f"{driver.contribution.value:+g} (per the source hierarchy)",
                        reason=DisagreementReason.rounding if gap <= 3 else DisagreementReason.definitional,
                        explanation="The documents decompose the same movement with different bar framings; "
                        "the gap is framing/rounding, not a data conflict."
                        if gap <= 3
                        else "The documents use different decompositions of the same movement.",
                    )
                )
        elif n_sources <= 1:
            # Corroboration dimension (user, 2026-08-26): a quantified claim
            # seen in only one document cannot claim near-certainty.
            driver.checks_passed.append("single_source")
            driver.confidence = min(driver.confidence, 85)


def check_drivers_reconcile(attribution) -> tuple[list[str], list[str]]:
    """Quantified drivers + residual should sum to the movement delta.
    Tolerance follows the evidence: drivers sourced from a presentation walk
    inherit its endpoint-rounding slack (the CBA CET1 slide case)."""
    passed, failed = [], []
    if attribution.movement is None:
        return passed, failed
    quantified = [d.contribution.value for d in attribution.drivers if d.contribution]
    if not quantified:
        return passed, ["no_quantified_drivers"]
    presentation_walk = any(
        r.kind == "walk_vision" and ("presentation" in r.doc_id or "discussion" in r.doc_id)
        for r in attribution.evidence_records
    )
    tolerance = WALK_SUM_TOL_PRESENTATION if presentation_walk else 1.0
    residual = attribution.residual.value if attribution.residual else 0.0
    total = sum(quantified) + residual
    if abs(total - attribution.movement.delta) <= tolerance:
        passed.append("drivers_reconcile")
    else:
        failed.append(
            f"drivers_reconcile (drivers {sum(quantified):+.1f} + residual {residual:+.1f} "
            f"!= delta {attribution.movement.delta:+.1f}, tol {tolerance})"
        )
    return passed, failed
