---
title: deep-plan
url: https://skills.sh/idrevnii/perks/deep-plan
---

# deep-plan

skills/idrevnii/perks/deep-plan
deep-plan
Installation
$ npx skills add https://github.com/idrevnii/perks --skill deep-plan
SKILL.md
Deep Plan

Systematic approach for gathering requirements and clarifying decisions before implementation.

When to Activate
User is in PLANNING mode
User explicitly asks to "plan", "discuss", "let's think through", "review approach", "before we start", "what do you think about"
Agent identifies choices between 2+ valid approaches
Agent lacks context needed for confident decision-making
When NOT to Activate
Fixing obvious bugs/typos (clear single correct solution)
User explicitly says "do as you see fit" or similar
Trivial changes with single logical approach
User already provided specific requirements
Clarification Process
1. Context Questions First

Before technical decisions, understand the project context:

Timeline/deadline constraints?
Team size and experience level?
Existing tech stack or constraints?
Scale expectations?

These answers inform all subsequent recommendations.

2. Identify Decision Points

Scan the task and categorize decisions by priority:

🔴 Blocking — cannot proceed without answer
🟡 Important — affects outcome, but has reasonable default
🟢 Nice-to-know — can decide later

Types of decisions:

Technical choices: libraries, tools, patterns, algorithms
Architecture decisions: structure, component breakdown, data flow
Scope boundaries: what's included vs excluded
Priority conflicts: what to implement first
Missing context: unclear requirements, ambiguous terminology
3. Progressive Questioning

Ask questions in phases, starting with most critical:

Phase 1: Context questions + 🔴 Blocking questions (max 5-7 per message) Phase 2: After blocking resolved, ask 🟡 Important questions Phase 3: Ask 🟢 Nice-to-know only when relevant phase begins

Do NOT dump all questions at once. Batch by priority and wait for responses.

4. Question Format with Confidence

Group questions by category, indicate recommendation confidence:

## [Category] Decisions

1. **[Brief description]** 🔴
   - Option A: [description] — **strongly recommend** because [reason]
   - Option B: [description] — better for [use case]

2. **[Another question]** 🟡
   - Option A: [description] — **lean towards** this
   - Option B: [description] — **no strong preference**, depends on [factor]


Confidence levels:

strongly recommend — almost always the right choice
lean towards — good option, but context-dependent
no strong preference — both options are equally valid
5. Handle Unanswered Questions

If user does not answer some questions:

Do NOT assume defaults silently
Explicitly ask: "For questions X and Y, should I proceed with my recommendations, or do you have other preferences?"
Wait for explicit confirmation before proceeding
6. Mid-Execution Re-check

If during implementation agent discovers:

New ambiguity not covered by initial planning
A decision that has multiple valid approaches
Context that contradicts earlier assumptions

→ STOP and return to clarification mode. Do not make assumptions.

7. Decision Summary (Optional)

After all questions resolved, offer to create a decision log:

"Would you like me to save these decisions to the implementation plan for reference?"
Only create if user agrees
Do NOT create files by default
Key Principles
Context before details — understand the big picture first
Ask first, implement after — when in doubt, ask
Progressive disclosure — blocking → important → nice-to-know
Explicit consent — never assume silence means agreement
Stay focused — max 5-7 questions per message
Re-check when uncertain — new ambiguity = new questions
Weekly Installs
21
Repository
idrevnii/perks
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass