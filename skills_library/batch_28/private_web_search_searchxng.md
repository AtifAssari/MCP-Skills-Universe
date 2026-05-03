---
title: private-web-search-searchxng
url: https://skills.sh/site/skills.volces.com/private-web-search-searchxng
---

# private-web-search-searchxng

skills/skills.volces.com/private-web-search-searchxng
private-web-search-searchxng
$ npx skills add https://skills.volces.com/skills/clawhub/adelpro
SKILL.md
Private Web Search (SearXNG)

Privacy-respecting, self-hosted metasearch engine for AI agents.

Quick Setup
# 1. Start container
docker run -d --name searxng -p 8080:8080 -e BASE_URL=http://localhost:8080/ searxng/searxng

# 2. Enable JSON API
docker exec searxng sed -i 's/  formats:/  formats:\n    - json/' /etc/searxng/settings.yml
docker restart searxng

# 3. Verify
curl -sL "http://localhost:8080/search?q=test&format=json" | jq '.results[0]'

Usage
Basic Search
curl -sL "http://localhost:8080/search?q=YOUR_QUERY&format=json" | jq '.results[:10]'

Using the Helper Script
./scripts/search.sh "openclaw ai" 5

Environment Variables
Variable	Default	Description
SEARXNG_PORT	8080	Container port
SEARXNG_HOST	localhost	Server host
BASE_URL	http://localhost:8080	Public URL
Available Engines

Google, Bing, DuckDuckGo, Brave, Startpage, Wikipedia, and more.

Management
docker start searxng   # Start
docker stop searxng    # Stop
docker logs searxng    # View logs
docker rm searxng -f   # Remove

Troubleshooting
Issue	Solution
No results	Check docker logs searxng
403 Forbidden	Enable JSON format (step 2)
Connection refused	Run docker start searxng
Weekly Installs
15
Source
skills.volces.c…/adelpro
First Seen
Mar 25, 2026