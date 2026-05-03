---
rating: ⭐⭐
title: dt-app-dashboards
url: https://skills.sh/dynatrace/dynatrace-for-ai/dt-app-dashboards
---

# dt-app-dashboards

skills/dynatrace/dynatrace-for-ai/dt-app-dashboards
dt-app-dashboards
Installation
$ npx skills add https://github.com/dynatrace/dynatrace-for-ai --skill dt-app-dashboards
SKILL.md
Dynatrace Dashboard Skill
Overview

Dynatrace dashboards are JSON documents stored in the Document Store. Each dashboard contains:

Tiles: Visual components displaying markdown content or data visualizations
Layouts: Grid-based positioning (20-unit width) defining tile placement
Variables: Dynamic parameters ($VariableName) for query filtering
Configuration: Version metadata and dashboard-level settings

When to use this skill:

Creating new dashboards with skill-based query generation
Modifying existing dashboards (queries, tiles, layouts)
Querying dashboard JSON to extract data or analyze structure
Analyzing dashboard purpose, metrics coverage, and health

Four main workflows:

Creating - Build dashboards with skill-based queries
Modifying - Update tiles, queries, layouts, variables
Querying - Extract data from dashboard JSON
Analyzing - Understand structure, purpose, gaps, and health
Dashboard Document Structure

Dashboards in the Dynatrace Document Store include both metadata and content:

{
  "id": "dashboard-abc123",
  "name": "My Dashboard",  
  "type": "dashboard",
  "owner": "user-uuid",
  "version": 60,
  "modificationInfo": {...},
  "content": {
    "version": 21,
    "variables": [],
    "tiles": {...},
    "layouts": {...}
  }
}


Metadata (top-level):

.id - Document ID
.name - Dashboard name
.owner - Owner UUID
.version - Document version (change tracking)
.modificationInfo - Creation/modification timestamps

Dashboard content (.content):

.content.version - Dashboard schema version (current: 21)
.content.tiles - Tile definitions
.content.layouts - Tile positioning
.content.variables - Dashboard variables

All jq examples in this skill use the .content.* paths.

When to Load References

This skill uses progressive disclosure - load only what you need:

Start here: SKILL.md provides core concepts and quick-start examples
Load references on-demand: Each reference file covers a specific deep-dive topic
Context efficiency: Progressive loading enables task completion without external documentation

Loading strategy:

Try answering with just SKILL.md first
If you need detailed specifications or advanced patterns, load the relevant reference file
The "References" section below maps each file to its use case

💡 Tip: Reference files are linked throughout this document with → arrows pointing to when you should load them.

Working with Dashboards

For detailed workflows and mandatory requirements:

Creating & Updating dashboards → Load references/create-update.md for complete workflow, skill-based query generation, validation, and modification patterns
Analyzing dashboards → Load references/analyzing.md for structure analysis, health assessment, and JSON extraction

⚠️ MANDATORY for creation/modification:

Follow this exact order (do not reorder):

Define purpose and load required skills, references and assets
Explore available data fields/metrics
Plan dashboard structure: logic, variables, tiles and layout
Design and validate all variable/tile DQL with dtctl query "<DQL>" --plain
Construct/update dashboard JSON
Validate the dashboard JSON structure and queries
Deploy the dashboard via the Dynatrace API

Full requirements and examples: references/create-update.md.

Dashboard Structure
Required Structure
{
  "name": "My Dashboard",
  "type": "dashboard",
  "content": {
    "version": 21,
    "tiles": {},
    "layouts": {}
  }
}


Optional properties inside content:

variables - Array of dashboard variables (filters/parameters)
settings - Dashboard-level settings (grid layout, default timeframe)
refreshRate - Dashboard refresh rate in milliseconds (e.g., 60000)
gridColumnsCount - Number of grid columns (default: 20)
annotations - Array of dashboard annotations

Structure concept: Variables define reusable parameters, tiles contain content/visualizations, layouts control positioning. Each tile ID in tiles must have a corresponding entry in layouts.

Tiles Overview

📊 For detailed tile specifications, visualization settings, and query configuration, load references/tiles.md

Markdown tiles: {"type": "markdown", "content": "# Title"} Data tiles: {"type": "data", "title": "...", "query": "...", "visualization": "..."}

Visualizations:

Time-series (MUST have time dimension via timeseries/makeTimeseries): lineChart, areaChart, barChart, bandChart
Categorical (no time dimension, summarize ... by:{field}): categoricalBarChart, pieChart, donutChart
Single value / gauge (single numeric record): singleValue, meterBar, gauge
Tabular / raw (any data shape): table, raw, recordList
Distribution / status: histogram, honeycomb
Geographic maps: choroplethMap, dotMap, connectionMap, bubbleMap
Matrix / correlation: heatmap, scatterplot

→ See references/tiles.md for specifications

Layouts Overview

📐 For complex layout patterns, grid system details, and positioning examples, load references/layouts.md

Grid: 20 units wide. Common widths: Full (20), Half (10), Third (6-7), Quarter (5) Properties: x (0-19), y (0+), w (1-20), h (1-20)

Example: {"1": {"x": 0, "y": 0, "w": 20, "h": 1}, "2": {"x": 0, "y": 1, "w": 10, "h": 8}}

→ See references/layouts.md for patterns

Variables Overview

🔧 For detailed variable configurations, replacement strategies, multi-select, and limitations, load references/variables.md

Definition: {"version": 2, "key": "ServiceFilter", "type": "query", "visible": true, "editable": true, "input": "smartscapeNodes SERVICE | fields name", "multiple": false, "defaultValue": "*"} Usage (single-select): fetch logs | filter service.name == $ServiceFilter Usage (multi-select): fetch logs | filter in(service.name, array($ServiceFilter))

→ See references/variables.md for complete property reference, replacement strategies (:noquote, :backtick), and usage patterns

Validation

⚠️ MANDATORY for create/update workflows: Validate the dashboard JSON before deploying. Check:

Schema structure — required top-level keys (name, type, content) and content keys (version, variables, tiles, layouts)
Variable resolution — all variable queries execute successfully
Tile query execution — all tile DQL queries run without errors
Best-practice checks — warnings for hardcoded time filters, CSV variables, etc.

→ Load references/create-update.md for full validation workflow.

References
Reference File	When to Use
create-update.md	Creating and updating dashboards - workflows, skill-based queries, validation, patterns
tiles.md	Tile types, visualization settings, query configuration, thresholds
layouts.md	Grid system details, layout patterns, positioning examples
variables.md	Variable types, multi-select, default values, query integration
analyzing.md	Structure analysis, purpose identification, health assessment, JSON extraction
Common Patterns & Best Practices

Patterns: Executive (header + KPIs + trends) · Service Health (RED metrics) · Infrastructure (resource metrics + tables)

Key rules: Match tile IDs in tiles and layouts · Use descriptive variable IDs · Start with full-width headers (y=0) · Optimize queries with limit/summarize · Set version=21 · No time-range filters in queries unless explicitly requested by the user

Weekly Installs
293
Repository
dynatrace/dynat…e-for-ai
GitHub Stars
59
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass