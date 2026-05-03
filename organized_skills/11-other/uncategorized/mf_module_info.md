---
rating: ⭐⭐
title: mf-module-info
url: https://skills.sh/module-federation/core/mf-module-info
---

# mf-module-info

skills/module-federation/core/mf-module-info
mf-module-info
Installation
$ npx skills add https://github.com/module-federation/core --skill mf-module-info
SKILL.md

Step 1: Parse $ARGUMENTS:

First token → <module-name>
If a second token looks like a URL (starts with http) → <remoteEntry-url> (standalone mode); remaining tokens → [project-root]
Otherwise → [project-root] (consumer mode)

Step 2 — consumer mode (no URL provided): Call the mf-context Skill (passing [project-root]) to collect MFContext, then run:

node scripts/module-info.js --context '<MFContext-JSON>' --module '<module-name>'


Step 2 — standalone mode (URL provided): Run with an empty context and the explicit URL:

node scripts/module-info.js --context '{}' --module '<module-name>' --url '<remoteEntry-url>'


Step 3: Present the result from the script output:

Field	Description
publicPath	Base URL of the remote
remoteEntry	Full URL to remoteEntry.js
typesZip	URL to @mf-types.zip
typesApi	URL to @mf-types.api (shown only if present)
hasSsr	Whether SSR build artifacts were detected
exposes	Modules this remote exposes
remotes	Remotes this module depends on
shared	Shared dependencies declared by this module

If result.error is set, surface it directly and stop.

Step 4 (conditional): If the user explicitly asks to see the type declarations (e.g. "show me the types", "what types does it export"), fetch result.typesZip or result.typesApi and display the relevant type definitions.

Weekly Installs
54
Repository
module-federation/core
GitHub Stars
2.5K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail