---
title: dashboard-creator
url: https://skills.sh/mhattingpete/claude-skills-marketplace/dashboard-creator
---

# dashboard-creator

skills/mhattingpete/claude-skills-marketplace/dashboard-creator
dashboard-creator
Installation
$ npx skills add https://github.com/mhattingpete/claude-skills-marketplace --skill dashboard-creator
SKILL.md
Dashboard Creator

Create interactive HTML dashboards with KPI cards and charts.

When to Use
"Create dashboard for [metrics]"
"Show KPI visualization"
"Generate performance dashboard"
"Make analytics dashboard with charts"
Components
KPI Cards: metric name, value, change %, trend icon
Charts: bar/pie/line using SVG or CSS
Progress Bars: completion indicators
Data Tables: tabular data display
HTML Structure
<!DOCTYPE html>
<html>
<head>
  <title>[Project] Dashboard</title>
  <style>
    body { font-family: system-ui; background: #f7fafc; }
    .kpi-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .kpi-value { font-size: 36px; font-weight: bold; }
    .trend-up { color: #48bb78; }
    .trend-down { color: #e53e3e; }
  </style>
</head>
<body>
  <h1>[Dashboard Name]</h1>
  <div class="grid">
    <!-- KPI cards -->
    <!-- Charts -->
    <!-- Progress bars -->
  </div>
</body>
</html>

KPI Card Pattern
<div class="kpi-card">
  <div class="kpi-label">Revenue</div>
  <div class="kpi-value">$124K</div>
  <div class="trend-up">↑ 12.5%</div>
</div>

Chart Pattern (SVG Bar Chart)
<svg viewBox="0 0 400 300">
  <rect x="50" y="100" width="40" height="150" fill="#4299e1"/>
  <rect x="120" y="80" width="40" height="170" fill="#48bb78"/>
  <!-- bars for each data point -->
</svg>

Workflow
Extract metrics and data
Create KPI cards grid
Generate charts (bar/pie/line) as SVG
Add progress indicators
Write to [name]-dashboard.html

Use semantic colors: green (positive), red (negative), blue (neutral).

Weekly Installs
117
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