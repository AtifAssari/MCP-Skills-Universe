---
title: seo-content-writer
url: https://skills.sh/aaron-he-zhu/seo-geo-claude-skills/seo-content-writer
---

# seo-content-writer

skills/aaron-he-zhu/seo-geo-claude-skills/seo-content-writer
seo-content-writer
Installation
$ npx skills add https://github.com/aaron-he-zhu/seo-geo-claude-skills --skill seo-content-writer
Summary

Keyword-optimized content creation with 12-step SEO workflow and CORE-EEAT quality standards.

Executes a structured 12-step process covering keyword integration, title optimization (5 formula options), meta descriptions, header hierarchy, featured snippet targeting, internal/external linking, and readability enhancement
Produces full drafts with embedded SEO elements, multiple title variants, FAQ sections with schema markup, and self-scored CORE-EEAT checklists
Supports multiple content types: blog posts, landing pages, how-to guides, product descriptions, comparison articles, and pillar content
Applies 16 core CORE-EEAT constraints during writing (intent alignment, direct answers, citation density, evidence mapping, entity precision) with optional full 80-item audit via content-quality-auditor
SKILL.md
SEO Content Writer

Creates SEO content that aligns with search intent, integrates keywords naturally, and stays usable for readers.

Quick Start
Write an SEO-optimized article about [topic] targeting the keyword [keyword]

Here's my content brief: [brief]. Write SEO-optimized content following this outline.

Skill Contract

Expected output: a ready-to-use draft plus the standard handoff summary for memory/content/.

Reads: the brief, target keywords, entity inputs, quality constraints, and prior decisions from CLAUDE.md and the shared State Model when available.
Writes: a user-facing content deliverable and reusable summary.
Promotes: approved angles, messaging choices, missing evidence, and publish blockers to memory/hot-cache.md, memory/decisions.md, and memory/open-loops.md.
Primary next skill: content-quality-auditor when the draft is ready for gating.
Handoff Summary

Emit the standard shape from skill-contract.md §Handoff Summary Format.

Data Sources

Use ~~SEO tool and ~~search console when connected; otherwise ask for keywords, intent, and competitors. See CONNECTORS.md.

Instructions

When a user requests SEO content, run these nine steps:

Gather Requirements — confirm primary and secondary keywords, word count, content type, audience, intent, tone, CTA, and competitors.
Load CORE-EEAT Constraints — apply the 16 high-weight items listed in the companion reference.
Research and Plan — analyze the SERP, map keywords, and choose the content angle.
Create Optimized Title — keep it concise, keyword-led, and aligned with intent.
Write Meta Description — include the keyword, value proposition, and CTA.
Structure Content and Write — use a clean H1 > intro > H2/H3 > FAQ > conclusion flow.
Apply On-Page Best Practices — manage keyword placement, readability, snippets, and supporting visuals.
Add Internal / External Links — include relevant internal and authoritative external links.
Run Final SEO + CORE-EEAT Review — score the draft, auto-fix small issues, and surface any decisions that still need the user.

Reference: See references/instructions-detail.md for the compact workflow, pre-write checklist, issue-classification rules, and self-check format.

Example

Sample outcome: a keyword-led H1, optimized meta description, clear H2 structure, FAQ section, and a brief Changes Made block after the self-check. See references/seo-writing-checklist.md for the copy-start checklist and article template.

Content Type Templates

Quick-start patterns for how-to guides, comparisons, listicles, pillar pages, reviews, and FAQ pages live in references/content-structure-templates.md.

Tips for Success

Match intent, front-load value, support claims with evidence, and write for humans before optimizing for the SERP.

Save Results

On user confirmation, save memory/content/YYYY-MM-DD-<topic>.md and promote key conclusions to memory/hot-cache.md.

Reference Materials
Instructions Detail — Workflow, CORE-EEAT constraints, issue handling, self-check
SEO Writing Checklist — On-page checklist, snippet patterns, and copy-start template
Title Formulas — Headline formulas and CTR patterns
Content Structure Templates — Compact content blueprints
Next Best Skill
Primary: content-quality-auditor — gate the draft before publishing.
Weekly Installs
4.6K
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