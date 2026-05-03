---
title: plotly-dashboard-skill
url: https://skills.sh/fmschulz/omics-skills/plotly-dashboard-skill
---

# plotly-dashboard-skill

skills/fmschulz/omics-skills/plotly-dashboard-skill
plotly-dashboard-skill
Installation
$ npx skills add https://github.com/fmschulz/omics-skills --skill plotly-dashboard-skill
SKILL.md
Plotly Dashboard Skill

Create interactive dashboards with a single source of truth for UI and figure styling.

Instructions
Capture audience, questions, and data constraints.
Pick a layout pattern and component library.
Define a theme and Plotly figure template.
Build the layout skeleton before callbacks.
Implement callbacks with clear inputs/outputs.
Optimize slow callbacks with caching or pre-aggregation.
Quick Reference
Task	Action
UI style guide	See STYLE_GUIDE.md
Figure template	See FIGURE_STYLE.md
Palettes	See PALETTES.md
App architecture	See DASH_ARCHITECTURE.md
Performance	See PERFORMANCE.md
Input Requirements
Audience and key decisions
Data sources and update cadence
Required filters and views
Deployment constraints
Output
Dash app scaffold (layout + callbacks)
Consistent theming and figure templates
README with usage notes
Quality Gates
 Layout communicates hierarchy and intent
 Callbacks are small and focused
 p95 interaction latency acceptable
 Styling is consistent across charts
Examples
Example 1: Layout-first workflow
Header + filters + KPI row + primary trends + breakdown table

Troubleshooting

Issue: Slow callbacks Solution: Cache expensive steps or pre-aggregate data.

Weekly Installs
17
Repository
fmschulz/omics-skills
GitHub Stars
1
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass