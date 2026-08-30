# ADR-0005 — Quality-first closed-loop research agent

Status: accepted 2026-08-30 (user-ratified).

## Context

The five-arm bake-off (ticket 32) established two facts. Movement numbers are
tier-independent and loop-independent: every arm, including the cheapest
pipeline, scored 4/4. The why-layer is loop-dependent: open-loop context
assembly scored 0-1/15 on the narrative checklist regardless of reasoner
price, while every closed-loop agent beat it.

Ticket 22 then tested whether code can imitate a closed loop cheaply:
deterministic reference-following reached 3/15 against the closed-loop 6/15,
at the price of bank-format-specific regexes — a new fragility surface for
every unseen bank. For an agent whose stated test is generalisation to unseen
banks, that trade is wrong.

The user has set the objective explicitly: build the most accurate and most
generalisable bank equity researcher possible. A budget exists as a rail, not
as a target. Cost is a secondary consideration and is never the thing being
optimised.

## Decision

1. The research loop is a closed-loop tool-use agent: it reads, reasons, and
   chooses what to read next. The default model is the strongest reliably
   tool-calling model available, not the cheapest workable one.
2. The deterministic estate is not retired — it is re-scoped along the
   ADR-0004 boundary, which the bake-off located empirically. Navigation and
   synthesis are "unknown" and belong to the agent. Arithmetic, sign and
   basis conventions, comparison classification, confidence caps, citation
   gates, and scoring are "known" and stay code: they become the agent's
   tools and the post-hoc verifiers of its output.
3. No workarounds that imitate agent behaviour in code. A general mechanism
   beats a shortcut special-cased to a bank or a document shape, even when
   the shortcut is cheaper. Simplicity still binds: general and simple, not
   clever and brittle.
4. Cheap-model combos survive only as comparison arms. They measure how much
   the model tier buys inside a closed loop; they are not the product.
5. Cost ceilings, tool-call caps and wall-clock deadlines remain as runaway
   protection, set generously enough that they never shape a normal run.

## Consequences

- Ticket 22's reference follower retires as a primary path. `refs.py`
  survives as an agent tool (`follow_references`), where it is a capability
  instead of a workaround.
- The artifact contract, validators, confidence caps and the eval harness
  are unchanged: they are answerer-agnostic and score the agent exactly as
  they scored the pipeline. The frozen quarantine and sealed sets remain the
  final generalisation test.
- The open-loop pipeline remains in the repo as the measured baseline and as
  the bake-off's control arm.
