---
rating: ⭐⭐⭐
title: cyrus-setup-prerequisites
url: https://skills.sh/ceedaragents/cyrus/cyrus-setup-prerequisites
---

# cyrus-setup-prerequisites

skills/ceedaragents/cyrus/cyrus-setup-prerequisites
cyrus-setup-prerequisites
Installation
$ npx skills add https://github.com/ceedaragents/cyrus --skill cyrus-setup-prerequisites
SKILL.md

CRITICAL: Never use Read, Edit, or Write tools on ~/.cyrus/.env or any file inside ~/.cyrus/. Use only Bash commands (grep, printf >>, etc.) to interact with env files — secrets must never be read into the conversation context.

Setup Prerequisites

Checks system prerequisites and installs cyrus-ai.

Step 1: Detect Package Manager

If the user hasn't already specified their preferred package manager, ask:

Which package manager do you prefer? npm, pnpm, bun, or yarn?

Store the answer for use in this and subsequent skills.

Step 2: Check System Dependencies

Run the following checks and report results:

# Node.js >= 18
node --version

# jq (required for Claude Code parsing)
jq --version

# GitHub CLI (required for GitHub integration)
gh --version


For each missing dependency, provide the install command:

Dependency	macOS	Linux/Ubuntu
Node.js	brew install node	curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs
jq	brew install jq	sudo apt install -y jq
gh	brew install gh	See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

If all dependencies are present, print a checkmark for each and continue.

If any are missing, offer to install them (detect OS via uname). Wait for user confirmation before installing.

Step 3: Check for agent-browser (Optional)

If the user selected any integration surface (Linear, GitHub, Slack), check for agent-browser:

which agent-browser


If installed, ensure it's up to date:

npm update -g agent-browser


If not found, inform the user:

agent-browser is optional but enables automated app creation for Linear/GitHub/Slack. Without it, you'll be guided through manual setup steps instead.

Install with: npm install -g agent-browser

Do NOT block on this — it's optional. Note whether it's available for downstream skills.

Step 4: Install cyrus-ai

Check if already installed:

which cyrus


If not found, install using the user's preferred package manager:

# npm
npm install -g cyrus-ai

# pnpm
pnpm install -g cyrus-ai

# bun
bun install -g cyrus-ai

# yarn
yarn global add cyrus-ai


Verify installation:

cyrus --version

Step 5: Ensure ~/.cyrus directory exists
mkdir -p ~/.cyrus


If ~/.cyrus/.env already exists, note it and inform the user that existing values will be preserved.

Completion

Print a summary:

Prerequisites:
  ✓ Node.js v22.x
  ✓ jq 1.7
  ✓ gh 2.x
  ✓ cyrus-ai installed
  ✓ agent-browser available (or: ⚠ not installed — manual setup mode)

Weekly Installs
135
Repository
ceedaragents/cyrus
GitHub Stars
564
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn