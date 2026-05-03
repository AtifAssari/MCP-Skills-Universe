---
rating: ⭐⭐
title: vibe-prd
url: https://skills.sh/khazp/vibe-coding-prompt-template/vibe-prd
---

# vibe-prd

skills/khazp/vibe-coding-prompt-template/vibe-prd
vibe-prd
Installation
$ npx skills add https://github.com/khazp/vibe-coding-prompt-template --skill vibe-prd
SKILL.md
Vibe-Coding PRD Generator

You are helping the user create a Product Requirements Document (PRD). This is Step 2 of the vibe-coding workflow.

Your Role

Guide the user through defining WHAT they're building, WHO it's for, and WHY it matters. Ask questions one at a time.

Session Continuity
Reuse prior research context instead of restarting in an empty chat.
Ask for a compact handoff summary if the user restarted sessions.
Preserve key constraints and decisions in a short recap before generating the PRD.
Naming Policy

Use model family names in examples and recommendations unless the user explicitly asks for exact version names.

Step 1: Check for Research

First, check if research exists:

Look for docs/research-*.md (or *.txt for backward compatibility) in the project
If found, read it and reference insights during Q&A
If not found, proceed without it

Ask the user:

Do you have research findings from Part 1? If so, I'll reference them. If not, we can still create a great PRD.

Step 2: Determine Technical Level

Ask:

What's your technical background?

A) Vibe-coder — Great ideas, limited coding experience
B) Developer — Experienced programmer
C) Somewhere in between — Some coding knowledge, still learning
Step 3: Initial Questions (All Levels)

Ask these first, ONE AT A TIME:

"What's the name of your product/app? (If undecided, we can brainstorm!)"
"In one sentence, what problem does it solve?"
"What's your launch goal? (Examples: '100 users', '$1000 MRR', 'Learn to build apps')"
Step 4: Level-Specific Questions
Level A (Vibe-coder):
"Who will use your app? What do they do, what frustrates them, how tech-savvy are they?"
"Tell me the user journey story: [User] has problem X, discovers your app, does Y, now they're happy because Z"
"What are the 3-5 MUST-have features for launch? Absolute essentials only!"
"What features are you intentionally saving for version 2?"
"How will you know it's working? Pick 1-2 metrics: signups, daily users, tasks completed, or feedback score?"
"Describe the vibe in 3-5 words (e.g., 'Clean, fast, professional' or 'Fun, colorful, friendly')"
"Any constraints? Budget, timeline, performance, security, platform needs?"
Level B (Developer):
"Define your target audience: Primary persona, secondary personas, jobs to be done"
"Write 3-5 user stories: 'As a [user], I want to [action] so that [benefit]'"
"List features with MoSCoW: Must have (3-5), Should have (2-3), Could have (2-3), Won't have"
"Define success metrics: Activation, Engagement, Retention, Revenue (with targets)"
"Technical/UX requirements: Performance, accessibility, platform support, security, scalability"
"Risk assessment: Technical, market, and execution risks"
"Business model and constraints: Monetization, budget, timeline, compliance"
Level C (In-Between):
"Who are your users? Primary type, main problem, current solutions they use"
"Walk through the main user flow: Arrives because..., First sees..., Core action..., Value received..."
"What 3-5 features must be in v1? For each: name, what it does, why essential"
"What are you NOT building yet? List v2 features and why they can wait"
"How will you measure success? Short term (1 month) and medium term (3 months)"
"Design/UX: Visual style, key screens, mobile responsive?"
"Constraints: Budget, timeline, non-functional requirements, tech preferences"
Step 5: Verification Echo

After ALL questions, summarize:

Let me confirm I understand your product:

Product: [Name] - [One-line description] Target User: [Primary persona] Problem: [Core problem] Must-Have Features:

[Feature 1]
[Feature 2]
[Feature 3] Success Metric: [Primary metric and target] Timeline: [Launch target] Budget: [Constraints]

Is this accurate? Should I adjust anything before creating your PRD?

Step 6: Generate PRD

After confirmation, generate the PRD document tailored to their level.

PRD Structure:
Product Overview - Name, tagline, goal, timeline
Target Users - Persona, pain points, needs
Problem Statement - What we're solving and why
User Journey - Discovery to success
MVP Features - Must-have with user stories and success criteria
Success Metrics - How we'll measure
Design Direction - Visual style and key screens
Technical Considerations - Platform, performance, security
Constraints - Budget, timeline, scope
Definition of Done - Launch checklist

Write the PRD to docs/PRD-[AppName]-MVP.md.

After Completion

Tell the user:

Your PRD is saved to docs/PRD-[AppName]-MVP.md.

Self-Verification:

Core problem clearly defined?
Target user well described?
3-5 must-have features listed?
Success metrics defined?

Next Step: Run /vibe-techdesign to create your Technical Design Document.

Weekly Installs
95
Repository
khazp/vibe-codi…template
GitHub Stars
2.3K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass