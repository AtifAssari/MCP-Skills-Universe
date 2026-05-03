---
title: wallet
url: https://skills.sh/starchild-ai-agent/official-skills/wallet
---

# wallet

skills/starchild-ai-agent/official-skills/wallet
wallet
Installation
$ npx skills add https://github.com/starchild-ai-agent/official-skills --skill wallet
Summary

Multi-chain wallet operations for EVM and Solana with balance queries, transfers, signing, and transaction history.

Supports 13 tools across EVM (Ethereum, Base, Arbitrum, Optimism, Polygon, Linea) and Solana, including balance checks, fund transfers, message signing, and transaction history
Use wallet_get_all_balances() for complete portfolio visibility across all chains with USD values in a single call
Transfers are policy-gated by Privy TEE — only whitelisted addresses and amounts within daily limits are allowed, even if the agent is compromised
Includes EIP-712 typed data signing for permits and off-chain orders, plus transaction pre-signing without broadcasting for multi-step workflows
Authentication is automatic via Fly OIDC token; no API keys or manual wallet address entry needed
SKILL.md
💰 Wallet Skill

Multi-chain wallet for EVM (DeBank-supported chains) + Solana. Balances, transfers, signing, policy management.

Tools
Tool	Description
wallet_info	Get all wallet addresses
wallet_balance	EVM balance on a chain (DeBank)
wallet_sol_balance	Solana balance (Birdeye)
wallet_get_all_balances	All chains at once
wallet_transfer	Broadcast EVM tx (gas sponsored by default, user-paid fallback)
wallet_sign_transaction	Sign EVM tx (no broadcast)
wallet_sign	EIP-191 message signing
wallet_sign_typed_data	EIP-712 typed data signing
wallet_transactions	EVM tx history
wallet_sol_transfer	Broadcast Solana tx
wallet_sol_sign_transaction	Sign Solana tx (no broadcast)
wallet_sol_sign	Solana message signing
wallet_sol_transactions	Solana tx history
wallet_get_policy	Check policy status
wallet_propose_policy	Propose policy (sends to UI)
Key Facts
Gas is sponsored by default on EVM chains — user doesn't need native tokens for gas. Falls back to user-paid if sponsorship is unavailable. Use sponsor=false in wallet_transfer to explicitly pay gas from wallet balance.
Policy default: OFF (allow-all). Only when user enables policy do transactions need UI confirmation
Supported EVM chains: All DeBank-supported chains. Common names auto-mapped to DeBank chain IDs (e.g. avalanche → avax, bsc → bsc, zksync → era). For full chain list call db_chain_list() from the debank skill. The 16 common chains (ethereum, base, arbitrum, optimism, polygon, linea, bsc, avalanche, fantom, gnosis, zksync, scroll, blast, mantle, celo, aurora) have built-in fallback mapping.
Balance sources: DeBank (EVM), Birdeye (Solana), wallet-service (fallback)
Workflow
Check Balances
Single chain: wallet_balance(chain="base") or wallet_sol_balance()
All at once: wallet_get_all_balances()
Send Transaction (EVM)
Check balance: wallet_balance(chain=...)
Transfer: wallet_transfer(to=..., amount=..., chain_id=...)
Verify: wallet_transactions() or check balance again
Policy Management
Check: wallet_get_policy(chain_type="ethereum")
If user wants to enable: wallet_propose_policy(chain_type, rules, title, description)
User confirms in UI → policy applied
Standard Wildcard Policy (when needed)
rules = [
  {"name": "Deny key export", "method": "exportPrivateKey", "conditions": [], "action": "DENY"},
  {"name": "Allow all", "method": "*", "conditions": [], "action": "ALLOW"},
]

Policy Modes — CRITICAL DECISION TABLE

⚠️ DENY > ALLOW in Privy. DENY * overrides ALL ALLOW rules. NEVER mix them.

Mode	Rules	Effect
Allow-all (default)	DENY exportPrivateKey + ALLOW *	Everything allowed except key export
Deny-all (lockdown)	DENY exportPrivateKey + DENY *	Nothing works. No ALLOW rules!
Whitelist (selective)	DENY exportPrivateKey + specific ALLOW rules only	Only whitelisted ops work, rest implicitly denied
Mode 1: Allow-All (Standard Wildcard)
rules = [
  {"name": "Deny key export", "method": "exportPrivateKey", "conditions": [], "action": "DENY"},
  {"name": "Allow all", "method": "*", "conditions": [], "action": "ALLOW"},
]

Mode 2: Deny-All (Lockdown)
rules = [
  {"name": "Deny key export", "method": "exportPrivateKey", "conditions": [], "action": "DENY"},
  {"name": "Deny all actions", "method": "*", "conditions": [], "action": "DENY"},
]
# ⚠️ NO ALLOW rules here — DENY * would override them!

Mode 3: Whitelist (Selective Allow)
rules = [
  {"name": "Deny key export", "method": "exportPrivateKey", "conditions": [], "action": "DENY"},
  {"name": "Allow transfer to Uniswap", "method": "eth_sendTransaction", "conditions": [
    {"field_source": "ethereum_transaction", "field": "to", "operator": "eq", "value": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"}
  ], "action": "ALLOW"},
]
# ⚠️ NO "DENY *" here! enabled=true already denies everything not ALLOWed.
# Adding DENY * would override the ALLOW rules above (DENY > ALLOW).

Privy Policy Rules — Key Constraints
Rule	Details
Default behavior	enabled=true → deny-all unless explicitly ALLOWed
DENY > ALLOW	DENY always wins when both match
Empty conditions	Only exportPrivateKey and * (wildcard) allow conditions: []
TX methods need conditions	eth_sendTransaction, eth_signTransaction, eth_signTypedData_v4, eth_signUserOperation, signAndSendTransaction, etc. ALL require ≥1 condition
Valid field_sources	EVM: ethereum_transaction (to/value/chain_id), ethereum_calldata (function_name), ethereum_typed_data_domain (chainId/verifyingContract), ethereum_typed_data_message, system
Valid operators	eq, gt, gte, lt, lte, in (array, max 100 values)
Dual chain	Call wallet_propose_policy TWICE for EVM + Solana
Gotchas
wallet_propose_policy sends SSE event to frontend — needs streaming context
DeBank/Birdeye keys are auto-injected by sc-proxy
wallet_balance requires chain param — use wallet_get_all_balances for discovery
For both EVM + Solana policy, call wallet_propose_policy TWICE
Weekly Installs
5.5K
Repository
starchild-ai-ag…l-skills
GitHub Stars
11
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn