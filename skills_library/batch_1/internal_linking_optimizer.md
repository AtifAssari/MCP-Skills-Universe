---
title: internal-linking-optimizer
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/internal-linking-optimizer
---

# internal-linking-optimizer

skills/aaron-he-zhu/seo-geo-claude-skills/internal-linking-optimizer
internal-linking-optimizer
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill internal-linking-optimizer
Summary

Analyzes and optimizes internal link structure to improve site authority distribution and search engine crawlability.

Maps current internal linking patterns, identifies orphan pages with no inbound links, and detects authority flow bottlenecks across the site
Provides anchor text optimization recommendations to improve topical relevance and avoid over-optimization
Creates topic cluster and pillar-cluster linking strategies with specific source-target-anchor recommendations
Generates phased implementation plans with navigation optimization, contextual link opportunities, and tracking metrics
Requires sitemap, page list, or web crawler integration; works with manual data if automated crawl unavailable
SKILL.md
Internal Linking Optimizer

Analyzes internal link structure, authority flow, orphan pages, anchor text, and topic clusters, then delivers a prioritized linking plan with source/target/anchor recommendations.

Quick Start

Start with one of these prompts, then finish with the standard handoff summary from Skill Contract.

Analyze internal linking structure for [domain/sitemap]
Find internal linking opportunities for [URL]
Create internal linking plan for topic cluster about [topic]
Suggest internal links for this new article: [content/URL]
Find orphan pages on [domain]
Optimize anchor text across the site

Skill Contract

Expected output: a scored diagnosis, prioritized repair plan, and a short handoff summary ready for memory/audits/.

Reads: the current page or site state, symptoms, prior audits, and current priorities from CLAUDE.md and the shared State Model when available.
Writes: a user-facing audit or optimization plan plus a reusable summary that can be stored under memory/audits/.
Promotes: blocking defects, repeated weaknesses, and fix priorities to memory/open-loops.md and memory/decisions.md.
Next handoff: use the Next Best Skill below when the repair path is clear.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

Uses ~~web crawler and ~~analytics when connected; otherwise asks user for sitemap, key page URLs, and content categories. See CONNECTORS.md and SECURITY.md §Scraping Boundaries.

Instructions

When a user requests internal linking optimization:

Analyze Current Structure -- Capture domain, pages analyzed, total internal links, average links/page, link distribution, top linked pages, under-linked important pages, and a structure score. Flag crawl-depth and authority-flow problems.
Identify Orphan Pages -- List pages with no inbound internal links. Prioritize high-value orphans with traffic/rankings, medium-potential pages that need category/tag links, and low-value pages to delete, noindex, or redirect.
Analyze Anchor Text Distribution -- Check current anchor patterns, distribution by page, over-optimization, generic anchors, and CORE-EEAT R08 alignment.

Reference: references/linking-templates.md contains the Step 3 output template.

Create Topic Cluster Link Strategy -- Map pillar/cluster links, recommend structure, and list specific links to add.

Reference: references/linking-templates.md contains the Step 4 template.

Find Contextual Link Opportunities -- For each page, identify topic-relevant source/target/anchor opportunities and prioritize high-impact additions.

Reference: references/linking-templates.md contains the Step 5 template.

Optimize Navigation and Footer Links -- Review main/footer/sidebar/breadcrumb navigation; recommend pages to add, demote, or remove.

Reference: references/linking-templates.md contains the Step 6 template.

Generate Implementation Plan -- Include executive summary, current-state metrics, phased priority actions, implementation guide, and tracking plan.

Reference: references/linking-templates.md contains the Step 7 template.

Example

User: "Find internal linking opportunities for my blog post on 'email marketing best practices'"

Output: 5 high-value links with source paragraph, destination URL, recommended anchor text, and priority. Example targets might include list-building, subject-line, segmentation, automation, and tools pages.

Reference: See references/linking-example.md for the full worked example.

Tips for Success
Prioritize relevance and user navigation over link volume.
Use descriptive, varied anchors; avoid exact-match repetition.
Link important pages from hubs, navigation, or strong contextual sources.
Audit regularly as content grows.
Save Results

Ask to save results; if yes, write a dated summary to memory/audits/internal-linking-optimizer/YYYY-MM-DD-<topic>.md. Append veto-level issues to memory/hot-cache.md automatically.

Reference Materials
Link Architecture Patterns -- Architecture models, selection thresholds, migration safeguards, and measurement targets
Linking Templates -- Detailed output templates for steps 3-7
Linking Example -- Full worked example for internal linking opportunities
Next Best Skill

Primary: on-page-seo-auditor -- verify that revised internal links support page-level goals.

Weekly Installs
3.0K
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