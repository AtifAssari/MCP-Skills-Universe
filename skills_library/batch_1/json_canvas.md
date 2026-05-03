---
title: json-canvas
url: https://skills.sh/kepano/obsidian-skills/json-canvas
---

# json-canvas

skills/kepano/obsidian-skills/json-canvas
json-canvas
Installation
$ npx skills add https://github.com/kepano/obsidian-skills --skill json-canvas
Summary

Create and edit JSON Canvas files with nodes, edges, groups, and visual connections.

Supports four node types: text (with Markdown), file references, external links, and visual groups for organizing layouts
Edges connect nodes with optional labels, directional arrows, anchor points (top/right/bottom/left), and color coding
Includes comprehensive validation workflows: ID uniqueness checks, edge reference integrity, and JSON parsing to prevent broken canvases
Provides layout guidelines with suggested dimensions for different node types and spacing rules to avoid overlaps
SKILL.md
JSON Canvas Skill
File Structure

A canvas file (.canvas) contains two top-level arrays following the JSON Canvas Spec 1.0:

{
  "nodes": [],
  "edges": []
}

nodes (optional): Array of node objects
edges (optional): Array of edge objects connecting nodes
Common Workflows
1. Create a New Canvas
Create a .canvas file with the base structure {"nodes": [], "edges": []}
Generate unique 16-character hex IDs for each node (e.g., "6f0ad84f44ce9c17")
Add nodes with required fields: id, type, x, y, width, height
Add edges referencing valid node IDs via fromNode and toNode
Validate: Parse the JSON to confirm it is valid. Verify all fromNode/toNode values exist in the nodes array
2. Add a Node to an Existing Canvas
Read and parse the existing .canvas file
Generate a unique ID that does not collide with existing node or edge IDs
Choose position (x, y) that avoids overlapping existing nodes (leave 50-100px spacing)
Append the new node object to the nodes array
Optionally add edges connecting the new node to existing nodes
Validate: Confirm all IDs are unique and all edge references resolve to existing nodes
3. Connect Two Nodes
Identify the source and target node IDs
Generate a unique edge ID
Set fromNode and toNode to the source and target IDs
Optionally set fromSide/toSide (top, right, bottom, left) for anchor points
Optionally set label for descriptive text on the edge
Append the edge to the edges array
Validate: Confirm both fromNode and toNode reference existing node IDs
4. Edit an Existing Canvas
Read and parse the .canvas file as JSON
Locate the target node or edge by id
Modify the desired attributes (text, position, color, etc.)
Write the updated JSON back to the file
Validate: Re-check all ID uniqueness and edge reference integrity after editing
Nodes

Nodes are objects placed on the canvas. Array order determines z-index: first node = bottom layer, last node = top layer.

Generic Node Attributes
Attribute	Required	Type	Description
id	Yes	string	Unique 16-char hex identifier
type	Yes	string	text, file, link, or group
x	Yes	integer	X position in pixels
y	Yes	integer	Y position in pixels
width	Yes	integer	Width in pixels
height	Yes	integer	Height in pixels
color	No	canvasColor	Preset "1"-"6" or hex (e.g., "#FF0000")
Text Nodes
Attribute	Required	Type	Description
text	Yes	string	Plain text with Markdown syntax
{
  "id": "6f0ad84f44ce9c17",
  "type": "text",
  "x": 0,
  "y": 0,
  "width": 400,
  "height": 200,
  "text": "# Hello World\n\nThis is **Markdown** content."
}


Newline pitfall: Use \n for line breaks in JSON strings. Do not use the literal \\n -- Obsidian renders that as the characters \ and n.

File Nodes
Attribute	Required	Type	Description
file	Yes	string	Path to file within the system
subpath	No	string	Link to heading or block (starts with #)
{
  "id": "a1b2c3d4e5f67890",
  "type": "file",
  "x": 500,
  "y": 0,
  "width": 400,
  "height": 300,
  "file": "Attachments/diagram.png"
}

Link Nodes
Attribute	Required	Type	Description
url	Yes	string	External URL
{
  "id": "c3d4e5f678901234",
  "type": "link",
  "x": 1000,
  "y": 0,
  "width": 400,
  "height": 200,
  "url": "https://obsidian.md"
}

Group Nodes

Groups are visual containers for organizing other nodes. Position child nodes inside the group's bounds.

Attribute	Required	Type	Description
label	No	string	Text label for the group
background	No	string	Path to background image
backgroundStyle	No	string	cover, ratio, or repeat
{
  "id": "d4e5f6789012345a",
  "type": "group",
  "x": -50,
  "y": -50,
  "width": 1000,
  "height": 600,
  "label": "Project Overview",
  "color": "4"
}

Edges

Edges connect nodes via fromNode and toNode IDs.

Attribute	Required	Type	Default	Description
id	Yes	string	-	Unique identifier
fromNode	Yes	string	-	Source node ID
fromSide	No	string	-	top, right, bottom, or left
fromEnd	No	string	none	none or arrow
toNode	Yes	string	-	Target node ID
toSide	No	string	-	top, right, bottom, or left
toEnd	No	string	arrow	none or arrow
color	No	canvasColor	-	Line color
label	No	string	-	Text label
{
  "id": "0123456789abcdef",
  "fromNode": "6f0ad84f44ce9c17",
  "fromSide": "right",
  "toNode": "a1b2c3d4e5f67890",
  "toSide": "left",
  "toEnd": "arrow",
  "label": "leads to"
}

Colors

The canvasColor type accepts either a hex string or a preset number:

Preset	Color
"1"	Red
"2"	Orange
"3"	Yellow
"4"	Green
"5"	Cyan
"6"	Purple

Preset color values are intentionally undefined -- applications use their own brand colors.

ID Generation

Generate 16-character lowercase hexadecimal strings (64-bit random value):

"6f0ad84f44ce9c17"
"a3b2c1d0e9f8a7b6"

Layout Guidelines
Coordinates can be negative (canvas extends infinitely)
x increases right, y increases down; position is the top-left corner
Space nodes 50-100px apart; leave 20-50px padding inside groups
Align to grid (multiples of 10 or 20) for cleaner layouts
Node Type	Suggested Width	Suggested Height
Small text	200-300	80-150
Medium text	300-450	150-300
Large text	400-600	300-500
File preview	300-500	200-400
Link preview	250-400	100-200
Validation Checklist

After creating or editing a canvas file, verify:

All id values are unique across both nodes and edges
Every fromNode and toNode references an existing node ID
Required fields are present for each node type (text for text nodes, file for file nodes, url for link nodes)
type is one of: text, file, link, group
fromSide/toSide values are one of: top, right, bottom, left
fromEnd/toEnd values are one of: none, arrow
Color presets are "1" through "6" or valid hex (e.g., "#FF0000")
JSON is valid and parseable

If validation fails, check for duplicate IDs, dangling edge references, or malformed JSON strings (especially unescaped newlines in text content).

Complete Examples

See references/EXAMPLES.md for full canvas examples including mind maps, project boards, research canvases, and flowcharts.

References
JSON Canvas Spec 1.0
JSON Canvas GitHub
Weekly Installs
17.9K
Repository
kepano/obsidian-skills
GitHub Stars
28.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass