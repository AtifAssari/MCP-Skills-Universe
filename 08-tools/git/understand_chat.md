---
title: understand-chat
url: https://skills.sh/lum1104/understand-anything/understand-chat
---

# understand-chat

skills/lum1104/understand-anything/understand-chat
understand-chat
Installation
$ npx skills add https://github.com/lum1104/understand-anything --skill understand-chat
SKILL.md
/understand-chat

Answer questions about this codebase using the knowledge graph at .understand-anything/knowledge-graph.json.

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

Check that .understand-anything/knowledge-graph.json exists in the current project root. If not, tell the user to run /understand first.

Read project metadata only — use Grep or Read with a line limit to extract just the "project" section from the top of the file for context (name, description, languages, frameworks).

Search for relevant nodes — use Grep to search the knowledge graph file for the user's query keywords: "$ARGUMENTS"

Search "name" fields: grep -i "query_keyword" in the graph file
Search "summary" fields for semantic matches
Search "tags" arrays for topic matches
Note the id values of all matching nodes

Find connected edges — for each matched node ID, Grep for that ID in the edges section to find:

What it imports or depends on (downstream)
What calls or imports it (upstream)
This gives you the 1-hop subgraph around the query

Read layer context — Grep for "layers" to understand which architectural layers the matched nodes belong to.

Answer the query using only the relevant subgraph:

Reference specific files, functions, and relationships from the graph
Explain which layer(s) are relevant and why
Be concise but thorough — link concepts to actual code locations
If the query doesn't match any nodes, say so and suggest related terms from the graph
Weekly Installs
145
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