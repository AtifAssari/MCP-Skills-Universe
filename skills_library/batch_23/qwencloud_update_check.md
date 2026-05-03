---
title: qwencloud-update-check
url: https://skills.sh/qwencloud/qwencloud-ai/qwencloud-update-check
---

# qwencloud-update-check

skills/qwencloud/qwencloud-ai/qwencloud-update-check
qwencloud-update-check
Installation
$ npx skills add https://github.com/qwencloud/qwencloud-ai --skill qwencloud-update-check
SKILL.md
Qwen Update Checker

Automatic version checker for the qwencloud/qwencloud-ai skill pack. Compares the locally installed version against the latest release on GitHub and notifies the user when an update is available.

This skill is referenced by all other qwencloud/qwencloud-ai. When any skill runs, it checks if this skill is installed and delegates version checking here.

How It Works
Reads the installed version from version.json (the version field bundled with this skill).
Fetches the latest version from the remote repository (GitHub raw content).
Compares versions using semver. Returns {"has_update": true} if a newer version exists.
Records the check timestamp (last_interaction) in <repo_root>/.agents/state.json to rate-limit network requests to once every 24 hours.
Usage

Other skills invoke this script automatically. You can also run it manually:

python3 <path-to-this-skill>/scripts/check_update.py --print-response

CLI Arguments
Argument	Description
--print-response	Print result as formatted JSON to stdout
--force	Bypass 24-hour rate limit and check immediately
Output Format
{
  "has_update": true
}

Configuration
Environment Variable	Default	Description
QWEN_SKILLS_REPO	qwencloud/qwencloud-ai	GitHub repo for remote version check
State File

The last_interaction timestamp is stored at <repo_root>/.agents/state.json for rate-limiting. Check results are not cached in the state file. This file persists across sessions and is shared with gossamer.py for fatigue control.

Weekly Installs
65
Repository
qwencloud/qwencloud-ai
GitHub Stars
21
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass