---
title: nutmeg-review
url: https://skills.sh/withqwerty/nutmeg/nutmeg-review
---

# nutmeg-review

skills/withqwerty/nutmeg/nutmeg-review
nutmeg-review
Installation
$ npx skills add https://github.com/withqwerty/nutmeg --skill nutmeg-review
SKILL.md
Review

Dispatch specialised reviewers to check football data code and visualisations for correctness, convention compliance, and edge cases.

Accuracy

Read and follow docs/accuracy-guardrail.md before answering any question about provider-specific facts.

First: check profile

Read .nutmeg.user.md. If it doesn't exist, tell the user to run /nutmeg first.

Determine scope

Look at what the user wants reviewed. Read the relevant files. Then decide which reviewers to dispatch:

Signal	Dispatch
Code processes football data (fetching, filtering, transforming, computing metrics)	data-reviewer agent
Code renders a chart or visualisation	chart-reviewer agent (Mode 1: Code Review)
User provides a URL or says "check how it looks"	chart-reviewer agent (Mode 2: Visual Inspection)
Chart has filters, tooltips, state, or dynamic data	chart-reviewer agent (Mode 3: Interactive Edge Cases)
Code imports @withqwerty/campos-* (React + campos)	chart-reviewer agent (Mode 4: React + Campos) — pass skills/_shared/campos-bridge.md in context
Code does both data processing AND chart rendering	Both agents in parallel

Always dispatch at least one. If unclear, dispatch both — redundant findings are better than missed issues.

Detection for Mode 4: grep the reviewed files for @withqwerty/campos- or from "@withqwerty/campos. Any match activates Mode 4 alongside Mode 1.

Dispatch

Spawn agents in parallel when dispatching multiple. Each agent receives:

The file paths to review
The user's profile (language, provider, experience level)
Which mode(s) to run (for chart-reviewer)
Context: what the user said they built and what they're worried about
Data reviewer prompt template
Review the football data code in [FILE_PATHS].

The user is working with [PROVIDER] data in [LANGUAGE].
They built: [DESCRIPTION]
Their concern: [WHAT_THEY_SAID]

Follow the full review checklist in your agent prompt. Use search_docs to verify
provider-specific facts (coordinate systems, qualifier IDs, event types).

Chart reviewer prompt template
Review the chart code in [FILE_PATHS].

Mode(s): [Code Review / Visual Inspection / Interactive Edge Cases]
The user is building: [DESCRIPTION]
Their concern: [WHAT_THEY_SAID]
Stack: [LANGUAGE + LIBRARIES from profile]
[If visual inspection: URL or instructions to render]

Load skills/brainstorm/references/chart-canon.md for convention checking.

Synthesise findings

After both agents report back:

Deduplicate — if both flag the same issue (e.g., wrong coordinate system), merge into one finding
Sort by severity — Critical first, then Warning, then Info
Group logically — Data issues, then Rendering issues, then Convention issues, then Edge cases
Present concisely — table format with severity, location, issue, fix
When to suggest visual inspection

If the chart-reviewer's code review finds potential rendering issues but can't confirm without seeing the output, suggest:

"The code review found [N] potential rendering issues. Want me to visually inspect the chart? I'll need a URL or you can run it locally."

Don't require visual inspection — many users can't easily serve their chart locally. Code review alone catches most issues.

After review

If findings are found:

Ask the user which ones to fix
For Critical issues, offer to fix them directly
For Warning/Info, explain the trade-off and let them decide

If no findings:

Say so clearly. Don't invent issues to justify the review.
Optionally mention what was checked so the user knows the review was thorough.
Weekly Installs
37
Repository
withqwerty/nutmeg
GitHub Stars
18
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn