---
rating: ⭐⭐
title: understand-explain
url: https://skills.sh/lum1104/understand-anything/understand-explain
---

# understand-explain

skills/lum1104/understand-anything/understand-explain
understand-explain
Installation
$ npx skills add https://github.com/lum1104/understand-anything --skill understand-explain
SKILL.md
/understand-explain

Provide a thorough, in-depth explanation of a specific code component.

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

Find the target node — use Grep to search the knowledge graph for the component: "$ARGUMENTS"

For file paths (e.g., src/auth/login.ts): search for "filePath" matches
For function notation (e.g., src/auth/login.ts:verifyToken): search for the function name in "name" fields filtered by the file path
Note the exact node id, type, summary, tags, and complexity

Find all connected edges — Grep for the target node's ID in the edges section:

"source" matches → things this node calls/imports/depends on (outgoing)
"target" matches → things that call/import/depend on this node (incoming)
Note the connected node IDs and edge types

Read connected nodes — for each connected node ID from step 3, Grep for those IDs in the nodes section to get their name, summary, and type. This builds the component's neighborhood.

Identify the layer — Grep for the target node's ID in the "layers" section to find which architectural layer it belongs to and that layer's description.

Read the actual source file — Read the source file at the node's filePath for the deep-dive analysis.

Explain the component in context:

Its role in the architecture (which layer, why it exists)
Internal structure (functions, classes it contains — from contains edges)
External connections (what it imports, what calls it, what it depends on — from edges)
Data flow (inputs → processing → outputs — from source code)
Explain clearly, assuming the reader may not know the programming language
Highlight any patterns, idioms, or complexity worth understanding
Weekly Installs
146
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