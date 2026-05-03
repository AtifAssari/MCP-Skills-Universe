---
rating: ⭐⭐
title: understand-diff
url: https://skills.sh/lum1104/understand-anything/understand-diff
---

# understand-diff

skills/lum1104/understand-anything/understand-diff
understand-diff
Installation
$ npx skills add https://github.com/lum1104/understand-anything --skill understand-diff
SKILL.md
/understand-diff

Analyze the current code changes against the knowledge graph at .understand-anything/knowledge-graph.json.

Graph Structure Reference

The knowledge graph JSON has this structure:

project — {name, description, languages, frameworks, analyzedAt, gitCommitHash}
nodes[] — each has {id, type, name, filePath, summary, tags[], complexity, languageNotes?}
Node types: file, function, class, module, concept
IDs: file:path, function:path:name, class:path:name
edges[] — each has {source, target, type, direction, weight}
Key types: imports, contains, calls, depends_on
layers[] — each has {id, name, description, nodeIds[]}
tour[] — each has {order, title, description, nodeIds[]}
How to Read Efficiently
Use Grep to search within the JSON for relevant entries BEFORE reading the full file
Only read sections you need — don't dump the entire graph into context
Node names and summaries are the most useful fields for understanding
Edges tell you how components connect — follow imports and calls for dependency chains
Instructions

Check that .understand-anything/knowledge-graph.json exists. If not, tell the user to run /understand first.

Get the changed files list (do NOT read the graph yet):

If on a branch with uncommitted changes: git diff --name-only
If on a feature branch: git diff main...HEAD --name-only (or the base branch)
If the user specifies a PR number: get the diff from that PR

Read project metadata only — use Grep or Read with a line limit to extract just the "project" section for context.

Find nodes for changed files — for each changed file path, use Grep to search the knowledge graph for:

Nodes with matching "filePath" values (e.g., grep "changed/file/path")
This finds file nodes AND function/class nodes defined in those files
Note the id values of all matched nodes

Find connected edges (1-hop) — for each matched node ID, Grep for that ID in the edges to find:

What imports or depends on the changed nodes (upstream callers)
What the changed nodes import or call (downstream dependencies)
These are the "affected components" — things that might break or need updating

Identify affected layers — Grep for the matched node IDs in the "layers" section to determine which architectural layers are touched.

Provide structured analysis:

Changed Components: What was directly modified (with summaries from matched nodes)
Affected Components: What might be impacted (from 1-hop edges)
Affected Layers: Which architectural layers are touched and cross-layer concerns
Risk Assessment: Based on node complexity values, number of cross-layer edges, and blast radius (number of affected components)
Suggest what to review carefully and any potential issues

Write diff overlay for dashboard — after producing the analysis, write the diff data to .understand-anything/diff-overlay.json so the dashboard can visualize changed and affected components. The file contains:

{
  "version": "1.0.0",
  "baseBranch": "<the base branch used>",
  "generatedAt": "<ISO timestamp>",
  "changedFiles": ["<list of changed file paths>"],
  "changedNodeIds": ["<node IDs from step 4>"],
  "affectedNodeIds": ["<node IDs from step 5, excluding changedNodeIds>"]
}


After writing, tell the user they can run /understand-anything:understand-dashboard to see the diff overlay visually.

Weekly Installs
143
Repository
lum1104/underst…anything
GitHub Stars
10.2K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass