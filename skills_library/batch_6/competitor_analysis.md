---
title: competitor-analysis
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/competitor-analysis
---

# competitor-analysis

skills/aaron-he-zhu/seo-geo-claude-skills/competitor-analysis
competitor-analysis
Originally fromlangchain-ai/deepagents
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill competitor-analysis
Summary

Comprehensive competitor SEO and GEO analysis revealing ranking strategies, content approaches, and market opportunities.

Analyzes keyword rankings, content strategies, backlink profiles, and technical SEO across 2-5 competitors to identify performance gaps and actionable insights
Includes GEO/AI citation analysis showing how competitors appear in AI responses and where citation opportunities exist
Supports both automated data collection via SEO tool integrations (Ahrefs API) and manual data input for flexibility
Produces structured reports with competitive landscape comparisons, strength/weakness assessments, keyword opportunities, and prioritized action plans (immediate, short-term, long-term)
SKILL.md
Competitor Analysis

Analyzes competitor SEO and GEO strategies to reveal repeatable wins, weak spots, and market gaps.

Quick Start
Analyze SEO strategy for [competitor URL]

Compare my site [URL] against [competitor 1], [competitor 2], [competitor 3]

Skill Contract

Expected output: a prioritized competitor brief plus the standard handoff summary for memory/research/.

Reads: goals, market inputs, tool data, and prior strategy from CLAUDE.md and the shared State Model when available.
Writes: a user-facing analysis and reusable summary.
Promotes: durable competitor facts, keyword priorities, entity candidates, and strategy decisions to memory/hot-cache.md, memory/decisions.md, and memory/research/.
Primary next skill: content-gap-analysis when the competitive landscape is clear.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

Optional integrations: ~~SEO tool, ~~analytics, ~~AI monitor. Without tools, ask for competitor URLs, your site metrics, and industry context. See CONNECTORS.md.

Instructions

When a user requests competitor analysis:

Identify Competitors — separate direct competitors, indirect alternatives, and content competitors if the user has not named them already.
Gather Competitor Data — capture URL, domain age, estimated traffic, domain authority, business model, target audience, and key offerings.
Analyze Keyword Rankings — document total rankings, top 10/top 3 counts, high-value keywords, intent mix, and keyword gaps.
Audit Content Strategy — review content volume, top performers, publishing patterns, themes, and success factors.
Analyze Backlink Profile — review backlink totals, quality mix, top linking domains, link acquisition patterns, and linkable assets.
Technical SEO Assessment — evaluate Core Web Vitals, mobile-friendliness, architecture, internal linking, URL structure, and standout strengths/weaknesses.
GEO / AI Citation Analysis — test which queries cite competitors, what formats get cited, and where competitors still leave openings.
Synthesize Competitive Intelligence — deliver an Executive Summary, comparison table, CITE comparison, strengths to learn from, weaknesses to exploit, keyword opportunities, content recommendations, and an Immediate / Short-term / Long-term plan.

Reference: See references/analysis-templates.md for the compact templates used at each step.

Example

See references/example-report.md for a full sample analyzing HubSpot's marketing keyword dominance.

Advanced Analysis Types
Content Gap Analysis
Show me content [competitor] has that I don't, sorted by traffic potential

Link Intersection
Find sites linking to [competitor 1] AND [competitor 2] but not me

SERP Feature Analysis
What SERP features do competitors win? (Featured snippets, PAA, etc.)

Historical Tracking
How has [competitor]'s SEO strategy evolved over the past year?

Tips for Success

Analyze 3-5 competitors, include indirect players, and study both strengths and failures.

Save Results

After delivering, offer to save memory/research/competitor-analysis/YYYY-MM-DD-<topic>.md and promote durable conclusions to memory/hot-cache.md.

Reference Materials
Analysis Templates — Step-by-step analysis templates
Battlecard Template — Quick-reference battlecard format
Positioning Frameworks — Positioning and differentiation frameworks
Example Report — Worked sample
Next Best Skill

Primary: content-gap-analysis. Also: serp-analysis and backlink-analyzer.

Weekly Installs
3.6K
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