---
rating: ⭐⭐
title: mf-bridge-check
url: https://skills.sh/module-federation/core/mf-bridge-check
---

# mf-bridge-check

skills/module-federation/core/mf-bridge-check
mf-bridge-check
Installation
$ npx skills add https://github.com/module-federation/core --skill mf-bridge-check
SKILL.md

Step 1: Call the mf-context Skill (pass $ARGUMENTS) to collect MFContext.

Step 2: Serialize MFContext to JSON and pass it to the check script via the --context argument:

node scripts/bridge-check.js --context '<MFContext-JSON>'


Process each item in the output results and context.mfConfig:

BRIDGE-USAGE · info — No export-app export found

No key matching the export-app pattern found in exposes
If this project is a sub-app that should follow the Bridge spec, guide the user to:
Add "./export-app": "./src/export-app.tsx" to exposes
The exported module must return an object conforming to the Bridge spec (containing render and destroy methods)

BRIDGE-USAGE · info — Consumer API recommendation

Advise consumers to use official Bridge APIs such as createRemoteAppComponent
Avoid directly concatenating remote URLs or manually calling loadRemote

If context.mfRole is host (no exposes), skip the producer-side check and only provide consumer-side recommendations.

Weekly Installs
56
Repository
module-federation/core
GitHub Stars
2.5K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass