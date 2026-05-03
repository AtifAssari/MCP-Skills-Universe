---
title: config
url: https://skills.sh/fibrous-finance/fibx-skills/config
---

# config

skills/fibrous-finance/fibx-skills/config
config
Installation
$ npx skills add https://github.com/fibrous-finance/fibx-skills --skill config
SKILL.md
Configuration Management

Manage local configuration for the fibx CLI. The primary use case is setting custom RPC URLs for supported chains to bypass public RPC rate limits or connection issues.

Prerequisites
None.
Rules
Rate Limits: If a tool fails with a "Rate limit exceeded" or "429" error, use this skill to check the current RPC and set a new one.
Persistence: Settings are stored locally in an OS-dependent config directory (e.g. ~/.config/fibx/config.json on Linux, ~/Library/Preferences/fibx-nodejs/config.json on macOS) and persist across sessions.
Validation: The CLI validates URL format but not connectivity. Ensure the RPC URL is valid before setting.
Commands
# Set a custom RPC
npx fibx@latest config set-rpc <chain> <url>

# Get current RPC
npx fibx@latest config get-rpc <chain>

# Reset a single chain to default
npx fibx@latest config reset-rpc <chain>

# Reset all chains to default
npx fibx@latest config reset-rpc

# List all configs
npx fibx@latest config list

Parameters
Parameter	Type	Description	Required
chain	string	base, citrea, hyperevm, or monad	Yes
url	string	The full HTTP(S) RPC endpoint URL	Yes
Examples

User: "I'm getting rate limit errors on Base." Agent: "I will set a custom RPC for Base."

npx fibx@latest config set-rpc base https://mainnet.base.org


User: "Check my current configuration."

npx fibx@latest config list


User: "Reset Base RPC to default."

npx fibx@latest config reset-rpc base


User: "Reset all custom RPCs."

npx fibx@latest config reset-rpc

Error Handling
Error	Action
Unsupported chain	Check spelling of chain name.
Invalid URL	Ensure URL starts with http:// or https://
Related Skills
All other skills may trigger rate limit errors that this skill resolves.
Use get-rpc to verify the current RPC before troubleshooting connectivity issues.
Weekly Installs
9
Repository
fibrous-finance…x-skills
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass