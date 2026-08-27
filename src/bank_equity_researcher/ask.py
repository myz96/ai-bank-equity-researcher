"""Free-form question answering over the corpus (ticket 26): hybrid
retrieval with model-generated query variants, evidence extraction, and an
answer author under the same never-guess rules as the attribution author."""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone

from .config import COMBOS, OUT_DIR
from .corpus import Document, documents_for_period
from .extract import extract_text_evidence
from .llm import LLM
from .retrieve import retrieve
from .schema import EvidenceRecord

MAX_ASK_PAGES = 12
# Per-document cap so one long book cannot crowd out the other documents —
# cross-reference questions need evidence consolidated across documents.
MAX_PAGES_PER_DOC = 6
MAX_AUTHOR_ROUNDS = 2

# Source hierarchy rank, mirrored from the pipeline (which owns its own copy
# inside run_case; pipeline.py is not importable state).
DOC_TYPE_RANK = {
    "profit_announcement": 0, "results_announcement": 0, "results_book": 0,
    "results_presentation": 1, "investor_presentation": 1, "investor_discussion_pack": 1,
    "pre_results_note": 2,
    "asx_announcement": 3,
}

VARIANTS_PROMPT = """You write retrieval queries for Australian bank results \
documents (profit announcements, results presentations, investor packs).

QUESTION: {question}

Return JSON only: a list of 3 short search queries that would find the pages
answering the question. Use different vocabulary in each: the bank's own
jargon, likely table row labels, and likely footnote wording. No explanations."""

ANSWER_PROMPT = """You are a first-pass banking-sector equity research analyst.

TASK: answer this question about {bank} using the periods {periods}:

QUESTION: {question}

EVIDENCE RECORDS (the only facts you may use; cite records by id):
{evidence}

SOURCE HIERARCHY when sources disagree: audited statements and Profit
Announcement tables > Profit Announcement narrative > presentation slides >
transcripts > else. Restated comparatives from the newer document win.

ABSOLUTE RULES — never break these:
1. NEVER GUESS. Every number you state must come from an evidence record you
   cite. A key fact containing a number without evidence ids will be deleted
   by the validator. If you do not know, say so in limitations.
2. Consolidate. The answer may require combining a chart value, a footnote,
   and narrative text from different pages or documents. Cite every location
   that carries part of the answer, not just one.
3. State the basis (cash / statutory) where it matters, and the period each
   number belongs to.
4. Confidence is 0-100: the probability the answer would be judged correct
   against the bank's own disclosure. A claim seen in only one document must
   not exceed confidence 85.
5. State limitations honestly: anything the question asks for that the
   evidence does not establish, and any caveat that changes interpretation.

Reply with JSON only, in this exact shape:
{{"answer": "<=200 words, the direct answer with the load-bearing numbers>",
  "key_facts": [{{"fact": "<one fact, <=40 words>", "evidence": ["ev-1", ...]}}],
  "confidence": int,
  "limitations": ["..."]}}

If — and only if — one specific missing table, footnote, or section blocks
you, reply instead with: {{"request_evidence": "<one retrieval query>"}}
(you may do this at most {rounds_left} more time(s))."""


def _slugify(text: str, max_words: int = 8) -> str:
    words = re.findall(r"[a-z0-9]+", text.lower())[:max_words]
    return "-".join(words)[:64] or "question"


def _query_variants(llm: LLM, model: str, question: str) -> list[str]:
    """2-3 model-generated retrieval variants; a failure falls back to none."""
    try:
        raw = llm.chat_json(model, VARIANTS_PROMPT.format(question=question), max_tokens=500)
    except Exception as exc:  # noqa: BLE001 - variants are best-effort, never fatal
        print(f"[ask] query-variant generation failed, using the question alone: {exc}", file=sys.stderr)
        return []
    return [str(q) for q in raw if isinstance(q, str)][:3] if isinstance(raw, list) else []


def render_answer(output: dict) -> str:
    lines = [f"# Q: {output['question']}", ""]
    lines += [
        (
            f"*{output['bank']}, periods {', '.join(output['periods'])} — "
            f"confidence {output['confidence']}/100*"
        ),
        "",
    ]
    lines += [output["answer"], ""]
    records = {r["id"]: r for r in output["evidence_records"]}
    if output["key_facts"]:
        lines += ["## Key facts", ""]
        for fact in output["key_facts"]:
            lines.append(f"- {fact['fact']}")
            for ev_id in fact["evidence"]:
                record = records.get(ev_id)
                if record:
                    page = (f"printed p{record['printed_page']}" if record.get("printed_page")
                            else f"PDF p{record['pdf_page']}")
                    lines.append(f"  > [{ev_id}] {record['doc_id']}, {page}: \"{record['quote']}\"")
        lines.append("")
    if output["limitations"]:
        lines += ["## Limitations"] + [f"- {item}" for item in output["limitations"]] + [""]
    lines.append("## Provenance")
    lines += [f"- {key}: {value}" for key, value in output["provenance"].items()]
    lines.append("")
    return "\n".join(lines)


def run_ask(bank: str, periods: list[str], question: str, combo_name: str = "cheap"):
    """Answer a free-form question from the corpus. Returns (output_dict, out_dir)."""
    started = time.time()
    combo = COMBOS[combo_name]
    llm = LLM()
    bank = bank.upper()

    docs = documents_for_period(bank, *periods)
    if not docs:
        raise RuntimeError(f"no documents in corpus for {bank} {'/'.join(periods)}")
    doc_by_id: dict[str, Document] = {d.doc_id: d for d in docs}

    # 1. Retrieve candidate pages: the question plus 2-3 model variants,
    # unioned per (doc, page) keeping the best score.
    queries = [question] + _query_variants(llm, combo.extract, question)
    candidates: dict[tuple[str, int], float] = {}
    for query in queries:
        for doc in docs:
            for page, score in retrieve(doc, query, top_k=4):
                key = (doc.doc_id, page)
                candidates[key] = max(candidates.get(key, 0.0), score)

    # 2. Order pages: primary period (first in --periods) first, then the
    # source hierarchy, then retrieval score; cap per document for diversity.
    primary = periods[0]

    def page_order(dp: tuple[str, int]):
        doc = doc_by_id[dp[0]]
        return (
            0 if doc.period == primary else 1,
            DOC_TYPE_RANK.get(doc.doc_type, 4),
            -candidates.get(dp, 0.0),
            dp[1],
        )

    pages: list[tuple[str, int]] = []
    per_doc: dict[str, int] = {}
    for dp in sorted(candidates, key=page_order):
        if len(pages) >= MAX_ASK_PAGES:
            break
        if per_doc.get(dp[0], 0) >= MAX_PAGES_PER_DOC:
            continue
        pages.append(dp)
        per_doc[dp[0]] = per_doc.get(dp[0], 0) + 1

    # 3. Extract evidence from the selected pages.
    counter = iter(range(1, 1000))
    next_id = lambda: f"ev-{next(counter)}"
    records: list[EvidenceRecord] = []
    for doc_id, page in pages:
        records.extend(
            extract_text_evidence(llm, combo.extract, doc_by_id[doc_id], page, question, next_id)
        )

    # 4. Author the answer, with the bounded evidence-request hook.
    def fetch_more(query: str) -> list[EvidenceRecord]:
        extra: list[EvidenceRecord] = []
        for doc in docs:
            for page, score in retrieve(doc, query, top_k=2):
                if (doc.doc_id, page) not in candidates:
                    candidates[(doc.doc_id, page)] = score
                    extra.extend(
                        extract_text_evidence(llm, combo.extract, doc, page, question, next_id)
                    )
        return extra

    reply: dict = {}
    for round_no in range(MAX_AUTHOR_ROUNDS + 1):
        prompt = ANSWER_PROMPT.format(
            bank=bank,
            periods=", ".join(periods),
            question=question,
            evidence=json.dumps([r.model_dump() for r in records], indent=1),
            rounds_left=MAX_AUTHOR_ROUNDS - round_no,
        )
        reply = llm.chat_json(combo.author, prompt, max_tokens=combo.author_max_tokens)
        if isinstance(reply, dict) and "request_evidence" in reply and round_no < MAX_AUTHOR_ROUNDS:
            records.extend(fetch_more(str(reply["request_evidence"])))
            continue
        break
    if not isinstance(reply, dict) or "answer" not in reply:
        raise RuntimeError(f"answer author returned no answer: {str(reply)[:200]}")

    # 5. The never-guess gate, mirrored from schema.enforce_evidence_gate:
    # a key fact carrying a number with no resolvable evidence id is deleted,
    # and the deletion is logged, never silent.
    raw_limitations = reply.get("limitations", []) or []
    if isinstance(raw_limitations, str):  # models sometimes return one string
        raw_limitations = [raw_limitations]
    limitations = [str(item) for item in raw_limitations]
    known_ids = {record.id for record in records}
    key_facts: list[dict] = []
    for item in reply.get("key_facts", []):
        if not isinstance(item, dict):
            continue
        evidence = item.get("evidence", [])
        evidence = [evidence] if isinstance(evidence, str) else list(evidence)
        resolved = [e for e in evidence if e in known_ids]
        fact = str(item.get("fact", ""))
        if re.search(r"\d", fact) and not resolved:
            limitations.append(f"Stripped unsupported quantified fact: \"{fact[:80]}\"")
            continue
        key_facts.append({"fact": fact, "evidence": resolved})

    confidence = int(reply.get("confidence", 0) or 0)
    if not key_facts:
        confidence = min(confidence, 20)

    output = {
        "question": question,
        "bank": bank,
        "periods": periods,
        "answer": str(reply.get("answer", "")),
        "key_facts": key_facts,
        "confidence": confidence,
        "limitations": limitations,
        "evidence_records": [r.model_dump() for r in records],
        "provenance": {
            "combo": combo.name,
            "models": f"extract={combo.extract}, author={combo.author}",
            "documents": ", ".join(f"{d.doc_id} ({(d.sha256 or '')[:12]})" for d in docs),
            "queries": queries,
            "pages_read": [f"{doc_id} p{page}" for doc_id, page in pages],
            "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "seconds": round(time.time() - started, 1),
            "cost_usd": round(llm.usage.cost_usd, 4),
            "tokens": f"{llm.usage.prompt_tokens} in / {llm.usage.completion_tokens} out",
        },
    }

    # 6. Save.
    out = OUT_DIR / f"ask-{bank.lower()}-{_slugify(question)}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "answer.json").write_text(json.dumps(output, indent=2))
    (out / "answer.md").write_text(render_answer(output))
    return output, out


__all__ = ["render_answer", "run_ask"]
