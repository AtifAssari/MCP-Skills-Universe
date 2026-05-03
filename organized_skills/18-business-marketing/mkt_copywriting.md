---
rating: ⭐⭐⭐
title: mkt-copywriting
url: https://skills.sh/hungv47/agent-skills/mkt-copywriting
---

# mkt-copywriting

skills/hungv47/agent-skills/mkt-copywriting
mkt-copywriting
Installation
$ npx skills add https://github.com/hungv47/agent-skills --skill mkt-copywriting
SKILL.md
Copywriting

Horizontal skill — applied wherever persuasive writing is needed. Also bootstraps product context for all marketing skills.

Inputs Required
Page purpose, audience, product/offer, traffic context
.agents/mkt/product-context.md (created below if missing)
Output
Copy by section + annotations + 2-3 alternatives per key line
.agents/mkt/product-context.md (if it didn't exist)
Quality Gate

Before delivering, verify:

 Every headline/hook contains a concrete noun or specific number (not abstract: "better", "innovative", "leading")
 Every key line passes 3-question test (visual? falsifiable? uniquely yours?)
 CTA follows [Action Verb] + [What They Get] formula
 Competitor swap test: Replace brand name with competitor — if it still works, rewrite
Chain Position

Horizontal — called from any skill. Creates .agents/mkt/product-context.md used by all marketing skills.

Before Starting
Step 0: Product Context

Check for .agents/mkt/product-context.md. If missing: INTERVIEW. Ask 8 product questions and save to .agents/mkt/product-context.md.

Required Artifacts
Artifact	Source	If Missing
product-context.md	mkt-copywriting	INTERVIEW. Ask 8 product questions and save to .agents/mkt/product-context.md.
Optional Artifacts
Artifact	Source	Benefit
icp-research.md	mkt-icp-research	Audience language for better copy
imc-plan.md	mkt-imc	Angle context when called from IMC
Product Context Bootstrap

Check for .agents/mkt/product-context.md. If missing, interview with these 8 questions and save:

# Product Context

**Date:** [today]

## Product
[One sentence: what you sell]

## Buyer
[Primary buyer: role, company type, situation]

## Problem
[The pain it solves — in their words, not yours]

## Differentiator
[What's different — something a competitor CANNOT claim]

## Social Proof
[Best testimonial or most repeated praise]

## Model
[Price, pricing model, free trial availability]

## Voice
[3 adjectives: e.g., "direct, technical, warm"]

## Primary CTA
[What should people do next: e.g., "Start free trial"]


All marketing skills read this file for product context.

The Three-Question Test

Run every key sentence through:

Visual? Close your eyes. Can you see it? ("Couch to 5K" = yes. "Regain fitness" = no.)
Falsifiable? Is it true or false? ("6'2, reads on the tube" = yes. "Funny, smart, good values" = no.)
Uniquely yours? Could a competitor sign this? ("The dating app designed to be deleted" = only Hinge. "The best platform" = anyone.)

Three yeses = keep. Any no = rewrite.

Core Rules
Make It Visual

Abstract words evaporate. Concrete words stick. Zoom-in technique: Write the abstract word → ask "what do I actually mean?" → keep zooming until you hit something you can drop on your foot.

"Regain fitness" → "Couch to 5K"
"Worn by pretty and old people" → "Worn by supermodels in London and dads in Ohio"
Make It Falsifiable

True-or-false statements put your head on the chopping block. Ears prick up. "Don't talk, only point" — point at the graph, the statistic, the specific feature.

Volvo: "Your car has five numbers on the speedometer. Volvo has six."
Make It Yours Alone

"Never write an ad a competitor can sign." — Jim Durfee

Test: Swap in competitor's name. Still works? Rewrite.

Facts Over Adjectives

Start with a fact. Build from there. "Even when it's not Heinz, it's Heinz."

The Conflict Framework

Draw a line. Write opposites. Left: "Throw money and pray." Right: "Learn copywriting." Contrast sharpens both sides.

Speed Test

Show someone your copy. Two seconds. If they don't get it, rewrite.

CTA Formula

[Action Verb] + [What They Get] + [Qualifier]

Bad: Submit, Learn More, Click Here Good: "Start your free trial", "Download the 2026 playbook", "See pricing for your team"

Page-Specific Guidance
Page	Key Principle
Homepage	What you do in one sentence. Primary use case, not every feature.
Landing Page	One goal, one CTA. Match headline to traffic source. Remove nav.
Pricing	Lead with value, not price. Anchor with most popular plan.
Feature	Lead with outcome ("Track time in one click"), not feature name.
About	Founding story. What you believe. Team photos + real context.
Cross-Skill Integration
Called From	Focus On	Return
mkt-content-create	Hook + CTA copy	Specific text, not frameworks
mkt-lp-optimization	Headline variants + PAS body	10+ headline options, scored
mkt-imc	Angle descriptions, pillar messaging	Sharpened angle text
Output Format

When saving copy artifacts, use this frontmatter:

---
skill: mkt-copywriting
version: 1
date: [today's date]
status: draft
---


On re-run: rename existing artifact to [name].v[N].md and create new with incremented version.

Copy by section — Hero, social proof, problem, solution, how it works, testimonials, CTA
Annotations — Why each choice was made, tied to which rule
Alternatives — 2-3 headline options, 2-3 CTA options
Meta — Page title + description if relevant
Process
Check for .agents/mkt/product-context.md — create if missing
Who am I talking to? What do they currently believe? What should they believe after?
What can I say that nobody else can?
Write 3-5 versions of every key line
Run each through 3-question test
Two-second test
Cut everything not working for you
See references/copy-frameworks.md for headline formulas
References
references/copy-frameworks.md — Headline formulas, PAS framework, page templates
Weekly Installs
19
Repository
hungv47/agent-skills
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass