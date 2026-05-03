---
rating: ⭐⭐
title: pedagogy-review
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/pedagogy-review
---

# pedagogy-review

skills/pedrohcgs/claude-code-my-workflow/pedagogy-review
pedagogy-review
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill pedagogy-review
SKILL.md
Pedagogical Review of Lecture Slides

Perform a comprehensive pedagogical review.

Steps

Identify the file specified in $ARGUMENTS

If no argument, ask user which lecture to review
If just a name, look in Quarto/ or Slides/

Launch the pedagogy-reviewer agent with the full file path

The agent checks 13 pedagogical patterns
Performs deck-level analysis (narrative arc, pacing, visual rhythm, notation)
Considers student perspective (prerequisites, objections)

The agent produces a report saved to: quality_reports/[FILENAME_WITHOUT_EXT]_pedagogy_report.md

Present summary to user:

Patterns followed vs violated (out of 13)
Deck-level assessments
Critical recommendations (top 3-5)
Important Notes
This is a read-only review — no files are edited
Focuses on pedagogy not visual layout (use /visual-audit for that)
For a combined review, use /slide-excellence instead
Weekly Installs
19
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