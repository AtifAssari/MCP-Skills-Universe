---
title: ens-primary-name
url: https://skills.sh/bankrbot/openclaw-skills/ens-primary-name
---

# ens-primary-name

skills/bankrbot/openclaw-skills/ens-primary-name
ens-primary-name
Installation
$ npx skills add https://github.com/bankrbot/openclaw-skills --skill ens-primary-name
SKILL.md
ENS Primary Name

Set your primary ENS name on Base and other L2 chains via the ENS Reverse Registrar.

A primary name creates a bi-directional link:

Forward: name.eth → 0x1234... (set in ENS resolver)
Reverse: 0x1234... → name.eth (set via this skill)
Requirements
Required: Bankr CLI

This skill requires the Bankr CLI for transaction signing:

bun install -g @bankr/cli
bankr login


The scripts use bankr agent to submit transactions like:

Submit this transaction: {"to": "0x...", "data": "0x...", "value": "0", "chainId": 8453}

Required: Node.js

Scripts use Node.js with viem for ENS namehash calculation and ABI encoding.

npm install -g viem

Quick Start
# Set primary name on Base
./scripts/set-primary.sh myname.eth

# Set on specific chain
./scripts/set-primary.sh myname.eth arbitrum

# Verify primary name is set
./scripts/verify-primary.sh 0x1234... base

# Set avatar (L1 only)
./scripts/set-avatar.sh myname.eth https://example.com/avatar.png

Supported Chains
Chain	Reverse Registrar
Base	0x0000000000D8e504002cC26E3Ec46D81971C1664
Arbitrum	0x0000000000D8e504002cC26E3Ec46D81971C1664
Optimism	0x0000000000D8e504002cC26E3Ec46D81971C1664
Ethereum	0x283F227c4Bd38ecE252C4Ae7ECE650B0e913f1f9
Prerequisites
Own or control an ENS name - The name must be registered
Forward resolution configured - The name must resolve to your address
Native tokens for gas - ETH on the target chain
How It Works
Checks forward resolution exists (name → address)
Warns if chain-specific address is not set
Encodes setName(string) calldata
Submits transaction to the Reverse Registrar
Verifies the primary name is correctly set
Verification

The skill automatically verifies after setting. You can also verify manually:

./scripts/verify-primary.sh 0xYourAddress base


Output:

✅ Reverse record: 0x1234... → myname.eth
✅ Forward resolution: myname.eth → 0x1234...
🎉 PRIMARY NAME VERIFIED: myname.eth

Setting Avatars
# Set avatar (requires L1 transaction + ETH for gas)
./scripts/set-avatar.sh myname.eth https://example.com/avatar.png


Supported avatar formats:

HTTPS: https://example.com/image.png
IPFS: ipfs://QmHash
NFT: eip155:1/erc721:0xbc4ca.../1234

Note: Avatars are text records stored on Ethereum mainnet. The script automatically looks up the resolver for your ENS name (works with both public and custom resolvers).

Troubleshooting
Issue	Solution
"Transaction reverted"	Ensure the ENS name resolves to your address
"Name not showing"	Forward resolution may not be set for that chain's cointype
"Not authorized"	You must call from the address the name resolves to
"Bankr CLI not found"	Install with bun install -g @bankr/cli && bankr login
"Chain-specific address not set"	Set the address for the target chain via app.ens.domains
"Could not find resolver"	Ensure the ENS name exists and has a resolver set
Links
ENS Docs: https://docs.ens.domains/web/reverse
ENS App: https://app.ens.domains
Primary Names UI: https://primary.ens.domains
Bankr CLI: https://www.npmjs.com/package/@bankr/cli
Weekly Installs
105
Repository
bankrbot/openclaw-skills
GitHub Stars
1.1K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn