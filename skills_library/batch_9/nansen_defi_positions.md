---
title: nansen-defi-positions
url: https://skills.sh/nansen-ai/nansen-cli/nansen-defi-positions
---

# nansen-defi-positions

skills/nansen-ai/nansen-cli/nansen-defi-positions
nansen-defi-positions
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-defi-positions
SKILL.md
DeFi Exposure

Answers: "What DeFi positions does this wallet have across protocols?"

ADDR=<address>

nansen research portfolio defi --wallet $ADDR
# → protocol_name, chain, total_value_usd, total_assets_usd, total_debts_usd, total_rewards_usd, tokens

nansen research profiler balance --address $ADDR --chain ethereum
# → token_symbol, token_name, token_amount, value_usd per holding

nansen research profiler balance --address $ADDR --chain base


Combine DeFi positions (lending, LPs, staking) with spot balances for a complete picture of on-chain exposure.

Note: portfolio defi may return empty for wallets with no tracked DeFi positions.

Weekly Installs
271
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn