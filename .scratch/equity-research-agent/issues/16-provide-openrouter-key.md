# 16 — Provide the OpenRouter API key

Type: task
Status: resolved

## Question

HITL: the user creates an OpenRouter API key (openrouter.ai → Keys), funds it under the AUD 50 run budget, and saves it as `OPENROUTER_API_KEY=...` in `/Users/michaelzhao/swe/ai-bank-equity-researcher/.env` (gitignored). Resolved when a test model call succeeds. Blocks both prototypes (13, 14) and all agent runs.

## Answer

Done 2026-08-25. Key saved in `.env` (gitignored), verified via `/api/v1/auth/key`: USD 100 limit, zero usage, expires 2026-11-23. Test completion through `anthropic/claude-haiku-4.5` succeeded. Model slate chosen with the user from the live catalogue: cheap `qwen/qwen3.7-flash` ($0.03/$0.13 per M, vision); normal author `z-ai/glm-5.3`; cross-family judge `deepseek/deepseek-v4-pro-0813`; free stealth `stealth/ox-alpha` featured in every prototype arm while it lasts; `moonshotai/kimi-k3` as vision quality ceiling.
