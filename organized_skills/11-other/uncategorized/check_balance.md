---
rating: ⭐⭐
title: check-balance
url: https://skills.sh/casualsecurityinc/xno-skills/check-balance
---

# check-balance

skills/casualsecurityinc/xno-skills/check-balance
check-balance
Installation
$ npx skills add https://github.com/casualsecurityinc/xno-skills --skill check-balance
SKILL.md
Check XNO Balance (RPC)

When a user asks "did you receive it?" / "check the balance", you need an on-chain data source. This skill queries a Nano node RPC (user-provided) for balance and pending (both in raw).

Important nuance: pending vs received

Nano can show funds as pending until the receiving wallet publishes the receive/open block. Many wallet apps do this automatically; raw keys alone do not.

If you see pending funds, you must call wallet_receive to pocket them.

Well-known Public RPC Nodes

If the user doesn't have an RPC URL, suggest these public nodes:

https://rpc.nano.org (Nano Foundation)
https://app.natrium.io/api/rpc (Natrium)
https://nanonode.cc/api (NanoNode.cc)
https://node.somenano.site/api (SomeNano)
CLI usage (xno-skills)

Set an RPC URL (recommended):

export NANO_RPC_URL="https://rpc.nano.org"


Then:

npx -y xno-skills rpc account-balance <address> --json --xno


Or pass the URL explicitly:

npx -y xno-skills rpc account-balance <address> --url "https://rpc.nano.org" --json --xno


If the user has a mnemonic and isn't sure whether it's bip39 or legacy (common with 24-word phrases), prefer:

# Don't paste mnemonics into chat; run locally and use stdin
npx -y xno-skills wallet probe-mnemonic --stdin --url "https://rpc.nano.org" --json

MCP usage (xno-mcp)

If the agent has access to the xno-mcp tools:

First, set defaults (recommended):

config_set: { "rpcUrl": "https://rpc.nano.org" }


Then check balance:

rpc_account_balance with { "address": "...", "includeXno": true }
wallet_balance with { "name": "A", "index": 0 }
wallet_probe_balances with { "name": "A", "count": 5 } - Also shows which accounts are opened

If you see pending funds, receive them:

wallet_receive with { "name": "A", "index": 0 }
Fallback (no RPC available)

If the user can't provide an RPC URL (or the environment has no network access), ask them to check the address in a block explorer or in their wallet app and report back:

confirmed on-chain balance
pending/receivable amount (if shown)
Weekly Installs
17
Repository
casualsecurityi…o-skills
GitHub Stars
1
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn