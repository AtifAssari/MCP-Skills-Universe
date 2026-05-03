---
rating: ⭐⭐
title: okx-cex-smartmoney
url: https://skills.sh/okx/agent-skills/okx-cex-smartmoney
---

# okx-cex-smartmoney

skills/okx/agent-skills/okx-cex-smartmoney
okx-cex-smartmoney
Installation
$ npx skills add https://github.com/okx/agent-skills --skill okx-cex-smartmoney
SKILL.md
OKX CEX Smart Money CLI

Smart Money leaderboard, trader analytics, position tracking, and aggregated consensus signals.

Preflight

Before running any command, follow ../_shared/preflight.md. Use metadata.version from this file's frontmatter as the reference for Step 2.

Prerequisites
Install okx CLI:
npm install -g @okx_ai/okx-trade-cli

Configure credentials:
okx config add-profile AK=<your_api_key> SK=<your_secret_key> PP=<your_passphrase> name=live
# or interactive wizard:
okx config init

Verify: okx --profile live smartmoney traders --limit 5
Credential & Profile Check

Run okx config show before any authenticated command.

Error or no configuration → stop, guide user to run okx config init, wait for completion.
Credentials configured → proceed.

On 401 errors: stop immediately, tell the user their credentials may be invalid or expired, guide them to update ~/.okx/config.toml (do NOT ask them to paste credentials into chat), then verify with okx config show and retry.

Skill Routing
User intent	Route to skill
Market prices, tickers, candles	okx-cex-market
Spot / swap / futures / options orders	okx-cex-trade
Account balance, positions, transfers	okx-cex-portfolio
Grid / DCA trading bots	okx-cex-bot
Simple Earn, On-chain Earn, DCD	okx-cex-earn
Smart Money leaderboard, signals, trader analytics	This skill
Command Index (5 commands, all read-only)
Trader Data
Command	Type	Auth	Description
smartmoney traders	READ	Required	List/filter traders from leaderboard
smartmoney trader --authorId <id>	READ	Required	Trader full portrait (profile + positions + trades)
smartmoney overview [--ts <ms>|--dataVersion <ver>]	READ	Required	Multi-currency smart money overview (prefer --ts)
Signal Data
Command	Type	Auth	Description
smartmoney signal [--ts <ms>|--dataVersion <ver>]	READ	Required	Single-currency aggregated consensus signal (prefer --ts)
smartmoney signal-history --instId <id> [--ts <ms>|--dataVersion <ver>]	READ	Required	Signal history timeline for trend analysis (prefer --ts)

Note: Prefer --ts (e.g. --ts $(date +%s)000 for latest snapshot) for overview / signal / signal-history; --dataVersion is an alternative for replaying a prior snapshot. At least one of the two must be provided; if both are sent, --ts wins.

For full command syntax and parameters, read {baseDir}/references/trader-commands.md and {baseDir}/references/signal-commands.md.

Operation Flow
Step 0 — Credential & Profile Check

Before any command: see Credential & Profile Check. Always use --profile live silently.

Step 1 — Identify intent

Trader discovery / ranking:

"推荐交易员" / "top traders" / "牛人榜" → smartmoney traders with sorting/filtering. See {baseDir}/references/trader-commands.md.
"看看某个交易员" / "trader detail" → smartmoney trader --authorId <id>. See {baseDir}/references/trader-commands.md. Signal analysis:
"BTC 聪明钱信号" / "smart money signal for BTC" → smartmoney signal. See {baseDir}/references/signal-commands.md.
"聪明钱总览" / "smart money overview" → smartmoney overview. See {baseDir}/references/signal-commands.md.
"信号趋势" / "signal trend over time" → smartmoney signal-history. See {baseDir}/references/signal-commands.md.
Step 2 — Execute and present

All commands are READ-only — no confirmation needed. Always pass --json and render results as Markdown tables.

For multi-step workflows (recommend traders then drill down, signal analysis with context), read {baseDir}/references/workflows.md.

Global Notes
Security: Never ask users to paste API keys or secrets into chat.
Output: Always pass --json to list/query commands and render results as a Markdown table — never paste raw terminal output.
Network errors: If commands fail with a connection error, prompt user to check VPN: curl -I https://www.okx.com
Language: Always respond in the user's language.
Signal availability: Signal commands (overview, signal, signal-history) require either --ts (preferred — use $(date +%s)000 for latest) or --dataVersion (for historical snapshot replay). If both are sent, --ts wins.

For number/time formatting and response structure conventions, read {baseDir}/references/templates.md.

Weekly Installs
506
Repository
okx/agent-skills
GitHub Stars
103
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn