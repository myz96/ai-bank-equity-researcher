"""The closed-loop research agent (ADR-0005), the estate's only shell.

The model reads, reasons, and chooses what to read next, through tools that
wrap the deterministic estate — retrieval, page text, the vision walk reader,
reference following, the bank registry.

A submission becomes an Attribution, and the same validators and confidence
caps then run over it, so the eval harness scores one artifact contract.

Two gates keep the loop honest and bounded:

- CITATION. Every evidence record the agent submits must quote its page
  verbatim. Code checks each quote against the page's own text and rejects one
  that is not there, so a paraphrase can never reach the artifact wearing a
  citation. Rejection is fed back, so the agent can re-read and correct.
- BUDGET. Tool calls, cost and wall-clock are runaway protection, set
  generously (ADR-0005 point 5). On exhaustion the agent is asked for the
  answer it has, with the shortfall declared as a limitation. It never crashes.
"""

from __future__ import annotations

import json
import re
import time
from datetime import UTC, datetime

from ..config import COMBOS, LIVE_COMBO, OUT_DIR, REGISTRY_DIR
from ..llm import LLM
from ..render import case_slug, render_answer, render_report, slugify
from ..taxonomy import METRIC_ALIASES, TAXONOMY
from ..tools.corpus import Document, documents_for_period, documents_for_question
from ..tools.extract import extract_walk, extract_walk_annotations, printed_page_of
from ..tools.refs import relevance_terms, scan_page
from ..tools.retrieve import retrieve
from ..validation.quotes import match_quote, quote_key
from ..validation.schema import (
    Attribution,
    Disagreement,
    DriverClaim,
    EvidenceRecord,
    NumberFact,
    enforce_answer_gate,
    enforce_evidence_gate,
)
from ..validation.validate import (
    _movement_source,
    _percent_evidenced,
    _settle_basis,
    annotate_walks,
    build_period_note,
    cap_drivers_on_failed_walks,
    cap_unreconciled_drivers,
    cap_weakly_cited_claims,
    check_comparison_leak,
    check_component_columns,
    check_drivers_reconcile,
    check_movement,
    check_movement_basis,
    check_movement_columns,
    check_movement_variant,
    check_ratio_level,
    check_walk,
    corroborate,
    cross_source_view,
    default_comparator,
    drop_off_unit_contributions,
    half_label,
    movement_arithmetic_tolerance,
    period_end_date,
    primary_basis,
    quote_prints,
    settle_charge_sign,
    settle_identity_scale,
    settle_ratio_scale,
    walks_for_view,
)
from .prompts import (
    CASE_PROMPT,
    QUESTION_PROMPT,
    QUESTION_SUBMIT_SPEC,
    QUESTION_SYSTEM_PROMPT,
    SUBMIT_SPEC,
    SYSTEM_PROMPT,
    TOOL_SPECS,
)

# How much of one page the read_page tool returns. A results-book page runs to
# about 3000 characters, so this covers the densest of them whole; beyond it a
# page is a chapter and the agent should search inside it instead.
MAX_PAGE_CHARS = 7000
MAX_SEARCH_HITS = 8
SNIPPET_CHARS = 240
# A rejected submission is returned to the agent to correct. After this many
# attempts the answer ships with the unverifiable records dropped, because an
# honest partial answer beats no answer at all.
MAX_SUBMIT_ATTEMPTS = 3
# A model that answers in prose instead of calling a tool is nudged back to the
# tools. A loop of nudges is a stuck model, not a research strategy.
MAX_PROSE_TURNS = 3
# The hard stop, counted in TURNS rather than tool calls. Once a budget runs
# out the loop asks for a submission and offers only the submit tool; a model
# that keeps asking for other tools would never meet another budget, because
# the first one to run out latches. These two bounds end the loop regardless.
MAX_TURNS_AFTER_BUDGET = 10
HARD_STOP_FACTOR = 1.5


def _start_run(combo_name: str):
    """The shared head of both shells: clocks, combo, model client.

    time.time() drives the loop's budget messages; the retry ladders hold to
    an absolute time.monotonic() deadline, a clock that never steps backwards.
    """
    started = time.time()
    combo = COMBOS[combo_name]
    if not combo.agent:
        raise ValueError(f"combo {combo_name} declares no agent model")
    deadline = time.monotonic() + _hard_stop_s(combo)
    return started, combo, deadline, LLM()


def _provenance(combo, docs, started: float, llm, research, exhausted) -> dict:
    """The audit block both shells stamp: any claim is checkable months later
    without rerunning anything (models, document hashes, cost, budgets)."""
    return {
        "combo": combo.name,
        "models": f"agent={combo.agent}, vision={combo.vision}",
        "documents": ", ".join(f"{d.doc_id} ({(d.sha256 or '')[:12]})" for d in docs),
        "generated": datetime.now(UTC).isoformat(timespec="seconds"),
        "seconds": round(time.time() - started, 1),
        "cost_usd": round(llm.usage.cost_usd, 4),
        "tokens": f"{llm.usage.prompt_tokens} in / {llm.usage.completion_tokens} out",
        "orchestration": "agent",
        "tool_calls": research.tool_calls,
        "pages_read": len(research.pages_read),
        "charts_read": len(research.walks),
        "budget_exhausted": exhausted or "no",
    }


def _document_lines(docs) -> str:
    """The corpus listing both task prompts print: one line per document."""
    return "\n".join(f"- {d.doc_id} ({d.period}, {len(d.page_texts())} pages)" for d in docs)


def _stopped_early_note(exhausted: str) -> str:
    return (
        f"Research stopped early: {exhausted} was reached, so the evidence behind this "
        "answer is less complete than a full run's."
    )


def _recover_minted(cited_ids, minted_by_id, present, id_map, records) -> None:
    """A cited id the tools minted but the reply dropped from its records list
    is restored from the tool's own record — never from the model's text. Both
    shells recover the same way, or one would ground facts the other drops."""
    for cited in cited_ids:
        key = str(cited)
        if key in minted_by_id and key not in present and key not in id_map:
            records.append(minted_by_id[key])
            present.add(key)


_REJECTED_CITATIONS_NOTE = (
    "These citations were dropped because the quote was not found on the page "
    "given: "
)


def _budget_hit(research, llm, combo, spent_s: float, wall_limit_s: float) -> str | None:
    """The first budget that binds, or None; the same words wherever it stops.

    The turn-top check measures the soft wall clock and the per-call check the
    hard stop: a turn already under way may finish its calls, but must not
    start new work past the hard stop. Budgets bind per CALL, not per turn —
    read once at the top of a turn, a turn that began one call inside the
    budget dispatched every call it carried (measured at 25 calls against a
    budget of 2)."""
    if research.tool_calls >= combo.max_tool_calls:
        return f"the tool-call budget ({combo.max_tool_calls} calls)"
    if llm.usage.cost_usd >= combo.cost_ceiling_usd:
        return f"the cost ceiling (${combo.cost_ceiling_usd:.2f})"
    if spent_s >= wall_limit_s:
        return f"the wall-clock budget ({combo.wall_clock_s:.0f}s)"
    return None


def _hard_stop_s(combo) -> float:
    """The loop's hard stop in seconds — the wall-clock rail with its overrun
    factor. Stated once: the loop's budget messages measure it on time.time()
    and the retry ladders on time.monotonic(), and the two must agree on the
    quantity they measure."""
    return HARD_STOP_FACTOR * combo.wall_clock_s


# --------------------------------------------------------------------------
# The toolbox
# --------------------------------------------------------------------------


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

    def search_pages(self, query: str, doc_id: str | None = None) -> dict:
        docs = [self._doc(doc_id)] if doc_id else self.docs
        hits: list[tuple[float, str, int]] = []
        for doc in docs:
            for page, score in retrieve(doc, str(query), top_k=6):
                hits.append((score, doc.doc_id, page))
        hits.sort(key=lambda h: (-h[0], h[1], h[2]))
        results = []
        for score, did, page in hits[:MAX_SEARCH_HITS]:
            text = self._page_text(self.doc_by_id[did], page)
            results.append(
                {
                    "doc_id": did,
                    "pdf_page": page,
                    "score": round(score, 3),
                    "snippet": _snippet(text, str(query)),
                }
            )
        return {"query": query, "results": results}

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
            except Exception:  # noqa: BLE001 - a malformed number is dropped, not fatal
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
            # with the wrong name (Fable review cycle 6, finding 2).
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


def _keep_valid(items, model, dropped: list[str], what: str) -> list:
    """Every item the schema accepts, with each rejection recorded.

    One malformed sub-object must not cost a whole research run its answer. A
    driver rated 105, or a disagreement whose reason is not one of the five,
    is dropped and named in limitations — the artifact then says what it lost,
    which is the honest outcome and the one a reader can check.
    """
    kept = []
    for item in items or []:
        try:
            kept.append(model.model_validate(item))
        except Exception as exc:  # noqa: BLE001
            dropped.append(f"{what} dropped as malformed ({str(exc).splitlines()[0][:120]})")
    return kept


def _snippet(text: str, query: str) -> str:
    """A window of the page around the first query word that appears on it."""
    words = [w for w in re.findall(r"[A-Za-z]{4,}", query.lower())]
    lowered = text.lower()
    at = next((lowered.find(w) for w in words if lowered.find(w) >= 0), -1)
    start = max(0, at - SNIPPET_CHARS // 3) if at >= 0 else 0
    return re.sub(r"\s+", " ", text[start:start + SNIPPET_CHARS]).strip()


def _numeric(value) -> float | None:
    """A number the submission carries, however it spelt it, or None.

    A model sends "2.05" or "30,153" often enough that refusing strings would
    drop real movements; anything that does not parse is None, never a raise.
    """
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def _relevance_terms(metric_cfg: dict) -> set[str]:
    return relevance_terms(" ".join([*metric_cfg["retrieval_queries"], metric_cfg["name"]]))


# --------------------------------------------------------------------------
# From a submission to the artifact
# --------------------------------------------------------------------------


def build_attribution(payload: dict, research: Research, case: dict, metric_cfg: dict,
                      registry: dict) -> tuple[Attribution, list[str]]:
    """Assemble the Attribution a submission describes.

    The reply-level normalisers are the author's own (unit slips, the charge
    sign convention, the basis word, the delta against its endpoints): the
    agent writes the same reply shape, so it inherits the same corrections and
    the artifact stays one contract rather than two.
    """
    records, rejections, id_map = research.build_records(payload.get("evidence"))
    reply = dict(payload)

    def remap(ids) -> list[str]:
        return [id_map.get(str(e), str(e)) for e in ids or [] if isinstance(e, (str, int))]

    # A citation to a record a tool already verified is a citation, whether or
    # not the submission repeated it in the evidence list. The record is
    # carried in rather than stripped: it was minted from the page's own words,
    # so dropping the claim that rests on it would punish bookkeeping, not a
    # guess. An id no tool minted still resolves to nothing and still falls to
    # the evidence gate.
    #
    # This runs BEFORE every normaliser that reads the evidence:
    # `_percent_evidenced` decides the percent-to-bps lift against the record
    # list, so a recovery running after it leaves a NIM movement whose only
    # evidence arrived through `headline_evidence` on its percent scale
    # ("2.08 -> 2.05, -0.03 bps").
    minted_by_id = {record.id: record for record in research.records}
    present = {record.id for record in records}
    _recover_minted(
        [
            *(reply.get("headline_evidence") or []),
            *(e for driver in reply.get("drivers") or []
              if isinstance(driver, dict) for e in driver.get("evidence") or []),
        ],
        minted_by_id, present, id_map, records,
    )

    movement = reply.get("movement")
    if isinstance(movement, dict) and any(
        movement.get(k) is None for k in ("from_value", "to_value", "delta")
    ):
        movement = None
        reply.setdefault("limitations", []).append(
            "The movement could not be established from the evidence."
        )
    if isinstance(movement, dict):
        # The submit schema cannot forbid every malformed shape a model can
        # send, and a ValidationError here would end a 10-30 minute run with
        # no artifact (Fable review cycle 6, finding 1). Coerce or degrade,
        # never crash: numbers-as-strings are read, anything else drops the
        # movement to None with the reason declared.
        coerced = {k: _numeric(movement.get(k)) for k in ("from_value", "to_value", "delta")}
        unit = str(movement.get("unit") or "").strip()
        if None in coerced.values() or not unit:
            movement = None
            reply.setdefault("limitations", []).append(
                "The submitted movement was malformed (non-numeric values or a missing "
                "unit), so no movement is stated."
            )
        else:
            movement = {**movement, **coerced, "unit": unit}
    if isinstance(movement, dict) and metric_cfg["unit"] == "bps":
        frm, to = movement.get("from_value"), movement.get("to_value")
        if (
            isinstance(frm, (int, float))
            and isinstance(to, (int, float))
            and max(abs(frm), abs(to)) < 100
            and _percent_evidenced(frm, records)
            and _percent_evidenced(to, records)
        ):
            movement["from_value"], movement["to_value"] = frm * 100, to * 100
            if abs(movement.get("delta", 0) - round((to - frm) * 100, 1)) > (
                movement_arithmetic_tolerance(movement.get("unit"))
            ):
                movement["delta"] = round((to - frm) * 100, 1)
            reply.setdefault("limitations", []).append(
                f"Movement endpoints converted from percent ({frm}, {to}) to bps: the unit "
                "for this metric is bps."
            )
    if isinstance(movement, dict):
        movement = settle_charge_sign(movement, metric_cfg, reply)
    if isinstance(movement, dict):
        # The threshold is check_movement's own, indexed by the movement's unit.
        implied = round(movement["to_value"] - movement["from_value"], 2)
        if (
            abs(movement["delta"] - implied)
            > movement_arithmetic_tolerance(movement.get("unit"))
            and implied != 0
        ):
            reply.setdefault("limitations", []).append(
                f"Movement delta normalised from {movement['delta']} to {implied} "
                "(unit slip against the endpoints)."
            )
            movement["delta"] = implied

    prepared = []
    for driver in reply.get("drivers") or []:
        if not isinstance(driver, dict):
            continue
        driver = dict(driver)
        contribution = driver.get("contribution")
        if isinstance(contribution, dict) and contribution.get("value") is None:
            driver["contribution"] = None
        if driver.get("columns") is not None:
            driver["columns"] = str(driver["columns"]).strip()[:120] or None
        driver["evidence"] = remap(driver.get("evidence"))
        driver["narrative"] = str(driver.get("narrative") or "")
        prepared.append(driver)
    dropped: list[str] = drop_off_unit_contributions(prepared, metric_cfg["unit"])
    drivers = _keep_valid(prepared, DriverClaim, dropped, "driver")
    disagreements = _keep_valid(
        reply.get("disagreements"), Disagreement, dropped, "disagreement"
    )

    residual = reply.get("residual") if isinstance(reply.get("residual"), dict) else None
    if residual is not None and (
        _numeric(residual.get("value")) is None or not str(residual.get("unit") or "").strip()
    ):
        residual = None
        reply.setdefault("limitations", []).append(
            "The submitted residual was malformed (non-numeric value or a missing unit), "
            "so no residual is stated."
        )

    raw_confidence = _numeric(reply.get("attribution_confidence"))
    confidence = 0 if raw_confidence is None else int(raw_confidence)
    if not 0 <= confidence <= 100:
        reply.setdefault("limitations", []).append(
            f"attribution_confidence clamped from {confidence} into 0-100."
        )
        confidence = min(100, max(0, confidence))

    # _settle_basis records its own substitution in reply["limitations"], so it
    # runs before the limitations list is read out of the reply.
    basis = _settle_basis(reply.get("basis"), registry, records, reply)
    limitations = [str(item) for item in reply.get("limitations") or []] + dropped
    if rejections:
        limitations.append(
            _REJECTED_CITATIONS_NOTE + "; ".join(rejections)
        )
    attribution = Attribution(
        bank=case["bank"],
        metric=case["metric"],
        period=case["period"],
        comparator=case["comparator"],
        basis=basis,
        movement=movement,
        movement_source=_movement_source(reply),
        headline=str(reply.get("headline") or ""),
        headline_evidence=remap(reply.get("headline_evidence")),
        drivers=drivers,
        residual=residual,
        notable_items=[str(i) for i in reply.get("notable_items") or []],
        disagreements=disagreements,
        attribution_confidence=confidence,
        limitations=limitations,
        evidence_records=records,
    )
    return enforce_evidence_gate(attribution), rejections


def finalise(attribution: Attribution, research: Research, case: dict, metric_cfg: dict,
             registry: dict, headline_label: str | None) -> Attribution:
    """Run the estate's validators and confidence caps over a submission.

    An answer is scored by what it can prove: the checks, the thresholds and
    the grading of which failure is fatal do not read who assembled it.
    """
    calendar = research.calendar
    period, comparator = case["period"], case["comparator"]
    period_date = period_end_date(period, calendar)
    comparator_date = period_end_date(comparator, calendar)
    prior_half_date = None
    if period_date:
        prior_half_date = (
            (period_date[0] - 6, period_date[1]) if period_date[0] > 6
            else (period_date[0] + 6, period_date[1] - 1)
        )
        if prior_half_date == comparator_date:
            prior_half_date = None
    prior_half_tag = half_label(prior_half_date, calendar)
    bank_basis = primary_basis(registry)
    is_bridge = metric_cfg["method"] == "bridge_extraction"

    walks = research.walks
    walks.sort(key=lambda w: 0 if w.get("comparison") == "primary" else 1)
    primary_walks = [w for w in walks if w.get("comparison") == "primary"]
    context_walks = [w for w in walks if w.get("comparison") == "context"]
    classified = primary_walks + context_walks
    label_map = registry.get(f"{case['metric']}_walk_labels", {})
    view_walks, _view_note = walks_for_view(walks)
    cross_source = cross_source_view(view_walks, label_map)
    primary_view = cross_source_view(primary_walks, label_map)
    context_view = cross_source_view(context_walks, label_map)

    # Ratio-scale corrector first: it restates a movement written in basis
    # points, and settle_identity_scale then reads the corrected endpoints.
    settle_ratio_scale(attribution, metric_cfg["unit"])
    settle_identity_scale(attribution, metric_cfg["method"])
    corroborate(attribution, cross_source)
    cap_weakly_cited_claims(attribution)
    if is_bridge:
        split = {
            d.canonical: d
            for d in attribution.drivers
            if d.contribution is not None
            and d.canonical in ("operating_expenses", "notable_items")
        }
        if len(split) == 2:
            for driver in split.values():
                driver.confidence = min(driver.confidence, 80)
            attribution.limitations.append(
                "Expenses are claimed on the underlying/notable split; the bank equally "
                "publishes the combined headline framing, so both claims are capped at 80."
            )

    validation = research.validation
    output_failed: list[str] = []
    drivers_passed, drivers_failed = check_drivers_reconcile(attribution)
    component = (
        check_component_columns(
            attribution, period_date, comparator_date, prior_half_date, prior_half_tag
        )
        if is_bridge
        else ([], [])
    )
    for check in (
        check_movement(attribution.movement),
        check_ratio_level(attribution.movement, metric_cfg["unit"]),
        (drivers_passed, drivers_failed),
        check_comparison_leak(attribution, primary_view, context_view),
        check_movement_columns(attribution, period_date, comparator_date, prior_half_date),
        check_movement_variant(attribution, headline_label),
        check_movement_basis(attribution, bank_basis, headline_label),
        component,
    ):
        validation["passed"] += check[0]
        output_failed += check[1]

    peripheral = [f for f in validation["failed"] if f.startswith("walk_extraction_error")]
    primary_sum_ok = any("walk_sum" in walk.get("checks_passed", []) for walk in primary_walks)
    for walk in walks:
        if not walk.get("checks_failed"):
            continue
        load_bearing = walk.get("comparison") == "primary" and not (
            primary_sum_ok and "drivers_reconcile" in drivers_passed
        )
        if not load_bearing:
            peripheral += walk["checks_failed"]
    fatal = output_failed + [f for f in validation["failed"] if f not in peripheral]
    honest_partial: list[str] = []
    if metric_cfg["method"] == "two_level_arithmetic" or (
        metric_cfg["method"] == "walk_extraction" and classified and not primary_walks
    ):
        fatal = [f for f in fatal if f != "no_quantified_drivers"]
        honest_partial += [f for f in output_failed if f == "no_quantified_drivers"]
    if peripheral and "walk_sum" not in validation["passed"]:
        fatal += peripheral
        peripheral = []
    peripheral += honest_partial
    validation["failed"] += output_failed
    cap_drivers_on_failed_walks(attribution, walks)
    if fatal or peripheral:
        attribution.limitations.extend(f"Failed check: {f}" for f in fatal + peripheral)
    if fatal:
        attribution.attribution_confidence = min(attribution.attribution_confidence, 40)
        cap_unreconciled_drivers(attribution, fatal)
    elif metric_cfg["method"] == "walk_extraction" and classified and not primary_walks:
        attribution.limitations.append(
            f"No published walk covers {period} vs {comparator}: the bank's walk for this "
            "metric describes another comparison, so the driver split is not walk-verified "
            "for this comparison. Confidence is capped at 85."
        )
        attribution.attribution_confidence = min(attribution.attribution_confidence, 85)
        for driver in attribution.drivers:
            driver.confidence = min(driver.confidence, 85)
    if metric_cfg["method"] == "walk_extraction" and not primary_walks and (
        classified or not walks
    ):
        for driver in attribution.drivers:
            driver.confidence = min(driver.confidence, 85)
    return attribution


# --------------------------------------------------------------------------
# The loop
# --------------------------------------------------------------------------


def _arguments(call: dict) -> dict:
    """The arguments of one tool call, whichever way the provider encoded them."""
    raw = (call.get("function") or {}).get("arguments")
    if isinstance(raw, dict):
        return raw
    try:
        parsed = json.loads(raw or "{}")
    except (TypeError, ValueError):
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _assistant_turn(message: dict) -> dict:
    """The assistant message as it must be echoed back into the transcript."""
    turn = {"role": "assistant", "content": message.get("content") or ""}
    if message.get("tool_calls"):
        turn["tool_calls"] = message["tool_calls"]
    return turn


def _tool_result(call_id: str, payload: dict) -> dict:
    return {"role": "tool", "tool_call_id": call_id, "content": json.dumps(payload)[:60000]}


def research_loop(llm: LLM, combo, research: Research, messages: list[dict],
                  submit_spec: dict, started: float,
                  deadline_monotonic: float | None = None) -> tuple[dict | None, str | None]:
    """Drive the closed loop until it submits, or until a budget ends it.

    Returns (the submitted payload or None, the budget that ran out or None).
    The loop knows nothing about what is being submitted: it moves tool calls
    to the toolbox and results back, and it runs the citation gate over any
    submission before it accepts one. That is why a movement and a free-form
    question share it - only the submit schema and the prompts differ.

    `deadline_monotonic` is the same hard stop this loop reads between turns,
    handed to every model call so ONE call cannot sit past it. The loop reads
    its wall clock between calls only, so a turn holding a retry ladder would
    otherwise add minutes the loop cannot see. The submit turns carry it too: a
    submission asked for after the budget ran out is still inside the case.
    """
    tools = [*TOOL_SPECS, submit_spec]
    payload: dict | None = None
    submit_attempts = 0
    prose_turns = 0
    turns = 0
    exhausted: str | None = None
    while payload is None:
        spent = time.time() - started
        # The hard stop. Asking for a submission is a REQUEST, and a model that
        # ignores it — by calling a tool it was no longer offered, turn after
        # turn — would otherwise loop for ever, because the first budget to run
        # out latches and stops being re-read. These two bounds cannot be
        # talked past: they end the loop whatever the reply says.
        turns += 1
        turn_cap = combo.max_tool_calls + MAX_TURNS_AFTER_BUDGET
        if turns > turn_cap:
            # A model that ignores the submit request, turn after turn, is a
            # different stop from running out of time: such a run never comes
            # near the wall clock. The budget that latched first is kept beside
            # it: it is why the model was being asked to submit at all.
            exhausted = (
                f"the turn cap ({turn_cap} turns)" if exhausted is None
                else f"the turn cap ({turn_cap} turns), after {exhausted}"
            )
            break
        if spent >= _hard_stop_s(combo):
            exhausted = exhausted or f"the wall-clock budget ({combo.wall_clock_s:.0f}s)"
            break
        if exhausted is None:
            exhausted = _budget_hit(research, llm, combo, spent, combo.wall_clock_s)
            if exhausted:
                messages.append(
                    {
                        "role": "user",
                        "content": (
                            f"The research budget is spent: you reached {exhausted}. Call "
                            "submit now with the answer your evidence already supports. "
                            "Leave unproved claims unquantified, name every gap in "
                            "limitations, and lower your confidence to match. Do not "
                            "state a number you did not read."
                        ),
                    }
                )
        turn_tools = [submit_spec] if exhausted else tools
        message = llm.chat_tools(
            combo.agent, messages, turn_tools, max_tokens=combo.agent_max_tokens,
            deadline_monotonic=deadline_monotonic,
        )
        messages.append(_assistant_turn(message))
        calls = message.get("tool_calls") or []
        if not calls:
            prose_turns += 1
            if prose_turns > MAX_PROSE_TURNS:
                break
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Answer only by calling a tool. Keep researching, or call submit "
                        "with the answer."
                    ),
                }
            )
            continue
        # Every call in a turn is answered, whatever happens to the others: a
        # provider that asked for two tools and got one result back rejects the
        # next request outright.
        for call in calls:
            name = (call.get("function") or {}).get("name") or ""
            call_id = call.get("id") or name
            arguments = _arguments(call)
            # An accepted answer is FINAL. Every remaining call in the turn is
            # ANSWERED, so the transcript the provider sees stays complete, but
            # none of them RUNS. A tool dispatched after acceptance writes into
            # the same research state the accepted answer is built from — a
            # cite placed after submit mints the very record the answer cites —
            # so the artifact would turn on how the provider happened to order
            # one turn's calls.
            if payload is not None:
                messages.append(
                    _tool_result(call_id, {
                        "accepted": False,
                        "reason": "the answer was already submitted; this call was not run",
                    })
                )
                continue
            if name != "submit":
                # Cost binds per CALL as well. It was read once a turn, and
                # one read_chart now costs TWO vision calls (the bars and
                # the annotation layer) while counting as one tool call, so
                # a single turn carrying five chart reads issued ten vision
                # calls with no cost check between them.
                stop = _budget_hit(research, llm, combo,
                                   time.time() - started, _hard_stop_s(combo))
                if stop is not None:
                    exhausted = exhausted or stop
                    messages.append(
                        _tool_result(call_id, {
                            "accepted": False,
                            "reason": (
                                f"{stop} ran out, so this call was not run. Call submit with "
                                "the answer your evidence already supports."
                            ),
                        })
                    )
                    continue
                research.tool_calls += 1
                messages.append(_tool_result(call_id, research.dispatch(name, arguments)))
                continue
            submit_attempts += 1
            rejections = research.check_citations(arguments.get("evidence"))
            if rejections and submit_attempts < MAX_SUBMIT_ATTEMPTS:
                research.tool_calls += 1
                messages.append(
                    _tool_result(
                        call_id,
                        {
                            "accepted": False,
                            "rejected_citations": rejections,
                            "instruction": (
                                "Each rejected quote is not on the page you named. Re-read "
                                "that page with read_page, copy the words exactly as printed, "
                                "and submit again. Drop any claim you cannot quote."
                            ),
                        },
                    )
                )
                continue
            payload = arguments
            messages.append(_tool_result(call_id, {"accepted": True}))
    return payload, exhausted


def run_agent_case(bank: str, metric: str, period: str, comparator: str | None,
                   combo_name: str = LIVE_COMBO):
    """Research one case in a closed loop, then write the case artifacts."""
    started, combo, deadline, llm = _start_run(combo_name)
    metric_key = METRIC_ALIASES[metric.lower()]
    metric_cfg = TAXONOMY[metric_key]
    comparator = comparator or default_comparator(period)
    case = {"bank": bank, "metric": metric_key, "period": period, "comparator": comparator}
    case["description"] = f"{bank} {metric_cfg['name']} in {period} vs {comparator}"

    registry_path = REGISTRY_DIR / f"{bank.lower()}.json"
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    period_note = build_period_note(period, comparator, registry.get("calendar", {}))
    headline_label = registry.get("measures", {}).get(
        {
            "cash_earnings": "core_profit",
            "cti": "cti_label",
            "roe": "roe_label",
            "impairment": "impairment_line",
        }.get(metric_key, "")
    )

    docs = documents_for_period(bank, period, comparator)
    if not docs:
        raise RuntimeError(f"no documents in corpus for {bank} {period}/{comparator}")
    research = Research(llm, combo, docs, case, metric_cfg, registry,
                        deadline_monotonic=deadline)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": CASE_PROMPT.format(
                bank=bank,
                metric_name=metric_cfg["name"],
                period=period,
                comparator=comparator,
                period_note=period_note,
                method_hint=metric_cfg.get("method_hint", ""),
                taxonomy=json.dumps(metric_cfg["drivers"], indent=1),
                headline_row=headline_label
                or (
                    "the registry records no row for this metric - take the bank's own "
                    "headline measure from the results book's KPI table"
                ),
                unit=metric_cfg["unit"],
                documents=_document_lines(docs),
            ),
        },
    ]

    payload, exhausted = research_loop(llm, combo, research, messages, SUBMIT_SPEC, started,
                                       deadline_monotonic=deadline)

    if payload is None:
        # An artifact still ships: it carries what was read and says plainly
        # that nothing was concluded.
        payload = {
            "evidence": [{"id": record.id} for record in research.records],
            "headline": "",
            "drivers": [],
            "attribution_confidence": 0,
            "limitations": [
                "The research loop ended without a submitted attribution "
                f"({exhausted or 'the model stopped calling tools'})."
            ],
        }
    attribution, _rejections = build_attribution(payload, research, case, metric_cfg, registry)
    if exhausted:
        attribution.limitations.append(_stopped_early_note(exhausted))
    attribution = finalise(attribution, research, case, metric_cfg, registry, headline_label)

    attribution.provenance = _provenance(combo, docs, started, llm, research, exhausted)

    out = OUT_DIR / case_slug(bank, metric_key, period, comparator, combo.name)
    out.mkdir(parents=True, exist_ok=True)
    (out / "attribution.json").write_text(attribution.model_dump_json(indent=2))
    (out / "report.md").write_text(render_report(attribution))
    return attribution, out


# --------------------------------------------------------------------------
# The question shell: the same loop, a smaller submission.
# --------------------------------------------------------------------------


def question_scope(question: str, docs: list[Document]) -> tuple[dict, dict, dict]:
    """The case, the metric config and the registries a question researches with.

    A question has no metric, so the fields the toolbox reads off a metric are
    filled from the question itself: its own words are the relevance terms
    reference-following ranks by, and there is no period pair to classify a
    chart against.
    """
    banks = list(dict.fromkeys(doc.bank for doc in docs))
    registries: dict[str, dict] = {}
    for bank in banks:
        path = REGISTRY_DIR / f"{bank.lower()}.json"
        registries[bank] = json.loads(path.read_text()) if path.exists() else {}
    case = {
        "bank": ", ".join(banks),
        "metric": None,
        "period": None,
        "comparator": None,
        "description": str(question)[:300],
    }
    metric_cfg = {
        "name": "the question",
        # No metric, so no unit: an empty unit makes read_chart ask the agent
        # for one instead of stamping every chart with a default.
        "unit": "",
        "method": "free_form",
        "retrieval_queries": [str(question)],
        "drivers": {},
    }
    return case, metric_cfg, registries


def build_answer(payload: dict, research: Research, question: str, docs: list[Document]) -> dict:
    """Assemble the answer artifact one submission describes.

    Every record is re-checked against its page here, exactly as a movement's
    records are: the loop's own check is a dry run that mints nothing. The
    output is one answer shape, so the renderer, the scorers and the judge
    read one artifact for every question, whichever entry point asked it.
    """
    records, rejections, id_map = research.build_records(payload.get("evidence"))
    # A record a tool minted and the note cites, but the evidence list forgot,
    # is carried in rather than stripped: it was verified against the page's
    # own words when the tool minted it (the same rule the movement path uses).
    minted_by_id = {record.id: record for record in research.records}
    present = {record.id for record in records}
    for fact in payload.get("key_facts") or []:
        if not isinstance(fact, dict):
            continue
        _recover_minted(fact.get("citations", fact.get("evidence")) or [],
                        minted_by_id, present, id_map, records)

    def remap(fact: dict) -> dict:
        cited = fact.get("citations", fact.get("evidence")) or []
        cited = [cited] if isinstance(cited, str) else list(cited)
        return {
            "fact": str(fact.get("fact", "")),
            "citations": [id_map.get(str(e), str(e)) for e in cited],
        }

    raw_limitations = payload.get("limitations") or []
    if isinstance(raw_limitations, str):
        raw_limitations = [raw_limitations]
    limitations = [str(item) for item in raw_limitations]
    if rejections:
        limitations.append(
            _REJECTED_CITATIONS_NOTE + "; ".join(rejections)
        )
    key_facts, limitations, confidence = enforce_answer_gate(
        [remap(f) for f in payload.get("key_facts") or [] if isinstance(f, dict)],
        limitations,
        int(_numeric(payload.get("confidence")) or 0),
        {record.id for record in records},
    )
    return {
        "question": question,
        "bank": ", ".join(dict.fromkeys(doc.bank for doc in docs)),
        "periods": list(dict.fromkeys(doc.period for doc in docs)),
        "answer": str(payload.get("answer") or ""),
        "key_facts": key_facts,
        "confidence": confidence,
        "limitations": limitations,
        "evidence_records": [record.model_dump() for record in records],
    }


def run_agent_question(bank: str | None, question: str, combo_name: str = LIVE_COMBO,
                       periods: list[str] | None = None):
    """Answer one free-form question in the closed loop. Returns (output, out_dir).

    The signature is the one routing.question_runner_for hands to every caller,
    so no caller needs an adapter. `bank` and `periods` are hints from a caller
    that already knows them; a question that names its own banks and periods
    needs neither.
    """
    started, combo, deadline, llm = _start_run(combo_name)

    scope_notes: list[str] = []
    docs = documents_for_question(question, bank, periods, notes=scope_notes)
    if not docs:
        raise RuntimeError(
            f"no documents in corpus for {bank or 'the banks named'} "
            f"{'/'.join(periods or []) or 'in the question'}"
        )
    case, metric_cfg, registries = question_scope(question, docs)
    research = Research(
        llm, combo, docs, case, metric_cfg,
        next(iter(registries.values()), {}), registries,
        deadline_monotonic=deadline,
    )

    messages = [
        {"role": "system", "content": QUESTION_SYSTEM_PROMPT},
        {
            "role": "user",
            "content": QUESTION_PROMPT.format(
                question=question,
                # The scope note reaches the AGENT, not the reader alone. A
                # question about a period the corpus does not hold gets another
                # period's documents; an agent not told that spends its budget
                # hunting for pages that do not exist.
                period_note=(
                    "\nSCOPE OF THE DOCUMENTS YOU WERE GIVEN:\n"
                    + "\n".join(f"- {note}" for note in scope_notes)
                    + "\nResearch the periods the documents cover, and say which period every\n"
                    "figure belongs to.\n"
                    if scope_notes
                    else ""
                ),
                documents=_document_lines(docs),
            ),
        },
    ]
    payload, exhausted = research_loop(
        llm, combo, research, messages, QUESTION_SUBMIT_SPEC, started,
        deadline_monotonic=deadline,
    )
    if payload is None:
        payload = {
            "evidence": [{"id": record.id} for record in research.records],
            "answer": "",
            "key_facts": [],
            "confidence": 0,
            "limitations": [
                "The research loop ended without a submitted answer "
                f"({exhausted or 'the model stopped calling tools'})."
            ],
        }
    output = build_answer(payload, research, question, docs)
    # The scope note travels with the answer that rests on it, so a substituted
    # period is never silent.
    output["limitations"] = scope_notes + list(output["limitations"])
    if exhausted:
        output["limitations"].append(_stopped_early_note(exhausted))
    output["provenance"] = _provenance(combo, docs, started, llm, research, exhausted)

    out = OUT_DIR / f"ask-{slugify(question)}-{combo.name}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "answer.json").write_text(json.dumps(output, indent=2))
    (out / "answer.md").write_text(render_answer(output))
    return output, out


__all__ = [
    "QUESTION_SUBMIT_SPEC",
    "SUBMIT_SPEC",
    "TOOL_SPECS",
    "Research",
    "build_answer",
    "build_attribution",
    "finalise",
    "question_scope",
    "quote_key",
    "research_loop",
    "run_agent_case",
    "run_agent_question",
]
