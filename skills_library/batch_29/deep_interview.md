---
title: deep-interview
url: https://skills.sh/aviz85/claude-skills-library/deep-interview
---

# deep-interview

skills/aviz85/claude-skills-library/deep-interview
deep-interview
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill deep-interview
SKILL.md
Deep Interview

Conduct adaptive interviews that progressively extract knowledge and build organized knowledge bases in real-time.

Core Loop
ASK -> LISTEN -> WRITE -> DEEPEN -> REPEAT


Each cycle: ask targeted questions, capture answers into files, identify gaps, go deeper. The knowledge base grows with every answer.

Process
1. Initialize

Parse the topic from user input. Determine output path:

If --output <path> provided: use that path
If inside a project with CLAUDE.md: use project root or relevant subfolder
Default: create ~/Documents/interviews/<topic>-<date>/

Create the output directory and an _interview-index.md file:

# Interview: <Topic>
**Date:** <today>
**Status:** In Progress
**Depth:** <shallow|medium|deep>

## Themes Discovered
(updated as interview progresses)

## Files Created
(updated as files are written)

2. Opening Round - Broad Context

Use AskUserQuestion to understand the landscape. Ask 2-3 broad questions max per call.

First call - establish scope and the interviewee's relationship to the topic:

What is this topic about? (if unclear)
What is the user's role/expertise level?
What's the goal of capturing this knowledge?

IMPORTANT: After EACH AskUserQuestion response, immediately write what was learned to a file before asking more questions. Never accumulate more than one round of answers without writing.

3. Adaptive Deepening

Based on answers, identify themes (3-7 major areas). For each theme:

Create a file: <theme-slug>.md
Ask 2-4 targeted questions about that theme using AskUserQuestion
Write answers into the theme file
If a theme is complex enough, create a subfolder: <theme-slug>/ and split into sub-files

Question strategy per depth:

Depth	Questions per theme	Total rounds	Output size
shallow	2-3	3-5	5-10 files
medium	4-6	6-10	10-20 files
deep	8-12	12-20	20-40 files

Default depth: medium.

4. Question Techniques

Vary question types to extract different knowledge layers:

What questions: facts, definitions, components
How questions: processes, workflows, methods
Why questions: reasoning, philosophy, decisions
When/Where questions: context, triggers, conditions
Who questions: stakeholders, audiences, roles
What if questions: edge cases, exceptions, failures
Rank/Priority questions: force prioritization ("pick top 3")
Contrast questions: "how is X different from Y?"

Tip: Use the options field in AskUserQuestion to suggest concrete answers when possible - this makes it easier for the user and surfaces assumptions to validate.

5. Writing Rules

File naming: kebab-case, descriptive. e.g., target-audience.md, pricing-strategy.md, session-1-agenda.md

File format:

# <Theme Title>

> Source: Deep Interview, <date>

## Key Points
- Point extracted from answer
- Another point

## Details
<Expanded content from follow-up questions>

## Open Questions
- Things that still need clarification


Folder creation trigger: When a theme has 3+ sub-themes, create a folder:

output/
├── _interview-index.md
├── overview.md
├── simple-theme.md
└── complex-theme/
    ├── _index.md
    ├── sub-topic-1.md
    └── sub-topic-2.md

6. Progress Tracking

After every 3 rounds of questions, show the user a brief status:

**Interview Progress:**
- Themes covered: X/Y
- Files created: N
- Current focus: <theme>
- Estimated remaining: ~Z more rounds

7. Synthesis & Closing

When all themes are covered (or user signals done):

Update _interview-index.md with final table of contents
Create _summary.md - a concise synthesis of everything learned
Identify and list gaps in _open-questions.md
Tell user: total files created, folder structure, and suggested next steps
AskUserQuestion Best Practices
Max 2-3 questions per call (don't overwhelm)
Always provide concrete options when possible (user can still type "Other")
Use multiSelect: true for "which of these apply?" questions
Keep headers short (max 12 chars) - they show as chips/tags
Phrase options as clear, distinct choices - not vague
After receiving answers, acknowledge briefly before writing + asking more
If user gives short answers, ask follow-ups. If detailed, move on.
Anti-Patterns
Don't ask 10 questions at once - max 3-4 per AskUserQuestion call
Don't wait until the end to write files - write incrementally
Don't ask yes/no questions when open-ended would yield more
Don't repeat questions the user already answered
Don't assume knowledge - always verify with the user
Don't create empty placeholder files - only write when there's real content
Weekly Installs
21
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass