"""The verbatim-quote fidelity gate for TEXT quotes: is this quote on this
page, and under which test? Applied twice — when `cite` mints a record and
again when a submission's evidence list is resolved. Vision-read records
(walk bars, chart annotations) do not pass here: their quote strings are
built by code from the extracted values, so their fidelity discipline is the
walk checks, not a page-text match.
"""

from __future__ import annotations

import re

_PUNCTUATION = str.maketrans(
    {
        "‘": "'", "’": "'", "‚": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "−": "-", " ": " ", " ": " ",
    }
)


# A footnote or reference marker, in the SHAPE a marker takes: one or two
# digits sitting between the end of a row LABEL and that row's VALUE. The CBA
# FY26 Profit Announcement p2 text layer reads "Revenue from ordinary
# activities 2 3 30,153"; the 2 and the 3 point at notes, and a reader of the
# page sees the row as "Revenue from ordinary activities 30,153". A quote
# faithful to what the reader sees was rejected as not on the page.
#
# The shape rule is the whole of the fix. A bare "standalone one- or two-digit
# token" cannot tell a marker from data, and over the 607 pages of CBA's FY26
# and 1H26 books it removed 10,158 tokens, 16.7 a page, most of them real: the
# day and the two-digit year of every column header, every bps value under 100,
# and the tier of every capital instrument. Under that rule the page said
# "Additional Tier 1 and Tier 2 Capital" and a quote reading "Additional Tier
# and Tier Capital" was accepted as verbatim, though Tier 1 and Tier 2 are
# different instruments. The relaxation exists to let a quote OMIT a marker, so
# it must remove markers and nothing else.
#
# Four conditions, all required: a LETTER ends the label before the run; the
# run sits on the LABEL'S OWN LINE; the run is one or two digits (repeated,
# because a row carries two markers); and a VALUE follows it — three or more
# characters of digits and thousands separators, optionally bracketed.
# "decreased 1 basis point", "31 December 2025" and "Tier 1 and Tier 2" all
# fail the last condition.
#
# The same-line condition is the fourth, and it exists because a PDF text layer
# puts every column of a table on its own line. ANZ's 1H26 results announcement
# p59 reads "Credit and Capital Markets \n \n80 \n102 \n114"; under a run that
# crossed newlines the 80 was a "marker", and the quote "Credit and Capital
# Markets 102 114" was accepted as verbatim while dropping the current period
# and presenting 102 as the first column. Measured over all 30 corpus documents
# and 3,546 pages, the newline-crossing run removed 1,670 tokens; holding the
# run to the label's own line removes 779 and takes the whole column class with
# it. A footnote marker the reader sees between a label and its value is on the
# label's line by construction.
_MARKER_RE = re.compile(r"(?<=[A-Za-z])((?:[ \t]+\d{1,2})+)(?=\s+\(?[\d,]{3,})")
# A superscript digit is a marker wherever it stands: no page prints a value in
# superscript. "Restructuring and notable items ¹" is the whole row label.
_SUPERSCRIPT_MARKER_RE = re.compile(r"[¹²³⁰-⁹]+")


def strip_markers(text: str) -> str:
    """The page as a reader sees it, with interleaved footnote markers gone."""
    return _MARKER_RE.sub(" ", _SUPERSCRIPT_MARKER_RE.sub(" ", str(text or "")))


MARKER_RELAXATION = (
    "quote_match:markers_stripped — matched this page once its interleaved "
    "footnote markers were removed"
)


def match_quote(quote: str, text: str) -> tuple[bool, str]:
    """Is this quote on this page, and under which test?

    Returns (matched, relaxation). The strict test compares the characters
    themselves. The second test removes footnote markers from the PAGE only,
    never from the quote: that lets a quote OMIT a marker the page prints,
    while still refusing a quote that STATES a number the page does not.
    Relaxing both sides would erase every one- and two-digit number from the
    comparison, so "the margin fell 5 basis points" would match a page saying 3.
    """
    key = quote_key(quote)
    if key in quote_key(text):
        return True, ""
    if key in quote_key(strip_markers(text)):
        return True, MARKER_RELAXATION
    return False, ""


def quote_key(text: str) -> str:
    """The comparable form of a quote: no whitespace, one spelling per mark.

    Whitespace is dropped rather than collapsed because a PDF text layer breaks
    a table row wherever the column gaps fall, and era pages split a number
    across a space ("47. 0"). Dropping it compares the characters themselves,
    in order, which is what "verbatim" means on a page whose layout the reader
    cannot see. Case is ignored: a text layer re-cases small-caps headings.
    """
    return "".join(
        ch for ch in str(text or "").translate(_PUNCTUATION).lower() if not ch.isspace()
    )


