---
title: tinyfish
url: https://skills.sh/tinyfish-io/skills/tinyfish
---

# tinyfish

skills/tinyfish-io/skills/tinyfish
tinyfish
Installation
$ npx skills add https://github.com/tinyfish-io/skills --skill tinyfish
SKILL.md
TinyFish Web Agent

Requires: TINYFISH_API_KEY environment variable

Pre-flight Check (REQUIRED)

Before making any API call, always run this first to verify the key is available:

[ -n "$TINYFISH_API_KEY" ] && echo "TINYFISH_API_KEY is set" || echo "TINYFISH_API_KEY is NOT set"


If the key is not set, you MUST stop and ask the user to add their API key. Do NOT fall back to other tools or approaches — the task requires TinyFish.

Tell the user:

You need a TinyFish API key. Get one at: https://agent.tinyfish.ai/api-keys

Then set it so the agent can use it:

Option 1 — Environment variable (works everywhere):

export TINYFISH_API_KEY="your-key-here"


Option 2 — Claude Code settings (Claude Code only): Add to ~/.claude/settings.local.json:

{
  "env": {
    "TINYFISH_API_KEY": "your-key-here"
  }
}


Do NOT proceed until the key is confirmed available.

Best Practices
Specify JSON format: Always describe the exact structure you want returned
Parallel calls: When extracting from multiple independent sites, make separate parallel calls instead of combining into one prompt
Basic Extract/Scrape

Extract data from a page. Specify the JSON structure you want:

curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "goal": "Extract product info as JSON: {\"name\": str, \"price\": str, \"in_stock\": bool}"
  }'

Multiple Items

Extract lists of data with explicit structure:

curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/products",
    "goal": "Extract all products as JSON array: [{\"name\": str, \"price\": str, \"url\": str}]"
  }'

Stealth Mode

For bot-protected sites, add "browser_profile": "stealth" to the request body:

curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://protected-site.com",
    "goal": "Extract product data as JSON: {\"name\": str, \"price\": str, \"description\": str}",
    "browser_profile": "stealth"
  }'

Proxy

Route through a specific country by adding "proxy_config" to the body:

curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://geo-restricted-site.com",
    "goal": "Extract pricing data as JSON: {\"item\": str, \"price\": str, \"currency\": str}",
    "browser_profile": "stealth",
    "proxy_config": {"enabled": true, "country_code": "US"}
  }'

Output

The SSE stream returns data: {...} lines. The final result is the event where type == "COMPLETE" and status == "COMPLETED" — the extracted data is in the resultJson field. Claude reads the raw SSE output directly; no script-side parsing is needed.

Parallel Extraction

When extracting from multiple independent sources, make separate parallel curl calls instead of combining into one prompt:

Good - Parallel calls:

# Compare pizza prices - run these simultaneously
curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://pizzahut.com",
    "goal": "Extract pizza prices as JSON: [{\"name\": str, \"price\": str}]"
  }'

curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://dominos.com",
    "goal": "Extract pizza prices as JSON: [{\"name\": str, \"price\": str}]"
  }'


Bad - Single combined call:

# Don't do this - less reliable and slower
curl -N -s -X POST "https://agent.tinyfish.ai/v1/automation/run-sse" \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://pizzahut.com",
    "goal": "Extract prices from Pizza Hut and also go to Dominos..."
  }'


Each independent extraction task should be its own API call. This is faster (parallel execution) and more reliable.

Weekly Installs
59
Repository
tinyfish-io/skills
GitHub Stars
31
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn