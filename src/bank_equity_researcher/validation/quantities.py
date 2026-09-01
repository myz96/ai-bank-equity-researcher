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
# "grew two billion dollars"); the grounding cap stands down rather than call
# a worded statement ungrounded. The same noun list as QUANTITY_RE's worded
# branch — one standard, not two.
WORDED_QUANTITY_RE = re.compile(
    rf"\b(?:{NUMBER_WORDS})\s+(?:{WORDED_NOUNS})\b",
    re.IGNORECASE,
)

# A bare one- or two-digit token with no decimal, no thousands run and no
# unit word beside it is as likely a label index or a note number as a
# quantity ("See Note 1" printed the 1 that laundered a +1 ppt delta).
# Stripping those tokens before a printed-check holds the grounding bar at
# QUANTITY_RE's digit standard.
BARE_INDEX_RE = re.compile(
    rf"(?<![\d.,$])\b\d{{1,2}}\b(?![.,]\d)(?!\s*(?:{UNIT_TOKENS}))"
)
