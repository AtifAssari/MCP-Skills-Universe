---
rating: ⭐⭐
title: balance
url: https://skills.sh/fibrous-finance/fibx-skills/balance
---

# balance

skills/fibrous-finance/fibx-skills/balance
balance
Installation
$ npx skills add https://github.com/fibrous-finance/fibx-skills --skill balance
SKILL.md
Check Balance

Fetch wallet holdings: native tokens and all ERC-20 tokens with non-zero balances.

Prerequisites
Active session required. If not authenticated, run authenticate-wallet skill first.
Rules
If the user specifies a chain, you MUST include --chain <name>.
If the user does NOT specify a chain, default to base and state it: "Checking your balance on Base."
Use --json when the output will be consumed by another skill or pipeline.
Chain Reference
Chain	Flag	Native Token
Base	--chain base	ETH
Citrea	--chain citrea	cBTC
HyperEVM	--chain hyperevm	HYPE
Monad	--chain monad	MON
Commands
npx fibx@latest balance [--chain <chain>] [--json]

Parameters
Parameter	Type	Description	Required
chain	string	base, citrea, hyperevm, or monad	No
json	flag	Output as JSON	No

Default chain: base

Examples

User: "Check my balance"

npx fibx@latest balance


User: "What's my Monad balance?"

npx fibx@latest balance --chain monad

Error Handling
Error	Action
Not authenticated	Run authenticate-wallet skill first.
Network error	Retry once. If persistent, use config to set custom RPC.
Rate limit / 429	Use config skill to set a custom RPC.
Related Skills
Run this BEFORE send or trade to verify sufficient funds.
Run this BEFORE aave supply to confirm available assets.
Use portfolio for a cross-chain overview with USD valuations.
Use config to set a custom RPC if you encounter rate limit errors.
Weekly Installs
25
Repository
fibrous-finance…x-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn