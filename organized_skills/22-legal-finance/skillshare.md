---
rating: ⭐⭐⭐
title: skillshare
url: https://skills.sh/haha0815/claude-meta-skills/skillshare
---

# skillshare

skills/haha0815/claude-meta-skills/skillshare
skillshare
Installation
$ npx skills add https://github.com/haha0815/claude-meta-skills --skill skillshare
SKILL.md
Skillshare CLI
Two Modes
Global: ~/.config/skillshare/skills → ~/.claude/skills, ~/.cursor/skills, ...
Project: .skillshare/skills/        → .claude/skills, .cursor/skills (per-repo)


Auto-detection: commands run in project mode when .skillshare/config.yaml exists in cwd. Force with -p (project) or -g (global).

Commands
Category	Commands	Project?
Inspect	status, diff, list, doctor	✓ (auto)
Sync	sync, collect	✓ (auto)
Remote	push, pull	✗ (use git)
Skills	new, install, uninstall, update, check, search	✓ (-p)
Targets	target add/remove/list	✓ (-p)
Security	audit [name]	✓ (-p)
Trash	trash list|restore|delete|empty	✓ (-p)
Log	log [--audit] [--tail N]	✓ (-p)
Backup	backup, restore	✗
Web UI	ui (-g global, -p project)	✓ (-p)
Upgrade	upgrade [--cli|--skill]	—

Workflow: Most commands require sync afterward to distribute changes.

AI Usage Notes
Non-Interactive Mode

AI cannot respond to CLI prompts. Always pass flags to skip interactive prompts.

# Key non-interactive patterns
skillshare init --no-copy --all-targets --git --skill   # Global fresh start
skillshare init -p --targets "claude,cursor"       # Project init
skillshare install user/repo --all                      # Install all skills
skillshare install user/repo -s pdf,commit              # Select specific


See init.md and install.md for all flags.

Safety
install auto-scans skills; CRITICAL findings block install (--force to override)
install shows license from SKILL.md frontmatter in selection/confirmation prompts
uninstall accepts multiple names and --group/-G for batch removal; auto-detects group directories
uninstall moves to trash (7-day retention) — restore with trash restore <name>
NEVER rm -rf symlinked skills — deletes source. Use skillshare uninstall or target remove

See audit.md and trash.md for details.

References
Topic	File
Init flags (global + project)	init.md
Sync/collect/push/pull	sync.md
Install/update/uninstall/new	install.md
Status/diff/list/search/check	status.md
Security audit	audit.md
Trash (soft-delete)	trash.md
Operation log	log.md
Target management	targets.md
Backup/restore	backup.md
Troubleshooting	TROUBLESHOOTING.md
Weekly Installs
9
Repository
haha0815/claude…a-skills
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn