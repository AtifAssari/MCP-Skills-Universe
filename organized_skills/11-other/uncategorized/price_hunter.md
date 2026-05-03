---
rating: ⭐⭐
title: price-hunter
url: https://skills.sh/mary4data/clawbee/price-hunter
---

# price-hunter

skills/mary4data/clawbee/price-hunter
price-hunter
Installation
$ npx skills add https://github.com/mary4data/clawbee --skill price-hunter
SKILL.md
Price Hunter

Find and track the best grocery prices in Berlin.

Setup
bash /data/workspace/clawbee/skills/price-hunter/scripts/init-db.sh

Commands
/prices search <item>
Web search: "[item] price supermarket Berlin Germany Rewe Lidl Aldi 2025"
Extract prices for 2–3 stores. See references/berlin-prices.md for typical ranges.
Save results:
bash /data/workspace/clawbee/skills/price-hunter/scripts/save-price.sh '[item]' '[store]' [price] '[unit]'

Display sorted cheapest first:
Prices for pasta (500g):
• Aldi:  €0.89
• Lidl:  €0.99
• Rewe:  €1.29
Cheapest: Aldi

/prices best <item>
sqlite3 /data/workspace/pantry.db "SELECT store, price, unit FROM prices WHERE item=lower(?) ORDER BY price ASC LIMIT 1;" '[item]'


Reply: "Best price for [item]: €[price] [unit] at [store]"

/prices list
sqlite3 /data/workspace/pantry.db "SELECT item, store, MIN(price) as price, unit FROM prices GROUP BY item ORDER BY item;"


Display as a table grouped by item.

Notes
Aldi/Lidl are typically 20–30% cheaper than Rewe
Data is shared with shopping-agent for budget optimization
See references/berlin-prices.md for typical price ranges
Weekly Installs
28
Repository
mary4data/clawbee
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn