---
rating: ⭐⭐
title: update
url: https://skills.sh/boshu2/agentops/update
---

# update

skills/boshu2/agentops/update
update
Installation
$ npx skills add https://github.com/boshu2/agentops --skill update
SKILL.md
/update — Reinstall AgentOps Skills

Purpose: One command to pull the latest skills from the repo and install them globally across all agents.

YOU MUST EXECUTE THIS WORKFLOW. Do not just describe it.

Execution
Step 1: Install
bash <(curl -fsSL https://raw.githubusercontent.com/boshu2/agentops/main/scripts/install.sh)


Run this command. Wait for it to complete.

Step 2: Verify

Confirm the output shows all skills installed with no failures.

If any skills failed to install, report which ones failed and suggest re-running the installer. If the failure is isolated to one skill, tell the user to inspect the target agent's installed skill or plugin directory and restore just that skill from the latest repo copy.

# Retry the full installer:
bash <(curl -fsSL https://raw.githubusercontent.com/boshu2/agentops/main/scripts/install.sh)

Step 3: Report

Tell the user:

How many skills installed successfully
Any failures and how to fix them
Examples
Routine skill update

User says: /update

What happens:

Runs the install script to pull the latest skills from the repository and install them globally.
Verifies the output confirms all skills installed with no failures.
Reports the total count of successfully installed skills.

Result: All AgentOps skills are updated to the latest version and available globally across all agent sessions.

Recovering from a partial failure

User says: /update (after a previous run failed for some skills)

What happens:

Re-runs the install script which re-downloads and overwrites all skills from the latest source.
Detects that 2 of 50 skills failed to install and identifies them by name.
Reports the failures and provides manual sync commands as a fallback.

Result: 48 skills installed successfully, with clear instructions to retry the installer and recover the 2 failed skills from the latest repo copy if needed.

Troubleshooting
Problem	Cause	Solution
curl: command not found	curl is not installed	Install curl via your package manager
Download fails	Network or GitHub unreachable	Check connectivity; retry
Individual skills fail	Permissions issue in the agent's install or plugin directory	Fix permissions on the target agent's install home, then re-run /update
Skills not available after install	Agent session not restarted	Restart your agent session
EACCES: permission denied	Restrictive permissions on the install target	Fix permissions on the install target, then re-run /update
Weekly Installs
449
Repository
boshu2/agentops
GitHub Stars
323
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail