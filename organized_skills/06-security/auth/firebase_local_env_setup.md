---
rating: ⭐⭐⭐
title: firebase-local-env-setup
url: https://skills.sh/firebase/agent-skills/firebase-local-env-setup
---

# firebase-local-env-setup

skills/firebase/agent-skills/firebase-local-env-setup
firebase-local-env-setup
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill firebase-local-env-setup
Summary

Prerequisite setup for Firebase agent integration: Node.js, CLI authentication, and MCP server installation.

Verifies Node.js v20+ installation and guides setup via nvm or official installers for macOS, Linux, and Windows
Confirms Firebase CLI availability through npx firebase-tools and authenticates via firebase login with remote environment support
Directs agent-specific MCP server and skill installation for Gemini CLI, Antigravity, Claude Code, Cursor, GitHub Copilot, and other platforms
Enforces completion of all four verification steps before proceeding to other Firebase tasks
SKILL.md
Firebase Local Environment Setup

This skill documents the bare minimum setup required for a full Firebase experience for the agent. Before starting to use any Firebase features, you MUST verify that each of the following steps has been completed.

1. Verify Node.js

Action: Run node --version.

Handling: Ensure Node.js is installed and the version is >= 20. If Node.js is missing or < v20, install it based on the operating system:

Recommended: Use a Node Version Manager This avoids permission issues when installing global packages.

For macOS or Linux:

Guide the user to the official nvm repository.
Request the user to manually install nvm and reply when finished. Stop and wait for the user's confirmation.
Make nvm available in the current terminal session by sourcing the appropriate profile:
# For Bash
source ~/.bash_profile
source ~/.bashrc

# For Zsh
source ~/.zprofile
source ~/.zshrc

Install Node.js:
nvm install 24
nvm use 24


For Windows:

Guide the user to download and install nvm-windows.
Request the user to manually install nvm-windows and Node.js, and reply when finished. Stop and wait for the user's confirmation.
After the user confirms, verify Node.js is available:
node --version


Alternative: Official Installer

Guide the user to download and install the LTS version from nodejs.org.
Request the user to manually install Node.js and reply when finished. Stop and wait for the user's confirmation.
2. Verify Firebase CLI

The Firebase CLI is the primary tool for interacting with Firebase services.

Action: Run npx -y firebase-tools@latest --version.
Handling: Ensure this command runs successfully and outputs a version number.
3. Verify Firebase Authentication

You must be authenticated to manage Firebase projects.

Action: Run npx -y firebase-tools@latest login.
Handling: If the environment is remote or restricted (no browser access), run npx -y firebase-tools@latest login --no-localhost instead.
4. Install Agent Skills and MCP Server

To fully manage Firebase, the agent needs specific skills and the Firebase MCP server installed. Identify the agent environment you are currently running in and follow the corresponding setup document strictly.

Read the setup document for your current agent:

Gemini CLI: Review references/gemini_cli.md
Antigravity: Review references/antigravity.md
Claude Code: Review references/claude_code.md
Cursor: Review references/cursor.md
GitHub Copilot: Review references/github_copilot.md
Other Agents (Windsurf, Cline, etc.): Review references/other_agents.md

CRITICAL AGENT RULE: Do NOT proceed with any other Firebase tasks until EVERY step above has been successfully verified and completed.

Weekly Installs
5.0K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn