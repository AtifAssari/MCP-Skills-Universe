---
rating: ⭐⭐
title: skill-amazon-spapi
url: https://skills.sh/zero2ai-hub/skill-amazon-spapi/skill-amazon-spapi
---

# skill-amazon-spapi

skills/zero2ai-hub/skill-amazon-spapi/skill-amazon-spapi
skill-amazon-spapi
Installation
$ npx skills add https://github.com/zero2ai-hub/skill-amazon-spapi --skill skill-amazon-spapi
SKILL.md
Amazon SP-API Skill

Fetch orders, check FBA inventory, and manage listings — plug-and-play for any OpenClaw agent.

Setup
1. Install dependency
npm install amazon-sp-api

2. Create credentials file
{
  "lwaClientId": "amzn1.application-oa2-client.YOUR_CLIENT_ID",
  "lwaClientSecret": "YOUR_CLIENT_SECRET",
  "refreshToken": "Atzr|YOUR_REFRESH_TOKEN",
  "region": "eu",
  "marketplace": "YOUR_MARKETPLACE_ID",
  "sellerId": "YOUR_SELLER_ID"
}


Save as amazon-sp-api.json. Set AMAZON_SPAPI_PATH env var to point to it (default: ./amazon-sp-api.json).

Regions: na | eu | fe Marketplace IDs: Full list

Scripts
auth.js — Test Connection
node scripts/auth.js

orders.js — Orders
node scripts/orders.js --list                          # last 7 days
node scripts/orders.js --list --days 30
node scripts/orders.js --list --status Unshipped
node scripts/orders.js --list --out orders.json
node scripts/orders.js --get ORDER-ID

inventory.js — FBA Inventory
node scripts/inventory.js
node scripts/inventory.js --sku "MY-SKU"
node scripts/inventory.js --out inventory.json

listings.js — Listings & Pricing
node scripts/listings.js --get "MY-SKU"
node scripts/listings.js --update "MY-SKU" --price 99.00
node scripts/listings.js --update "MY-SKU" --price 99.00 --currency USD

Notes
Tokens auto-refresh via LWA — no manual management
Keep credential files at chmod 600
Respect SP-API rate limits per endpoint
Related
skill-amazon-ads — Campaign & bid management
Weekly Installs
20
Repository
zero2ai-hub/ski…on-spapi
GitHub Stars
1
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass