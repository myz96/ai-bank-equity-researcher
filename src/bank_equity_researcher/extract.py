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
- TABLES: emit one record per relevant row. quote = the row label with its
  printed values (e.g. "Net interest income 25,586 24,023 7"). numbers = one
  entry per period column with the period in the label (e.g. "NII FY26",
  "NII FY25"). A heading alone is NOT a record.
- COLUMN ORDER: read the column headers printed above the table (e.g.
  "31 Dec 25 | 30 Jun 25 | 31 Dec 24"). A row's values follow that order.
  Emit ONE number per period column - ALL of them, never only the first two -
  and label each with that column's own printed period ("ROE cash 31 Dec 24").
  A half-year table's second column is the PRIOR HALF and its third column is
  the same half one year earlier; never relabel the second column as the prior
  year. Columns headed like "Dec 25 vs Dec 24 %" are CHANGES, not levels:
  label them as the change, name both periods, and keep the sign.
- A performance-summary table (income, expenses, impairment, tax, profit rows)
  is the highest-value content: cover EVERY line row with both period columns,
  before anything else on the page.
- MOVEMENT STATEMENTS: when the text states a change (e.g. "increased $62
  million or 9% to $788 million"), keep the full statement in the quote and
  emit BOTH the signed delta (e.g. +62) and the level (788) as numbers.
- DIVISIONAL DETAIL: rows or bullets that break the task's metric down by
  division, segment, or product are core evidence, not background — extract
  each one with both period columns (and any stated change).
- BASIS: fill "basis" ONLY when the row, its heading or the table title prints
  the word itself - cash, statutory, underlying, ex-notable. When the page
  prints no such word beside the number, return null. Never infer a basis from
  where the table sits or from the fact that the figure is audited: a guessed
  basis is read downstream as the bank's own label.
- Extract only what is on this page. If nothing is relevant, return [].
- Percentages: keep the unit "%" and the printed value (2.05% -> value 2.05).
- Negative values in parentheses are negative numbers.
- At most 10 records for this page; prefer table rows and quantified statements.

PAGE TEXT:
{page_text}"""

WALK_PROMPT = """This bank results page contains a waterfall (walk/bridge) chart relevant to: {case}.
Extract the walk as JSON only:
{{"title": "<chart title>", "start_label": str, "start_bps": float,
  "bars": [{{"label": str, "bps": float}}], "end_label": str, "end_bps": float}}
Rules: ALL values in {unit}. When the unit is bps, convert percentages fully
(2.08% = 208 bps, 12.3% = 1230 bps; a chart labelled bpts is already bps).
When the unit is $m, keep dollar-million values as printed. Bars in
parentheses are negative. A dash bar is 0. Keep the chart's bar order. Use
only what is on this page.
ENDPOINT LABELS: copy start_label and end_label VERBATIM from the two end
columns of the chart (for example "Dec 24 Half", "Jun 25 Level 2", "FY25").
Never write the task's periods there: code reads these labels to decide which
comparison the chart describes, so an invented label misfiles the chart.
BARS: the "bars" list holds ONLY the movement columns between the two
endpoints. Never repeat the start or end column as a bar."""


PRESENTATION_DOC_TYPES = ("results_presentation", "investor_presentation", "investor_discussion_pack")


def _label_key(label) -> str:
    """Case- and punctuation-insensitive form of a chart label, for comparing
    a bar's label against the chart's endpoint labels."""
    return "".join(ch for ch in str(label or "").lower() if ch.isalnum())


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


def extract_walk(llm: LLM, model: str, doc: Document, page_no: int, case: str, next_id, unit: str = "bps"):
    """Vision read of a walk chart page. Returns (walk_dict, EvidenceRecord)."""
    prompt = WALK_PROMPT.format(case=case, unit=unit)
    # The parse-failure retry now lives in LLM.chat_json, so every JSON caller
    # gets it (ticket 27). The budget stays at the retry's old ceiling.
    try:
        walk = llm.chat_json(model, prompt, image_png=doc.render_page(page_no), max_tokens=4000)
    except ValueError:
        # Last resort for a page that keeps coming back unreadable: send a
        # bigger render. Diagnosis on the CBA FY25 PA p28 NIM chart says the
        # failure is a truncated reply, not a rendering problem, so this only
        # adds a second axis of variation after the retries above are spent.
        walk = llm.chat_json(
            model, prompt, image_png=doc.render_page(page_no, zoom=3.0), max_tokens=4000
        )
    # A null bar value is a partial read, not a crash (defect 23): drop the
    # bar and record the gap on the walk.
    bars = walk.get("bars", [])
    walk["bars"] = [b for b in bars if b.get("bps") is not None]
    if len(walk["bars"]) < len(bars):
        walk["dropped_bars"] = [b.get("label") for b in bars if b.get("bps") is None]
    # Endpoint-as-a-bar: the vision reader sometimes repeats the chart's final
    # column as a last bar (CBA FY26 PA p28 emitted "Jun 26 Full Year: 205"
    # beside its real bars, and the walk_sum check then failed by +205). Only
    # a bar whose LABEL is an endpoint label is dropped, so a real bar that
    # happens to equal an endpoint value survives.
    endpoint_labels = {
        _label_key(walk.get("start_label")), _label_key(walk.get("end_label"))
    } - {""}
    kept = [b for b in walk["bars"] if _label_key(b.get("label")) not in endpoint_labels]
    if len(kept) < len(walk["bars"]):
        walk["endpoint_bars_dropped"] = [
            b.get("label") for b in walk["bars"] if _label_key(b.get("label")) in endpoint_labels
        ]
        walk["bars"] = kept
    for key in ("start_bps", "end_bps"):
        if walk.get(key) is None:
            raise ValueError(f"walk endpoints unreadable on {doc.doc_id} p{page_no}")
    # Endpoint scale harmoniser: vision sometimes converts endpoints and bars
    # at different scales (12.3% -> 123 with bars in true bps). If one scale
    # factor on the endpoints makes the walk sum, apply and record it.
    bar_sum = sum(b["bps"] for b in walk["bars"])
    if abs(walk["start_bps"] + bar_sum - walk["end_bps"]) > 10:
        for factor in (10.0, 100.0, 0.1, 0.01):
            s, e = walk["start_bps"] * factor, walk["end_bps"] * factor
            if abs(s + bar_sum - e) <= 10:
                walk["start_bps"], walk["end_bps"] = s, e
                walk["scale_adjusted"] = f"endpoints x{factor}"
                break
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
