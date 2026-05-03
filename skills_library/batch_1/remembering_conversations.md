---
title: remembering-conversations
url: https://skills.sh/obra/episodic-memory/remembering-conversations
---

# remembering-conversations

skills/obra/episodic-memory/remembering-conversations
remembering-conversations
Installation
$ npx skills add https://github.com/obra/episodic-memory --skill remembering-conversations
Summary

Search conversation history to avoid reinventing solutions and inform architectural decisions.

Dispatch the search-conversations subagent to query past conversations; the agent synthesizes results into actionable insights with sources
Use after understanding the task when facing "how should I..." questions, architectural decisions, or unfamiliar workflows
Activate when stuck on complex problems, following past patterns, or when user references previous work or decisions
Avoid searching for current codebase structure or information already in the active conversation; explore code first with grep or read tools
SKILL.md
Remembering Conversations

Core principle: Search before reinventing. Searching costs nothing; reinventing or repeating mistakes costs everything.

Mandatory: Use the Search Agent

YOU MUST dispatch the search-conversations agent for any historical search.

Announce: "Dispatching search agent to find [topic]."

Then use the Task tool with subagent_type: "search-conversations":

Task tool:
  description: "Search past conversations for [topic]"
  prompt: "Search for [specific query or topic]. Focus on [what you're looking for - e.g., decisions, patterns, gotchas, code examples]."
  subagent_type: "search-conversations"


The agent will:

Search with the search tool
Read top 2-5 results with the show tool
Synthesize findings (200-1000 words)
Return actionable insights + sources

Saves 50-100x context vs. loading raw conversations.

When to Use

You often get value out of consulting your episodic memory once you understand what you're being asked. Search memory in these situations:

After understanding the task:

User asks "how should I..." or "what's the best approach..."
You've explored current codebase and need to make architectural decisions
User asks for implementation approach after describing what they want

When you're stuck:

You've investigated a problem and can't find the solution
Facing a complex problem without obvious solution in current code
Need to follow an unfamiliar workflow or process

When historical signals are present:

User says "last time", "before", "we discussed", "you implemented"
User asks "why did we...", "what was the reason..."
User says "do you remember...", "what do we know about..."

Don't search first:

For current codebase structure (use Grep/Read to explore first)
For info in current conversation
Before understanding what you're being asked to do
Direct Tool Access (Discouraged)

You CAN use MCP tools directly, but DON'T:

mcp__plugin_episodic-memory_episodic-memory__search
mcp__plugin_episodic-memory_episodic-memory__show

Using these directly wastes your context window. Always dispatch the agent instead.

See MCP-TOOLS.md for complete API reference if needed for advanced usage.

Weekly Installs
7.7K
Repository
obra/episodic-memory
GitHub Stars
366
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass