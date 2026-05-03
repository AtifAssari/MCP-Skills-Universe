---
title: claude-skills-troubleshooting
url: https://skills.sh/daymade/claude-code-skills/claude-skills-troubleshooting
---

# claude-skills-troubleshooting

skills/daymade/claude-code-skills/claude-skills-troubleshooting
claude-skills-troubleshooting
Installation
$ npx skills add https://github.com/daymade/claude-code-skills --skill claude-skills-troubleshooting
SKILL.md
Claude Skills Troubleshooting
Overview

Diagnose and resolve common Claude Code plugin and skill configuration issues. This skill provides systematic debugging workflows for plugin installation, enablement, and activation problems.

Quick Diagnosis

Run the diagnostic script to identify common issues:

python3 scripts/diagnose_plugins.py


The script checks:

Installed vs enabled plugins mismatch
Missing enabledPlugins entries in settings.json
Stale marketplace cache
Invalid plugin configurations
Common Issues
Issue 1: Plugin Installed But Not Showing in Available Skills

Symptoms:

/plugin shows plugin as installed
Skill not appearing in Skill tool's available list
Plugin metadata exists in installed_plugins.json

Root Cause: Known bug (GitHub #17832) - plugins are added to installed_plugins.json but NOT automatically added to enabledPlugins in settings.json.

Diagnosis:

# Check if plugin is in installed_plugins.json
cat ~/.claude/plugins/installed_plugins.json | grep "plugin-name"

# Check if plugin is enabled in settings.json
cat ~/.claude/settings.json | grep "plugin-name"


Solution:

# Option 1: Use CLI to enable
claude plugin enable plugin-name@marketplace-name

# Option 2: Manually edit settings.json
# Add to enabledPlugins section:
# "plugin-name@marketplace-name": true

Issue 2: Understanding Plugin State Architecture

Key files:

File	Purpose
~/.claude/plugins/installed_plugins.json	Registry of ALL plugins (installed + disabled)
~/.claude/settings.json → enabledPlugins	Controls which plugins are ACTIVE
~/.claude/plugins/known_marketplaces.json	Registered marketplace sources
~/.claude/plugins/cache/	Actual plugin files

A plugin is active ONLY when:

Exists in installed_plugins.json (registered)
Listed in settings.json → enabledPlugins with value true
Issue 3: Marketplace Cache Stale

Symptoms:

GitHub has latest changes
Install finds plugin but gets old version
Newly added plugins not visible

Solution:

# Update marketplace cache
claude plugin marketplace update marketplace-name

# Or clear and re-fetch
rm -rf ~/.claude/plugins/cache/marketplace-name
claude plugin marketplace update marketplace-name

Issue 4: Plugin Not Found in Marketplace

Common causes (in order of likelihood):

Local changes not pushed to GitHub - Most common!

git status
git push
claude plugin marketplace update marketplace-name


marketplace.json configuration error

python3 -m json.tool .claude-plugin/marketplace.json


Skill directory missing

ls -la skill-name/SKILL.md

Diagnostic Commands Reference
Purpose	Command
List marketplaces	claude plugin marketplace list
Update marketplace	claude plugin marketplace update {name}
Install plugin	claude plugin install {plugin}@{marketplace}
Enable plugin	claude plugin enable {plugin}@{marketplace}
Disable plugin	claude plugin disable {plugin}@{marketplace}
Uninstall plugin	claude plugin uninstall {plugin}@{marketplace}
Check installed	cat ~/.claude/plugins/installed_plugins.json | jq '.plugins | keys'
Check enabled	cat ~/.claude/settings.json | jq '.enabledPlugins'
Batch Enable Missing Plugins

To enable all installed but disabled plugins from a marketplace:

python3 scripts/enable_all_plugins.py marketplace-name

Skills vs Commands Architecture

Claude Code has two types of user-invocable extensions:

Skills (in skills/ directory)

Auto-activated based on description matching
Loaded when user request matches skill description

Commands (in commands/ directory)

Explicitly invocable via /command-name
Appears in Skill tool's available list
Requires command file (e.g., commands/seer.md)

If a skill should be explicitly invocable, add a corresponding command file.

References
See references/known_issues.md for GitHub issue tracking
See references/architecture.md for detailed plugin architecture
Weekly Installs
252
Repository
daymade/claude-…e-skills
GitHub Stars
968
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn