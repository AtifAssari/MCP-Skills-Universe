---
title: t2000-withdraw
url: https://skills.sh/mission69b/t2000/t2000-withdraw
---

# t2000-withdraw

skills/mission69b/t2000/t2000-withdraw
t2000-withdraw
Installation
$ npx skills add https://github.com/mission69b/t2000 --skill t2000-withdraw
SKILL.md
t2000: Withdraw from Savings
Purpose

Withdraw from savings and receive USDC. If savings are held in a non-USDC stablecoin (due to rebalance), t2000 auto-swaps back to USDC before returning funds to the checking balance.

Command
t2000 withdraw <amount>
t2000 withdraw all

# Examples:
t2000 withdraw 25
t2000 withdraw all


You always receive USDC regardless of which stablecoin your savings are held in internally.

Fees
No protocol fee on withdrawals
Standard DEX fees apply if an auto-swap from non-USDC is needed
Output
✓ Withdrew $XX.XX USDC
  Tx: https://suiscan.xyz/mainnet/tx/0x...

Safety

If there's an active borrow, t2000 checks the health factor before withdrawing. If the withdrawal would drop HF below 1.5, it throws WITHDRAW_WOULD_LIQUIDATE with a safeWithdrawAmount.

Error handling
WITHDRAW_WOULD_LIQUIDATE: withdrawal would make health factor unsafe. Check safeWithdrawAmount in error data.
NO_COLLATERAL: no savings to withdraw
INSUFFICIENT_BALANCE: requested amount exceeds savings balance
Weekly Installs
20
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