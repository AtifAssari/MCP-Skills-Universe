---
rating: ⭐⭐
title: t2000-borrow
url: https://skills.sh/mission69b/t2000-skills/t2000-borrow
---

# t2000-borrow

skills/mission69b/t2000-skills/t2000-borrow
t2000-borrow
Installation
$ npx skills add https://github.com/mission69b/t2000-skills --skill t2000-borrow
SKILL.md
t2000: Borrow USDC
Purpose

Take a collateralized loan using savings deposits as collateral. Borrowed USDC goes to the available balance. A 0.05% protocol fee applies.

Command
t2000 borrow <amount>

# Examples:
t2000 borrow 40
t2000 borrow 100

Safety

Before borrowing, t2000 checks:

Savings collateral exists (NO_COLLATERAL if not)
Requested amount ≤ max safe borrow (HEALTH_FACTOR_TOO_LOW if exceeds)
Health factor stays above 1.5 after the borrow

If the amount exceeds the safe limit, the CLI shows:

⚠ Max safe borrow: $XX.XX (HF X.XX → min 1.5)

Fees
Protocol fee: 0.05% of the borrow amount
Output
✓ Borrowed $XX.XX USDC
  Health Factor: X.XX
  Tx: https://suiscan.xyz/mainnet/tx/0x...

Error handling
NO_COLLATERAL: no savings deposited to borrow against
HEALTH_FACTOR_TOO_LOW: borrow would drop HF below 1.5. Error data includes maxBorrow.
Weekly Installs
23
Repository
mission69b/t2000-skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn