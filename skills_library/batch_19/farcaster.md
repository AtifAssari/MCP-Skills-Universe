---
title: farcaster
url: https://skills.sh/alsk1992/cloddsbot/farcaster
---

# farcaster

skills/alsk1992/cloddsbot/farcaster
farcaster
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill farcaster
SKILL.md
Farcaster

Interact with the Farcaster decentralized social protocol via Neynar API.

Setup

Get your API key from dev.neynar.com:

export NEYNAR_API_KEY=xxx

# Optional: For posting (requires signer)
export NEYNAR_SIGNER_UUID=xxx

Commands
Users
/fc user <username>           Look up user profile
/fc search-users <query>      Search for users

Feeds
/fc feed [--channel X]        Get feed (optionally from channel)
/fc trending                  Trending casts
/fc channel <id>              Get channel info
/fc channels <query>          Search channels

Search
/fc search <query>            Search casts

Write Operations (require signer)
/fc post <text>               Post a cast
/fc reply <hash> <text>       Reply to a cast
/fc like <hash>               Like a cast
/fc recast <hash>             Recast
/fc follow <username>         Follow user
/fc unfollow <username>       Unfollow user

Examples
/fc user vitalik.eth
/fc trending
/fc channel base
/fc search "ethereum"
/fc post "Hello Farcaster!"
/fc follow dwr.eth

Rate Limits
Free tier: 300 requests/minute
Standard: 1,000 requests/minute
Premium: Higher limits
Features
User profiles with verified addresses
Cast search and feeds
Channel discovery
Trending content
Full write operations (with signer)
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn