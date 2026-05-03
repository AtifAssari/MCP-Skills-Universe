---
title: hormozi-ad-factory
url: https://skills.sh/pedronauck/skills/hormozi-ad-factory
---

# hormozi-ad-factory

skills/pedronauck/skills/hormozi-ad-factory
hormozi-ad-factory
Installation
$ npx skills add https://github.com/pedronauck/skills --skill hormozi-ad-factory
SKILL.md
Hormozi Ad Factory

A systematic framework for generating 150-750+ unique ad variations from a single product or offer, based on Alex Hormozi's combinatorial ad creation method.

Core Concept

Ads consist of three modular parts: Hook, Meat, and CTA. Instead of writing one ad at a time, generate each component independently, then combine them:

50 Hooks x 3-5 Meats x 1-3 CTAs = 150 to 750 unique ads

This approach creates massive variety for testing, which is what wins at scale.

Workflow

Execute the following four steps in order. Before starting, gather context from the user.

Step 0: Gather Context

Before generating any ad components, ask the user these questions (skip any the user has already answered):

Product/Offer: What product, service, or offer is being advertised?
Target Audience: Who is the ideal customer? (demographics, psychographics, pain points)
Platform: Where will these ads run? (Instagram, YouTube, TikTok, Facebook, LinkedIn, Google)
Format: Text ads, video scripts, carousel, or a mix?
Existing Assets: Are there any past ads that performed well? Any organic content with strong engagement?
Competitor References: Any competitor ads to draw inspiration from?
Unique Mechanism: What makes this product/approach different from alternatives?
Key Results/Proof: Specific numbers, testimonials, or case studies available?
Language: Default to English. For Portuguese-speaking users, generate all content in Portuguese (BR) unless told otherwise.

If the user provides minimal context, infer reasonable defaults and state the assumptions clearly before proceeding.

Step 1: Generate 50 Hooks

Hooks are the first 1-3 seconds (video) or first line (text) of the ad. They stop the scroll and earn attention. Use these five sourcing methods to create variety:

Winning hooks from previous ads — Adapt hooks from the user's past high-performing ads.
Hooks from organic content — Pull hooks from the user's best-performing free content.
Winning hooks from competitors — Adapt proven hooks from competitor paid ads.
Hooks from competitors' organic content — Pull hooks from competitor top free content.
Platform ad libraries — Use hooks found in Facebook Ad Library, TikTok Creative Center, etc.

Distribute the 50 hooks across awareness levels to cover different audience segments:

Level	Description	Hook Style
Unaware	Does not know they have a problem	Pattern interrupt, curiosity, shock
Problem-Aware	Knows the problem, not the solution	Call out the pain, frustration, desire
Solution-Aware	Knows solutions exist, has not chosen one	Compare approaches, reveal flaws in alternatives
Product-Aware	Knows the product, has not bought	Overcome objections, social proof, urgency
Most Aware	Knows the product well, needs a push	Deals, bonuses, scarcity, direct offer

Default to a balanced spread (~10 hooks per level) unless the user specifies a focus.

For hook formula templates and examples, read references/hook-formulas.md.

Step 2: Generate 3-5 Meats

The meat is the body of the ad — it educates the audience on the offer, the product, the solution, or the problem. Generate one meat per format:

Demonstration — Show the product/service in action. Best for product-aware audiences.
Testimonial — Let customers tell the story. Best for solution-aware and product-aware audiences.
Educational — Teach something valuable. Best for problem-aware and solution-aware audiences.
Story — Tell a narrative (founder story, customer journey, transformation). Best for unaware and problem-aware audiences.
Faceless — Text on screen, voiceover, b-roll, or screen recordings. Best for scaling without personal brand dependency.

Each meat must be self-contained and work with any hook and any CTA.

For detailed meat structures and length guidelines, read references/meat-formats.md.

Step 3: Generate 1-3 CTAs

The CTA tells the viewer exactly what to do next. A strong CTA includes up to five elements:

What to do — The specific action (click, comment, DM, sign up, buy)
How to do it — The mechanic (click the link below, comment "X", tap the button)
What they get — The immediate result of taking action
Why now — Urgency or scarcity element
Risk reversal — Remove the fear (free trial, money-back, no commitment)

Not every CTA needs all five, but the best ones cover most of them.

For CTA templates and examples, read references/cta-templates.md.

Step 4: Assemble the Combinations

After generating all components, combine them into a matrix. Present the output as:

Summary table showing total combinations (Hooks x Meats x CTAs)
Top 10-15 "golden" combinations — the ones most likely to perform well based on audience-message fit, with rationale for each
Full component library organized by type, for the user to mix and match

For the full output format template, read assets/output-template.md.

Platform Adaptation

Adapt the format of each component based on the target platform:

Platform	Hook	Meat	CTA
Video ads (TikTok, YouTube, Reels)	Opening line/scene (1-3s)	Script section with visual directions (15-45s)	Closing sequence with on-screen text
Text/copy ads (Facebook, LinkedIn)	Headline or opening line	Body copy paragraphs (3-8 sentences)	Closing paragraph with link
Carousel ads (Instagram, LinkedIn)	Slide 1	Slides 2-8	Last slide
Short-form (Twitter/X, Stories)	Single punchy line	1-3 sentences max	Inline CTA
Error Handling
User provides no product info: Do not generate ads. Ask for at minimum: product name, what it does, and who it is for.
Vague audience: Generate hooks for all five awareness levels with a balanced spread and note the assumption.
Too many platforms: Generate a single platform-agnostic set first, then offer to adapt for specific platforms.
User wants fewer than 50 hooks: Adjust proportionally but maintain the awareness-level distribution.
User wants full ads, not components: Generate the components first, then assemble the top 15 golden combinations as complete ready-to-use ads.
Examples
Example 1: SaaS Product

User: "Generate ads for my project management tool aimed at remote teams."

Process:

Clarify: pricing, key differentiator, existing testimonials, platform
Generate 50 hooks across awareness levels (e.g., "Your remote team is wasting 5 hours/week in status meetings" for problem-aware)
Generate 4 meats: demo walkthrough, customer testimonial, educational ("3 signs your PM tool is slowing you down"), founder story
Generate 2 CTAs: free trial (risk reversal) + limited-time discount (urgency)
Assemble 400 combinations, highlight top 15 golden ads
Example 2: Physical Product (Portuguese)

User: "Crie anuncios para meu curso de culinaria online para iniciantes."

Process:

All content generated in Portuguese (BR)
Hooks adapted for cooking/education audience awareness levels
Meats include: demo (cooking a recipe), testimonial (student transformation), educational (common beginner mistakes)
CTAs include engagement ("Comente RECEITA") and direct ("Clique no link da bio")
Golden combinations prioritize video format for Instagram/TikTok
Example 3: Minimal Context

User: "I need some ad ideas for my coaching business."

Process:

Ask: What type of coaching? Who is the target client? What platform? What is the offer/price point?
Wait for answers before generating
If user says "just give me something," state assumptions explicitly and proceed with a general framework
Weekly Installs
78
Repository
pedronauck/skills
GitHub Stars
338
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn