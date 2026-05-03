---
rating: ⭐⭐
title: drift
url: https://skills.sh/alsk1992/cloddsbot/drift
---

# drift

skills/alsk1992/cloddsbot/drift
drift
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill drift
SKILL.md
Drift Protocol

Drift is a Solana DEX for perpetual futures and prediction markets.

Commands
Trading
/drift long <market> <size> [price]    Open long position
/drift short <market> <size> [price]   Open short position
/drift close <market>                  Close position
/drift cancel [orderId]                Cancel order(s)

Positions & Orders
/drift positions                       View open positions
/drift orders                          View open orders
/drift balance                         Check account balance

Market Info
/drift markets                         List available markets
/drift market <index>                  Get market details
/drift leverage <market> <amount>      Set leverage

Examples
/drift long SOL-PERP 0.5
/drift short BTC-PERP 0.01 95000
/drift positions
/drift balance
/drift leverage SOL-PERP 5

Market Types
perp: Perpetual futures (SOL-PERP, BTC-PERP, ETH-PERP)
spot: Spot markets
prediction: Prediction markets
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