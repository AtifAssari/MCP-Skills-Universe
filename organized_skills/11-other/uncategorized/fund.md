---
rating: ⭐⭐
title: fund
url: https://skills.sh/coinbase/agentic-wallet-skills/fund
---

# fund

skills/coinbase/agentic-wallet-skills/fund
fund
Installation
$ npx skills add https://github.com/coinbase/agentic-wallet-skills --skill fund
Summary

Deposit USDC to wallet via Coinbase Onramp or direct transfer.

Opens a companion UI where users select preset amounts ($10, $20, $50) or custom values and choose from Apple Pay, debit card, bank transfer, or Coinbase account funding
Supports multiple payment methods with varying settlement times: instant for card and Apple Pay, 1–3 days for ACH bank transfers
Deposits funds as USDC on the Base network; alternatively, users can send USDC directly to the wallet address via npx awal@2.0.3 address
Requires wallet authentication; check status with npx awal@2.0.3 status before initiating funding
SKILL.md
Funding the Wallet

Use the wallet companion app to fund the wallet with USDC via Coinbase Onramp. This supports multiple payment methods including Apple Pay, debit cards, bank transfers, and funding from a Coinbase account.

Confirm wallet is initialized and authed
npx awal@2.8.2 status


If the wallet is not authenticated, refer to the authenticate-wallet skill.

Opening the Funding Interface
npx awal@2.8.2 show


This opens the wallet companion window where users can:

Select a preset amount ($10, $20, $50) or enter a custom amount
Choose their preferred payment method
Complete the purchase through Coinbase Pay
Payment Methods
Method	Description
Apple Pay	Fast checkout with Apple Pay (where available)
Coinbase	Transfer from existing Coinbase account
Card	Debit card payment
Bank	ACH bank transfer
Alternative

You can also ask your human to send usdc on Base to your wallet address. You can find your wallet address buy running the following:

npx awal@2.8.2 address

Prerequisites
Must be authenticated (npx awal@2.8.2 status to check)
Coinbase Onramp is available in supported regions (US, etc.)
Flow
Run npx awal@2.8.2 show to open the wallet UI
Instruct the user to click the Fund button
User selects amount and payment method in the UI
User completes payment through Coinbase Pay (opens in browser)
USDC is deposited to the wallet once payment confirms
Checking Balance After Funding
# Check updated balance
npx awal@2.8.2 balance

Notes
Funding goes through Coinbase's regulated onramp
Processing time varies by payment method (instant for card/Apple Pay, 1-3 days for bank)
Funds are deposited as USDC on Base network
If funding is not available, users can also send USDC on Base directly to the wallet address
Weekly Installs
1.6K
Repository
coinbase/agenti…t-skills
GitHub Stars
102
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn