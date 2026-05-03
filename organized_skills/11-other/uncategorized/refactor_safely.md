---
rating: ⭐⭐
title: refactor safely
url: https://skills.sh/tirth8205/code-review-graph/refactor-safely
---

# refactor safely

skills/tirth8205/code-review-graph/Refactor Safely
Refactor Safely
Installation
$ npx skills add https://github.com/tirth8205/code-review-graph --skill 'Refactor Safely'
SKILL.md
Refactor Safely

Use the knowledge graph to plan and execute refactoring with confidence.

Steps
Use refactor_tool with mode="suggest" for community-driven refactoring suggestions.
Use refactor_tool with mode="dead_code" to find unreferenced code.
For renames, use refactor_tool with mode="rename" to preview all affected locations.
Use apply_refactor_tool with the refactor_id to apply renames.
After changes, run detect_changes to verify the refactoring impact.
Safety Checks
Always preview before applying (rename mode gives you an edit list).
Check get_impact_radius before major refactors.
Use get_affected_flows to ensure no critical paths are broken.
Run find_large_functions to identify decomposition targets.
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