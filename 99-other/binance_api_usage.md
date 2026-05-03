---
title: binance-api-usage
url: https://skills.sh/jkpark/agent-skills/binance-api-usage
---

# binance-api-usage

skills/jkpark/agent-skills/binance-api-usage
binance-api-usage
Installation
$ npx skills add https://github.com/jkpark/agent-skills --skill binance-api-usage
SKILL.md
Binance API Usage Skill

This skill provides a structured way to interact with the Binance exchange using the python-binance Python wrapper.

Core Workflows
1. Market Data Retrieval

Fetch current prices, order books, or historical K-line (candle) data.

Reference: See references/api_usage.md
Example Script: scripts/historical_data.py
2. Account & Portfolio Management

Check balances and manage account settings.

Example Script: scripts/basic_ops.py
3. Order Execution

Place Market, Limit, or OCO (One-Cancels-the-Other) orders.

Reference: See references/api_usage.md
Example Script: scripts/order_examples.py
4. Real-time Streaming (WebSockets)

Stream ticker updates, trade data, or account updates using asyncio.

Example Script: scripts/async_sockets.py
Best Practices

Security: Always use environment variables (BINANCE_API_KEY, BINANCE_API_SECRET or BINANCE_SECRET_KEY) instead of hardcoding keys.

.env file (required): Place your API keys in a .env file at the project root. If .env does not exist, create it from the provided template:

cp skills/binance-trader/assets/.env.example .env
# then edit .env and fill in your keys


Scripts shipped with this skill will automatically look for .env in the script directory, the test/ folder, and the project root.

Error Handling: Wrap API calls in try-except blocks to handle BinanceAPIException.

Rate Limits: Be mindful of Binance's rate limits (weight-based).

Testnet: Use testnet=True during development to avoid losing real funds.

Resources
Repository: sammchardy/python-binance
Official Docs: python-binance.readthedocs.io
Weekly Installs
38
Repository
jkpark/agent-skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn