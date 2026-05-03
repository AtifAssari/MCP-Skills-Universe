---
title: understand-onboard
url: https://skills.sh/lum1104/understand-anything/understand-onboard
---

# understand-onboard

skills/lum1104/understand-anything/understand-onboard
understand-onboard
Installation
$ npx skills add https://github.com/lum1104/understand-anything --skill understand-onboard
SKILL.md
/understand-onboard

Generate a comprehensive onboarding guide from the project's knowledge graph.

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

Read project metadata — use Grep or Read with a line limit to extract the "project" section (name, description, languages, frameworks).

Read layers — Grep for "layers" to get the full layers array. These define the architecture and will structure the guide.

Read the tour — Grep for "tour" to get the guided walkthrough steps. These provide the recommended learning path.

Read file-level nodes only — use Grep to find nodes with "type": "file" in the knowledge graph. Skip function-level and class-level nodes to keep the guide high-level. Extract each file node's name, filePath, summary, and complexity.

Identify complexity hotspots — from the file-level nodes, find those with the highest complexity values. These are areas new developers should approach carefully.

Generate the onboarding guide with these sections:

Project Overview: name, languages, frameworks, description (from project metadata)
Architecture Layers: each layer's name, description, and key files (from layers + file nodes)
Key Concepts: important patterns and design decisions (from node summaries and tags)
Guided Tour: step-by-step walkthrough (from the tour section)
File Map: what each key file does (from file-level nodes, organized by layer)
Complexity Hotspots: areas to approach carefully (from complexity values)

Format as clean markdown

Offer to save the guide to docs/ONBOARDING.md in the project

Suggest the user commit it to the repo for the team

Weekly Installs
148
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