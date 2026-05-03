---
rating: ⭐⭐
title: skill-dropshipping-sourcing
url: https://skills.sh/zero2ai-hub/skill-dropshipping-sourcing/skill-dropshipping-sourcing
---

# skill-dropshipping-sourcing

skills/zero2ai-hub/skill-dropshipping-sourcing/skill-dropshipping-sourcing
skill-dropshipping-sourcing
Installation
$ npx skills add https://github.com/zero2ai-hub/skill-dropshipping-sourcing --skill skill-dropshipping-sourcing
SKILL.md
CJ Sourcing

Use this skill to reliably pull CJ product data (instead of manual browsing).

Files / creds (local convention)
Config: ./cj-api.json
apiKey, baseUrl, accessToken, tokenExpiry
1) Refresh access token
node scripts/token.js

2) Search products by keyword (listV2)
node scripts/source.js --keyword "sunset lamp" --size 20 --out cj-results.json


Output: cj-results.json with normalized fields.

Notes
Token refresh is conservative (refreshes ~10 minutes before expiry).
source.js uses GET /product/listV2 and requests enable_description + category fields.
Weekly Installs
66
Repository
zero2ai-hub/ski…sourcing
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn