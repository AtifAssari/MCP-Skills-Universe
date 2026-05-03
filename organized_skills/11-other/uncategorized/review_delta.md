---
rating: ⭐⭐
title: review-delta
url: https://skills.sh/tirth8205/code-review-graph/review-delta
---

# review-delta

skills/tirth8205/code-review-graph/review-delta
review-delta
Installation
$ npx skills add https://github.com/tirth8205/code-review-graph --skill review-delta
SKILL.md
Review Delta

Perform a focused, token-efficient code review of only the changed code and its blast radius.

Token optimization: Before starting, call get_docs_section_tool(section_name="review-delta") for the optimized workflow. Use ONLY changed nodes + 2-hop neighbors in context.

Steps

Ensure the graph is current by calling build_or_update_graph_tool() (incremental update).

Get review context by calling get_review_context_tool(). This returns:

Changed files (auto-detected from git diff)
Impacted nodes and files (blast radius)
Source code snippets for changed areas
Review guidance (test coverage gaps, wide impact warnings, inheritance concerns)

Analyze the blast radius by reviewing the impacted_nodes and impacted_files in the context. Focus on:

Functions whose callers changed (may need signature/behavior verification)
Classes with inheritance changes (Liskov substitution concerns)
Files with many dependents (high-risk changes)

Perform the review using the context. For each changed file:

Review the source snippet for correctness, style, and potential bugs
Check if impacted callers/dependents need updates
Verify test coverage using query_graph_tool(pattern="tests_for", target=<function_name>)
Flag any untested changed functions

Report findings in a structured format:

Summary: One-line overview of the changes
Risk level: Low / Medium / High (based on blast radius)
Issues found: Bugs, style issues, missing tests
Blast radius: List of impacted files/functions
Recommendations: Actionable suggestions
Advantages Over Full-Repo Review
Only sends changed + impacted code to the model (5-10x fewer tokens)
Automatically identifies blast radius without manual file searching
Provides structural context (who calls what, inheritance chains)
Flags untested functions automatically
Weekly Installs
139
Repository
tirth8205/code-…ew-graph
GitHub Stars
14.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass