---
rating: ⭐⭐
title: marketing-strategy
url: https://skills.sh/manojbajaj95/claude-gtm-plugin/marketing-strategy
---

# marketing-strategy

skills/manojbajaj95/claude-gtm-plugin/marketing-strategy
marketing-strategy
Installation
$ npx skills add https://github.com/manojbajaj95/claude-gtm-plugin --skill marketing-strategy
SKILL.md
Marketing Strategy

Strategy and positioning layer for B2B SaaS — from product-market fit through competitive intelligence, sales enablement, and growth loops. For launch execution and channel strategy, see go-to-market-strategy.

Product Strategy Stack
VISION      — Where are we going? (3–10 years)
STRATEGY    — How will we win? (1–3 years)
ROADMAP     — What are we building? (Quarters)
EXECUTION   — How are we building? (Sprints)


Philosophy: Start with the customer problem, not your solution. Make trade-offs explicit — strategy is choosing what NOT to do. Systems over tactics: growth loops compound; growth hacks don't.

Product-Market Fit Spectrum
Level 0: Problem Fit    → Real problem worth solving
Level 1: Solution Fit   → Your solution addresses the problem
Level 2: PMF            → Customers pull the product from you
Level 3: Scale Fit      → Repeatable growth engine working
Level 4: Moat Fit       → Defensible competitive advantage established


PMF validation signals: 5+ ICP customers, below-median sales cycle, above-median LTV, <5% churn, NPS 9–10.

Market Opportunity (TAM/SAM/SOM)
Metric	What It Means	How to Calculate
TAM	Everyone who could theoretically buy	Target customers × avg contract value
SAM	Those you can reach and serve	TAM × geographic/product constraints
SOM	Realistic near-term share	SAM × 1–5% penetration

Validate top-down with bottom-up: (realistic customers × conversion rate × ACV). Gap >3x → revisit assumptions.

ICP & Segmentation

ICP Firmographics (Series A sweet spot): 50–5,000 employees, SaaS/Tech/Professional Services, $5M–$500M revenue.

Buyer Personas:

Economic Buyer (VP/Director): Cares about ROI, cost reduction → business outcomes + case studies
Technical Buyer (Engineer): Cares about integration, security → architecture, uptime, SOC 2
Champion (Manager): Cares about ease of use → UX, quick wins

ICP Scoring (HubSpot): A (perfect fit) → D (poor fit). Focus acquisition on A/B, disqualify D.

Positioning (April Dunford Method)
Competitive alternatives — What would customers do without you? (competitors, spreadsheets, DIY, status quo)
Unique attributes — What do you have that alternatives don't?
Value mapping — Attribute → Value → Outcome (e.g., AI automation → eliminates manual entry → save 10 hrs/week)
Best-fit customers — Who values this most? Use win/loss data.
Market category — Head-to-head, niche ("CRM for agencies"), or new category
Trend layer — What macro trend makes now the right time to buy?

Value proposition: [Product] helps [Target] [Achieve Goal] by [Unique Approach]

Positioning template:

For [target customer]
Who [need/problem]
[Product] is a [category]
That [key benefit]
Unlike [competitors]
Our product [unique differentiator]


Messaging hierarchy: One-liner → 3–5 key benefits → feature/outcome pairs → proof points (logos, stats, case studies)

Working Backwards (PR/FAQ)

Write an internal press release BEFORE building. If you can't write a compelling press release, you don't have a compelling product.

Press Release structure (~1 page):

Headline — product name + one-sentence customer benefit
Opening — who is the customer and what problem is solved
Problem paragraph — the current pain in detail
Solution paragraph — what the product does
Customer quote (fictional) — how it changes their life
Getting started + CTA

FAQ (External + Internal): External = questions real customers would ask. Internal = questions your skeptical colleagues would ask (the hard ones).

Anti-patterns: Writing the PR after building, solution-first thinking, vague customer definition ("everyone could use this"), skipping the hard internal FAQ, marketing hyperbole instead of specific measurable claims.

Competitive Intelligence

Tiers: Direct competitors | Indirect/adjacent | Status quo (spreadsheets, DIY, do nothing)

Intel sources: Product trials, website monitoring, customer interviews, Gong/Chorus recordings, G2 reviews, competitor job postings, industry reports.

Battlecard template (one per competitor):

Competitor | Strengths | Weaknesses | Our advantages
When we win | When we lose
Talk tracks for top 3 objections
Proof points (case studies, review comparisons, win rate)


Update monthly. Distribute via Notion/Confluence to Sales, CS, Product.

Win/Loss process: Interview within 2 weeks of close. Track in HubSpot: reason, competitor, price factor, product gap. Share monthly insights report with product and sales.

Competitive moat types:

Moat	Description	Examples
Network Effects	Product improves as more users join	Slack, LinkedIn
Switching Costs	Painful to leave	Salesforce, Workday
Data Advantages	Proprietary data improves product	Google, Waze
Scale Economies	Cost advantages at scale	AWS, Stripe
Brand	Trust and recognition	Apple, Notion
Growth Loops & PLG
Growth Loop Types
Loop	Mechanism	Key Metric
Viral	Users invite users	K-factor
Content	Users create discoverable content	Indexed pages
Paid	Revenue funds acquisition	CAC payback
SEO	Content ranks, drives traffic	Organic traffic
PLG Motion Types
Motion	Best For	Key Lever
Freemium	Simple products, network effects	Free → paid conversion
Free Trial	Complex products	Trial conversion rate
Reverse Trial	High-value products	Premium feature discovery
Usage-Based	API/variable consumption	Usage expansion
North Star Metric

A good North Star measures value delivered, is a leading indicator of revenue, reflects product strategy, and is actionable by the product team. Examples: Slack → DAU sending messages; Airbnb → Nights booked

AARRR Funnel: Acquisition → Activation → Retention → Revenue → Referral. Fix activation before optimizing acquisition — don't fill a leaky bucket.

Business Model Design
Model	Pros	Cons
SaaS	Predictable, high LTV	Long sales cycle
Freemium	Low CAC, viral	Free → paid conversion hard
Usage-Based	Scales with customer	Revenue unpredictability
Marketplace	Network effects	High volume needed

Unit economics:

LTV = (Monthly Revenue × Gross Margin %) ÷ Monthly Churn Rate
Target: LTV > 3x CAC, CAC payback < 18 months

Sales Enablement

Core assets: Sales deck (15 slides, visual-first) · One-pagers (product, competitive, case study, pricing) · Battlecards · Demo script (discover → show → Q&A → next step) · Email sequences · ROI calculator

Enablement cadence:

Monthly: Competitive update call — product updates, battlecards, win/loss, best practices
Quarterly: Half-day workshop — positioning refresh, role-play, customer panel
New hire: 4-week ramp — company → ICP/messaging → competitive intel → demo certification

PMM handoffs: Demand Gen (2-week lead time) | Sales (48-hr SLA on competitive questions) | Product (weekly sync) | CS (1-week for launch enablement)

Product Marketing Context Document

Create strategy/brand.md (or .agents/product-marketing-context.md) capturing:

Product Overview — one-liner, what it does, category, business model
Target Audience — company type, decision-makers, use case, jobs to be done
Buyer Personas — user, champion, economic buyer, technical influencer (pain + value promise each)
Problems & Pain Points — core challenge, why alternatives fail, cost of the problem
Competitive Landscape — direct, secondary, indirect competitors + how each falls short
Differentiation — key differentiators, why customers choose you
Objections & Anti-Personas — top 3 objections + who is NOT a good fit
Customer Language — verbatim phrases customers use for the problem and your solution
Brand Voice — tone, style, personality (3–5 adjectives)
Proof Points — metrics, notable customers, testimonial snippets

Auto-draft approach: Study the repo (README, landing pages, marketing copy), draft V1, then ask: "What needs correcting? What's missing?"

All other marketing skills reference this file automatically.

PMM KPIs
KPI	Target
Feature adoption (90 days)	>40%
Win rate (competitive deals)	>30%
Sales velocity	-20% YoY
Deal size (ACV)	+25% YoY
Launch ROMI	3:1 (pipeline : spend)

QBR slide structure: Executive summary → KPI dashboard (target vs. actual) → what worked / what didn't → next quarter priorities + budget ask

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
Weekly Installs
40
Repository
manojbajaj95/cl…m-plugin
GitHub Stars
43
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass