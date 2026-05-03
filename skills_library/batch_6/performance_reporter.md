---
title: performance-reporter
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/performance-reporter
---

# performance-reporter

skills/aaron-he-zhu/seo-geo-claude-skills/performance-reporter
performance-reporter
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill performance-reporter
Summary

Comprehensive SEO and GEO performance reports combining rankings, traffic, backlinks, and AI visibility metrics.

Aggregates data from multiple sources (analytics, search console, SEO tools, AI monitors) into executive summaries, detailed analyses, and visual presentations
Generates 11-section reports covering organic traffic, keyword rankings, domain authority, content quality (CORE-EEAT), backlinks, and GEO/AI citation performance
Includes period-over-period trend analysis, benchmark comparisons against goals, and ROI calculations for stakeholder communication
Supports manual data input when automated connectors unavailable; customizable for executive, technical, and client audiences with actionable recommendations prioritized by impact
SKILL.md
Performance Reporter

Aggregates SEO/GEO data, builds stakeholder reports, benchmarks goals/competitors, calculates ROI, and turns deltas into prioritized recommendations.

Quick Start
Create an SEO performance report for [domain] for [time period]
Generate an executive summary of SEO performance for [month/quarter]
Create a GEO visibility report for [domain]
Generate a content performance report

Skill Contract

Expected output: a delta summary, alert/report output, and a short handoff summary ready for memory/monitoring/.

Reads: current metrics, previous baselines, alert thresholds, and reporting context from CLAUDE.md and the shared State Model when available.
Writes: a user-facing monitoring deliverable plus a reusable summary that can be stored under memory/monitoring/.
Promotes: significant changes, confirmed anomalies, and follow-up actions to memory/open-loops.md and memory/decisions.md.
Next handoff: use the Next Best Skill below when a change needs action.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

All integrations optional (see CONNECTORS.md). With tools connected, aggregates traffic from ~~analytics, search data from ~~search console, rankings/backlinks from ~~SEO tool, and AI visibility from ~~AI monitor. Without tools, ask user for analytics exports, Search Console data, ranking data, and KPIs.

Instructions

When a user requests a performance report, use references/report-output-templates.md and cover:

Define Report Parameters -- Domain, period, comparison period, report type, audience, focus areas, and data freshness.
Create Executive Summary -- Overall rating, wins, watch areas, required actions, metrics at a glance (traffic, rankings, conversions, DA/authority, AI citations), and SEO ROI.
Report Organic Traffic -- Sessions, users, pageviews, engagement/bounce, trend visualization, source/device split, top pages.
Report Keyword Rankings -- Position ranges, distribution change, top improvements/declines, SERP features.
Report GEO/AI Performance -- AI citation overview, citations by topic, GEO wins, and optimization opportunities.
Report Domain Authority (CITE) -- Include CITE dimension scores and veto status when available; otherwise mark "Not yet evaluated."
Report Content Quality (CORE-EEAT) -- Include average scores and trends when available; otherwise mark "Not yet evaluated."
Report Backlinks -- Link profile summary, acquisition trend, notable links, competitive position.
Report Content Performance -- Publishing summary, top content, content needing attention, and content ROI.
Generate Recommendations -- Immediate, short-term, and long-term actions with priority, owner, expected impact, and next-period goals.
Compile Full Report -- Add table of contents, appendix, data sources, methodology, and glossary.
Example

Sample output: an executive summary with overall status, metrics-at-a-glance for traffic/rankings/conversions/authority/AI citations, SEO ROI, and immediate/month/quarter actions with owners and dates.

Tips for Success

Lead with insights, compare periods, state data freshness, include owner/deadline/impact for actions, tailor depth to audience, and track GEO/AI citation metrics when in scope.

Save Results

Ask "Save these results?" If yes, write memory/monitoring/YYYY-MM-DD-<topic>.md with the headline finding, actionable items, and open loops.

Reference Materials
Report Output Templates -- Compact starter blocks for all 11 report sections
KPI Definitions -- SEO/GEO metric definitions with benchmarks, thresholds, trend analysis, and attribution guidance
Report Templates by Audience -- Copy-ready templates for executive, marketing, technical, and client audiences
Next Best Skill

Primary: alert-manager -- turn reporting insights into ongoing monitoring rules.

Weekly Installs
2.9K
Repository
aaron-he-zhu/se…e-skills
GitHub Stars
1.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn