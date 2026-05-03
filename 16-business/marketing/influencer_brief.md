---
title: influencer-brief
url: https://skills.sh/indranilbanerjee/digital-marketing-pro/influencer-brief
---

# influencer-brief

skills/indranilbanerjee/digital-marketing-pro/influencer-brief
influencer-brief
Installation
$ npx skills add https://github.com/indranilbanerjee/digital-marketing-pro --skill influencer-brief
SKILL.md
/dm:influencer-brief
Purpose

Create a complete influencer campaign brief that covers creator discovery criteria, content guidelines, compliance requirements, compensation framework, and performance measurement.

Input Required

The user must provide (or will be prompted for):

Campaign objective: Awareness, engagement, conversions, content generation, or event promotion
Product/service: What the influencer will promote
Target audience: Who the campaign should reach
Platform(s): Instagram, TikTok, YouTube, X, LinkedIn, podcasts
Budget: Total influencer budget or per-creator range
Creator tier: Nano (1-10K), Micro (10-100K), Mid (100K-500K), Macro (500K-1M), Mega (1M+)
Timeline: Campaign dates and content delivery deadlines
Content type: Posts, stories, reels, videos, reviews, unboxing, tutorials, live streams
Process
Load brand context: Read ~/.claude-marketing/brands/_active-brand.json for the active slug, then load ~/.claude-marketing/brands/{slug}/profile.json. Apply brand voice, compliance rules for target markets (skills/context-engine/compliance-rules.md), and industry context. Also check for guidelines at ~/.claude-marketing/brands/{slug}/guidelines/_manifest.json — if present, load restrictions and relevant category files. Check for custom templates at ~/.claude-marketing/brands/{slug}/templates/. Check for agency SOPs at ~/.claude-marketing/sops/. If no brand exists, ask: "Set up a brand first (/dm:brand-setup)?" — or proceed with defaults.
Define creator discovery criteria: niche, audience demographics, engagement rate minimums, brand safety filters, aesthetic alignment
Build the creator brief: campaign overview, key messages, creative freedom boundaries, required and prohibited elements, hashtags, disclosures
Draft compensation framework: flat fee, performance bonus, affiliate commission, product gifting, or hybrid
Create content approval workflow: draft review, revision rounds, posting timeline
Build FTC/ASA compliance checklist: disclosure requirements, claim restrictions, platform-specific rules
Define usage rights: organic only, paid amplification, repurposing, duration
Set measurement framework: reach, engagement, clicks, conversions, CPE, EMV
Output

A structured influencer campaign brief containing:

Campaign overview with objectives and success metrics
Creator discovery criteria and ideal profile description
Creator brief document (shareable with influencers)
Key messaging framework with creative guardrails
Compensation structure and negotiation guidelines
Content approval and revision process
FTC/ASA compliance checklist with required disclosures
Usage rights and licensing terms
Measurement dashboard with KPIs and reporting cadence
Agents Used
influencer-manager — Creator strategy, brief development, compliance, measurement, campaign architecture
Weekly Installs
28
Repository
indranilbanerje…ting-pro
GitHub Stars
71
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass