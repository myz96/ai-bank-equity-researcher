# Session state snapshot — 2026-08-29 ~14:15 HKT (pre-compaction)

Read this alongside map.md. Deadline: hard 2026-09-03, internal target 2026-09-01.

## Where the project stands

- All design tickets (01–07) resolved; POC → iteration → honest-eval loop mature.
- **Frozen dev baseline** (evals/results/baseline-20260829-devonly.md): 15/15 movements OK,
  Brier 0.058, confidently-wrong 0.0, 85+ claims 31/31 correct. All-cheap combo, ~$0.002/case.
- **Judge sweep** (20260829-0438-cheap-dev-judge.md): narrative checklist 1/43 (2%) — the
  why-layer gap, root cause = open-loop page starvation (footnotes/sub-splits never enter the
  page budget; pages read in isolation). THE headline open problem.
- Dev pool: 25 metric cases (CBA 15, NAB 5, WBC 5 — NAB/WBC non-NIM added 2026-08-29).
- Holdout estate: 8 frozen metric cases (Codex-designed slate, user-ratified: NAB/WBC NIM ×4 +
  CBA FY21 cash_earnings/impairment/cti/roe) + 4 crossref webs + 1 longitudinal = 13 in-repo
  (prospective quarantine) + 5 SEALED cases outside repo at ~/equity-holdout-sealed/ (four-bank
  NIM, ANZ impairment note, WBC consumer restatement, WBC CTI statutory, CBA credit cycle) +
  planned sealed holdout BANK (identity only in sealed README). Sealed dir must NEVER be
  referenced in repo/prompts/subagent briefs.

## UPDATE 2026-08-29 ~23:30 — overnight autonomous run

Everything below in "In-flight" COMPLETED. Current state:

- Ticket 27 dev-fix round: gated (leakage scan clean, only tolerance change is
  the new tighter COMPONENT_TOL $2m, 88 tests pass, scorecard verified) and
  committed at 9a9d13d. 25-case suite: Brier 0.035, confidently-wrong 0.0,
  85+ claims 36/36, no baseline case red. Three NAB/WBC first-run movement
  misses (NAB cti, WBC roe, WBC impairment) are logged, out of ticket scope.
- Bake-off COMPLETE, all five arms, four anchors each: cheap 0/15, glm 1/15,
  Sonnet 6/15, Fable 3/15, Codex 1/15 on the judge checklist; movements 4/4
  everywhere. Decision table + recommendation written into ticket 32.
  Verdict: reasoning tier is NOT the bottleneck; loop shape is. Round 2 =
  ticket 22 deterministic reference-following as the engineered arm.
- $130m FY25 notables gold RESTORED after page-sight (both PAs print it;
  52+33+45=130). Ticket 22 design section written. Codex trio was stuck in a
  paused sleep (machine slept through the quota-reset timer) — killed the
  timer, all three cases completed.
- glm-5.3 operational finding: author_max_tokens 24000 was too small on the
  densest bridge prompt (empty content x5); raised to 40000 in config.py.
- Spend check: key usage $3.07 of $100 limit (the account-level $177 figure
  is lifetime, not this project).

## In-flight at snapshot time — ALL DONE, see update above (kept for history)

1. **Dev-fix agent** (resumed after stream drop): component-column fix (cash_earnings 1H26
   0/3→2/3 verified single-case), completeness nudge, per-driver caps, extraction budget 6000
   tokens + column-order/divisional/basis rules. Finishing 25-case dev suite + report. Its
   uncommitted work spans author/taxonomy/pipeline/extract/validate/llm/schema.
2. **Research-loop bake-off (ticket 32 priority arm)** — four cases (CBA nim FY26,
   cash_earnings FY26, impairment FY26, nim FY21), five arms:
   - Cheap pipeline: baseline artifacts exist.
   - glm-5.3 same-context control: background bash b0a679cx9 (answers "reasoning or context?").
   - Sonnet agentic: COMPLETE 4/4 at ceiling (out/baseline-sonnet/) — found audited Note 2.2 on
     PDF p118 (appendix retrieval never reaches); made the correct PA-over-slide framing call
     (defect 20's ideal); FY21 7/7; cash bridge $0 residual conf 96; impairment dual
     decomposition conf 90 (report.md for impairment was written by ME after a subagent
     file-policy block).
   - Fable agentic: 4/4 (3 reused + impairment new: dual decomposition, +150/−17/−71 exact).
   - Codex agentic: 1/4 done (nim-fy26); 3 queued behind OpenAI quota reset 15:19 (background
     bash bxvhic4sf sleeps then runs).
   - Emerging verdict: numbers are tier-independent (cheap pipeline matches frontier); INSIGHT
     is loop-dependent (closed-loop wins at every tier); Sonnet ≈ Fable → research loop prices
     at midpoint tier. Pending: formal scoring funnel (gold adapter for benchmark-format JSON +
     judge sweep over all arms + cost table) → decision.
3. Sonnet independently confirmed the quarantined $130m FY25 notables level — one page-sight
   from gold restoration (evals/gold/cba-fy26-crossref.json).

## Next steps (ordered)

1. Gate + commit dev-fix round when it reports (leakage scan, tolerance diff, ownership).
2. Score the bake-off (adapter + judge sweep on out/baseline-*/), write the decision table into
   ticket 32; likely outcome: hybrid — cheap pipeline for numbers + a closed-loop research pass
   (Sonnet-tier) or deterministic reference-following (ticket 22) for the why-layer.
3. Ticket 22 build (reference-following: extracted "refer to page X"/footnote markers add pages
   to budget) — the cheap-tier counter to the insight gap; joins bake-off round 2.
4. Milestone (frozen commit): quarantine suite + sealed set one run + benchmark rerun + judge.
5. Write-up: README, design doc (4 decisions: tools/context/memory/evals), results, transcript.
   Protect a half-day. Buffer days are polish only.

## Open items on the user

- Sealed gold spot-check + optional own case in ~/equity-holdout-sealed/.
- Ratify crossref pass thresholds (coverage 1.0, fact accuracy 0.75) + partial-vs-stated rule.
- Eval-review-guide judgment calls 1/2/5 (tolerances, 85 boundary, min n).
- NEW: ratify the bake-off decision in ticket 32 (build ticket 22 first;
  hybrid with a Sonnet-tier research pass only if it half-works).
- NEW (from the dev-fix agent): the CBA 1H26 expense-framing choice — the
  answer claims underlying -348 + notables -170 = -518, which is exactly the
  value the 1H26 gold verifies on the combined row, but the FY26 gold verifies
  the underlying row. Choose: accept a split that sums to a verified parent,
  or settle one framing per bank. (Framing cap keeps both claims at 80
  meanwhile, so nothing reads confidently wrong.)

## Key facts easy to lose

- Spend: < USD 2.5 of 100 OpenRouter; Codex quota tight (resets 15:19); Fable/Sonnet agent
  tokens on Claude sub.
- Recovery playbook: agents stall on stream drops/quotas → SendMessage resume with context
  intact (proven ×6). Liveness proof = spend-delta + file mtimes + ListAgents, never vibes.
- The infra hardening story for the write-up: quota exhaustion, DNS outage, slow-drip streaming
  (wall-clock deadline in llm.py), truncated replies (chat_json retry), zsh word-splitting.
- Codex review (docs/reviews/codex-eval-review-2026-08-27.md) → tickets 28 (done), 29 (partial:
  judge landed, Wilson/coverage headers partial), 30 (done except user items), 31 (longitudinal
  done for NIM), 32 (in progress).
- Latest commit before snapshot: a89086c + judge/subset-filter commits (0230948, aea965f);
  uncommitted: dev-fix agent's working tree.
