---
title: agents-md-improver
url: https://skills.sh/ericmjl/skills/agents-md-improver
---

# agents-md-improver

skills/ericmjl/skills/agents-md-improver
agents-md-improver
Installation
$ npx skills add https://github.com/ericmjl/skills --skill agents-md-improver
SKILL.md
AGENTS.md improver

This skill helps keep repository instructions accurate and consistent. When a user corrects the coding agent's behavior, treat it as a potential update to the repo's instruction files and propose a clean, integrated edit to AGENTS.md.

Usage

Use this skill anytime the user:

Corrects the agent ("don't do X", "do Y instead", "from now on...", "remember to...", "add a rule that...").
Asks to update instruction files like AGENTS.md, CLAUDE.md, .claude/CLAUDE.md, or GEMINI.md, or to align or consolidate those files.
Notices contradictions, duplication, or drift between repository instruction files.
Requirements
Repo-local file access to read and edit AGENTS.md.
If present in the repo, read access to CLAUDE.md and/or .claude/CLAUDE.md.
What It Does
Proposes a patch to incorporate the user's correction into AGENTS.md seamlessly.
Looks for contradictions and resolves them in the proposal (or asks for clarification when needed).
If repo-local CLAUDE.md or .claude/CLAUDE.md exists, proposes consolidating instructions into AGENTS.md, then offers follow-up options to delete, symlink, or stub those files.
How It Works
Scope

This skill is repo-specific.

Only consider repo-local instruction files:
AGENTS.md
CLAUDE.md (repo root)
.claude/CLAUDE.md
GEMINI.md (repo root and/or repo subdirectories if present)
Ignore system-wide instructions and files under the user's home directory (for example ~/.claude/, ~/.gemini/, ~/.config/, etc.).
Propose-first workflow (do not auto-edit)
Read AGENTS.md.
Identify the user's correction and translate it into a durable, repo-specific instruction.
Decide where it belongs:
Prefer editing the most relevant existing section.
If it introduces a genuinely new topic, propose a new ## section near related content.
Draft the exact text change(s) as a small patch/snippet.
Ask for confirmation before applying:
"Apply these changes to AGENTS.md? (y/n)"

Only apply edits after the user confirms.

Seamless integration rules
Do not add dated changelog entries like "YYYY-MM-DD: correction".
Update the existing prose/bullets/steps so the rule reads like it has always been part of the document.
Keep formatting consistent with the surrounding AGENTS.md style.
Contradiction checks

Before proposing a patch:

Scan AGENTS.md for conflicts with the new correction.
If a conflict exists, include conflict resolution in the proposed patch by rewriting/removing the conflicting lines.
If resolution is ambiguous, ask a single targeted question before proposing a patch.

Then scan repo-local guidance (if present):

Compare AGENTS.md against CLAUDE.md and .claude/CLAUDE.md.
Flag duplication and conflicts.
Prefer consolidating into AGENTS.md as the canonical source of truth.
Consolidation flow for CLAUDE.md files (if present)

If CLAUDE.md and/or .claude/CLAUDE.md exists in the repo:

Propose a consolidation patch to AGENTS.md.
After the user approves the AGENTS.md patch, propose what to do for each CLAUDE file:
Delete the file.
Replace the file with a symlink pointing to AGENTS.md.
Replace the file contents with a small stub that points humans/tools to AGENTS.md (fallback when symlinks are undesirable).
Confirm destructive actions (deletes) in a separate prompt.

Symlink directions (when chosen):

CLAUDE.md -> AGENTS.md
.claude/CLAUDE.md -> ../AGENTS.md
Notes for multi-instruction environments

Some harnesses merge multiple instruction sources and may apply conflicting rules non-deterministically. Prefer a single canonical source (AGENTS.md) and reduce parallel instruction files via consolidation + delete/symlink/stub.

Weekly Installs
19
Repository
ericmjl/skills
GitHub Stars
32
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass