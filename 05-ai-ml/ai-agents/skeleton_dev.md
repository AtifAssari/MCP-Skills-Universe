---
title: skeleton-dev
url: https://skills.sh/finnan444/skills/skeleton-dev
---

# skeleton-dev

skills/finnan444/skills/skeleton-dev
skeleton-dev
Installation
$ npx skills add https://github.com/finnan444/skills --skill skeleton-dev
SKILL.md
Skeleton Dev

Reference Skeleton UI v4 LLM-optimized docs before writing or reviewing Skeleton components.

Docs Sources

First fetch https://www.skeleton.dev/llms.txt — this is the comprehensive index of all available LLM docs.

Then detect the framework from the project (package.json, file extensions, imports) and fetch the matching full docs:

Framework	URL
Svelte	https://www.skeleton.dev/llms-svelte.txt
React	https://www.skeleton.dev/llms-react.txt

Use WebFetch to retrieve the correct reference before starting any task.

Usage
Fetch llms.txt index to check for any new/updated doc URLs
Confirm Skeleton version in package.json/lockfiles; if not v4, pause and alert the user before proceeding.
Detect framework from the project context. If unclear, ask the user; if still ambiguous, fetch both Svelte/React docs but only read the relevant sections.
Fetch the matching framework-specific docs (reuse a cached copy during the session unless llms.txt changed).
Read the relevant sections for the components needed
Write or review code following the documented patterns
Weekly Installs
12
Repository
finnan444/skills
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn