---
rating: ⭐⭐
title: bug-triage
url: https://skills.sh/jmerta/codex-skills/bug-triage
---

# bug-triage

skills/jmerta/codex-skills/bug-triage
bug-triage
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill bug-triage
SKILL.md
Bug triage
Goal

Turn an ambiguous bug report into:

a reliable repro (or a clear “cannot reproduce yet” with next info to collect)
a root-cause explanation
a minimal, reviewed fix
verification steps (commands + manual checks)
First checks
Read any repo-specific guidance (AGENTS.md, CONTRIBUTING.md, README).
Clarify impact: severity, who is affected, and whether it’s a regression.
If info is missing, ask for it
Exact steps to reproduce (starting state + inputs).
Expected vs actual behavior.
Error text / stack trace / logs (full, unedited if possible).
Environment: OS, runtime versions (Node/Bun), browser, commit hash/tag.
Frequency: always / sometimes / only certain data.
“Last known good” version or approximate date when it started.
Workflow (checklist)
Reproduce locally
Prefer the simplest, fastest repro.
If it’s flaky, try to reduce nondeterminism (seed, fixed time, retries).
Localize the failure
Narrow to a file/function/component/config.
Use rg to find relevant code paths and error strings.
Identify root cause
Form a hypothesis, confirm with logs/breakpoints, then refine.
If it’s a regression and git history exists, consider git bisect.
Implement the minimal fix
Fix the cause, not the symptom.
Avoid drive-by refactors and formatting churn.
Verify
Run the project’s standard checks (lint/tests/build).
Re-run the repro steps and confirm the fix.
Repo-aware command hints

Use what the repo actually uses:

If bun.lock exists: prefer bun ... (e.g. bun lint, bun build, bun dev).
Otherwise: use the project’s documented commands (npm, pnpm, yarn, etc.).
If bun.lock exists but bun is not available, tell the user and ask whether to install bun or use the repo’s alternative package manager.
Deliverable (paste this in the chat / PR / issue)

Use this format:

Summary: ...
Repro: ...
Root cause: ...
Fix: ...
Verification: ...
Risk/notes: ...

If you need a bug-report structure to ask the user for, use references/bug-report-template.md.

Weekly Installs
30
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass