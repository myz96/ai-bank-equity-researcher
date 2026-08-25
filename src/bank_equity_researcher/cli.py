"""CLI entry point: the surface the evaluators run (ticket 07)."""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(prog="bank-equity-researcher")
    sub = parser.add_subparsers(dest="command", required=True)

    analyse = sub.add_parser("analyse", help="attribute a headline-metric movement")
    analyse.add_argument("--bank", required=True, help="e.g. CBA, NAB, WBC")
    analyse.add_argument("--metric", required=True, help="nim | cash_earnings | roe | cet1 | impairment | cti")
    analyse.add_argument("--period", required=True, help="e.g. FY26, 1H26")
    analyse.add_argument("--comparator", default=None, help="defaults: FY->prior FY, half->PCP")
    analyse.add_argument("--combo", default="cheap", help="model combo: cheap | normal")
    args = parser.parse_args()

    from .pipeline import run_case

    attribution, out_dir = run_case(args.bank.upper(), args.metric, args.period, args.comparator, args.combo)
    print((out_dir / "report.md").read_text())
    print(f"\n[saved to {out_dir}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
