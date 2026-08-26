"""Evidence extraction: cheap model over retrieved pages; vision over walk
charts (ADR-0002). Provenance is stamped by code, never by the model."""

from __future__ import annotations

import re

from .corpus import Document
from .llm import LLM
from .schema import EvidenceRecord, NumberFact

TEXT_PROMPT = """You extract evidence for bank equity research. Today's task: {case}.

Below is the text of one page from {doc_desc}. Extract every fact on this page
relevant to the task as JSON only:

[{{"quote": "<verbatim quote from the page, 50 words maximum>",
   "numbers": [{{"label": "<what the number is>", "value": <float>,
                "unit": "<bps|$m|%|ppt|ratio>",
                "basis": "<cash|statutory|ex_notables|null>"}}],
   "kind": "<text|table>"}}]

Rules:
- Quotes must be VERBATIM from the page text. Never paraphrase inside "quote".
- Extract only what is on this page. If nothing is relevant, return [].
- Percentages: keep the unit "%" and the printed value (2.05% -> value 2.05).
- Negative values in parentheses are negative numbers.
- At most 6 records for this page; prefer tables and quantified statements.

PAGE TEXT:
{page_text}"""

WALK_PROMPT = """This bank results page contains a waterfall (walk) chart relevant to: {case}.
Extract the walk as JSON only:
{{"title": "<chart title>", "start_label": str, "start_bps": float,
  "bars": [{{"label": str, "bps": float}}], "end_label": str, "end_bps": float}}
Rules: values in basis points (2.08% = 208 bps; a chart labelled bpts is already
bps). Bars in parentheses are negative. A dash bar is 0. Keep the chart's bar
order. Use only what is on this page."""


PRESENTATION_DOC_TYPES = ("results_presentation", "investor_presentation", "investor_discussion_pack")


def printed_page_of(text: str, pdf_page: int, doc_type: str = "") -> int | None:
    """Bank documents print the page number in the footer line. Presentations
    number by slide, which tracks the PDF page (defect 21), so use that; for
    books, a footer number implausibly far from the PDF page is a misparse."""
    if doc_type in PRESENTATION_DOC_TYPES:
        return pdf_page
    for line in text.splitlines()[-4:] + text.splitlines()[:2]:
        match = re.match(r"^\s*(\d{1,3})\s*$|^\s*(\d{1,3})\s{2,}", line)
        if match:
            printed = int(match.group(1) or match.group(2))
            # Front matter offsets run to ~16 pages (CBA); beyond 25 the
            # "page number" is almost certainly table data, not a footer.
            if 0 < pdf_page - printed <= 25:
                return printed
    return None


def extract_text_evidence(
    llm: LLM, model: str, doc: Document, page_no: int, case: str, next_id
) -> list[EvidenceRecord]:
    text = doc.page_texts()[page_no - 1]
    if not text.strip():
        return []
    raw = llm.chat_json(
        model,
        TEXT_PROMPT.format(case=case, doc_desc=doc.doc_id, page_text=text[:8000]),
        max_tokens=3000,
    )
    records = []
    for item in raw if isinstance(raw, list) else []:
        try:
            records.append(
                EvidenceRecord(
                    id=next_id(),
                    doc_id=doc.doc_id,
                    pdf_page=page_no,
                    printed_page=printed_page_of(text, page_no, doc.doc_type),
                    kind=item.get("kind", "text"),
                    quote=str(item.get("quote", ""))[:600],
                    numbers=[NumberFact(**n) for n in item.get("numbers", []) if "value" in n],
                )
            )
        except Exception:  # noqa: BLE001 - a malformed record is dropped, not fatal
            continue
    return records


def extract_walk(llm: LLM, model: str, doc: Document, page_no: int, case: str, next_id):
    """Vision read of a walk chart page. Returns (walk_dict, EvidenceRecord)."""
    png = doc.render_page(page_no)
    try:
        walk = llm.chat_json(model, WALK_PROMPT.format(case=case), image_png=png, max_tokens=3000)
    except ValueError:
        # One retry: vision replies occasionally truncate or mangle JSON.
        walk = llm.chat_json(model, WALK_PROMPT.format(case=case), image_png=png, max_tokens=3000)
    # A null bar value is a partial read, not a crash (defect 23): drop the
    # bar and record the gap on the walk.
    bars = walk.get("bars", [])
    walk["bars"] = [b for b in bars if b.get("bps") is not None]
    if len(walk["bars"]) < len(bars):
        walk["dropped_bars"] = [b.get("label") for b in bars if b.get("bps") is None]
    for key in ("start_bps", "end_bps"):
        if walk.get(key) is None:
            raise ValueError(f"walk endpoints unreadable on {doc.doc_id} p{page_no}")
    text = doc.page_texts()[page_no - 1]
    record = EvidenceRecord(
        id=next_id(),
        doc_id=doc.doc_id,
        pdf_page=page_no,
        printed_page=printed_page_of(text, page_no, doc.doc_type),
        kind="walk_vision",
        quote=f"[walk chart] {walk.get('title', '')}: {walk.get('start_label')} "
        f"{walk.get('start_bps')} -> {walk.get('end_label')} {walk.get('end_bps')}",
        numbers=[
            NumberFact(label=bar.get("label", "?"), value=float(bar.get("bps", 0)), unit="bps")
            for bar in walk.get("bars", [])
        ],
    )
    return walk, record
