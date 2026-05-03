---
rating: ⭐⭐⭐
title: hyva-exec-shell-cmd
url: https://skills.sh/hyva-themes/hyva-ai-tools/hyva-exec-shell-cmd
---

# hyva-exec-shell-cmd

skills/hyva-themes/hyva-ai-tools/hyva-exec-shell-cmd
hyva-exec-shell-cmd
Installation
$ npx skills add https://github.com/hyva-themes/hyva-ai-tools --skill hyva-exec-shell-cmd
SKILL.md
Execute Shell Commands in Magento Environment

This utility skill detects the Magento development environment and provides the appropriate command wrapper for executing shell commands.

Usage

Other skills should reference this skill when they need to execute commands in the Magento environment. The detected wrapper ensures commands run in the correct context (container or local).

Step 1: Detect Environment

Important: Execute this script from the Magento project root directory, or provide the path as an argument.

Run this detection once at the start of any skill that needs to execute shell commands:

<skill_path>/scripts/detect_env.sh [magento_root_path]


Where <skill_path> is the directory containing this SKILL.md file (e.g., .claude/skills/hyva-exec-shell-cmd).

The optional magento_root_path argument specifies the Magento installation directory. If omitted, the script uses the current working directory.

Output: warden, docker-magento, ddev, or local

Step 2: Apply Command Wrapper

Based on detected environment, wrap commands as follows:

Environment	Command Wrapper	Description
Warden	warden env exec -T php-fpm bash -c "<command>"	Docker environment managed by Warden
docker-magento	bin/clinotty bash -c "<command>"	Mark Shust's docker-magento setup
DDEV	ddev exec <command>	DDEV containerized environment
Local	Run <command> directly	Native environment without containers
Examples
Single command
# Warden
warden env exec -T php-fpm bash -c "bin/magento cache:clean"

# docker-magento
bin/clinotty bash -c "bin/magento cache:clean"

# DDEV
ddev exec bin/magento cache:clean

# Local
bin/magento cache:clean

Command with directory change
# Warden
warden env exec -T php-fpm bash -c "cd vendor/hyva-themes/magento2-default-theme/web/tailwind && npm run build"

# docker-magento
bin/clinotty bash -c "cd vendor/hyva-themes/magento2-default-theme/web/tailwind && npm run build"

# DDEV
ddev exec bash -c "vendor/hyva-themes/magento2-default-theme/web/tailwind && npm run build"

# Local
cd vendor/hyva-themes/magento2-default-theme/web/tailwind && npm run build

Commands That Do NOT Require Wrapping

Some commands run on the host system and should NOT be wrapped:

composer commands (runs on host, not in container)
git commands
File operations on the host filesystem (ls, find, cp for files accessible from host)
warden CLI commands
ddev CLI commands
Integration Pattern

Skills that need to execute commands should:

Reference this skill: "Use the hyva-exec-shell-cmd skill to determine the command wrapper"
Detect environment once using Step 1
Store the wrapper pattern for use throughout the skill
Apply the wrapper to all container commands per Step 2
Weekly Installs
318
Repository
hyva-themes/hyv…ai-tools
GitHub Stars
65
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass