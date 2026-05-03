---
rating: ⭐⭐
title: trial conversion drafter
url: https://skills.sh/sixtysecondsapp/use60/trial-conversion-drafter
---

# trial conversion drafter

skills/sixtysecondsapp/use60/Trial Conversion Drafter
Trial Conversion Drafter
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Trial Conversion Drafter'
SKILL.md
Available Context & Tools

@_platform-references/org-variables.md @_platform-references/capabilities.md

Trial Conversion Drafter
Goal

Generate stage-appropriate trial conversion emails at two critical trigger points: Day 7 (check-in with usage insights and adoption help) and Day 12 (conversion push with ROI summary and pricing reminder). The tone shifts from supportive at Day 7 to urgency-balanced at Day 12. Both emails focus on value realization, not pressure tactics.

Why Trial Conversion Timing Matters

Trial conversion is a high-stakes, time-sensitive process where timing and messaging quality directly impact conversion rates:

Trial conversion rates peak at 18-23% for well-executed SaaS trials (ProfitWell trial conversion benchmarks, 2024).
Day 7 check-ins increase conversion rates by 31% by surfacing blockers before they compound (Intercom Product Engagement Study).
82% of trial users who experience a clear "aha moment" in the first 7 days convert, vs. 12% for those who don't (OpenView SaaS Benchmarks).
Day 12 conversion emails have 2.7x higher reply rates than day 14 emails — urgency matters, but not desperation (Lavender Email Intelligence data).
Two-Stage Trial Conversion Cadence
Day 7: Check-In, Usage Insights, Adoption Help

Purpose: Ensure the trial user is on the path to value realization and surface any blockers.

Tone: Supportive, helpful, adoption-focused. "We're here to make sure you succeed."

Key Content:

Acknowledge progress (features explored, usage activity)
Share usage insights (what they've done, what they haven't yet tried)
Offer specific help (training, onboarding call, resource sharing)
Highlight the "aha moment" feature or use case they should explore
No pricing or conversion pressure — pure value focus

CTA: "Would a 15-minute call to walk through [high-value feature] be helpful this week?"

Day 12: Conversion Push, ROI Summary, Pricing Reminder

Purpose: Drive a conversion decision by quantifying value delivered and introducing urgency.

Tone: Consultative urgency, ROI-focused, decision-driving. "Here's what you've accomplished — let's make this permanent."

Key Content:

Recap value delivered during trial (quantified metrics: time saved, tasks completed, wins achieved)
ROI summary (project 30/60/90 day value if they continue)
Pricing reminder with conversion offer (discount, extended trial, flexible terms)
Urgency framing (trial ending, limited-time offer, or internal decision deadline)
Clear conversion CTA (schedule pricing call, sign contract, extend trial)

CTA: "Let's schedule a 20-minute call this week to discuss pricing and next steps. Would Thursday at 2pm or Friday at 10am work?"

Output Contract

Return a SkillResult with:

data.email_draft: object with subject, body, sections, tone, trial_stage
data.usage_summary: object with engagement_level, features_activated, usage_volume, aha_moment_reached
data.conversion_incentive (Day 12 only): object with incentive_type, details, expiration, value_estimate
data.roi_summary (Day 12 only): object with time_saved_monthly, cost_avoidance_monthly, roi projections
data.next_steps: array of 2-3 action items with owner and deadline
Weekly Installs
–
Repository
sixtysecondsapp/use60
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass