---
rating: ⭐⭐⭐⭐
title: vega
url: https://skills.sh/markdown-viewer/skills/vega
---

# vega

skills/markdown-viewer/skills/vega
vega
Installation
$ npx skills add https://github.com/markdown-viewer/skills --skill vega
SKILL.md
Vega / Vega-Lite Visualizer

Quick Start: Structure data as array of objects → Choose mark type (bar/line/point/area/arc/rect) → Map encodings (x, y, color, size) to fields → Set data types (quantitative/nominal/ordinal/temporal) → Wrap in ```vega-lite or ```vega fence. Always include $schema, use valid JSON with double quotes, field names are case-sensitive. Use Vega-Lite for 90% of charts; Vega only for radar, word cloud, force-directed.

Critical Syntax Rules
Rule 1: Always Include Schema
"$schema": "https://vega.github.io/schema/vega-lite/v5.json"

Rule 2: Valid JSON Only
❌ {field: "x",}     → Trailing comma, unquoted key
✅ {"field": "x"}    → Proper JSON

Rule 3: Field Names Must Match Data
❌ "field": "Category"  when data has "category"
✅ "field": "category"  → Case-sensitive match

Rule 4: Type Must Be Valid
✅ quantitative | nominal | ordinal | temporal
❌ numeric | string | date

Common Pitfalls
Issue	Solution
Chart not rendering	Check JSON validity, verify $schema
Data not showing	Field names must match exactly
Wrong chart type	Match mark to data structure
Colors not visible	Check color scale contrast
Dual-axis issues	Add resolve: {scale: {y: "independent"}}
Output Format
```vega-lite
{...}
```


Or for full Vega:

```vega
{...}
```

Related Files

For advanced chart patterns and complex visualizations, refer to references below:

examples.md — Stacked bar, grouped bar, multi-series line, area, heatmap, radar (Vega), word cloud (Vega), and interactive chart examples
Weekly Installs
1.5K
Repository
markdown-viewer/skills
GitHub Stars
2.4K
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass