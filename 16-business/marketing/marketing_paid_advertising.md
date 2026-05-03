---
title: marketing-paid-advertising
url: https://skills.sh/vasilyu1983/ai-agents-public/marketing-paid-advertising
---

# marketing-paid-advertising

skills/vasilyu1983/ai-agents-public/marketing-paid-advertising
marketing-paid-advertising
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill marketing-paid-advertising
SKILL.md
PAID ADVERTISING — ACQUISITION OS (OPERATIONAL)

No-fluff execution skill for paid acquisition across Google, Meta, TikTok, LinkedIn.

References: Google Ads, Meta Business, TikTok Ads, LinkedIn Campaign Manager

Modern Best Practices (January 2026)
Algorithmic buying wins when you provide strong signals: clean conversion events, value, and enough volume per campaign to learn.
Creative is the main lever on social: plan for volume and refresh cadence; treat creative like a product pipeline.
Default measurement: server-side signals where possible (Enhanced Conversions / Conversions API / Events API), consistent UTMs, and closed-loop revenue in CRM.
Use attribution as directional; use incrementality tests to answer budget questions (geo-lift/holdouts) when stakes are high.
Optimize to profit and payback (not just CPL/ROAS) when margins, refunds, or LTV vary materially.
Compliance is non-negotiable: platform policies, privacy consent, and avoiding sensitive targeting/claims.
When to Use
New campaigns: structure, audiences, bidding, creative
Scaling spend: budget allocation, ROAS targets
Platform selection: which channels for which goals
Unit economics: CAC/LTV modeling, payback period
Revenue attribution: multi-touch, incrementality
When NOT to Use
Scenario	Use Instead
Organic social	marketing-social-media
SEO/content	marketing-seo-complete
Landing pages	marketing-cro
Quick Start (What I Need From You)
Goal: revenue, pipeline, leads, trials, purchases (pick 1 primary)
ICP/offer: who, pain, positioning, price/ACV, gross margin, refund rate (if relevant)
Geo/language + budget horizon (test budget + monthly cap)
Tracking: conversion events + where they’re recorded (GA4, CRM, Shopify, app DB), attribution window expectations
Constraints: creative/brand limits, compliance constraints, sales capacity + SLAs (B2B)

If unknown, start with assumptions and label them; then validate with data in week 1.

Platform Selection
Platform	Best For	Typical Cost (Relative)
Google Search	High intent capture	Medium
Meta	Efficient demand creation + retargeting	Low–Medium
LinkedIn	B2B precision, ABM	High
TikTok	Low-cost reach + creative velocity	Low

Note: Costs vary massively by industry, geo, offer, tracking quality, and seasonality. Use as directional only.

Decision Tree
HIGH INTENT?
├─ YES → Google Search (always include)
└─ NO → What's your goal?
    ├─ Awareness → Meta, TikTok, YouTube
    ├─ B2B/Enterprise → LinkedIn, Google
    └─ E-commerce → Meta, Google Shopping

Measurement & Tracking (2026 Default)

Minimum viable measurement before scaling:

Conversion events defined (lead, SQL, purchase, subscription) with dedupe and clear “source of truth”
UTMs standardized across every platform
Server-side signals where feasible:
Google: Enhanced Conversions + offline conversion imports (B2B)
Meta: Pixel + Conversions API
TikTok: Pixel + Events API
LinkedIn: Insight Tag + offline conversions (when available)
Reporting views: spend → conversions → revenue/pipeline (weekly), incrementality tests (quarterly or when budgets materially change)

For deep dives: references/revenue-attribution-guide.md, references/sales-alignment-guide.md.

Campaign Structure
Google Ads
├─ Campaign: Brand (Search)
├─ Campaign: Non-Brand (Search)
├─ Campaign: Retargeting (Display)
└─ Campaign: Performance Max

Meta Ads
├─ Campaign: Prospecting
│   ├─ Ad Set: Lookalike 1%
│   └─ Ad Set: Broad (Advantage+)
├─ Campaign: Retargeting
└─ Campaign: Testing

Bidding Strategy
Strategy	When to Use
Manual CPC	<50 conversions/month
Target CPA	50-100 conversions
Target ROAS	>100 conversions
Budget Allocation
Stage	% of Budget
Brand	10-20%
Prospecting	40-60%
Retargeting	20-30%
Testing	10-15%
Unit Economics
LTV:CAC	Status	Action
< 1:1	Losing money	Stop spending
3:1	Healthy	Maintain/scale
> 5:1	Under-investing	Scale aggressively

Payback Targets:

B2C SaaS: < 6 months
B2B SaaS: < 12 months
E-commerce: < 3 months
Decision Tree (Triage)
CPL too high?
├─ Check audience size
├─ Check creative CTR (<1% = new creative)
├─ Check landing page CVR (<2% = landing issue)
└─ Check bid strategy

ROAS below target?
├─ Check conversion tracking
├─ Check audience quality
└─ Check offer strength

Metrics
Metric	Target
CTR	>1% (creative health)
CVR	>2% (landing health)
Frequency	<3 (fatigue)
Quality Score	>6 (Google)
Anti-Patterns
Changing bids daily → Wait 2-4 weeks
Too many audiences → Use 3-5 max
Single creative → Use 3-5 variants
No negative keywords → Build weekly
Resources
Resource	Purpose
data/sources.json	Authoritative sources (platform docs, measurement, privacy)
references/google-ads-guide.md	Google specifics
references/meta-ads-guide.md	Meta specifics
references/tiktok-ads-guide.md	TikTok specifics
references/linkedin-ads-guide.md	LinkedIn specifics
references/unit-economics-guide.md	CAC/LTV deep dive
references/revenue-attribution-guide.md	Attribution models
references/sales-alignment-guide.md	Pipeline + CRM alignment
references/operational-sops.md	Weekly/monthly SOPs
references/programmatic-display.md	Programmatic buying, DSPs, DOOH
references/remarketing-retargeting.md	Retargeting strategy + windows
references/youtube-ads-guide.md	YouTube + Shorts specifics
references/creative-testing-ads.md	Creative testing methodology
references/privacy-cookieless-ads.md	Privacy-first advertising
references/amazon-ads-guide.md	Amazon Sponsored Products/Brands/Display, DSP
references/microsoft-ads-guide.md	Bing/Microsoft Ads, LinkedIn targeting, Copilot
Templates
Template	Purpose
assets/campaign-structure.md	Campaign hierarchy
assets/budget-allocation.md	Budget planning
assets/unit-economics-calculator.md	CAC/LTV calculator
assets/creative-brief.md	Ad creative spec
assets/google-rsa-asset-pack.md	RSA copy + asset pack
assets/creative-test-plan.md	Creative testing cadence
assets/performance-review.md	Weekly/monthly review doc
International Markets

This skill covers US-centric platforms. For regional advertising:

Need	See Skill
China platforms (Baidu, WeChat, Douyin)	marketing-geo-localization
Japan/Korea (Yahoo Japan, Naver, Kakao)	marketing-geo-localization
Russia/CIS (Yandex, VK)	marketing-geo-localization
Regional CAC benchmarks	marketing-geo-localization

Tip: If your query mentions regional platforms or specific countries, also use marketing-geo-localization.

Related Skills
Skill	Purpose
marketing-geo-localization	International markets
marketing-leads-generation	Lead capture
marketing-cro	Landing optimization
startup-go-to-market	Channel strategy
Weekly Installs
102
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass