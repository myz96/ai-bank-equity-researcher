"""The quantity vocabulary: what counts as a stated number, in digits or in
words. One home, because the answer gate, the movement-grounding cap and the
bare-index strip must agree on the standard or a value could count as a
quantity under one rule and not another.
"""

from __future__ import annotations

import re

NUMBER_WORDS = (
    "zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|"
    "thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred"
)

# The unit and currency tokens a digit counts beside.
UNIT_TOKENS = r"%|bps|bp\b|ppt|per\s?cent|percent|basis|million|billion|bn\b|m\b"

# The quantity nouns a NUMBER WORD counts beside ("three basis points",
# "two million dollars"). A number word beside anything else is prose ("the
# first half" names a period, not a number).
WORDED_NOUNS = (
    r"basis[-\s]+points?|bps|per\s?cent|percent(?:age)?\s+points?|"
    r"percent|ppt|points?|million|billion|dollars?"
)

# A fact states a quantity when it prints a digit in quantity form — a
# decimal or thousands separator, three or more digits, a currency mark, or a
# unit beside it — or spells a number word beside a quantity noun. A bare
# one- or two-digit token can be a LABEL INDEX ("Tier 1 capital", "Stage 3"),
# and stripping the qualitative sentence it sits in punishes prose that
# claims no number. The trade accepted: "rose by 5" alone escapes.
QUANTITY_RE = re.compile(
    rf"\d+[.,]\d|\d{{3,}}|\$\s*\d|\d+\s*(?:{UNIT_TOKENS})|"
    rf"\b(?:{NUMBER_WORDS})\s+(?:{WORDED_NOUNS})\b",
    re.IGNORECASE,
)

# A movement stated in WORDS is still stated ("fell three basis points",
# "grew two billion dollars"). The parser reads the FULL number phrase, its
# noun, and any direction verb before it, so a worded statement grounds only
# the number it actually states: "rose ten basis points" is not a
# three-point fall, and "twenty five basis points" is 25, never a bare 5.
_TENS_WORDS = "twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety"
_UNITS_WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen"
)
WORDED_QUANTITY_RE = re.compile(
    rf"(?:\b(?P<direction>rose|increased|grew|up|higher|improved|"
    rf"fell|decreased|declined|down|lower|reduced)\b[\w\s,]{{0,30}}?)?"
    rf"\b(?:(?P<tens>{_TENS_WORDS})[-\s]+)?(?P<word>{_UNITS_WORDS}|{_TENS_WORDS}|zero|hundred)"
    rf"\s+(?P<noun>{WORDED_NOUNS})\b",
    re.IGNORECASE,
)

_WORD_VALUES = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
}

_FALL_WORDS = {"fell", "decreased", "declined", "down", "lower", "reduced"}

# Bare "dollars" carries no scale — "two dollars per account" is not a $m
# movement — so only the scaled money nouns map to units here.
_NOUN_UNITS = (
    ("basis", "bps"), ("bps", "bps"), ("percentage", "ppt"), ("ppt", "ppt"),
    ("per", "%"), ("percent", "%"), ("point", "ppt"),
    ("million", "$m"), ("billion", "$bn"),
)


def worded_quantities(text: str) -> list[tuple[float, str, int]]:
    """Every (value, unit, sign) a quote states in words.

    "fell twenty five basis points" -> (25.0, "bps", -1). Sign is 0 when no
    direction verb precedes the phrase; a caller comparing against a signed
    delta must treat a stated direction that disagrees as NOT a statement of
    that delta.
    """
    found = []
    for match in WORDED_QUANTITY_RE.finditer(text or ""):
        value = _WORD_VALUES.get(match.group("word").lower())
        if value is None:
            continue
        tens = match.group("tens")
        if tens:
            tens_value = _WORD_VALUES.get(tens.lower())
            if tens_value is None or value >= 10:
                continue
            value = tens_value + value
        noun = match.group("noun").lower()
        unit = next((u for prefix, u in _NOUN_UNITS if noun.startswith(prefix)), None)
        if unit is None:
            continue
        direction = (match.group("direction") or "").lower()
        sign = 0 if not direction else (-1 if direction in _FALL_WORDS else 1)
        found.append((float(value), unit, sign))
    return found


# A bare one- or two-digit token with no decimal, no thousands run and no
# unit word beside it is as likely a label index or a note number as a
# quantity ("See Note 1" printed the 1 that laundered a +1 ppt delta).
# Stripping those tokens before a printed-check holds the grounding bar at
# QUANTITY_RE's digit standard.
BARE_INDEX_RE = re.compile(
    rf"(?<![\d.,$])\b\d{{1,2}}\b(?![.,]\d)(?!\s*(?:{UNIT_TOKENS}))"
)

# A run of bare digits is a TABLE ROW only when a unit declaration precedes
# it in the same quote ("Return on equity (%) 13 14"); the header names the
# unit its cells omit. Without one, a bare-digit run is label indexes
# ("See Notes 1 2", "Stage 2") — a numeric neighbour proved nothing (Sol
# review round 6 laundered "Stage 2 4,504" through the neighbour rule).
_UNIT_HEADER_RE = re.compile(r"\((?:%|\$m|\$bn|bps|bpts|ppt)\)", re.IGNORECASE)


def strip_bare_indexes(text: str) -> str:
    """The quote with label-index digits removed, table-row cells kept.

    A quote carrying a unit-declaration header keeps every digit: the header
    names the unit its bare cells omit, so those cells are values."""
    text = str(text or "")
    if _UNIT_HEADER_RE.search(text):
        return text
    return BARE_INDEX_RE.sub(" ", text)
