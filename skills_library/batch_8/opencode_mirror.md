---
title: opencode-mirror
url: https://skills.sh/different-ai/openwork/opencode-mirror
---

# opencode-mirror

skills/different-ai/openwork/opencode-mirror
opencode-mirror
Installation
$ npx skills add https://github.com/different-ai/openwork --skill opencode-mirror
SKILL.md
Quick Usage (Already Configured)
Update mirror
git -C vendor/opencode pull --ff-only

Common Gotchas
Keep the mirror gitignored; never commit vendor/opencode.
Use --ff-only to avoid merge commits in the mirror.
First-Time Setup (If Not Configured)
Clone mirror
git clone https://github.com/anomalyco/opencode vendor/opencode

Weekly Installs
412
Repository
different-ai/openwork
GitHub Stars
14.6K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn