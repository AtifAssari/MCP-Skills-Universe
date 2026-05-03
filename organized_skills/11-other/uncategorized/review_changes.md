---
rating: ⭐⭐
title: review changes
url: https://skills.sh/tirth8205/code-review-graph/review-changes
---

# review changes

skills/tirth8205/code-review-graph/Review Changes
Review Changes
Installation
$ npx skills add https://github.com/tirth8205/code-review-graph --skill 'Review Changes'
SKILL.md
Review Changes

Perform a thorough, risk-aware code review using the knowledge graph.

Steps
Run detect_changes to get risk-scored change analysis.
Run get_affected_flows to find impacted execution paths.
For each high-risk function, run query_graph with pattern="tests_for" to check test coverage.
Run get_impact_radius to understand the blast radius.
For any untested changes, suggest specific test cases.
Output Format

Provide findings grouped by risk level (high/medium/low) with:

What changed and why it matters
Test coverage status
Suggested improvements
Overall merge recommendation
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