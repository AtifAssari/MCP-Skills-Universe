---
title: debug issue
url: https://skills.sh/tirth8205/code-review-graph/debug-issue
---

# debug issue

skills/tirth8205/code-review-graph/Debug Issue
Debug Issue
Installation
$ npx skills add https://github.com/tirth8205/code-review-graph --skill 'Debug Issue'
SKILL.md
Debug Issue

Use the knowledge graph to systematically trace and debug issues.

Steps
Use semantic_search_nodes to find code related to the issue.
Use query_graph with callers_of and callees_of to trace call chains.
Use get_flow to see full execution paths through suspected areas.
Run detect_changes to check if recent changes caused the issue.
Use get_impact_radius on suspected files to see what else is affected.
Tips
Check both callers and callees to understand the full context.
Look at affected flows to find the entry point that triggers the bug.
Recent changes are the most common source of new issues.
Token Efficiency Rules
ALWAYS start with get_minimal_context(task="<your task>") before any other graph tool.
Use detail_level="minimal" on all calls. Only escalate to "standard" when minimal is insufficient.
Target: complete any review/debug/refactor task in ≤5 tool calls and ≤800 total output tokens.
Weekly Installs
–
Repository
tirth8205/code-…ew-graph
GitHub Stars
14.8K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass