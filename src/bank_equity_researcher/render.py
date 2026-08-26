"""Deterministic markdown report rendered from the attribution JSON (ticket 06).
No model writes prose here; the report cannot contradict its own data."""

from __future__ import annotations

from .schema import Attribution


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
    lines.append("")
    lines.append(a.headline)
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
            lines.append(f"| *residual (unexplained)* | — | {a.residual.value:+g} {a.residual.unit} | — | — |")
        lines.append("")

    narrative = [d for d in a.drivers if not d.contribution]
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
        for ev_id in d.evidence:
            record = next((r for r in a.evidence_records if r.id == ev_id), None)
            if record:
                page = f"printed p{record.printed_page}" if record.printed_page else f"PDF p{record.pdf_page}"
                lines.append(f"> [{ev_id}] {record.doc_id}, {page}: \"{record.quote}\"")
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
    del narrative
    return "\n".join(lines)
