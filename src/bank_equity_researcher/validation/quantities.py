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
# "grew two billion dollars"). The parser below reads the VALUE and the
# noun, so a worded statement grounds only the number it actually states —
# "rose ten basis points" must not stand in for a three-point fall.
WORDED_QUANTITY_RE = re.compile(
    rf"\b(?P<word>{NUMBER_WORDS})\s+(?P<noun>{WORDED_NOUNS})\b",
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

_NOUN_UNITS = (
    ("basis", "bps"), ("bps", "bps"), ("percentage", "ppt"), ("ppt", "ppt"),
    ("per", "%"), ("percent", "%"), ("point", "ppt"),
    ("million", "$m"), ("billion", "$bn"), ("dollar", "$m"),
)


def worded_quantities(text: str) -> list[tuple[float, str]]:
    """Every (value, unit) a quote states in words: "fell three basis
    points" -> (3.0, "bps"). Single number words only — compounds are rarer
    than the movements this serves and a miss errs conservative."""
    found = []
    for match in WORDED_QUANTITY_RE.finditer(text or ""):
        value = _WORD_VALUES.get(match.group("word").lower())
        noun = match.group("noun").lower()
        unit = next((u for prefix, u in _NOUN_UNITS if noun.startswith(prefix)), None)
        if value is not None and unit is not None:
            found.append((float(value), unit))
    return found

# A bare one- or two-digit token with no decimal, no thousands run and no
# unit word beside it is as likely a label index or a note number as a
# quantity ("See Note 1" printed the 1 that laundered a +1 ppt delta).
# Stripping those tokens before a printed-check holds the grounding bar at
# QUANTITY_RE's digit standard.
# A digit BESIDE another number is a table-row run, not an index: "13 14"
# is two ratio cells, "Stage 2 4,504" is an index and its figure. Stripping
# the run capped a valid "Return on equity (%) 13 14" movement (Sol audit
# round 6, executed repro), so a bare token survives when a number adjoins
# it on either side.
BARE_INDEX_RE = re.compile(
    rf"(?<![\d.,$])(?<!\d )\b\d{{1,2}}\b(?![.,]\d)(?!\s*(?:{UNIT_TOKENS}))(?! \d)"
)
