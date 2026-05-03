---
rating: ⭐⭐
title: firecrawl-web
url: https://skills.sh/bextuychiev/firecrawl-claude-code-skill/firecrawl-web
---

# firecrawl-web

skills/bextuychiev/firecrawl-claude-code-skill/firecrawl-web
firecrawl-web
Installation
$ npx skills add https://github.com/bextuychiev/firecrawl-claude-code-skill --skill firecrawl-web
SKILL.md
Firecrawl Web Skill

This skill provides web access through Firecrawl's API.

Script Location

All commands use the bundled script: ~/.claude/skills/firecrawl-web/fc.py

Getting Page Content

Fetch any webpage as clean markdown:

python3 ~/.claude/skills/firecrawl-web/fc.py markdown "https://example.com"


For cleaner output without navigation and footers:

python3 ~/.claude/skills/firecrawl-web/fc.py markdown "https://example.com" --main-only

Taking Screenshots

Capture a full-page screenshot:

python3 ~/.claude/skills/firecrawl-web/fc.py screenshot "https://example.com" -o page.png

Extracting Structured Data

Extract specific data using a JSON schema. Create a schema file first:

{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "price": {"type": "number"},
    "features": {"type": "array", "items": {"type": "string"}}
  }
}


Then extract:

python3 ~/.claude/skills/firecrawl-web/fc.py extract "https://example.com/product" --schema schema.json


Add a prompt for better accuracy:

python3 ~/.claude/skills/firecrawl-web/fc.py extract "https://example.com/product" --schema schema.json --prompt "Extract the main product details"

Searching the Web

Search for current information:

python3 ~/.claude/skills/firecrawl-web/fc.py search "Python 3.13 new features"


Limit results:

python3 ~/.claude/skills/firecrawl-web/fc.py search "latest React documentation" --limit 3

Crawling Documentation

Crawl a documentation site to learn about a new framework:

python3 ~/.claude/skills/firecrawl-web/fc.py crawl "https://docs.newframework.dev" --limit 30


Save pages to a directory:

python3 ~/.claude/skills/firecrawl-web/fc.py crawl "https://docs.example.com" --limit 50 --output ./docs


Each page costs one credit. Set a reasonable limit to avoid burning through your quota.

Weekly Installs
47
Repository
bextuychiev/fir…de-skill
GitHub Stars
11
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn