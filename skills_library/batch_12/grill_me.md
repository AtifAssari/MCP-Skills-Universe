---
title: grill-me
url: https://skills.sh/blogic-cz/blogic-marketplace/grill-me
---

# grill-me

skills/blogic-cz/blogic-marketplace/grill-me
grill-me
Installation
$ npx skills add https://github.com/blogic-cz/blogic-marketplace --skill grill-me
SKILL.md

Run a rigorous decision-clarification loop for the user's plan or design.

Use this loop:

Identify open decisions, assumptions, dependencies, and risks.
Prioritize the single highest-leverage unresolved decision (the one most likely to unblock other choices or prevent rework).
Ask one focused question that resolves that decision.
Summarize current understanding, including what is now decided, what remains open, and why the next question matters.
Repeat until exit criteria are met.

Choose evidence source before asking:

Inspect available artifacts (codebase, docs, specs, prior decisions) first when the answer is factual and recoverable from existing information.
Ask the user directly when the answer is preference-, strategy-, risk-tolerance-, or business-priority-dependent.

Separate elicitation from recommendation:

During elicitation, avoid leading phrasing and avoid presenting a preferred answer in the question.
After enough context is collected for a decision, provide a recommendation with rationale, tradeoffs, and explicit assumptions.

Exit criteria:

Stop when all blocker-level decisions are resolved and remaining open items are low impact or explicitly deferred.
Stop when the user confirms sufficient clarity to proceed.
If unresolved blockers remain, end with a concise blocker list and the minimum next questions needed.
Weekly Installs
9
Repository
blogic-cz/blogi…ketplace
GitHub Stars
3
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass