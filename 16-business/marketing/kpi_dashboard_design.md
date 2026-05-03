---
title: kpi-dashboard-design
url: https://skills.sh/secondsky/claude-skills/kpi-dashboard-design
---

# kpi-dashboard-design

skills/secondsky/claude-skills/kpi-dashboard-design
kpi-dashboard-design
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill kpi-dashboard-design
SKILL.md
KPI Dashboard Design

Design effective dashboards that communicate key metrics clearly.

KPI Selection Framework

Good KPIs are:

Relevant to business goals
Measurable and quantifiable
Influenced by the team
Updated frequently
Simple to understand
Common Business KPIs
Goal	KPIs
Revenue	MRR, ARR, Revenue Growth
Acquisition	CAC, New Users, Conversion Rate
Retention	Churn Rate, NPS, DAU/MAU
Efficiency	LTV:CAC, Burn Rate
Quality	Error Rate, Response Time
Dashboard Layout
┌─────────────────────────────────────────────────┐
│              Executive Summary                  │
│  [Revenue ▲12%]  [Users ▲8%]  [Churn ▼2%]      │
├─────────────────────┬───────────────────────────┤
│                     │                           │
│   Revenue Trend     │    User Acquisition      │
│   (Line Chart)      │    (Bar Chart)           │
│                     │                           │
├─────────────────────┼───────────────────────────┤
│                     │                           │
│   Retention Funnel  │    Top Products          │
│   (Funnel Chart)    │    (Table)               │
│                     │                           │
└─────────────────────┴───────────────────────────┘

Visual Design Principles
/* Traffic light colors for status */
.metric-good { color: #22c55e; }    /* Green */
.metric-warning { color: #f59e0b; } /* Amber */
.metric-bad { color: #ef4444; }     /* Red */

/* Visual hierarchy */
.metric-primary {
  font-size: 2.5rem;
  font-weight: 700;
}

.metric-secondary {
  font-size: 1.5rem;
  font-weight: 500;
}

Chart Selection
Data Type	Chart
Trend over time	Line chart
Comparison	Bar chart
Composition	Pie/Donut
Distribution	Histogram
Correlation	Scatter plot
Funnel stages	Funnel chart
Interactivity Features
Drill-down to detailed views
Date range selection
Filtering by segment
Export to CSV/PDF
Scheduled email reports
Best Practices
Limit to 5-7 KPIs per dashboard
Show trends, not just snapshots
Use consistent color coding
Include comparison periods (vs last month)
Update data in real-time or hourly
Review dashboard relevance quarterly
Common Mistakes
Too many metrics (information overload)
No clear visual hierarchy
Missing context (no comparisons)
Outdated or stale data
Metrics without ownership
Weekly Installs
211
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass