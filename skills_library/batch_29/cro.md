---
title: cro
url: https://skills.sh/phrazzld/claude-config/cro
---

# cro

skills/phrazzld/claude-config/cro
cro
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill cro
SKILL.md
Conversion Rate Optimization

Orchestrates conversion optimization across the user journey.

Routing

Identify the conversion context and load appropriate patterns:

Context	Reference	Triggers
Marketing pages, landing pages, pricing	references/page-patterns.md	"page not converting", "improve landing page"
Forms (non-signup)	references/form-patterns.md	"form friction", "contact form", "lead capture"
Signup/registration	references/signup-patterns.md	"signup dropoff", "registration friction"
Post-signup onboarding	references/onboarding-patterns.md	"activation rate", "first-run experience"
Paywalls, upgrade screens	references/paywall-patterns.md	"convert free to paid", "upgrade modal"
Popups, modals, banners	references/popup-patterns.md	"exit intent", "email popup"
Workflow
Identify stage: Which part of the funnel?
Load patterns: Read relevant reference file
Assess current state: What exists today?
Apply framework: Use patterns for analysis
Output recommendations: Prioritized by impact
Common Cross-Cutting Concerns
Mobile Optimization
Touch targets 44px+
Appropriate keyboard types
Single-column layouts
Sticky CTAs
Trust Signals
Social proof near conversion points
Privacy assurances
Security badges where relevant
Clear expectations
Friction Reduction
Minimize required fields
Smart defaults
Progressive disclosure
Clear error handling
Measurement

For any CRO work, ensure tracking:

Funnel step completion rates
Drop-off points
Field-level analytics for forms
Device/source segmentation
Output Format
Quick Wins

Changes implementable same-day with high confidence.

High-Impact Changes

Bigger changes requiring more effort but significant improvement.

Test Hypotheses

Ideas worth A/B testing rather than assuming.

Expert Panel Review (MANDATORY)

Before returning CRO recommendations, run expert panel review on proposed changes.

See: ui-skills/references/expert-panel-review.md

Have 10 advertorial experts score the optimizations 0-100
Each provides specific improvement feedback
If average < 90: Iterate on recommendations
Only return when 90+ average achieved

Key reviewers for CRO:

Laja - Conversion optimization
Wiebe - CTA and form copy
Wroblewski - Mobile and form UX
Cialdini - Persuasion psychology
Related Skills
ab-test-setup - For testing changes
analytics-tracking - For measuring impact
copywriting - For copy rewrites
Weekly Installs
25
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass