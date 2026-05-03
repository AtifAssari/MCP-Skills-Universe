---
title: tech-planner
url: https://skills.sh/jkappers/agent-skills/tech-planner
---

# tech-planner

skills/jkappers/agent-skills/tech-planner
tech-planner
Installation
$ npx skills add https://github.com/jkappers/agent-skills --skill tech-planner
SKILL.md
Technical Planning

Create technical overviews and Architecture Decision Records (ADRs) that document HOW a feature is built — architecture, integration, and decisions.

Workflow
Read the spec — Load the spec from the argument path. If no path is provided, ask the user for the spec location.
Analyze architecture — Evaluate the analysis questions below against the spec.
Create technical overview — Write specs/feature-name/tech.md using assets/tech.md.
Determine if ADR(s) are needed — Apply the decision criteria below. Skip if no ADR is warranted.
Create ADR(s) — Write docs/adr/NNN-title.md using assets/adr-template.md. Scan existing ADRs for the highest number, increment by one, and pad to 3 digits.
Architectural Analysis

Evaluate these questions for every technical plan:

What existing systems does this touch?
Where does this feature start and end?
How does it connect to existing components?
How does data flow through the system?
What are we gaining and giving up?
When to Create an ADR

Create an ADR when the decision:

Chooses between competing technologies or frameworks
Sets a project-wide pattern or convention
Selects an authentication or authorization approach
Introduces a trade-off with long-term implications
Is difficult or expensive to reverse
When NOT to Create an ADR

Skip the ADR when the decision:

Affects only a single feature (document in the feature spec instead)
Covers implementation details within one component
Describes a temporary workaround or experiment

See references/adr-guide.md for extended ADR guidance, status lifecycle, and content guidelines.

Constraints
Never include specific file paths, implementation order, code snippets, line-by-line details, time estimates, or timeline references in technical overviews or ADRs.
Keep technical overviews focused on architecture boundaries, data flow, and integration — not implementation steps.
Assets
assets/tech-template.md — Technical overview template
assets/adr-template.md — ADR template
references/adr-guide.md — Extended ADR guidance
Weekly Installs
10
Repository
jkappers/agent-skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass