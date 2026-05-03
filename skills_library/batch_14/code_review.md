---
title: code-review
url: https://skills.sh/sungkhum/agent-skills-pack/code-review
---

# code-review

skills/sungkhum/agent-skills-pack/code-review
code-review
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill code-review
SKILL.md
Code Review
Overview

Perform a rigorous, adversarial review that cross-checks story claims and acceptance criteria against the real code changes. Prioritize concrete, reproducible findings with file and line references. If the code is clean, explicitly say so.

Quick Start
Determine scope: story file + repository, or a diff/PR.
Identify repo root (use git) and collect changed files via git status --porcelain, git diff --name-only, and git diff --cached --name-only.
Load story/spec inputs if provided; otherwise ask for the story/spec or acceptance criteria.
Exclude non-application files and folders (.cursor/, .windsurf/, .claude/, and other tooling/config folders unless explicitly requested).
Workflow

Follow the detailed workflow in references/workflow.md. Use these guardrails when adapting it to a standalone repo:

If {project-root}/workflow-config.yaml does not exist, treat config values as optional and ask the user for missing items that affect output (language, skill level, story path, etc.).
If planning artifacts (architecture/ux/epics) are unavailable, proceed with the story/spec and code changes only; note missing context explicitly.
If no story file exists, replace “story validation” with “requirements validation” using the user-provided criteria or a PR description.
Review Expectations
Validate each Acceptance Criterion and each task marked complete. Missing ACs are HIGH severity; tasks marked complete but not implemented are CRITICAL.
Cross-check story File List against actual git changes; report discrepancies.
Cover security, performance, error handling, test quality, and maintainability.
If no issues remain after a second pass, report a clean review.
Output
Present findings grouped by severity with evidence (file:line), and a short impact statement.
If asked, fix issues or create action items; otherwise provide a concise remediation list.
When applicable, update story status and sprint status in accordance with the workflow.
References
references/workflow.md for the full standalone code review flow.
references/discover-inputs.md for input discovery/loading strategy.
references/checklist.md for the review completion checklist.
Weekly Installs
9
Repository
sungkhum/agent-…lls-pack
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass