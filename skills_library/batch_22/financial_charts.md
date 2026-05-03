---
title: financial-charts
url: https://skills.sh/pedro-mello30/stock-analyst/financial-charts
---

# financial-charts

skills/pedro-mello30/stock-analyst/financial-charts
financial-charts
Installation
$ npx skills add https://github.com/pedro-mello30/stock-analyst --skill financial-charts
SKILL.md
Financial Charts

Create publication-quality financial visualizations: Sankey flows, waterfalls, bar charts, and line charts.

Quick Reference
Need	Function	Script
Income statement flow	create_income_statement_sankey()	sankey_chart.py
Profit walkdown	create_profit_walkdown()	waterfall_chart.py
Revenue bridge	create_revenue_bridge()	waterfall_chart.py
Margin comparison	create_margin_comparison_chart()	bar_chart.py
Revenue segments	create_revenue_segment_chart()	bar_chart.py
Trend analysis	create_trend_chart()	line_chart.py
Multi-line comparison	create_multi_line_chart()	line_chart.py
Workflow
Identify chart type from Quick Reference
Prepare data in required format
Select theme (default, corporate, dark, apple, tech, financial, minimal)
Run script with parameters
Output as .png, .html, or .pdf
Example: Income Statement Sankey

Creates a flow diagram like Apple's FY22 visualization (see assets/chart-example.png):

from scripts.sankey_chart import create_income_statement_sankey

create_income_statement_sankey(
    revenue_sources={
        "iPhone": 205.5e9,
        "Mac": 40.2e9,
        "iPad": 29.3e9,
        "Wearables": 41.2e9,
        "Services": 78.1e9,
    },
    cost_of_revenue=223.6e9,
    operating_expenses={"R&D": 26.2e9, "SG&A": 25.1e9},
    other_expenses={"Tax": 19.3e9, "Other": 0.3e9},
    company_name="Apple",
    fiscal_period="FY22",
    theme="apple",
    output_path="apple_income_flow.png",
)

Example: Waterfall Chart
from scripts.waterfall_chart import create_profit_walkdown

create_profit_walkdown(
    revenue=100e6,
    cost_of_goods_sold=60e6,
    operating_expenses={"R&D": 10e6, "SG&A": 15e6},
    other_items={"Tax": -3e6},
    title="Q4 Profit Walkdown",
    output_path="walkdown.png",
)

Themes

All scripts accept theme parameter:

default - Professional blue/green
corporate - Traditional business
dark - Dark mode dashboards
apple - Apple-style clean
tech - Modern tech
financial - Banking style
minimal - Grayscale with accents
Dependencies
pip install plotly kaleido

Extended Reference

For detailed API, all parameters, and advanced customization, see references/chart-guide.md.

Weekly Installs
10
Repository
pedro-mello30/s…-analyst
GitHub Stars
1
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass