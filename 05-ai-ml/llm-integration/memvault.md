---
title: memvault
url: https://skills.sh/site/skills.volces.com/memvault
---

# memvault

skills/skills.volces.com/memvault
memvault
$ npx skills add https://skills.volces.com/skills/clawhub/wjy9902
SKILL.md
MemVault — Long-term Memory for AI Agents
Quick Start
# Install (one command — Docker handles everything)
bash scripts/install.sh

# Verify
memvault health

Usage
# Store a memory
memvault memorize-text <user_id> "<message>" "[reply]"

# Retrieve memories (strength-weighted)
memvault retrieve <user_id> "<query>"

# Run daily decay (memories fade like human memory)
memvault decay <user_id>

# Check stats
memvault stats <user_id>

API Endpoints
Method	Endpoint	Description
POST	/memorize	Store conversation → extract facts/events/knowledge
POST	/retrieve	Strength-weighted vector search (similarity × strength)
POST	/decay	Ebbinghaus forgetting curve (run daily via cron)
GET	/stats	Memory distribution, access patterns, agent breakdown
GET	/health	Service health
How It Works
Store: Conversations → LLM extracts facts → embedded → stored in pgvector
Retrieve: Query embedded → cosine similarity × memory strength → ranked results
Decay: strength = exp(-rate × days / (1 + damping × ln(1 + access_count)))
Access boost: Each retrieval increments access_count, slowing decay

Fading memories (strength < 0.1) are excluded from search.

Configuration

All via environment variables in .env (created by install script):

MEMVAULT_LLM_BASE_URL — Default: Ollama local. Set to OpenAI/Groq/etc URL if preferred
MEMVAULT_LLM_MODEL — Default: qwen2.5:3b
MEMVAULT_TRANSLATION — Set true + MEMVAULT_TRANSLATION_LANG for auto-translation
MEMVAULT_PORT — Default: 8002
Daily Cron Setup

Add Ebbinghaus decay to your agent's cron:

0 3 * * *  curl -s -X POST 'http://127.0.0.1:8002/decay?user_id=YOUR_USER_ID'

TOOLS.md Snippet
## MemVault 🧠
memvault memorize-text "<user_id>" "<content>" "<context>"
memvault retrieve "<user_id>" "<query>"
memvault decay <user_id>
memvault stats <user_id>
- API: 127.0.0.1:8002

Multi-Agent Memory

Tag memories by source agent:

curl -X POST http://localhost:8002/memorize -H "Content-Type: application/json" \
  -d '{"conversation": [
    {"role": "metadata", "content": "{\"source_agent\": \"research-bot\"}"},
    {"role": "user", "content": "Found new papers on transformers"}
  ], "user_id": "team"}'

Troubleshooting
"Connection refused" → Run docker compose -f ~/.openclaw/workspace/skills/memvault/docker-compose.yml up -d
Slow memorize → Normal, LLM extraction takes 5-15s per conversation
No results from retrieve → Check memvault stats — if total=0, nothing stored yet
All memories fading → Reduce decay_rate: curl -X POST 'http://localhost:8002/decay?decay_rate=0.05'
Weekly Installs
14
Source
skills.volces.c…/wjy9902
First Seen
Mar 24, 2026