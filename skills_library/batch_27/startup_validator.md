---
title: startup-validator
url: https://skills.sh/alpoxdev/hypercore/startup-validator
---

# startup-validator

skills/alpoxdev/hypercore/startup-validator
startup-validator
Installation
$ npx skills add https://github.com/alpoxdev/hypercore --skill startup-validator
SKILL.md

@rules/evidence-and-scoring.md @references/frameworks.md

Startup Validator

Score startup ideas with explicit evidence and uncertainty instead of optimism. Organize results as a multi-file folder for future reference.

<when_to_use>

Use this skill when:

validating a new startup or product idea
deciding whether to proceed, pivot, or narrow the market
preparing for customer discovery or fundraising conversations

Do not use this skill when:

the main job is generating many new ideas
the request is technical implementation planning
the user wants first-principles redesign rather than validation scoring

Boundary:

use genius-thinking for broad ideation
use elon-musk for assumption teardown and redesign

Examples:

/startup-validator AI-based education service
/startup-validator subscription healthcare app
/startup-validator B2B purchasing automation


</when_to_use>

<input_check>

If $ARGUMENTS is missing, ask:

Which startup idea should we validate?

If founder, market, or customer evidence is missing, continue with explicit assumptions instead of inventing certainty.

</input_check>

<owned_job>

For each run:

Restate the idea and identify the key unknowns.
Score the idea using the framework set in references/frameworks.md.
Mark evidence quality and uncertainty for each major claim.
Summarize the strongest strengths, critical weaknesses, and next validation steps.

</owned_job>

<document_shape>

Output Structure
.hypercore/startup-validator/[topic-slug]/
├── flow.json           # phase tracking
├── thesis.md           # idea framing + key hypotheses
├── thiel-scores.md     # per-question rationale and scores
├── pmf-forces.md       # PMF checklist + Forces of Progress
└── verdict.md          # final score + grade + weaknesses + roadmap

Use ASCII kebab-case for [topic-slug] (e.g., ai-education-service).
Each phase produces its own file for organized reference.
flow.json tracks progress through phases. See references/flow-schema.md for the schema.
If the folder exists from a prior run, read existing files before updating.

</document_shape>

<flow_tracking>

Flow Tracking

Write flow.json at the start and update as each phase completes.

Phase progression
Phase	Output file	Next
frame	thesis.md — idea thesis + 3 key hypotheses	score
score	thiel-scores.md — 7 questions with per-question rationale	pmf
pmf	pmf-forces.md — PMF checklist + Forces of Progress analysis	verdict
verdict	verdict.md — total score, grade, weaknesses, roadmap	done
Resume support

If flow.json already exists, read it and continue from the last incomplete phase. Do not restart completed phases.

</flow_tracking>

Workflow
Phase	Task	Output file
1	Frame the idea and missing context	thesis.md
2	Score the Thiel questions	thiel-scores.md
3	Check PMF and switching forces	pmf-forces.md
4	Apply penalties, summarize, recommend next actions	verdict.md

Scoring rule:

do not fabricate precise scores when evidence is thin
mark uncertain sections as provisional and explain what evidence would change them

<output_contract>

Each output file should follow the formats defined in the KO version's result_structure section:

thesis.md: one-line thesis, value hypothesis, growth hypothesis, key unknowns
thiel-scores.md: per-question score + rationale + improvement direction
pmf-forces.md: PMF checklist, Forces of Progress (Push/Pull/Habit/Anxiety), switching probability
verdict.md: total score/grade, critical weaknesses with severity, improvement roadmap (immediate/30d/90d)

</output_contract>

Before finishing, check:

unsupported certainty is called out as provisional
evidence quality is distinguished from opinion
the score ties back to named frameworks
the output includes concrete next validation actions
all output files are saved under .hypercore/startup-validator/[topic-slug]/
flow.json status is set to completed
Weekly Installs
31
Repository
alpoxdev/hypercore
GitHub Stars
3
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass