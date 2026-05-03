---
title: agent-coordination
url: https://skills.sh/ruvnet/ruflo/agent-coordination
---

# agent-coordination

skills/ruvnet/ruflo/agent-coordination
agent-coordination
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill agent-coordination
SKILL.md
Agent Coordination Skill
Purpose

Spawn and coordinate agents for complex multi-agent tasks.

Agent Types
Core Development

coder, reviewer, tester, planner, researcher

V3 Specialized

security-architect, security-auditor, memory-specialist, performance-engineer

Swarm Coordination

hierarchical-coordinator, mesh-coordinator, adaptive-coordinator, collective-intelligence-coordinator

Consensus

byzantine-coordinator, raft-manager, gossip-coordinator, consensus-builder

GitHub

pr-manager, code-review-swarm, issue-tracker, release-manager

SPARC

sparc-coord, sparc-coder, specification, pseudocode, architecture, refinement

Commands
Spawn Agent
npx claude-flow agent spawn --type coder --name my-coder

List Agents
npx claude-flow agent list --filter active

Agent Status
npx claude-flow agent status --id agent-123

Agent Metrics
npx claude-flow agent metrics --id agent-123

Stop Agent
npx claude-flow agent stop --id agent-123

Pool Management
npx claude-flow agent pool --size 5 --type coder

Routing Codes
Code	Task	Agents
1	Bug Fix	coordinator, researcher, coder, tester
3	Feature	coordinator, architect, coder, tester, reviewer
5	Refactor	coordinator, architect, coder, reviewer
7	Performance	coordinator, perf-engineer, coder
9	Security	coordinator, security-architect, auditor
Best Practices
Use hierarchical topology for coordination
Keep agent count under 8 for tight coordination
Use specialized agents for specific tasks
Coordinate via memory, not direct communication
Weekly Installs
192
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass