"""Review round 3: the convergence round.

Every test carries the repro that found the defect, as the reviewer executed
it. Four of the six sit inside round-2 fresh code, and two of those are
regressions the round-2 fix introduced:

- `quote_prints` verified a NumberFact's VALUE and never its UNIT, so a "$m"
  fact minted off a basis-point sentence, and B3's conversion table then bound
  a unit the page never printed.
- `_FAMILY_WORDS["ppt"]` held the token "pt", which is a substring of "bpts",
  so a bps quote grounded a ppt claim 100x too large — the same inversion as
  round-2 finding B1, inside B1's own replacement.
- `settle_ratio_scale` keyed on the movement's unit, which the model writes,
  rather than the METRIC's unit, which the taxonomy fixes. It therefore
  reversed the percent-to-bps lift under exactly the condition the lift exists
  for.
- The reconciliation sum became unit-typed for the CONTRIBUTIONS and stayed
  unit-blind for the RESIDUAL, so three basis points still closed a dollar
  bridge.
- `cap_unreconciled_drivers` covered two fatal names out of eight, and
  `check_comparison_leak` named the offending driver and capped nobody.
- `strip_markers` narrowed to a shape rule that still deleted a data column
  whenever the run of digits sat on its own line.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.research_agent import match_quote, strip_markers
from bank_equity_researcher.schema import (
    Attribution,
    Contribution,
    DriverClaim,
    EvidenceRecord,
    Movement,
    NumberFact,
)
from bank_equity_researcher.validate import (
    CLAIM_CITATION_CAP,
    WHOLE_TABLE_FAILURES,
    _quote_numbers,
    _states,
    cap_drivers_on_failed_walks,
    cap_unreconciled_drivers,
    cap_weakly_cited_claims,
    check_comparison_leak,
    check_drivers_reconcile,
    check_movement,
    check_ratio_level,
    quote_prints,
    quote_states,
    settle_ratio_scale,
    sign_flip_hint,
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
                 residual=None, metric="cash_earnings") -> Attribution:
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
        residual=None if residual is None else Contribution(value=residual[0], unit=residual[1]),
        evidence_records=list(records),
    )


# ---------------------------------------------------------------------------
# 1 + 5. The NumberFact's UNIT is verified where the fact is minted
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "quote,expected",
    [
        # The spelled-out ratio units the pool used to read as bare numbers.
        # Without them "decreased 5 basis points" reached the conversion table
        # as a unitless 5, and any unit the model named was accepted for it.
        ("Net interest margin decreased 5 basis points", [(5.0, "bps")]),
        ("The margin fell 1 basis point", [(1.0, "bps")]),
        ("a CET1 impact of 13 bpts", [(13.0, "bps")]),
        ("cost-to-income rose 2 percentage points", [(2.0, "ppt")]),
        ("the ratio was 2.03 per cent", [(2.03, "%")]),
        ("the ratio was 12.2 percent", [(12.2, "%")]),
        # Money stays money, and a word that merely starts with a unit letter
        # is still not a unit.
        ("cash NPAT of $10,982m", [(10982.0, "$m")]),
        ("a decrease of $1 million on the prior comparative period.", [(1.0, "$m")]),
        ("12 months at 31 December 2025", [(12.0, ""), (31.0, "")]),
    ],
)
def test_the_pool_reads_a_spelled_out_ratio_unit(quote, expected):
    assert _quote_numbers(quote) == expected


def test_a_basis_point_sentence_does_not_mint_a_dollar_fact():
    """Reviewer C finding 1, verbatim.

    The agent cites a real, verbatim, basis-point sentence and attaches
    {"value": 5, "unit": "$m"}. `quote_prints` compared magnitudes with no unit
    at all, so the fact was kept, `_states` then bound it, and a `+5 $m` driver
    kept confidence 95.
    """
    quote = "Net interest margin decreased 5 basis points to 2.03 per cent."
    assert quote_prints(quote, 5, "$m") is False
    assert quote_prints(quote, 5, "bps") is True
    # Codex finding 2's spelling of the same defect, in the other direction.
    assert quote_prints("NPAT was $150m", 150, "bps") is False
    assert quote_prints("NPAT was $150m", 150, "$m") is True


def test_a_bare_number_still_mints_whatever_unit_the_fact_names():
    """The bare-number branch is untouched: a table cell prints no unit, and
    the row is what says which unit it is in."""
    assert quote_prints("Loan impairment expense 319 406 320", 319, "$m") is True
    assert quote_prints("Loan impairment expense 319 406 320", 319, "bps") is True


def test_the_dollar_fact_no_longer_reaches_the_citation_cap():
    """The whole chain C executed: mint, bind, cap."""
    record = _record("ev-1", "Net interest margin decreased 5 basis points to 2.03 per cent.",
                     [("NIM change", 5.0, "$m")])
    attribution = _attribution(
        drivers=[("net_interest_income", 5.0, 95, ["ev-1"], None)], records=[record]
    )
    # The fact would not be minted at all now; even if it were, it grounds
    # nothing, so the driver loses its right to near-certainty.
    assert _states(5.0, "$m", 5.0, "$m", 0.5) is True  # the fact's own unit is self-consistent
    assert quote_prints(record.quote, 5.0, "$m") is False
    record.numbers = []
    assert cap_weakly_cited_claims(attribution) == ["net_interest_income +5 $m"]
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


@pytest.mark.parametrize(
    "quote,value",
    [
        # Two real shipped quotes. "pt" is a substring of "bpts", so the ppt
        # family test passed on a quote that names only basis points, and a
        # bare 34 grounded a claim of 34 ppt — 100x wrong.
        ("Movements in bpts Credit Risk (34)", 34.0),
        ("RBS1 bpts 209 227 2H20 1H21 2H21", 209.0),
    ],
)
def test_a_basis_point_table_does_not_ground_a_points_claim(quote, value):
    assert quote_states(quote, value, "ppt") is False


@pytest.mark.parametrize(
    "quote",
    [
        # Ordinary English that carries "pt" or "cent" inside a word.
        "Restructuring costs of 45 were accepted in September, except where adopted",
        "In recent periods the balance was 45 and 60",
    ],
)
def test_an_english_word_does_not_name_a_unit_family(quote):
    assert quote_states(quote, 45.0, "ppt") is False
    assert quote_states(quote, 45.0, "cents") is False


def test_the_quote_that_does_name_the_family_still_grounds_its_number():
    """The tightening must not take the legitimate readings with it."""
    assert quote_states("Cost to income ratio, per cent 45.0 46.2", 45.0, "ppt") is True
    assert quote_states("Movement in CET1 (bps) 12 34", 34.0, "bps") is True
    assert quote_states("Dividend of 245 cents per share", 245.0, "cents") is True
    assert quote_states("Total operating income $m 12,345", 12345.0, "$m") is True


# ---------------------------------------------------------------------------
# 2. The ratio corrector keys on the METRIC's unit
# ---------------------------------------------------------------------------


def test_the_ratio_corrector_does_not_reverse_the_percent_to_bps_lift():
    """Reviewer C finding 2, verbatim.

    CET1's taxonomy unit is bps. The model labels the movement "%", the lift
    multiplies the endpoints by 100, and `settle_ratio_scale` — keying on the
    model's own label — divided them straight back. No check then fires, and
    the artifact ships +0.1 % against a gold of +10 bps, carrying two
    limitations that contradict each other.
    """
    record = _record("ev-1", "Common Equity Tier 1 ratio 12.20% 12.30%",
                     [("CET1 Sep 24", 12.20, "%"), ("CET1 Sep 25", 12.30, "%")])
    attribution = _attribution(
        unit="%", movement=(1220.0, 1230.0, 10.0), metric="cet1", records=[record]
    )
    assert settle_ratio_scale(attribution, "bps") is None
    assert (attribution.movement.from_value, attribution.movement.to_value) == (1220.0, 1230.0)
    assert attribution.movement.delta == 10.0


def test_the_ratio_corrector_still_fires_for_a_points_metric():
    """NAB's FY25 ROE run, unchanged: the METRIC is ppt and the endpoints
    arrived in basis points."""
    record = _record("ev-1", "Cash return on equity 11.4% 11.6% (20 bps)",
                     [("ROE FY25", 11.4, "%"), ("ROE FY24", 11.6, "%")])
    attribution = _attribution(
        unit="ppt", movement=(1160.0, 1140.0, -20.0), metric="roe", records=[record]
    )
    assert settle_ratio_scale(attribution, "ppt") is not None
    assert (attribution.movement.from_value, attribution.movement.to_value) == (11.6, 11.4)
    assert attribution.movement.delta == -0.2
    assert check_ratio_level(attribution.movement)[1] == []


def test_a_money_metric_never_reaches_the_ratio_corrector():
    attribution = _attribution(unit="$m", movement=(5132.0, 5445.0, 313.0))
    assert settle_ratio_scale(attribution, "$m") is None


# ---------------------------------------------------------------------------
# 3. The marker relaxation keeps the row's own line
# ---------------------------------------------------------------------------


def test_a_newline_column_is_not_a_footnote_marker():
    """Reviewer C finding 3, ANZ 1H26 results announcement p59.

    The first data column held 80 and the second 102, and the shape rule could
    not tell that row from a footnote marker. The quote was accepted as
    verbatim while dropping the current-period value and presenting 102 as the
    first column.
    """
    page = "Credit and Capital Markets \n \n80 \n102 \n114  \n-22% \n-30%"
    assert "80" in strip_markers(page)
    assert match_quote("Credit and Capital Markets 102 114", page)[0] is False


def test_the_footnote_repro_still_matches():
    """Round 1's own repro: CBA FY26 Profit Announcement p2 interleaves two
    note markers between the label and the value."""
    page = "Revenue from ordinary activities 2 3 30,153"
    matched, relaxation = match_quote("Revenue from ordinary activities 30,153", page)
    assert matched is True
    assert relaxation != ""


# ---------------------------------------------------------------------------
# 4. The off-unit residual never joins the sum
# ---------------------------------------------------------------------------


def test_three_basis_points_do_not_close_a_dollar_bridge():
    """Reviewer C finding 4 and Codex finding 5, verbatim.

    B7 made the sum unit-typed for the CONTRIBUTIONS and left the RESIDUAL
    unfiltered, so `drivers_reconcile` PASSED beside its own
    `drivers_unit_mismatch` failure.
    """
    attribution = _attribution(
        drivers=[("net_interest_income", 310.0, 85, [], None)], residual=(3.0, "bps")
    )
    passed, failed = check_drivers_reconcile(attribution)
    assert "drivers_reconcile" not in passed
    assert any(f.startswith("drivers_reconcile") for f in failed)
    assert any(f.startswith("drivers_unit_mismatch") for f in failed)


def test_a_residual_in_the_movement_s_own_unit_still_closes_the_bridge():
    attribution = _attribution(
        drivers=[("net_interest_income", 310.0, 85, [], None)], residual=(3.0, "$m")
    )
    passed, failed = check_drivers_reconcile(attribution)
    assert "drivers_reconcile" in passed
    assert not any(f.startswith("drivers_unit_mismatch") for f in failed)


def test_a_residual_with_no_unit_still_closes_the_bridge():
    """An unlabelled residual makes no competing unit claim, so it is read in
    the movement's unit, exactly as the contribution filter reads it."""
    attribution = _attribution(
        drivers=[("net_interest_income", 310.0, 85, [], None)], residual=(3.0, "")
    )
    assert "drivers_reconcile" in check_drivers_reconcile(attribution)[0]


def test_the_sign_hint_does_not_let_an_off_unit_residual_hide_the_gap():
    """`sign_flip_hint` repeated the same unit-blind arithmetic, so an off-unit
    residual closed the gap it was built to measure and the hint stayed
    silent."""
    attribution = _attribution(
        movement=(5132.0, 5445.0, 313.0),
        drivers=[
            ("net_interest_income", 312.0, 85, [], None),
            ("credit_impairment_charge", -1.0, 85, [], None),
        ],
        residual=(2.0, "bps"),
    )
    hint = sign_flip_hint(attribution)
    assert hint is not None
    assert "credit_impairment_charge" in hint


# ---------------------------------------------------------------------------
# 6. A fatal check that NAMES its offender caps that offender
# ---------------------------------------------------------------------------


def test_a_broken_movement_caps_the_whole_driver_table():
    """The table was written against the movement, so a movement that does not
    add up condemns every share of it. Same argument for a contribution stated
    in another unit: the bridge it closed was never closed."""
    for failure in ("movement_arithmetic (5132.0 + 313.0 != 5000.0, tol 0.51 $m)",
                    "drivers_unit_mismatch (+3 bps is not stated in the movement's unit)"):
        attribution = _attribution(drivers=[("net_interest_income", 310.0, 95, [], None)])
        assert cap_unreconciled_drivers(attribution, [failure]) != []
        assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


def test_walk_sum_is_not_a_whole_table_failure():
    """A walk that does not sum indicts the CHART READ, not the driver table.

    Measured on the saved set: `cba-nim-fy26-vs-fy25-agentic-cheap` has one
    driver of seven citing the broken walk and six citing prose, so a blanket
    cap would lower six claims the chart never touched. It is capped by name
    instead — see `test_a_driver_that_cites_a_broken_walk_is_capped`.
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


def test_a_comparison_leak_caps_the_driver_it_names():
    """Reviewer C finding 6 and Codex finding 1.

    B2's stated reason for capping the whole table is that code cannot name the
    offender. `check_comparison_leak` CAN name it — it prints the bar, its
    label and its source — and it capped nobody.
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
    assert named["dividend_net_drp"].confidence == CLAIM_CITATION_CAP
    assert "comparison_leak_cap_80" in named["dividend_net_drp"].checks_passed
    # The driver the check does NOT name keeps its confidence.
    assert named["net_interest_income"].confidence == 95


def test_a_leaking_driver_already_below_the_cap_is_left_alone():
    attribution = _attribution(drivers=[("dividend_net_drp", -91.0, 70, [], None)])
    context_view = {"dividend_net_drp": [{"value": -91.0, "label": "Dividends paid",
                                          "source": "CBA/1H26 p9"}]}
    check_comparison_leak(attribution, {}, context_view)
    assert attribution.drivers[0].confidence == 70
    assert attribution.drivers[0].checks_passed == []


def test_the_movement_check_still_passes_a_movement_that_adds_up():
    assert check_movement(
        Movement(from_value=5132.0, to_value=5445.0, delta=313.0, unit="$m")
    ) == (["movement_arithmetic"], [])
