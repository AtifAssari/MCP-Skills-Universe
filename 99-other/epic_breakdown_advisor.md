---
rating: ⭐⭐⭐
title: epic-breakdown-advisor
url: https://skills.sh/deanpeters/product-manager-skills/epic-breakdown-advisor
---

# epic-breakdown-advisor

skills/deanpeters/product-manager-skills/epic-breakdown-advisor
epic-breakdown-advisor
Installation
$ npx skills add https://github.com/deanpeters/product-manager-skills --skill epic-breakdown-advisor
Summary

Break down large epics into vertical-slice user stories using Humanizing Work's 9 splitting patterns.

Guides product managers through sequential pattern application (workflow steps, CRUD operations, business rules, data variations, UI methods, major effort, simple/complex, performance deferral, and spikes) to identify which pattern fits
Validates epics against INVEST criteria before splitting to ensure stories are independent, negotiable, valuable, estimable, and testable
Generates equal-sized, end-to-end user stories that preserve vertical value rather than creating horizontal technical slices
Evaluates splits to reveal low-value work worth eliminating or deprioritizing, turning vague feature blobs into sprint-ready stories
SKILL.md
Purpose

Guide product managers through breaking down epics into user stories using Richard Lawrence's complete Humanizing Work methodology—a systematic, flowchart-driven approach that applies 9 splitting patterns sequentially. Use this to identify which pattern applies, split while preserving user value, and evaluate splits based on what they reveal about low-value work you can eliminate. This ensures vertical slicing (end-to-end value) rather than horizontal slicing (technical layers).

This is not arbitrary slicing—it's a proven, methodical process that starts with validation, walks through patterns in order, and evaluates results strategically.

Key Concepts
Core Principles: Vertical Slices Preserve Value

A user story is "a description of a change in system behavior from the perspective of a user." Splitting must maintain vertical slices—work that touches multiple architectural layers and delivers observable user value—not horizontal slices addressing single components (e.g., "front-end story" + "back-end story").

The Three-Step Process
Pre-Split Validation: Check if story satisfies INVEST criteria (except "Small")
Apply Splitting Patterns: Work through 9 patterns sequentially until one fits
Evaluate Splits: Choose the split that reveals low-value work or produces equal-sized stories
The 9 Splitting Patterns (In Order)
Workflow Steps — Thin end-to-end slices, not step-by-step
Operations (CRUD) — Create, Read, Update, Delete as separate stories
Business Rule Variations — Different rules = different stories
Data Variations — Different data types/structures
Data Entry Methods — Simple UI first, fancy UI later
Major Effort — "Implement one + add remaining"
Simple/Complex — Core simplest version first, variations later
Defer Performance — "Make it work" before "make it fast"
Break Out a Spike — Time-box investigation when uncertainty blocks splitting
Meta-Pattern (Applies Across All Patterns)
Identify the core complexity
List all variations
Reduce variations to one complete slice
Make other variations separate stories
Why This Works
Prevents arbitrary splitting: Methodical checklist prevents guessing
Preserves user value: Every story delivers observable value
Reveals waste: Good splits expose low-value work you can deprioritize
Repeatable: Apply to any epic consistently
Facilitation Source of Truth

Use workshop-facilitation as the default interaction protocol for this skill.

It defines:

session heads-up + entry mode (Guided, Context dump, Best guess)
one-question turns with plain-language prompts
progress labels (for example, Context Qx/8 and Scoring Qx/5)
interruption handling and pause/resume behavior
numbered recommendations at decision points
quick-select numbered response options for regular questions (include Other (specify) when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

Application
Step 0: Provide Epic Context

Agent asks:

Please share your epic:

Epic title/ID
Description or hypothesis
Acceptance criteria (especially multiple "When/Then" pairs)
Target persona
Rough estimate

You can paste from Jira, Linear, or describe briefly.

Step 1: Pre-Split Validation (INVEST Check)

Before splitting, verify your story satisfies INVEST criteria (except "Small"):

Agent asks questions sequentially:

1. Independent? "Can this story be prioritized and developed without hard technical dependencies on other stories?"

Options:

Yes — No blocking dependencies
No — Requires other work first (flag this)

2. Negotiable? "Does this story leave room for the team to discover implementation details collaboratively, rather than prescribing exact solutions?"

Options:

Yes — It's a conversation starter, not a spec
No — It's too prescriptive (may need reframing)

3. Valuable? "Does this story deliver observable value to a user? (If not, combine it with related work rather than splitting.)"

Options:

Yes — Users see/experience something different
No — It's a technical task (not a user story—don't split, reframe)

⚠️ Critical Check: If story fails "Valuable," STOP. Don't split. Instead, combine with other work to create a meaningful increment.

4. Estimable? "Can your team size this story relatively (even if roughly)?"

Options:

Yes — Team can estimate days/points
No — Too much uncertainty (may need spike first)

5. Testable? "Does this story have concrete acceptance criteria that QA can verify?"

Options:

Yes — Clear pass/fail conditions
No — Needs clearer acceptance criteria (refine before splitting)

If story passes all checks → Proceed to Step 2 (Splitting Patterns) If story fails any check → Fix the issue before splitting

Step 2: Apply Splitting Patterns Sequentially

Work through patterns in order. For each pattern, ask "Does this apply?"

Pattern 1: Workflow Steps

Key insight: Split into thin end-to-end slices, not step-by-step. Start with a simple case covering the full workflow, then add intermediate steps as separate stories.

Agent asks: "Does your epic involve a multi-step workflow where you could deliver a simple case first, then add intermediate steps later?"

Example:

Original: "Publish content (requires editorial review, legal approval, staging)"
❌ Wrong split (step-by-step): Story 1 = Editorial review, Story 2 = Legal approval, Story 3 = Publish
✅ Right split (thin end-to-end):
Story 1: Publish content (simple path: author uploads, content goes live immediately—no reviews)
Story 2: Add editorial review step (now content waits for editor approval before going live)
Story 3: Add legal approval step (content waits for legal + editorial before going live)

Each story delivers full workflow, just with increasing sophistication.

Options:

Yes, multi-step workflow → "Describe the workflow steps"
No, single step → Continue to Pattern 2

If YES: Agent generates thin end-to-end slice splits.

Pattern 2: Operations (CRUD)

Key insight: The word "manage" signals multiple operations. Split into Create, Read, Update, Delete.

Agent asks: "Does your epic use words like 'manage,' 'handle,' or 'maintain'? If so, it likely bundles multiple operations (CRUD)."

Example:

Original: "Manage user accounts"
Split:
Story 1: Create user account
Story 2: View user account details
Story 3: Edit user account info
Story 4: Delete user account

Options:

Yes, contains multiple operations → "List the operations (Create/Read/Update/Delete/etc.)"
No, single operation → Continue to Pattern 3

If YES: Agent generates one story per operation.

Pattern 3: Business Rule Variations

Key insight: When identical functionality operates under different rules, each rule becomes its own story.

Agent asks: "Does your epic have different business rules for different scenarios (user types, regions, tiers, conditions)?"

Example:

Original: "Flight search with flexible dates (date range, specific weekends, date offsets)"
Split:
Story 1: Search by date range (+/- N days)
Story 2: Search by specific weekends only
Story 3: Search by date offsets (N days before/after)

Options:

Yes, different rules → "Describe the rule variations"
No, same rules for all → Continue to Pattern 4

If YES: Agent generates one story per rule variation.

Pattern 4: Data Variations

Key insight: Complexity from handling different data types or structures. Add variations just-in-time as needed.

Agent asks: "Does your epic handle different data types, formats, or structures (e.g., file types, geographic levels, user attributes)?"

Example:

Original: "Geographic search (counties, cities/towns/neighborhoods, custom provider areas)"
Split:
Story 1: Search by county
Story 2: Add city/town/neighborhood search
Story 3: Add custom provider area search

Options:

Yes, different data types → "List the data variations"
No, single data type → Continue to Pattern 5

If YES: Agent generates one story per data variation (deliver simplest first).

Pattern 5: Data Entry Methods

Key insight: UI complexity independent of core functionality. Build simplest interface first, then add sophisticated UI as follow-ups.

Agent asks: "Does your epic include fancy UI elements (date pickers, autocomplete, drag-and-drop) that aren't essential to core functionality?"

Example:

Original: "Search with calendar date picker"
Split:
Story 1: Search by date (basic text input: "YYYY-MM-DD")
Story 2: Add visual calendar picker UI

Options:

Yes, fancy UI elements → "Describe the UI enhancements"
No, basic UI only → Continue to Pattern 6

If YES: Agent generates Story 1 = basic input, Story 2+ = UI enhancements.

Pattern 6: Major Effort

Key insight: When initial implementation carries most complexity, with additions being trivial. Frame as "implement one + add remaining."

Agent asks: "Does your epic involve building infrastructure where the first implementation is hard, but adding more is easy?"

Example:

Original: "Accept credit card payments (Visa, Mastercard, Amex, Discover)"
Split:
Story 1: Accept Visa payments (build full payment infrastructure)
Story 2: Add Mastercard, Amex, Discover support (trivial additions)

⚠️ Note: First story does the heavy lift (payment gateway, security, compliance). Subsequent stories are small additions.

Options:

Yes, major effort pattern → "What's the first implementation + what are the additions?"
No, no infrastructure work → Continue to Pattern 7

If YES: Agent generates Story 1 = build infrastructure, Story 2 = add remaining variants.

Pattern 7: Simple/Complex

Key insight: Identify story's core by asking "What's the simplest version?" Extract variations into separate stories.

Agent asks: "What's the simplest version of this epic that still delivers value? Can you strip away complexity and add it back later?"

Example:

Original: "Flight search (with max stops, nearby airports, flexible dates)"
Split:
Story 1: Basic flight search (origin, destination, date)
Story 2: Add max stops filter
Story 3: Add nearby airports option
Story 4: Add flexible dates option

Options:

Yes, can identify simplest core → "Describe the simplest version + what variations to defer"
No, it's already simple → Continue to Pattern 8

If YES: Agent generates Story 1 = simplest core, Story 2+ = variations.

Pattern 8: Defer Performance

Key insight: Split "make it work" from "make it fast." Non-functional requirements (performance, security, scalability) can follow functional delivery.

Agent asks: "Can you deliver functional value first, then optimize performance/security/scalability later?"

Example:

Original: "Real-time search with <100ms response time"
Split:
Story 1: Search works (functional, no performance guarantee)
Story 2: Optimize search to <100ms (add caching, indexing)

Options:

Yes, can defer optimization → "What's the functional version + what's the optimization?"
No, performance is essential → Continue to Pattern 9

If YES: Agent generates Story 1 = functional, Story 2 = optimize.

Pattern 9: Break Out a Spike

Key insight: Last resort when uncertainty prevents splitting. Time-box investigation to answer specific questions, then split implementation story with better understanding.

Agent says: "None of patterns 1-8 apply, which suggests high uncertainty. Before splitting, run a spike to reduce uncertainty."

A spike is a time-boxed investigation (not a story), answering questions like:

Is this technically feasible?
Which approach performs best?
What does the API actually return?

Agent asks: "What's the biggest unknown preventing you from splitting this epic?"

Options:

Technical feasibility — "Can we build this with our stack?"
Approach uncertainty — "Multiple ways to solve it, unclear which is best"
External dependency — "Don't know what third-party API provides"

Agent recommends: → "Run a 1-2 day spike to answer [question]. After the spike, come back and we'll split the epic with better understanding."

⚠️ Spikes produce learning, not shippable code. After the spike, restart at Pattern 1.

Step 3: Evaluate Split Quality

After splitting, evaluate using these criteria:

Agent asks:

1. Does this split reveal low-value work you can deprioritize or eliminate?

Good splits expose the 80/20 principle: most value concentrates in a small portion of functionality
Example: After splitting "Flight search" into 4 stories, you realize "flexible dates" is rarely used → deprioritize or kill it

2. Does this split produce more equally-sized stories?

Equal-sized stories give Product Owners greater prioritization flexibility
Example: Instead of one 10-day epic, five 2-day stories allow reordering mid-sprint

If split doesn't satisfy either criterion, try a different pattern.

Meta-Pattern Application

Across all patterns, follow this sequence:

Identify core complexity — What makes this epic hard?
List variations — What are all the different ways/cases/rules?
Reduce to one complete slice — Pick the simplest variation that still delivers end-to-end value
Make other variations separate stories
Cynefin Domain Considerations

Strategy shifts based on complexity domain:

Agent asks: "How much uncertainty surrounds this epic?"

Options:

Low uncertainty (Obvious/Complicated domain) — "We know what to build; it's just engineering work" → Find all stories, prioritize by value/risk

High uncertainty (Complex domain) — "We're not sure what customers want or what will work" → Identify 1-2 learning stories; avoid exhaustive enumeration (work itself teaches what matters)

Chaos — "Everything is on fire; priorities shift daily" → Defer splitting until stability emerges; focus on stabilization first

Output: Generate Story Breakdown
# Epic Breakdown Plan

**Epic:** [Original epic]
**Pre-Split Validation:** ✅ Passes INVEST (except Small)
**Splitting Pattern Applied:** [Pattern name]
**Rationale:** [Why this pattern fits]

---

## Story Breakdown

### Story 1: [Title] (Simplest Complete Slice)

**Summary:** [User-value-focused title]

**Use Case:**
- **As a** [persona]
- **I want to** [action]
- **so that** [outcome]

**Acceptance Criteria:**
- **Given:** [Preconditions]
- **When:** [Action]
- **Then:** [Outcome]

**Why This First:** [Delivers core value; simpler variations follow]
**Estimated Effort:** [Days/points]

---

### Story 2: [Title] (First Variation)

[Repeat...]

---

### Story 3: [Title] (Second Variation)

[Repeat...]

---

## Split Evaluation

✅ **Does this split reveal low-value work?**
- [Analysis: Which stories could be deprioritized/eliminated?]

✅ **Does this split produce equal-sized stories?**
- [Analysis: Are stories roughly equal in effort?]

---

## INVEST Validation (Each Story)

✅ **Independent:** Stories can be developed in any order
✅ **Negotiable:** Implementation details can be discovered collaboratively
✅ **Valuable:** Each story delivers observable user value
✅ **Estimable:** Team can size each story
✅ **Small:** Each story fits in 1-5 days
✅ **Testable:** Clear acceptance criteria for each

---

## Next Steps

1. **Review with team:** Do PM, design, engineering agree?
2. **Check for further splitting:** Are any stories still >5 days? If yes, **restart at Pattern 1** for that story.
3. **Prioritize:** Which story delivers most value first?
4. **Consider eliminating:** Did split reveal low-value stories? Kill or defer them.

---

**If stories are still too large, re-apply patterns starting at Pattern 1.**

Examples
Example 1: Pattern 1 Applied (Workflow Steps - Thin End-to-End)

Epic: "Publish blog post (requires editorial review, legal approval, staging)"

Pre-Split Validation: ✅ Passes INVEST

Pattern 1: "Does this have workflow steps?" → YES ✅

❌ Wrong Split (Step-by-Step):

Editorial review story
Legal approval story
Publish story → Problem: Story 1 doesn't deliver value (users see nothing)

✅ Right Split (Thin End-to-End):

Publish post (simple path) — Author uploads, post goes live immediately (no reviews)
Add editorial review — Post now waits for editor approval before going live
Add legal approval — Post waits for legal + editorial before going live

Why this works: Each story delivers full workflow, just with increasing sophistication.

Example 2: Pattern 2 Applied (CRUD Operations)

Epic: "Manage user profiles"

Pattern 2: "Does this say 'manage'?" → YES ✅ (signals CRUD)

Split:

Create user profile
View user profile details
Edit user profile info
Delete user profile

Split Evaluation:

✅ Reveals low-value work: After analysis, "Delete profile" is rarely used → deprioritize
✅ Equal-sized stories: Each 1-2 days
Example 3: Pattern 7 Applied (Simple/Complex)

Epic: "Flight search with max stops, nearby airports, flexible dates"

Pattern 7: "What's the simplest version?" → Basic search ✅

Split:

Basic flight search (origin, destination, date) — Core value
Add max stops filter — Enhancement
Add nearby airports option — Enhancement
Add flexible dates option — Enhancement

Split Evaluation:

✅ Reveals low-value work: User research shows "flexible dates" rarely used → kill or defer
✅ Equal-sized stories: Story 1 = 3 days, others = 1 day each
Example 4: Iterative Splitting (Multiple Patterns)

Epic: "Checkout flow with discounts (member, VIP, first-time) and payment (Visa, Mastercard, Amex)"

First Pass - Pattern 1 (Workflow): YES ✅

Story 1: Add items to cart
Story 2: Apply discount
Story 3: Complete payment

Check Story 2 ("Apply discount"): Still 4 days → Too large, re-split

Second Pass on Story 2 - Pattern 3 (Business Rules): YES ✅

Story 2a: Apply member discount (10%)
Story 2b: Apply VIP discount (20%)
Story 2c: Apply first-time discount (5%)

Check Story 3 ("Complete payment"): Still 5 days → Too large, re-split

Third Pass on Story 3 - Pattern 6 (Major Effort): YES ✅

Story 3a: Accept Visa payments (build payment infrastructure)
Story 3b: Add Mastercard, Amex support

Final Breakdown: 6 stories, all 1-2 days each

Common Pitfalls
Pitfall 1: Skipping Pre-Split Validation

Symptom: Jump straight to splitting without checking INVEST

Consequence: Split a story that shouldn't be split (e.g., not Valuable = technical task)

Fix: Always run Step 1 (INVEST check) before Step 2 (splitting patterns)

Pitfall 2: Step-by-Step Workflow Splitting (Pattern 1 Done Wrong)

Symptom: Story 1 = "Editorial review," Story 2 = "Legal approval"

Consequence: Stories don't deliver end-to-end value

Fix: Each story should cover full workflow (thin end-to-end slice), just with increasing sophistication

Pitfall 3: Horizontal Slicing (Technical Layers)

Symptom: "Story 1: Build API. Story 2: Build UI."

Consequence: Neither story delivers user value

Fix: Vertical slicing—each story includes front-end + back-end to deliver observable user behavior

Pitfall 4: Forcing a Pattern That Doesn't Fit

Symptom: "We'll split by workflow even though there's no sequence"

Consequence: Arbitrary, meaningless split

Fix: If pattern doesn't apply, say NO and continue to next pattern

Pitfall 5: Not Re-Splitting Large Stories

Symptom: Split epic into 3 stories, but each is still 5+ days

Consequence: Stories too large for sprint

Fix: Restart at Pattern 1 for each large story until all are 1-5 days

Pitfall 6: Ignoring Split Evaluation (Step 3)

Symptom: Split but don't evaluate if it reveals low-value work

Consequence: Miss opportunity to eliminate waste

Fix: After splitting, ask: "Does this reveal work we can kill or defer?"

Practice & Skill Development

Humanizing Work recommendation: Teams reach fluency in 2.5-3 hours across multiple practice sessions.

Practice approach:

Analyze recently completed features (hindsight makes patterns obvious)
Walk completed work through the flowchart — Which pattern would have applied?
Find multiple split approaches for each feature
Build shared vocabulary of domain-specific pattern examples

Don't skip practice work. Skill develops through analyzing past deliverables, not just refining future work.

References
Related Skills
user-story-splitting.md — The 9 patterns in detail
user-story.md — Format for writing stories
epic-hypothesis.md — Original epic format
External Frameworks
Richard Lawrence & Peter Green, The Humanizing Work Guide to Splitting User Stories — Complete methodology
Bill Wake, INVEST in Good Stories (2003) — Quality criteria
Sources
https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/

Skill type: Interactive Suggested filename: epic-breakdown-advisor.md Suggested placement: /skills/interactive/ Dependencies: Uses user-story-splitting.md, user-story.md, epic-hypothesis.md

Weekly Installs
836
Repository
deanpeters/prod…r-skills
GitHub Stars
3.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass