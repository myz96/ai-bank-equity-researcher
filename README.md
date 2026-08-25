# ai-bank-equity-researcher

An agent that does first-pass banking-sector equity research on Australian banks.

Given a bank, a reporting period, and a headline metric, the agent explains how the metric moved against the prior comparable period, attributes the movement to drivers, and produces a confidence-rated attribution that cites the evidence behind each driver.

**Metrics in scope:** net interest margin, cash earnings, return on equity, CET1 ratio, credit impairment charge, cost-to-income ratio. All figures in AUD. Periods follow each bank's own financial calendar.

**Status:** under construction. The project is driven by a wayfinder map at `.scratch/equity-research-agent/map.md`; the design doc and eval results will land here as they are produced.

## Layout

- `src/bank_equity_researcher/` — the agent
- `docs/` — design doc, ADRs, agent configuration
- `CONTEXT.md` — the domain glossary
- `data/` (gitignored) — the document cache, rebuilt from a committed manifest
- `.scratch/equity-research-agent/` — the wayfinder map and decision tickets
