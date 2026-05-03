---
rating: ⭐⭐
title: gtm-skills
url: https://skills.sh/arnaudjnn/gtm-skills/gtm-skills
---

# gtm-skills

skills/arnaudjnn/gtm-skills/gtm-skills
gtm-skills
Installation
$ npx skills add https://github.com/arnaudjnn/gtm-skills --skill gtm-skills
SKILL.md
GTM Skills
Overview

Outbound email workflows, buying signal detection, and LinkedIn social intelligence, powered by Bash. Covers the full cold outreach lifecycle (sending campaigns, classifying replies, following up, cleaning bounces, reporting analytics), buying signal detection across Trustpilot reviews, social media growth, and LinkedIn hiring activity, plus LinkedIn tools for profiles, posts, jobs, company research, and messaging.

All tools are called in the Bash tool. Just set the endpoint URL and API key as environment variables.

Sub-Skills
Skill	Description	Use When
setup	Interactive setup wizard	First-time setup, deploying servers, configuring API keys
outbound	Outbound email workflows	Sending emails, campaigns, reply classification, follow-ups, bounce cleanup, analytics
signals	Buying signal detection	Scanning domains for buying signals (Trustpilot reviews, social spikes, LinkedIn hiring)
socials	LinkedIn social intelligence	LinkedIn profiles, posts, jobs, company employees, and messaging
Quick Routing

First time using GTM skills? → setup

Anything related to cold email? → outbound

Looking for buying signals on a domain? → signals

LinkedIn research, posts, or messaging? → socials

Common Setup

Run the setup sub-skill to get started. It walks you through selecting skill groups (Outbound, Signals, Socials, or All), deploying the required servers, configuring API keys as environment variables, and verifying everything works.

Just ask: "Set up GTM skills." or run /setup.

Resources
mailpool.io: Email infrastructure for outbound workflows
outbound-tools: Outbound email server (self-hosted on Railway)
gtm-engine.sh: Admin server for authentication and billing
signals.gtm-engine.sh: Hosted server for buying signal detection
socials.gtm-engine.sh: Hosted server for LinkedIn social intelligence
Weekly Installs
13
Repository
arnaudjnn/gtm-skills
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn