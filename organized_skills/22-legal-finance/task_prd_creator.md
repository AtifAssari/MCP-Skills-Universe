---
rating: ⭐⭐⭐
title: task-prd-creator
url: https://skills.sh/shipshitdev/library/task-prd-creator
---

# task-prd-creator

skills/shipshitdev/library/task-prd-creator
task-prd-creator
Installation
$ npx skills add https://github.com/shipshitdev/library --skill task-prd-creator
SKILL.md
Task & PRD Creator

Write a clear, actionable PRD or task. Output depends on where the user tracks work.

Step 1: Detect workflow preference

Check in order:

User explicitly says "GitHub issue", "local file", or both
Check if gh auth status succeeds and a GitHub remote exists → GitHub available
Check if .agents/TASKS/ or .agents/PRDS/ exist → local available
If ambiguous, ask: "GitHub issue, local file, or both?"
Step 2: Understand the request

Ask only what's missing — don't interrogate if context is clear:

What problem does this solve?
Who's affected? (user-facing, internal, infra)
Any hard constraints or dependencies?
Is this part of a larger epic? (→ sub-issue)
Priority: critical / high / medium / low
Step 3: Research before writing
Read relevant architecture docs if available (.agents/SYSTEM/ARCHITECTURE.md)
Search codebase for related patterns
Check for existing issues on same topic: gh issue list --search "[keyword]"
Step 4: Write the PRD

See references/full-guide.md for the full PRD structure.

A good PRD has:

Problem — why this exists, what breaks without it
Goal — one sentence, measurable outcome
Scope — what's in, what's explicitly out
Acceptance criteria — testable, not vague
Technical notes — approach, risks, dependencies

Keep it tight. No filler. Acceptance criteria must be checkable by a human.

Step 5: Output to correct destination
GitHub (primary if available)

New issue:

gh issue create \
  --title "[type]: clear title" \
  --body "$(cat <<'BODY'
[PRD content here]
BODY
)" \
  --label "feature" \
  --assignee "@me"


Sub-issue (linked to parent):

# Create sub-issue
gh issue create --title "..." --body "..." 

# Link as sub-issue to parent #N
gh issue develop N --checkout  # only if needed
# Use: gh api repos/{owner}/{repo}/issues/{parent}/sub_issues --method POST -f sub_issue_id={child_id}


Draft PR from issue:

gh issue develop [issue-number] --branch "feature/[name]"

Local files (optional, or when no GitHub)
Task: .agents/TASKS/[kebab-name].md
PRD: .agents/PRDS/[kebab-name].md

See references/full-guide.md for local file templates.

Step 6: Get approval before creating

Show the draft PRD. Wait for "looks good" or edits. Then create.

Rules
disable-model-invocation: true → only runs when user explicitly invokes
Never create files or GitHub issues without user seeing the draft first
Sub-issues should be small enough to ship in one PR
If requirements are unclear, write the problem statement first — not the solution
Related
spec-first — spec-driven development before writing code
gh-fix-ci — fix CI on existing PRs
strategy-expert — broader roadmap and content planning
Weekly Installs
126
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn