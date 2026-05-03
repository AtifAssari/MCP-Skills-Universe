---
rating: ⭐⭐⭐
title: architecture-diagram-creator
url: https://skills.sh/mhattingpete/claude-skills-marketplace/architecture-diagram-creator
---

# architecture-diagram-creator

skills/mhattingpete/claude-skills-marketplace/architecture-diagram-creator
architecture-diagram-creator
Installation
$ npx skills add https://github.com/mhattingpete/claude-skills-marketplace --skill architecture-diagram-creator
SKILL.md
Architecture Diagram Creator

Create comprehensive HTML architecture diagrams with data flows, business context, and system architecture.

When to Use
"Create architecture diagram for [project]"
"Generate high-level overview"
"Document system architecture"
"Show data flow and processing pipeline"
Components to Include
Business Context: objectives, users, value, metrics
Data Flow: sources → processing → outputs with SVG diagram
Processing Pipeline: multi-stage visualization
System Architecture: layered components (data/processing/services/output)
Features: functional and non-functional requirements
Deployment: model, prerequisites, workflows
HTML Structure
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Project] Architecture</title>
  <style>
    body { font-family: system-ui; max-width: 1200px; margin: 0 auto; padding: 20px; }
    h1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; }
    .section { margin: 30px 0; }
    svg { max-width: 100%; }
    /* Use semantic colors: #4299e1 (data), #ed8936 (processing), #9f7aea (AI), #48bb78 (success) */
  </style>
</head>
<body>
  <h1>[Project Name] - Architecture Overview</h1>

  <!-- Business Context Section -->
  <!-- Data Flow Diagram (SVG) -->
  <!-- Processing Pipeline (SVG) -->
  <!-- System Architecture Layers -->
  <!-- Features Grid -->
  <!-- Deployment Info -->
</body>
</html>

SVG Pattern for Data Flow
<svg viewBox="0 0 800 400">
  <!-- Data sources (left, blue) -->
  <rect x="50" y="150" width="120" height="80" fill="#4299e1"/>

  <!-- Processing (center, orange) -->
  <rect x="340" y="150" width="120" height="80" fill="#ed8936"/>

  <!-- Outputs (right, green) -->
  <rect x="630" y="150" width="120" height="80" fill="#48bb78"/>

  <!-- Arrows connecting -->
  <path d="M170,190 L340,190" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>
</svg>

Workflow
Analyze project (README, code structure)
Extract: purpose, data sources, processing, tech stack, outputs
Create HTML with all 6 sections
Use semantic colors for visual hierarchy
Write to [project]-architecture.html

Keep diagrams clear, use consistent styling, include real project details.

Weekly Installs
239
Repository
mhattingpete/cl…ketplace
GitHub Stars
563
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass