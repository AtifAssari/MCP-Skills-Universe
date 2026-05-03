---
rating: ⭐⭐
title: elite-ux-strategy
url: https://skills.sh/rshvr/elite-web-design/elite-ux-strategy
---

# elite-ux-strategy

skills/rshvr/elite-web-design/elite-ux-strategy
elite-ux-strategy
Installation
$ npx skills add https://github.com/rshvr/elite-web-design --skill elite-ux-strategy
SKILL.md
Elite UX Strategy

Beautiful design means nothing if it doesn't convert. This skill bridges psychology, design, and business strategy.

Quick Reference
Topic	Reference File
Psychology & Persuasion	psychology-foundations.md
Funnel Strategy	funnel-strategy.md
Copywriting	copywriting.md
Social Proof & Trust	social-proof-trust.md
Pricing Pages	references/pricing-pages.md
Forms & CTAs	forms-ctas.md
Testing & Benchmarks	testing-benchmarks.md
Mobile Conversion	mobile-conversion.md
Ethical Boundaries	ethical-boundaries.md
Modern Patterns	modern-patterns.md
Navigation patterns	navigation-patterns.md
Forms & feedback	forms-feedback.md
Conversion-First Philosophy
The Hierarchy
1. CLARITY    → Can users understand what you offer in 5 seconds?
2. RELEVANCE  → Does it match what brought them here?
3. VALUE      → Is the benefit clear and compelling?
4. FRICTION   → What's stopping them from acting?
5. URGENCY    → Why should they act now?

When Aesthetics vs Conversion Conflict
Situation	Decision
Beautiful animation delays CTA visibility	Reduce/remove animation
Minimal design hides trust signals	Add trust signals strategically
Creative layout confuses scanning	Use proven patterns
Bold design choice feels risky	A/B test it
"Cleaner" means fewer conversion elements	Test removal vs keeping

Default rule: When in doubt, optimize for clarity over creativity.

The Conversion Funnel (AIDA+RR)
┌─────────────────────────────────────────────────────────────┐
│  AWARENESS   │ First impression, hero, headline             │
│              │ Goal: Stop the scroll, communicate value     │
├─────────────────────────────────────────────────────────────┤
│  INTEREST    │ Features, benefits, how it works             │
│              │ Goal: Build curiosity, answer "what?"        │
├─────────────────────────────────────────────────────────────┤
│  DESIRE      │ Social proof, case studies, emotional appeal │
│              │ Goal: Create want, answer "why me?"          │
├─────────────────────────────────────────────────────────────┤
│  ACTION      │ CTA, pricing, signup form                    │
│              │ Goal: Remove friction, make it easy          │
├─────────────────────────────────────────────────────────────┤
│  RETENTION   │ Onboarding, engagement, value delivery       │
│              │ Goal: Create habit, deliver promised value   │
├─────────────────────────────────────────────────────────────┤
│  REFERRAL    │ Share mechanics, referral program            │
│              │ Goal: Turn users into advocates              │
└─────────────────────────────────────────────────────────────┘


See funnel-strategy.md for stage-specific patterns.

Buyer Persona Quick Reference
By Decision Style
Type	Characteristics	Design Approach
Analytical	Needs data, compares options, slow decision	Feature tables, specs, case studies with metrics
Emotional	Decides by feeling, influenced by stories	Testimonials, imagery, transformation narrative
Impulsive	Quick decisions, responds to urgency	Strong CTAs, limited-time offers, social proof
Methodical	Process-driven, needs all information	FAQs, detailed documentation, guided tours
By Context
Context	Buyer Behavior	Strategy
B2B	Multiple stakeholders, longer cycle	ROI focus, case studies, demos, security signals
B2C	Individual decision, emotional factors	Benefits over features, lifestyle imagery, reviews
High-ticket	Considered purchase, risk averse	Trust signals, guarantees, human touch (calls/chat)
Low-ticket	Impulse-friendly, price sensitive	Urgency, social proof, frictionless checkout
Enterprise	Committee decision, compliance needs	Custom solutions, SLAs, dedicated support
SMB	Speed matters, budget conscious	Quick value, clear pricing, self-serve
Key Benchmarks (2024-2026)
Metric	Poor	Average	Good	Excellent
Landing page conversion	< 2%	2-5%	6-10%	15%+
Email capture rate	< 1%	1-2%	2-5%	5%+
Cart abandonment	> 80%	70-80%	60-70%	< 60%
Free trial → Paid (SaaS)	< 5%	5-10%	10-20%	25%+
Mobile vs Desktop gap	> 2.5x	2-2.5x	1.5-2x	< 1.5x
Integration with Other Elite Skills

Every design decision affects conversion. Here's how the other skills impact business outcomes:

elite-gsap (Animations)
Pattern	Conversion Impact
ScrollTrigger reveals	Progressive disclosure keeps attention → lower bounce
SplitText headlines	Attention capture → increased engagement
Flip filtering	Smooth product browsing → higher AOV
Loading animations	Perceived performance → lower abandonment

Warning: Over-animation delays CTAs and frustrates users. Use purposefully.

elite-layouts (Structure)
Pattern	Conversion Impact
Bento grids	Scannable features → faster comprehension
Horizontal scroll	Immersive storytelling → emotional connection
Sticky sections	Persistent CTAs → higher click-through
Container queries	Consistent experience → mobile conversion
elite-performance (Speed)

Every second counts:

1s delay = 7% conversion loss
3s load time = 53% mobile bounce
LCP > 2.5s = significant ranking penalty

Speed IS a conversion factor.

elite-accessibility
Practice	Conversion Impact
WCAG compliance	Larger addressable audience
Clear focus states	Keyboard users can convert
Accessible forms	Fewer errors, more completions
Trust signal	Signals professionalism
Quick Decision Framework
Should I add this element?
1. Does it reduce friction? → Add it
2. Does it build trust? → Add it (strategically placed)
3. Does it distract from the CTA? → Remove or de-emphasize
4. Does it answer an objection? → Add it near the decision point
5. Does it look good but serve no purpose? → Remove it

Should I test this change?
HIGH IMPACT (test first):
- Headlines and value props
- CTA copy and placement
- Pricing presentation
- Form fields (removing any)
- Social proof placement

LOW IMPACT (implement without test):
- Minor copy tweaks
- Color variations (usually)
- Icon changes
- Spacing adjustments

Common Conversion Killers
Above the Fold
 Unclear value proposition
 No visible CTA
 Slow loading hero image/video
 Generic stock photography
 Jargon-heavy headline
Throughout the Page
 Missing social proof
 No trust signals (especially near payment)
 Too many choices (paradox of choice)
 Friction in forms (unnecessary fields)
 No urgency or reason to act now
 Mobile experience significantly worse
Psychological
 Not addressing objections
 Benefits buried under features
 No risk reversal (guarantees, free trials)
 Asking for too much too soon
 Ignoring user's awareness level
Project Type Quick-Starts
SaaS Landing Page
Priority order:
1. Clear value prop in headline
2. Social proof (logos, testimonials)
3. Feature/benefit section
4. Pricing with recommended tier
5. FAQ addressing objections
6. Final CTA with guarantee

E-commerce Product Page
Priority order:
1. High-quality product images
2. Clear price and availability
3. Reviews and ratings
4. Add to cart (prominent, sticky on mobile)
5. Trust signals (shipping, returns, security)
6. Cross-sells/upsells (post add-to-cart)
7. Scarcity badges for real inventory status
→ See mobile-conversion.md: Sticky Add-to-Cart
→ See social-proof-trust.md: Scarcity Badges

Lead Generation
Priority order:
1. Compelling offer (what they get)
2. Minimal form (name + email minimum)
3. Social proof (number of subscribers, testimonials)
4. Clear privacy assurance
5. Expectation setting (what happens next)

Advanced: Quiz-based lead gen (40-60% completion rates)
→ See forms-ctas.md: Quiz-Based Lead Generation

Service Business (Legal, Medical, Trades)
Priority order:
1. Trust signals (credentials, trust strips)
2. Clear service descriptions
3. Mobile bottom bar CTA (call + book)
4. Social proof (testimonials, reviews)
5. FAQ addressing common concerns
→ See mobile-conversion.md: Mobile Bottom Bar CTA
→ See social-proof-trust.md: Trust Strips and Credential Logos

Enterprise/B2B
Priority order:
1. Credibility (client logos, case studies)
2. Clear problem/solution framing
3. Demo/consultation CTA (not "Buy Now")
4. Security and compliance signals
5. Multiple contact options
6. Detailed documentation accessible

The 80/20 of Conversion

Focus here first for maximum impact:

Headline clarity - 5-second test: does a stranger understand your value?
CTA visibility - Is it obvious what to do next?
Social proof placement - Near decision points, not just at bottom
Mobile experience - Where most traffic comes from
Page speed - Sub-3-second loads
Trust signals - Especially near payment/signup
Resources
psychology-foundations.md - The science behind decisions
funnel-strategy.md - Stage-by-stage optimization
copywriting.md - Words that convert
testing-benchmarks.md - What to test and what's "good"
ethical-boundaries.md - Persuasion vs manipulation
Weekly Installs
20
Repository
rshvr/elite-web-design
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass