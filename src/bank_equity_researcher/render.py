"""Deterministic markdown rendering of both artifacts — the attribution report
and the free-form answer. No model writes prose here; neither artifact can
contradict its own data."""

from __future__ import annotations

import re

from .validation.schema import Attribution


def _quote_line(ev_id: str, doc_id: str, pdf_page, printed_page, quote: str, indent: str = "") -> str:
    """One block-quote citation line. The "> " prefix is load-bearing:
    judge.answer_prose drops every line that starts with ">" before asking
    whether the note STATES a fact, so a pasted quote can never be mistaken
    for the note's own words. `indent` stays a parameter because that judge
    rule strips on lstrip() while render_answer nests quotes two spaces in."""
    page = f"printed p{printed_page}" if printed_page else f"PDF p{pdf_page}"
    return f'{indent}> [{ev_id}] {doc_id}, {page}: "{quote}"'


def _quote_lines(attribution: Attribution, evidence_ids: list[str]) -> list[str]:
    """One block-quote line per cited record, in the order the answer cites it.

    Block quotes, always: judge.answer_prose drops every line that starts with
    ">" before it asks whether the note STATES a fact, so a pasted quote can
    never be mistaken for the note's own words.
    """
    lines = []
    for ev_id in evidence_ids:
        record = next((r for r in attribution.evidence_records if r.id == ev_id), None)
        if record is None:
            continue
        lines.append(_quote_line(ev_id, record.doc_id, record.pdf_page,
                                 record.printed_page, record.quote))
    return lines


def render_report(attribution: Attribution) -> str:
    a = attribution
    lines: list[str] = []
    lines.append(f"# {a.bank} — {a.metric} — {a.period} vs {a.comparator}")
    lines.append("")
    if a.movement:
        m = a.movement
        lines.append(
            f"**Movement ({a.basis} basis):** {m.from_value:g}{m.unit} → {m.to_value:g}{m.unit} "
            f"({m.delta:+g}{m.unit}) | **Attribution confidence:** {a.attribution_confidence}/100"
        )
        if a.movement_source:
            # Which period COLUMN each endpoint came from: the only way a
            # reader can tell this movement from a half-on-half one.
            lines.append("")
            lines.append(f"*Read from: {a.movement_source}*")
    lines.append("")
    lines.append(a.headline)
    lines.append("")
    # The headline's own citations: the facts it carries belong to no driver,
    # so this is the only list a reader can check them against.
    headline_quotes = _quote_lines(a, a.headline_evidence)
    if headline_quotes:
        lines.extend(headline_quotes)
        lines.append("")

    quantified = [d for d in a.drivers if d.contribution]
    if quantified:
        lines.append("## Drivers")
        lines.append("")
        lines.append("| Driver | Bank's label | Contribution | Confidence | Sources | Evidence |")
        lines.append("|---|---|---|---|---|---|")
        for d in quantified:
            source_docs = {r.doc_id for r in a.evidence_records if r.id in d.evidence}
            corroboration = next(
                (c for c in d.checks_passed if c.startswith(("corroborated", "single_source", "cross_source"))),
                "",
            )
            lines.append(
                f"| `{d.canonical}` | {d.bank_label or '—'} | {d.contribution.value:+g} "
                f"{d.contribution.unit} | {d.confidence} | {len(source_docs)} ({corroboration}) "
                f"| {', '.join(d.evidence)} |"
            )
        if a.residual:
            lines.append(
                f"| *residual (unexplained)* | — | {a.residual.value:+g} {a.residual.unit} "
                "| — | — | — |"
            )
        lines.append("")

    if a.residual and not quantified:
        # The residual is part of the arithmetic story whether or not any
        # driver is quantified; it vanished from the report whenever the
        # table did not render (five saved artifacts hide non-zero residuals).
        lines.append(f"**Residual (unexplained): {a.residual.value:+g} {a.residual.unit}**")
        lines.append("")

    for d in a.drivers:
        lines.append(f"### {d.canonical}" + (f" — \"{d.bank_label}\"" if d.bank_label else ""))
        contribution = (
            f"{d.contribution.value:+g} {d.contribution.unit}" if d.contribution else "unquantified"
        )
        lines.append(f"*{contribution} | confidence {d.confidence}/100*")
        if d.checks_failed:
            lines.append(f"*Failed checks: {'; '.join(d.checks_failed)}*")
        lines.append("")
        lines.append(d.narrative)
        lines.extend(_quote_lines(a, d.evidence))
        lines.append("")

    if a.notable_items:
        lines.append("## Notable items")
        lines.extend(f"- {item}" for item in a.notable_items)
        lines.append("")
    if a.disagreements:
        lines.append("## Source disagreements")
        for dis in a.disagreements:
            lines.append(f"- **{dis.topic}** ({dis.reason.value}): " + " vs ".join(dis.values))
            lines.append(f"  Preferred: {dis.preferred}. {dis.explanation}")
        lines.append("")
    if a.limitations:
        lines.append("## Limitations")
        lines.extend(f"- {item}" for item in a.limitations)
        lines.append("")

    lines.append("## Provenance")
    for key, value in a.provenance.items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# The free-form ANSWER artifact
# --------------------------------------------------------------------------


def slugify(text: str, max_words: int = 8) -> str:
    words = re.findall(r"[a-z0-9]+", text.lower())[:max_words]
    return "-".join(words)[:64] or "question"


def case_slug(bank: str, metric: str, period: str, comparator: str, combo: str) -> str:
    """The out/<slug>/ name for a metric case. The WRITER (run_agent_case) and
    the READERS (evals rescore/judge via artifact_dir) must build the same
    name, or a rescore silently finds no artifact — so it is built here, once."""
    return f"{bank}-{metric}-{period}-vs-{comparator}-{combo}".lower()


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
                    lines.append(_quote_line(ev_id, record["doc_id"], record["pdf_page"],
                                             record.get("printed_page"), record["quote"],
                                             indent="  "))
        lines.append("")
    if output["limitations"]:
        lines += ["## Limitations"] + [f"- {item}" for item in output["limitations"]] + [""]
    lines.append("## Provenance")
    lines += [f"- {key}: {value}" for key, value in output["provenance"].items()]
    lines.append("")
    return "\n".join(lines)
