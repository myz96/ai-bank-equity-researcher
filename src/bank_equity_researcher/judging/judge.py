"""The citation-grounding judge.

A narrative claim is quarantined from numeric calibration: a claim with no
published number is never scored against gold values. It is graded here
instead, by asking whether the note SAYS the claim and whether the note's own
cited quotes SUPPORT it.

Coverage is not correctness. Citing the right page proves the retriever found
the page. It does not prove the answer states the fact, and it does not prove
the quote entails the fact. So each fact gets two narrow questions, and each
question goes to two judges from different model families (config.Combo.judges):

1. Does the answer state this fact?      stated | partial | absent
2. Do the cited quotes entail this fact?  entailed | not-entailed

The two questions are two separate calls. One call is cheaper, but the judge
then reads its own "stated" answer before it rules on entailment, and a note
that confidently states a fact drags the entailment answer with it. Separate
calls keep the grounding question independent of the fluency question.

Verdict rules, in order:

- A judge reply that does not parse, or that answers outside the allowed
  vocabulary, makes the fact `flagged_for_human`. A judge that cannot answer
  the question is not evidence that the answer is right.
- Two judges that disagree ON THE VERDICT make the fact `flagged_for_human`.
  The disagreement is the finding; it is never resolved by a tie-break. One
  judge saying `partial` while the other says `absent` is not a verdict
  disagreement: both say the note does not state the fact, and the item fails
  under either reading. A human is flagged for a decision the judges could not
  make, never for a difference of wording, and the split is still recorded in
  the verdict reason.
- Both judges agreeing on `stated` AND `entailed` is a `pass`.
- Any other agreement is a `fail`.

Empty citations are `not-entailed` deterministically, and no entailment call is
made: nothing cannot entail anything, and asking a model to confirm that wastes
money.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# The "does the answer say it" vocabulary. `partial` is its own answer, not a
# soft pass: a note that names a driver but drops its load-bearing number has
# not stated the fact.
STATED = "stated"
PARTIAL = "partial"
ABSENT = "absent"
STATED_VALUES = (STATED, PARTIAL, ABSENT)

# The "do the cited quotes support it" vocabulary.
ENTAILED = "entailed"
NOT_ENTAILED = "not-entailed"
ENTAILMENT_VALUES = (ENTAILED, NOT_ENTAILED)

# The three verdicts. A flagged fact counts as neither a pass nor a fail; it is
# reported on its own so a run cannot hide behind an unreadable judge.
PASS = "pass"
FAIL = "fail"
FLAGGED = "flagged_for_human"

# Prompt budgets. The judge reads the note's prose and its cited quotes, never
# a whole PDF. Truncation is recorded in the verdict, so a reader can tell an
# absent fact from a fact that fell off the end of the window.
MAX_ANSWER_CHARS = 6000
MAX_QUOTE_CHARS = 4000
MAX_QUOTES = 24
# A judge answers one word plus a short reason; a large budget only pays for
# a model talking to itself.
JUDGE_MAX_TOKENS = 300

_TRUNCATION_MARK = "\n[... truncated for the judge ...]"

STATED_PROMPT = """You check whether a written analyst note states one specific fact.

FACT:
{fact}

NOTE (the analyst's own prose; source quotes were removed):
\"\"\"
{answer}
\"\"\"

Answer ONE question: does the NOTE state the FACT?

- "stated": the note says the fact in its own words, and any load-bearing
  number, direction or period in the fact agrees with the note.
- "partial": the note says part of the fact, or names the topic but drops the
  load-bearing number or direction, or states it for a different period.
- "absent": the note does not say the fact at all.

Rules:
- Do NOT judge whether the fact is true. Judge only whether the note says it.
- Do NOT use outside knowledge about the bank.
- The FACT may end with a bracketed source reference such as "(PA p28 text)".
  That reference is context for you. The note does not have to repeat it.

Reply with JSON only:
{{"stated": "stated|partial|absent", "why": "at most 20 words"}}"""

ENTAILMENT_PROMPT = """You check whether verbatim source quotes support one specific fact.

FACT:
{fact}

QUOTES (verbatim extracts from the bank's own documents; the only evidence you have):
{quotes}

Answer ONE question: do the QUOTES entail the FACT?

- "entailed": the quotes state the fact, or the fact follows from them directly.
  Every load-bearing number in the fact must appear in the quotes.
- "not-entailed": any part of the fact is unsupported by the quotes.

Rules:
- Use ONLY the quotes. Outside knowledge is not evidence.
- Plausibility is not entailment. "The bank probably means..." is not-entailed.
- The FACT may end with a bracketed source reference such as "(PA p28 text)".
  That reference is context for you. The quotes do not have to repeat it.

Reply with JSON only:
{{"entailed": "entailed|not-entailed", "why": "at most 20 words"}}"""


@dataclass(frozen=True)
class JudgeReply:
    """One judge model's answer to one narrow question."""

    model: str
    question: str  # "stated" | "entailed"
    answer: str | None
    why: str = ""
    error: str = ""


@dataclass(frozen=True)
class Verdict:
    """The combined ruling on one fact."""

    fact: str
    verdict: str  # PASS | FAIL | FLAGGED
    stated: str | None
    entailed: str | None
    reason: str
    replies: list[JudgeReply] = field(default_factory=list)
    answer_truncated: bool = False
    # How many quotes the judge actually read, and whether the character budget
    # dropped any. A verdict reached on a cut evidence window is a weaker
    # verdict, and the scorecard cannot say so unless the count is the true one.
    quotes_used: int = 0
    quotes_truncated: bool = False


def _truncate(text: str, limit: int) -> tuple[str, bool]:
    text = text or ""
    if len(text) <= limit:
        return text, False
    return text[:limit] + _TRUNCATION_MARK, True


def _fit_quotes(quotes: list[str], char_limit: int) -> tuple[str, int, bool]:
    """The quote block, how many quotes it holds, and whether any were dropped.

    Whole quotes only, and the count is the number the judge actually read: a
    half-quote at the cut can only push a judge towards NOT_ENTAILED, and a
    count taken before the cut overstates the evidence window.
    """
    lines: list[str] = []
    used = 0
    for index, quote in enumerate(quotes, start=1):
        line = f'{index}. "{quote}"'
        length = len(line) + (1 if lines else 0)
        if lines and sum(len(x) for x in lines) + len(lines) - 1 + length > char_limit:
            return "\n".join(lines) + _TRUNCATION_MARK, used, True
        lines.append(line)
        used += 1
    block = "\n".join(lines)
    # A single quote longer than the whole budget is still shown, cut, because
    # some grounding beats none. It is reported as truncated all the same.
    if len(block) > char_limit:
        return block[:char_limit] + _TRUNCATION_MARK, used, True
    return block, used, False


def _read_answer(reply, key: str, allowed: tuple[str, ...]) -> str:
    """Strict parsing: a reply outside the vocabulary is an error, not a guess.

    Models write "Stated", "not entailed" and "NOT-ENTAILED" for the same
    answer, so case and the space/hyphen slip are normalised. Anything else —
    "yes", a missing key, a list instead of an object — raises.
    """
    if not isinstance(reply, dict):
        raise TypeError(f"judge reply is {type(reply).__name__}, not a JSON object")
    if key not in reply:
        raise ValueError(f"judge reply has no {key!r} key: {str(reply)[:120]}")
    value = str(reply[key]).strip().lower().replace(" ", "-").replace("_", "-")
    if value not in allowed:
        raise ValueError(f"{key}={value!r} is outside {allowed}")
    return value


def _ask(llm, model: str, question: str, prompt: str, allowed: tuple[str, ...]) -> JudgeReply:
    """One judge, one question. Any failure becomes a recorded error reply."""
    try:
        raw = llm.chat_json(model, prompt, max_tokens=JUDGE_MAX_TOKENS)
    except Exception as exc:  # noqa: BLE001 - an unreachable judge is a flag, not a crash
        return JudgeReply(model=model, question=question, answer=None, error=f"call failed: {exc}"[:300])
    try:
        answer = _read_answer(raw, question, allowed)
    except (TypeError, ValueError) as exc:
        return JudgeReply(model=model, question=question, answer=None, error=str(exc)[:300])
    why = str(raw.get("why", ""))[:200] if isinstance(raw, dict) else ""
    return JudgeReply(model=model, question=question, answer=answer, why=why)


def judge_fact(
    llm,
    fact_text: str,
    answer_text: str,
    cited_quotes: list[str],
    judges: tuple[str, ...],
    max_quotes: int | None = None,
) -> Verdict:
    """Grade one fact with the two-judge, two-question protocol.

    `llm` is any object with `chat_json(model, prompt, max_tokens=...)`, so the
    tests drive the verdict table without a network call.

    `max_quotes` widens the evidence window past MAX_QUOTES for answer classes
    whose grounding is legitimately larger (a researcher-question answer cites
    ~40 records; the default window dropped 15 of them before entailment, so
    a MORE thorough answer lost grounding it actually had). The character
    budget scales with it. The default stays frozen for every existing suite.
    """
    limit = MAX_QUOTES if max_quotes is None else max_quotes
    char_limit = MAX_QUOTE_CHARS * max(1, (limit + MAX_QUOTES - 1) // MAX_QUOTES)
    answer, truncated = _truncate(answer_text, MAX_ANSWER_CHARS)
    quotes = [q for q in (cited_quotes or []) if str(q).strip()][:limit]
    quote_block, quotes_used, quotes_truncated = _fit_quotes(quotes, char_limit)

    replies: list[JudgeReply] = []
    for model in judges:
        replies.append(
            _ask(
                llm,
                model,
                STATED,
                STATED_PROMPT.format(fact=fact_text, answer=answer),
                STATED_VALUES,
            )
        )
        if quotes:
            replies.append(
                _ask(
                    llm,
                    model,
                    ENTAILED,
                    ENTAILMENT_PROMPT.format(fact=fact_text, quotes=quote_block),
                    ENTAILMENT_VALUES,
                )
            )

    return _combine(fact_text, replies, bool(quotes), truncated, quotes_used, quotes_truncated)


def _combine(
    fact_text: str,
    replies: list[JudgeReply],
    has_quotes: bool,
    truncated: bool,
    quotes_used: int,
    quotes_truncated: bool = False,
) -> Verdict:
    def answers(question: str) -> set[str]:
        return {r.answer for r in replies if r.question == question and r.answer}

    def build(verdict: str, stated: str | None, entailed: str | None, reason: str) -> Verdict:
        return Verdict(
            fact=fact_text,
            verdict=verdict,
            stated=stated,
            entailed=entailed,
            reason=reason,
            replies=replies,
            answer_truncated=truncated,
            quotes_used=quotes_used,
            quotes_truncated=quotes_truncated,
        )

    errors = [f"{r.model} ({r.question}): {r.error}" for r in replies if r.error]
    if errors:
        return build(FLAGGED, None, None, "unreadable judge reply — " + "; ".join(errors))

    notes: list[str] = []
    stated_answers = answers(STATED)
    if len(stated_answers) == 1:
        stated, stated_split = stated_answers.pop(), None
    elif stated_answers <= {PARTIAL, ABSENT}:
        # Both judges say the note does not state the fact; they differ only on
        # how much of it is missing. The verdict is the same either way, so the
        # item fails here instead of costing a human a review. The split is
        # still recorded.
        stated, stated_split = PARTIAL, None
        notes.append(f"judges split {sorted(stated_answers)}, both short of stated")
    else:
        stated, stated_split = None, f"stated: judges answered {sorted(stated_answers)}"

    if not has_quotes:
        # Nothing cited entails nothing. No call was made, so no judge can
        # disagree with this.
        entailed, entailed_split = NOT_ENTAILED, None
        notes.append("no quote was cited to entail it")
    else:
        entailed_answers = answers(ENTAILED)
        if len(entailed_answers) == 1:
            entailed, entailed_split = entailed_answers.pop(), None
        else:
            entailed, entailed_split = None, f"entailed: judges answered {sorted(entailed_answers)}"

    splits = [msg for msg in (stated_split, entailed_split) if msg]
    if splits:
        return build(FLAGGED, stated, entailed, "judges disagree — " + "; ".join(splits))

    detail = f" ({'; '.join(notes)})" if notes else ""
    if stated == STATED and entailed == ENTAILED:
        return build(PASS, stated, entailed,
                     f"the answer states the fact and the cited quotes entail it{detail}")
    return build(FAIL, stated, entailed, f"stated={stated}; entailed={entailed}{detail}")


def judge_facts(
    llm,
    facts: list[str],
    answer_text: str,
    cited_quotes: list[str],
    judges: tuple[str, ...],
    max_quotes: int | None = None,
) -> dict:
    """Grade a list of facts and summarise them, coverage first.

    `passed` counts only facts that are BOTH stated and entailed. A flagged
    fact is never counted as a pass, and its count is reported beside the rate
    so a run with many flags cannot read as a clean result.
    """
    verdicts = [
        judge_fact(llm, fact, answer_text, cited_quotes, judges, max_quotes=max_quotes)
        for fact in facts
    ]
    passed = sum(1 for v in verdicts if v.verdict == PASS)
    flagged = [v for v in verdicts if v.verdict == FLAGGED]
    # The two flag causes need different work. A split needs a human to read
    # the fact; an unreadable or unreachable judge needs the run repeating.
    # One count for both hides which.
    flagged_split = sum(1 for v in flagged if v.reason.startswith("judges disagree"))
    flagged_unreadable = len(flagged) - flagged_split
    flagged = len(flagged)
    stated_not_entailed = sum(
        1 for v in verdicts if v.verdict == FAIL and v.stated == STATED and v.entailed == NOT_ENTAILED
    )
    not_stated = sum(1 for v in verdicts if v.verdict == FAIL and v.stated in (PARTIAL, ABSENT))
    total = len(verdicts)
    return {
        "status": "judged",
        "judges": list(judges),
        "total": total,
        "passed": passed,
        "failed": total - passed - flagged,
        "flagged": flagged,
        "flagged_split": flagged_split,
        "flagged_unreadable": flagged_unreadable,
        "stated_not_entailed": stated_not_entailed,
        "not_stated": not_stated,
        "fact_accuracy": f"{passed}/{total}" if total else "n/a (no facts)",
        "accuracy_fraction": round(passed / total, 3) if total else None,
        "answer_truncated": any(v.answer_truncated for v in verdicts),
        "quotes_used": verdicts[0].quotes_used if verdicts else 0,
        "quotes_truncated": any(v.quotes_truncated for v in verdicts),
        "facts": [_verdict_dict(v) for v in verdicts],
    }


def _verdict_dict(verdict: Verdict) -> dict:
    return {
        "fact": verdict.fact,
        "verdict": verdict.verdict,
        "stated": verdict.stated,
        "entailed": verdict.entailed,
        "reason": verdict.reason,
        "replies": [
            {"model": r.model, "question": r.question, "answer": r.answer, "why": r.why, "error": r.error}
            for r in verdict.replies
        ],
    }


# ---------------------------------------------------------------------------
# Artifact adapters: what the judge reads out of a saved out/<slug>/ case.
# ---------------------------------------------------------------------------


def answer_prose(report_md: str) -> str:
    """The note's own words: report.md without its quote lines or provenance.

    The quotes must not reach the "does the answer state this" question. A note
    that pastes a quote saying the fact has not stated the fact itself, and a
    judge reading both cannot tell the two apart.
    """
    body = report_md.split("## Provenance")[0]
    return "\n".join(line for line in body.splitlines() if not line.lstrip().startswith(">")).strip()


def cited_quotes(attribution: dict) -> list[str]:
    """The verbatim quotes of the evidence records the ANSWER actually cites.

    An answer cites a record in two places, and both are its own citations: a
    DRIVER's evidence list, and the HEADLINE's. A headline states facts that
    belong to no single driver — the movement as a second document states it,
    the statutory-versus-cash framing, the summary measures the bank leads with
    — so a headline-only fact reading driver lists alone could never be
    entailed however well the answer had sourced it.

    Records the answer never cited are not the answer's grounding, so they are
    not evidence for it here.

    MAX_QUOTES bounds the window, and the two lists share it: neither may
    starve the other. Drivers cite many records and a headline cites few, so
    the drivers take every slot the headline does not need, and never fewer
    than half.
    """
    driver_ids = {e for driver in attribution.get("drivers", []) for e in driver.get("evidence", [])}
    headline_ids = {e for e in (attribution.get("headline_evidence") or [])} - driver_ids
    records = attribution.get("evidence_records", [])

    def quotes_of(wanted: set) -> list[str]:
        return [r["quote"] for r in records if r.get("id") in wanted and r.get("quote")]

    driver_quotes, headline_quotes = quotes_of(driver_ids), quotes_of(headline_ids)
    driver_room = MAX_QUOTES - min(len(headline_quotes), MAX_QUOTES // 2)
    kept = driver_quotes[:driver_room]
    return kept + headline_quotes[: MAX_QUOTES - len(kept)]


__all__ = [
    "ABSENT",
    "ENTAILED",
    "FAIL",
    "FLAGGED",
    "NOT_ENTAILED",
    "PARTIAL",
    "PASS",
    "STATED",
    "JudgeReply",
    "Verdict",
    "answer_prose",
    "cited_quotes",
    "judge_fact",
    "judge_facts",
]
