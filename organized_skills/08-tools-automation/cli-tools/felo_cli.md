---
rating: ⭐⭐
title: felo-cli
url: https://skills.sh/doggy8088/felo-cli/felo-cli
---

# felo-cli

skills/doggy8088/felo-cli/felo-cli
felo-cli
Installation
$ npx skills add https://github.com/doggy8088/felo-cli --skill felo-cli
SKILL.md

Use this skill for Felo Open Platform chat workflows in this repository.

Prefer project tools in this order:

CLI: npx -y @willh/felo-cli --json "<query>" (always use --json when retrieving content so the full structured output is preserved).
SDK: createFeloClient() / feloChat() from src/felo-client.ts when programmatic integration is needed.
Direct API call only when validating protocol-level behavior.

For direct HTTP reference, use POST https://openapi.felo.ai/v2/chat with:

Environment variable: FELO_API_KEY
Authorization: Bearer <FELO_API_KEY>
Content-Type: application/json
Body { "query": "<string>" } where query is 1..2000 characters

Handle success/error payloads and rate-limit headers using references/api-contract.md and references/workflow.md.

Weekly Installs
75
Repository
doggy8088/felo-cli
GitHub Stars
7
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn