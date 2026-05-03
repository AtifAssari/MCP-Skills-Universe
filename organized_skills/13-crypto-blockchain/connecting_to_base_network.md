---
rating: ⭐⭐
title: connecting-to-base-network
url: https://skills.sh/base/skills/connecting-to-base-network
---

# connecting-to-base-network

skills/base/skills/connecting-to-base-network
connecting-to-base-network
Installation
$ npx skills add https://github.com/base/skills --skill connecting-to-base-network
SKILL.md
Connecting to Base Network
Mainnet
Property	Value
Network Name	Base
Chain ID	8453
RPC Endpoint	https://mainnet.base.org
Currency	ETH
Explorer	https://basescan.org
Testnet (Sepolia)
Property	Value
Network Name	Base Sepolia
Chain ID	84532
RPC Endpoint	https://sepolia.base.org
Currency	ETH
Explorer	https://sepolia.basescan.org
Security
Never use public RPC endpoints in production — they are rate-limited and offer no privacy guarantees; use a dedicated node provider or self-hosted node
Never embed RPC API keys in client-side code — proxy requests through a backend to protect provider credentials
Validate chain IDs before signing transactions to prevent cross-chain replay attacks
Use HTTPS RPC endpoints only — reject any http:// endpoints to prevent credential interception
Critical Notes
Public RPC endpoints are rate-limited - not for production
For production: use node providers or run your own node
Testnet ETH available from faucets in Base documentation
Wallet Setup
Add network with chain ID and RPC from tables above
For testnet, use Sepolia configuration
Bridge ETH from Ethereum or use faucets
Weekly Installs
210
Repository
base/skills
GitHub Stars
66
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass