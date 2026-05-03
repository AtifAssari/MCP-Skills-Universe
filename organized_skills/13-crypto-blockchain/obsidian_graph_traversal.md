---
rating: ⭐⭐
title: obsidian-graph-traversal
url: https://skills.sh/richfrem/agent-plugins-skills/obsidian-graph-traversal
---

# obsidian-graph-traversal

skills/richfrem/agent-plugins-skills/obsidian-graph-traversal
obsidian-graph-traversal
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill obsidian-graph-traversal
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Obsidian Graph Traversal

Status: Active Author: Richard Fremmerlid Domain: Obsidian Integration Depends On: obsidian-markdown-mastery (WP05, obsidian-parser)

Purpose

This skill transforms static vault notes into a queryable semantic graph. It answers questions like "What connects to Note X?" and "What are the 2nd-degree connections of Concept A?" — instantly, without rescanning the vault.

Performance Target: < 2 seconds for deep queries across 1000+ notes.

Available Commands
Build the Graph Index
python ./graph_ops.py build --vault-root <path>

Get Forward Links (outbound)
python ./graph_ops.py forward --note "Note Name"

Get Backlinks (inbound)
python ./graph_ops.py backlinks --note "Note Name"

Get N-Degree Connections
python ./graph_ops.py connections --note "Note Name" --depth 2

Find Orphaned Notes
python ./graph_ops.py orphans --vault-root <path>

Architecture
In-Memory Graph Index
On build, every .md file in the vault is parsed using the obsidian-parser
Wikilinks are extracted; embeds (![[...]]) are filtered out
A bidirectional adjacency map is built: {source: [targets], ...} and {target: [sources], ...}
The index is cached as .graph-index.json at the vault root
Invalidation uses file mtime — if a file changed since last build, only that file is re-indexed
The Primary Agent as Librarian

The graph index enables the agent to:

Detect blind spots: Orphaned notes indicate areas where agents act without historical context
Resolve conflicts: If two agents update the same note, the graph shows the impact radius
Enforce schema: Frontmatter metadata (status, trust_score) tracked across linked notes
Weekly Installs
26
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass