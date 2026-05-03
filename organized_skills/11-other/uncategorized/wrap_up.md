---
rating: ⭐⭐
title: wrap-up
url: https://skills.sh/rohitg00/pro-workflow/wrap-up
---

# wrap-up

skills/rohitg00/pro-workflow/wrap-up
wrap-up
Installation
$ npx skills add https://github.com/rohitg00/pro-workflow --skill wrap-up
SKILL.md
Wrap-Up Ritual

End your coding session with intention.

Trigger

Use when ending a session, saying "wrap up", "done for now", or before closing the editor.

Workflow
Changes Audit — What files were modified? Anything uncommitted? TODOs left in code?
Quality Check — Run lint, typecheck, and tests. All passing? Any warnings?
Learning Capture — What mistakes were made? What patterns worked well? Format as [LEARN] Category: Rule
Next Session Context — What's the next logical task? Any blockers? Context to preserve?
Summary — One paragraph: what was accomplished, current state, what's next.
Commands
git status
git diff --stat

npm run lint 2>&1 | head -20
npm run typecheck 2>&1 | head -20
npm test -- --changed --passWithNoTests

Learning Categories

Navigation, Editing, Testing, Git, Quality, Context, Architecture, Performance

Guardrails
Do not skip any checklist step.
If tests are failing, flag before ending session.
If uncommitted changes exist, ask whether to commit or stash.
Output
Modified file list with uncommitted changes highlighted
Quality gate results
Captured learnings (if any)
One-paragraph session summary
Next session resume context

After completing checklist, ask: "Ready to end session?"

Weekly Installs
38
Repository
rohitg00/pro-workflow
GitHub Stars
2.0K
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass