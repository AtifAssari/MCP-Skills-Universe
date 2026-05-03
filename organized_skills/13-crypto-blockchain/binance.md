---
rating: ⭐⭐
title: binance
url: https://skills.sh/binance/binance-skills-hub/binance
---

# binance

skills/binance/binance-skills-hub/binance
binance
Installation
$ npx skills add https://github.com/binance/binance-skills-hub --skill binance
SKILL.md
Binance

Use binance-cli for Binance Spot, Futures (USD-S), and Convert. Requires auth.

PREREQUISITE: Read auth.md for auth, global flags, and security rules.

Helper Commands
Command	Description
algo	Algo Trading
alpha	Alpha
c2c	C2C
convert	Convert
copy-trading	Copy Trading
crypto-loan	Crypto Loan
derivatives-options	Derivatives Trading (Options)
derivatives-portfolio-margin	Derivatives Trading (Portfolio Margin)
derivatives-portfolio-margin-pro	Derivatives Trading (Portfolio Margin Pro)
dual-investment	Dual Investment
fiat	Fiat
futures-coin	Derivatives Trading (COIN-M Futures)
futures-usds	Derivatives Trading (USDS-M Futures)
gift-card	Gift Card
margin-trading	Margin Trading
mining	Mining
pay	Pay
rebate	Rebate
simple-earn	Simple Earn
spot	Spot Trading
staking	Staking
sub-account	Sub Account
vip-loan	VIP Loan
wallet	Wallet
Notes
⚠️ Prod transactions — always ask user to type CONFIRM before executing.
Append --profile <name> to any command to use a non-active profile.
All authenticated endpoints accept optional --recvWindow <ms> (max 60 000).
Timestamps (startTime, endTime) are Unix ms.
For endpoints not listed in the skill, use binance-cli request (GET|POST|PUT...) <url> [--signed]. Any Parameters can be added to the request (e.g: --param1 value --param2 value).
Weekly Installs
1.5K
Repository
binance/binance…ills-hub
GitHub Stars
801
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn