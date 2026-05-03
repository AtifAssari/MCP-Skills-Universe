---
title: wallet
url: https://skills.sh/merit-systems/x402scan-skills/wallet
---

# wallet

skills/merit-systems/x402scan-skills/wallet
wallet
Installation
$ npx skills add https://github.com/merit-systems/x402scan-skills --skill wallet
SKILL.md
x402 Wallet Management

Your wallet is auto-created on first use and stored at ~/.x402scan-mcp/wallet.json.

Quick Reference
Task	Tool	Notes
Check balance	x402.get_wallet_info	Shows address + USDC balance
Redeem code	x402.redeem_invite(code="...")	One-time use per code
Deposit	Send USDC to wallet address	Base network only
Check Balance
x402.get_wallet_info


Returns:

Wallet address (Base network)
USDC balance
Deposit link

Always check balance before expensive operations.

Redeem Invite Code
x402.redeem_invite(code="YOUR_CODE")

One-time use per code
Credits added instantly
Run x402.get_wallet_info after to verify
Deposit USDC
Get your wallet address: x402.get_wallet_info
Use it to add funds in the deposit UI (point the user towards this URL: https://x402scan.com/mcp/deposit/)

Important: Only Base network USDC. Other networks or tokens will be lost.

Troubleshooting
Issue	Solution
"Insufficient balance"	Check balance, deposit or redeem code
"Payment failed"	Transient error, retry the request
"Invalid invite code"	Code already used or doesn't exist
Balance not updating	Wait for Base network confirmation (~2 sec)
Weekly Installs
25
Repository
merit-systems/x…n-skills
GitHub Stars
3
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail