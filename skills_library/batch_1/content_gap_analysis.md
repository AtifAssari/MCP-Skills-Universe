---
title: content-gap-analysis
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/content-gap-analysis
---

# content-gap-analysis

skills/aaron-he-zhu/seo-geo-claude-skills/content-gap-analysis
content-gap-analysis
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill content-gap-analysis
Summary

Identify missing topics and keywords your competitors rank for that you don't.

Analyzes keyword gaps, topic coverage, content format distribution, and audience journey stage alignment between your site and 2-5 competitors
Surfaces high-priority quick wins (low difficulty, achievable volume) and long-term strategic opportunities with priority scoring based on business relevance and effort
Detects GEO opportunities where competitors receive AI citations for topics you're missing, plus identifies underserved Q&A, definition, and comparison content
Generates prioritized content calendar with Tier 1 quick wins, Tier 2 strategic builds, and Tier 3 long-term initiatives mapped to realistic timeframes
Works with manual data input (site URLs, competitor URLs, traffic metrics) or integrates with SEO tools, Search Console, and analytics via MCP connectors when available
SKILL.md
Content Gap Analysis

Identifies content opportunities by comparing your site against competitors and scoring the gaps worth closing first.

Quick Start
Find content gaps between my site [URL] and [competitor URLs]

What content am I missing compared to my top 3 competitors?

Skill Contract

Expected output: a prioritized gap brief plus the standard handoff summary for memory/research/.

Reads: goals, market inputs, tool data, and prior strategy from CLAUDE.md and the shared State Model when available.
Writes: a user-facing analysis and reusable summary.
Promotes: durable keyword priorities, competitor facts, and strategy decisions to memory/hot-cache.md, memory/decisions.md, and memory/research/.
Primary next skill: seo-content-writer when the prioritized gap list is approved.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

Optional integrations: ~~SEO tool, ~~search console, ~~analytics, ~~AI monitor. Without tools, ask for site URL, content inventory, competitor URLs, and business goals. See CONNECTORS.md.

Instructions

When a user requests content gap analysis:

Define Analysis Scope — confirm your site, competitors, topic focus, content types, audience, and business goals.
Audit Your Existing Content — map indexed pages, content types, topic clusters, winners, and weaknesses.
Analyze Competitor Content — compare content volume, traffic, type mix, topic coverage, and unique assets.
Identify Keyword Gaps — group gaps into High Priority, Quick Wins, and Long-term based on volume, difficulty, and relevance.
Map Topic Gaps — compare topic-cluster coverage and recommend pillar / cluster approaches for missing themes.
Identify Content Format Gaps — compare guides, tutorials, comparisons, case studies, tools, templates, video, and research.
Analyze GEO / AI Gaps — identify missing Q&A, definition, and comparison content that competitors get cited for.
Map to Audience Journey — compare Awareness, Consideration, Decision, and Retention coverage.
Prioritize and Create Action Plan — deliver an Executive Summary, Prioritized Gap List (Quick Wins / Strategic Builds / Long-term), Content Calendar, and Success Metrics.

Reference: See references/analysis-templates.md for the compact templates used in each step.

Example

See references/example-report.md for a full SaaS marketing sample.

Advanced Analysis
Competitive Cluster Comparison
Compare our topic cluster coverage for [topic] vs top 5 competitors

Temporal Gap Analysis
What content have competitors published in the last 6 months that we haven't covered?

Intent-Based Gaps
Find gaps in our [commercial/informational] intent content

Tips for Success

Focus on actionable gaps, respect execution constraints, and include GEO opportunities instead of only traditional search gaps.

Save Results

After delivering, offer to save memory/research/content-gap-analysis/YYYY-MM-DD-<topic>.md and promote durable conclusions to memory/hot-cache.md.

Reference Materials
Analysis Templates — Gap-analysis templates
Gap Analysis Frameworks — Audit and prioritization frameworks
Example Report — Worked sample
Next Best Skill

Primary: seo-content-writer.

Weekly Installs
3.1K
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