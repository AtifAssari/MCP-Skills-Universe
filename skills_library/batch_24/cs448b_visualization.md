---
title: cs448b-visualization
url: https://skills.sh/sundial-org/skills/cs448b-visualization
---

# cs448b-visualization

skills/sundial-org/skills/cs448b-visualization
cs448b-visualization
Installation
$ npx skills add https://github.com/sundial-org/skills --skill cs448b-visualization
SKILL.md
CS448B Visualization
When to Use Each Reference
Reference	Use When
encoding-perception.md	Choosing how to map data to visual properties, or evaluating if encodings are effective
chart-design.md	Deciding which chart type fits the data, or configuring axes/scales
d3-patterns.md	Writing D3.js code for bindings, scales, axes, transitions
interaction-animation.md	Adding brushing, filtering, tooltips, or animated transitions
color.md	Selecting color palettes or ensuring accessibility
networks-text.md	Visualizing graphs, hierarchies, or text/document data
Critique Checklist

When reviewing any visualization:

Expressiveness - Does it show all the data? Only the data? No misleading elements?
Effectiveness - Is the most important data on the most accurate encoding (position > length > area > color)?
Zero baseline - Do bar charts start at zero?
Accessibility - Works for colorblind viewers (~8% of males)?
Data-ink ratio - Can any non-data elements be removed?
Aspect ratio - Are line charts banked so slopes are ~45°?
Encoding Decision Order

When mapping data fields to visual channels:

Most important quantitative → Position (x or y)
Second quantitative → Position (other axis) or Length
Categories (≤7) → Color hue
Categories (>7) → Position or small multiples
Magnitude/importance → Size (but expect ~30% underestimation)
Chart Selection Logic
One variable, distribution → Histogram
One variable, categories → Bar chart
Two variables, both quantitative → Scatterplot
Two variables, time + quantitative → Line chart
Two variables, both categorical → Heatmap
Hierarchy → Treemap or node-link tree
Network (sparse) → Force-directed layout
Network (dense) → Matrix diagram
Animation Decision
Presentation context → Use animation (faster, engaging)
Analysis context → Use small multiples (more accurate)
State transitions → Animate to maintain object constancy
Duration: 200-300ms quick feedback, 500-700ms standard, 1000ms+ complex
Weekly Installs
9
Repository
sundial-org/skills
GitHub Stars
149
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass