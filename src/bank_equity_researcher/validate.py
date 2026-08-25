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


def check_drivers_reconcile(attribution) -> tuple[list[str], list[str]]:
    """Quantified drivers + residual should sum to the movement delta."""
    passed, failed = [], []
    if attribution.movement is None:
        return passed, failed
    quantified = [d.contribution.value for d in attribution.drivers if d.contribution]
    if not quantified:
        return passed, ["no_quantified_drivers"]
    residual = attribution.residual.value if attribution.residual else 0.0
    total = sum(quantified) + residual
    if abs(total - attribution.movement.delta) <= 1.0:
        passed.append("drivers_reconcile")
    else:
        failed.append(
            f"drivers_reconcile (drivers {sum(quantified):+.1f} + residual {residual:+.1f} "
            f"!= delta {attribution.movement.delta:+.1f})"
        )
    return passed, failed
