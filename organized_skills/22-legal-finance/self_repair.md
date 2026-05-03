---
rating: ⭐⭐
title: self-repair
url: https://skills.sh/simhacker/moollm/self-repair
---

# self-repair

skills/simhacker/moollm/self-repair
self-repair
Installation
$ npx skills add https://github.com/simhacker/moollm --skill self-repair
SKILL.md
Self Repair

Missing state triggers repair, not failure.

Checklist-based self-healing demons.

[!IMPORTANT] NEVER-CRASH — The core principle. Repair instead of fail. Always.

The Principle

When something's wrong:

Detect — Checklist finds missing/invalid state
Repair — Demon creates/fixes what's needed
Log — Document what was repaired
Continue — Never crash, always converge
Contents
File	Purpose
SKILL.md	Full protocol documentation
CHECKLIST.yml.tmpl	Checklist template
Repair Demons
Demon	Watches For
checklist_repairer	Missing canonical files
sticky_note_maintainer	Missing sidecar metadata
membrane_keeper	Files outside boundaries
The Intertwingularity

Self-repair is the immune system. It monitors everything.

graph LR
    SR[🔧 self-repair] -->|monitors| SL[📜 session-log]
    SR -->|monitors| WS[working-set.yml]
    SR -->|creates| HOT[hot.yml / cold.yml]
    SR -->|repairs| FILES[missing files]
    
    SR -->|part of| KERNEL[kernel/self-healing]

Dovetails With
Sister Skills
Skill	Relationship
session-log/	Self-repair monitors log integrity
summarize/	Triggered when context exceeds budget
honest-forget/	Graceful memory decay
Protocol Symbols
Symbol	Link
NEVER-CRASH	PROTOCOLS.yml
REPAIR-DEMON	PROTOCOLS.yml
ROBUST-FIRST	PROTOCOLS.yml
BEST-EFFORT	PROTOCOLS.yml
Kernel
kernel/self-healing-protocol.md — Full specification
schemas/agent-directory-schema.yml — What gets repaired
Navigation
Direction	Destination
⬆️ Up	skills/
⬆️⬆️ Root	Project Root
📜 Sister	session-log/
Weekly Installs
37
Repository
simhacker/moollm
GitHub Stars
38
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass