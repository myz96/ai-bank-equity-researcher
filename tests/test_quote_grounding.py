"""The quote-grounding matrix.

Three functions decide whether a page really carries a number the answer
claims, and every test here is the repro that found a hole in one of them:

- `_quote_numbers` builds the pool of numbers a quote prints, each with the
  unit the sentence or the row header gives it.
- `quote_prints` decides whether a submitted NumberFact may be minted at all.
- `quote_states` decides whether a cited record grounds a driver's claim, and
  therefore whether that driver keeps its near-certain confidence.

A defect in any of them inverts the citation cap: the wrong claim is certified
and its neighbour is capped.
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
    _quote_numbers,
    cap_weakly_cited_claims,
    convert_unit,
    quote_prints,
    quote_states,
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
# 1. The pool keeps every digit, and the unit the sentence names
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "quote,expected",
    [
        # The reviewer's own repro, verbatim. The trailing lookahead failed on a
        # glued unit, so the engine backtracked and the pool took a PREFIX of
        # the number: these returned [10.0], [], and [2.0].
        ("cash NPAT of $10,982m", [(10982.0, "$m")]),
        ("fell 5bps", [(5.0, "bps")]),
        ("$2.5bn buyback", [(2.5, "$bn")]),
        # Real quotes from the shipped set: 8% of them glue a digit to a letter.
        ("(CET1 impact of -13bpts)", [(13.0, "bps")]),
        # A bank spells the money unit out as often as it glues it.
        ("a decrease of $1 million on the prior comparative period.", [(1.0, "$m")]),
        ("increased by 3% to $1,002.9 billion", [(3.0, "%"), (1002.9, "$bn")]),
        # The spelled-out ratio units the pool used to read as bare numbers.
        # Without them "decreased 5 basis points" reached the conversion table
        # as a unitless 5, and any unit the model named was accepted for it.
        ("Net interest margin decreased 5 basis points", [(5.0, "bps")]),
        ("cost-to-income rose 2 percentage points", [(2.0, "ppt")]),
        ("the ratio was 2.03 per cent", [(2.03, "%")]),
        # A word that merely starts with a unit letter is not a unit, and a
        # period tag is not a magnitude.
        ("12 months at 31 December 2025", [(12.0, ""), (31.0, "")]),
    ],
)
def test_a_number_keeps_its_glued_unit_and_its_digits(quote, expected):
    assert _quote_numbers(quote) == expected


def test_a_bare_year_is_not_a_magnitude():
    """A period TAG was already excluded; a sentence spells the year out."""
    assert (2025.0, "") not in _quote_numbers("at 31 December 2025 the ratio was 12.2%")


def test_the_citation_cap_is_not_inverted_by_a_digit_prefix():
    """One record, both directions of the defect at once.

    The quote prints 10,982. Before the fix the driver claiming +10982 was
    CAPPED (the pool held 10, not 10982) and a neighbour claiming +10 was
    certified at 95 by that same prefix.
    """
    quote = "Cash net profit after tax was $10,982m, up 7% on the prior year."
    assert quote_states(quote, 10982, "$m") is True
    assert quote_states(quote, 10, "$m") is False


# ---------------------------------------------------------------------------
# 2. The citation cap binds the unit, not only the magnitude
# ---------------------------------------------------------------------------


def test_a_dollar_cell_does_not_ground_a_percentage_point_claim():
    """The shipped CBA 1H26 cost-to-income record, exactly as it was saved.

    `notable_items +0.0 ppt` kept confidence 90 because a cited record carried
    a NumberFact of `0.0 $m`. A zero in another unit grounds nothing, and a
    zero-valued claim is the easiest of all to ground by accident.
    """
    record = _record(
        "ev-16",
        "Restructuring and notable items",
        [("Notable items 31 Dec 25", -170.0, "$m"),
         ("Notable items 30 Jun 25", -130.0, "$m"),
         ("Notable items 31 Dec 24", 0.0, "$m")],
    )
    attribution = _attribution(
        unit="ppt",
        movement=(45.7, 45.5, -0.2),
        metric="cti",
        drivers=[("notable_items", 0.0, 90, ["ev-16"], None)],
        records=[record],
    )
    assert cap_weakly_cited_claims(attribution) == ["notable_items +0 ppt"]
    assert attribution.drivers[0].confidence == CLAIM_CITATION_CAP


def test_basis_points_ground_the_same_movement_in_points():
    """A -20 bps fact grounds -0.2 ppt, and never -20 ppt."""
    record = _record("ev-1", "Cash return on equity 11.4% 11.6% (20 bps)",
                     [("ROE change", -20.0, "bps")])
    grounded = _attribution(
        unit="ppt", movement=(11.6, 11.4, -0.2), metric="roe",
        drivers=[("earnings", -0.2, 95, ["ev-1"], None)], records=[record],
    )
    assert cap_weakly_cited_claims(grounded) == []
    at_the_wrong_scale = _attribution(
        unit="ppt", movement=(11.6, 11.4, -0.2), metric="roe",
        drivers=[("earnings", -20.0, 95, ["ev-1"], None)], records=[record],
    )
    assert at_the_wrong_scale.drivers[0].canonical in cap_weakly_cited_claims(
        at_the_wrong_scale
    )[0]


def test_a_number_with_no_unit_grounds_nothing():
    """Absent unit is no evidence either way, in either direction."""
    assert convert_unit(5.0, "", "$m") is None
    assert convert_unit(5.0, "$m", "") is None
    assert convert_unit(5.0, "bps", "$m") is None
    assert convert_unit(2.5, "$bn", "$m") == 2500.0


# ---------------------------------------------------------------------------
# 3. A NumberFact's UNIT is verified where the fact is minted
# ---------------------------------------------------------------------------


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


def test_a_basis_point_table_does_not_ground_a_points_claim():
    """A real shipped quote. "pt" is a substring of "bpts", so the ppt family
    test passed on a quote that names only basis points, and a bare 34 grounded
    a claim of 34 ppt — 100x wrong."""
    assert quote_states("Movements in bpts Credit Risk (34)", 34.0, "ppt") is False


def test_an_english_word_does_not_name_a_unit_family():
    """Ordinary English that carries "pt" or "cent" inside a word."""
    quote = "Restructuring costs of 45 were accepted in September, except where adopted"
    assert quote_states(quote, 45.0, "ppt") is False
    assert quote_states(quote, 45.0, "cents") is False


def test_the_quote_that_does_name_the_family_still_grounds_its_number():
    """The tightening must not take the legitimate readings with it."""
    assert quote_states("Cost to income ratio, per cent 45.0 46.2", 45.0, "ppt") is True
    assert quote_states("Movement in CET1 (bps) 12 34", 34.0, "bps") is True
    assert quote_states("Dividend of 245 cents per share", 245.0, "cents") is True
    assert quote_states("Total operating income $m 12,345", 12345.0, "$m") is True


# ---------------------------------------------------------------------------
# 4. A unit the ROW HEADER declares binds the cells that stand after it
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


@pytest.mark.parametrize(
    "quote,value,unit",
    [
        # A bare cell under no unit signal at all still grounds a claim of an
        # unstated unit: the row is what says which unit it is in.
        ("Loan impairment expense 319 406 320", 319, "$m"),
        ("Loan impairment expense 319 406 320", 319, "bps"),
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
        # Facts the saved set loses to this fix, in their own words: a billions
        # row whose fact claims the same magnitude in millions.
        ("Risk weighted assets ($bn) 482 496 505", 482.0),
        ("Average interest earning assets ($bn) 1,001.2 978.7 2.3%", 1001.2),
    ],
)
def test_a_billions_row_does_not_print_the_same_number_in_millions(quote, value):
    assert quote_prints(quote, value, "$m") is False
    assert quote_prints(quote, value, "$bn") is True
    assert quote_prints(quote, value * 1000.0, "$m") is True


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
# 5. The digits of a LABEL are not the numbers a quote prints
# ---------------------------------------------------------------------------


def test_a_full_row_grounds_its_own_figures_and_no_others():
    """The row the round-4 reviewer's artifact quotes IN FULL: its printed
    figures ground the fact they state and refuse the one they do not.

    The extractor gate read the digits of a LABEL as printed numbers, so
    "Level 2 common equity Tier 1 capital ratio" lost its no-number exemption
    and dropped the 12.53%/12.49% facts the record was cited for.
    """
    quote = ("Level 2 common equity Tier 1 capital ratio: - Australian Prudential "
             "Regulation Authority (APRA) 12.53% 12.49% 4 bps")
    assert quote_prints(quote, 12.53, "%") is True
    assert quote_prints(quote, 999.0, "%") is False


def test_the_round_three_drop_still_holds():
    """A quote that prints real numbers still drops the fact it does not carry."""
    assert quote_prints(
        "Loan impairment expense was $554 million, a decrease of $1,964 million",
        2518.0,
        "$m",
    ) is False
