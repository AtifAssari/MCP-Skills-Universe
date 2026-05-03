---
rating: ⭐⭐
title: consulting-issue-tree-mece
url: https://skills.sh/santos-sanz/lifeskills/consulting-issue-tree-mece
---

# consulting-issue-tree-mece

skills/santos-sanz/lifeskills/consulting-issue-tree-mece
consulting-issue-tree-mece
Installation
$ npx skills add https://github.com/santos-sanz/lifeskills --skill consulting-issue-tree-mece
SKILL.md
MECE Issue Tree

Use $ARGUMENTS as initial context.

When to use this skill
Diagnosing root causes in performance decline or execution failures.
Structuring strategic questions into mutually exclusive branches.
Creating a prioritized analysis plan before data deep-dives.
Aligning teams on problem scope and ownership.
Required inputs
Problem statement, metric, and baseline.
Scope boundaries (segment, geography, time horizon).
Available data and decision deadline.
Workflow
Convert the request into one decision-oriented problem statement.
Select tree type: driver, process, option, or hypothesis tree.
Build 2-3 levels of MECE branches with parallel labels.
Run formal checks for overlap, gaps, and level-mixing.
Prioritize branches by impact, controllability, and learning speed.
Translate top branches into an analysis backlog with owners and timing.
Ask-first questions

Ask up to 3 questions before building the tree:

Which metric and baseline define the problem severity?
What scope is explicitly in or out?
What decision must this tree support?
Assumption policy
Proceed if data is incomplete, but list assumptions in a dedicated section.
Tag assumptions with confidence and validation path.
Do not invent branch evidence; flag unknowns explicitly.
Output contract

Always produce these sections in order:

Context
Decision or Recommendation
Analysis
Risks
Next Actions
Assumptions
Guardrails
No branch overlap at the same level.
No mixing causes and outcomes in one branch layer.
No "other" bucket unless unavoidable and quantified.
Keep branch naming at equivalent abstraction depth.
Resources
references/issue-tree-patterns.md - Tree patterns and branch design rules.
references/mece-checks.md - Validation gates and failure diagnostics.
templates/issue-tree.md - Decision-ready tree template.
examples/issue-tree-example.md - Golden example with partial information.
Keywords

issue tree, MECE, root cause, problem structuring, analysis backlog, driver tree

Weekly Installs
47
Repository
santos-sanz/lifeskills
GitHub Stars
1
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass