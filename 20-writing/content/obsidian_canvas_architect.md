---
title: obsidian-canvas-architect
url: https://skills.sh/richfrem/agent-plugins-skills/obsidian-canvas-architect
---

# obsidian-canvas-architect

skills/richfrem/agent-plugins-skills/obsidian-canvas-architect
obsidian-canvas-architect
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill obsidian-canvas-architect
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Obsidian Canvas Architect

Status: Active Author: Richard Fremmerlid Domain: Obsidian Integration Depends On: obsidian-vault-crud (WP06)

Purpose

Obsidian Canvas files (.canvas) use the JSON Canvas Spec 1.0 to define visual boards with nodes (text, file references, URLs) connected by directional edges. This skill lets agents programmatically generate visual planning boards, architecture diagrams, and execution flowcharts.

JSON Canvas Spec 1.0 Overview

A .canvas file is JSON with two top-level arrays:

{
  "nodes": [
    {"id": "1", "type": "text", "text": "Hello", "x": 0, "y": 0, "width": 250, "height": 60},
    {"id": "2", "type": "file", "file": "path/to/note.md", "x": 300, "y": 0, "width": 250, "height": 60}
  ],
  "edges": [
    {"id": "e1", "fromNode": "1", "toNode": "2", "fromSide": "right", "toSide": "left"}
  ]
}

Node Types
Type	Required Fields	Purpose
text	text, x, y, width, height	Inline text content
file	file, x, y, width, height	Reference to a vault note
link	url, x, y, width, height	External URL
group	label, x, y, width, height	Visual grouping container
Edge Properties
Field	Required	Description
fromNode	Yes	Source node ID
toNode	Yes	Target node ID
fromSide	No	top, right, bottom, left
toSide	No	top, right, bottom, left
label	No	Edge label text
Available Commands
Create a Canvas
python ./canvas_ops.py create --file <path.canvas>

Add a Node
python ./canvas_ops.py add-node \
  --file <path.canvas> --type text --text "My Node" --x 100 --y 200

Add an Edge
python ./canvas_ops.py add-edge \
  --file <path.canvas> --from-node id1 --to-node id2

Read a Canvas
python ./canvas_ops.py read --file <path.canvas>

Safety Guarantees
All writes go through obsidian-vault-crud atomic write protocol
Malformed JSON triggers a clean error report, never a crash
Node IDs are auto-generated (UUID) to prevent collisions
Schema validation ensures all required fields are present before write
Weekly Installs
22
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