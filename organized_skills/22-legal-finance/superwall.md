---
rating: ⭐⭐⭐
title: superwall
url: https://skills.sh/superwall/skills/superwall
---

# superwall

skills/superwall/skills/superwall
superwall
Installation
$ npx skills add https://github.com/superwall/skills --skill superwall
SKILL.md
Superwall

This skill covers three areas. Read the relevant reference doc before proceeding.

API — REST API wrapper & auth

Use when: making API calls, managing projects/paywalls/campaigns, bootstrapping org structure, or setting up API keys.

→ references/api.md

Quick start:

scripts/sw-api.sh bootstrap

Data & Analytics — ClickHouse data warehouse

Use when: querying event data, analyzing revenue/subscriptions, running SQL against Superwall's ClickHouse tables, or investigating user behavior.

→ references/data-analytics.md

Query endpoint:

scripts/sw-api.sh -m POST -d 'SELECT ... FORMAT CSVWithNames' /v2/organizations/:organizationId/query

Docs — Documentation, SDK integration, dashboard links

Use when: looking up Superwall docs, integrating an SDK, linking to dashboard pages, cloning SDK source for debugging, or configuring webhooks.

→ references/docs.md

Doc lookup:

curl -sL https://superwall.com/docs/llms.txt        # Find the right page
curl -sL https://superwall.com/docs/{path}.md        # Fetch a specific page

Weekly Installs
823
Repository
superwall/skills
GitHub Stars
17
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn