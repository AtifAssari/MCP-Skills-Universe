---
title: exocortex
url: https://skills.sh/totto2727-dotfiles/agents/exocortex
---

# exocortex

skills/totto2727-dotfiles/agents/exocortex
exocortex
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill exocortex
SKILL.md
Exocortex MCP Server

A "second brain" for AI agents — persist insights, recall past decisions, and build knowledge graphs across sessions.

Core Tools
Tool	Purpose
exo_store_memory	Persist insights with tags, context, and optional "painful memory" flag
exo_recall_memories	Search knowledge base with natural language queries and filters
exo_link_memories	Connect memories via relations (related, extends, depends_on, supersedes, contradicts, evolved_from, rejected_because, caused_by)
exo_explore_related	Discover adjacent knowledge through links, tags, and context
exo_trace_lineage	Trace decision evolution backward/forward through relations
exo_curiosity_scan	Detect contradictions, orphans, and outdated information
exo_sleep	Background maintenance: deduplication, orphan rescue, pattern mining
exo_consolidate	Extract common themes from similar memories
exo_analyze_knowledge	Diagnose health issues (orphans, stale content)
exo_get_stats	Knowledge base overview with counts and trending tags
Basic Workflow
Session Start: exo_recall_memories — retrieve relevant context
During Work: exo_store_memory — persist discoveries with structured Problem/Solution/Rationale sections and specific tags
Session End: exo_sleep — consolidate and maintain the knowledge base
Relation Types Guide

Choose the appropriate relation when linking memories:

Relation	Use When
related	Two memories share a topic but neither depends on the other
extends	Memory B adds detail or depth to memory A
depends_on	Memory B requires knowledge from memory A
supersedes	Memory B replaces an outdated memory A
contradicts	Two memories contain conflicting information
evolved_from	Memory B is a refined version of memory A
rejected_because	A decision was abandoned — link to the reason
caused_by	An outcome was triggered by a prior event or decision
Tagging Strategy
Use specific, lowercase tags: auth-flow, postgres-migration, api-v2
Include a category prefix for large knowledge bases: bug:, decision:, pattern:
Tag with the project or module name to scope recall: billing-service, frontend-auth
Mark time-sensitive insights with a date tag: 2026-03, sprint-42
Storing Effective Memories

Structure the content field for maximum recall value:

**Problem:** [What happened or what question arose]
**Solution:** [What was done or decided]
**Rationale:** [Why this approach was chosen]
**Tags:** specific-module, decision-type

Reference
Usage Guide
Weekly Installs
11
Repository
totto2727-dotfi…s/agents
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass