---
title: convex
url: https://skills.sh/get-convex/agent-skills/convex
---

# convex

skills/get-convex/agent-skills/convex
convex
Installation
$ npx skills add https://github.com/get-convex/agent-skills --skill convex
SKILL.md
Convex

Use this as the routing skill for Convex work in this repo.

If a more specific Convex skill clearly matches the request, use that instead.

Start Here

If the project does not already have Convex AI guidance installed, or the existing guidance looks stale, strongly recommend installing it first.

Preferred:

npx convex ai-files install


This installs or refreshes the managed Convex AI files. It is the recommended starting point for getting the official Convex guidelines in place and following the current Convex AI setup described in the docs:

Convex AI docs

Simple fallback:

convex_rules.txt

Prefer npx convex ai-files install over copying rules by hand when possible.

Route to the Right Skill

After that, use the most specific Convex skill for the task:

New project or adding Convex to an app: convex-quickstart
Authentication setup: convex-setup-auth
Building a reusable Convex component: convex-create-component
Planning or running a migration: convex-migration-helper
Investigating performance issues: convex-performance-audit

If one of those clearly matches the user's goal, switch to it instead of staying in this skill.

When Not to Use
The user has already named a more specific Convex workflow
Another Convex skill obviously fits the request better
Weekly Installs
13.4K
Repository
get-convex/agent-skills
GitHub Stars
25
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass