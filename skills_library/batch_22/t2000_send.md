---
title: t2000-send
url: https://skills.sh/mission69b/t2000/t2000-send
---

# t2000-send

skills/mission69b/t2000/t2000-send
t2000-send
Installation
$ npx skills add https://github.com/mission69b/t2000 --skill t2000-send
SKILL.md
t2000: Send USDC
Purpose

Transfer USDC from the agent's available balance to any Sui address. Gas is self-funded from the agent's SUI reserve (auto-topped up if needed).

Command
t2000 send <amount> <asset> to <address_or_contact>
t2000 send <amount> <asset> <address_or_contact>

# Examples:
t2000 send 10 USDC to 0x8b3e...d412
t2000 send 50 USDC to Tom
t2000 send 50 USDC 0xabcd...1234


The to keyword is optional. The recipient can be a Sui address (0x...) or a saved contact name (e.g. "Tom"). Use t2000 contacts to list saved contacts.

Pre-flight checks (automatic)
Sufficient available USDC balance
SUI gas reserve present; if not, auto-topup triggers transparently
Output
✓ Sent $XX.XX USDC → 0x8b3e...d412
  Gas: X.XXXX SUI (self-funded)
  Balance: $XX.XX USDC
  Tx: https://suiscan.xyz/mainnet/tx/0x...

Error handling
INSUFFICIENT_BALANCE: available balance is less than the requested amount
INVALID_ADDRESS: destination is not a valid Sui address
CONTACT_NOT_FOUND: name is not a saved contact or valid address
SIMULATION_FAILED: transaction would fail on-chain; details in error message
Weekly Installs
23
Repository
mission69b/t2000
GitHub Stars
10
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn