# 19 — CBA NIM POC: tool layer + orchestration comparison

Type: prototype
Status: open

## Question

Build the shared tool layer (corpus, hybrid retrieval, evidence extraction, vision walk reading, deterministic validation, schema enforcement, report rendering) and run the first end-to-end case: CBA, net interest margin, FY26 vs FY25. Then run the same case through both orchestration shells (Python pipeline with bounded evidence loop; single tool-calling agent) and compare correctness against the hand-verified gold walk, tokens, context size, and latency. Output: the attribution JSON, the rendered report, and the shell comparison — all for the user to react to. The user's reaction sets the orchestration default and closes the POC milestone.
