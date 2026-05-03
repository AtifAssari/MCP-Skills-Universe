---
rating: ⭐⭐⭐
title: nansen-wallet-clustering
url: https://skills.sh/nansen-ai/nansen-cli/nansen-wallet-clustering
---

# nansen-wallet-clustering

skills/nansen-ai/nansen-cli/nansen-wallet-clustering
nansen-wallet-clustering
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-wallet-clustering
SKILL.md
Wallet Attribution

Answers: "Who controls this wallet? Are these wallets related?"

Chain: 0x → --chain ethereum (also base, arbitrum, optimism, polygon). Base58 → --chain solana.

ADDR=<address> CHAIN=<ethereum|solana|base|...>  # detect from address format above
# 1. Identity
nansen research profiler labels --address $ADDR --chain $CHAIN
# 2. Related wallets (paginate with --page N)
nansen research profiler related-wallets --address $ADDR --chain $CHAIN
# 3. Counterparties (paginate with --page N; widen with --days 365 if empty)
nansen research profiler counterparties --address $ADDR --chain $CHAIN --days 90
# 4. Batch profile cluster
nansen research profiler batch --addresses "addr1,addr2" --chain $CHAIN --include labels,balance,pnl
# 5. Compare pairs → shared_counterparties, shared_tokens, balances
nansen research profiler compare --addresses "addr1,addr2" --chain $CHAIN
# 6. Historical balances (fingerprint drained wallets)
nansen research profiler historical-balances --address $ADDR --chain $CHAIN --days 90
# 7. Multi-hop trace (credit-heavy — keep --width ≤3)
nansen research profiler trace --address $ADDR --chain $CHAIN --depth 2 --width 3


Expansion: Run steps 1-2 on seed. For each new address found, ask the human before querying. Reserve step 3 for seed only. Stop when: known protocol/CEX · Low confidence · already visited · cluster > 10 wallets. Confidence: High = first funder / shared Safe signers / same CEX deposit. Medium = coordinated movements / related-wallets + label match. Exclude = ENS only, single CEX withdrawal, single deployer. Full attribution rules in REFERENCE.md.

Weekly Installs
259
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn