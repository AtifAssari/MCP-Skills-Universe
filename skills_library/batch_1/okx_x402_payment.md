---
title: okx-x402-payment
url: https://skills.sh/okx/onchainos-skills/okx-x402-payment
---

# okx-x402-payment

skills/okx/onchainos-skills/okx-x402-payment
okx-x402-payment
Installation
$ npx skills add https://github.com/okx/onchainos-skills --skill okx-x402-payment
SKILL.md
Onchain OS HTTP 402 Payment (Dispatcher)

Detects whether a 402 is MPP or x402 and loads the matching protocol playbook end-to-end.

Read ../okx-agentic-wallet/_shared/preflight.md before any onchainos command. EVM only — CAIP-2 eip155:<chainId> (run onchainos wallet chains for the list).

Skill Routing
Intent	Use skill
Token prices / charts / wallet PnL / tracker activities	okx-dex-market
Token search / metadata / holders / cluster analysis	okx-dex-token
Smart money / whale / KOL signals	okx-dex-signal
Meme / pump.fun token scanning	okx-dex-trenches
Token swaps / trades / buy / sell	okx-dex-swap
Authenticated wallet (balance / send / tx history)	okx-agentic-wallet
Public address holdings	okx-wallet-portfolio
Tx broadcasting (MPP feePayer=false hash mode)	okx-onchain-gateway
Security scanning (token / DApp / tx / signature)	okx-security

MPP mid-session ops (close / topup / settle / voucher / refund mentioned with an active channel_id, regardless of fresh 402) → stay here, load protocols/mpp.md, jump to the matching phase. Do NOT search for a separate close-channel / topup-channel / settle-channel tool — they're all onchainos payment mpp-session-* variants.

Step 1: Send the Original Request

Make the HTTP request the user asked for. If status is not 402, return the body directly — no payment, no wallet check, no other tool calls.

Step 2: Detect the Protocol
Priority 1: response.headers['WWW-Authenticate']
  starts with "Payment "        → MPP      → protocols/mpp.md
Priority 2: response.headers['PAYMENT-REQUIRED']
  base64-encoded JSON           → x402 v2  → protocols/x402.md
Priority 3: response body JSON has "x402Version"
                                → x402 v1  → protocols/x402.md
Otherwise                       → not a supported payment protocol, stop


Both headers present — STOP and ask:

The server offers both MPP and x402 payment protocols. Which would you like to use?

MPP (newer, supports sessions and streaming, recommended)
x402 (simpler, single-shot)
Step 3: Dispatch

Load the matching playbook and follow it from decode → confirm → wallet check → sign → assemble header → replay → suggest next steps:

MPP → protocols/mpp.md (charge + session, transaction + hash, splits, state tracking, seller error handling).
x402 → protocols/x402.md (v1 + v2, TEE signing, local-key fallback).
Weekly Installs
2.3K
Repository
okx/onchainos-skills
GitHub Stars
234
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail