---
rating: ⭐⭐
title: gpd-build-lifecycle
url: https://skills.sh/rudrankriyam/app-store-connect-cli-skills/gpd-build-lifecycle
---

# gpd-build-lifecycle

skills/rudrankriyam/app-store-connect-cli-skills/gpd-build-lifecycle
gpd-build-lifecycle
Installation
$ npx skills add https://github.com/rudrankriyam/app-store-connect-cli-skills --skill gpd-build-lifecycle
SKILL.md
GPD Build Lifecycle

Use this skill to manage build state, processing, and retention.

Upload and validate
gpd publish upload app.aab --package com.example.app

Inspect release status
gpd publish status --package com.example.app --track internal
gpd publish status --package com.example.app --track production

Recent tracks and releases
gpd publish tracks --package com.example.app

Internal app sharing

Use for fast distribution of a build without a full track release.

gpd publish internal-share upload app.aab --package com.example.app

Cleanup and rollback
gpd publish halt --package com.example.app --track production --confirm
gpd publish rollback --package com.example.app --track production --confirm

Notes
Prefer gpd publish release for end-to-end flow instead of manual steps.
Use a new version code for each uploaded build.
Weekly Installs
224
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