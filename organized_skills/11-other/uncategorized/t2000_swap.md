---
rating: ⭐⭐
title: t2000-swap
url: https://skills.sh/mission69b/t2000/t2000-swap
---

# t2000-swap

skills/mission69b/t2000/t2000-swap
t2000-swap
Installation
$ npx skills add https://github.com/mission69b/t2000 --skill t2000-swap
SKILL.md
t2000: Swap Tokens
Purpose

Execute a token swap through Cetus DEX with on-chain slippage protection.

Command
t2000 swap <amount> <from> <to>
t2000 swap <amount> <from> <to> --slippage <percent>

# Examples:
t2000 swap 5 USDC SUI
t2000 swap 100 USDC SUI
t2000 swap 10 USDC SUI --slippage 0.5

Fees
Protocol fee: Free — no t2000 fee on swaps
DEX fee: Cetus standard (typically 0.01–0.05%)
Output
Preview:
  Swap: XX.XX USDC → XX.XXXX SUI
  Pool Price: 1 SUI = $X.XX

✓ Swapped XX.XX USDC → XX.XXXX SUI
  Tx: https://suiscan.xyz/mainnet/tx/0x...

Notes
Default slippage: 3%. Reduce with --slippage for large swaps on thin markets.
Supported: any Cetus-listed pair (USDC, SUI, USDT, and more)
Weekly Installs
10
Repository
mission69b/t2000
GitHub Stars
10
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn