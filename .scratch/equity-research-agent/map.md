# Map: equity-research-agent

Label: wayfinder:map

## Destination

A shared GitHub repo (`myz96/ai-bank-equity-researcher`) that contains a working banking-sector equity-research agent, an eval harness with recorded results, a README, a design doc with the rationale for the four owned decisions (tools, context management, memory, evals), and the saved coding-agent session transcript. Banks: CBA (POC), then NAB and Westpac.

## Notes

- Execution is carried into this map (agreed at charting): build steps are `task` tickets, and the map is done when the deliverable ships.
- Deadline: 2026-09-01. Quality beats speed; cut from iteration first if time runs short.
- Stack: Python 3.12+, `uv`, `pytest`. Model gateway: OpenRouter (`OPENROUTER_API_KEY`), chosen so cheap OSS models can be swapped in.
- Spend policy: under AUD 50 total for model runs. Develop and iterate on cheap models; run the normal model late and only when needed.
- Model slate (2026-08-25, from the live OpenRouter catalogue): cheap `qwen/qwen3.7-flash`; normal author `z-ai/glm-5.3`; cross-family judge `deepseek/deepseek-v4-pro-0813`; `stealth/ox-alpha` (free alpha, strong on recent evals) featured in every prototype arm with glm-5.3 as stable fallback; `moonshotai/kimi-k3` as vision ceiling reference. Final combinations are eval-decided.
- Repo: private under `myz96`, MIT license. Reviewers get access at the end; transcript attached at the end.
- Documents: never commit PDFs. Commit a manifest (URLs, checksums, metadata) plus a fetch script that fills a gitignored `data/` cache. The agent may fetch live on a cache miss. Evals run from the cache.
- Comparison defaults: full-year input compares against the prior full year; half-year input compares against the PCP (same half, one year earlier). The agent always names its comparator.
- Eval axes are period-types, not lengths: a half-year result, a full-year result, and at least one older period (format drift is the robustness test and a stand-in for the unseen case).
- Named eval case: the cash-vs-statutory earnings disagreement.
- Unseen-case posture: no hard-coded banks. A bank registry plus generic document discovery; honest uncertainty in output when disclosure is thin.
- Skills: grilling tickets use /grilling + /domain-modeling (that pair is /grill-with-docs). Research tickets use /research background subagents. The glossary lives in `CONTEXT.md`; qualifying decisions get ADRs in `docs/adr/`.
- Prose shown to the user follows ASD-STE100 (user's global CLAUDE.md).
- Pace note (user, 2026-08-25): work tickets back-to-back in the current conversation until a first CBA POC produces inspectable results. No steps are skipped: grilling tickets stay HITL, and every resolution still gets the user's confirmation before the ticket closes.

## Decisions so far

<!-- one line per closed ticket: gist + link -->

- [09 — NAB disclosure inventory](issues/09-nab-disclosure-inventory.md) — the half-year results book is the master document (NIM walk printed p22; cash-to-statutory reconciliation printed pp100–101); no Excel P&L pack since FY20, so P&L comes from PDFs; cash earnings is the primary basis; full-year format broke at FY21; scrape the results landing page, do not construct URLs.
- [10 — Westpac disclosure inventory](issues/10-westpac-disclosure-inventory.md) — Westpac dropped cash earnings at 1H23 (now statutory net profit + "excluding Notable Items"), which sharpens the cash-vs-statutory eval case; a "Key Financial Information" Excel pack exists since 1H23; NIM walk in IDP slide 24 and announcement p7 (1H26); format breaks at 1H23 and 1H25; scrape landing pages, filenames drift.
- [08 — CBA disclosure inventory](issues/08-cba-disclosure-inventory.md) — FY26 results published 12 Aug 2026 (freshest possible POC period); no Excel P&L pack, so PDF parsing is unavoidable; NIM walk at Profit Announcement printed p12 (printed page = PDF page − 16); cash-vs-statutory reconciliation at Appendix 6.3; FY20/21 PDFs are AES-encrypted; division changes since FY20 break time series; scrape links, never template URLs.
- [12 — Scaffold the repo](issues/12-scaffold-repo.md) — repo live at https://github.com/myz96/ai-bank-equity-researcher (private, `main`); uv library layout, pytest + ruff, MIT; map and tickets are committed as part of the deliverable.
- [11 — Decomposition conventions](issues/11-decomposition-conventions.md) — NIM walks share one stable driver set across the four majors (labels differ per bank); core-profit vocabulary diverges hardest (cash earnings / cash profit / cash NPAT / ex-Notables); CET1 walk convention is standard with IRRBB as a separate volatile bar; a cross-bank canonical driver taxonomy with per-bank label mappings is viable.
- [01 — Driver taxonomy and decomposition](issues/01-driver-taxonomy-and-decomposition.md) — canonical cross-bank taxonomy with per-bank label maps; walk-first layered method (extract walks → derive ROE/CTI arithmetically → narrative marked unquantified) plus deterministic validation in code; explicit residuals; notable items first-class; basis always tagged. Artifact: docs/design/driver-taxonomy.md; ADR-0001.
- [02 — Confidence and calibration](issues/02-confidence-and-calibration.md) — one self-reported 0–100 confidence per driver and per attribution, sources and check results attached, fixed truth-condition meaning; no rubric; calibration measured only against objective gold (hand-recorded walks + identity checks); narrative claims quarantined behind citation grounding; headline stat is the confidently-wrong rate.
- [15 — Acquire the CBA corpus](issues/15-acquire-cba-corpus.md) — manifest + idempotent fetch script live; CBA FY26 suite and FY25 Profit Announcement fetched and checksum-pinned; page counts and the +16 printed-page offset verified against ticket 08.

## Not yet specified

- Corpus acquisition for NAB and Westpac (CBA graduated to ticket 15) — sharpens after eval design (05) fixes the case list.
- Generalisation of the CBA pipeline to NAB and Westpac — sharpens after the POC exists.
- Unseen-bank hardening (a dry run on ANZ, Macquarie, or a regional bank) — after generalisation.
- Model-combination selection per pipeline stage — after the harness exists.
- The full eval matrix run and the results write-up — after ticket 05 and the build.
- Iteration priorities — after the first eval results.
- Final report: README, design doc, transcript attachment, reviewer access.

## Out of scope

- Investment advice: recommendations, price targets, forecasts. The agent explains movement; it does not predict.
- Banks outside Australia; figures in currencies other than AUD.
- Real-time market data, consensus estimates, paid data feeds.
- Any UI beyond a CLI and library surface.
