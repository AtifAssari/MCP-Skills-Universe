---
rating: ⭐⭐
title: memory-management
url: https://skills.sh/jzocb/openclaw-memory-management/memory-management
---

# memory-management

skills/jzocb/openclaw-memory-management/memory-management
memory-management
Installation
$ npx skills add https://github.com/jzocb/openclaw-memory-management --skill memory-management
SKILL.md
Memory Management Skill

Manage agent memory efficiently using a three-layer architecture with automatic archival.

Quick Setup
Format MEMORY.md with priority tags:
- [P0] Core identity item (never expires)
- [P1][2026-02-10] Active project (90-day TTL)
- [P2][2026-02-10] Temporary item (30-day TTL)

Set up auto-archive cron:
0 4 * * * python3 ~/.openclaw/workspace/scripts/memory-janitor.py

Store lessons in memory/lessons/*.jsonl:
{"id": "lesson-001", "date": "2026-02-10", "category": "infra", "title": "Problem title", "problem": "What happened", "solution": "How to fix", "tags": ["tag1"]}

Three-Layer Architecture

Layer 1: Hot Memory (MEMORY.md)

Always loaded, ≤200 lines
P0: Core identity, never expires
P1: Active projects, 90-day TTL
P2: Temporary, 30-day TTL

Layer 2: Cold Memory (searchable)

memory/lessons/*.jsonl — structured lessons
memory/archive/ — expired content
Use memory_search to recall

Layer 3: Raw Logs

memory/YYYY-MM-DD.md — daily logs
Not loaded automatically
Priority Guidelines
Priority	Use For	TTL
P0	User identity, preferences, safety rules	Never
P1	Active projects, current strategies	90 days
P2	Debug notes, one-time events	30 days
Core Principles (max 5 in AGENTS.md)

Keep only essential rules in AGENTS.md. Other lessons go to lessons/*.jsonl.

Example 5 rules:

Real money = correctness > speed
External actions require confirmation
Check both cron systems (system + OpenClaw)
Long-running processes need setsid isolation
Read platform rules before trading
When Memory Gets Too Large

Run janitor with stats:

python3 scripts/memory-janitor.py --stats


If >200 lines:

Review P0 entries — are they all truly permanent?
Add dates to P1/P2 entries missing them
Move detailed content to lessons/*.jsonl
Run --dry-run then archive
Weekly Installs
160
Repository
jzocb/openclaw-…nagement
GitHub Stars
38
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass