---
rating: ⭐⭐
title: backlink-analyzer
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/backlink-analyzer
---

# backlink-analyzer

skills/aaron-he-zhu/seo-geo-claude-skills/backlink-analyzer
backlink-analyzer
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill backlink-analyzer
Summary

Comprehensive backlink profile analysis with toxic link detection, opportunity discovery, and competitor benchmarking.

Analyzes link authority, quality metrics (DA/DR), anchor text distribution, and link velocity to assess profile health
Identifies toxic and spammy links with risk scoring and generates disavow recommendations
Discovers link building opportunities through competitor intersection analysis, broken links, and unlinked mentions
Tracks new and lost links over time, compares profiles across competitors, and integrates backlink data into domain authority scoring
Requires backlink data (CSV exports or manual input) and optional SEO tool API access for automated profile collection
SKILL.md
Backlink Analyzer

Analyzes backlink profiles for quality, risk, competitive gaps, and link-building opportunities.

Quick Start
Analyze backlink profile for [domain]

Find link building opportunities by analyzing [competitor domains]

Skill Contract

Expected output: a backlink report or delta summary plus the standard handoff summary for memory/monitoring/.

Reads: current metrics, baselines, alert thresholds, and reporting context from CLAUDE.md and the shared State Model when available.
Writes: a user-facing monitoring deliverable and reusable summary.
Promotes: significant changes, confirmed anomalies, and follow-up actions to memory/open-loops.md and memory/decisions.md.
Primary next skill: domain-authority-auditor when toxicity or authority concerns need formal scoring.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

All integrations optional (see CONNECTORS.md). With tools, pull backlink profiles from ~~link database and competitor data from ~~SEO tool. Without tools, ask for backlink CSVs, referring domains, competitor domains, and link changes. Respect robots.txt and TOS per SECURITY.md.

Instructions

When a user requests backlink analysis:

Generate Profile Overview — key metrics, link velocity, authority distribution, and profile health score.
Analyze Link Quality — top backlinks, link type mix, anchor text distribution, and geography.
Identify Toxic Links — risk indicators, links to review, and disavow recommendations.
Compare Against Competitors — profile comparison, link intersection, and top linked competitor content.
Find Link Building Opportunities — intersection prospects, broken links, unlinked mentions, resource pages, guest posts, and effort-vs-impact priorities.
Track Link Changes — new and lost links, net change, and recovery priorities.
Generate Backlink Report — executive summary, strengths, concerns, opportunities, competitive position, recommended actions, and KPIs.

Reference: See references/analysis-templates.md for the compact output templates used in all seven steps.

CITE Item Mapping

When running domain-authority-auditor after this analysis, the following data feeds directly into CITE scoring:

Backlink Metric	CITE Item	Dimension
Referring domains count	C01 (Referring Domain Volume)	Citation
Authority distribution (DA breakdown)	C02 (Referring Domains Quality)	Citation
Link velocity	C04 (Link Velocity)	Citation
Geographic distribution	C10 (Link Source Diversity)	Citation
Dofollow/Nofollow ratio	T02 (Dofollow Ratio Normality)	Trust
Toxic link analysis	T01 (Link Profile Naturalness), T03 (Link-Traffic Coherence)	Trust
Competitive link intersection	T05 (Profile Uniqueness)	Trust
Example

Sample outcome: a link-intersection table, top immediate opportunities, and an estimated impact model. Keep the full structure in references/analysis-templates.md.

Tips for Success

Prioritize quality, monitor regularly, diversify anchors and link types, and disavow cautiously.

Link Quality and Strategy Reference

Reference: See references/link-quality-rubric.md for the scoring matrix, toxic-link criteria, benchmarks, and disavow guidance.

Reference: See references/outreach-templates.md for outreach frameworks, subject lines, response benchmarks, follow-up sequences, and templates.

Save Results

Ask "Save these results?" If yes, write memory/monitoring/YYYY-MM-DD-<topic>.md with headline finding, actions, and open loops. If toxic ratio exceeds 15%, recommend domain-authority-auditor.

Reference Materials
Link Quality Rubric — Quality and toxicity rubric
Outreach Templates — Outreach frameworks and examples
Next Best Skill

Toxic ratio > 15% → domain-authority-auditor. Otherwise → Terminal. Visited-set rule applies per skill-contract.md.

Weekly Installs
18.0K
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