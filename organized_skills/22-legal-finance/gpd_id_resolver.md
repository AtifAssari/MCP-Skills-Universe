---
rating: ⭐⭐
title: gpd-id-resolver
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/gpd-id-resolver
---

# gpd-id-resolver

skills/rudrankriyam/app-store-connect-cli-skills/gpd-id-resolver
gpd-id-resolver
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill gpd-id-resolver
SKILL.md
GPD ID Resolver

Use this skill to map names to IDs needed by other gpd commands.

Package name (app ID)
Package name is the primary identifier: com.example.app.
Always pass --package explicitly for deterministic results.
Track names
Common tracks: internal, alpha, beta, production.
List tracks:
gpd publish tracks --package com.example.app
Version codes and release status
Use release status to find version codes on a track:
gpd publish status --package com.example.app --track production
Tester groups
List testers by track:
gpd publish testers list --package com.example.app --track internal
Monetization IDs
Products:
gpd monetization products list --package com.example.app
gpd monetization products get sku123 --package com.example.app
One-time products:
gpd monetization onetimeproducts list --package com.example.app
Subscriptions:
gpd monetization subscriptions list --package com.example.app
gpd monetization subscriptions get sub123 --package com.example.app
Base plans and offers:
gpd monetization baseplans migrate-prices --package com.example.app sub123 plan456 --region-code US --price-micros 9990000
gpd monetization offers list --package com.example.app sub123 plan456
Permissions IDs
Developer users:
gpd permissions users list --developer-id DEV_ID
App grants:
gpd permissions grants create --package com.example.app --email user@example.com --app-permissions CAN_REPLY_TO_REVIEWS
Output tips
JSON is default; use --pretty for debugging.
Use --all on list commands to avoid missing items.
Weekly Installs
217
Repository
rudrankriyam/ap…i-skills
GitHub Stars
776
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass