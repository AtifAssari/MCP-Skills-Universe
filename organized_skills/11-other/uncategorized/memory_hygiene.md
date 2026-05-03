---
rating: ⭐⭐
title: memory-hygiene
url: https://skills.sh/aaaaqwq/claude-code-skills/memory-hygiene
---

# memory-hygiene

skills/aaaaqwq/claude-code-skills/memory-hygiene
memory-hygiene
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill memory-hygiene
SKILL.md
Memory Hygiene

Keep vector memory lean. Prevent token waste from junk memories.

Quick Commands

Audit: Check what's in memory

memory_recall query="*" limit=50


Wipe: Clear all vector memory

rm -rf ~/.clawdbot/memory/lancedb/


Then restart gateway: clawdbot gateway restart

Reseed: After wipe, store key facts from MEMORY.md

memory_store text="<fact>" category="preference|fact|decision" importance=0.9

Config: Disable Auto-Capture

The main source of junk is autoCapture: true. Disable it:

{
  "plugins": {
    "entries": {
      "memory-lancedb": {
        "config": {
          "autoCapture": false,
          "autoRecall": true
        }
      }
    }
  }
}


Use gateway action=config.patch to apply.

What to Store (Intentionally)

✅ Store:

User preferences (tools, workflows, communication style)
Key decisions (project choices, architecture)
Important facts (accounts, credentials locations, contacts)
Lessons learned

❌ Never store:

Heartbeat status ("HEARTBEAT_OK", "No new messages")
Transient info (current time, temp states)
Raw message logs (already in files)
OAuth URLs or tokens
Monthly Maintenance Cron

Set up a monthly wipe + reseed:

cron action=add job={
  "name": "memory-maintenance",
  "schedule": "0 4 1 * *",
  "text": "Monthly memory maintenance: 1) Wipe ~/.clawdbot/memory/lancedb/ 2) Parse MEMORY.md 3) Store key facts to fresh LanceDB 4) Report completion"
}

Storage Guidelines

When using memory_store:

Keep text concise (<100 words)
Use appropriate category
Set importance 0.7-1.0 for valuable info
One concept per memory entry
Weekly Installs
321
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn