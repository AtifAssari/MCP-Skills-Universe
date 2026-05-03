---
title: safe-rm
url: https://skills.sh/beshkenadze/claude-skills-marketplace/safe-rm
---

# safe-rm

skills/beshkenadze/claude-skills-marketplace/safe-rm
safe-rm
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill safe-rm
SKILL.md
Safe RM
Overview

Wrapper around rm -rf with safety checks. Use this instead of direct rm -rf commands.

When to Use
Deleting directories or files recursively
Any rm -rf or rm -r operation
Cleaning up temporary files/folders
Usage
# Dry-run (default) - shows what would be deleted
safe-rm /path/to/delete

# Actually delete (if path is not protected)
safe-rm --force /path/to/delete
safe-rm -f /path/to/delete

Protected Paths

The script blocks deletion of:

System: /, /bin, /boot, /dev, /etc, /lib, /opt, /proc, /root, /sbin, /sys, /usr, /var, /home, /Users

Home config: ~, ~/.ssh, ~/.gnupg, ~/.config, ~/.local, ~/.claude, ~/.zshrc, ~/.bashrc

Project: .git, git repository root

Exit Codes
0 — success (or dry-run completed)
1 — path is protected
2 — path does not exist
Instructions for Claude
NEVER use rm -rf directly — always use safe-rm script
Run without --force first to preview what will be deleted
If path is protected, inform user and do not proceed
Only use --force after confirming dry-run output is correct
Weekly Installs
10
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass