"""CLI entry point: the surface the evaluators run (ticket 07)."""

from __future__ import annotations

import argparse
import json


def main() -> int:
    parser = argparse.ArgumentParser(prog="bank-equity-researcher")
    sub = parser.add_subparsers(dest="command", required=True)

    analyse = sub.add_parser("analyse", help="attribute a headline-metric movement")
    analyse.add_argument("--bank", required=True, help="e.g. CBA, NAB, WBC")
    analyse.add_argument("--metric", required=True, help="nim | cash_earnings | roe | cet1 | impairment | cti")
    analyse.add_argument("--period", required=True, help="e.g. FY26, 1H26")
    analyse.add_argument("--comparator", default=None, help="defaults: FY->prior FY, half->PCP")
    analyse.add_argument("--combo", default="agentic",
                         help="model combo: agentic | agentic-cheap | cheap | normal")

    ask = sub.add_parser("ask", help="answer a free-form question from the corpus")
    ask.add_argument("--bank", default=None,
                     help="e.g. CBA, NAB, WBC; omit when the question names its banks")
    ask.add_argument("--periods", default=None,
                     help="comma-separated, e.g. FY26,FY25; omit when the question names them")
    ask.add_argument("--question", required=True, help="the question to answer")
    ask.add_argument("--combo", default="agentic",
                     help="model combo: agentic | agentic-cheap | cheap | normal")

    discover_cmd = sub.add_parser("discover", help="agentically build a manifest for a bank")
    discover_cmd.add_argument("--bank", required=True)
    discover_cmd.add_argument("--periods", required=True, help="comma-separated, e.g. 1H26,1H25")
    discover_cmd.add_argument("--seed", required=True, help="the bank's homepage or IR page URL")

    evals_cmd = sub.add_parser("evals", help="run the eval harness")
    evals_cmd.add_argument("action", choices=["run", "crossref", "rescore", "judge"])
    evals_cmd.add_argument("--suite", default="dev",
                           help="dev | holdout | questions (free-form researcher questions)")
    evals_cmd.add_argument("--combo", default="cheap")
    evals_cmd.add_argument("--only", default=None,
                           help="run: subset filter for fast loops, comma-separated matches "
                                "against BANK-metric-PERIOD (e.g. 'cash_earnings' or 'nim-1H26')")
    evals_cmd.add_argument("--bank", default=None)
    # rescore: score saved out/*/attribution.json artifacts again, no model calls.
    evals_cmd.add_argument("--since", default=None,
                           help="rescore: skip artifacts generated before this ISO timestamp")
    evals_cmd.add_argument("--until", default=None,
                           help="rescore: skip artifacts generated after this ISO timestamp")
    evals_cmd.add_argument("--baseline", default=None,
                           help="rescore: a previous run's .jsonl to compare against")
    evals_cmd.add_argument("--label", default=None,
                           help="rescore: output file stem under evals/results/")
    args = parser.parse_args()

    if args.command == "evals":
        if args.action == "crossref":
            from .evals import run_crossref_suite

            card = run_crossref_suite(args.combo, args.bank)
        elif args.action == "judge":
            # Citation-grounding judge over SAVED out/*/ artifacts: it grades
            # each case's narrative checklist and calls no pipeline stage.
            from .evals import run_judge_suite

            card = run_judge_suite(args.suite, args.combo, args.bank)
        elif args.action == "rescore":
            from .evals import rescore

            card = rescore(args.suite, args.combo, args.bank, args.since, args.until,
                           args.baseline, args.label)
        elif args.suite == "questions":
            # Free-form researcher questions: the answer suite, scored on
            # location coverage and judged fact accuracy.
            from .evals import run_question_suite

            card = run_question_suite(args.combo, args.bank, only=args.only)
        else:
            from .evals import run_suite

            card = run_suite(args.suite, args.combo, args.bank, args.only)
        print("\n" + card.read_text())
        return 0

    if args.command == "ask":
        # The combo chooses the shell here exactly as it does for analyse.
        from .config import question_runner_for

        run_question = question_runner_for(args.combo)
        _, out_dir = run_question(
            args.bank.upper() if args.bank else None,
            args.question,
            args.combo,
            args.periods.split(",") if args.periods else None,
        )
        print((out_dir / "answer.md").read_text())
        print(f"\n[saved to {out_dir}]")
        return 0

    if args.command == "discover":
        from datetime import date

        from .discover import discover

        manifest = discover(args.bank, args.periods.split(","), args.seed, date.today().isoformat())
        print(json.dumps(manifest, indent=2))
        return 0

    # A combo chooses its own orchestration shell (ADR-0005): "agent" is the
    # closed-loop research agent, anything else is the open-loop pipeline. Both
    # shells write the same artifacts, so every downstream reader is unchanged.
    from .config import runner_for

    run_case = runner_for(args.combo)
    attribution, out_dir = run_case(args.bank.upper(), args.metric, args.period, args.comparator, args.combo)
    print((out_dir / "report.md").read_text())
    print(f"\n[saved to {out_dir}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
