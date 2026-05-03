---
title: memory-setup
url: https://skills.sh/sundial-org/awesome-openclaw-skills/memory-setup
---

# memory-setup

skills/sundial-org/awesome-openclaw-skills/memory-setup
memory-setup
Installation
$ npx skills add https://github.com/sundial-org/awesome-openclaw-skills --skill memory-setup
Summary

Configure persistent memory search for Moltbot/Clawdbot agents to retain context across sessions.

Add memorySearch config block with provider (Voyage, OpenAI, or local), sources (memory files and/or sessions), and relevance thresholds
Create a workspace structure with MEMORY.md for curated long-term facts and memory/logs/ for daily timestamped logs
Supports three embedding providers; Voyage recommended but local option available without API keys
Includes troubleshooting for common issues: verify config is enabled, restart gateway, and adjust minScore and maxResults if results lack relevance
SKILL.md
Memory Setup Skill

Transform your agent from goldfish to elephant. This skill helps configure persistent memory for Moltbot/Clawdbot.

Quick Setup
1. Enable Memory Search in Config

Add to ~/.clawdbot/clawdbot.json (or moltbot.json):

{
  "memorySearch": {
    "enabled": true,
    "provider": "voyage",
    "sources": ["memory", "sessions"],
    "indexMode": "hot",
    "minScore": 0.3,
    "maxResults": 20
  }
}

2. Create Memory Structure

In your workspace, create:

workspace/
├── MEMORY.md              # Long-term curated memory
└── memory/
    ├── logs/              # Daily logs (YYYY-MM-DD.md)
    ├── projects/          # Project-specific context
    ├── groups/            # Group chat context
    └── system/            # Preferences, setup notes

3. Initialize MEMORY.md

Create MEMORY.md in workspace root:

# MEMORY.md — Long-Term Memory

## About [User Name]
- Key facts, preferences, context

## Active Projects
- Project summaries and status

## Decisions & Lessons
- Important choices made
- Lessons learned

## Preferences
- Communication style
- Tools and workflows

Config Options Explained
Setting	Purpose	Recommended
enabled	Turn on memory search	true
provider	Embedding provider	"voyage"
sources	What to index	["memory", "sessions"]
indexMode	When to index	"hot" (real-time)
minScore	Relevance threshold	0.3 (lower = more results)
maxResults	Max snippets returned	20
Provider Options
voyage — Voyage AI embeddings (recommended)
openai — OpenAI embeddings
local — Local embeddings (no API needed)
Source Options
memory — MEMORY.md + memory/*.md files
sessions — Past conversation transcripts
both — Full context (recommended)
Daily Log Format

Create memory/logs/YYYY-MM-DD.md daily:

# YYYY-MM-DD — Daily Log

## [Time] — [Event/Task]
- What happened
- Decisions made
- Follow-ups needed

## [Time] — [Another Event]
- Details

Agent Instructions (AGENTS.md)

Add to your AGENTS.md for agent behavior:

## Memory Recall
Before answering questions about prior work, decisions, dates, people, preferences, or todos:
1. Run memory_search with relevant query
2. Use memory_get to pull specific lines if needed
3. If low confidence after search, say you checked

Troubleshooting
Memory search not working?
Check memorySearch.enabled: true in config
Verify MEMORY.md exists in workspace root
Restart gateway: clawdbot gateway restart
Results not relevant?
Lower minScore to 0.2 for more results
Increase maxResults to 30
Check that memory files have meaningful content
Provider errors?
Voyage: Set VOYAGE_API_KEY in environment
OpenAI: Set OPENAI_API_KEY in environment
Use local provider if no API keys available
Verification

Test memory is working:

User: "What do you remember about [past topic]?"
Agent: [Should search memory and return relevant context]


If agent has no memory, config isn't applied. Restart gateway.

Full Config Example
{
  "memorySearch": {
    "enabled": true,
    "provider": "voyage",
    "sources": ["memory", "sessions"],
    "indexMode": "hot",
    "minScore": 0.3,
    "maxResults": 20
  },
  "workspace": "/path/to/your/workspace"
}

Why This Matters

Without memory:

Agent forgets everything between sessions
Repeats questions, loses context
No continuity on projects

With memory:

Recalls past conversations
Knows your preferences
Tracks project history
Builds relationship over time

Goldfish → Elephant. 🐘

Weekly Installs
1.2K
Repository
sundial-org/awe…w-skills
GitHub Stars
589
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass