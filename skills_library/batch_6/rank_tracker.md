---
title: rank-tracker
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/rank-tracker
---

# rank-tracker

skills/aaron-he-zhu/seo-geo-claude-skills/rank-tracker
rank-tracker
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill rank-tracker
Summary

Track keyword rankings over time with trend analysis, movement detection, and competitive benchmarking.

Records and monitors keyword positions across traditional SERPs and AI-generated responses, with historical trend analysis and significant movement alerts
Tracks SERP features (featured snippets, PAA, image/video packs) and AI Overview citation rates for comprehensive search visibility
Compares rankings against competitors with share-of-voice metrics and head-to-head keyword analysis
Generates detailed ranking reports with position distribution, wins/declines, recovery recommendations, and GEO/AI performance insights
Requires keyword list with search volumes, target domain, location, and competitor domains; integrates with SEO tools via optional MCP network access
SKILL.md
Rank Tracker

Tracks keyword positions, SERP feature ownership, and AI visibility over time.

Quick Start
Set up rank tracking for [domain] targeting these keywords: [keyword list]

Analyze ranking changes for [domain] over the past [time period]

Skill Contract

Expected output: a ranking report or delta summary plus the standard handoff summary for memory/monitoring/.

Reads: current metrics, baselines, alert thresholds, and reporting context from CLAUDE.md and the shared State Model when available.
Writes: a user-facing monitoring deliverable and reusable summary.
Promotes: significant changes, confirmed anomalies, and follow-up actions to memory/open-loops.md and memory/decisions.md.
Primary next skill: alert-manager when recurring monitoring should become automated.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

All integrations optional (see CONNECTORS.md). With tools, pull rankings from ~~SEO tool, impressions from ~~search console, traffic from ~~analytics, and AI citations from ~~AI monitor. Without tools, ask for positions, volumes, competitor data, and SERP feature status.

Instructions

When a user requests rank tracking or analysis:

Set Up Keyword Tracking — configure domain, market, device, language, update frequency, priorities, and competitor watchlist.
Record Current Rankings — summarize position ranges, detailed rankings, ranking URLs, feature ownership, and movement.
Analyze Ranking Changes — highlight biggest wins, declines, stable terms, new rankings, lost rankings, likely causes, and recovery ideas.
Track SERP Features — compare ownership of snippets, PAA, image/video packs, local packs, and related feature shifts.
Track GEO / AI Visibility — monitor AI Overview presence, citation rate, citation position, and trend.
Compare Against Competitors — report share of voice, head-to-head comparisons, and threat levels.
Generate Ranking Report — summarize overall trend, key wins, concerns, opportunities, SERP feature changes, GEO visibility, and recommendations.

Reference: See references/ranking-analysis-templates.md for the complete output templates for all seven steps.

Example

Sample outcome: average position improves from 15.3 to 12.8, top-10 keywords rise from 12 to 17, and the report highlights the biggest winners, biggest drops, and next actions.

Tips for Success

Track consistently, segment by intent, watch competitors, and include SERP feature plus GEO signals.

Rank Change Quick Reference
Response Protocol
Change	Timeframe	Action
Drop 1-3 positions	Wait 1-2 weeks	Monitor — may be normal fluctuation
Drop 3-5 positions	Investigate within 1 week	Check technical issues and competitor changes
Drop 5-10 positions	Investigate immediately	Run a full diagnostic: technical, content, links
Drop off page 1	Emergency response	Comprehensive audit + recovery plan
Position gained	Document and learn	Identify what worked and replicate

Reference: See references/tracking-setup-guide.md for tracking setup, root-cause taxonomy, CTR benchmarks, SERP feature impact, and algorithm-update assessment.

Save Results

Ask "Save these results?" If yes, write memory/monitoring/YYYY-MM-DD-<topic>.md with headline finding, actions, and open loops.

Reference Materials
Tracking Setup Guide — Setup rules, feature tracking, and interpretation guidance
Next Best Skill

Initial setup (no baseline) → alert-manager. Subsequent runs (baseline exists) → Terminal. Visited-set rule applies per skill-contract.md.

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
SnykPass