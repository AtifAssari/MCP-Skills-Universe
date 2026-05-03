---
title: searxng-api
url: https://skills.sh/iails01/skills/searxng-api
---

# searxng-api

skills/iails01/skills/searxng-api
searxng-api
Installation
$ npx skills add https://github.com/iails01/skills --skill searxng-api
SKILL.md
SearXNG API
What the API can do
Run meta-search queries and return aggregated results in JSON.
Filter by engines, categories, language, and time range.
Paginate results.
Return suggestions, answers, and infoboxes (when available).
How to use it
Build the endpoint from SEARXNG_BASE_URL; if it is unset, use http://localhost:8080.
Call /search (or /) with q=...&format=json.
Parse the JSON response (results, answers, suggestions, etc.).
Minimal request
GET: {BASE_URL}/search?q={QUERY}&format=json
POST: {BASE_URL}/search with form data q=...&format=json
References
references/searxng-search-api.md - parameters and response fields
Weekly Installs
11
Repository
iails01/skills
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn