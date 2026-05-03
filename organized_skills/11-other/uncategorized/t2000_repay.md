---
rating: ⭐⭐
title: t2000-repay
url: https://skills.sh/mission69b/t2000-skills/t2000-repay
---

# t2000-repay

skills/mission69b/t2000-skills/t2000-repay
t2000-repay
Installation
$ npx skills add https://github.com/mission69b/t2000-skills --skill t2000-repay
SKILL.md
t2000: Repay Borrow
Purpose

Repay outstanding debt in USDC. Supports specific amounts or repay all to clear the full balance including accrued interest.

Command
t2000 repay <amount>
t2000 repay all

# Examples:
t2000 repay 20
t2000 repay all

Fees
No protocol fee on repayment
Output
✓ Repaid $XX.XX USDC
  Remaining Debt: $XX.XX
  Tx: https://suiscan.xyz/mainnet/tx/0x...

Notes
repay all calculates full outstanding principal + accrued interest
Available USDC balance must cover the repayment amount
Weekly Installs
21
Repository
mission69b/t2000-skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn