---
title: meal-planner
url: https://skills.sh/mary4data/clawbee/meal-planner
---

# meal-planner

skills/mary4data/clawbee/meal-planner
meal-planner
Installation
$ npx skills add https://github.com/mary4data/clawbee --skill meal-planner
SKILL.md
Meal Planner

Weekly dinner planning for a family of 4 using fridge contents and a budget.

Setup
bash /data/workspace/clawbee/skills/meal-planner/scripts/init-db.sh

Commands
/meals plan [budget]

Default budget: €100.

Load fridge contents:

sqlite3 /data/workspace/pantry.db "SELECT item FROM fridge;" 2>/dev/null


Generate a 7-day plan — see references/meal-templates.md for default meals and output format.

Mark each ingredient as "have" (in fridge) or "buy" (missing).

Save plan:

bash /data/workspace/clawbee/skills/meal-planner/scripts/save-plan.sh '[week]' '[plan_json]' [budget]


Display the plan and shopping list. End with: "Run /shopping send to send to Telegram."

/meals show
sqlite3 /data/workspace/pantry.db "SELECT plan_json FROM meal_plans ORDER BY created_at DESC LIMIT 1;"


Display in readable format. If none: "No plan yet. Run /meals plan first."

/meals pref <key> <value>
sqlite3 /data/workspace/pantry.db "CREATE TABLE IF NOT EXISTS family_prefs (key TEXT PRIMARY KEY, value TEXT);"
sqlite3 /data/workspace/pantry.db "INSERT OR REPLACE INTO family_prefs (key, value) VALUES (?, ?);" '<key>' '<value>'


Examples: /meals pref people 4, /meals pref vegetarian yes, /meals pref budget 80

Notes
Default family size: 4 people
Berlin context: Aldi/Lidl for staples, Rewe for quality
See references/meal-templates.md for the weekly template and display format
Weekly Installs
34
Repository
mary4data/clawbee
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass