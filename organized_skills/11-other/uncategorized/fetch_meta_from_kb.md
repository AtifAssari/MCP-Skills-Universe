---
rating: ⭐⭐
title: fetch-meta-from-kb
url: https://skills.sh/tiangong-ai/skills/fetch-meta-from-kb
---

# fetch-meta-from-kb

skills/tiangong-ai/skills/fetch-meta-from-kb
fetch-meta-from-kb
Installation
$ npx skills add https://github.com/tiangong-ai/skills --skill fetch-meta-from-kb
SKILL.md
Fetch Meta from KB
Workflow
Read DB env vars from .env or process env: KB_DB_HOST, KB_DB_PORT, KB_DB_NAME, KB_DB_USER, KB_DB_PASSWORD.
Query journals where created_at >= now_utc - DAYS, ordered by created_at DESC, selecting only doi, title, abstract, date.
Return/write JSON array records with exactly these fields: doi, title, abstract, date.
Script

Run:

cd fetch-meta-from-kb
python3 scripts/fetch_meta_from_kb.py --days 7 --output selected-abstract.json


Env example:

KB_DB_HOST=<HOST>
KB_DB_PORT=5432
KB_DB_NAME=<DATABASE>
KB_DB_USER=<USER>
KB_DB_PASSWORD=<PASSWORD>

Output Rules
Return UTF-8 JSON.
Keep each item as: doi, title, abstract, date.
Do not output DB credentials.
Weekly Installs
24
Repository
tiangong-ai/skills
GitHub Stars
6
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass