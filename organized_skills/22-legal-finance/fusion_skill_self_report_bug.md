---
rating: ⭐⭐
title: fusion-skill-self-report-bug
url: https://skills.sh/equinor/fusion-skills/fusion-skill-self-report-bug
---

# fusion-skill-self-report-bug

skills/equinor/fusion-skills/fusion-skill-self-report-bug
fusion-skill-self-report-bug
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion-skill-self-report-bug
SKILL.md
Self-report Fusion Skill Bugs
When to use

Use this skill when a Fusion skill workflow fails and you need a consistent, triage-ready bug report draft. Treat this as the default failure handoff for any fusion-* skill execution.

Typical triggers:

"a fusion-* skill failed"
"this skill run failed"
"self-report this skill error"
"create a bug from this workflow failure"
"capture this automation failure for triage"
When not to use

Do not use this skill for:

Feature requests or roadmap planning
General implementation tasks without observed failure
Publishing GitHub changes without explicit user confirmation
Required inputs

Collect before drafting:

Target repository for the bug report (default: equinor/fusion-skills)
Failing command or workflow step
Environment context (OS/shell/runtime/tooling versions if available)
Observed output/error evidence
Reproduction signal (exact steps or best-effort notes)
Optional parent issue number for linking
Instructions
Detect or confirm failure intent.
If failure context is missing, ask for command used, expected behavior, actual behavior, and key error output.
Capture failure context.
Normalize context into: command, environment, observed error/output, reproducibility, and impact.
Draft locally first.
Write .tmp/BUG-skill-failure-<context>.md using assets/issue-templates/skill-workflow-failure-bug.md.
Include reproducible steps and explicit observed/expected behavior.
Propose issue metadata.
Recommend issue type: Bug.
Recommend labels for reliability/automation triage (for example bug, automation, reliability), then validate labels against the target repository before mutation.
Ask assignee preference (@me, specific user, or unassigned).
Offer optional relationship linking.
If parent issue is provided, prepare to link the new bug as a sub-issue after issue creation.
Ask explicit publish confirmation.
Do not run any GitHub mutation until the user explicitly confirms publish.
Mutate only after confirmation.
Create issue via MCP issue mutation.
Apply labels/assignee.
If parent issue was provided, link as sub-issue.
If confirmation is not provided, stop after draft.
Return status No GitHub state changes made.
Expected output

Return:

Draft bug report file path under .tmp/
Captured failure-context summary (command, environment, observed output)
Proposed title/body and reproduction steps
Proposed issue type + labels + assignee plan
Optional parent issue linking plan
Explicit status: Awaiting publish confirmation or No GitHub state changes made
Created issue URL/number only after confirmed mutation
Safety & constraints

Never:

Perform GitHub create/edit/comment/close actions without explicit confirmation
Claim failure evidence that was not provided or observed
Request or expose secrets/credentials

Always:

Keep draft-first behavior
Prefer minimal reproducible detail over long narrative
Validate label existence in the target repository before applying
Weekly Installs
52
Repository
equinor/fusion-skills
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass