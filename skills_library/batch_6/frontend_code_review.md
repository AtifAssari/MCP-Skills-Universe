---
title: frontend-code-review
url: https://skills.sh/langgenius/dify/frontend-code-review
---

# frontend-code-review

skills/langgenius/dify/frontend-code-review
frontend-code-review
Installation
$ npx skills add https://github.com/langgenius/dify --skill frontend-code-review
Summary

Automated frontend code review against a multi-category checklist, supporting both pending-change and targeted file reviews.

Triggers on user requests to review frontend files (.tsx, .ts, .js) and applies a canonical checklist across Code Quality, Performance, and Business Logic categories
Supports two review modes: pending-change review for staged/working-tree files before commit, and file-targeted review for specific named files
Flags violations with urgency metadata (Urgent vs. Suggestion) and groups findings by severity, then by category for prioritized remediation
Outputs structured reviews with file paths, line numbers, code snippets, and suggested fixes; prompts user to apply fixes if issues are found
SKILL.md
Frontend Code Review
Intent

Use this skill whenever the user asks to review frontend code (especially .tsx, .ts, or .js files). Support two review modes:

Pending-change review – inspect staged/working-tree files slated for commit and flag checklist violations before submission.
File-targeted review – review the specific file(s) the user names and report the relevant checklist findings.

Stick to the checklist below for every applicable file and mode.

Checklist

See references/code-quality.md, references/performance.md, references/business-logic.md for the living checklist split by category—treat it as the canonical set of rules to follow.

Flag each rule violation with urgency metadata so future reviewers can prioritize fixes.

Review Process
Open the relevant component/module. Gather lines that relate to class names, React Flow hooks, prop memoization, and styling.
For each rule in the review point, note where the code deviates and capture a representative snippet.
Compose the review section per the template below. Group violations first by Urgent flag, then by category order (Code Quality, Performance, Business Logic).
Required output

When invoked, the response must exactly follow one of the two templates:

Template A (any findings)
# Code review
Found <N> urgent issues need to be fixed:

## 1 <brief description of bug>
FilePath: <path> line <line>
<relevant code snippet or pointer>


### Suggested fix
<brief description of suggested fix>

---
... (repeat for each urgent issue) ...

Found <M> suggestions for improvement:

## 1 <brief description of suggestion>
FilePath: <path> line <line>
<relevant code snippet or pointer>


### Suggested fix
<brief description of suggested fix>

---

... (repeat for each suggestion) ...


If there are no urgent issues, omit that section. If there are no suggestions, omit that section.

If the issue number is more than 10, summarize as "10+ urgent issues" or "10+ suggestions" and just output the first 10 issues.

Don't compress the blank lines between sections; keep them as-is for readability.

If you use Template A (i.e., there are issues to fix) and at least one issue requires code changes, append a brief follow-up question after the structured output asking whether the user wants you to apply the suggested fix(es). For example: "Would you like me to use the Suggested fix section to address these issues?"

Template B (no issues)
## Code review
No issues found.

Weekly Installs
7.1K
Repository
langgenius/dify
GitHub Stars
139.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail