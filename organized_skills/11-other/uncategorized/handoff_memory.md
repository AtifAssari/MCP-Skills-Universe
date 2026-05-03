---
rating: ⭐⭐
title: handoff-memory
url: https://skills.sh/17-sss/agent-skills/handoff-memory
---

# handoff-memory

skills/17-sss/agent-skills/handoff-memory
handoff-memory
Installation
$ npx skills add https://github.com/17-sss/agent-skills --skill handoff-memory
SKILL.md
Handoff Memory
Overview

Keep shared memory documents close to the work they describe. For a single repository, keep the canonical handoff in the repo. For a multi-repository workspace, keep workspace-wide memory in the workspace root and workstream-specific memory under dedicated workstream folders.

This skill keeps one canonical handoff per scope and adds lightweight operational tooling:

resolve the right document path
resolve the right resume target without guessing a workstream
create or refresh the canonical file
sync a lightweight _memory/INDEX.json for workspace workstreams
validate that the document is structurally usable
check whether the document is stale before trusting it
optionally write timestamped session snapshots without making them the primary state
Compatibility and Prerequisites
python3 must be available in PATH to run the bundled scripts.
git must be available in PATH for freshness checks and repo metadata.
The skill still resolves paths and validates documents outside Git, but stale checks are less informative there.
All bundled scripts are non-interactive and expose --help. Prefer running them directly instead of recreating their logic by hand.
Branch names may still be recorded in repo-local metadata, but resume selection should not use branch as the primary signal.
Default Workflow

Use this as the default flow unless the user already has a stronger convention:

Resolve or initialize the canonical document. Run scripts/create_handoff.py --project-root <path> --scope auto --document handoff --format json. Add --workstream <name> when the task belongs to one specific repo combination inside a larger workspace.

Read the canonical document before changing it. Preserve still-valid context. Remove stale claims that would mislead the next session.

Update the canonical document with the current state. Keep it short, explicit, and action-oriented.

Validate it before ending the session. Run scripts/validate_handoff.py --project-root <path> --scope auto --document handoff. Use --strict only when strict template conformance should fail the check. The default mode only requires the handoff to be resume-usable.

When resuming, check staleness before trusting old notes. Run scripts/resolve_handoff_path.py --project-root <path> --scope auto --document handoff --resume --format json first, then scripts/check_staleness.py --project-root <path> --scope auto --document handoff.

In mixed multi-repo workspaces, do not treat the parent folder as automatically workspace-wide. Resume selection should prefer an explicit handoff or workstream, then repo overlap, then _memory/INDEX.json, then a unique current workstream. If more than one workstream still matches, return an ambiguous result instead of guessing. Use --workspace-wide only when the user explicitly wants status for every child repository.

For resume-style requests such as "continue", "resume", or "pick up where we left off", treat Next Actions as the default execution queue and Resume Prompt as the default execution framing. Do not reopen design direction that the handoff already narrowed unless the user asks to rethink it or the current repo state clearly invalidates it.

Use --snapshot with create_handoff.py only when the user wants a timestamped checkpoint that is worth preserving. Always pair it with --snapshot-kind and a short --snapshot-reason. Do not make snapshots the default shared state.

For day-to-day agent behavior, follow references/agent-usage-best-practices.md.

Path Rules
Prefer an explicit --handoff-path when the project already defines a canonical location.
If --handoff-path points inside _memory/workstreams/<name>/..., the scripts infer workspace scope and workstream name automatically.
Explicit --handoff-path or --workstream should override auto-detection.
In repo scope, reuse an existing shared handoff file in a recognized location such as docs/HANDOFF.md, memories/HANDOFF.md, or HANDOFF.md.
In workspace scope, keep cross-repo memory under _memory/.
If no repo handoff exists, create docs/HANDOFF.md.
If no workspace handoff exists, create _memory/HANDOFF.md.
For workspace-wide memory, use these defaults:
_memory/HANDOFF.md for workspace-wide summary and active workstream index
_memory/WORKSPACE.md for durable workspace structure
_memory/DECISIONS.md for cross-repo architecture or policy choices
_memory/PATTERNS.md for repeatable conventions
For workstream-specific memory, use these defaults:
_memory/workstreams/<name>/HANDOFF.md
_memory/workstreams/<name>/WORKSTREAM.md
_memory/workstreams/<name>/DECISIONS.md
_memory/workstreams/<name>/PATTERNS.md
Most sessions should only update the canonical handoff for the active scope. Touch companion workspace or workstream documents only when durable shared context changed.
In workspace scope, maintain a lightweight _memory/INDEX.json with last_active_workstream plus per-workstream canonical_path, last_updated, status, and repositories.
Optional snapshots live under docs/handoffs/, _memory/handoffs/, or _memory/workstreams/<name>/handoffs/.
Canonical files keep canonical names such as HANDOFF.md and WORKSTREAM.md. Only snapshots get timestamped names, using YYYYMMDD_HHMMSS[-n]-<kind>-<label>.md.
Avoid .codex, .claude, .windsurf, or .agents as the default shared mutable handoff location.
Scope Guidance
Repo Scope

Use repo scope when the task belongs to one repository.

Canonical file: docs/HANDOFF.md
Session snapshots: docs/handoffs/*.md
Keep implementation-level detail here
Workspace Scope

Use workspace scope when the agent session starts from a parent folder that coordinates multiple repositories and the task spans more than one of them at the workspace-wide level.

Canonical file: _memory/HANDOFF.md
Session snapshots: _memory/handoffs/*.md
Keep workspace-wide coordination and durable shared context here
Leave repo-specific implementation detail in each repo's own docs/HANDOFF.md
Workstream Scope

Use workstream scope when the same workspace hosts multiple independent repo combinations and one handoff per workspace would blur them together.

Canonical file: _memory/workstreams/<name>/HANDOFF.md
Durable overview: _memory/workstreams/<name>/WORKSTREAM.md
Session snapshots: _memory/workstreams/<name>/handoffs/*.md
Keep only the repos relevant to that initiative in the workstream handoff
Prefer workstream names that describe the initiative, not just the repo list
Content Rules
Keep the document scan-friendly. The next session should understand it in under a minute.
Start with a strong TL;DR.
Prefer exact workspace-relative paths, commands, dates, and repo names over vague prose.
Avoid machine-specific absolute paths such as /Users/... or other paths outside the current project root unless they are truly required. The validator warns on foreign absolute paths for portability.
Record what is true now, not a transcript of the full chat.
Note what changed recently, what is risky, and what should happen next.
Include a quick reference section with the few files, commands, dashboards, or docs that matter most.
Keep a short resume checklist so the next session can verify the notes before acting on them.
Note when a claim is unverified.
Do not store secrets, tokens, private keys, raw credentials, or long confidential logs.
Document Model

The canonical handoff is the shared source of truth. Optional session snapshots are secondary artifacts for traceability.

Canonical handoff:
repo: docs/HANDOFF.md
workspace-wide: _memory/HANDOFF.md
workstream: _memory/workstreams/<name>/HANDOFF.md
Snapshot archive:
repo: docs/handoffs/*.md
workspace-wide: _memory/handoffs/*.md
workstream: _memory/workstreams/<name>/handoffs/*.md
Workspace index:
_memory/INDEX.json with lightweight workstream metadata for resume-time targeting

This model keeps the current state easy to find while still allowing point-in-time captures when they are useful.

Resume Workflow

When asked to continue work from a prior session:

Resolve the resume target, not just the generic canonical handoff path. Run scripts/resolve_handoff_path.py --project-root <path> --scope auto --document handoff --resume --format json. The selection priority is: explicit --handoff-path, explicit --workstream, current repo overlap, index last_active_workstream, unique current or in-progress workstream, then ambiguous instead of guessed restore.
Read the canonical handoff before planning or editing code.
Treat the first unfinished item in Next Actions as the default plan, and treat Resume Prompt as the default continuation frame.
Run the staleness check if the document might be old.
If working in workspace scope, read companion memory files only when they are directly relevant.
If the task is only one initiative inside a larger workspace, resolve the workstream document instead of the workspace-wide handoff.
In a parent folder with unrelated repositories, narrow validation to the selected workstream or the repositories named in the selected handoff before considering a workspace-wide scan.
Compare the document against the current repo, workstream, or workspace state and call out drift.
Execute the first unfinished next action. Explore only as needed to complete it, not to replace it with fresh design work.
Refresh and validate the canonical handoff again before ending the session if anything material changed.
Scripts
scripts/resolve_handoff_path.py

Resolve the canonical repo-local, workspace-wide, or workstream-specific memory path. Use --scope repo|workspace|auto, --document handoff|workspace|workstream|decisions|patterns, --workstream, or --handoff-path to honor an explicit override. Use --resume to apply resume target selection and return ambiguous instead of guessing when multiple workstreams still match. Use --ensure to create the file when it does not exist.

scripts/create_handoff.py

Initialize or refresh the canonical file and sync metadata such as project root and update timestamp. In workspace scope, this also refreshes _memory/INDEX.json. Use --snapshot --snapshot-kind <kind> --snapshot-reason <text> to write a timestamped archive copy before the canonical file is refreshed.

scripts/validate_handoff.py

Check that the document is resume-usable by default, warn on portability issues such as foreign absolute paths, and stay short enough to be useful. Use --strict when strict template conformance should fail on missing sections, placeholders, or empty required sections.

scripts/check_staleness.py

Compare the handoff timestamp against recent repo activity. The script prefers Last Updated metadata over file mtime, uses the selected workstream's declared repos when available, and does not fall back to scanning every child repo unless --workspace-wide is explicit. If resume targeting is ambiguous, it returns an ambiguous result instead of guessing.

References
references/handoff-template.md

Use this to understand the expected handoff structure and section intent.

references/workspace-memory-guide.md

Use this when the task spans multiple repositories and you need to decide whether the canonical workspace handoff is enough or whether the task needs a dedicated workstream.

references/agent-usage-best-practices.md

Use this when you want the recommended start-of-session, end-of-session, and scope-selection behavior for agents using this skill in normal work.

references/snapshot-strategy.md

Use this when you need explicit guidance on when to create a snapshot, when not to, and which snapshot kind to use.

references/agent-integrations.md

Use this when the user asks where to install the skill for Codex or another agent. Keep install notes separate from the handoff workflow itself.

Notes
Installation scope and data location are separate concerns.
The skill may be installed globally or per-project, but the shared mutable documents should stay inside the repository or workspace root they describe.
Agent-specific files such as AGENTS.md, CLAUDE.md, .codex/*, or .windsurf/rules/* may reference the shared handoff, but should not become the primary mutable store.
Weekly Installs
17
Repository
17-sss/agent-skills
GitHub Stars
2
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass