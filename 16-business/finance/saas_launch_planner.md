---
title: saas-launch-planner
url: https://skills.sh/sitechfromgeorgia/georgian-distribution-system/saas-launch-planner
---

# saas-launch-planner

skills/sitechfromgeorgia/georgian-distribution-system/saas-launch-planner
saas-launch-planner
Installation
$ npx skills add https://github.com/sitechfromgeorgia/georgian-distribution-system --skill saas-launch-planner
SKILL.md
SaaS Launch Planner
Purpose

Transform validated ideas into concrete, executable plans for building SaaS products in 3-4 weeks. Ensures subscription-first design, prevents scope creep, and prioritizes shipping fast to validate with paying customers.

Core Principles
Ship Fast, Validate with Paying Users - 3-4 weeks to working product that users can pay for
Subscription-First Mindset - SaaS = recurring revenue, build for retention not just acquisition
No Feature Creep - Only core loop features in MVP, "nice to have" goes post-MVP
Next.js + Supabase + Stripe Optimized - Use proven stack's strengths, don't reinvent
Revenue-Focused Building - Every feature must answer "Who will pay?" and "What problem does this solve?"
Planning Workflow
Phase 1: Problem & Market Definition

Required Information:

Problem: One sentence describing what problem you're solving
Current Solution: How people solve this today (and why it sucks)
Willingness to Pay: Evidence people would pay for better solution
Target Customer: Precise description with pain level (1-10) and budget
Market Size: >10k potential customers minimum

Validation Checklist:

 Talked to 10+ potential customers
 They currently pay for similar solutions
 This is a painkiller (must-have) not vitamin (nice-to-have)
 You can reach customers within budget
 Market size is large enough
Phase 2: Pricing Strategy Selection

Decision Tree:

IF product requires teams → Per-Seat Pricing ($X/user/month)
ELSE IF usage varies greatly → Usage-Based Pricing ($base + $per-use)
ELSE IF clear feature differentiation → Tiered Pricing (Starter/Pro/Enterprise)
ELSE IF need viral growth → Freemium (free + paid)


MVP Recommendation: Tiered Pricing (2-3 tiers maximum)

Standard MVP Pricing:

Starter: $29/month - Core features, single user, email support
Pro: $79/month - All features, multiple users, priority support
Enterprise: Custom - Post-MVP

Trial Strategy:

Recommended: 14-day free trial (no credit card required)
Alternative: 7-day trial (credit card required)
Goal: 10-15% trial-to-paid conversion

See references/PRICING_STRATEGIES.md for complete pricing models and optimization tactics.

Phase 3: Core User Loop Definition

Template:

Discovery & Signup:
1. User lands on landing page → Sees value proposition
2. User starts free trial → Creates account
3. User completes onboarding → First value within 5 minutes

Core Value Loop:
4. User [action 1] → System [response 1]
5. User [action 2] → System [response 2]
→ Value Delivered: [What user achieves]

Subscription Conversion:
7. Trial ending reminder → Upgrade prompt
8. User adds payment → Stripe Checkout
9. Subscription activated → Full access granted
10. User continues using → Retention tracked

Success Metrics:
- Activation: 60%+ users complete key action within 24h
- Conversion: 10-15% trial users become paying
- Retention: 85%+ paid users stay active monthly

Phase 4: MVP Scope Definition

Must Have Criteria:

✅ Essential for core functionality
✅ Users can't get value without it
✅ Can be implemented in 3-5 days
✅ No complex 3rd party integrations
✅ Directly impacts conversion or retention

SaaS-Specific Must Haves:

User authentication (email + social login)
Basic subscription management
Stripe payment integration
Core feature set (2-3 main features only)
User dashboard
Basic settings page

Post-MVP Features (Not Now):

Advanced analytics
Team collaboration
Mobile apps
API access
Integrations (Zapier, Slack)
Custom branding
Advanced automation

Anti-Feature-Creep Rules:

One-Sentence Test: If you can't explain why this feature is essential in one sentence, it doesn't go in MVP
Manual Alternative Test: If this can be done manually for first 100 users, defer it
Value-Per-Day Test: Does value added justify X days of development before having paying customers?
Phase 5: Technical Architecture

Fixed Tech Stack:

Frontend: Next.js 15 (App Router), TypeScript, Tailwind CSS, shadcn/ui
Backend: Next.js API Routes, Supabase (PostgreSQL)
Auth: Supabase Auth (email + OAuth)
Payments: Stripe Checkout + Billing + Webhooks
Email: Resend or SendGrid
Hosting: Vercel + Supabase

Database Tables (Standard):

profiles         -- User profiles (extends auth.users)
customers        -- Stripe customer mapping
subscriptions    -- Subscription status & plan info
[feature_tables] -- Your core feature data


Key API Routes:

POST /api/stripe/create-checkout-session  -- Start subscription
POST /api/stripe/customer-portal          -- Manage subscription
POST /api/webhooks/stripe                 -- Handle Stripe events
GET/POST/PUT/DELETE /api/[resource]      -- Core features


See references/TECHNICAL_ARCHITECTURE.md for complete schemas, app structure, and Stripe integration code.

Phase 6: Development Roadmap

Week 1: Foundation + Core Feature

Days 1-2: Project setup + Authentication
Days 3-5: Core feature implementation (1-2 key features)
Weekend: Testing + polish

Week 2: Payments + Subscription

Days 1-2: Stripe integration (checkout + webhooks)
Days 3-4: Subscription management + billing page
Day 5: Essential features (settings, emails)
Weekend: End-to-end testing

Week 3: Polish + Launch

Days 1-2: Landing page + pricing page
Days 3-4: Final polish (onboarding, error handling, empty states)
Day 5: Deploy + monitor + 🚀 LAUNCH

Week 4: Validation + Iteration (Optional)

Get first users, gather feedback, monitor metrics, quick bug fixes
Output Format - PRD Template

When user requests complete planning, generate PRD using structure from references/PRD_TEMPLATE.md.

Required PRD Sections:

Executive Summary
Problem & Solution
Business Model (with pricing tiers)
Core User Journey
Success Metrics
MVP Scope (Must Have vs Post-MVP)
Technical Architecture
Development Roadmap (week-by-week)
Marketing & Launch Plan
Risk Assessment
Success Criteria
Questions to Ask Before Building

Product Questions:

Who will pay for this? (specific customer segment)
What ONE problem does this solve? (single, clear problem)
How do we measure success? (specific metrics)
Why would they pay monthly? (ongoing value proposition)
What's the alternative? (current solution)
Why switch to us? (key differentiator)

Pricing Questions:

What can customers afford? (price range research)
What are competitors charging? (competitive analysis)
What's our cost per user? (CAC, hosting, support)
How will we handle trials? (credit card required or not)

Scope Questions:

What can be manual initially? (MVP shortcuts)
What features can wait? (post-MVP backlog)
Where's the biggest risk? (technical unknowns)
What's the critical path? (must-have sequence)
Common SaaS Mistakes to Avoid

Top 10 Mistakes:

❌ Building too many features → ✅ Focus on ONE thing
❌ Complex pricing (5+ tiers) → ✅ 2-3 clear tiers
❌ Ignoring churn → ✅ Build retention features day 1
❌ Over-engineering → ✅ Use Next.js + Supabase (proven stack)
❌ Building in isolation → ✅ Share progress, get feedback
❌ Poor trial strategy → ✅ Email sequence + onboarding
❌ Not testing payments → ✅ Test all Stripe scenarios
❌ Ignoring failed payments → ✅ Dunning emails + retry logic
❌ No onboarding → ✅ 3-step onboarding flow
❌ Underpricing → ✅ Match market rates ($29+ minimum)

See references/COMMON_MISTAKES.md for detailed explanations and solutions.

Usage Examples
Basic Request
I want to build a SaaS project management tool for freelancers.

Use saas-launch-planner to create complete PRD with:
- Pricing strategy
- Technical architecture
- 3-week roadmap

Detailed Request
Use saas-launch-planner:

SaaS Idea: AI-powered invoice generator for freelancers
Target: Freelancers earning $50k-$150k annually
Pricing: Tiered (Basic/Pro)
Key Differentiator: AI auto-fills invoice details from past data

Create complete plan including:
- PRD with subscription model
- Next.js + Supabase + Stripe architecture
- Week-by-week development roadmap
- Claude Code starter prompt

Update Existing Plan
We completed Week 1 of the SaaS roadmap.

Use saas-launch-planner to:
- Review progress
- Adjust Week 2 plan based on learnings
- Re-prioritize features if needed

Claude Code Integration

When generating PRD, include optimized Claude Code starter prompt:

## Claude Code Starter Prompt



Create Next.js 15 SaaS application with subscription billing:

Project: [Name] Core Value: [One sentence]

Tech Stack:

Next.js 15 (App Router) + TypeScript
Tailwind CSS + shadcn/ui
Supabase (Auth + Database)
Stripe (Checkout + Billing + Webhooks)

Core Features:

[Feature 1 with acceptance criteria]
[Feature 2 with acceptance criteria]
Stripe subscription integration
User dashboard
Subscription management

Pricing:

Starter: $29/month - [features]
Pro: $79/month - [features]
14-day free trial (no credit card)

Database Schema: [SQL from technical architecture]

Stripe Integration:

Create checkout session for subscription
Handle webhooks (subscription created/updated/deleted)
Customer Portal for self-service
Trial countdown in UI
Access control based on plan

Start with project setup and authentication flow.

Integration with Other Skills

Recommended Workflow:

idea-validator-pro → Validate market demand
saas-launch-planner (this skill) → Create complete PRD
Claude Code → Build the product
Ship in 3-4 weeks 🚀
Key Success Metrics

Week 1 (MVP Launch):

50+ trial signups
10+ activated users
3+ paying customers

Month 1:

200+ trial signups
15+ paying customers ($1,000+ MRR)
10%+ trial-to-paid conversion

Month 3:

600+ trial signups
40+ paying customers ($3,000+ MRR)
12%+ trial-to-paid conversion
<8% monthly churn
Critical Reminders

DO ✅:

Start with pricing model first (it influences architecture)
Talk to customers about pricing before building
Keep pricing simple (2-3 tiers max)
Set up Stripe webhooks early
Test payment flows thoroughly (success + failure)
Implement trial countdown prominently
Monitor trial-to-paid conversion obsessively
Track churn reasons

DON'T ❌:

Build 5+ pricing tiers
Defer billing integration
Forget to test webhook failures
Ignore trial expiration edge cases
Make cancellation hard
Ignore failed payments
Hardcode pricing (use Stripe products)
Skip webhook verification

💡 Key Insight: SaaS success = Build fast, charge early, retain relentlessly. Every decision should optimize for one of these three goals.

🎯 Goal: Not a perfect product, but a profitable one. Not every feature, but the right features. Not someday, but within 3-4 weeks.

🚀 Remember: Your first 10 paying customers teach you more than 1000 hours of planning. Ship, learn, iterate.

Weekly Installs
17
Repository
sitechfromgeorg…n-system
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn