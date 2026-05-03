---
title: moonpay-x402
url: https://skills.sh/moonpay/skills/moonpay-x402
---

# moonpay-x402

skills/moonpay/skills/moonpay-x402
moonpay-x402
Installation
$ npx skills add https://github.com/moonpay/skills --skill moonpay-x402
SKILL.md
x402 paid API requests
Goal

Make HTTP requests to x402-protected endpoints. The CLI automatically detects 402 Payment Required responses, builds and signs a payment transaction with your local wallet, and retries the request with the payment proof.

Command
mp x402 request \
  --method POST \
  --url <x402-endpoint-url> \
  --body '<json-body>' \
  --wallet <wallet-name-or-address> \
  --chain solana

Available x402 endpoints
Endpoint	Cost	Input
https://agents.moonpay.com/x402/upgrade	$1-$20	{"duration": "day"} or {"duration": "month"}
Example flow
User: "Upgrade my rate limit for a day."
Run: mp upgrade --duration day --wallet my-wallet --chain solana
The CLI handles the 402 payment flow automatically and applies the upgrade.
Notes
Requires a local wallet with USDC on Solana or Base.
Payments accepted on Solana mainnet and Base.
If the request fails (status >= 400), the payment is not settled — you don't pay for errors.
Use moonpay-auth to set up a local wallet first.
Related skills
moonpay-auth — Create or import a local wallet.
moonpay-check-wallet — Check your wallet balance before making paid requests.
moonpay-upgrade — Upgrade your rate limit via x402.
Weekly Installs
29
Repository
moonpay/skills
GitHub Stars
101
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn