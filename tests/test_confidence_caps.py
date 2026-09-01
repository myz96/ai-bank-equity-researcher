"""The confidence-cap rules.

A check that fails proves something is wrong. These rules decide WHO loses
confidence for it:

- `cap_unreconciled_drivers` reads `WHOLE_TABLE_FAILURES`: a failure that
  condemns the whole driver table caps every quantified driver in it.
- `cap_drivers_on_failed_walks` caps by NAME: a broken chart read indicts the
  drivers that cite that chart, and nobody else.
- `cap_weakly_cited_claims` caps a claim whose own cited records neither print
  its value nor state it in words.
- An unstated self-report is LOW, never a crash.

Each test carries the shipped artifact that found the hole. A driver that keeps
85 or 95 behind a failed check is exactly the confidently-wrong population the
calibration metrics exist to measure.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.validation.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    EvidenceRecord,
    Movement,
    NumberFact,
)
from bank_equity_researcher.validation.validate import (
    CLAIM_CITATION_CAP,
    WHOLE_TABLE_FAILURES,
    cap_drivers_on_failed_walks,
    cap_unreconciled_drivers,
    cap_weakly_cited_claims,
    check_comparison_leak,
)


def _record(record_id: str, quote: str, numbers: list[tuple] = ()) -> EvidenceRecord:
    return EvidenceRecord(
        id=record_id,
        doc_id="CBA/1H26/profit_announcement",
        pdf_page=34,
        kind="table",
        quote=quote,
        numbers=[NumberFact(label=label, value=value, unit=unit) for label, value, unit in numbers],
    )


def _attribution(unit="$m", movement=(5132.0, 5445.0, 313.0), drivers=(), records=(),
                 metric="cash_earnings") -> Attribution:
    return Attribution(
        bank="CBA",
        metric=metric,
        period="1H26",
        comparator="1H25",
        basis="cash",
        movement=Movement(
            from_value=movement[0], to_value=movement[1], delta=movement[2], unit=unit
        ),
        drivers=[
            DriverClaim(
                canonical=canonical,
                contribution=Contribution(value=value, unit=driver_unit or unit),
                confidence=confidence,
                evidence=list(evidence),
            )
            for canonical, value, confidence, evidence, driver_unit in drivers
        ],
        evidence_records=list(records),
    )


# ---------------------------------------------------------------------------
# 1. A fatal check reaches the drivers
# ---------------------------------------------------------------------------


def test_a_bridge_that_does_not_close_caps_every_quantified_driver():
    """The live confidently-wrong claim.

    CBA 1H26 cash earnings failed drivers_reconcile, the answer declared 40,
    and `credit_impairment_charge -1.0` shipped at 85 against a gold of +1.
    A bridge that does not close proves one contribution is wrong without
    saying which, so none of them may claim near-certainty.

    A failed check used to lower `attribution_confidence` alone. The
    calibration metrics read PER-DRIVER confidence, so every failed check was
    invisible to them.
    """
    attribution = _attribution(
        drivers=[
            ("nii", 761.0, 85, ["ev-1"], None),
            ("credit_impairment_charge", -1.0, 85, ["ev-1"], None),
        ]
    )
    capped = cap_unreconciled_drivers(
        attribution, ["drivers_reconcile (drivers +760.0 + residual +0.0 != delta +313.0, tol 1.0)"]
    )
    assert len(capped) == 2
    assert [d.confidence for d in attribution.drivers] == [CLAIM_CITATION_CAP, CLAIM_CITATION_CAP]
    assert any("unreconciled_bridge_cap_80" in d.checks_passed for d in attribution.drivers)


def test_an_unrelated_failed_check_leaves_the_drivers_alone():
    """The cap names the failures that condemn the WHOLE table, not every one."""
    attribution = _attribution(drivers=[("nii", 313.0, 90, ["ev-1"], None)])
    assert cap_unreconciled_drivers(attribution, ["movement_from_variant (…)"]) == []
    assert attribution.drivers[0].confidence == 90


def test_a_driver_already_at_or_below_the_cap_is_left_alone():
    attribution = _attribution(drivers=[("nii", 313.0, 60, ["ev-1"], None)])
    cap_unreconciled_drivers(attribution, ["drivers_reconcile (…)"])
    assert attribution.drivers[0].confidence == 60


def test_a_broken_movement_caps_the_whole_driver_table():
    """The table was written against the movement, so a movement that does not
    add up condemns every share of it. Same argument for a contribution stated
    in another unit: the bridge it closed was never closed."""
    for failure in ("movement_arithmetic (5132.0 + 313.0 != 5000.0, tol 0.51 $m)",
                    "drivers_unit_mismatch (+3 bps is not stated in the movement's unit)"):
        attribution = _attribution(drivers=[("net_interest_income", 310.0, 95, [], None)])
        assert cap_unreconciled_drivers(attribution, [failure]) != []
        assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


@pytest.mark.parametrize(
    "failure",
    [
        # `comparison_leak` fired on a 95-confidence driver,
        # `cap_unreconciled_drivers` returned [] and the confidence stayed
        # at 95.
        (
            "comparison_leak (funding.deposits claims -3, which is the 'Deposits' bar of "
            "CBA/1H26/results_presentation p28, a walk for a different comparison; "
            "the task-comparison walk shows -5)"
        ),
        (
            "component_from_prior_half (credit_impairment_charge claims -1 $m, which is a "
            "delta against the PRIOR HALF's column and matches no 1H26 versus 1H25 delta "
            "in the evidence)"
        ),
    ],
)
def test_a_wrong_claim_check_that_lost_its_named_cap_caps_the_table(failure):
    """The cleanup regression, both halves of it.

    Ticket 33 wave 1 deleted `comparison_leak_cap_80` and
    `component_column_cap_80` because neither override fired on the 90 saved
    artifacts. Nothing replaced them, and `WHOLE_TABLE_FAILURES` still named
    both as absent BECAUSE they cap in place. A demonstrably wrong driver was
    therefore left at 95.
    """
    attribution = _attribution(drivers=[("credit_impairment_charge", -1.0, 95, [], None)])
    assert cap_unreconciled_drivers(attribution, [failure]) != []
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


def test_both_names_are_whole_table_failures():
    assert "comparison_leak" in WHOLE_TABLE_FAILURES
    assert "component_from_prior_half" in WHOLE_TABLE_FAILURES


# ---------------------------------------------------------------------------
# 2. A broken chart read is capped by NAME
# ---------------------------------------------------------------------------


def test_the_walk_names_stay_out_of_the_whole_table_set():
    """A walk that does not sum indicts the CHART READ, not the driver table.

    Measured on the saved set: `cba-nim-fy26-vs-fy25-agentic-cheap` has one
    driver of seven citing the broken walk and six citing prose, so a blanket
    cap would lower six claims the chart never touched.
    """
    assert "walk_sum" not in WHOLE_TABLE_FAILURES
    assert "walk_extraction_error" not in WHOLE_TABLE_FAILURES


def test_a_driver_that_cites_a_broken_walk_is_capped():
    """`wbc-cet1-fy25-vs-fy24-cheap`, verbatim from the saved set.

    Five drivers, all citing ev-1, whose bars sum to 1225 against that chart's
    own end of 1253. Every one of them shipped at 85. The neighbour grounded
    in prose keeps its confidence.
    """
    attribution = _attribution(
        unit="bps",
        movement=(1249.0, 1253.0, 4.0),
        drivers=[
            ("earnings_generation", 4.0, 85, ["ev-1"], "bps"),
            ("rwa", -16.0, 90, ["ev-1", "ev-20"], "bps"),
            ("asset_pricing", -5.0, 90, ["ev-5"], "bps"),
        ],
    )
    failure = "walk_sum (start 1249 + bars -24.0 = 1225.0 != end 1253, tol 1.0 bps)"
    walks = [
        {"record_id": "ev-1", "checks_failed": [failure]},
        {"record_id": "ev-9", "checks_failed": []},
    ]
    capped = cap_drivers_on_failed_walks(attribution, walks)
    named = {d.canonical: d for d in attribution.drivers}
    assert capped == ["earnings_generation +4 bps", "rwa -16 bps"]
    assert named["earnings_generation"].confidence == CLAIM_CITATION_CAP
    assert named["rwa"].confidence == CLAIM_CITATION_CAP
    assert named["asset_pricing"].confidence == 90
    assert "failed_walk_cap_80" in named["rwa"].checks_passed


def test_a_walk_that_sums_caps_nobody():
    attribution = _attribution(
        unit="bps", movement=(1249.0, 1253.0, 4.0),
        drivers=[("earnings_generation", 4.0, 90, ["ev-1"], "bps")],
    )
    assert cap_drivers_on_failed_walks(
        attribution, [{"record_id": "ev-1", "checks_failed": []}]
    ) == []
    assert attribution.drivers[0].confidence == 90
    assert attribution.limitations == []


# ---------------------------------------------------------------------------
# 3. A check that NAMES its offender reports, and does not mutate
# ---------------------------------------------------------------------------


def test_a_comparison_leak_names_the_driver_it_finds():
    """The check names the offender — it prints the bar, its label and its
    source. It used to cap that driver at 80 as well. Ticket 33 wave 1 deleted
    the cap: `comparison_leak_cap_80` fired on 0 of the 90 saved artifacts, so
    it cited no run. The naming, and the fatal grading of a failed check, are
    untouched.
    """
    attribution = _attribution(
        drivers=[
            ("dividend_net_drp", -91.0, 95, [], None),
            ("net_interest_income", 310.0, 95, [], None),
        ]
    )
    primary_view = {"dividend_net_drp": [{"value": -40.0, "label": "Dividends paid",
                                          "source": "CBA/FY26 p12"}]}
    context_view = {"dividend_net_drp": [{"value": -91.0, "label": "Dividends paid",
                                          "source": "CBA/1H26 p9"}]}
    failed = check_comparison_leak(attribution, primary_view, context_view)[1]
    assert any(f.startswith("comparison_leak") for f in failed)
    named = {d.canonical: d for d in attribution.drivers}
    # The check reports and no longer mutates: both drivers keep what they said.
    assert named["dividend_net_drp"].confidence == 95
    assert named["dividend_net_drp"].checks_passed == []
    assert named["net_interest_income"].confidence == 95


# ---------------------------------------------------------------------------
# 4. The weak-citation cap, and the unstated self-report
# ---------------------------------------------------------------------------


def test_the_dollar_fact_no_longer_reaches_the_citation_cap():
    """The whole chain: mint, bind, cap.

    The fact would not be minted at all now; even if it were, it grounds
    nothing, so the driver loses its right to near-certainty.
    """
    record = _record("ev-1", "Net interest margin decreased 5 basis points to 2.03 per cent.",
                     [("NIM change", 5.0, "$m")])
    attribution = _attribution(
        drivers=[("net_interest_income", 5.0, 95, ["ev-1"], None)], records=[record]
    )
    record.numbers = []
    assert cap_weakly_cited_claims(attribution) == ["net_interest_income +5 $m"]
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


def test_null_confidence_is_low_not_a_crash():
    """An explicit JSON null is the other common form of an unstated
    self-report; both forms mean LOW, never a crash."""
    assert DriverClaim(canonical="x").confidence == 40
    assert DriverClaim(canonical="x", confidence=None).confidence == 40
