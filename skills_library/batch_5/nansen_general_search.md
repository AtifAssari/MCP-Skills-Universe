---
title: nansen-general-search
url: https://skills.sh/nansen-ai/nansen-cli/nansen-general-search
---

# nansen-general-search

skills/nansen-ai/nansen-cli/nansen-general-search
nansen-general-search
Installation
$ npx skills add https://github.com/nansen-ai/nansen-cli --skill nansen-general-search
SKILL.md
Search
nansen research search "jupiter" --type token
nansen research search "Vitalik" --type entity --limit 5
nansen research search "bonk" --chain solana --fields address,name,symbol,chain

Flag	Purpose
--type	token or entity
--chain	Filter by chain
--limit	Number of results (default 25, max 50)
--fields	Select specific output fields

Case-insensitive. Does NOT match by address — use profiler labels for address lookup.

Weekly Installs
274
Repository
nansen-ai/nansen-cli
GitHub Stars
121
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass