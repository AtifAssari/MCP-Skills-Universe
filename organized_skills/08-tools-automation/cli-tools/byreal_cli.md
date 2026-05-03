---
rating: ⭐⭐⭐
title: byreal-cli
url: https://skills.sh/byreal-git/byreal-cli/byreal-cli
---

# byreal-cli

skills/byreal-git/byreal-cli/byreal-cli
byreal-cli
Installation
$ npx skills add https://github.com/byreal-git/byreal-cli --skill byreal-cli
SKILL.md
Byreal LP Management
Get Full Documentation

Always run these commands first to get complete, up-to-date documentation:

# Complete documentation (commands, parameters, workflows, constraints)
byreal-cli skill

# Structured capability discovery (all capabilities with params)
byreal-cli catalog list

# Detailed parameter info for a specific capability
byreal-cli catalog show <capability-id>

Installation
# Check if already installed
which byreal-cli && byreal-cli --version

# Install
npm install -g @byreal-io/byreal-cli

Check for Updates
byreal-cli update check


If an update is available:

byreal-cli update install

Credentials & Permissions
Read-only commands (pool, token, tvl, stats): No wallet required
Write commands (swap, position open/close/claim): Require wallet setup via byreal-cli wallet set or byreal-cli setup
Private keys are stored locally at ~/.config/byreal/keys/ with strict file permissions (mode 0600)
The CLI never transmits private keys over the network — keys are only used locally for transaction signing
AI agents should never ask users to paste private keys in chat; always direct them to run byreal-cli setup interactively
Hard Constraints
-o json only for parsing — when showing results to the user, omit it and let the CLI's built-in tables/charts render directly. Never fetch JSON then re-draw charts yourself.
Never truncate on-chain data — always display the FULL string for: transaction signatures (txid), mint addresses, pool addresses, NFT addresses, wallet addresses. Never use xxx...yyy abbreviation.
Never display private keys - use keypair paths only
Preview first with --dry-run, then --confirm
Large amounts (>$1000) require explicit confirmation
High slippage (>200 bps) must warn user
Check wallet before write ops — run wallet address before any wallet-required command
Weekly Installs
56
Repository
byreal-git/byreal-cli
GitHub Stars
135
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn