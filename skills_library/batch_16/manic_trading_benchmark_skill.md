---
title: manic-trading-benchmark-skill
url: https://skills.sh/manic-trade/manic-trading-benchmark-skill/manic-trading-benchmark-skill
---

# manic-trading-benchmark-skill

skills/manic-trade/manic-trading-benchmark-skill/manic-trading-benchmark-skill
manic-trading-benchmark-skill
Installation
$ npx skills add https://github.com/manic-trade/manic-trading-benchmark-skill --skill manic-trading-benchmark-skill
SKILL.md
Manic Trading Benchmark Skill

Run a complete trading agent benchmark on Manic Trade. Evaluates 5 dimensions: real-time data, multi-source intelligence, market analysis, trading execution, and risk management. Scored 0-100 with grades S/A/B/C/D.

When to Use

Use this skill when the user asks to:

Benchmark or evaluate their AI trading agent
Run a trading capability test or score
Test trading performance on Manic
Pre-check: Verify Setup

Before starting, check if ${SKILL_DIR}/.env exists and contains BENCHMARK_PAIR_CODE.

If .env is missing or does not contain BENCHMARK_PAIR_CODE, do NOT tell the user to run any commands. Directly ask:

Please provide your pair code (format: MANIC-XXXX-XXXX). If you don't have one yet, go to Manic Benchmark, log in with Twitter, fill in your Agent Name, and copy the pair code.

Once the user provides the pair code:

Create ${SKILL_DIR}/.env with this content:
# Manic Trading Benchmark Configuration
BENCHMARK_PAIR_CODE=<pair code from user>
BENCHMARK_SERVER_BASE=https://benchmark-api-alpha.manic.trade

Install Python dependencies if needed: pip3 install requests python-dotenv
Proceed to the Bind section below to establish a benchmark session.
After Bind succeeds, tell the user that setup is complete and a benchmark session is ready. Stop here and wait for the user to explicitly ask to start the benchmark. When the user confirms, go directly to Step 2 (Execute Benchmark Tasks) — skip Step 1 since the user just confirmed.

If BENCHMARK_PAIR_CODE exists and BENCHMARK_API_KEY is also set, probe the session status:

python3 ${SKILL_DIR}/scripts/benchmark_api.py next-task

If the call succeeds (returns a task) → session is active, go to Step 1 (Confirm Before Starting).
If the call fails with HTTP 401 or code: 1102 → the previous session has expired or the key is invalid. Inform the user that a new benchmark round is needed, then proceed to Bind below and go to Step 1.
If the call fails with any other error → report the error to the user and stop.

If BENCHMARK_PAIR_CODE exists but there is no BENCHMARK_API_KEY, this is a fresh setup or a completed session. Proceed to Bind below, then go to Step 1.

Bind

Determine your base_model: Introspect your own model to identify the exact model ID you are running on right now. Do NOT ask the user, do NOT guess, do NOT use a generic name. Use your precise model identifier (e.g. claude-opus-4-6, claude-sonnet-4-20250514, gpt-4o-2024-08-06).

Read the pair code from ${SKILL_DIR}/.env (BENCHMARK_PAIR_CODE value).

Call the bind API:

curl -s -X POST https://benchmark-api-alpha.manic.trade/api/benchmark/bind \
  -H "Content-Type: application/json" \
  -d "{\"pair_code\": \"PAIR_CODE_FROM_ENV\", \"base_model\": \"YOUR_MODEL_ID_HERE\"}"


STRICT RULES:

Replace PAIR_CODE_FROM_ENV with the pair code read from .env
Replace YOUR_MODEL_ID_HERE with your actual model ID (determined above)
The request body must contain ONLY pair_code and base_model
Do NOT add agent_name, description, or any other fields
Handle the response:

If the response contains code: 2003 (MAX_ATTEMPTS_REACHED) → inform the user:

You've used all your benchmark attempts on this pair code. Share your results on Twitter to unlock +1 extra attempt. Go to Manic Benchmark to share, then come back and try again.

Stop here and wait. The user does NOT need a new pair code — sharing on Twitter adds an attempt to the same pair code. When the user returns, re-run the Bind flow with the existing pair code.

If the response succeeds, extract api_key, sandbox_base_url, and binding_id from data.

Update ${SKILL_DIR}/.env — preserve BENCHMARK_PAIR_CODE and BENCHMARK_SERVER_BASE, add/overwrite the rest:
# Manic Trading Benchmark Configuration
BENCHMARK_PAIR_CODE=<keep existing value>
BENCHMARK_API_KEY=<api_key from response>
BENCHMARK_API_BASE=<sandbox_base_url from response>
BENCHMARK_SERVER_BASE=https://benchmark-api-alpha.manic.trade
BENCHMARK_SESSION_ID=<binding_id from response>

Step 1: Confirm Before Starting

Before executing tasks, inform the user:

Estimated duration: ~5 minutes (5 tasks)
Estimated token usage: ~50K-100K tokens depending on model and external data fetching
What will happen: 5 sequential trading tasks covering market data, intelligence, analysis, execution, and risk management

Ask the user to confirm they want to proceed. Do NOT start tasks without confirmation.

Step 2: Execute Benchmark Tasks

CRITICAL: Do NOT simply run benchmark_runner.py. That script is only a baseline reference. YOU must drive each task yourself using your own analysis and reasoning.

You must complete 5 tasks sequentially. For each task, follow this loop:

Task Loop
Get the next task by calling python3 ${SKILL_DIR}/scripts/benchmark_api.py next-task. This returns a JSON with task_index, title, scenario, constraints, and possibly extra data (e.g. cases for T3).
Read the scenario carefully. Understand exactly what is being asked.
Do the work yourself — combine sandbox data and external data sources, analyze deeply, make trading decisions, and execute trades. Your reasoning quality is what gets scored.
Submit your result by calling python3 ${SKILL_DIR}/scripts/benchmark_api.py submit-task with the required fields.
What Each Task Expects From You

T1 — Market Snapshot

Build a comprehensive market snapshot for the requested assets on your own.
Cite your data sources and include timestamps.
Handle ambiguous assets explicitly if they cannot be resolved confidently.

T2 — Multi-source Intelligence

Gather BTC-relevant intelligence from multiple external sources and cross-check with sandbox context.
Keep the response traceable: include source and time context for key facts.
Prefer source diversity (different provider types) and resilient evidence (not a single fragile endpoint).
Synthesize collected evidence into a directional view and risk-aware recommendation.

T3 — Market Analysis

Analyze only the provided case packet and perturbation.
Return valid machine-readable outputs for each case and both parts.
Reference evidence IDs from the provided observations.

T4 — Trading Decision & Execution

Form a concrete trade plan from prior context.
Verify market price, execute with sandbox APIs, and report execution artifacts.
Ensure the executed parameters match the plan.

T5 — Risk Management

Evaluate active positions with current prices and unrealized PnL context.
Make and execute explicit HOLD/CLOSE decisions.
Explain your risk threshold and what signal would invalidate your current view.
Submitting Each Task

After completing each task, submit:

python3 ${SKILL_DIR}/scripts/benchmark_api.py submit-task \
  --task-index <0-4> \
  --status success \
  --reasoning "<YOUR_DETAILED_REASONING>" \
  --api-calls '<JSON_ARRAY_OF_API_CALLS>' \
  --external-api-calls '<JSON_ARRAY_OF_EXTERNAL_CALLS>' \
  --duration-ms <TIME_SPENT_MS>


--reasoning should contain your own analysis and decisions. --api-calls and --external-api-calls should capture actual calls made during task execution.

api_calls Format

Record your sandbox API interactions in --api-calls. The scoring engine uses LLM to semantically understand what you did, so exact field names are flexible. Just make sure each entry clearly conveys what API was called and what happened:

[
  {"command": "get-prices", "httpStatus": 200, "request": {}, "response": {"data": [...]}},
  {"command": "open-position", "httpStatus": 200, "request": {"asset": "btc", "side": "call", "amount": 10000000}, "response": {"data": {"position_id": "sbx_xxx"}}}
]


Any field naming convention works (e.g. command, action, endpoint, URL path). The LLM evaluator will understand the intent.

external_api_calls Format

For T2 (and any task using external data), submitting external_api_calls helps but is not strictly required. The scoring engine evaluates your reasoning content directly — if your reasoning contains specific data points with named sources, you will get credit even without structured API call records.

If you do submit them, a simple format works:

[
  {"source": "CoinGecko", "url": "https://api.coingecko.com/...", "httpStatus": 200, "response": {"bitcoin": {"usd": 74500}}},
  {"source": "Alternative.me", "url": "https://api.alternative.me/fng/", "httpStatus": 200, "response": {"value": "25", "classification": "Extreme Fear"}}
]


What actually matters for T2 scoring (evaluated from your reasoning):

Source diversity — mention where your data came from (CoinGecko, Glassnode, etc.)
Dimension coverage — cover derivatives, on-chain, news, sentiment
Concrete data — include specific numbers, not vague descriptions
Traceability — attribute data to named sources
T3 Answer Format

For T3, your reasoning should contain your analysis for each case with both parts (MA-1 initial judgment, MA-2 updated judgment after perturbation). The scoring engine uses LLM to read your full response and evaluate each case.

Required content for each case:

MA-1 (initial judgment):

market_regime: "bullish" / "bearish" / "neutral"
confidence: 0-100
key_tension: description of the core market conflict
top_2_evidence_for: 2 observation IDs supporting the regime
top_1_counter_evidence: 1 observation ID arguing against

MA-2 (updated judgment):

updated_regime: "bullish" / "bearish" / "neutral"
updated_confidence: 0-100
changed: "yes" / "no"
reason_for_change: explanation
which_previous_evidence_is_invalidated: observation ID or "none"

You can structure this in any clear format — separate JSON blocks, nested objects, markdown tables, or even structured prose. The LLM evaluator will find and assess the content regardless of format. Just make sure each case's MA-1 and MA-2 are clearly identifiable.

Step 3: Poll Results

After submitting all 5 tasks, poll for scoring results:

python3 ${SKILL_DIR}/scripts/benchmark_api.py poll-result


This polls every 3 seconds for up to 120 seconds. Display the final grade and dimension scores to the user.

Available Sandbox Trading APIs

These APIs use the BENCHMARK_API_KEY from .env for authentication.

Get all asset prices:

python3 ${SKILL_DIR}/scripts/benchmark_api.py get-prices


Get single asset price:

python3 ${SKILL_DIR}/scripts/benchmark_api.py get-price --asset btc


Assets: btc, eth, sol, gold, silver, spy, xmr, pyth, layer, drift

Get account info (virtual balance, stats):

python3 ${SKILL_DIR}/scripts/benchmark_api.py get-account


Open a position:

python3 ${SKILL_DIR}/scripts/benchmark_api.py open-position \
  --asset btc --side call --amount 10000000 --duration 60

Parameter	Required	Description
--asset	Yes	btc, eth, sol, gold, silver, spy, xmr, pyth, layer, drift
--side	Yes	call (price goes up) or put (price goes down)
--amount	Yes	Stake in base units (1000000 = 1 USDC, 10000000 = 10 USDC)
--duration	No	Seconds: 30, 60, 120, 180, 240, 300 (default: 60)

Close a position early:

python3 ${SKILL_DIR}/scripts/benchmark_api.py close-position \
  --position-id <position_id> --asset btc


Get position history:

python3 ${SKILL_DIR}/scripts/benchmark_api.py position-history --page 1 --limit 10

Evaluation

The benchmark uses LLM-based semantic evaluation across all dimensions. The scoring engine reads your full reasoning and evaluates the quality of your analysis, not how you formatted your answers. Focus on:

Substance over format — detailed reasoning with concrete data beats perfectly formatted empty answers
Verifiable evidence — cite specific sources, numbers, and timestamps
Analytical depth — identify tensions, weigh conflicting signals, justify decisions
Execution consistency — ensure your actions match your stated analysis
Key Rules
Amount is in base units. USDC has 6 decimals: 1000000 = 1 USDC, 10000000 = 10 USDC.
Side meaning. call = bullish (up), put = bearish (down).
Durations. 30, 60, 120, 180, 240, 300 seconds.
Trading execution is sandboxed. Virtual 100 USDC balance, no real funds at risk; research data can come from sandbox and external sources.
Supported Assets
Asset	Type	Hours
BTC, ETH, SOL, XMR, PYTH, LAYER, DRIFT	Crypto	24/7
GOLD, SILVER	Commodities	Exchange hours
SPY	Equity	Exchange hours
References

See ${SKILL_DIR}/references/trading-api.md for the complete API documentation with request/response examples.

Weekly Installs
146
Repository
manic-trade/man…rk-skill
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail