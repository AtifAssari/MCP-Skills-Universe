---
title: devvit-docs
url: https://skills.sh/reddit/devvit-skills/devvit-docs
---

# devvit-docs

skills/reddit/devvit-skills/devvit-docs
devvit-docs
Installation
$ npx skills add https://github.com/reddit/devvit-skills --skill devvit-docs
SKILL.md
Devvit Docs

Look up Devvit documentation from reddit/devvit-docs.

Constraints:

Use only reddit/devvit-docs as the source of truth.
Do not use other repos, forks, blog posts, or web search results.
If the answer isn't found, say so and cite the closest relevant file.
How It Works
Run the ensure-docs.js script to clone or refresh the local docs cache.
Read the JSON output to get the docs directory path.
Search that directory to answer the user's question.
Cite specific files/sections in your answer.
Usage
node ./scripts/ensure-docs.cjs [--force] [--ttl <hours>] [--project-dir <path>]


Script path is relative to this skill's directory.

--force — Pull regardless of cache age
--ttl <hours> — Cache TTL in hours (default: 24)
--project-dir <path> — User's project root for version detection (default: cwd)

Examples:

node ./scripts/ensure-docs.cjs
node ./scripts/ensure-docs.cjs --force

Output
{
  "docsRoot": "node_modules/.cache/devvit-docs/versioned_docs/version-0.11",
  "repoDir": "node_modules/.cache/devvit-docs",
  "appDevvitVersion": "0.11"
}

docsRoot — The directory to search. Versioned if a matching version was found, otherwise docs/.
repoDir — Root of the cloned repo (use as fallback if versioned docs are incomplete).
appDevvitVersion — Devvit version from the user's package.json, or null.
Present Results to User
Quote the specific doc file and section supporting each claim.
Provide a minimal code example if the docs include one.
If the docs don't cover it, say so and suggest the closest material found.
Troubleshooting
git not found — Requires git on PATH.
Network errors — Script uses existing cache if pull fails.
Stale docs — Use --force to bypass the TTL cache.
Weekly Installs
41
Repository
reddit/devvit-skills
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass