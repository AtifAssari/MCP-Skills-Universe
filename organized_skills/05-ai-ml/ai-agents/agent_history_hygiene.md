---
rating: ⭐⭐⭐
title: agent-history-hygiene
url: https://skills.sh/daviddwlee84/agent-skills/agent-history-hygiene
---

# agent-history-hygiene

skills/daviddwlee84/agent-skills/agent-history-hygiene
agent-history-hygiene
Installation
$ npx skills add https://github.com/daviddwlee84/agent-skills --skill agent-history-hygiene
SKILL.md
agent-history-hygiene

Keep agent chat transcripts and plan files committed together with the code they produced, without leaking secrets. Pairs with the redact-agent-secrets + gitleaks pre-commit hooks the skill installs.

Three surfaces, separated by purpose:

Surface	Question it answers
find-session.sh	"Which transcript / plan file is my current session?"
stage-agent-artifacts.sh	"Which agent files belong in the next commit?"
bootstrap-project.sh	"How do I get pre-commit + gitleaks + redactor into a repo?"
scan-staged.sh	"Is there a leaked secret in what I'm about to commit?"
references/remediation.md	"I already pushed a secret — now what?"
Core invariants
Agent transcripts and plan files are committed alongside the diff that produced them. Never add them to .gitignore. An agent that drops these from a commit has broken the user's review trail.
Rotate at the provider before any git rewrite. The only act that revokes a leaked credential is rotation. History rewriting scrubs bytes on one clone and leaves them on every other.
git push --force against a shared branch is never the fix for a leak. At best it's useless; at worst it destroys teammate work and silently re-introduces the secret when someone merges their old history back.
When to use this skill

Use it when the user (or you) surface any of:

"Commit my chat" / "save the specstory session" / "include the plan file in this commit" / "把 plan 跟 specstory 一起 commit 進去".
You see dirty .specstory/history/*.md, .claude/plans/*.md, .cursor/plans/*.md, or any other configured agent artifact during git status and you're about to commit a feature.
"Scrub this transcript" / "redact my key" / "gitleaks flagged my chat history".
"Set up pre-commit for this repo" / "I'm starting a new project — how do I get the hook stack?" / "bootstrap secret scanning here".
"I pushed a .env" / "a secret went to main" / "do I need to force push?" — the agent must steer to references/remediation.md and stop the user from force-pushing reflexively.
When NOT to use
The user explicitly wants agent transcripts excluded from the repo. Respect that; suggest a one-liner .gitignore addition and skip this skill entirely.
The leak is already on a shared main/release branch. Do not offer to rewrite history — jump to references/remediation.md §5.
The project genuinely has no agent session (no .specstory/, no .claude/plans/, etc.). Nothing to stage.
Single-file, single-commit hygiene that the agent handles without any script (e.g., adding a missing trailing newline).
Integration with existing infrastructure

This skill sits on top of any chezmoi-managed stack the user already has. It does not duplicate:

chezmoi's global core.hooksPath (~/.config/git/hooks/pre-commit) — that wrapper runs the repo's .pre-commit-config.yaml and then optionally gitleaks git --staged. The skill bootstraps the repo-level config the wrapper expects to find.
chezmoi's .gitleaks.toml — the user's config already carries curated rules for common API keys (OpenAI, Anthropic, Supabase, Linear, WakaTime, Cursor, HuggingFace, Notion, Tailscale, Clash / V2Ray tokens). The skill's assets/gitleaks.toml.template ships the same rule IDs so .gitleaksignore / allowlist tweaks stay portable.
chezmoi's scripts/redact_secrets.py — remains the upstream source of truth. The skill bundles a copy so non-chezmoi users get protection; sync procedure in references/pre-commit-redaction-stack.md.

What this skill adds:

Agent-facing discipline (this SKILL.md + references/remediation.md).
A single-command project bootstrap (bootstrap-project.sh) for repos without chezmoi or where the user wants the stack in one go.
Session-discovery heuristics (find-session.sh) for the "find my current transcript among many" problem.
An exit-code wrapper (scan-staged.sh) agents can branch on before committing.
Workflow A: commit-time hygiene

Default flow when the agent is about to commit feature changes plus chat/plan artifacts.

# 1. Make sure the agent knows which session is "ours" — mostly
#    relevant when multiple Claude/SpecStory sessions run in the repo.
bash skills/local/agent-history-hygiene/scripts/find-session.sh

# 2. Stage code the usual way, then auto-add agent artifacts.
git add path/to/feature/file.ts
bash skills/local/agent-history-hygiene/scripts/stage-agent-artifacts.sh
# Use --session-only if you want ONLY the current SpecStory + newest plan;
# default stages every dirty *.md in every configured agent dir.

# 3. Belt-and-suspenders secret scan before commit. Exit 0 = clean.
bash skills/local/agent-history-hygiene/scripts/scan-staged.sh || {
  # Exit 10/20: leaks found. Jump to references/remediation.md.
  echo "Leaks detected — see references/remediation.md before committing." >&2
  exit 1
}

# 4. Commit. pre-commit (installed by bootstrap) runs redact-agent-secrets
#    then gitleaks again as a catch-all.
git commit -m "feat: ..."

Workflow B: bootstrap a new project

For repos that don't yet have .pre-commit-config.yaml / .gitleaks.toml installed. Runs once per repo.

cd /path/to/new/project
bash skills/local/agent-history-hygiene/scripts/bootstrap-project.sh \
  --install-hook            # optional: auto-stage on every commit

# Verify: shake out any existing issues in the working tree.
pre-commit run --all-files


What bootstrap-project.sh does:

Drops .pre-commit-config.yaml + .gitleaks.toml into the repo (skips if already present unless --force).
Writes scripts/redact_secrets.py (bundled copy; use --from-chezmoi to symlink the chezmoi source so fixes propagate).
Runs pre-commit install (or uvx pre-commit@4 install if pre-commit isn't on PATH).
Audits .gitignore / .git/info/exclude for patterns that would silently hide an agent artifact dir — warns without editing.
Checks ~/.claude/settings.json for plansDirectory; prints the one-line patch if missing.
With --install-hook: writes a prepare-commit-msg hook that calls stage-agent-artifacts.sh --session-only --allow-empty so every git commit auto-attaches the current session file.
Workflow C: post-leak remediation

When scan-staged.sh reports exit 10/20, or the user says "I committed / pushed a secret":

STOP the user from running git push --force reflexively.
Read references/remediation.md end-to-end.
Walk the user through step 1 (rotate) regardless of blast radius. Only after rotation does the question of scrubbing history become worth discussing.
Use the decision tree in the runbook to pick the right git action.
Gotchas
plansDirectory project-level sometimes ignored. Claude Code issue #19537 reports project-level plansDirectory being ignored in some versions. After running a /plan, verify the file actually landed where you expected before relying on stage-agent-artifacts.sh picking it up. User-level config (~/.claude/settings.json with "plansDirectory": "./.claude/plans") is the recommended default.
gitleaks protect is deprecated. Since v8.19.0 use gitleaks git --staged --redact (pre-commit) and gitleaks dir <path> (working directory). The older commands still work but emit a deprecation notice. This skill uses the modern syntax everywhere.
pre-commit install is per-clone. Each teammate must run pre-commit install in their own clone for hooks to fire. CI cannot be trusted as the single gate — it's second-chance, not last-chance.
Transcript files can be huge. A long SpecStory session can exceed 2 MB. The template bumps check-added-large-files to --maxkb=2048 to avoid false positives, but a very long session can still overflow. If you hit the limit, rotate sessions (specstory run claude creates a fresh file) instead of raising the cap further.
Session-UUID divergence between SpecStory CLI and VS Code extension. The extension autosaves into .specstory/history/ continuously; the CLI (specstory run claude) creates one file per invocation. If both are active you can end up with two transcripts for what feels like "one session" — mtime-newest wins in find-session.sh.
Global core.hooksPath means bare repos aren't protected. The chezmoi setup's global hook runs .pre-commit-config.yaml IF it exists — so a repo without .pre-commit-config.yaml has no protection. Run bootstrap-project.sh before the first commit with agent artifacts, not after.
Active SpecStory writer can defeat the redact loop. The standard git add → git commit → pre-commit auto-fixes → re-stage → re-commit flow assumes the file is quiescent during the commit. SpecStory's specstory_*_watch daemon tails the agent transcript continuously, so if the chat captured ps -axo args-style output that contained an unrelated daemon's secret in argv (e.g. SpecStory's own --cloud-token … flag), every diagnostic command (grep, sed -n '<line>p', cat | head | tail) prints the secret again, SpecStory appends it to the transcript, and the redact-then-restage cycle never converges. Symptom: pre-commit says "Successfully redacted N file(s)" but gitleaks-system immediately fails on the same line, re-running git add && git commit doesn't help, and grep -c '<secret-prefix>' file shows the count increasing over commit attempts. Workaround: a single atomic python3 -c "<in-place re.sub>" && git add <file> && git commit -m "..." pipeline so the index is frozen before any new specstory write lands. Don't print, grep, or diff the secret line during the recovery — every print echoes back into the transcript. Diagnose with lsof <file> (looking for specstory_* writers) instead. See pitfalls/redact-secrets-loop-with-active-specstory-writer.md in upstream chezmoi for the full debugging trail.
Available scripts

scripts/find-session.sh [--format=specstory|claude|both] [--json] Discover the current agent session files for $PWD. TSV default, --json for structured callers. Never exits non-zero (always 0, empty fields signal absence).

scripts/stage-agent-artifacts.sh [--session-only] [--include-all-plans] [--dry-run] [--allow-empty] git add the right agent artifacts before the next commit. --session-only stages only the current SpecStory + newest plan; default stages every dirty *.md in every configured artifact dir. Refuses to run if there are no code changes (prevents "commit just transcript"); override with --allow-empty.

scripts/scan-staged.sh [--redact] [--verbose] Run gitleaks git --staged with agent-friendly exit codes (0 clean / 10 redacted / 20 leaks / 30 gitleaks missing). JSON lines on stdout, prose diagnostics on stderr.

scripts/bootstrap-project.sh [--from-chezmoi] [--install-hook] [--force] [--dry-run] Install .pre-commit-config.yaml + .gitleaks.toml + the redactor into the current repo, then run pre-commit install. Audits .gitignore and ~/.claude/settings.json for misconfigurations (warns, never silently edits).

Bundled assets
assets/artifact-dirs.txt — the canonical list of agent artifact directories (SpecStory, Claude plans, Cursor plans + rules, OpenCode plans, Spec-kit, Codex). Consumed by stage-agent-artifacts.sh and by bootstrap-project.sh when rendering the pre-commit files: regex.
assets/pre-commit-config.yaml.template — minimal .pre-commit-config.yaml with redact-agent-secrets + gitleaks + standard hygiene hooks.
assets/gitleaks.toml.template — portable subset of the chezmoi .gitleaks.toml with custom rule IDs + a path-scoped allowlist for agent artifact dirs.
assets/redact_secrets.py — bundled copy of chezmoi's scripts/redact_secrets.py. Chezmoi version is upstream; sync doc in references/pre-commit-redaction-stack.md.
Reference files
references/transcript-session-discovery.md — SpecStory / Claude session layouts and the $PWD → slug algorithm. Read when find-session.sh returns empty or ambiguous results.
references/pre-commit-redaction-stack.md — three-layer defense (redact → gitleaks → scan-staged.sh), allowlist design, sync procedure for the bundled redactor. Read when tuning rules or debugging unexpected pre-commit failures.
references/remediation.md — rotate-first runbook for "I committed / pushed a secret". Read before any git filter-repo / git push --force action.
Tests

The skill ships with a three-level test suite under tests/. Run from repo root:

make test-skill

test_redact_secrets.py — pytest for pure redactor functions.
test_gitleaks_corpus.py — golden-corpus fixtures staged in tmp git repos, asserting real-key shapes fire and example shapes are allowlisted only inside configured artifact dirs.
test_scan_staged.sh — exit-code contract for scripts/scan-staged.sh (0 / 20 / 30 / 2).

The corpus + shell tests skip gracefully when gitleaks isn't on PATH. See tests/README.md for what each regression the suite locks in.

Related skills
project-knowledge-harness — complementary memory harness (TODO.md + backlog/ + pitfalls/) that references .claude/plans/ as "ephemeral agent scratchpads". This skill fills the gap: those scratchpads belong in git, not ignored.
Weekly Installs
8
Repository
daviddwlee84/ag…t-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass