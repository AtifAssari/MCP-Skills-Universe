---
title: meta-tags-optimizer
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/meta-tags-optimizer
---

# meta-tags-optimizer

skills/aaron-he-zhu/seo-geo-claude-skills/meta-tags-optimizer
meta-tags-optimizer
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill meta-tags-optimizer
Summary

Optimized meta tags for search results and social sharing with CTR-focused title and description generation.

Generates title tags (50-60 characters), meta descriptions (150-160 characters), Open Graph tags, and Twitter cards with keyword placement and power-word optimization
Provides three title and description variations with CTR analysis, A/B testing suggestions, and character-count validation for SERP display
Includes CORE-EEAT alignment checks to ensure meta tag promises match actual page content
Supports multiple page types (blog, product, landing, service, homepage) and integrates with SEO tools for competitor patterns and CTR metrics when available
SKILL.md
Meta Tags Optimizer

Creates title tags, meta descriptions, and social meta tags that improve CTR and sharing quality.

Quick Start
Create meta tags for a page about [topic] targeting [keyword]

Improve these meta tags for better CTR: [current tags]

Skill Contract

Expected output: a ready-to-use metadata package plus the standard handoff summary for memory/content/.

Reads: the brief, target keywords, entity inputs, quality constraints, and prior decisions from CLAUDE.md and the shared State Model when available.
Writes: a user-facing metadata deliverable and reusable summary.
Promotes: approved angles, messaging choices, missing evidence, and publish blockers to memory/hot-cache.md, memory/decisions.md, and memory/open-loops.md.
Primary next skill: schema-markup-generator when the metadata package is ready for structured-data support.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

Optional search console and SEO tool integrations pull CTR data and competitor patterns automatically; otherwise ask for current tags, keywords, and competitors. See CONNECTORS.md.

Instructions

When a user requests meta-tag optimization, run these six steps:

Gather Page Information — URL, page type, primary and secondary keywords, audience, CTA, and value proposition.
Create Optimized Title Tag — keep it near 50-60 characters, front-load the keyword, and generate three options using the supported title formulas.
Write Meta Description — target 150-160 characters, include the keyword and CTA, and generate three options.
Create Open Graph, Twitter Card, and Additional Meta Tags — include OG, Twitter, canonical, robots, viewport, author, and article tags as needed.
CORE-EEAT Alignment Check — verify C01 (Intent Alignment) and C02 (Direct Answer).
Provide CTR Optimization Tips — explain the winning elements, tradeoffs, and A/B test options.

Reference: See references/instructions-detail.md for the compact workflow, formulas, alignment matrix, CTR analysis, and example. See references/meta-tag-code-templates.md for HTML blocks.

Example

Sample outcome: a 55-character title, a 150-160 character description, and a complete OG / Twitter / Article tag block. See the full worked sample in references/instructions-detail.md.

Tips for Success

Front-load keywords, match intent, be specific, test variations, and refresh tags when the SERP changes.

Save Results

On user confirmation, save memory/content/YYYY-MM-DD-<topic>.md and promote key conclusions to memory/hot-cache.md.

Reference Materials
Instructions Detail — Workflow, formulas, alignment matrix, example
Meta Tag Formulas — Title and description formulas
Meta Tag Code Templates — HTML templates
CTR and Social Reference — CTR patterns and social guidance
Next Best Skill
Primary: schema-markup-generator — complete the SERP package with structured data.
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