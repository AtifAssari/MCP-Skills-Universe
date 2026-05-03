---
rating: ⭐⭐
title: explain-changes
url: https://skills.sh/elie222/inbox-zero/explain-changes
---

# explain-changes

skills/elie222/inbox-zero/explain-changes
explain-changes
Installation
$ npx skills add https://github.com/elie222/inbox-zero --skill explain-changes
SKILL.md

Review the recent changes and provide:

Summary: What was built or changed? Explain in 2-3 sentences.

Files changed: List the files that were added or modified, grouped by area (e.g., API routes, components, database, utils).

Security check:

Any new API endpoints? Are they properly authenticated?
Any database writes? Is the input validated?
Any external API calls? Are secrets handled correctly?
Any user-facing inputs? Are they sanitized?

Risk areas: Which files or functions are most likely to cause problems? Why?

Edge cases: What scenarios might break this? What hasn't been tested?

Missing pieces: Based on what this feature is supposed to do, is anything obviously incomplete or not wired up?

Questions for me: Anything you're uncertain about or made assumptions on that I should verify?

Be concise. Flag problems, don't over-explain things that are fine.

Weekly Installs
20
Repository
elie222/inbox-zero
GitHub Stars
10.6K
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass