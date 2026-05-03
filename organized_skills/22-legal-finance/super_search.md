---
rating: ⭐⭐
title: super-search
url: https://skills.sh/supermemoryai/claude-supermemory/super-search
---

# super-search

skills/supermemoryai/claude-supermemory/super-search
super-search
Installation
$ npx skills add https://github.com/supermemoryai/claude-supermemory --skill super-search
Summary

Search your coding memory for past work, sessions, and implementation details.

Queries personal session memories, project/repo memories, or both in parallel using optional scope flags (--user, --repo, --both)
Returns formatted results with timestamps and relevance scores to help recall previous decisions, implementations, and coding patterns
Designed for retrieving context about past work when users ask about earlier sessions, how something was implemented, or what they worked on before
SKILL.md
Super Search

Search Supermemory for past coding sessions, decisions, and saved information.

How to Search

Run the search script with the user's query and optional scope flag:

node "${CLAUDE_PLUGIN_ROOT}/scripts/search-memory.cjs" [--user|--repo|--both] "USER_QUERY_HERE"

Scope Flags
--both (default): Search both personal session and project memories across team members in parallel
--user: Search personal/user memories across sessions
--repo: Search project/repo memories across team members
Examples

User asks "what did I work on yesterday":

node "${CLAUDE_PLUGIN_ROOT}/scripts/search-memory.cjs" "work yesterday recent activity"


User asks "how did we implement auth" (project-specific):

node "${CLAUDE_PLUGIN_ROOT}/scripts/search-memory.cjs" --repo "authentication implementation"


User asks "what are my coding preferences":

node "${CLAUDE_PLUGIN_ROOT}/scripts/search-memory.cjs" --user "coding preferences style"

Present Results

The script outputs formatted memory results with timestamps and relevance scores. Present them clearly to the user and offer to search again with different terms if needed.

Weekly Installs
2.9K
Repository
supermemoryai/c…ermemory
GitHub Stars
2.6K
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass