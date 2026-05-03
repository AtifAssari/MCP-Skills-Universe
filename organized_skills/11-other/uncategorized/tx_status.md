---
rating: ⭐⭐
title: tx-status
url: https://skills.sh/fibrous-finance/fibx-skills/tx-status
---

# tx-status

skills/fibrous-finance/fibx-skills/tx-status
tx-status
Installation
$ npx skills add https://github.com/fibrous-finance/fibx-skills --skill tx-status
SKILL.md
Transaction Status

Fetch on-chain receipt data for a transaction hash: status, block number, gas used, and explorer link.

Prerequisites
A valid transaction hash (starts with 0x).
No authentication required — this is a public chain query.
Rules
You MUST use the same --chain flag that was used for the original transaction. A Base tx hash will not be found on Monad.
Use this skill AFTER every send or trade to verify success.
Commands
npx fibx@latest tx-status <hash> [--chain <chain>] [--json]

Parameters
Parameter	Type	Description	Required
hash	string	Transaction hash (0x...)	Yes
chain	string	base, citrea, hyperevm, or monad	No
json	flag	Output as JSON	No

Default chain: base.

Examples

User: "Did my transaction go through?"

npx fibx@latest tx-status 0x123...abc


User: "Check tx 0xabc...def on Monad"

npx fibx@latest tx-status 0xabc...def --chain monad

JSON Output Structure
{
	"status": "success",
	"blockNumber": "12345",
	"gasUsed": "21000",
	"from": "0x...",
	"to": "0x...",
	"explorerLink": "https://basescan.org/tx/0x...",
	"chain": "base"
}

Error Handling
Error	Action
Transaction not found	Verify you are querying the correct chain.
Pending	Transaction is still in the mempool — wait and retry.
Rate limit / 429	Use config skill to set a custom RPC.
Related Skills
This skill is used AFTER send or trade to verify transaction success.
Use config to set a custom RPC if you encounter rate limit errors.
Weekly Installs
14
Repository
fibrous-finance…x-skills
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn