---
title: divergence
url: https://skills.sh/alsk1992/cloddsbot/divergence
---

# divergence

skills/alsk1992/cloddsbot/divergence
divergence
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill divergence
SKILL.md
Divergence Trading - Spot vs Poly Price Lag

Detects when Binance spot prices move but Polymarket 15-minute binary markets haven't caught up yet. Buys the lagging side and sells when it corrects.

Strategy tags match the CLAUDE.md encoding: BTC_DOWN_s12-14_w15 (0.12-0.14% move in 15s window).

Starts in dry-run mode by default (no real orders).

Quick Start
/div start                     # Dry-run on BTC,ETH,SOL,XRP
/div start BTC,ETH --size 30   # Specific assets + size
/div status                    # Stats, open positions
/div stop                      # Stop and show summary

Commands
Start / Stop
/div start [ASSETS] [--size N] [--dry-run]
/div stop

Monitor
/div status       Stats + open positions + round info
/div positions    Last 20 closed trades with strategy tags
/div markets      Active 15-min markets from Gamma API

Configure
/div config                           Show current config
/div config --tp 20 --sl 30          Set TP/SL %
/div config --size 50                 Set trade size
/div config --windows 5,10,30         Set detection windows

Detection Algorithm

For each spot tick, across all configured windows (5s, 10s, 15s, 30s, 60s, 90s, 120s):

Look up spot price N seconds ago via binary search
Calculate spotMovePct = (now - then) / then * 100
If move >= threshold AND poly is fresh (< 5s stale):
Generate signal with strategy tag: {ASSET}_{DIR}_s{bucket}_w{window}
e.g., BTC_DOWN_s12-14_w15 = 0.12-0.14% spot drop over 15s
Threshold Buckets
Bucket	Spot Move Range
s08-10	0.08% - 0.10%
s10-12	0.10% - 0.12%
s12-14	0.12% - 0.14%
s14-16	0.14% - 0.16%
s16-20	0.16% - 0.20%
s20+	0.20%+
Exit Logic
Force exit — < 30s before market expiry
Take profit — PnL >= 15% (configurable)
Stop loss — PnL <= -25% (configurable)
Trailing stop — Activated at +10%, exits if drops 8% from HWM
Time exit — < 2min before expiry
Weekly Installs
14
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