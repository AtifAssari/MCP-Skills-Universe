---
title: flowchart-creator
url: https://skills.sh/mhattingpete/claude-skills-marketplace/flowchart-creator
---

# flowchart-creator

skills/mhattingpete/claude-skills-marketplace/flowchart-creator
flowchart-creator
Installation
$ npx skills add https://github.com/mhattingpete/claude-skills-marketplace --skill flowchart-creator
SKILL.md
Flowchart Creator

Create interactive HTML flowcharts and process diagrams.

When to Use
"Create flowchart for [process]"
"Generate process flow diagram"
"Make decision tree for [workflow]"
"Show workflow visualization"
Components
Start/End nodes: rounded rectangles (#48bb78 green, #e53e3e red)
Process boxes: rectangles (#4299e1 blue)
Decision diamonds: diamonds (#f59e0b orange)
Arrows: connecting paths with labels
Swimlanes: grouped sections (optional)
HTML Structure
<!DOCTYPE html>
<html>
<head>
  <title>[Process] Flowchart</title>
  <style>
    body { font-family: system-ui; }
    svg { max-width: 100%; }
    .start-end { fill: #48bb78; }
    .process { fill: #4299e1; }
    .decision { fill: #f59e0b; }
  </style>
</head>
<body>
  <h1>[Process Name] Flowchart</h1>
  <svg viewBox="0 0 800 600">
    <!-- flowchart nodes and connectors -->
  </svg>
</body>
</html>

Node Patterns
<!-- Start/End (rounded rect) -->
<rect x="350" y="50" width="100" height="50" rx="25" class="start-end"/>
<text x="400" y="80" text-anchor="middle">Start</text>

<!-- Process box -->
<rect x="350" y="150" width="100" height="60" class="process"/>
<text x="400" y="185" text-anchor="middle">Process</text>

<!-- Decision diamond -->
<path d="M400,250 L450,280 L400,310 L350,280 Z" class="decision"/>
<text x="400" y="285" text-anchor="middle">Decision?</text>

<!-- Arrow -->
<path d="M400,100 L400,150" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>

Workflow
Break down process into steps
Identify decision points
Layout nodes vertically or horizontally
Connect with arrows
Add labels to decision branches
Write to [process]-flowchart.html

Keep layout clean, use consistent spacing (100px between nodes).

Weekly Installs
232
Repository
mhattingpete/cl…ketplace
GitHub Stars
563
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass