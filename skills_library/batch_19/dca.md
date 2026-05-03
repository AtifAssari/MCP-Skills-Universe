---
title: dca
url: https://skills.sh/alsk1992/cloddsbot/dca
---

# dca

skills/alsk1992/cloddsbot/dca
dca
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill dca
SKILL.md
DCA (Dollar-Cost Averaging)

Spread orders over time across multiple platforms including Polymarket, Kalshi, PumpFun, Hyperliquid, Binance Futures, Bybit, MEXC, Drift, Opinion.trade, Predict.fun, Orca, Raydium, Virtuals, and Jupiter.

Commands
/dca poly <token-id> <total-$> --per <$> --every <interval>    Polymarket DCA
/dca kalshi <ticker> <total-$> --per <$> --every <interval>    Kalshi DCA
/dca pump <mint> <total-SOL> --per <SOL> --every <interval>    PumpFun DCA
/dca hl <coin> <total-$> --per <$> --every <interval>          Hyperliquid DCA
/dca bf <symbol> <total-$> --per <$> --every <interval>        Binance Futures DCA
/dca bb <symbol> <total-$> --per <$> --every <interval>        Bybit DCA
/dca list                                                       List active DCA orders
/dca info <id>                                                  Show order details
/dca pause <id>                                                 Pause DCA order
/dca resume <id>                                                Resume DCA order
/dca cancel <id>                                                Cancel DCA order
/dca help                                                       Show all commands

Weekly Installs
11
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn