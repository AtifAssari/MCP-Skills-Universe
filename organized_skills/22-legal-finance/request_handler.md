---
rating: ⭐⭐
title: request-handler
url: https://skills.sh/duck4nh/antigravity-kit/request-handler
---

# request-handler

skills/duck4nh/antigravity-kit/request-handler
request-handler
Installation
$ npx skills add https://github.com/duck4nh/antigravity-kit --skill request-handler
SKILL.md
Request Handler Workflow

When receiving a user request, follow this process:

Step 1: Classify the Task

Identify which of the 4 categories the request belongs to:

Icon	Type	Keywords to Detect
CONSULT	"should", "recommend", "compare", "suggest", "advice"	
BUILD	"create", "make", "build", "add", "implement", "write"	
DEBUG	"error", "bug", "not working", "wrong", "fix"	
OPTIMIZE	"slow", "refactor", "clean", "improve", "optimize"	

Note: If unclear → Ask the user before proceeding.

Step 2: Execute Based on Mode
CONSULT Mode
Clarify context & constraints
Provide 2-3 options with clear trade-offs
Recommend the optimal option with reasoning
WAIT for confirmation before coding
BUILD Mode
Confirm scope & acceptance criteria
Propose file/component structure
Code in order: Types → Logic/Hooks → UI → Styles
Run checklist before delivery
DEBUG Mode
Gather info: what, where, when
Analyze root cause
Propose fix + explanation
Suggest prevention measures
OPTIMIZE Mode
Measure baseline
Identify main bottlenecks
Propose improvements + predict results
Refactor + compare before/after
Step 3: Pre-Delivery Checklist

Code Quality:

 No any types
 No hardcoded magic numbers/strings
 Proper error handling
 Clear variable/function naming

Structure:

 Correct folder structure
 Consistent naming convention
 Split files appropriately (< 200 lines/file)

UI/UX (if applicable):

 Follows Design System
 Responsive, mobile-first
 Loading/Error/Empty states
Tips
Don't expand scope unilaterally
Don't use any types
Ask when requirements are unclear
Comment complex logic
Prioritize: Readability → Performance → Cleverness
Weekly Installs
9
Repository
duck4nh/antigravity-kit
GitHub Stars
16
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass