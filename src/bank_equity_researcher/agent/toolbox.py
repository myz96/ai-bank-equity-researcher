"""The agent's toolbox: the Research class, the tools it exposes to the model,
and the evidence records those tools mint from the corpus.
"""

from __future__ import annotations

import re

from ..llm import LLM
from ..tools.corpus import Document
from ..tools.extract import extract_walk, extract_walk_annotations, printed_page_of
from ..tools.refs import relevance_terms, scan_page
from ..tools.retrieve import retrieve_pool
from ..validation.quotes import match_quote
from ..validation.schema import EvidenceRecord, NumberFact
from ..validation.validate import annotate_walks, check_walk, quote_prints

# How much of one page the read_page tool returns. A results-book page runs to
# about 3000 characters, so this covers the densest of them whole; beyond it a
# page is a chapter and the agent should search inside it instead.
MAX_PAGE_CHARS = 7000
MAX_SEARCH_HITS = 8
SNIPPET_CHARS = 240


class Research:
    """The tools, and the evidence they mint.

    Provenance is stamped by code: the agent names a document and a page, and
    the record's ids, page numbers and kinds are filled in from the corpus,
    never from the model's reply.
    """

    def __init__(self, llm: LLM, combo, docs: list[Document], case: dict, metric_cfg: dict,
                 registry: dict, registries: dict[str, dict] | None = None,
                 deadline_monotonic: float | None = None) -> None:
        self.llm = llm
        self.combo = combo
        # The case's absolute deadline on time.monotonic(). Every model call a
        # tool makes carries it, so no retry ladder can outlive the case.
        self.deadline_monotonic = deadline_monotonic
        self.docs = docs
        self.doc_by_id: dict[str, Document] = {d.doc_id: d for d in docs}
        self.case = case
        self.metric_cfg = metric_cfg
        self.registry = registry
        # A question may span banks, so bank_language answers for the bank it
        # is asked about. A metric case has one bank and leaves this empty.
        self.registries = registries or {}
        self.calendar = registry.get("calendar", {})
        self.records: list[EvidenceRecord] = []
        self.walks: list[dict] = []
        self.validation: dict = {"passed": [], "failed": []}
        self.pages_read: set[tuple[str, int]] = set()
        self.tool_calls = 0
        self.plan: list[str] = []
        self.plan_reviewed = False
        self._counter = 0

    # -- helpers ----------------------------------------------------------

    def next_id(self) -> str:
        self._counter += 1
        return f"ev-{self._counter}"

    def _doc(self, doc_id: str) -> Document:
        doc = self.doc_by_id.get(str(doc_id))
        if doc is not None:
            return doc
        # A near-miss on a doc_id is common and cheap to fix: match on the
        # unique suffix so the agent does not spend a call on a typo.
        matches = [d for key, d in self.doc_by_id.items() if str(doc_id).lower() in key.lower()]
        if len(matches) == 1:
            return matches[0]
        raise KeyError(
            f"unknown doc_id {doc_id!r}; the corpus holds: {', '.join(sorted(self.doc_by_id))}"
        )

    def _page_text(self, doc: Document, pdf_page: int) -> str:
        texts = doc.page_texts()
        if not 1 <= int(pdf_page) <= len(texts):
            raise IndexError(
                f"{doc.doc_id} has {len(texts)} pages; page {pdf_page} does not exist"
            )
        return texts[int(pdf_page) - 1]

    # -- tools ------------------------------------------------------------

    def search_pages(self, query: str, doc_id: str | None = None,
                     variants: list | None = None) -> dict:
        """One search, optionally fanned over query VARIANTS.

        A weak model under-queries: one phrasing, one hit list, stop. The fan
        runs each phrasing through the same pooled retrieval and merges by
        best score, so two or three wordings cost one tool call and the model
        is prompted to always send them (the bank's printed vocabulary and
        the question's own words rank different pages).
        """
        docs = [self._doc(doc_id)] if doc_id else self.docs
        queries = [str(query)]
        for v in variants or []:
            v = str(v).strip()
            if v and v.lower() not in (q.lower() for q in queries) and len(queries) < 4:
                queries.append(v)
        best: dict[tuple, tuple] = {}
        for q in queries:
            for doc, page, score in retrieve_pool(docs, q, top_k=MAX_SEARCH_HITS):
                key = (doc.doc_id, page)
                if key not in best or score > best[key][0]:
                    best[key] = (score, doc, q)
        ranked = sorted(best.items(), key=lambda kv: -kv[1][0])[:MAX_SEARCH_HITS]
        results = []
        for (did, page), (score, doc, q) in ranked:
            text = self._page_text(doc, page)
            results.append(
                {
                    "doc_id": did,
                    "pdf_page": page,
                    "score": round(score, 3),
                    "snippet": _snippet(text, q),
                }
            )
        return {"query": query, "variants": queries[1:], "results": results}

    def plan_research(self, items: list) -> dict:
        """Record the model's own coverage plan: where the answer's pieces
        should live. Free text, no matching by code — at submit time the loop
        reads the plan back once and asks for each item to be cited or
        written off, which turns thoroughness into bookkeeping."""
        self.plan = [str(item)[:200] for item in items or [] if str(item).strip()][:12]
        return {"recorded": self.plan,
                "instruction": "Research each item. At submit, every item must be "
                               "cited or its absence explained in limitations."}

    def read_page(self, doc_id: str, pdf_page: int) -> dict:
        doc = self._doc(doc_id)
        page = int(pdf_page)
        text = self._page_text(doc, page)
        self.pages_read.add((doc.doc_id, page))
        body = text[:MAX_PAGE_CHARS]
        return {
            "doc_id": doc.doc_id,
            "pdf_page": page,
            "printed_page": printed_page_of(text, page, doc.doc_type),
            "doc_type": doc.doc_type,
            "period": doc.period,
            "truncated": len(text) > MAX_PAGE_CHARS,
            "text": body,
        }

    def read_chart(self, doc_id: str, pdf_page: int, unit: str | None = None) -> dict:
        doc = self._doc(doc_id)
        page = int(pdf_page)
        # A metric case knows its unit. A free-form question has no metric and
        # so no unit to default to: the agent names it, and the reply echoes
        # what the bars were read and checked in. A defaulted unit stamps a
        # margin walk as dollars and measures bps against a money tolerance.
        unit = str(unit).strip() if unit else (self.metric_cfg.get("unit") or "")
        if not unit:
            return {
                "error": (
                    f"name the unit of the bars on {doc.doc_id} p{page} and call read_chart "
                    "again: pass unit as one of bps, $m, % or ppt. This question fixes no "
                    "metric, so the chart's unit cannot be assumed."
                )
            }
        case_desc = self.case["description"]
        try:
            walk, record = extract_walk(
                self.llm, self.combo.vision, doc, page, case_desc, self.next_id, unit=unit,
                deadline_monotonic=self.deadline_monotonic,
            )
        except Exception as exc:  # noqa: BLE001 - an unreadable chart is a gap, not a crash
            self.validation["failed"].append(f"walk_extraction_error p{page}: {exc}")
            # The annotation read below can still mint evidence from this page,
            # so provenance must count it read.
            self.pages_read.add((doc.doc_id, page))
            # The ANNOTATION layer is a separate read of the same page, so it is
            # attempted whether or not the walk read succeeded: returning here
            # would cost the agent its callout evidence exactly where a page is
            # hardest to read. The bar labels are simply unknown.
            return {
                "error": f"the chart on {doc.doc_id} p{page} could not be read: {exc}",
                "annotations": self._read_annotations(doc, page, case_desc, unit, ()),
            }
        passed, failed = check_walk(walk, doc.doc_type, unit)
        walk["source"] = f"{doc.doc_id} PDF p{page} ({record.id})"
        walk["record_id"] = record.id
        walk["checks_passed"] = passed
        walk["checks_failed"] = [f"{f} [{walk['source']}]" for f in failed]
        self.validation["passed"] += passed
        self.validation["failed"] += walk["checks_failed"]
        # Classify the chart against the task comparison before the agent reads
        # it. A free-form question fixes no single comparison, so there is
        # nothing to classify against: the agent reads the span off the chart's
        # own labels.
        if self.case.get("period") and self.case.get("comparator"):
            annotate_walks([walk], self.calendar, self.case["period"], self.case["comparator"])
        else:
            walk["comparison"] = "unclassified"
            walk["comparison_note"] = (
                "This question fixes no single comparison, so this chart was not matched "
                "against one. Read its endpoint labels before you use a bar, and name the "
                "span the bar belongs to."
            )
        self.walks.append(walk)
        self.records.append(record)
        self.pages_read.add((doc.doc_id, page))
        # The chart's ANNOTATION layer: the bank's own sub-split of each bar.
        # One extra vision call per chart, and it degrades to nothing on any
        # failure.
        bar_labels = tuple(str(bar.get("label", "")) for bar in walk.get("bars", []))
        return {
            "doc_id": doc.doc_id,
            "pdf_page": page,
            "evidence_id": record.id,
            "unit": unit,
            "walk": {k: v for k, v in walk.items() if k != "record_id"},
            "annotations": self._read_annotations(doc, page, case_desc, unit, bar_labels),
        }

    def _read_annotations(self, doc: Document, page: int, case_desc: str, unit: str,
                          bar_labels: tuple[str, ...]) -> list[dict]:
        """The chart's callout layer, minted and returned. Never raises.

        The cost ceiling is read AGAIN here. One read_chart costs two vision
        calls and counts as one tool call, so the loop's per-call check binds
        the pair and neither call inside it: a $0.50 ceiling admitted two $0.60
        calls and ended at $1.20. The callout layer is the optional half of the
        pair — the walk is what the caller asked for — so it is the half that
        gives way.
        """
        if self.llm.usage.cost_usd >= self.combo.cost_ceiling_usd:
            return []
        callouts = extract_walk_annotations(
            self.llm, self.combo.vision, doc, page, case_desc, self.next_id,
            unit=unit, bar_labels=bar_labels,
            deadline_monotonic=self.deadline_monotonic,
        )
        self.records.extend(callouts)
        return [
            {
                "evidence_id": r.id,
                "quote": r.quote,
                "numbers": [
                    {"label": n.label, "value": n.value, "unit": n.unit} for n in r.numbers
                ],
            }
            for r in callouts
        ]

    def follow_references(self, doc_id: str, pdf_page: int) -> dict:
        doc = self._doc(doc_id)
        page = int(pdf_page)
        terms = _relevance_terms(self.metric_cfg)
        try:
            references = scan_page(doc, page, terms)
        except Exception as exc:  # noqa: BLE001 - an unreadable page points nowhere
            return {"error": f"references on {doc.doc_id} p{page} could not be read: {exc}"}
        return {
            "doc_id": doc.doc_id,
            "pdf_page": page,
            "references": [
                {
                    "target": r.target,
                    "kind": ("note", "page", "footnote")[r.tier],
                    "pdf_pages": list(r.pages),
                    "shared_terms_with_task": r.relevance,
                }
                for r in references
            ],
        }

    def cite(self, doc_id: str, pdf_page: int, quotes: list) -> dict:
        """Mint evidence records from verbatim quotes on ONE page.

        Verification belongs where the reading happens, not at the end. The
        agent learns immediately whether a quote is really on the page, and it
        pays one call for as many quotes as the page supports. A record minted
        here is cited later by its id alone.
        """
        doc = self._doc(doc_id)
        page = int(pdf_page)
        text = self._page_text(doc, page)
        self.pages_read.add((doc.doc_id, page))
        cited, rejected, unprinted = [], [], []
        for item in quotes if isinstance(quotes, list) else []:
            entry = item if isinstance(item, dict) else {"quote": item}
            record, reason, dropped = self._mint_record(doc, page, text, entry)
            if record is None:
                rejected.append({"quote": str(entry.get("quote"))[:120], "reason": reason})
                continue
            self.records.append(record)
            cited.append({"id": record.id, "quote": record.quote})
            unprinted.extend(f"{record.id}: {d}" for d in dropped)
        result = {"doc_id": doc.doc_id, "pdf_page": page, "cited": cited}
        if rejected:
            result["rejected"] = rejected
            result["instruction"] = (
                "A rejected quote is not on this page as written. Copy the words from the "
                "page text exactly, or cite the page that really prints them."
            )
        if unprinted:
            result["dropped_numbers"] = unprinted
            result["numbers_instruction"] = (
                "A number in the numbers list must be printed by the quote it sits under. "
                "These were dropped. Quote the row or the sentence that prints the figure, "
                "then list it."
            )
        return result

    def _mint_record(self, doc: Document, page: int, text: str,
                     item: dict) -> tuple[EvidenceRecord | None, str, list[str]]:
        """One evidence record, or the reason the quote does not support one.

        Returns (record, reason, dropped numbers). A NumberFact is the model's
        own account of what the quote prints, so the quote is verified against
        the page before its numbers are read: a figure the quote prints is then
        a figure the PAGE prints, and every check over record.numbers — the
        column checks, the percent-evidence tests, the citation cap — reads
        figures a page states.
        """
        quote = str(item.get("quote") or "").strip()
        if not quote:
            return None, "no quote was given", []
        matched, relaxed = match_quote(quote, text)
        if not matched:
            return None, f"the quote is not on {doc.doc_id} p{page}", []
        numbers, dropped = [], []
        for number in item.get("numbers") or []:
            try:
                fact = NumberFact(
                    **{k: v for k, v in number.items()
                       if k in ("label", "value", "unit", "basis")}
                )
            except Exception:  # noqa: BLE001, S112 - a malformed number is dropped, not fatal
                continue
            if not quote_prints(quote, fact.value, fact.unit):
                dropped.append(
                    f"{fact.value:g} {fact.unit} ('{fact.label}') is not printed by that quote"
                )
                continue
            numbers.append(fact)
        return (
            EvidenceRecord(
                id=self.next_id(),
                doc_id=doc.doc_id,
                pdf_page=page,
                printed_page=printed_page_of(text, page, doc.doc_type),
                kind=str(item.get("kind") or "text"),
                # One line, always. The words are the page's own; the line
                # breaks are the PDF's column layout, and a record keeps only
                # the words. A stored newline would also break the report's
                # block quote, whose ">" prefix marks the first line alone —
                # and every reader that separates an answer's prose from its
                # quotes reads that prefix.
                quote=" ".join(quote.split())[:600],
                numbers=numbers,
                # The relaxation is recorded on the record, so a reader and the
                # grounding judge both see that this quote matched its page
                # under a weaker test than the others.
                provenance=relaxed or None,
            ),
            "",
            dropped,
        )

    def bank_language(self, bank: str | None = None) -> dict:
        """The registry entry, labels only. The registry holds no figures."""
        wanted = str(bank or self.case.get("bank") or "").upper()
        case_bank = str(self.case.get("bank") or "").upper()
        registry = self.registries.get(wanted)
        if registry is None and wanted == case_bank:
            registry = self.registry
        if registry is None:
            # A metric case loads one bank's registry. Answering for another
            # bank from it would hand out the case bank's vocabulary stamped
            # with the wrong name.
            return {
                "bank": wanted,
                "note": f"no language map is loaded for {wanted} in this case's scope",
            }
        language = {
            "bank": wanted or self.case.get("bank"),
            "measures": registry.get("measures", {}),
            "calendar": registry.get("calendar", {}),
        }
        metric = self.case.get("metric")
        if metric:
            language[f"{metric}_walk_labels"] = registry.get(f"{metric}_walk_labels", {})
        return language

    def dispatch(self, name: str, arguments: dict) -> dict:
        handlers = {
            "search_pages": self.search_pages,
            "plan_research": self.plan_research,
            "read_page": self.read_page,
            "read_chart": self.read_chart,
            "cite": self.cite,
            "follow_references": self.follow_references,
            "bank_language": self.bank_language,
        }
        handler = handlers.get(name)
        if handler is None:
            return {"error": f"no tool named {name!r}; available: {', '.join(handlers)}"}
        try:
            return handler(**arguments)
        except TypeError as exc:
            return {"error": f"{name} rejected those arguments: {exc}"}
        except Exception as exc:  # noqa: BLE001 - a failed tool is a message, not a crash
            return {"error": f"{name} failed: {type(exc).__name__}: {exc}"}

    # -- the citation gate -------------------------------------------------

    def check_citations(self, submitted: list) -> list[str]:
        """Why a submission's evidence entries would not hold, if any.

        The loop asks this BEFORE it accepts a submission, so a rejection can
        be handed back for correction. It mints nothing: a dry run that spent
        record ids would leave gaps in the artifact for every attempt.
        """
        return self._resolve_evidence(submitted)[1]

    def build_records(self, submitted: list) -> tuple[list[EvidenceRecord], list[str], dict]:
        """Turn a submission's evidence list into records, checking every quote.

        Returns (records, rejections, id_map). A record the agent identified by
        the id a tool already minted is taken from the tool, so a chart read
        keeps the numbers the vision pass extracted. Anything else must quote
        its page verbatim, and a quote that is not on that page is rejected.
        """
        resolved, rejections = self._resolve_evidence(submitted)
        records: list[EvidenceRecord] = []
        id_map: dict[str, str] = {}
        used: set[str] = set()
        for claimed, minted, page_source in resolved:
            if minted is not None:
                if claimed not in used:
                    records.append(minted)
                    used.add(claimed)
                id_map[claimed] = claimed
                continue
            doc, page, text, item = page_source
            record, _reason, _dropped = self._mint_record(doc, page, text, item)
            if record is None:  # pragma: no cover - _resolve_evidence checked it
                continue
            if claimed and claimed not in used:
                record = record.model_copy(update={"id": claimed})
            used.add(record.id)
            id_map[claimed or record.id] = record.id
            records.append(record)
        return records, rejections, id_map

    def _resolve_evidence(self, submitted: list) -> tuple[list[tuple], list[str]]:
        """Sort a submission's evidence into what holds and what does not."""
        by_id = {record.id: record for record in self.records}
        resolved: list[tuple] = []
        rejections: list[str] = []
        for item in submitted if isinstance(submitted, list) else []:
            if not isinstance(item, dict):
                continue
            claimed = str(item.get("id") or "").strip()
            minted = by_id.get(claimed)
            if minted is not None:
                resolved.append((claimed, minted, None))
                continue
            if not str(item.get("quote") or "").strip():
                rejections.append(
                    f"{claimed or '(no id)'}: no quote, and no tool minted that id"
                )
                continue
            try:
                doc = self._doc(item.get("doc_id"))
                page = int(item.get("pdf_page"))
                text = self._page_text(doc, page)
            except Exception as exc:  # noqa: BLE001
                rejections.append(f"{claimed or '(no id)'}: {exc}")
                continue
            if not match_quote(str(item.get("quote")), text)[0]:
                rejections.append(
                    f"{claimed or '(no id)'}: the quote is not on {doc.doc_id} p{page}. "
                    "Re-read that page and copy the words exactly, or cite the page that "
                    "really prints them."
                )
                continue
            resolved.append((claimed, None, (doc, page, text, item)))
        return resolved, rejections


def _snippet(text: str, query: str) -> str:
    """A window of the page around the first query word that appears on it."""
    words = re.findall(r"[A-Za-z]{4,}", query.lower())
    lowered = text.lower()
    at = next((lowered.find(w) for w in words if lowered.find(w) >= 0), -1)
    start = max(0, at - SNIPPET_CHARS // 3) if at >= 0 else 0
    return re.sub(r"\s+", " ", text[start:start + SNIPPET_CHARS]).strip()


def _relevance_terms(metric_cfg: dict) -> set[str]:
    return relevance_terms(" ".join([*metric_cfg["retrieval_queries"], metric_cfg["name"]]))
