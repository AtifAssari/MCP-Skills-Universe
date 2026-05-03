---
rating: ⭐⭐
title: oro-gold
url: https://skills.sh/behfar-dev/oro-agent-skill/oro-gold
---

# oro-gold

skills/behfar-dev/oro-agent-skill/oro-gold
oro-gold
Installation
$ npx skills add https://github.com/behfar-dev/oro-agent-skill --skill oro-gold
SKILL.md
ORO Gold Agent Skill

Quick reference for building agents that work with ORO GRAIL gold infrastructure.

Base URL
https://oro-tradebook-devnet.up.railway.app/api

Authentication
Request challenge → 2. Sign with wallet → 3. Get API key
// Step 1: Request challenge
POST /auth/challenge
{ "walletAddress": "...", "keyType": "PARTNER", "partnerId": "1" }

// Step 2: Sign message with Ed25519 (nacl.sign.detached)
// Step 3: Exchange for API key
POST /auth/api-key
{ "challengeId": "...", "signature": "...", "keyName": "..." }


API key goes in header: x-api-key: your-key

Core Endpoints
Endpoint	Method	Use
/trading/gold-price	GET	Get current gold price (Pyth oracle)
/trading/estimate/buy	POST	Calculate USDC cost for gold amount
/trading/estimate/sell	POST	Calculate USDC received for selling gold
/trading/purchases/user	POST	Buy gold for a user
/trading/purchases/partner	POST	Buy gold into partner treasury
/trading/sales/user	POST	Sell user's gold
/trading/sales/partner	POST	Sell partner's gold reserves
/users	POST	Create a user (KYC'd)
/users/{id}	GET	Get user details + balance
/distribution/partner/me	GET	Get partner details
Quick Scripts

See references/ for detailed patterns:

references/price-checker.md - Simple gold price fetch
references/balance-checker.md - Check user gold balance
references/buy-gold.md - Purchase gold flow
references/sell-gold.md - Sell gold flow
references/dca-agent.md - Dollar Cost Averaging agent
Key Concepts
Custodial: You hold user gold, they don't see blockchain
Self-Custody: Users hold GRAIL tokens in their own wallets
Partner: Your integration account (needs whitelist approval)
PDA: Program Derived Address - where gold is stored on-chain
Agent Use Cases
Price Agent - Fetch + alert on gold price movements
DCA Agent - Auto-buy gold on schedule
Balance Agent - Track agent/user gold holdings
Tip Jar - Agent-to-agent gold rewards (via treasury)
Weekly Installs
43
Repository
behfar-dev/oro-…nt-skill
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail