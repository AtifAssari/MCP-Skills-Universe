---
rating: ⭐⭐⭐
title: specdriven
url: https://skills.sh/vasylrakivnenko/specdriven/specdriven
---

# specdriven

skills/vasylrakivnenko/specdriven/specdriven
specdriven
Installation
$ npx skills add https://github.com/vasylrakivnenko/specdriven --skill specdriven
SKILL.md
specdriven

A deliberately small, three-phase scaffold for building software with AI coding agents — designed for people who would rather describe their idea than write a technical spec. No constitution document, no clarification phase, no ceremony. Just three plain-English artifacts the agent reads on every turn.

If you (the agent) need to know whether to invoke this skill, see When to use below. Otherwise, the rest of this file is the playbook.

When to use this skill

Invoke when:

The user describes a new project ("I want to make…", "I'm thinking about building…")
The user wants a new feature on an existing project but acceptance is fuzzy
The user explicitly says "concept", "roadmap", "feature", "spec", "plan", "what should I build first?"
The user lists a wish-list and you can't tell what to build first

Do not invoke when:

The task is small and scoped ("rename this variable", "fix this typo", "why isn't this loop terminating?")
A specdriven/ folder already exists and the user is in the middle of building a specific feature — just consult the existing artifacts and keep working
The three phases
  ┌────────────┐     ┌────────────┐     ┌────────────┐
  │  CONCEPT   │ ──▶ │  ROADMAP   │ ──▶ │  FEATURES  │
  │  the why   │     │  the path  │     │  the work  │
  └────────────┘     └────────────┘     └────────────┘
   concept.md         roadmap.md         features/NN-name.md


Each phase produces ONE markdown artifact under a top-level specdriven/ folder in the user's project:

<user-project>/
└── specdriven/
    ├── concept.md
    ├── roadmap.md
    └── features/
        ├── 01-sign-up.md
        ├── 02-create-post.md
        └── 03-share-link.md


These artifacts are the contract between the user and the agent. Read them on every turn. If the user says something that contradicts them, surface the contradiction before acting.

Phase 1 — Concept

Goal: capture what the user wants to build, who it's for, and what done looks like — in plain English, on one page.

How to run it:

Read whatever the user just said. If anything is fuzzy, ask 3–5 short clarifying questions. Keep it light — a numbered list works, or one at a time, whichever the user prefers.
Pull the answers into the concept.md template below. If something is genuinely unknown after asking, write ? in that slot. Never invent requirements.
Show the filled draft. Ask for fixes. Save to specdriven/concept.md.

concept.md template:

# Concept: <one-line title>

**Elevator pitch.** <one or two sentences a non-technical friend would understand>

**Who's it for.** <who the user is — be specific>

**The problem.** <what's broken or missing today>

**Done looks like.** <3–5 bullets describing success>
- ...
- ...
- ...

**Ground rules.** <non-negotiables: e.g. "must work on phone", "no login", "free to host">
- ...

**Out of scope.** <tempting additions we will NOT do in v1>
- ...

**Open questions.** <things to flag — never invent>
- ?


Anti-patterns:

✗ Don't write a 5-page spec. One page, max.
✗ Don't propose a tech stack here — that's roadmap territory.
✗ Don't list features here — that's roadmap territory.
✗ Don't ask 20 questions. 3–5 short ones.

When the concept is saved and the user approves, move to Roadmap.

Phase 2 — Roadmap

Goal: turn the concept into an ordered list of features that, built one by one, deliver the concept.

How to run it:

Re-read specdriven/concept.md. Every feature in the roadmap must map to at least one bullet under "Done looks like".
Propose 4–10 features. Each gets a name, a one-line "why", and a rough size (S / M / L). Order them so the user has something usable as early as possible — skateboard before car, not wheels before chassis.
Note dependencies in plain English ("needs sign-up done first").
Show the proposal. Let the user reorder, drop, or add. Save to specdriven/roadmap.md.

roadmap.md template:

# Roadmap

Built in this order so we have something usable as early as possible.

## 1. <feature name> — S
**Why.** <one line tied to a "Done looks like" bullet from concept.md>
**Depends on.** none
**Status.** ☐ not started

## 2. <feature name> — M
**Why.** ...
**Depends on.** #1
**Status.** ☐ not started

## 3. <feature name> — S
**Why.** ...
**Depends on.** #1
**Status.** ☐ not started

...


Sizing guide (rough — not hours):

S — one sitting, one file or two, no new concepts
M — a few sittings, multiple files, maybe a new library
L — week or more, new architectural piece. If something feels L, try to split it.

Anti-patterns:

✗ More than 10 features in v1. If there are more, this is really two roadmaps; pick one.
✗ Sequencing by easiest-first instead of "what makes the thing usable soonest".
✗ Putting "research X" or "figure out the database" as a feature. Either it's a real feature or it's an open question on concept.md.

When the roadmap is saved and approved, move to Features.

Phase 3 — Features

Goal: pick the next feature off the roadmap, expand it just enough to build it well, then build it.

How to run it:

Look at specdriven/roadmap.md. The next feature is the lowest-numbered one whose dependencies are done.
Create specdriven/features/NN-feature-name.md from the template below. Fill it in with your best understanding; flag any open questions.
Show the feature card to the user. If they approve, build it. If they push back, revise the card first — do not argue while coding.
After building:
Tick the acceptance checks you actually verified (ran the code, clicked the flow). Untested boxes stay unticked.
Mark this feature ☑ done in roadmap.md.
Ask the user whether to move to the next feature.

features/NN-name.md template:

# Feature N — <name>

From: roadmap.md item #N

**What it does.** <1–2 sentences in user terms>

**User flow.**
1. User does X
2. System responds with Y
3. ...

**Acceptance checks.** <what must be true for this to count as done>
- [ ] ...
- [ ] ...
- [ ] ...

**Tech notes.** <specific choices: library, file layout, API. Brief.>
- ...

**Open questions.** <flag, don't invent>
- ?


Rules of thumb:

A feature card is half a page, not three pages.
Acceptance checks must be testable by clicking around or running one command. "Works well" is not a check; "user lands on /home after sign-in" is.
If building reveals a missing feature, don't silently bolt it onto this card — open a new card and update the roadmap.
If building reveals the concept was wrong, stop and update concept.md first. The artifacts are a contract; do not drift.
Working agreement (cross-cutting rules)

These apply across all three phases:

Read the artifacts every turn. concept.md and roadmap.md are the source of truth. If a request contradicts them, surface the contradiction before acting.
Plain English wins. No jargon unless the user used it first. Say "who's it for", not "ICP". Say "first usable version", not "MVP scaffolding". Say "what done looks like", not "acceptance criteria for the user story".
One page per artifact. If a doc sprawls, scope was split wrong.
Flag, don't invent. If something is unknown, write ? and ask. Never fabricate requirements to fill a gap.
Tick boxes truthfully. Only mark an acceptance check ☑ if you actually verified it. If you couldn't test (e.g. no browser available), say so explicitly — don't claim success.
Keep the roadmap honest. When a feature ships, mark it ☑ done in roadmap.md so the next session has accurate state.
Small features beat big ones. If a feature card grows past 7 acceptance checks, split it.
Quick start (when you, the agent, walk in fresh)

State machine:

What you see in the user's project	What to do
No specdriven/ folder	Ask the user: "Want me to set this up — describe what you're building, and I'll draft the concept page, then we'll plan the roadmap together." On yes, run Phase 1.
specdriven/concept.md exists, no roadmap.md	Read concept.md, run Phase 2.
Both exist, user wants to build	Run Phase 3 on the next undone feature.
User asks something unrelated mid-feature	Answer it, then offer to return to the feature.
User contradicts an existing artifact	Surface the contradiction, ask whether to update the artifact, do not silently drift.
What this skill is NOT
Not a project manager. No time tracking, no assignees, no dates.
Not a design tool. It captures what, not how the UI looks.
Not a replacement for your judgment when coding. Once a feature card is approved, you (the agent) pick the implementation.
Not opinionated about tech stack. The roadmap can note choices; this skill doesn't dictate them.
Not a heavy methodology. For an engineer-grade flow with constitutions, dependency graphs, and cross-artifact analyzers, see GitHub's spec-kit. specdriven is the friendly cousin.
Why these three phases (and only three)

GitHub's spec-kit ships seven phases (Constitution, Specify, Clarify, Plan, Tasks, Analyze, Implement). That's the right shape for engineering teams; it's too much friction for a hobbyist building a side project on Replit.

specdriven folds the seven into three:

spec-kit phase	specdriven home
Constitution	One paragraph inside Concept's "Ground rules"
Specify	Concept
Clarify	The 3–5 questions during Concept
Plan	Roadmap (with tech notes inline)
Tasks	Features (each card is a small task list)
Analyze	Done implicitly: every feature reads concept + roadmap
Implement	Build step at the end of each Feature card

Three phases is the smallest scaffold that still forces clarity. Anything fewer collapses back into vibe-coding.

Weekly Installs
6
Repository
vasylrakivnenko…ecdriven
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass