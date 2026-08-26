# 19 — CBA NIM POC: tool layer + orchestration comparison

Type: prototype
Status: resolved

## Question

Build the shared tool layer (corpus, hybrid retrieval, evidence extraction, vision walk reading, deterministic validation, schema enforcement, report rendering) and run the first end-to-end case: CBA, net interest margin, FY26 vs FY25. Then run the same case through both orchestration shells (Python pipeline with bounded evidence loop; single tool-calling agent) and compare correctness against the hand-verified gold walk, tokens, context size, and latency. Output: the attribution JSON, the rendered report, and the shell comparison — all for the user to react to. The user's reaction sets the orchestration default and closes the POC milestone.

## Answer

Resolved 2026-08-26, in three acts:

1. **Pipeline POC (CBA NIM FY26 vs FY25, all-cheap combo):** 7/7 driver contributions match the hand-verified gold walk; $0.0011, ~100s. The first run failed instructively (wrong-year walk presented at confidence 100) and produced the period-match rule, marker-scanned walk pages, author retry, and code-level confidence caps.
2. **Orchestration comparison, reshaped per the user (ADR-0004):** instead of a monolithic agent shell, the agentic pocket was tested where agents win — cold-start discovery. The discovery agent built ANZ's manifest from anz.com in 4 calls ($0.013); the pipeline then ran ANZ 1H26 NIM with no registry entry: 7/7 drivers matching ANZ's own disclosure, honest single-source caps. The hybrid is the architecture.
3. **Fable frontier benchmark (fresh agent, same four documents, no taxonomy given):** movement correct; 8 drivers reconciling BOTH walk framings arithmetically (PA T&M −2 = slide T&M ex-repos −1 + repos −1); caught the "earnings-neutral liquids growth / underlying NIM broadly stable" insight unprompted; per-driver confidence 85–95, overall 93. Cost: ~64k frontier tokens, 342s, 27 tool calls — versus the pipeline's $0.0011/100s. The benchmark sets the quality ceiling and the iteration agenda: framing reconciliation (tickets 20/24), the what-the-walk-hides insight (22), calibrated confidence spread.

Output artifacts: out/cba-nim-fy26-vs-fy25-cheap/, out/anz-nim-1h26-vs-1h25-cheap/, out/baseline-fable/cba-nim-fy26/.
