---
title: orderflow-analysis
url: https://skills.sh/saanjaypatil78/trading-platform/orderflow-analysis
---

# orderflow-analysis

skills/saanjaypatil78/trading-platform/orderflow-analysis
orderflow-analysis
Installation
$ npx skills add https://github.com/saanjaypatil78/trading-platform --skill orderflow-analysis
SKILL.md
Orderflow Analysis Skill

Detects institutional trading patterns from Level 2 market data and trade executions.

Capabilities

This skill enables the agent to:

Analyze L2 orderbook depth for bid/ask walls
Detect absorption patterns (hidden liquidity)
Detect exhaustion at support/resistance
Identify imbalance sweeps
Generate trade signals with confidence levels
Prerequisites
Active L2 data connection (Alpaca Pro or Polygon)
Trading symbols configured in watchlist
Procedural Steps
1. Connect to L2 Data Stream
Use the trading-orderflow MCP server to establish WebSocket connection.
Call: connect_l2_stream(symbol: str, provider: "alpaca" | "polygon")

2. Monitor Orderbook State
Track bid/ask walls and imbalance ratios.
Call: get_orderbook_state(symbol: str) -> returns current book snapshot

3. Run Detection Algorithms

When sufficient data is collected:

Call: analyze_footprint(symbol: str, window_seconds: int) 
Returns: List[FootprintSignal] with pattern type, direction, confidence

4. Interpret Signals
Signal Type	Description	Suggested Action
ABSORPTION	Heavy volume absorbed without price movement	Fade the volume direction
EXHAUSTION	Declining volume at S/R	Prepare for reversal
IMBALANCE	3:1+ buy/sell ratio	Follow imbalance direction
SWEEP	Multiple levels cleared rapidly	Momentum follow
5. Forward to Confirmation Mesh

All signals must pass through confirmation mesh before execution:

Call: validate_signal(signal: FootprintSignal, quantity: float) -> ConfirmationResult

Safety Guardrails
Never execute trades based on LOW confidence signals
Require L2 liquidity verification before market orders
All executions must go through confirmation_mesh validation
Circuit breakers halt trading after consecutive failures
Example Workflow
# Agent detects high-confidence absorption
signal = await analyze_footprint("AAPL", window_seconds=60)

if signal.signal_type == "ABSORPTION" and signal.confidence == "HIGH":
    # Validate before execution
    result = await validate_signal(signal, quantity=100)
    
    if result.approved:
        # Proceed to execute-trade skill
        await execute_confirmed_trade(result)

Weekly Installs
25
Repository
saanjaypatil78/…platform
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn