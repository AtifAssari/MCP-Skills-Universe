---
rating: ⭐⭐⭐
title: web-design-patterns
url: https://skills.sh/jezweb/claude-skills/web-design-patterns
---

# web-design-patterns

skills/jezweb/claude-skills/web-design-patterns
web-design-patterns
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill web-design-patterns
Summary

Principle-based design patterns for website sections that avoid AI-generated aesthetics.

Covers five core section types: heroes, cards, CTAs, trust signals, and testimonials with context-specific guidance for different business types
Teaches WHY and WHEN to use each pattern, not just templates; includes explicit anti-patterns like democratic design, perfect symmetry, and generic copy
Provides cross-cutting principles on hierarchy, asymmetry, and restraint that apply across all patterns
Includes ethical rules for lead-gen sites, prohibiting fabricated ratings, years in business, and named individuals; offers safe alternatives instead
Load-on-demand reference structure with five detailed guides (350–550 lines each) covering constraint-based creativity, grid math, trust psychology, and placement strategy
SKILL.md
Web Design Patterns

Principle-based patterns for designing website sections that feel human-designed, not AI-generated. Each pattern teaches WHY and WHEN, not just templates to copy.

What You Produce

Well-designed website sections: heroes, card layouts, CTAs, trust signals, and testimonials that match the business context and avoid the "AI skeleton" look.

When to Read Which Reference
Building this...	Read this reference
Homepage hero, page headers, landing pages	references/hero-patterns.md
Service cards, team grids, pricing tiers, portfolios	references/card-patterns.md
Conversion sections, buttons, banner CTAs	references/cta-patterns.md
Credibility: badges, licences, reviews, guarantees	references/trust-signals.md
Customer reviews, social proof, quote sections	references/testimonial-patterns.md

Load on demand — don't read all five for every project. Read the one(s) relevant to the current section.

Cross-Cutting Principles

These apply to ALL patterns. Internalise these before reading any reference file.

Anti-AI Patterns (Avoid These)

The "AI skeleton" that signals template-generated design:

The sequence: Hero → trust bar → 3 identical cards → features → stats → CTA → footer
Democratic design: Every element gets equal visual weight, no hierarchy
Perfect symmetry: Everything centred, perfectly aligned, no intentional asymmetry
Identical repetition: All cards same size, same structure, same padding, same shadow
Generic copy: "Learn More" as every CTA, "Quality Service You Can Trust" as every headline
Decoration without purpose: Floating shapes, random gradients, abstract blobs
What Makes Design Feel Human
One element clearly dominates — hierarchy, not democracy
Asymmetry is intentional — not everything centred or balanced
Specific, opinionated copy — "Schedule Your Free Roof Inspection" not "Learn More"
Visual weight guides the eye — you know where to look first, second, third
Restraint — not every technique used, just the ones that serve the purpose
Context-appropriate — emergency plumber looks different from luxury hotel
Ethical Rules

Non-negotiable across all patterns:

On lead-gen sites (no real business data), NEVER fabricate:

Star ratings or review counts
Specific years in business
Licence or ABN numbers
Named individuals or team members
Exact customer counts

Safe alternatives for lead-gen:

"Experienced Team" (not "25 Years Experience")
"Highly Rated" (not "4.9 Stars (127 Reviews)")
"Licensed & Insured" (not "QBCC License #1234567")
Business Context Shapes Everything

The same section type looks completely different for different businesses:

Business type	Design feel
Emergency services	Direct, immediate, phone-first
Luxury/hospitality	Spacious, refined, atmospheric
Trades/local services	Trustworthy, capable, genuine
Professional/corporate	Confident, clean, structured
Creative/agency	Distinctive, bold, personality-driven
Quick Pattern Examples
Hero Approaches

Image-dominant (strong photography available):

Let the image do the work, minimal text
One clear focal point
Text placement within image composition, not slapped on top

Typography-dominant (no strong imagery):

Font choice, size, weight, spacing IS the design
Generous whitespace as active design element
Colour blocking or subtle texture instead of stock photos

Split/balanced (strong copy + strong imagery):

One side dominates slightly — true 50/50 feels indecisive
On mobile, order matters — which element first in vertical stack?
Card Layout Decision
Count items first — wrong grid math creates orphan cards
Check hierarchy — is one item more important? Feature it at 2x size
Content density — image-heavy = fewer columns, text-heavy = more columns
Orphan fix — never leave 1 card alone on a row
CTA Hierarchy

Match CTA urgency to business context:

Emergency services: Phone number IS the CTA. Huge, high-contrast, tappable.
Professional services: Lower commitment first. "Book a consultation."
Creative/agency: Relationship-building. "View our work."

Golden rule: Make your case first, then ask for action. CTA appears AFTER value.

Trust Signal Hierarchy
Tier	Type	Example
1 (Strongest)	Specific, verifiable	"QBCC License #1234567"
2	Third-party validation	"4.8 stars (127 Google Reviews)" + link
3	Self-claimed	"Fully licensed and insured"
4 (Weakest)	Generic assurances	"Quality guaranteed"

One Tier 1 signal beats three Tier 4 signals. Distribute trust throughout the page — don't isolate in one section.

Testimonial Approach
Situation	Approach
One powerful testimonial	Single featured quote, make it big
3-6 good testimonials	Grid with variety, one featured
No real testimonials	Service promises, guarantees, process descriptions

Never use carousels — users see 1 of 5 testimonials, <1% click controls. Show all or curate the best 3.

Reference File Index

Each reference is a deep-dive (300-470 lines) with full principles, anti-patterns, implementation patterns, and business-specific guidance.

File	Lines	Covers
hero-patterns.md	~470	Approach selection, constraint-based creativity, overlay techniques, responsive behaviour, page-specific heroes
card-patterns.md	~550	Layout decision framework, anti-sameness strategies, grid math, orphan handling, CSS patterns, business context
cta-patterns.md	~420	Action hierarchy, placement strategy, copy principles, visual design, mobile considerations, context-specific CTAs
trust-signals.md	~490	Trust psychology, trust hierarchy, context-sensitive trust, lead-gen vs client, placement strategy, anti-patterns
testimonial-patterns.md	~350	Social proof psychology, lead-gen ethics, design approach selection, content principles, placement, alternatives
Weekly Installs
464
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass