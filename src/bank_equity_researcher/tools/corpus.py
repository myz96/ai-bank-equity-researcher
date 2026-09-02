"""Corpus access: manifests, cached page text, page rendering, and which
documents one task is allowed to read."""

from __future__ import annotations

import json
import re
from functools import cache, lru_cache
from pathlib import Path

import pymupdf

from ..config import DATA_DIR, MANIFEST_DIR, REGISTRY_DIR


class Document:
    def __init__(self, bank: str, meta: dict) -> None:
        self.bank = bank
        self.period: str = meta["period"]
        self.doc_type: str = meta["doc_type"]
        self.filename: str = meta["filename"]
        self.sha256: str | None = meta.get("sha256")
        self.path = DATA_DIR / "raw" / bank / self.period / self.filename

    @property
    def doc_id(self) -> str:
        return f"{self.bank}/{self.period}/{self.doc_type}"

    def page_texts(self) -> list[str]:
        # CACHE-KEY INVARIANT: the page-text cache here and the embedding cache
        # in retrieve.py are both keyed by the FILENAME STEM, so two documents
        # that share a stem share a cache entry, and one bank's pages would be
        # served for another's. The manifests hold this by convention — every
        # filename is "BANK-PERIOD-doctype.pdf" and the stems stay distinct —
        # but nothing in code enforces it, and discover.py copies a filename
        # straight out of a model reply, where a generic basename such as
        # "results-announcement.pdf" is exactly what an IR page offers.
        # _assert_distinct_stems turns a collision into an error on every load
        # path. Neither cache invalidates on content change,
        # so a PDF replaced in place keeps serving its old text.
        cache = DATA_DIR / "cache" / "pages" / (Path(self.filename).stem + ".json")
        if cache.exists():
            return json.loads(cache.read_text())
        pdf = pymupdf.open(self.path)
        texts = [page.get_text() for page in pdf]
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(texts))
        return texts

    def render_page(self, page_no: int, zoom: float = 2.0) -> bytes:
        """page_no is 1-based PDF page number."""
        pdf = pymupdf.open(self.path)
        return pdf[page_no - 1].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom)).tobytes("png")


@lru_cache(maxsize=1)
def _assert_distinct_stems() -> None:
    """Refuse a stem collision on EVERY load path, not only doc_alias_index.

    Reads the manifests, not Document objects, so it cannot recurse into
    load_documents.
    """
    stems: dict[str, str] = {}
    for bank in manifest_banks():
        manifest = json.loads((MANIFEST_DIR / f"{bank.lower()}.json").read_text())
        for meta in manifest["documents"]:
            stem = Path(meta["filename"]).stem
            doc_id = f"{manifest['bank']}/{meta['period']}/{meta['doc_type']}"
            if stems.get(stem, doc_id) != doc_id:
                raise RuntimeError(
                    f"{doc_id} and {stems[stem]} share the filename stem {stem!r}; "
                    "the page-text and embedding caches are keyed by that stem, so "
                    "one bank's pages would be served for the other's"
                )
            stems[stem] = doc_id


@cache
def load_documents(bank: str) -> list[Document]:
    manifest_path = MANIFEST_DIR / f"{bank.lower()}.json"
    if not manifest_path.exists():
        return []
    _assert_distinct_stems()
    manifest = json.loads(manifest_path.read_text())
    docs = [Document(manifest["bank"], meta) for meta in manifest["documents"]]
    return [d for d in docs if d.path.exists() and d.path.suffix == ".pdf"]


def documents_for_period(bank: str, *periods: str) -> list[Document]:
    return [d for d in load_documents(bank) if d.period in periods]


def manifest_banks() -> list[str]:
    """Every bank the manifests cover, by ticker."""
    return sorted(path.stem.upper() for path in MANIFEST_DIR.glob("*.json"))


def all_documents() -> list[Document]:
    return [doc for bank in manifest_banks() for doc in load_documents(bank)]


# ---------------------------------------------------------------------------
# Which documents a free-form question may read.
#
# A metric case names its bank and its two periods, so its corpus is given. A
# question names them in prose, so the scope is read out of the question with
# the vocabulary the registry already holds: the ticker, and the distinctive
# word of the bank's full name. Nothing here is specific to one bank or to one
# document shape.
# ---------------------------------------------------------------------------

# Words that name no bank on their own: every Australian bank's legal name is
# built from them, so a match on one of them identifies nothing.
_GENERIC_NAME_WORDS = {
    "australia", "australian", "bank", "banking", "corporation", "group",
    "holdings", "limited", "ltd", "national", "of", "the",
}

_PERIOD_RE = re.compile(r"\b(FY|1H|2H)\s?(?:20)?(\d{2})\b", re.IGNORECASE)


@lru_cache(maxsize=1)
def bank_name_words() -> dict[str, str]:
    """Distinctive lower-case name words -> ticker, from the registry."""
    words: dict[str, str] = {}
    for bank in manifest_banks():
        path = REGISTRY_DIR / f"{bank.lower()}.json"
        if not path.exists():
            continue
        full_name = str(json.loads(path.read_text()).get("full_name") or "")
        for word in re.findall(r"[A-Za-z]+", full_name):
            if word.lower() not in _GENERIC_NAME_WORDS:
                words[word.lower()] = bank
    return words


@lru_cache(maxsize=1)
def bank_name_phrases() -> dict[str, str]:
    """Full names as written -> ticker, for the names built ONLY from generic
    words.

    "National Australia Bank" is three words, and every one of them names some
    Australian bank, so the distinctive-word index holds nothing for NAB. A
    phrase is distinctive where its words are not, so the whole name is matched
    too. This reads the registry like everything else here: no bank is named in
    code.
    """
    phrases: dict[str, str] = {}
    for bank in manifest_banks():
        path = REGISTRY_DIR / f"{bank.lower()}.json"
        if not path.exists():
            continue
        full_name = str(json.loads(path.read_text()).get("full_name") or "").strip()
        if full_name:
            phrases[full_name.lower()] = bank
    return phrases


def banks_named(text: str) -> list[str]:
    """The banks a question names, in the order it names them.

    A ticker matches case-sensitively, because "nab" is an English verb and
    "anz" is not a word at all; a name word or a full name matches
    case-insensitively.
    """
    found: list[tuple[int, str]] = []
    for bank in manifest_banks():
        match = re.search(rf"\b{bank}\b", text or "")
        if match:
            found.append((match.start(), bank))
    for word, bank in bank_name_words().items():
        match = re.search(rf"\b{word}\b", text or "", re.IGNORECASE)
        if match and bank not in [b for _, b in found]:
            found.append((match.start(), bank))
    for phrase, bank in bank_name_phrases().items():
        pattern = r"\b" + r"\s+".join(re.escape(w) for w in phrase.split()) + r"\b"
        match = re.search(pattern, text or "", re.IGNORECASE)
        if match and bank not in [b for _, b in found]:
            found.append((match.start(), bank))
    return [bank for _, bank in sorted(found)]


# "from FY21 to FY26", "FY21-FY26", "between FY21 and FY26": a RANGE names
# every year inside it. Parsing only the endpoints handed a six-year question
# two years' documents, and the agent could never cite the middle (the
# longitudinal crossref case missed 4 of 6 required pages by construction).
# "and" separates a range only under "between": "compare FY21 and FY26"
# names two years, not six.
_PERIOD_RANGE_RE = re.compile(
    r"\bFY\s?(?:20)?(\d{2})\s*(?:-|–|—|to|through)\s*FY\s?(?:20)?(\d{2})\b"
    r"|\bbetween\s+FY\s?(?:20)?(\d{2})\s+and\s+FY\s?(?:20)?(\d{2})\b",
    re.IGNORECASE,
)


def periods_named(text: str) -> list[str]:
    """The reporting periods a question names; a range's endpoints come in
    the question's own order, then the expanded years between them."""
    seen: list[str] = []
    for prefix, year in _PERIOD_RE.findall(text or ""):
        period = f"{prefix.upper()}{year}"
        if period not in seen:
            seen.append(period)
    for a, b, c_, d in _PERIOD_RANGE_RE.findall(text or ""):
        start, end = (a, b) if a else (c_, d)
        lo, hi = int(start), int(end)
        # "FY99 to FY01" crosses the century: read it modulo 100 so the
        # interior year still expands. A span wider than 15 years is a
        # misparse, never a real question; a decade-long study is real.
        if hi < lo:
            hi += 100
        if hi - lo <= 15:
            for year in range(lo, hi + 1):
                period = f"FY{year % 100:02d}"
                if period not in seen:
                    seen.append(period)
    return seen


def period_sort_key(period: str) -> tuple[int, int]:
    """Newest last. A full year ends with its second half, so FY25 > 1H25."""
    match = re.fullmatch(r"(FY|1H|2H)(\d{2})", str(period).upper())
    if not match:
        return (0, 0)
    return (int(match.group(2)), 1 if match.group(1) == "1H" else 2)


def latest_period(bank: str) -> str | None:
    periods = {doc.period for doc in load_documents(bank)}
    return max(periods, key=period_sort_key) if periods else None


def documents_for_question(
    question: str,
    bank: str | None = None,
    periods: list[str] | None = None,
    notes: list[str] | None = None,
) -> list[Document]:
    """The documents one question may read.

    `bank` and `periods` are hints from a caller that already knows them; when
    they are absent the question's own words decide. A period the manifest does
    not hold is dropped rather than refused: a question about FY26 guidance is
    answered out of the FY25 documents that publish it.

    A silent substitution would read as though the answer came from the period
    the reader asked about. `notes` collects one line per substitution, and the
    caller puts those lines in the answer's limitations.
    """
    banks = [bank.upper()] if bank else banks_named(question)
    if not banks:
        raise RuntimeError(
            "the question names no bank in the corpus; name one of "
            f"{', '.join(manifest_banks())} in the question or pass --bank"
        )
    wanted = list(periods or []) or periods_named(question)
    docs: list[Document] = []
    for name in banks:
        available = load_documents(name)
        held = [p for p in wanted if any(d.period == p for d in available)]
        missing = [p for p in wanted if p not in held]
        if not held:
            held = [p for p in [latest_period(name)] if p]
        if missing and notes is not None:
            notes.append(
                f"The corpus holds no {name} document for "
                f"{', '.join(missing)}; this answer was researched in "
                f"{', '.join(held) or 'no document'} instead."
            )
        docs += [d for d in available if d.period in held]
    return docs


# ---------------------------------------------------------------------------
# Document names as a human writes them.
#
# A doc_id is "BANK/PERIOD/doc_type"; a person writing about the same document
# uses the file's own name ("WBC/FY25/presentation-and-IDP") or hyphenates the
# type ("NAB/FY25/investor-presentation"). Both spellings resolve here, so no
# caller has to keep a table of nicknames.
# ---------------------------------------------------------------------------


def _doc_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(text or "").lower()).strip("-")


def doc_alias_index(documents: list[Document] | None = None) -> dict[str, str]:
    """Every spelling of a document's name that resolves to its doc_id."""
    index: dict[str, str] = {}
    for doc in all_documents() if documents is None else documents:
        stem = Path(doc.filename).stem
        trimmed = re.sub(rf"^{doc.bank}[-_]{doc.period}[-_]", "", stem, flags=re.IGNORECASE)
        for name in (doc.doc_id, f"{doc.bank}/{doc.period}/{stem}",
                     f"{doc.bank}/{doc.period}/{trimmed}"):
            index.setdefault(_doc_key(name), doc.doc_id)
    return index


def resolve_doc_name(name: str, index: dict[str, str]) -> str | None:
    """The doc_id one written document name means, or None when it is unclear.

    An exact alias decides on its own. Otherwise the containment pass needs the
    written name to agree with the document's BANK and PERIOD: a bare
    "results-book" is inside exactly one alias whenever one bank happens to
    file its book under that word. A name that does not say which bank it means
    is unclear, and unclear returns None.
    """
    key = _doc_key(name)
    if not key:
        return None
    if key in index:
        return index[key]
    tokens = set(key.split("-"))
    matches = set()
    for alias, doc_id in index.items():
        if not (key in alias or alias in key):
            continue
        doc_bank, doc_period, _ = doc_id.split("/", 2)
        if _doc_key(doc_bank) in tokens and _doc_key(doc_period) in tokens:
            matches.add(doc_id)
    return matches.pop() if len(matches) == 1 else None
