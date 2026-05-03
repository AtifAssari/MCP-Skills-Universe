---
title: nextjs-v16
url: https://skills.sh/bobmatnyc/claude-mpm-skills/nextjs-v16
---

# nextjs-v16

skills/bobmatnyc/claude-mpm-skills/nextjs-v16
nextjs-v16
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill nextjs-v16
SKILL.md
Next.js 16
Async params/cookies/headers; opt-in caching via "use cache"; Turbopack default.

Anti-patterns:

❌ Sync request APIs; ✅ await params, cookies(), and headers().
❌ Keep middleware.ts; ✅ use proxy.ts and export function proxy.
❌ revalidateTag("posts"); ✅ revalidateTag("posts", "max") or { expire: ... }.

References: references/migration-checklist.md, references/cache-components.md, references/turbopack.md

Weekly Installs
159
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass