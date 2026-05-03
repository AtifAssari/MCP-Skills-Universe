---
rating: ⭐⭐
title: hive-mind
url: https://skills.sh/ruvnet/ruflo/hive-mind
---

# hive-mind

skills/ruvnet/ruflo/hive-mind
hive-mind
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill hive-mind
SKILL.md
Hive-Mind Skill
Purpose

Byzantine fault-tolerant consensus and distributed swarm coordination.

When to Trigger
Multi-agent distributed tasks
Fault-tolerant operations needed
Collective decision making
Complex coordination patterns
Topologies
Topology	Description	Use Case
hierarchical	Queen controls workers	Default, anti-drift
mesh	Fully connected peers	Research, exploration
hierarchical-mesh	Hybrid	Recommended for complex
adaptive	Dynamic based on load	Auto-scaling
Consensus Strategies
Strategy	Tolerance	Use Case
byzantine	f < n/3 faulty	Untrusted environment
raft	f < n/2 faulty	Leader-based, consistent
gossip	Eventual	Large scale, availability
crdt	Conflict-free	Concurrent updates
quorum	Configurable	Tunable consistency
Commands
Initialize Hive-Mind
npx claude-flow hive-mind init --topology hierarchical-mesh --consensus raft

Spawn Queen
npx claude-flow hive-mind spawn --role queen --name coordinator

Check Consensus Status
npx claude-flow hive-mind consensus --status

View Sessions
npx claude-flow hive-mind sessions --active

Best Practices
Use hierarchical for coding tasks (anti-drift)
Use raft consensus for consistency
Keep agent count under 8 for coordination
Run frequent checkpoints
Weekly Installs
186
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass