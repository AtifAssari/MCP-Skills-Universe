---
title: proofread
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/proofread
---

# proofread

skills/pedrohcgs/claude-code-my-workflow/proofread
proofread
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill proofread
SKILL.md
Proofread Lecture Files

Run the mandatory proofreading protocol on lecture files. This produces a report of all issues found WITHOUT editing any source files.

Steps

Identify files to review:

If $ARGUMENTS is a specific filename: review that file only
If $ARGUMENTS is "all": review all lecture files in Slides/ and Quarto/

For each file, launch the proofreader agent that checks for:

GRAMMAR: Subject-verb agreement, articles (a/an/the), prepositions, tense consistency TYPOS: Misspellings, search-and-replace artifacts, duplicated words OVERFLOW: Overfull hbox (LaTeX), content exceeding slide boundaries (Quarto) CONSISTENCY: Citation format, notation, terminology ACADEMIC QUALITY: Informal language, missing words, awkward constructions

Produce a detailed report for each file listing every finding with:

Location (line number or slide title)
Current text (what's wrong)
Proposed fix (what it should be)
Category and severity

Save each report to quality_reports/:

For .tex files: quality_reports/FILENAME_report.md
For .qmd files: quality_reports/FILENAME_qmd_report.md

IMPORTANT: Do NOT edit any source files. Only produce the report. Fixes are applied separately after user review.

Present summary to the user:

Total issues found per file
Breakdown by category
Most critical issues highlighted
Weekly Installs
21
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass