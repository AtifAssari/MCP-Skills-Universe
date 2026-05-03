---
title: grill-with-docs
url: https://skills.sh/mattpocock/skills/grill-with-docs
---

# grill-with-docs

skills/mattpocock/skills/grill-with-docs
grill-with-docs
Installation
$ npx skills add https://github.com/mattpocock/skills --skill grill-with-docs
SKILL.md

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.

If a question can be answered by exploring the codebase, explore the codebase instead.

Domain awareness

During codebase exploration, also look for existing documentation:

File structure

Most repos have a single context:

/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/


If a CONTEXT-MAP.md exists at the root, the repo has multiple contexts. The map points to where each one lives:

/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/


Create files lazily — only when you have something to write. If no CONTEXT.md exists, create one when the first term is resolved. If no docs/adr/ exists, create it when the first ADR is needed.

During the session
Challenge against the glossary

When the user uses a term that conflicts with the existing language in CONTEXT.md, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

Update CONTEXT.md inline

When a term is resolved, update CONTEXT.md right there. Don't batch these up — capture them as they happen. Use the format in CONTEXT-FORMAT.md.

Don't couple CONTEXT.md to implementation details. Only include terms that are meaningful to domain experts.

Offer ADRs sparingly

Only offer to create an ADR when all three are true:

Hard to reverse — the cost of changing your mind later is meaningful
Surprising without context — a future reader will wonder "why did they do it this way?"
The result of a real trade-off — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in ADR-FORMAT.md.

Weekly Installs
24.6K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass