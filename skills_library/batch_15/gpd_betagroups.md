---
title: gpd-betagroups
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/gpd-betagroups
---

# gpd-betagroups

skills/rudrankriyam/app-store-connect-cli-skills/gpd-betagroups
gpd-betagroups
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill gpd-betagroups
SKILL.md
GPD Beta Groups

Use this skill when managing beta testers, groups, and build distribution on Google Play.

List and manage testers
gpd publish testers list --package com.example.app --track internal
gpd publish testers list --package com.example.app --track beta
gpd publish testers add --package com.example.app --track internal --group testers@example.com

Distribute builds to testing tracks
gpd publish release --package com.example.app --track internal --status completed
gpd publish release --package com.example.app --track beta --status completed

Promote between testing tracks
gpd publish promote --package com.example.app --from-track internal --to-track beta
gpd publish promote --package com.example.app --from-track beta --to-track production

Notes
Use --track internal for fast internal distribution.
Prefer IDs for deterministic operations; use the ID resolver skill when needed.
Weekly Installs
221
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