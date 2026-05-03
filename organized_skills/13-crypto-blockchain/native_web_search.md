---
rating: ⭐⭐
title: native-web-search
url: https://skills.sh/mitsuhiko/agent-stuff/native-web-search
---

# native-web-search

skills/mitsuhiko/agent-stuff/native-web-search
native-web-search
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill native-web-search
SKILL.md
Native Web Search

Use this skill to run a fast model with native web search enabled and get a concise research summary with explicit full URLs.

Script
search.mjs
Usage

Run from this skill directory:

node search.mjs "<what to search>" --purpose "<why you need this>"


Examples:

node search.mjs "latest python release" --purpose "update dependency notes"
node search.mjs "vite 7 breaking changes" --purpose "prepare migration checklist"


Optional flags:

--provider openai-codex|anthropic
--model <model-id>
--timeout <ms>
--json
Output expectations

The script instructs the model to:

search the internet for the requested topic
provide a concise summary for the given purpose
include full canonical URLs (https://...) for each key finding
highlight disagreements between sources
Notes
No extra npm install is required.
If module resolution fails, set PI_AI_MODULE_PATH to @mariozechner/pi-ai's dist/index.js path.
If OAuth helper resolution fails, set PI_AI_OAUTH_MODULE_PATH to @mariozechner/pi-ai's dist/oauth.js path.
For OAuth providers, the script can fall back to a still-valid cached access token from ~/.pi/agent/auth.json.
Weekly Installs
41
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn