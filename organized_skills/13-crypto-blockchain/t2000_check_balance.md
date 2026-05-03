---
rating: ⭐⭐⭐
title: t2000-check-balance
url: https://skills.sh/mission69b/t2000-skills/t2000-check-balance
---

# t2000-check-balance

skills/mission69b/t2000-skills/t2000-check-balance
t2000-check-balance
Installation
$ npx skills add https://github.com/mission69b/t2000-skills --skill t2000-check-balance
SKILL.md
t2000: Check Balance
Purpose

Fetch the current balance across all accounts: available USDC, savings (NAVI), gas reserve (SUI), and total value.

Commands
t2000 balance                 # human-readable summary
t2000 balance --show-limits   # includes maxWithdraw, maxBorrow, healthFactor
t2000 balance --json          # machine-parseable JSON (works on all commands)

Output (default)
Available:  $150.00  (checking — spendable)
Savings:    $2,000.00  (earning 5.10% APY)
Gas:        0.50 SUI    (~$0.50)
──────────────────────────────────────
Total:      $2,150.50
Earning ~$0.27/day

Output (--show-limits)

Appends to the above:

Limits:
  Max withdraw:   $XX.XX
  Max borrow:     $XX.XX
  Health factor:  X.XX          (∞ if no active loan)

Notes
gasReserve.usdEquiv is an estimate at current SUI price; it fluctuates
If balance shows $0.00 available and wallet was just created, fund it first via Coinbase Onramp or a direct USDC transfer to the wallet address
--json is a global flag that works on all t2000 commands, not just balance
Weekly Installs
19
Repository
mission69b/t2000-skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass