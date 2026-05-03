---
rating: ⭐⭐
title: agent-memory-mcp
url: https://skills.sh/sickn33/antigravity-awesome-skills/agent-memory-mcp
---

# agent-memory-mcp

skills/sickn33/antigravity-awesome-skills/agent-memory-mcp
agent-memory-mcp
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill agent-memory-mcp
Summary

Persistent, searchable memory system for agents to store and retrieve architectural decisions, patterns, and project knowledge.

Provides four core MCP tools: memory_search for querying by text/type/tags, memory_write to record decisions and patterns, memory_read to retrieve specific entries, and memory_stats for usage analytics
Runs as an MCP server that syncs with project documentation, enabling long-term knowledge retention across agent sessions
Includes a standalone dashboard (port 3333) for visualizing memory usage and organization
Requires Node.js v18+ and simple npm-based setup with a helper script to bind the memory bank to your project workspace
SKILL.md
Agent Memory Skill

This skill provides a persistent, searchable memory bank that automatically syncs with project documentation. It runs as an MCP server to allow reading/writing/searching of long-term memories.

Prerequisites
Node.js (v18+)
Setup

Clone the Repository: Clone the agentMemory project into your agent's workspace or a parallel directory:

git clone https://github.com/webzler/agentMemory.git .agent/skills/agent-memory


Install Dependencies:

cd .agent/skills/agent-memory
npm install
npm run compile


Start the MCP Server: Use the helper script to activate the memory bank for your current project:

npm run start-server <project_id> <absolute_path_to_target_workspace>


Example for current directory:

npm run start-server my-project $(pwd)

Capabilities (MCP Tools)
memory_search

Search for memories by query, type, or tags.

Args: query (string), type? (string), tags? (string[])
Usage: "Find all authentication patterns" -> memory_search({ query: "authentication", type: "pattern" })
memory_write

Record new knowledge or decisions.

Args: key (string), type (string), content (string), tags? (string[])
Usage: "Save this architecture decision" -> memory_write({ key: "auth-v1", type: "decision", content: "..." })
memory_read

Retrieve specific memory content by key.

Args: key (string)
Usage: "Get the auth design" -> memory_read({ key: "auth-v1" })
memory_stats

View analytics on memory usage.

Usage: "Show memory statistics" -> memory_stats({})
Dashboard

This skill includes a standalone dashboard to visualize memory usage.

npm run start-dashboard <absolute_path_to_target_workspace>


Access at: http://localhost:3333

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
787
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn