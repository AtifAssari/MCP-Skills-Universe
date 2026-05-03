---
title: keyword-research
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/keyword-research
---

# keyword-research

skills/aaron-he-zhu/seo-geo-claude-skills/keyword-research
keyword-research
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill keyword-research
Summary

Discovers high-value keywords with intent classification, difficulty scoring, and topic clustering for SEO content strategy.

Classifies keywords by search intent (informational, commercial, transactional, navigational) and assigns opportunity scores based on volume, difficulty, and business value
Integrates with Ahrefs, SEMrush, Google Keyword Planner, and Google Search Console; also accepts manual data input for sites without tool access
Groups keywords into topic clusters with pillar page and cluster page assignments, plus priority-scored content calendars
Identifies long-tail variations, GEO-relevant keywords likely to trigger AI responses, and quick-win opportunities for new or established sites
SKILL.md
Keyword Research

Discovers, scores, and clusters keywords for SEO and GEO planning.

Quick Start
Research keywords for [topic/product/service]

What keywords is [competitor URL] ranking for that I should target?

Skill Contract

Expected output: a prioritized keyword brief plus the standard handoff summary for memory/research/.

Reads: goals, market inputs, tool data, and prior strategy from CLAUDE.md and the shared State Model when available.
Writes: a user-facing research deliverable and reusable summary.
Promotes: durable keyword priorities, competitor facts, and strategy decisions to memory/hot-cache.md, memory/decisions.md, and memory/research/.
Primary next skill: competitor-analysis when the keyword set is ready for market comparison.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

Optional integrations: ~~SEO tool, ~~search console. Without tools, ask for seed keywords, audience, goals, and any known metrics. See CONNECTORS.md.

Instructions

When a user requests keyword research, run eight phases and announce each as [Phase X/8: Name]:

Scope — clarify product, audience, business goal, DR, geography, and language.
Discover — seed from core, problem, solution, audience, and industry terms.
Variations — expand with modifiers and long-tail patterns.
Classify — tag by intent (informational, navigational, commercial, transactional).
Score — assign difficulty (1-100) and compute Opportunity = (Volume × Intent Value) / Difficulty, with Intent Value 1 / 1 / 2 / 3.
GEO-Check — flag AI-answer-friendly queries such as questions, definitions, comparisons, lists, and how-tos.
Cluster — group keywords into pillar + cluster topic hubs.
Deliver — output an Executive Summary, Quick Wins / Growth / GEO opportunities, Topic Clusters, Content Calendar, and Next Steps.

Quality bar: every recommendation includes at least one specific number. Rewrite generic advice into a concrete keyword + volume + difficulty + reason.

Reference: See references/instructions-detail.md for the full 8-phase templates, expansion patterns, intent table, difficulty tiers, opportunity matrix, GEO indicators, cluster template, actionable-vs-generic examples, and advanced usage.

Example

Example outcome: 150+ keywords analyzed, 23 high-priority opportunities, ~45K/month traffic potential across 3 focus areas. See the full sample in references/example-report.md.

Advanced Usage

Intent mapping, seasonal analysis, competitor gaps, and local keyword workflows live in references/instructions-detail.md.

Tips for Success

Start with seeds, respect intent, cluster tightly, prioritize quick wins, and review quarterly. Full notes live in references/instructions-detail.md.

Save Results

After delivering, offer to save memory/research/keyword-research/YYYY-MM-DD-<topic>.md and promote durable conclusions to memory/hot-cache.md.

Reference Materials
Instructions Detail — Workflow, scoring, cluster template, advanced usage
Keyword Intent Taxonomy — Intent signals and content mapping
Topic Cluster Templates — Pillar and cluster patterns
Keyword Prioritization Framework — Scoring and prioritization rules
Example Report — Worked sample
Next Best Skill

Primary: competitor-analysis. Also: content-gap-analysis and serp-analysis.

Weekly Installs
4.1K
Repository
aaron-he-zhu/se…e-skills
GitHub Stars
1.4K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn