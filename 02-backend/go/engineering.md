---
title: engineering
url: https://skills.sh/markdown-viewer/skills/engineering
---

# engineering

skills/markdown-viewer/skills/engineering
engineering
Installation
$ npx skills add https://github.com/markdown-viewer/skills --skill engineering
SKILL.md
Engineering Diagram Generator

Quick Start: Choose diagram type → Add symbols from stencil library → Connect with appropriate lines → Add labels/annotations → Wrap in ```drawio fence.

⚠️ IMPORTANT: Always use ```drawio code fence. NEVER use ```xml — it will NOT render as a diagram.

Critical Rules

🔗 This is a drawio-derived skill. All structure, layout, and edge routing rules inherit from drawio SKILL.md. Read the base rules first.

Engineering-specific additions:

Check stencils/README.md for exact symbol names (e.g., mxgraph.electrical.resistors.resistor_1)
Symbol colors: Black(#000000) for schematic, Blue(#0000FF) for pneumatic, Green(#00FF00) for hydraulic
Engineering Diagram Types
Type	Purpose	Stencil Library	Example
Electrical Schematic	Circuit diagrams, wiring diagrams	mxgraph.electrical.* (527 symbols)	electrical-circuit.md
P&ID	Process flow, piping & instrumentation	mxgraph.pid.* (478 symbols)	pid-process.md
Rack Diagram	Data center, server rack layout	mxgraph.rack.* (487 symbols)	rack-datacenter.md
Logic Gates	Digital logic circuits	mxgraph.electrical.logic_gates.*	logic-gates.md
Fault Tree	Fault tree analysis (FTA)	mxgraph.electrical.logic_gates.*	fault-tree.md
PLC Ladder	PLC ladder logic diagrams	mxgraph.electrical.plc_ladder.*	plc-ladder.md
Weekly Installs
113
Repository
markdown-viewer/skills
GitHub Stars
2.4K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass