"""Review round 4.

Every test carries the repro that found the defect, as the reviewer executed
it. All four sit inside round-2 and round-3 fresh code:

- `quote_prints` asked the unit question only of a number that carried a GLUED
  unit, so a row that declares its unit in a HEADER ("Net interest margin (%)
  2.05 2.08") minted a `$m` fact off a percent cell.
- The money family test held the generic token "$" for both `$m` and `$bn`, so
  "Assets ($bn) 2.5" stated 2.5 `$m` without the 1000x conversion.
- `settle_ratio_scale` corrected the NUMBERS and kept the model's conflicting
  movement UNIT, and `check_ratio_level` keyed off that retained unit.
- The extractor gate read the digits of a LABEL as printed numbers, so
  "Level 2 common equity Tier 1 capital ratio" lost its no-number exemption and
  dropped the 12.53%/12.49% facts the record was cited for.
"""

from __future__ import annotations

import pytest

from bank_equity_researcher.extract import _numbers_the_quote_prints
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
    cap_weakly_cited_claims,
    check_drivers_reconcile,
    check_ratio_level,
    printed_numbers,
    quote_prints,
    quote_states,
    settle_ratio_scale,
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
# 1. A unit the ROW HEADER declares binds the cells under it
# ---------------------------------------------------------------------------


def test_a_percent_row_does_not_mint_a_dollar_fact():
    """Reviewer finding 1, verbatim.

    Round 3 bound the unit of a number that carries its unit GLUED to it, and
    a table row does not: it prints the unit once, in the header, and the cells
    bare. `quote_prints` therefore took a percent cell for a dollar figure.
    """
    quote = "Net interest margin (%) 2.05 2.08"
    assert quote_prints(quote, 2.05, "$m") is False
    assert quote_prints(quote, 2.05, "%") is True
    assert quote_prints(quote, 2.05, "ppt") is True
    # 2.05 per cent is 205 basis points, so the bare cell grounds neither
    # 2.05 bps nor anything else the conversion table refuses.
    assert quote_prints(quote, 2.05, "bps") is False
    assert quote_prints(quote, 205.0, "bps") is True


def test_the_invented_dollar_fact_no_longer_survives_its_own_mint():
    """The whole chain the reviewer executed: mint, bind, cap."""
    quote = "Net interest margin (%) 2.05 2.08"
    assert _numbers_the_quote_prints(
        quote, [{"label": "invented money", "value": 2.05, "unit": "$m"}]
    ) == []
    record = _record("ev-1", quote)
    attribution = _attribution(
        drivers=[("net_interest_income", 2.05, 95, ["ev-1"], "$m")], records=[record]
    )
    assert cap_weakly_cited_claims(attribution) == ["net_interest_income +2.05 $m"]
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


@pytest.mark.parametrize(
    "quote,value,unit",
    [
        # A bare cell under no unit signal at all still grounds a claim of an
        # unstated unit: the row is what says which unit it is in.
        ("Loan impairment expense 319 406 320", 319, "$m"),
        ("Loan impairment expense 319 406 320", 319, "bps"),
        # The unit sits on ANOTHER number, not on the row: a percentage change
        # column does not make its dollar cells percentages.
        ("Operating expenses 6,000 5,800 3.4%", 6000, "$m"),
    ],
)
def test_a_cell_with_no_unit_signal_still_grounds_its_claim(quote, value, unit):
    assert quote_prints(quote, value, unit) is True


# One quote spanning four rows of one table, from `cba-roe-1h26-vs-1h25-cheap`.
_ROE_TABLE = (
    'Return on Equity - "cash basis" Average net assets 78,004 77,020 74,176 '
    'Net profit after tax - "cash basis" 5,445 5,120 5,132 '
    'ROE - "cash basis" (%) 13.8 13.4 13.7'
)


@pytest.mark.parametrize(
    "quote,value,unit",
    [
        # Measured on the saved set, both halves. A money row prints its
        # percentage change column under the one "($M)" header: reading the
        # header over the change cells dropped 10 real facts.
        ("Corporate tax expense ($M) 4,699 4,491 5 2,332 2,367 (1)", 5, "%"),
        ("Risk weighted assets (RWA) ($M) 505,310 496,145 482,369 2 5", 5, "%"),
        ("Corporate tax expense ($M) 4,699 4,491 5 2,332 2,367 (1)", 4699, "$m"),
        # A quote spans four rows of one table, and the header of the LAST row
        # says nothing about the cells of the first: reading the "(%)"
        # backwards over the whole quote dropped 54 real dollar facts.
        (_ROE_TABLE, 78004, "$m"),
        (_ROE_TABLE, 13.8, "%"),
    ],
)
def test_a_declaration_binds_only_what_stands_after_it(quote, value, unit):
    assert quote_prints(quote, value, unit) is True


@pytest.mark.parametrize(
    "quote,value",
    [
        # Every fact the saved set loses to this fix, in its own words: a
        # billions row whose fact claims the same magnitude in millions.
        ("Risk weighted assets ($bn) 482 496 505", 482.0),
        ("Risk Weighted Assets (RWA) ($bn) 455 454 451", 455.0),
        ("Total assets ($bn) 1,409 +7.7%", 1409.0),
        ("Average interest earning assets ($bn) 1,001.2 978.7 2.3%", 1001.2),
        ("Domestic Equity Hedge Balance $bn 57 2H21 Avg. Rate 0.80%", 57.0),
    ],
)
def test_a_billions_row_does_not_print_the_same_number_in_millions(quote, value):
    assert quote_prints(quote, value, "$m") is False
    assert quote_prints(quote, value, "$bn") is True
    assert quote_prints(quote, value * 1000.0, "$m") is True


# ---------------------------------------------------------------------------
# 2. $m and $bn are different units
# ---------------------------------------------------------------------------


def test_a_billions_row_does_not_state_a_millions_claim():
    """Reviewer finding 3, verbatim: both families held the generic "$"."""
    assert quote_states("Assets ($bn) 2.5", 2.5, "$m") is False
    assert quote_states("Assets ($bn) 2.5", 2.5, "$bn") is True
    # The conversion is available; it is the 1:1 reading that was wrong.
    assert quote_states("Assets ($bn) 2.5", 2500.0, "$m") is True
    assert quote_prints("Assets ($bn) 2.5", 2.5, "$m") is False


def test_a_dollar_row_that_names_no_scale_still_grounds_a_money_claim():
    """A generic "$" names the money family and not a scale within it."""
    assert quote_states("Total operating income $m 12,345", 12345.0, "$m") is True
    assert quote_states("Loan impairment expense was $319 million.", 319, "$m") is True


# ---------------------------------------------------------------------------
# 3. The ratio corrector settles the UNIT as well as the numbers
# ---------------------------------------------------------------------------


def test_the_ratio_corrector_settles_the_movement_unit():
    """Reviewer finding 2, verbatim.

    The NAB FY25 ROE submission carried the metric's numbers in basis points
    AND the label "bps". The corrector divided the numbers by 100 and left the
    label, so the artifact shipped "11.6 -> 11.4, -0.2 bps" — the gold movement
    written in a unit 100x out.
    """
    record = _record("ev-1", "Cash return on equity 11.4% 11.6% (20 bps)",
                     [("ROE FY25", 11.4, "%"), ("ROE FY24", 11.6, "%")])
    attribution = _attribution(
        unit="bps", movement=(1160.0, 1140.0, -20.0), metric="roe", records=[record]
    )
    note = settle_ratio_scale(attribution, "ppt")
    assert note is not None
    assert (attribution.movement.from_value, attribution.movement.to_value) == (11.6, 11.4)
    assert attribution.movement.delta == -0.2
    assert attribution.movement.unit == "ppt"
    assert "bps" in note and "ppt" in note


def test_the_ratio_level_check_keys_on_the_metric_unit():
    """The check read the model's own label, so a ppt metric submitted as
    "1160 bps" was never asked to be ratio-sized."""
    movement = Movement(from_value=1160.0, to_value=1140.0, delta=-20.0, unit="bps")
    assert check_ratio_level(movement, "ppt")[1] != []
    assert check_ratio_level(movement, "ppt")[1][0].startswith("movement_level_not_ratio_sized")
    # A metric whose own unit IS basis points keeps its basis-point levels.
    assert check_ratio_level(movement, "bps") == ([], [])


def test_the_corrected_movement_passes_every_check_in_its_own_unit():
    record = _record("ev-1", "Cash return on equity 11.4% 11.6% (20 bps)",
                     [("ROE FY25", 11.4, "%"), ("ROE FY24", 11.6, "%")])
    attribution = _attribution(
        unit="bps", movement=(1160.0, 1140.0, -20.0), metric="roe", records=[record]
    )
    settle_ratio_scale(attribution, "ppt")
    assert check_ratio_level(attribution.movement, "ppt")[1] == []
    assert check_drivers_reconcile(attribution)[1] == ["no_quantified_drivers"]


# ---------------------------------------------------------------------------
# 4. The digits of a LABEL are not the numbers a quote prints
# ---------------------------------------------------------------------------


def test_a_label_index_is_not_a_printed_number():
    """Reviewer finding 4, verbatim, and a LIVE regression.

    "Level 2 common equity Tier 1 capital ratio" parses as [2, 1], so the
    quote looked like one that prints numbers, the gate switched on, and the
    12.53%/12.49% facts the record was cited for were dropped. The saved WBC
    FY25 CET1 artifact carries the record with an empty `numbers` list.
    """
    quote = ("Level 2 common equity Tier 1 capital ratio: - Australian Prudential "
             "Regulation Authority (APRA)")
    assert printed_numbers(quote, 12.53, "%") == []
    facts = _numbers_the_quote_prints(
        quote,
        [{"label": "CET1 APRA FY25", "value": 12.53, "unit": "%"},
         {"label": "CET1 APRA FY24", "value": 12.49, "unit": "%"}],
    )
    assert [fact.value for fact in facts] == [12.53, 12.49]


def test_the_same_row_with_its_figures_still_gates_on_them():
    """The row the reviewer's second artifact quotes IN FULL. Its figures are
    printed, so the gate stays on and a fact the row does not carry is
    dropped."""
    quote = ("Level 2 common equity Tier 1 capital ratio: - Australian Prudential "
             "Regulation Authority (APRA) 12.53% 12.49% 4 bps")
    assert printed_numbers(quote, 12.53, "%") == [(12.53, "%"), (12.49, "%"), (4.0, "bps")]
    facts = _numbers_the_quote_prints(
        quote,
        [{"label": "CET1 APRA FY25", "value": 12.53, "unit": "%"},
         {"label": "invented", "value": 999.0, "unit": "%"}],
    )
    assert [fact.value for fact in facts] == [12.53]


@pytest.mark.parametrize(
    "quote,value,unit",
    [
        # Round 3's protection: a quote that prints real numbers still drops
        # the fact it does not carry. None of these digits is a label index.
        ("Loan impairment expense was $554 million, a decrease of $1,964 million",
         2518.0, "$m"),
        ("Treasury & Markets impact on NIM 0.13% 0.13%", 0.0, "bps"),
    ],
)
def test_the_round_three_drop_still_holds(quote, value, unit):
    assert printed_numbers(quote, value, unit) != []
    assert _numbers_the_quote_prints(
        quote, [{"label": "computed", "value": value, "unit": unit}]
    ) == []


@pytest.mark.parametrize(
    "quote,value,unit",
    [
        # A digit that is not embedded in words is a figure, whatever its size.
        ("Stage 2 4,504 4,102", 4504.0, "$m"),
        ("Net interest margin (%) 2.05 2.08", 2.05, "%"),
        # A label index the FACT itself claims is not "unlike" the fact, so the
        # exemption is not handed out on it: the row declares $bn and the fact
        # says $m, which is a conflict, not an absence of evidence.
        ("Segment 3 income ($bn) by division", 3.0, "$m"),
    ],
)
def test_a_real_figure_is_never_read_as_a_label_index(quote, value, unit):
    assert printed_numbers(quote, value, unit) != []
