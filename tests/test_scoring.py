"""Scorer regression tests (ticket 28, Codex finding 13).

Every case names the counterexample it prevents:

- WRONG-SCORES-RIGHT: the old scorer gave credit to a materially wrong answer.
- RIGHT-SCORES-WRONG: the old scorer punished a defensible answer.

The tables are the specification. A change that makes a table row fail is a
change to what "correct" means — argue it in the ticket, never tune it here.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.evals import (
    CORRECT,
    INCORRECT,
    UNSCORED,
    calibration,
    gold_framings,
    normalize_unit,
    score_case,
    score_drivers,
    score_extraction,
    tolerance_for,
    values_match,
)
from bank_equity_researcher.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    EvidenceRecord,
    Movement,
    NumberFact,
)

# --------------------------------------------------------------------------
# builders
# --------------------------------------------------------------------------


def claim(canonical: str, value: float | None, confidence: int = 90, unit: str = "bps") -> DriverClaim:
    return DriverClaim(
        canonical=canonical,
        contribution=None if value is None else Contribution(value=value, unit=unit),
        confidence=confidence,
        evidence=["ev-1"],
    )


def walk_record(
    record_id: str,
    bars: dict[str, float],
    start: float,
    end: float,
    doc_id: str = "CBA/FY26/profit_announcement",
    page: int = 28,
    title: str = "NIM Movement",
) -> EvidenceRecord:
    """Mirrors the quote format extract.extract_walk stamps on walk records."""
    return EvidenceRecord(
        id=record_id,
        doc_id=doc_id,
        pdf_page=page,
        kind="walk_vision",
        quote=f"[walk chart] {title}: Start {start} -> End {end}",
        numbers=[NumberFact(label=label, value=value, unit="bps") for label, value in bars.items()],
    )


def attribution(
    drivers: list[DriverClaim] | None = None,
    movement: tuple[float, float, float, str] | None = (208, 205, -3, "bps"),
    basis: str = "cash",
    records: list[EvidenceRecord] | None = None,
    metric: str = "nim",
    period: str = "FY26",
    comparator: str = "FY25",
    confidence: int = 90,
) -> Attribution:
    return Attribution(
        bank="CBA",
        metric=metric,
        period=period,
        comparator=comparator,
        basis=basis,
        movement=None if movement is None else Movement(
            from_value=movement[0], to_value=movement[1], delta=movement[2], unit=movement[3]
        ),
        drivers=drivers or [],
        attribution_confidence=confidence,
        evidence_records=records or [],
    )


# A gold movement is stated in its metric's own unit. The default used to be
# "bps" whatever the metric, so a cash_earnings fixture carried $m claims
# against a bps movement — an inconsistency the scorer could not see until it
# started reading the claim's unit.
_METRIC_UNITS = {
    "nim": "bps", "cet1": "bps",
    "cash_earnings": "$m", "impairment": "$m",
    "roe": "ppt", "cti": "ppt",
}


def gold_case(
    gold_drivers: dict,
    metric: str = "nim",
    movement: dict | None = None,
    alt_framings: list[dict] | None = None,
    basis: str = "cash",
    period: str = "FY26",
    comparator: str = "FY25",
) -> dict:
    case = {
        "bank": "CBA",
        "metric": metric,
        "period": period,
        "comparator": comparator,
        "basis": basis,
        "movement": movement
        or {"from": 208, "to": 205, "delta": -3, "unit": _METRIC_UNITS.get(metric, "bps")},
        "gold_drivers": gold_drivers,
    }
    if alt_framings:
        case["alt_framings"] = alt_framings
    return case


WALK_GOLD = {"tier": "walk", "drivers": {"liquids": -3, "asset_pricing": -5}}
NIM_LABELS = {
    "Liquids": "liquids",
    "Asset pricing": "asset_pricing",
    "Funding costs": "funding",
    "Portfolio mix": "mix",
    "Basis risk": "basis_risk",
    "Treasury & Markets": "markets_treasury",
}


# --------------------------------------------------------------------------
# 1. typed tolerance (finding 6)
# --------------------------------------------------------------------------

TOLERANCE_TABLE = [
    # (name, unit, target, value, matches)
    ("bps_exact", "bps", -3.0, -3.0, True),
    ("bps_one_bar_off", "bps", -3.0, -4.0, False),
    ("ppt_within_a_tenth", "ppt", 0.5, 0.55, True),
    ("ppt_beyond_a_tenth", "ppt", 0.5, 0.7, False),
    # $m tolerance is max(1%, $10m) — the documented money rule, not a flat $10m.
    ("money_relative_arm_passes", "$m", 10252.0, 10330.0, True),
    ("money_relative_arm_fails", "$m", 10252.0, 10500.0, False),
    ("money_absolute_arm_passes", "$m", 62.0, 71.0, True),
    ("money_absolute_arm_fails", "$m", 62.0, 80.0, False),
    # A sign flip is never a rounding difference.
    ("sign_flip_never_matches", "$m", 1964.0, -1964.0, False),
    # ...including the small values the absolute arm used to swallow whole. The
    # sign rule was gated on `abs(target) > tol`, which only fires where the
    # distance check already fails, so the rule was dead code. Two live dev
    # gold targets sit in the hole: CBA 1H26 cash_earnings
    # credit_impairment_charge (+1 $m) and CBA 1H26 impairment movement delta
    # (-1 $m). A charge that FELL by 1 scored correct against a claim it ROSE
    # by 9.
    ("sign_flip_inside_the_money_floor", "$m", 5.0, -5.0, False),
    ("sign_flip_gold_plus_one", "$m", 1.0, -9.0, False),
    ("sign_flip_inside_the_bps_floor", "bps", 0.3, -0.2, False),
    ("sign_flip_inside_the_ppt_floor", "ppt", 0.05, -0.05, False),
    # A zero endpoint has no sign to flip, so the distance rule still decides.
    ("zero_target_still_matches_by_distance", "$m", 0.0, -5.0, True),
    ("zero_value_still_matches_by_distance", "$m", -5.0, 0.0, True),
]


@pytest.mark.parametrize("name,unit,target,value,expected", TOLERANCE_TABLE, ids=[r[0] for r in TOLERANCE_TABLE])
def test_typed_tolerance(name, unit, target, value, expected):
    assert values_match(value, target, unit) is expected


def test_money_tolerance_is_max_of_relative_and_absolute():
    tol = tolerance_for("$m")
    assert tol.for_target(100.0) == 10.0  # absolute arm
    assert tol.for_target(10000.0) == 100.0  # relative arm


@pytest.mark.parametrize(
    "raw,expected",
    [("bps", "bps"), ("bpts", "bps"), ("bps of average GLAA", "bps"), ("$m", "$m"),
     ("$ m", "$m"), ("ppt", "ppt"), ("%", "%"), (None, "")],
)
def test_normalize_unit(raw, expected):
    assert normalize_unit(raw) == expected


# --------------------------------------------------------------------------
# 2. driver scoring: framings, uniqueness, parent/child, three-state labels
# --------------------------------------------------------------------------

DRIVER_TABLE = [
    (
        "clean_primary_framing",
        "baseline: a correct answer scores full marks",
        gold_case(WALK_GOLD),
        [claim("liquids", -3), claim("asset_pricing", -5)],
        {"labels": [CORRECT, CORRECT], "precision": "2/2", "recall": "2/2", "framing": "primary"},
    ),
    (
        "duplicate_claim_counted_once",
        "WRONG-SCORES-RIGHT: the old scorer scored both copies right (2/2)",
        gold_case(WALK_GOLD),
        [claim("liquids", -3), claim("liquids", -3), claim("asset_pricing", -5)],
        {"labels": [CORRECT, INCORRECT, CORRECT], "precision": "2/3", "recall": "2/2",
         "duplicate_canonicals": 1},
    ),
    (
        "hybrid_framing_rejected",
        ("WRONG-SCORES-RIGHT: one value from the PA walk plus one from the slide walk "
         "used to score 2/2 against a decomposition no document publishes"),
        gold_case(
            {"tier": "walk", "drivers": {"liquids": -3, "markets_treasury": -2}},
            alt_framings=[{"source": "slide 60", "drivers": {"liquids": -4, "markets_treasury": -1}}],
        ),
        [claim("liquids", -3), claim("markets_treasury", -1)],
        {"labels": [CORRECT, INCORRECT], "precision": "1/2", "recall": "1/2", "framing": "primary"},
    ),
    (
        "alt_framing_scored_as_a_whole",
        ("RIGHT-SCORES-WRONG: a completely correct alternate framing used to lose recall "
         "because recall was always measured against the primary framing"),
        gold_case(
            {"tier": "walk", "drivers": {"liquids": -3, "markets_treasury": -2}},
            alt_framings=[{"source": "slide 60", "drivers": {"liquids": -4, "markets_treasury": -1}}],
        ),
        [claim("liquids", -4), claim("markets_treasury", -1)],
        {"labels": [CORRECT, CORRECT], "precision": "2/2", "recall": "2/2", "framing": "alt:slide 60"},
    ),
    (
        "child_claim_satisfies_parent_slot",
        ("RIGHT-SCORES-WRONG: funding.deposits -3 against a funding -3 parent slot "
         "was marked wrong by exact-string matching"),
        gold_case({"tier": "walk", "drivers": {"funding": -3}}),
        [claim("funding.deposits", -3)],
        {"labels": [CORRECT], "precision": "1/1", "recall": "1/1"},
    ),
    (
        "children_summing_to_parent_slot",
        "children may jointly satisfy one parent slot",
        gold_case({"tier": "walk", "drivers": {"rwa": -46}}),
        [claim("rwa.credit", -38), claim("rwa.irrbb", -16), claim("rwa.market", 8)],
        {"labels": [CORRECT, CORRECT, CORRECT], "precision": "3/3", "recall": "1/1"},
    ),
    (
        "children_not_summing_to_parent_slot",
        "WRONG-SCORES-RIGHT: an incomplete child set must not satisfy the parent slot",
        gold_case({"tier": "walk", "drivers": {"rwa": -46}}),
        [claim("rwa.credit", -20), claim("rwa.market", 5)],
        {"labels": [INCORRECT, INCORRECT], "precision": "0/2", "recall": "0/1"},
    ),
    (
        "known_child_value_is_scored_on_its_own_value",
        ("WRONG-SCORES-RIGHT: labelling the whole -46 RWA bar as credit RWA scored right "
         "because the child summed to the parent (gold says credit RWA is -38)"),
        gold_case(
            {"tier": "walk", "drivers": {"rwa": -46},
             "rwa_children": {"rwa.credit": -38, "rwa.irrbb": -16, "rwa.market": 8, "rwa.operational": 0}}
        ),
        [claim("rwa.credit", -46)],
        {"labels": [INCORRECT], "precision": "0/1", "recall": "0/1"},
    ),
    (
        "parent_claim_does_not_satisfy_child_slots",
        ("WRONG-SCORES-RIGHT: a parent claim satisfies a parent slot only; it must not "
         "collect two child slots it never decomposed"),
        gold_case({"tier": "walk", "drivers": {"funding.deposits": -1, "funding.wholesale": -2}}),
        [claim("funding", -3)],
        {"labels": [INCORRECT], "precision": "0/1", "recall": "0/2"},
    ),
    (
        "unscored_gold_slot_excludes_the_claim",
        "RIGHT-SCORES-WRONG: FY21 nii is 'not probed', yet the claim was counted false",
        gold_case(
            {"tier": "components",
             "drivers": {"credit_impairment_charge": {"value": 1964},
                         "nii": {"value": None, "provenance": "income split not probed"}}},
            metric="cash_earnings",
        ),
        [claim("credit_impairment_charge", 1964, unit="$m"), claim("nii", 229, unit="$m")],
        {"labels": [CORRECT, UNSCORED], "precision": "1/1", "recall": "1/1", "unscored_gold_slots": 1},
    ),
    (
        "claim_outside_non_exhaustive_gold_is_unscored",
        ("RIGHT-SCORES-WRONG: components gold is explicitly not force-fitted, so a claim "
         "it never covers (tax) is unknown, not wrong"),
        gold_case(
            {"tier": "components", "drivers": {"credit_impairment_charge": {"value": 1964}}},
            metric="cash_earnings",
        ),
        [claim("credit_impairment_charge", 1964, unit="$m"), claim("tax_and_other", -568, unit="$m")],
        {"labels": [CORRECT, UNSCORED], "precision": "1/1", "recall": "1/1"},
    ),
    (
        "claim_outside_walk_gold_is_incorrect",
        "WRONG-SCORES-RIGHT: a published walk is exhaustive, so an invented bar is wrong",
        gold_case(WALK_GOLD),
        [claim("liquids", -3), claim("asset_pricing", -5), claim("basis_risk", 4)],
        {"labels": [CORRECT, CORRECT, INCORRECT], "precision": "2/3", "recall": "2/2"},
    ),
    (
        "wrong_value_on_a_scored_slot_is_incorrect",
        "the verified case: gold knows the value, the answer disagrees",
        gold_case(WALK_GOLD),
        [claim("liquids", 3)],
        {"labels": [INCORRECT], "precision": "0/1", "recall": "0/2"},
    ),
    (
        "bucket_canonical_is_never_scored",
        ("other_unmapped is a catch-all bucket, not an economic concept: it can repeat "
         "and it satisfies no slot"),
        gold_case(
            {"tier": "components", "drivers": {"credit_impairment_charge": {"value": 1964}}},
            metric="impairment",
        ),
        [claim("other_unmapped", 11, unit="$m"), claim("other_unmapped", 6, unit="$m")],
        {"labels": [UNSCORED, UNSCORED], "precision": "0/0", "duplicate_canonicals": 0},
    ),
]


@pytest.mark.parametrize(
    "name,why,gold,claims,expected", DRIVER_TABLE, ids=[row[0] for row in DRIVER_TABLE]
)
def test_driver_scoring(name, why, gold, claims, expected):
    unit = gold["movement"]["unit"]
    result = score_drivers(gold_framings(gold), claims, unit)
    assert [c["label"] for c in result["claims"]] == expected["labels"], why
    for key, value in expected.items():
        if key == "labels":
            continue
        assert result[key] == value, f"{why} ({key})"


def test_unquantified_claims_are_not_scored():
    """A narrative driver with no contribution is not a quantified claim."""
    result = score_drivers(gold_framings(gold_case(WALK_GOLD)), [claim("liquids", None)], "bps")
    assert result["claims"] == []
    assert result["precision"] == "0/0"


# --------------------------------------------------------------------------
# 3. movement scoring: unit, basis, comparator (finding 6)
# --------------------------------------------------------------------------

MOVEMENT_TABLE = [
    (
        "exact_movement",
        "baseline: the right numbers, unit, basis and comparator",
        attribution(),
        {"movement_ok": True},
    ),
    (
        "wrong_unit_scores_wrong",
        "WRONG-SCORES-RIGHT: 2.05% is not 205 bps; the old scorer read the unit off gold",
        attribution(movement=(2.08, 2.05, -0.03, "%")),
        {"movement_ok": False, "unit_ok": False},
    ),
    (
        "wrong_basis_scores_wrong",
        "WRONG-SCORES-RIGHT: a statutory-basis answer to a cash-basis case",
        attribution(basis="statutory"),
        {"movement_ok": False, "basis_ok": False, "numbers_ok": True},
    ),
    (
        "wrong_comparator_scores_wrong",
        "WRONG-SCORES-RIGHT: the right numbers against the wrong comparator",
        attribution(comparator="1H25"),
        {"movement_ok": False, "comparison_ok": False},
    ),
    (
        "missing_movement_scores_wrong",
        "an absent movement is a failure, not an abstention",
        attribution(movement=None),
        {"movement_ok": False},
    ),
]


@pytest.mark.parametrize(
    "name,why,attr,expected",
    [(r[0], r[1] if len(r) == 4 else r[0], r[-2], r[-1]) for r in MOVEMENT_TABLE],
    ids=[r[0] for r in MOVEMENT_TABLE],
)
def test_movement_scoring(name, why, attr, expected):
    row = score_case(gold_case(WALK_GOLD), attr, label_map=NIM_LABELS)
    for key, value in expected.items():
        got = row["movement_ok"] if key == "movement_ok" else row["movement_detail"][key]
        assert got is value, f"{why} ({key})"


def test_cet1_basis_is_not_applicable():
    """RIGHT-SCORES-WRONG: the CET1 ratio has no cash/statutory basis, so a basis
    label must not fail an otherwise correct capital movement."""
    gold = gold_case({"tier": "walk", "drivers": {"rwa": -46}}, metric="cet1",
                     movement={"from": 1230, "to": 1200, "delta": -30, "unit": "bps"})
    row = score_case(gold, attribution(movement=(1230, 1200, -30, "bps"), basis="statutory",
                                       metric="cet1"), label_map={})
    assert row["movement_detail"]["basis_ok"] is None
    assert row["movement_ok"] is True


def test_money_movement_uses_the_shared_tolerance():
    """The documented money rule is max(1%, $10m); a flat $10m failed re-presented
    comparatives, and validate.py's 0.51 was unit-blind."""
    gold = gold_case({"tier": "components", "drivers": {}}, metric="cash_earnings",
                     movement={"from": 10252, "to": 10982, "delta": 730, "unit": "$m"})
    inside = score_case(gold, attribution(movement=(10330, 11050, 720, "$m"), metric="cash_earnings"))
    outside = score_case(gold, attribution(movement=(10252, 10982, 700, "$m"), metric="cash_earnings"))
    assert inside["movement_ok"] is True
    assert outside["movement_ok"] is False


# --------------------------------------------------------------------------
# 4. extraction: one-to-one by label, value and comparison (finding 5)
# --------------------------------------------------------------------------

FULL_WALK_GOLD = {
    "tier": "walk",
    "drivers": {"liquids": -3, "asset_pricing": -5, "funding": 0, "mix": 2, "basis_risk": 0},
}

EXTRACTION_TABLE = [
    (
        "labels_and_values_match",
        "baseline: the gold walk read correctly",
        FULL_WALK_GOLD,
        [walk_record("ev-1", {"Liquids": -3, "Asset pricing": -5, "Funding costs": 0,
                              "Portfolio mix": 2, "Basis risk": 0}, 208, 205)],
        {"extraction": "5/5"},
    ),
    (
        "one_extracted_zero_cannot_satisfy_two_gold_zeros",
        "WRONG-SCORES-RIGHT: the old scorer let one extracted 0 satisfy every 0 bar",
        FULL_WALK_GOLD,
        [walk_record("ev-1", {"Liquids": -3, "Asset pricing": -5, "Funding costs": 0}, 208, 205)],
        {"extraction": "3/5"},
    ),
    (
        "permuted_labels_score_wrong",
        ("WRONG-SCORES-RIGHT: every gold value is present, but on the wrong bar; "
         "the old value-only scorer read that as 5/5"),
        FULL_WALK_GOLD,
        [walk_record("ev-1", {"Liquids": -5, "Asset pricing": -3, "Funding costs": 2,
                              "Portfolio mix": 0, "Basis risk": 0}, 208, 205)],
        {"extraction": "1/5"},
    ),
    (
        "walk_for_another_comparison_is_ineligible",
        "WRONG-SCORES-RIGHT: the FY25 case scored 4/7 off the half-on-half walk",
        FULL_WALK_GOLD,
        [walk_record("ev-1", {"Liquids": -3, "Asset pricing": -5, "Funding costs": 0,
                              "Portfolio mix": 2, "Basis risk": 0}, 208, 208)],
        {"extraction": "0/5"},
    ),
    (
        "bars_from_two_walks_do_not_combine",
        "WRONG-SCORES-RIGHT: numbers were pooled across every walk record",
        FULL_WALK_GOLD,
        [
            walk_record("ev-1", {"Liquids": -3, "Asset pricing": -5}, 208, 205),
            walk_record("ev-2", {"Funding costs": 0, "Portfolio mix": 2, "Basis risk": 0}, 208, 205,
                        page=60),
        ],
        {"extraction": "3/5"},
    ),
]


@pytest.mark.parametrize(
    "name,why,gold_drivers,records,expected", EXTRACTION_TABLE, ids=[r[0] for r in EXTRACTION_TABLE]
)
def test_extraction_scoring(name, why, gold_drivers, records, expected):
    gold = gold_case(gold_drivers)
    result = score_extraction(gold, attribution(records=records), "bps", NIM_LABELS)
    assert result["extraction"] == expected["extraction"], why


def test_extraction_not_scored_when_gold_walk_is_another_comparison():
    """WRONG-SCORES-RIGHT: the FY26 CET1 case reported 4/4 extraction from a
    half-on-half walk while driver scoring said that walk is not FY-on-FY."""
    gold = gold_case(
        {"tier": "walk", "comparison": "2H26 vs 1H26, not FY-on-FY",
         "drivers": {"rwa": -46, "deductions_other": -8}},
        metric="cet1",
        movement={"from": 1230, "to": 1200, "delta": -30, "unit": "bps"},
    )
    row = score_case(
        gold,
        attribution(
            metric="cet1",
            movement=(1230, 1200, -30, "bps"),
            records=[walk_record("ev-1", {"RWA": -46, "Other": -8}, 1230, 1200)],
        ),
        label_map={"RWA": "rwa", "Other": "deductions_other"},
    )
    assert row["extraction"].startswith("n/a")
    assert row["driver_precision"].startswith("n/a")


# --------------------------------------------------------------------------
# 5. calibration and coverage (finding 1)
# --------------------------------------------------------------------------


def test_calibration_covers_scored_claims_only():
    """Unscored claims must leave precision, Brier and the confidently-wrong rate
    alone, and appear in the coverage count instead."""
    rows = [
        {"claims": [
            {"canonical": "liquids", "value": -3, "confidence": 90, "label": CORRECT},
            {"canonical": "asset_pricing", "value": 4, "confidence": 90, "label": INCORRECT},
            {"canonical": "nii", "value": 229, "confidence": 100, "label": UNSCORED},
        ]}
    ]
    cal = calibration(rows)
    assert cal["scored_claims"] == 2
    assert cal["unscored_claims"] == 1
    assert cal["brier"] == pytest.approx(((0.9 - 1) ** 2 + 0.9**2) / 2, abs=1e-9)
    assert cal["confidently_wrong_rate"] == 0.5


# ---------------------------------------------------------------------------
# Review round 2: the scorer reads the claim's own unit
#
# score_drivers took ONE unit from the gold movement and applied it to every
# claim, so a "+3 bps" contribution was measured against a "+3 $m" gold slot
# and graded correct by tolerance. A claim in another unit is a claim about
# something else.
# ---------------------------------------------------------------------------


def test_a_claim_in_another_unit_is_incorrect_not_correct():
    gold = gold_case(
        {"tier": "components", "drivers": {"nii": {"value": 229}}}, metric="cash_earnings"
    )
    result = score_drivers(gold_framings(gold), [claim("nii", 229, unit="bps")], "$m")
    assert result["claims"][0]["label"] == INCORRECT
    assert "claimed in bps" in result["claims"][0]["reason"]


def test_a_claim_with_no_unit_keeps_the_existing_behaviour():
    """Absence of evidence is not a mismatch: a claim that names no unit is
    scored as it always was, on its value."""
    gold = gold_case(
        {"tier": "components", "drivers": {"nii": {"value": 229}}}, metric="cash_earnings"
    )
    result = score_drivers(gold_framings(gold), [claim("nii", 229, unit="")], "$m")
    assert result["claims"][0]["label"] == CORRECT


def test_a_unit_spelling_difference_is_not_a_mismatch():
    gold = gold_case(
        {"tier": "components", "drivers": {"nii": {"value": 229}}}, metric="cash_earnings"
    )
    result = score_drivers(gold_framings(gold), [claim("nii", 229, unit="$M")], "$m")
    assert result["claims"][0]["label"] == CORRECT
