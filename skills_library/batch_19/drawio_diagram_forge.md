---
title: drawio-diagram-forge
url: https://skills.sh/aktsmm/agent-skills/drawio-diagram-forge
---

# drawio-diagram-forge

skills/aktsmm/agent-skills/drawio-diagram-forge
drawio-diagram-forge
Installation
$ npx skills add https://github.com/aktsmm/agent-skills --skill drawio-diagram-forge
SKILL.md
Draw.io Diagram Forge

Generate draw.io editable diagrams using AI-powered workflow.

When to Use
Creating architecture diagrams (Azure, AWS)
Converting flowcharts from text descriptions
Transforming images/screenshots into editable format
Generating swimlane, sequence diagrams
Prerequisites
Tool	Required
VS Code	Yes
Draw.io Integration	Yes
GitHub Copilot	Yes
Quick Start
Create a login flow diagram

Generate an Azure Hub-Spoke architecture diagram

From inputs/requirements.md, create a system diagram

Output Formats
Extension	Description	When to Use
*.drawio	Native format	Recommended
*.drawio.svg	SVG + metadata	Markdown/Web
*.drawio.png	PNG + metadata	Image with edit

Output: outputs/

Recommended Delivery Pattern

For documentation-facing diagrams, generate outputs as a pair:

name.drawio for editing in VS Code Draw.io
name.drawio.svg for README / web embedding

Recommended markdown pattern:

![Architecture Diagram](outputs/name.drawio.svg)

- [outputs/name.drawio.svg](outputs/name.drawio.svg)
- [outputs/name.drawio](outputs/name.drawio)


If multilingual variants are needed, keep parallel filenames instead of overwriting a single asset:

name.drawio / name.drawio.svg
name-ja.drawio / name-ja.drawio.svg

This keeps the editable source, the embeddable image, and the language variants aligned.

Workflow
USER INPUT → ORCHESTRATOR → MANIFEST GATEWAY → SVG FORGE → COMPLETED

Quality Gates
Score	Action
90-100	Proceed
70-84	Fix and retry
50-69	Simplify
0-29	Ask user
Limits
Limit	Value
Manifest revision	2
SVG revision	2
Total timeout	45min
Cloud Icons

→ references/cloud-icons.md

Enable in VS Code
Open .drawio file
Click "+ More Shapes" (bottom-left)
Enable: Azure, AWS
Apply
Azure Format (Critical)
<!-- WRONG -->
<mxCell style="shape=mxgraph.azure.front_door;..." />

<!-- CORRECT -->
<mxCell style="aspect=fixed;image=img/lib/azure2/networking/Front_Doors.svg;..." />

References
File	Description
mxcell-structure.md	mxCell XML structure
cloud-icons.md	Azure/AWS icon guide
style-guide.md	Node colors, edge styles
Scripts
Script	Description
scripts/validate_drawio.py	Validate mxCell structure
Troubleshooting
Issue	Solution
Blank in draw.io	Check content attribute
Edges not visible	Verify node IDs
Icons missing	Enable Azure/AWS shapes
README image only links to source	Generate *.drawio.svg and embed that instead of linking only to *.drawio
Too many crossing arrows	Simplify the main flow first, then move secondary flows to separate lanes or separate diagrams
Done Criteria
 .drawio or .drawio.svg file generated
 Diagram opens correctly in VS Code Draw.io extension
 All nodes and edges visible
 Quality gate score ≥ 85
 If diagram is referenced from documentation, both editable source and embeddable image are provided
Weekly Installs
95
Repository
aktsmm/agent-skills
GitHub Stars
11
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass