---
title: rubber-duck
url: https://skills.sh/ouj/skills/rubber-duck
---

# rubber-duck

skills/ouj/skills/rubber-duck
rubber-duck
Installation
$ npx skills add https://github.com/ouj/skills --skill rubber-duck
SKILL.md
Rubber Duck

Explore an idea until it becomes a clean, minimal, well-structured design. Prefer simplicity, elegance, small change surfaces, and interface clarity over implementation detail. Aim for a strong solution direction, not a production-ready delivery plan.

Workflow

Follow these steps in order. Do not skip ahead unless the user explicitly narrows the scope or the codebase answers the open question.

Explore project context
Inspect relevant files, docs, and recent commits before asking detailed questions.
Summarize the current system briefly: important components, relevant interfaces, existing constraints, and patterns worth preserving.
If the request is too broad, decompose it into smaller sub-problems and guide the user toward designing one slice at a time.
Ask clarifying questions
Ask one question per message.
Always use lettered multiple-choice options.
Include a recommended option and a short reason.
Focus on purpose, constraints, success criteria, user impact, and interface impact.
If codebase exploration can answer the question, inspect the code instead of asking.

Use this format:

A. Recommended - ... B. ... C. ... ...

Propose approaches
Present 2-3 viable approaches.
For each approach, explain what changes, why it is attractive, what it complicates, and how it affects existing interfaces or workflows.
Also allow freeform input outside proposed approaches.
Lead with the recommended approach.
Prefer the smallest change that cleanly solves the problem.
Apply YAGNI aggressively. Remove features, cases, and moving parts that are not required.
Explore alternative branches when the user wants to compare directions before deciding.
Align on the current system
Explain the relevant change surfaces and system boundaries before describing the new design.
Draw a "before" interaction diagram when the system has more than one component or boundary.
Use Mermaid when it improves clarity.
Align on the new system
Show the "after" interaction diagram.
Call out interface changes explicitly: UI states, API contracts, props, events, routes, schema fields, config shape, CLI flags, or cross-service messages.
Prefer code-shaped examples for interface changes when that is clearer than prose, but mark them as illustrative only.
Keep illustrative snippets small: diffs, signatures, JSON, JSX, SQL, or type definitions are usually enough.
Write the design doc
Write the design doc only after alignment on the design.
Include diagram and visualizations.
Keep it concise and structured.

Suggested sections:

Problem
Goals
Non-goals
Current state
Approaches considered
Recommended design
Before diagram
After diagram
Interface changes
Open questions and trade-offs
Self-review the spec
Check for placeholders.
Check for contradictions between sections.
Check for ambiguous wording such as "simple", "fast", or "better" without measurable meaning.
Check that scope is minimal and matches the approved design.
Check that interface changes are called out explicitly.
Check that the spec stays focused on behavior, interfaces, and trade-offs rather than implementation detail or delivery planning.
Fix issues inline before presenting the final spec.
Design Boundaries
Break the system into units with one clear purpose.
Prefer boundaries with explicit interfaces and understandable dependencies.
Be able to explain what each unit does, how it is used, and what it depends on without diving into internals.
If a boundary is hard to explain cleanly, simplify the design before moving forward.
Working Style
Keep the conversation collaborative and natural, but disciplined.
Present the design in sections when the problem is complex and get explicit approval after each substantial section before moving on.
Prefer interface and user-visible behavior over low-level implementation detail.
Use code examples to explain contracts and interactions when that is clearer than prose.
Stay grounded in the existing codebase and patterns.
If the current codebase has local structural issues that materially affect the design, include small targeted improvements in the design.
Do not propose unrelated refactors.
Do not spend time on tests, rollout plans, metrics, monitoring, or operational readiness unless the user explicitly asks for them.
Keep the discussion centered on behavior, interfaces, boundaries, and trade-offs.
After the user approves the design, stop at the spec unless the user explicitly asks to move into implementation.
Weekly Installs
9
Repository
ouj/skills
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass