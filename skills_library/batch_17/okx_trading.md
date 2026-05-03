---
title: okx-trading
url: https://skills.sh/jasonviipers/okx-trading-skill/okx-trading
---

# okx-trading

skills/jasonviipers/okx-trading-skill/okx-trading
okx-trading
Installation
$ npx skills add https://github.com/jasonviipers/okx-trading-skill --skill okx-trading
SKILL.md
OKX Provider Broker Skill

Use this workflow when editing src/providers/okx/*.

1. Load only needed references
For SDK usage patterns and method names, read references/okx-sdk-usage.md.
For error-to-action mapping, read references/okx-error-map.md.
For full source context, consult .trae/okx-api-llm.txt only for missing details.
2. Keep architecture compatibility
Preserve compatibility with src/providers/types.ts (BrokerProvider, MarketDataProvider, OptionsProvider).
Put OKX-specific expanded APIs behind OKX provider interfaces (for example OkxTradingProvider) while keeping generic provider methods working.
Ensure src/providers/broker-factory.ts can return OKX providers without adapter breakage.
3. Enforce auth and signing rules
Require all three credentials: API key, secret, passphrase.
Use OKX signing prehash: timestamp + UPPERCASE_METHOD + requestPathWithQuery + rawBody.
Use HMAC SHA256 base64 signing for both REST and private websocket auth via customSignMessageFn.
Pass demoTrading: true for simulated trading.
4. Trading and market coverage minimums
Trading: spot, margin, swap/futures, options order placement + cancel/query + list.
Account: balances, positions, bills/transactions, fills.
Market data: ticker(s), order book, trades, candles, instruments.
Websocket: ticker, orderbook, trades, candles, account/orders/positions subscriptions.
5. Error and rate-limit behavior
Parse and map OKX code + msg errors into internal error categories.
Handle known auth/order/risk/rate-limit codes explicitly.
Apply request throttling + retry with exponential backoff and jitter for retryable failures.
Avoid retrying invalid input/auth failures.
6. Documentation requirements for code changes
Update src/providers/okx/README.md with examples that match current method names.
Include one example each for: spot order, futures order, option order, account history, websocket subscription.
Keep examples SDK-realistic and aligned with references/okx-sdk-usage.md.
Weekly Installs
65
Repository
jasonviipers/ok…ng-skill
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn