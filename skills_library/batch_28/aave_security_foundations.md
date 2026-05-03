---
title: aave-security-foundations
url: https://skills.sh/0xweaksheep/aave_farmore/aave-security-foundations
---

# aave-security-foundations

skills/0xweaksheep/aave_farmore/aave-security-foundations
aave-security-foundations
Installation
$ npx skills add https://github.com/0xweaksheep/aave_farmore --skill aave-security-foundations
SKILL.md
AAVE Security Foundations

Security-first checklist for AAVE script development and operations.

Threat Areas
Over-approval risk: unlimited ERC20 approvals can expose wallet funds.
Health factor drift: market volatility can liquidate leveraged positions quickly.
Interest rate mode mismatch: stable mode assumptions can fail per asset.
RPC/data inconsistency: stale or failing RPC can produce bad decisions.
Execution race conditions: quote-time assumptions may be invalid at execution.
Required Pre-Execution Checks
Validate chain/token/account/amount format.
Read reserve status (isActive, isFrozen, borrowingEnabled).
Read account health (healthFactor, availableBorrowsBase).
Enforce HF safety threshold before withdraw and aggressive borrow.
Reject execution if allowance/balance preconditions fail.
References
references/audit-checklist.md
references/common-failures.md
Weekly Installs
8
Repository
0xweaksheep/aave_farmore
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn