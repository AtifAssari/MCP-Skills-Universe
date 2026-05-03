---
rating: ⭐⭐
title: restaurant-search
url: https://skills.sh/jackchuka/skills/restaurant-search
---

# restaurant-search

skills/jackchuka/skills/restaurant-search
restaurant-search
Installation
$ npx skills add https://github.com/jackchuka/skills --skill restaurant-search
SKILL.md
Restaurant Search

Find Japanese restaurants using the hpp CLI (HotPepper Gourmet API). https://github.com/jackchuka/hpp

Prerequisites
hpp CLI installed and HOTPEPPER_API_KEY env var set
Workflow
1. Parse the request

Extract from the user's request:

Location: Station name, area name, or coordinates
Party size: Number of people (maps to --party-capacity)
Day/time: Determines which restaurants are open (check open/close fields)
Genre preference: e.g., izakaya, Chinese, Italian (maps to --genre)
Budget: Price range (maps to --budget)
Features: Private rooms (--private-room), non-smoking (--non-smoking), WiFi (--wifi), free drink (--free-drink), etc.
Keywords: Free text like "ramen", "sushi" (maps to --keyword)
2. Resolve the area code

The API requires area codes, not free-text location names. Resolve the location:

hpp area small --keyword "<location-name>"


This returns small area codes (e.g., X085 for 浜松町) along with parent middle/large area codes.

If no small area matches, try middle area:

hpp area middle --keyword "<location-name>"


If the user provides coordinates (lat/lng), skip area lookup and use --lat, --lng, --range instead.

3. Resolve genre codes (if needed)

If the user requests a specific cuisine type:

hpp genre


Common genre codes:

Code	Genre
G001	居酒屋
G002	ダイニングバー・バル
G003	創作料理
G004	和食
G005	洋食
G006	イタリアン・フレンチ
G007	中華
G008	焼肉・ホルモン
G009	アジア・エスニック
G010	各国料理
G011	カラオケ・パーティ
G012	バー・カクテル
G013	ラーメン
G014	カフェ・スイーツ
G016	お好み焼き・もんじゃ
G017	韓国料理

If unsure, run hpp genre to get the full list.

4. Resolve budget codes (if needed)

If the user specifies a budget:

hpp budget


Common budget codes:

Code	Range
B001	~1500円
B002	2001~3000円
B003	3001~4000円
B008	4001~5000円
B004	5001~7000円
B005	7001~10000円
B006	10001~15000円
B012	15001~20000円
B013	20001~30000円
B014	30001円~
5. Search restaurants

Build the hpp search command with resolved codes and flags:

hpp search --small-area <code> --party-capacity <N> --count 10


Key flags to apply based on user needs:

Need	Flag
Party size	--party-capacity <N>
Genre	--genre <code>
Budget	--budget <code>
Private room	--private-room
Non-smoking	--non-smoking
WiFi	--wifi
All-you-can-drink	--free-drink
All-you-can-eat	--free-food
English menu	--english
Card payment	--card
Late night (after 11pm)	--midnight
Lunch	--lunch
Keyword	--keyword "<text>"
Coordinates	--lat <lat> --lng <lng> --range <1-5>

Range values for coordinate search: 1=300m, 2=500m, 3=1km, 4=2km, 5=3km.

Always use JSON output (default) for parsing, then present results as a table.

6. Present results

Display results as a markdown table with these columns:

Column	Source
#	Row number
Restaurant	name
Genre	genre.name
Budget	budget.average
Access	access (summarize to station + walk time)
Private Room	private_room (yes/no/semi)
Hours	open (show relevant day only)
Link	urls.pc (as clickable markdown link)

After the table, add brief recommendations highlighting the best options for the user's specific needs (e.g., closest to station, best for groups, has private rooms).

7. Refine (if requested)

If the user wants to narrow down, add more flags and re-search. Common refinements:

"with private rooms" → add --private-room
"under 4000 yen" → add --budget B001,B002,B003
"non-smoking" → add --non-smoking
"show me more" → increase --count or use --start for pagination
Other Useful Commands
hpp shop --name "<name>" — Look up a specific restaurant by name
hpp special list — Browse special features/tags
hpp creditcard — List accepted credit card types
Important Notes
Always use --count to limit results (default 10, max 100)
The API returns Japanese text — present it as-is, do not translate unless asked
Monday = 月, check open/close fields to verify the restaurant is open on the requested day
When the user specifies a day, check the close field for regular holidays (e.g., 日 = Sunday)
Coupon links are available in coupon_urls.sp — mention if the user asks about deals
Weekly Installs
58
Repository
jackchuka/skills
GitHub Stars
12
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass