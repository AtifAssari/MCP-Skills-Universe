---
title: nansen-dca-tracker
url: https://skills.sh/nansen-ai/nansen-cli/nansen-dca-tracker
---

# nansen-dca-tracker

skills/nansen-ai/nansen-cli/nansen-dca-tracker
nansen-dca-tracker
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-dca-tracker
SKILL.md
DCA Watch

Answers: "What tokens are whales dollar-cost averaging into on Solana?"

nansen research smart-money dcas --limit 20
# → trader_address, trader_address_label, input/output_token_symbol, deposit_value_usd, dca_status, dca_created_at

# For each top DCA target, check token fundamentals
TARGET=<output_token_address>
nansen research token info --token $TARGET --chain solana
# → name, symbol, price, market_cap, token_details

nansen research token flow-intelligence --token $TARGET --chain solana
# → net_flow_usd per label: smart_trader, whale, exchange, fresh_wallets


To see DCA strategies targeting a specific token: nansen research token jup-dca --token $TARGET

DCAs show long-term conviction — SM DCA targets with positive smart_trader_net_flow = high-confidence accumulation.

Weekly Installs
261
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass