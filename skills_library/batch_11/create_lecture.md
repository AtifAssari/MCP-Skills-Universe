---
title: create-lecture
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/create-lecture
---

# create-lecture

skills/pedrohcgs/claude-code-my-workflow/create-lecture
create-lecture
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill create-lecture
SKILL.md
Lecture Creation Workflow

Create a beautiful, pedagogically excellent Beamer lecture deck.

This is a collaborative, iterative process. The instructor drives the vision; Claude is a thinking partner.

CONSTRAINTS (Non-Negotiable)
Read the knowledge base FIRST — notation registry, narrative arc, applications database
Every new symbol MUST be checked against the notation registry
Motivation before formalism — no exceptions
Worked example within 2 slides of every definition
Max 2 colored boxes per slide
No \pause or overlay commands (check project rules)
Transition slides at major conceptual pivots
Thread at least 1 running empirical application throughout
All citations verified against the bibliography
Work in batches of 5-10 slides — share for feedback, don't bulk-dump
WORKFLOW
Phase 0: Intake & Context (Pre-Flight Report required)

Read the inputs, then produce a Pre-Flight Report in your response before Phase 1 starts.

Inputs to read:

.claude/rules/knowledge-base-template.md — notation registry, narrative arc, applications
.claude/rules/content-invariants.md — INV-1..INV-8 govern slide content
Any source papers / existing slides the user provided
The previous lecture's .tex (last section + ending slide) if one exists

Required Pre-Flight Report block:

## Pre-Flight Report

**Sources read:**
- [source 1]: [one-line takeaway — what notation, what result, what diagram]
- [source 2]: ...

**Notation registry check:**
- New symbols this lecture will introduce: [list]
- Symbols reused from prior lectures: [list, with the lecture each was introduced in]
- Conflicts detected: [none / specific clashes]

**Narrative position:** [Where does this lecture sit in the course arc? What did the previous lecture end on? What does the next lecture need you to set up?]

**Pedagogical goal:** [one sentence]

**Running application:** [which real-world example threads through this deck]


State the pedagogical goal, get user confirmation, then proceed.

First-lecture fallback (fresh fork, empty knowledge base). If .claude/rules/knowledge-base-template.md still has unfilled placeholder tables (no notation registry entries, no applications, no prior lectures in Slides/), do NOT halt waiting for it. Instead:

Acknowledge the template is empty and we're creating the course's first lecture.
Propose a minimal starter knowledge base from the user's topic: 5-8 key symbols with conventions, 1-2 running applications, a short narrative arc (intro → main idea → implications). Present for approval.
Write the approved stub into the knowledge base template so subsequent lectures inherit it.
Continue to Phase 1.

This prevents /create-lecture from deadlocking for every new forker.

Phase 1: Paper Analysis (When Papers Provided)
Split into chunks, extract key ideas
Map paper notation → course notation
Identify slide-worthy content
Present summary for approval
Phase 2: Structure Proposal
Propose outline (5-Act or 3-Part template)
List TikZ diagrams and R figures needed
List new notation to introduce
GATE: User approves before Phase 3
Phase 3: Draft Slides (Iterative)
Work in batches of 5-10 slides
Check notation, apply creation patterns
Quality checks during drafting
Phase 4: Figures & Code
R scripts following conventions
TikZ diagrams in Beamer source (single source of truth)
Save RDS for future Quarto integration
Phase 5: Polish & Compile
Full 3-pass compilation
Run Devil's Advocate
Run Substance Review (if domain reviewer configured)
Update knowledge base with new notation
Post-Creation Checklist
[ ] Lecture compiles without errors
[ ] No overfull hbox > 10pt
[ ] All citations resolve
[ ] Every definition has motivation + worked example
[ ] Max 2 colored boxes per slide
[ ] 2-3 Socratic questions embedded
[ ] Transition slides between sections
[ ] At least 1 running application threaded throughout
[ ] New notation added to knowledge base
[ ] Session log updated
[ ] Devil's Advocate run

Weekly Installs
22
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass