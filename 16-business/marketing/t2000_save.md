---
title: t2000-save
url: https://skills.sh/mission69b/t2000/t2000-save
---

# t2000-save

skills/mission69b/t2000/t2000-save
t2000-save
Installation
$ npx skills add https://github.com/mission69b/t2000 --skill t2000-save
SKILL.md
t2000: Save (Deposit to Savings)
Purpose

Deposit into savings to earn yield (auto-selects best rate across NAVI and Suilend, or specify --protocol navi|suilend). If wallet holds non-USDC stablecoins (suiUSDT, suiUSDe, USDsui), they are auto-converted to USDC atomically before deposit. Funds remain non-custodial and withdrawable at any time.

Command
t2000 save <amount> [--protocol <name>]
t2000 save all

# Examples:
t2000 save 80
t2000 save all
t2000 save 50 --protocol suilend

save all: deposits full stablecoin balance minus $1 reserve for gas
Non-USDC stables are auto-swapped to USDC in the same transaction
Rebalance may internally move savings to other stablecoins for better yield
Fees
Protocol fee: 0.1% on deposit (collected atomically on-chain)
Output
✓ Gas manager: $1.00 USDC → SUI          [only shown if auto-topup triggered]
✓ Saved $XX.XX USDC to best rate
✓ Current APY: X.XX%
✓ Savings balance: $XX.XX USDC
  Tx: https://suiscan.xyz/mainnet/tx/0x...

Notes
APY is variable based on protocol utilization
If available balance is $0 after gas conversion, returns INSUFFICIENT_BALANCE
t2000 supply is an alias for t2000 save
Use t2000 rebalance to auto-optimize yield across protocols and stablecoins
Weekly Installs
21
Repository
mission69b/t2000
GitHub Stars
10
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn