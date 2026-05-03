---
title: send
url: https://skills.sh/fibrous-finance/fibx-skills/send
---

# send

skills/fibrous-finance/fibx-skills/send
send
Installation
$ npx skills add https://github.com/fibrous-finance/fibx-skills --skill send
SKILL.md
Send Transaction

Transfer native tokens or ERC-20 tokens to a destination address. The CLI automatically simulates the transaction before execution — if simulation fails, no funds are sent.

Prerequisites
Active session required.
Sufficient balance for the transfer amount + gas fees.
Rules
BEFORE any send, you MUST run npx fibx@latest status and npx fibx@latest balance to verify connectivity and funds.
If the recipient address was NOT previously mentioned in the conversation, you MUST ask for explicit confirmation: "Sending [amount] [token] to [address]. Confirm?"
If the user specifies a chain, you MUST include --chain <name>. If not specified, default to base and state it.
Use the correct native token symbol for each chain. NEVER use ETH on non-Base chains.
AFTER a successful send, you MUST verify the transaction using tx-status with the same --chain flag.
Chain Reference
Chain	Flag	Native Token
Base	--chain base	ETH
Citrea	--chain citrea	cBTC
HyperEVM	--chain hyperevm	HYPE
Monad	--chain monad	MON
Commands
npx fibx@latest send <amount> <recipient> [token] [--chain <chain>] [--simulate] [--json]


If token is omitted, the chain's native token is used.

Parameters
Parameter	Type	Description	Required
amount	number	Amount to send (e.g. 0.1, 100)	Yes
recipient	string	Destination address (0x...)	Yes
token	string	Token symbol (e.g. USDC, ETH, MON)	No
chain	string	base, citrea, hyperevm, or monad	No
simulate	flag	Estimate gas without executing	No
json	flag	Output as JSON	No

Default token: chain native. Default chain: base.

Examples

User: "Send 10 USDC to 0x123...abc"

npx fibx@latest status
npx fibx@latest balance
# Confirm recipient with user
npx fibx@latest send 10 0x123...abc USDC
npx fibx@latest tx-status <hash>


User: "Send 0.05 MON to 0xdef...456 on Monad"

npx fibx@latest status
npx fibx@latest balance --chain monad
npx fibx@latest send 0.05 0xdef...456 MON --chain monad
npx fibx@latest tx-status <hash> --chain monad

Error Handling
Error	Action
Insufficient funds	Inform user of current balance via balance.
Simulation failed	Transaction would revert — check amount and gas.
Invalid address	Validate recipient is a valid 0x address.
Not authenticated	Run authenticate-wallet skill first.
Rate limit / 429	Use config skill to set a custom RPC.
Related Skills
Run balance BEFORE sending to verify sufficient funds.
Run portfolio to see your full holdings with USD values across all chains.
Run tx-status AFTER sending to confirm the transaction succeeded.
Use config to set a custom RPC if you encounter rate limit errors.
Weekly Installs
21
Repository
fibrous-finance…x-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn