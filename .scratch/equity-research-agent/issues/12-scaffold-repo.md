# 12 — Scaffold the repo

Type: task
Status: resolved

## Question

Stand up the project skeleton so every later ticket has a home: `git init`; `uv` project layout with `pytest`; MIT license; README stub; gitignore covering `data/` and secrets; create the private GitHub remote `myz96/ai-bank-equity-researcher` and push. The answer records the repo URL and the layout chosen. AFK.

## Answer

Done. The repo is `https://github.com/myz96/ai-bank-equity-researcher` (private, branch `main`, root commit a966e96).

Layout: `uv` library layout with package `src/bank_equity_researcher/`; dev deps `pytest` and `ruff`; `requires-python >=3.12`; MIT license (Michael Zhao, 2026); README stub describing the problem and layout; `.gitignore` covers `.venv`, `.env`, and the `data/` document cache. The wayfinder map, tickets, research findings, glossary, and agent config are committed — the process record is part of the deliverable.
