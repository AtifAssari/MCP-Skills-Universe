---
rating: ⭐⭐
title: alert-manager
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/alert-manager
---

# alert-manager

skills/aaron-he-zhu/seo-geo-claude-skills/alert-manager
alert-manager
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill alert-manager
Summary

Proactive monitoring and alert system for SEO and GEO metrics with threshold-based notifications.

Monitors rankings, traffic, technical issues, backlinks, competitor movements, and brand mentions across seven alert categories
Configures custom thresholds and priority levels (Critical, High, Medium, Low) with severity-based response plans
Supports multiple notification channels (Email, SMS, Slack) with recipient routing, suppression rules, and escalation paths
Includes alert fatigue prevention, threshold tuning guidance, and weekly review workflows to maintain alert system health
SKILL.md
Alert Manager

Sets up proactive monitoring alerts for ranking, traffic, technical, backlink, competitor, and GEO changes.

Quick Start
Set up SEO monitoring alerts for [domain]

Create ranking drop alerts for my top 20 keywords

Skill Contract

Expected output: an alert configuration summary plus the standard handoff summary for memory/monitoring/.

Reads: current metrics, baselines, alert thresholds, and reporting context from CLAUDE.md and the shared State Model when available.
Writes: a user-facing monitoring deliverable and reusable summary.
Promotes: significant anomalies, durable thresholds, and follow-up actions to memory/open-loops.md and memory/decisions.md.
Primary next skill: performance-reporter when alert output needs a reporting cadence.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

All integrations optional (see CONNECTORS.md). With tools, monitor real-time feeds from ~~SEO tool, ~~search console, and ~~web crawler. Without tools, ask for baselines, critical keywords, preferences, and historical data.

Instructions

When a user requests alert setup:

Define Alert Categories — choose from rankings, traffic, technical, backlinks, competitors, GEO / AI, and brand alerts.
Configure Alert Rules by Category — define trigger condition, threshold, alert name, and priority for each relevant rule.
Define Alert Response Plans — map Critical / High / Medium / Low to response time and next actions.
Set Up Alert Delivery — configure channels, routing, cooldowns, maintenance windows, and escalation paths.
Create Alert Summary — deliver category counts, critical playbook, and weekly review checklist.

Reference: See references/alert-configuration-templates.md for the full category tables, thresholds, and response-plan templates.

Example

Sample outcome: a keyword alert matrix with Critical vs High thresholds, a response plan for drops, and notification routing to email + Slack.

Tips for Success

Start simple, tune thresholds to normal volatility, avoid alert fatigue, and review the system regularly.

Alert Threshold Quick Reference
Metric	Warning	Critical	Frequency
Organic traffic	-15% WoW	-30% WoW	Daily
Keyword positions	>3 position drop	>5 position drop	Daily
Pages indexed	-5% change	-20% change	Weekly
Crawl errors	>10 new/day	>50 new/day	Daily
Core Web Vitals	"Needs Improvement"	"Poor"	Weekly
Backlinks lost	>5% in 1 week	>15% in 1 week	Weekly
AI citation loss	Any key query	>20% queries	Weekly
Security issues	Any detected	Any detected	Daily

Reference: See references/alert-threshold-guide.md for threshold setting, fatigue prevention, escalation paths, and response playbooks.

Save Results

Ask "Save these results?" If yes, write memory/monitoring/YYYY-MM-DD-<topic>.md with headline finding, actions, and open loops.

Reference Materials
Alert Threshold Guide — Thresholds, fatigue prevention, and escalation templates
Next Best Skill

Reporting cadence requested → performance-reporter. Standalone setup → Terminal. Visited-set rule applies per skill-contract.md.

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