---
title: yoink
url: https://skills.sh/alsk1992/cloddsbot/yoink
---

# yoink

skills/alsk1992/cloddsbot/yoink
yoink
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill yoink
SKILL.md
Yoink - Capture the Flag on Base

Play Yoink, an onchain capture-the-flag game on Base. Yoink the flag from the current holder to start your clock.

Contract

0x4bBFD120d9f352A0BEd7a014bd67913a2007a878 on Base (chain ID 8453)

Game Rules
Yoink the flag - Call yoink() to take the flag
Cooldown - 10 minutes (600 seconds) between yoinks
No self-yoink - You cannot yoink from yourself
Accumulate time - While holding the flag, your time score increases
Trophy - Player with most yoinks holds the trophy
Commands
Status
/yoink status                    Current flag holder and game stats
/yoink score <address>           Get player score
/yoink leaderboard               Top yoinkers

Play
/yoink                           Yoink the flag!
/yoink cooldown                  Check your cooldown status

Examples
/yoink status
/yoink score 0x1234...
/yoink

Setup
export PRIVATE_KEY="0x..."  # For yoinking

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