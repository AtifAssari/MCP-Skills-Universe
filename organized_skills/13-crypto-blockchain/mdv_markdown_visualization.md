---
rating: ⭐⭐⭐⭐⭐
title: mdv-markdown-visualization
url: https://skills.sh/aradotso/trending-skills/mdv-markdown-visualization
---

# mdv-markdown-visualization

skills/aradotso/trending-skills/mdv-markdown-visualization
mdv-markdown-visualization
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill mdv-markdown-visualization
SKILL.md
MDV Markdown Data & Visualization

Skill by ara.so — Daily 2026 Skills collection.

MDV is a Markdown superset (.mdv files) for writing reports, dashboards, and slide decks in a single workflow, then exporting to self-contained HTML or PDF. It extends CommonMark with four additions: YAML front-matter, fenced visualization blocks, ::: containers for layout, and auto-generated tables of contents.

Installation & Setup
git clone https://github.com/drasimwagan/mdv mdv
cd mdv
npm install
npm run build

# Render a file to HTML
node packages/mdv-cli/dist/index.js render examples/09-full-report.mdv

# Live preview with auto-reload
node packages/mdv-cli/dist/index.js preview examples/09-full-report.mdv

# Export to PDF
node packages/mdv-cli/dist/index.js export --pdf examples/09-full-report.mdv

CLI Commands
# Render .mdv → self-contained HTML
node packages/mdv-cli/dist/index.js render <file.mdv>
node packages/mdv-cli/dist/index.js render <file.mdv> --out output.html

# Live preview (opens browser, auto-reloads on save)
node packages/mdv-cli/dist/index.js preview <file.mdv>

# PDF export
node packages/mdv-cli/dist/index.js export --pdf <file.mdv>
node packages/mdv-cli/dist/index.js export --pdf <file.mdv> --out report.pdf

File Structure
.mdv project/
├── data/
│   ├── sales.csv
│   └── metrics.json
├── report.mdv
└── dashboard.mdv

Document Anatomy

Every .mdv file has three zones:

YAML front-matter — metadata, theme, named styles, dataset refs
Markdown body — standard CommonMark prose
Fenced blocks & containers — charts, stats, callouts, columns
YAML Front-Matter
---
title: Q1 Sales Report
author: Jane Smith
theme: report          # report | dashboard | slides | minimal
data:
  sales: ./data/sales.csv
  users: ./data/users.json
styles:
  highlight:
    background: "#fff3cd"
    border-left: "4px solid #ffc107"
  danger:
    background: "#fde8e8"
    border-left: "4px solid #e53e3e"
---

Available Themes
Theme	Best for
report	Long-form documents, articles
dashboard	KPI cards, dense data layouts
slides	Presentations, slide decks
minimal	Clean, unstyled output
Fenced Visualization Blocks
Stat / KPI Cards
```stat
label, value, delta
Total revenue, $2.06M, +14%
New customers, 1,238, +8%
Churn rate, 2.1%, -0.3%
Active accounts, 9,842, +5%


The `stat` block renders a row of KPI cards. Columns: `label`, `value`, `delta` (optional).

### Charts

All charts use `` ```chart `` with attributes on the opening fence line:

```markdown
```chart type=bar x=region y=sales title="Sales by Region"


**Chart attributes:**

| Attribute   | Values / Notes                                      |
|-------------|-----------------------------------------------------|
| `type`      | `bar`, `line`, `area`, `pie`, `donut`, `scatter`   |
| `data`      | Named dataset from front-matter (e.g. `data=sales`)|
| `x`         | Column name for x-axis                              |
| `y`         | Column name for y-axis                              |
| `series`    | Column name to split into multiple series           |
| `title`     | Chart title string                                  |
| `yFormat`   | `currency`, `percent`, `number`                     |
| `color`     | Hex or CSS color for single-series charts           |
| `width`     | `full`, `half`, `third` (layout hint)               |
| `height`    | Pixel height as number                              |

**Chart examples:**

```markdown
# Bar chart from referenced dataset
```chart type=bar data=sales x=region y=revenue title="Revenue by Region"

Line chart with multiple series
Pie chart
Scatter plot

### Inline Data in Chart Blocks

When no `data=` attribute is given, put CSV inline in the block body:

```markdown
```chart type=bar x=quarter y=revenue title="Quarterly Revenue"
quarter, revenue
Q1, 206000
Q2, 241000
Q3, 198000
Q4, 312000


### Tables

Standard CommonMark tables work as-is. For data-sourced tables:

```markdown
```table data=sales columns="region,revenue,growth" title="Regional Breakdown"


## `:::` Containers

Containers wrap content in styled or structural regions.

### Table of Contents

```markdown
::: toc
:::


Inserts an auto-generated TOC based on headings in the document.

Callout / Alert Boxes
::: callout
This is an important note rendered in a highlighted box.
:::

::: callout type=warning
Watch out — this may have side effects.
:::

::: callout type=danger
Do not run this in production.
:::


Callout types: info (default), warning, danger, success.

Column Layouts
::: columns
::: col
Left column content, charts, or stats here.
:::
::: col
Right column content.
:::
:::

Named Style Containers

Apply styles defined in front-matter:

::: highlight
This paragraph uses the `highlight` named style from front-matter.
:::

::: danger
Critical warning styled with the `danger` named style.
:::

Complete Document Examples
Report Document
---
title: Q1 2026 Report
theme: report
data:
  sales: ./data/sales.csv
---

::: toc
:::

# Executive Summary

::: callout type=success
Revenue grew 14% YoY, exceeding the $2M target.
:::

```stat
label, value, delta
Total Revenue, $2.06M, +14%
New Customers, 1,238, +8%
NPS Score, 67, +4

Revenue Breakdown

::: columns ::: col

::: ::: col

::: :::

Data Table

### Dashboard Document

```markdown
---
title: Operations Dashboard
theme: dashboard
data:
  ops: ./data/ops.csv
  alerts: ./data/alerts.json
---

# Live Metrics

```stat
label, value, delta
Uptime, 99.97%, +0.02%
Avg Latency, 42ms, -8ms
Error Rate, 0.03%, -0.01%
Active Users, 14,203, +312


::: columns ::: col

::: ::: col

::: :::


### Slide Deck

```markdown
---
title: Product Roadmap 2026
theme: slides
---

# Vision

Our goal: ship faster, break less.

---

# Q1 Achievements

```stat
label, value, delta
Features shipped, 24, +6
Bugs closed, 187, -12%
Deploy frequency, 3.2/day, +40%

Revenue Growth
quarter, arr
Q1, 1200000
Q2, 1450000
Q3, 1780000
Q4, 2060000


## Data Formats

### CSV (inline or file)

```csv
region, revenue, growth, deals
North, 680000, 0.18, 142
South, 410000, 0.09, 87
East, 520000, 0.22, 113
West, 450000, 0.11, 98

JSON (file reference)
[
  { "month": "Jan", "revenue": 180000, "region": "North" },
  { "month": "Feb", "revenue": 195000, "region": "North" },
  { "month": "Jan", "revenue": 120000, "region": "South" }
]


Reference in front-matter:

data:
  sales: ./data/sales.csv
  metrics: ./data/metrics.json

VS Code Extension

Install the VS Code extension for side-by-side live preview:

cd packages/mdv-vscode
npm install
npm run build
# Then install the generated .vsix via VS Code Extensions panel → "Install from VSIX"


Once installed:

Open any .mdv file
Press Ctrl+Shift+P → MDV: Open Preview
Preview updates on every save

See docs/vscode.md and docs/publishing-vscode-extension.md for marketplace publishing.

Project Package Structure
packages/
├── mdv-core/        # Parser, renderer, chart engine (TypeScript)
├── mdv-cli/         # CLI: render, preview, export commands
└── mdv-vscode/      # VS Code extension with live preview

Common Patterns
Pattern: Dashboard with KPIs + Charts
---
title: Sales Dashboard
theme: dashboard
data:
  pipeline: ./data/pipeline.csv
---

```stat
label, value, delta
Pipeline, $4.2M, +22%
Deals Open, 94, +11
Win Rate, 31%, +3%
Avg Deal Size, $44.7K, +8%


::: columns ::: col

::: ::: col

::: :::


### Pattern: Callout + Inline Data Chart

```markdown
::: callout type=warning
Revenue dipped in March due to seasonal effects.
:::

```chart type=area x=month y=revenue title="Revenue Trend"
month, revenue
Jan, 180000
Feb, 195000
Mar, 162000
Apr, 201000
May, 224000


### Pattern: Named Styles for Emphasis

```yaml
---
styles:
  metric-good:
    background: "#f0fff4"
    border-left: "4px solid #38a169"
  metric-bad:
    background: "#fff5f5"
    border-left: "4px solid #e53e3e"
---

::: metric-good
**Churn** dropped to 1.8% this quarter — lowest in 3 years.
:::

::: metric-bad
**Support tickets** up 23% — investigate root cause.
:::

Troubleshooting

Build fails: Run npm install from the repo root before npm run build. All packages must build together.

Charts render blank: Ensure data= references a dataset name defined in front-matter, and the CSV/JSON file path is correct relative to the .mdv file.

PDF export fails: PDF export typically requires a headless browser (Puppeteer/Chromium). Ensure dependencies are installed: npm install in packages/mdv-cli.

Preview not updating: The preview command watches for file saves. Ensure you're saving the .mdv file (not just a data file). If a data file changed, re-save the .mdv to trigger reload.

VS Code extension not showing preview: Confirm the extension built successfully (npm run build in packages/mdv-vscode) and was installed from the .vsix. Open a .mdv file specifically — the preview command only activates on .mdv files.

Inline CSV not parsing: Ensure column names have no leading/trailing spaces and that delimiter is a comma. The first non-empty line of an inline block is treated as the header row.

Theme not applying: Theme names are case-sensitive. Valid values: report, dashboard, slides, minimal.

Key Files for Contributors
packages/mdv-core/src/
├── parser.ts        # CommonMark + MDV extensions parser
├── renderer.ts      # HTML renderer
├── chart.ts         # SVG chart engine
├── data.ts          # CSV/JSON data loader
└── theme.ts         # Theme & named style resolution

packages/mdv-cli/src/
└── index.ts         # CLI entry: render | preview | export

packages/mdv-vscode/src/
└── extension.ts     # VS Code extension + preview panel

Weekly Installs
174
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
3 days ago
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn