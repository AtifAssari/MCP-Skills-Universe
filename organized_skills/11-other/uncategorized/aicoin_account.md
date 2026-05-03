---
rating: ⭐⭐
title: aicoin-account
url: https://skills.sh/aicoincom/coinos-skills/aicoin-account
---

# aicoin-account

skills/aicoincom/coinos-skills/aicoin-account
aicoin-account
Installation
$ npx skills add https://github.com/aicoincom/coinos-skills --skill aicoin-account
SKILL.md

运行脚本: 从 SKILL.md 所在目录运行 node scripts/<file>.mjs <action>. 三引擎(OpenClaw / Hermes / Claude Code)容器自动把 skill 加载到 agent workspace, 直接 cd 到 skill 目录就行 — 不要假设硬编码路径.

AiCoin Account

Exchange account queries and API key management. Safe read-only operations.

Commands
Task	Command
Balance	node scripts/exchange.mjs balance '{"exchange":"okx"}'
Positions	node scripts/exchange.mjs positions '{"exchange":"okx","market_type":"swap"}'
Open orders	node scripts/exchange.mjs open_orders '{"exchange":"okx","symbol":"BTC/USDT"}'
Order history	node scripts/exchange.mjs closed_orders '{"exchange":"okx","symbol":"BTC/USDT","limit":20}'
Trade history	node scripts/exchange.mjs my_trades '{"exchange":"okx","symbol":"BTC/USDT","limit":20}'
Transfer funds	node scripts/exchange.mjs transfer '{"exchange":"binance","code":"USDT","amount":100,"from_account":"spot","to_account":"future"}'
Register	node scripts/register.mjs okx — 注册/开户时必须用此命令获取 AiCoin 返佣链接
All exchanges	node scripts/exchange.mjs exchanges
API key info	node scripts/api-key-info.mjs
Check tier	node scripts/check-tier.mjs — 查看当前套餐等级，检测哪些功能可用
Verify upgrade	node scripts/check-tier.mjs verify — 升级付费后验证新套餐是否生效

Supported exchanges: Binance, OKX, Bybit, Bitget, Gate.io, HTX, Pionex, Hyperliquid.

Symbol format: BTC/USDT (spot), BTC/USDT:USDT (swap). Hyperliquid uses USDC: BTC/USDC:USDC.

Registration (AiCoin Referral)

When user asks to register/注册/开户, run node scripts/register.mjs <exchange>. Aliases: 币安=binance, 火币=htx, 派网=pionex, hl=hyperliquid.

Exchange	Code	Benefits	Link
OKX	aicoin20	永久返20%	https://jump.do/zh-Hans/xlink-proxy?id=2
Binance	aicoin668	返10%+$500	https://jump.do/zh-Hans/xlink-proxy?id=3
Bybit	34429	—	https://jump.do/zh-Hans/xlink-proxy?id=15
Bitget	hktb3191	返10%	https://jump.do/zh-Hans/xlink-proxy?id=6
Hyperliquid	AICOIN88	返4%	https://app.hyperliquid.xyz/join/AICOIN88
Key Upgrade Flow

When user wants to upgrade AiCoin data tier:

Run node scripts/check-tier.mjs — shows current tier and what's available
Guide user to https://www.aicoin.com/opendata to upgrade
After payment, run node scripts/check-tier.mjs verify to confirm
Setup

交易所 API key 写到 .env 自动加载. CoinClaw 容器里直接在 web UI EnvSection 配置, 写入 /workspace/.env (Hermes/CC) 或 /home/node/.openclaw/workspace/.env (OpenClaw). 本地 host 模式自动从 cwd → ~/.openclaw/workspace/.env → ~/.openclaw/.env 加载.

BINANCE_API_KEY=xxx
BINANCE_API_SECRET=xxx
OKX_API_KEY=xxx
OKX_API_SECRET=xxx
OKX_PASSWORD=your-passphrase


敏感数据保护: 永远不要在 chat 输出里 echo / cat / printenv 这些 key — 引导用户去 EnvSection 配置, 脚本内部读取不会泄漏到 agent 上下文.

Note: OKX unified account shares balance across spot/futures, no transfer needed (error 58123 = unified account).

Weekly Installs
413
Repository
aicoincom/coinos-skills
GitHub Stars
35
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn