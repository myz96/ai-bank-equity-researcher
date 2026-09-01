"""Deterministic reference-following, behind the follow_references tool.

Retrieval ranks a page by how much the page looks like the question. The
why-layer of a bank result does not look like the question: it sits in appendix
notes, on footnote targets and on continuation pages that the metric's own
words never name. A human analyst reaches those pages by FOLLOWING A
REFERENCE — reading "refer Note 2.2" beside the income statement line and
turning to it.

This module is that turn, written as code. No model is involved and no page is
scored by a model: one regex pass builds a notes index per document, and a
second pass resolves the reference markers on one named page to their target
pages. A case therefore replays identically.

Three marker kinds are followed, in this priority order:

a. a note reference — "Note 2.2", "refer to Appendix 6.2", or the note heading
   printed on the page itself ("2.2 Provisions for Impairment (continued)"),
   resolved against the notes index to every page the note occupies;
b. a page reference — "refer to page 21", "(page 106)", "Refer to slide 64",
   resolved through the document's own printed-page numbering;
c. a footnote reference — a footnote line that names another note by its title.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .corpus import Document

# A note that runs longer than this is a chapter, not a note; reading all of it
# would spend the whole cap on one reference.
MAX_PAGES_PER_NOTE = 4
# A note heading sits at the top of its page. Deeper down, "2.2" is a ratio in
# a table, not a heading (a divisional table prints dozens of them).
_HEADING_MAX_LINE = 20
# A page carrying this many note headings is the contents page, so it locates
# nothing: it lists where the notes are, and every id on it would otherwise
# resolve to the contents page itself.
_INDEX_PAGE_HEADINGS = 3
# Front matter and section dividers push the printed number behind the PDF
# number; beyond this the "page number" is table data, not a footer.
_MAX_PRINTED_OFFSET = 40
# How far into a target page the relevance probe reads. The running header and
# the printed page number occupy the first lines of every book page.
_TARGET_PROBE_LINES = 20
# Note ids run 1.1 to 12.99. A wider pattern swallows ratios ("17.73"), share
# counts and percentages printed alone on a line.
_NOTE_ID = r"(?:[1-9]|1[0-2])\.\d{1,2}"
_HEADING_SAME_LINE = re.compile(rf"^\s*({_NOTE_ID})[.:)]?\s+(\S.*?)\s*$")
_HEADING_ID_ONLY = re.compile(rf"^\s*({_NOTE_ID})[.:)]?\s*$")
_CONTINUED = re.compile(r"\s*\((?:continued|cont\.?|cont'd)\)\s*$", re.IGNORECASE)

# "Note 2.2" / "refer to Appendix 6.2". "Notes" and "Appendices" are the plural
# headings banks print above a reference COLUMN, so they are matched too.
_REF_NOTE = re.compile(rf"(?i)\b(?:notes?|appendix|appendices)\s+({_NOTE_ID})\b")
# "refer to page 21", "(page 106)", "Refer to slide 64", "pages 33-34".
_REF_PAGE = re.compile(r"(?i)\b(?:pages?|slides?)\s+(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?\b")
# A page number only counts as a REFERENCE when a referring word introduces it;
# otherwise "page" is part of a sentence about something else.
_REFERRING = re.compile(
    r"(?i)(refer|see|shown|set out|detail|discussed|described|further information|"
    r"disclos|reported|presented|analys)"
)
# A results book prints its note references in a narrow column headed "Note" or
# "Appendix", so the marker beside the income-statement row is the bare number.
# The text layer puts that heading on a line of its own.
_REF_COLUMN_HEADER = re.compile(r"(?im)^\s*(?:notes?|appendix|appendices|ref|reference)\s*$")
_BARE_ID_LINE = re.compile(rf"^\s*({_NOTE_ID})\s*$")
# A reference into ANOTHER document resolves nowhere in this corpus, and the
# same note number means something different there.
_EXTERNAL = re.compile(
    r"(?i)annual report|pillar 3|prospectus|sustainability report|"
    r"corporate governance|financial report of"
)
# A footnote line: "3. Refer to slide 64 ...", "1 Net other operating income ...".
_FOOTNOTE_LINE = re.compile(r"^\s*(?:\d{1,2}|[¹²³⁴-⁹])[.)]?\s+(\S.*)$")

# Page-number candidates: a footer number sits at the start or the end of a
# header/footer line, separated from the running title by wide whitespace.
_FOOTER_START = re.compile(r"^\s{0,4}(\d{1,3})(?:\s{2,}|\s*$)")
_FOOTER_END = re.compile(r"\s{2,}(\d{1,3})\s*$")

_STOPWORDS = frozenset(
    ["a", "an", "and", "or", "the", "of", "for", "to", "in", "on", "at", "by", "with", "from", "as", "is", "are", "was", "were", "be", "been", "its", "it", "this", "that", "these", "those", "group", "total", "net", "other", "movement", "movement's", "analysis", "basis", "points", "per", "cent"]
)

_notes_cache: dict[str, dict[str, Note]] = {}
_printed_cache: dict[str, dict[int, int]] = {}


@dataclass(frozen=True)
class Note:
    """One numbered note or appendix, and every PDF page it occupies."""

    note_id: str
    title: str
    pages: tuple[int, ...]


@dataclass(frozen=True)
class Reference:
    """A marker found on a selected page, already resolved to target pages."""

    doc_id: str
    source_page: int
    tier: int  # 0 = note, 1 = page, 2 = footnote
    target: str  # human-readable name of what was followed
    pages: tuple[int, ...]
    relevance: int = 0


def relevance_terms(text: str) -> set[str]:
    """The token set scan_page matches reference targets against: the public
    form of _words, so no caller reaches into a private helper to agree with
    it on tokenisation."""
    return _words(text)


def _words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{3,}", text.lower())} - _STOPWORDS


def _is_title(text: str) -> bool:
    """True when the text reads like a note heading rather than a table row."""
    text = _CONTINUED.sub("", text).strip()
    if not text or not text[0].isupper():
        return False
    if len(text) > 90:
        return False
    words = text.split()
    if len(words) < 2 or len(words) > 12:
        return False
    return sum(ch.isdigit() for ch in text) <= 2


def _page_headings(text: str, max_line: int | None = _HEADING_MAX_LINE) -> list[tuple[str, str, bool]]:
    """Note headings on one page: (id, title, continued).

    `max_line` bounds how far down the page a heading may sit. The bound is
    lifted only when reading a contents page, whose entries run the full page.
    """
    found: list[tuple[str, str, bool]] = []
    lines = text.splitlines() if max_line is None else text.splitlines()[: max_line + 4]
    for i, line in enumerate(lines):
        if max_line is not None and i > max_line:
            break
        match = _HEADING_SAME_LINE.match(line)
        title = match.group(2) if match else None
        if title is None:
            match = _HEADING_ID_ONLY.match(line)
            if not match:
                continue
            # Banks lay the number and the title on separate lines; the text
            # layer keeps that split.
            title = next((n.strip() for n in lines[i + 1 : i + 3] if n.strip()), "")
        if not _is_title(title):
            continue
        found.append(
            (match.group(1), _CONTINUED.sub("", title).strip(), bool(_CONTINUED.search(title)))
        )
    return found


def notes_index(doc: Document) -> dict[str, Note]:
    """Map every numbered note in a document to the pages it occupies.

    Built once per document from the text layer alone, in two passes. The first
    pass reads the contents pages — a page that lists three or more numbered
    notes — and keeps the note ids the document itself declares. The second pass
    locates each declared note by its heading.

    The declaration pass is what keeps the index honest. Slides print "1.9" and
    "12.5" as chart labels above two-word captions, and a results book prints
    ratios in the same shape; only a document with a real contents page has real
    notes, so a document without one yields an empty index and follows no note
    reference at all.
    """
    key = str(doc.path)
    if key in _notes_cache:
        return _notes_cache[key]
    texts = doc.page_texts()
    declared: dict[str, str] = {}
    contents_pages: set[int] = set()
    for page_no, text in enumerate(texts, 1):
        listed = _page_headings(text, max_line=None)
        if len({note_id for note_id, _, _ in listed}) < _INDEX_PAGE_HEADINGS:
            continue
        contents_pages.add(page_no)
        for note_id, title, _ in listed:
            declared.setdefault(note_id, title)
    pages: dict[str, list[int]] = {}
    titles: dict[str, str] = dict(declared)
    for page_no, text in enumerate(texts, 1):
        if page_no in contents_pages:
            continue
        for note_id, title, continued in _page_headings(text):
            if note_id not in declared:
                continue
            pages.setdefault(note_id, []).append(page_no)
            if not continued:
                titles[note_id] = title
    index = {
        note_id: Note(note_id, titles.get(note_id, ""), tuple(sorted(set(page_list))))
        for note_id, page_list in pages.items()
    }
    _notes_cache[key] = index
    return index


def printed_page_map(doc: Document) -> dict[int, int]:
    """Map the page number a document PRINTS to its PDF page number.

    Banks reference each other's pages by the printed number, which trails the
    PDF number by an offset that CHANGES at every section divider. A candidate
    is kept only when a neighbouring page carries the next or previous printed
    number, so an isolated number in a table never becomes a page mapping.
    """
    key = str(doc.path)
    if key in _printed_cache:
        return _printed_cache[key]
    texts = doc.page_texts()
    candidates: list[set[int]] = []
    for text in texts:
        lines = text.splitlines()
        found: set[int] = set()
        for line in lines[:6] + lines[-6:]:
            match = _FOOTER_START.match(line)
            if match:
                found.add(int(match.group(1)))
            match = _FOOTER_END.search(line)
            if match:
                found.add(int(match.group(1)))
        candidates.append(found)
    mapping: dict[int, int] = {}
    for i, found in enumerate(candidates):
        for printed in sorted(found):
            offset = (i + 1) - printed
            if not 0 <= offset <= _MAX_PRINTED_OFFSET:
                continue
            neighboured = (i > 0 and (printed - 1) in candidates[i - 1]) or (
                i + 1 < len(candidates) and (printed + 1) in candidates[i + 1]
            )
            if neighboured:
                mapping.setdefault(printed, i + 1)
    _printed_cache[key] = mapping
    return mapping


def _external(text: str, start: int, end: int) -> bool:
    """True when the words around a marker name a different document."""
    return bool(_EXTERNAL.search(text[max(0, start - 60) : end + 90]))


def _target_words(doc: Document, page: int) -> set[str]:
    """The opening words of a target page, for relevance ranking.

    The first lines of a book page are the running header and the printed page
    number, so the probe reaches far enough down to meet the section title and
    the first table rows, and stops before the page's footnotes.
    """
    texts = doc.page_texts()
    if not 1 <= page <= len(texts):
        return set()
    lines = [line.strip() for line in texts[page - 1].splitlines() if line.strip()]
    return _words(" ".join(lines[:_TARGET_PROBE_LINES]))


def scan_page(
    doc: Document, page_no: int, terms: set[str], index: dict[str, Note] | None = None
) -> list[Reference]:
    """Find every reference marker on one page and resolve it to target pages."""
    texts = doc.page_texts()
    if not 1 <= page_no <= len(texts):
        return []
    text = texts[page_no - 1]
    index = notes_index(doc) if index is None else index
    printed = printed_page_map(doc)
    found: list[Reference] = []
    seen: set[str] = set()

    def add(tier: int, target: str, pages: tuple[int, ...], relevance: int) -> None:
        pages = tuple(p for p in pages if 1 <= p <= len(texts))
        if not pages or target in seen:
            return
        seen.add(target)
        found.append(Reference(doc.doc_id, page_no, tier, target, pages, relevance))

    def note_target(note_id: str) -> None:
        note = index.get(note_id)
        if note is None:
            return
        add(
            0,
            f"Note {note.note_id} {note.title}".strip(),
            note.pages[:MAX_PAGES_PER_NOTE],
            len(_words(note.title) & terms),
        )

    # (a) Note references, written out or printed in a reference column.
    for match in _REF_NOTE.finditer(text):
        if not _external(text, match.start(), match.end()):
            note_target(match.group(1))
    # (a) The bare number in a reference column. An income statement points at
    # its note with the number alone, under a column headed "Note". Only a
    # number the document declared as a note resolves, so a ratio printed in the
    # same shape stays a ratio.
    if _REF_COLUMN_HEADER.search(text):
        for line in text.splitlines():
            match = _BARE_ID_LINE.match(line)
            if match:
                note_target(match.group(1))
    # (a) The note heading on the page itself. A selected page that IS part of a
    # note points at the rest of that note: the table continues over the page
    # break, and half a note is half an answer.
    for note_id, _, _ in _page_headings(text):
        note_target(note_id)

    # (b) Page references, resolved through the document's printed numbering.
    for match in _REF_PAGE.finditer(text):
        before = text[max(0, match.start() - 90) : match.start()]
        if not _REFERRING.search(before) or _external(text, match.start(), match.end()):
            continue
        first = int(match.group(1))
        last = int(match.group(2)) if match.group(2) else first
        if last < first or last - first > 3:
            last = first
        for number in range(first, last + 1):
            target_page = printed.get(number)
            if target_page is None or target_page == page_no:
                continue
            add(1, f"page {number}", (target_page,), len(_target_words(doc, target_page) & terms))

    # (c) Footnote lines that name another note by its title.
    for line in text.splitlines():
        match = _FOOTNOTE_LINE.match(line)
        if not match:
            continue
        body = match.group(1).lower()
        for note in index.values():
            if len(note.title.split()) >= 3 and note.title.lower() in body:
                add(
                    2,
                    f"Note {note.note_id} {note.title}".strip(),
                    note.pages[:MAX_PAGES_PER_NOTE],
                    len(_words(note.title) & terms),
                )
    return found


__all__ = [
    "Note",
    "Reference",
    "notes_index",
    "printed_page_map",
    "scan_page",
]
