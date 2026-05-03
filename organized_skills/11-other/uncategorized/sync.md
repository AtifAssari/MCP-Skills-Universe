---
rating: ⭐⭐⭐
title: sync
url: https://skills.sh/slamb2k/mad-skills/sync
---

# sync

skills/slamb2k/mad-skills/sync
sync
Installation
$ npx skills add https://github.com/slamb2k/mad-skills --skill sync
SKILL.md
Sync - Repository Synchronization

When this skill is invoked, IMMEDIATELY output the banner below before doing anything else. Pick ONE tagline at random — vary your choice each time. CRITICAL: Reproduce the banner EXACTLY character-for-character. The first line of the art has 4 leading spaces — you MUST preserve them.

{tagline}

⠀   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗
   ██╔╝██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝
  ██╔╝ ███████╗ ╚████╔╝ ██╔██╗ ██║██║
 ██╔╝  ╚════██║  ╚██╔╝  ██║╚██╗██║██║
██╔╝   ███████║   ██║   ██║ ╚████║╚██████╗
╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝


Taglines:

🎯 Pulling the latest moves...
🚂 All aboard the sync train!
🤝 Getting everyone on the same page!
📡 Fetching the latest plot twists!
🥷 Time to steal everyone else's code!
☕ Catching up on what you missed!
🔁 Rebase, merge, rinse, repeat!
🎬 Previously on main...
Output Formatting

After the banner, display parsed input:

┌─ Input ────────────────────────────────────────
│  {Field}:  {value}
│  Flags:    {parsed flags or "none"}
└────────────────────────────────────────────────


Pre-flight results:

── Pre-flight ───────────────────────────────────
  ✅ {dep}           {version or "found"}
  ⚠️ {dep}           not found → {fallback detail}
  ❌ {dep}           missing → stopping
──────────────────────────────────────────────────


Stage/phase headers: ━━ {N} · {Name} ━━━━━━━━━━━━━━━━━━━━━━━━━

Status icons: ✅ done · ❌ failed · ⚠️ degraded · ⏳ working · ⏭️ skipped

Synchronize local repository with the remote default branch using a deterministic bash script — no LLM subagent needed since all steps are pure git commands.

Flags

Parse optional flags from the request:

--no-stash: Don't auto-stash uncommitted changes
--no-cleanup: Don't delete stale local branches
--no-rebase: Use merge instead of rebase when on a feature branch
Pre-flight

Before starting, check all dependencies in this table:

Dependency	Type	Check	Required	Resolution	Detail
git	cli	git --version	yes	stop	Install from https://git-scm.com

For each row, in order:

Run the Check command (for cli/npm) or test file existence (for agent/skill)
If found: continue silently
If missing: apply Resolution strategy
stop: notify user with Detail, halt execution
url: notify user with Detail (install link), halt execution
install: notify user, run the command in Detail, continue if successful
ask: notify user, offer to run command in Detail, continue either way (or halt if required)
fallback: notify user with Detail, continue with degraded behavior
After all checks: summarize what's available and what's degraded
Pre-flight Detection

Before launching the subagent, detect the remote and default branch:

REMOTE=$(git remote | head -1)   # usually "origin"
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/$REMOTE/HEAD 2>/dev/null | sed 's|.*/||')


Fallback chain if symbolic-ref fails:

Check git show-ref --verify refs/heads/main → use main
Check git show-ref --verify refs/heads/master → use master
If neither exists, report error and stop

Pass {REMOTE} and {DEFAULT_BRANCH} into the subagent prompt.

Execution

Run the sync script directly — no LLM subagent needed since all steps are deterministic git commands:

# Resolve skill root (plugin install or direct install)
for SKILL_ROOT in \
  "${CLAUDE_PLUGIN_ROOT:-}" \
  "$HOME/.claude/plugins/marketplaces/slamb2k" \
  "$(dirname "$(readlink -f "$0")")/.."
do
  [ -f "$SKILL_ROOT/skills/sync/scripts/sync.sh" ] && break
done

bash "$SKILL_ROOT/skills/sync/scripts/sync.sh" \
  "{REMOTE}" "{DEFAULT_BRANCH}" {FLAGS}


Parse the output between SYNC_REPORT_BEGIN and SYNC_REPORT_END markers. Extract key=value pairs for the report fields: status, remote, default_branch, main_updated_to, current_branch, stash, rebase, branches_cleaned, errors.

Exit codes: 0=success, 1=fatal error, 2=partial success (conflict warnings).

Report to User

Parse the subagent's SYNC_REPORT and present a clean summary:

┌─ Sync · Report ────────────────────────────────
│
│  ✅ Sync complete
│
│  🌿 Main:     {commit} — {message}
│  🔀 Branch:   {current_branch}
│  📦 Stash:    {restored|none|conflict}
│  🧹 Cleaned:  {branches or "none"}
│
└─────────────────────────────────────────────────


If errors occurred:

│  ❌ {error description}
│     {suggested resolution}

Weekly Installs
15
Repository
slamb2k/mad-skills
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass