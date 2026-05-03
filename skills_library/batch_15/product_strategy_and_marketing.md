---
title: product-strategy-and-marketing
url: https://skills.sh/manojbajaj95/claude-gtm-plugin/product-strategy-and-marketing
---

# product-strategy-and-marketing

skills/manojbajaj95/claude-gtm-plugin/product-strategy-and-marketing
product-strategy-and-marketing
Installation
$ npx skills add https://github.com/manojbajaj95/claude-gtm-plugin --skill product-strategy-and-marketing
SKILL.md
Product Strategy & Marketing

Unified product strategy skill — from vision and market opportunity through competitive positioning, growth loops, PLG, and product marketing context.

Philosophy

Great product strategy asks the right questions and makes reversible decisions quickly while being thoughtful about irreversible ones.

Start with the customer problem — not your solution
Create optionality — platform thinking enables multiple futures
Make trade-offs explicit — strategy is choosing what NOT to do
Systems over tactics — growth loops compound; growth hacks don't
Product Strategy Stack
┌─────────────────────────────┐
│          VISION             │  Where are we going? (3-10 years)
├─────────────────────────────┤
│         STRATEGY            │  How will we win? (1-3 years)
├─────────────────────────────┤
│          ROADMAP            │  What are we building? (Quarters)
├─────────────────────────────┤
│         EXECUTION           │  How are we building? (Sprints)
└─────────────────────────────┘

Product-Market Fit Spectrum
Level 0: Problem Fit    → You've found a real problem worth solving
Level 1: Solution Fit   → Your solution addresses the problem
Level 2: PMF            → Customers pull the product from you
Level 3: Scale Fit      → Repeatable growth engine working
Level 4: Moat Fit       → Defensible competitive advantage established

Market Opportunity Framework

TAM → SAM → SOM

Metric	What It Means	How to Calculate
TAM	Everyone who could theoretically buy	Target customers × avg contract value
SAM	Those you can reach and serve	TAM × geographic/product constraints
SOM	Realistic near-term share	SAM × realistic penetration (1-5%)

Always validate top-down with bottom-up: (realistic customers × conversion rate × ACV). If gap is >3x, revisit assumptions.

Working Backwards (PR/FAQ)

Amazon's product methodology: start with the customer outcome, work backward to the solution.

Write an internal press release BEFORE building anything. If you can't write a compelling press release, you don't have a compelling product.

PR/FAQ Structure

Press Release (~1 page):

Headline — product name, one-sentence customer benefit
Dateline + subheadline
Opening paragraph — who is the customer and what problem is solved
Problem paragraph — the current pain in detail
Solution paragraph — what the product does
Customer quote (fictional) — how it changes their life
Company/founder quote — why this matters
Getting started — how to begin
Closing — call to action

FAQ (External + Internal):

External FAQ: Questions real customers would ask
Internal FAQ: Questions your skeptical colleagues would ask (the hard ones)

Anti-patterns to avoid:

Writing the PR after building (defeats the purpose)
Solution-first thinking — retrofitting a problem to your idea
Vague customer definition ("everyone could use this")
Skipping the hard internal FAQ questions
Marketing hyperbole instead of specific, measurable claims

For patterns and examples: see references/ directory

Competitive Positioning & Moats
Moat Type	Description	Examples
Network Effects	Product improves as more users join	Slack, LinkedIn
Switching Costs	Painful to leave	Salesforce, Workday
Data Advantages	Proprietary data improves product	Google, Waze
Scale Economies	Cost advantages at scale	AWS, Stripe
Brand	Trust and recognition	Apple, Notion

Positioning template:

For [target customer]
Who [customer need/problem]
[Product] is a [product category]
That [key benefit/differentiation]
Unlike [competitors]
Our product [unique value]


Competitive decision types:

Type 1 (irreversible): Business model, platform choice — take your time
Type 2 (reversible): Feature prioritization, pricing tiers — decide quickly
Growth Loops & PLG
Growth Loop Types
Loop	Mechanism	Key Metric
Viral	Users invite users	K-factor
Content	Users create discoverable content	Indexed pages
Paid	Revenue funds acquisition	CAC payback
SEO	Content ranks, drives traffic	Organic traffic
Sales	Pipeline → revenue → more reps	ACV/CAC
PLG Motion Types
Motion	Best For	Key Lever
Freemium	Simple products, network effects	Free → paid conversion
Free Trial	Complex products	Trial conversion rate
Reverse Trial	High-value products	Premium feature discovery
Usage-Based	API/variable consumption	Usage expansion
North Star Metric Framework

A good North Star:

Measures value delivered to customers
Is a leading indicator of revenue
Reflects product strategy
Is actionable by the product team

Examples: Slack → DAU sending messages; Airbnb → Nights booked; Figma → Weekly Active Editors

AARRR Funnel

Acquisition → Activation → Retention → Revenue → Referral

Rule: Fix activation before optimizing acquisition. Filling a leaky bucket wastes spend.

Product Marketing Context

Before any marketing work, create .agents/product-marketing-context.md capturing:

Product Overview — one-liner, what it does, product category, business model
Target Audience — company type, decision-makers, primary use case, jobs to be done
B2B Personas — user, champion, economic buyer, technical influencer (with pain + value promise)
Problems & Pain Points — core challenge, why alternatives fail, cost of the problem
Competitive Landscape — direct, secondary, and indirect competitors + how each falls short
Differentiation — key differentiators, why customers choose you
Objections & Anti-Personas — top 3 objections + who is NOT a good fit
Customer Language — verbatim phrases for how customers describe the problem and your solution
Brand Voice — tone, style, personality (3-5 adjectives)
Proof Points — metrics, notable customers, testimonial snippets

Auto-draft approach (recommended): Study the repo (README, landing pages, marketing copy, package.json), draft a V1, then ask: "What needs correcting? What's missing?"

All other marketing skills reference this file automatically — create it once, update as needed.

Business Model Design
Revenue Model Options
Model	Pros	Cons
SaaS	Predictable, high LTV	Long sales cycle
Freemium	Low CAC, viral	Free → paid conversion hard
Usage-Based	Scales with customer	Revenue unpredictability
Marketplace	Network effects	High volume needed
Unit Economics
LTV = (Monthly Revenue per Customer × Gross Margin %) ÷ Monthly Churn Rate
Target: LTV > 3x CAC, CAC payback < 18 months

Key Strategic Questions
Horizontal vs Vertical? — Serve many industries or dominate one deeply?
High-Touch vs Self-Service? — Drives CAC, LTV, and scaling ability
Niche vs Broad? — Start narrow, expand over time
Premium vs Budget? — Rarely can do both
First Mover vs Fast Follower? — Category size determines which matters
Anti-Patterns
Vision without strategy — inspiring destination, no map
Strategy without trade-offs — if everything is a priority, nothing is
TAM theater — unrealistic market sizes to impress investors
Feature parity obsession — chasing competitors instead of customers
Premature scaling — scaling before PMF
Optimizing acquisition before activation — filling a leaky bucket
Vanity metrics — MAU without engagement is meaningless
Related Skills
go-to-market-strategy — Launch planning and execution
pricing-strategy — Pricing decisions and packaging
sales-and-revenue-operations — Sales team, RevOps
Weekly Installs
121
Repository
manojbajaj95/cl…m-plugin
GitHub Stars
43
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass