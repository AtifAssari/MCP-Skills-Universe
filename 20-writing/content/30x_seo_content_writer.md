---
title: 30x-seo-content-writer
url: https://skills.sh/norahe0304-art/30x-seo/30x-seo-content-writer
---

# 30x-seo-content-writer

skills/norahe0304-art/30x-seo/30x-seo-content-writer
30x-seo-content-writer
Installation
$ npx skills add https://github.com/norahe0304-art/30x-seo --skill 30x-seo-content-writer
SKILL.md
SEO Content Writer
What This Skill Does

Generate SEO-optimized blog articles.

Two Modes
Mode	Input	Use Case
Plan Mode	seo-plan output files	Have complete SEO strategy, write per calendar
Standalone Mode	User provides keyword	Quick single article, no full planning needed
Mode 1: Plan Mode
Prerequisites

Have SEO plan (/seo plan):

CONTENT-CALENDAR.md - Content calendar
SEO-STRATEGY.md - Keyword and topic strategy
Process
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   seo-plan      │     │                 │     │                 │
│   output files  │ ──> │    Generate     │ ──> │   Markdown      │
│ CONTENT-CALENDAR│     │   SEO Content   │     │   blog article  │
│ SEO-STRATEGY    │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘

Context from Plan
Info	Source	Usage
Target keywords	SEO-STRATEGY.md	Title, H2, body optimization
Topic clusters	SEO-STRATEGY.md	Internal link planning
Competitor analysis	COMPETITOR-ANALYSIS.md	Differentiation angle
Mode 2: Standalone Mode
When to Use
Just want to quickly write one article
Don't have a complete SEO plan
Already know the target keyword
Required Input

Ask user:

Topic/Title: Article topic
Target Keyword: Primary keyword
Secondary Keywords: Secondary keywords (optional)
Search Intent: Informational / Commercial / Transactional
Target Length: Short (800-1200) / Medium (1500-2000) / Long (2500+)
CTA Goal: What action should readers take?
Content Generation
Article Structure
# [H1: Include primary keyword, 50-60 chars]

[Hook: Engaging first paragraph, mention keyword naturally]

## [H2: Section with keyword variation]

[Content with semantic keywords, 2-4 paragraphs]

### [H3: Subsection if needed]

[Supporting content]

## [H2: Another main section]

[Continue pattern...]

## Conclusion / Key Takeaways

[Summary, reiterate value, include CTA]

SEO Requirements Checklist
Element	Requirement
Title (H1)	Include primary keyword, 50-60 characters
Meta Description	Include keyword, 150-160 characters, compelling
URL Slug	Short, keyword-rich, hyphenated
First 100 Words	Include primary keyword naturally
Headings	H2s include keyword variations, logical hierarchy
Keyword Density	1-2%, natural placement
Internal Links	3-5 relevant internal links (placeholder: [Internal: topic])
External Links	2-3 authoritative sources
Images	Suggest placements with alt text descriptions
Readability	Short paragraphs, bullet lists, scannable
E-E-A-T Signals to Include
Signal	How to Include
Experience	First-hand examples, case studies, "we tested"
Expertise	Technical depth, accurate information, citations
Authoritativeness	Cite reputable sources, link to studies
Trustworthiness	Clear attribution, honest claims, no exaggeration
AI Citation Readiness (GEO)

For AI search visibility:

Include clear, quotable definitions
Use structured formats (tables, lists)
Answer questions directly in the first sentence
Include specific data points and statistics
Output Format
Deliverables

Blog Article (Markdown format)

Full article with SEO optimization
Meta title and description
Suggested URL slug

SEO Checklist (verification)

 Primary keyword in title
 Primary keyword in first 100 words
 H2s with keyword variations
 Internal link placeholders
 External authoritative links
 Image suggestions with alt text
 CTA included
Commands
Command	Mode
/seo content-writer	Auto-detect (plan mode if seo-plan output exists, otherwise standalone)
/seo content-writer "topic"	Standalone mode, directly specify topic
Integration with Other Skills
Skill	When to Use
seo-plan	Create plan first, then use plan mode to generate content
seo-internal-links suggest	Generate internal link suggestions after writing
seo-content-audit	Audit quality after writing
Quality Gates
Before Generation
 Target keyword confirmed
 Search intent understood
 Length decided
After Generation
 Keyword naturally integrated (not stuffed)
 E-E-A-T signals present
 Readability appropriate for audience
 CTA aligned with business goal
 No factual claims without sources

[PROTOCOL]: Update this header on changes, then check CLAUDE.md

Weekly Installs
40
Repository
norahe0304-art/30x-seo
GitHub Stars
27
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass