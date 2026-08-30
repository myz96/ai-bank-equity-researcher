# Holdout milestone runbook (Mon night, 2026-08-31)

The generalisation test. Everything below runs ONCE, on frozen code, and the
results go into the report as-is — no per-case feedback, no re-runs except a
documented infrastructure failure (an API 402/timeout is infrastructure; a
wrong answer is a result).

## 0. Freeze

1. Confirm the working tree is clean and tests pass:
   `git status --short` (empty) and `uv run python -m pytest tests/ -q`.
2. Tag the freeze: `git tag holdout-freeze-20260831 && git log -1 --oneline`.
3. Record the tag in the report. Every holdout artifact's provenance must
   show code from this commit.

## 1. Quarantine tier (in-repo, I run these)

```bash
set -a; source .env; set +a
# 8 frozen metric cases (NAB/WBC NIM x4, CBA FY21 x4)
uv run bank-equity-researcher evals run --suite holdout --combo agentic
# 4 crossref webs + the FY21->FY26 longitudinal (all case_class crossref)
uv run bank-equity-researcher evals crossref --combo agentic
```

Also the unseen-bank probe (cold start, registry entry intentionally thin):

```bash
uv run bank-equity-researcher analyse --bank ANZ --metric nim --period 1H26 --combo agentic
uv run bank-equity-researcher analyse --bank ANZ --metric impairment --period 1H26 --combo agentic
```

Estimated cost: ~8 x $0.6 + 5 webs x $0.8 + 2 ANZ x $0.7 ≈ $11 (opus).

## 2. Sealed tier (user-administered)

Per the sealed protocol: the user opens the sealed directory OUTSIDE this
repo, follows its own README, and runs the commands it specifies against the
frozen tag. Results are recorded there first, then the totals (not the
per-case gold) come back for the report. No sealed content enters the repo,
prompts, or any agent brief.

## 3. After the run

- One scorecard block per tier goes into the report verbatim, labelled with
  the freeze tag. Failures ship as failures.
- The dev-vs-holdout delta is the headline generalisation number.
- Tuesday's cleanup (ticket 33) is behaviour-neutral BY GATE: after the six
  passes, a dev subset re-runs and must score identically to the freeze tag.
