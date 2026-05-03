---
rating: ⭐⭐⭐
title: setup-agent-tail
url: https://skills.sh/qdhenry/claude-command-suite/setup-agent-tail
---

# setup-agent-tail

skills/qdhenry/claude-command-suite/setup-agent-tail
setup-agent-tail
Installation
$ npx skills add https://github.com/qdhenry/claude-command-suite --skill setup-agent-tail
SKILL.md

<quick_start> Run the auto-detect workflow below. The skill will:

Detect project framework and structure
Propose a configuration
Install agent-tail after user confirms
Configure framework plugins, CLI scripts, and gitignore </quick_start>

<essential_principles>

Logs are written to tmp/logs/latest/ — this is agent-tail's standard output directory
The tmp/ directory must be gitignored
Browser log capture requires a framework plugin (Vite or Next.js) in addition to the CLI
For monorepos, use agent-tail-core init at root and agent-tail-core wrap in each package
Always confirm the proposed configuration with the user before making changes </essential_principles>

Read these files to determine the project setup:

package.json — check for framework dependencies (vite, next, react, etc.) and existing scripts
vite.config.ts / vite.config.js — Vite project indicator
next.config.ts / next.config.js / next.config.mjs — Next.js project indicator
turbo.json / nx.json / pnpm-workspace.yaml / lerna.json — monorepo indicators
.gitignore — check if tmp/ is already ignored

Classify the project as one of:

vite — Vite-based project (React, Vue, Svelte, etc.)
nextjs — Next.js project
monorepo — Turborepo, Nx, pnpm workspaces, or Lerna
node-cli — Plain Node.js / any other project (CLI-only setup)

Step 2: Gather user preferences

Use AskUserQuestion to confirm detection and gather preferences:

Question 1: "I detected a [framework] project. Is this correct?"
  - Yes, proceed
  - No, it's actually [other options]

Question 2: "Which services should agent-tail manage?"
  - Based on detected scripts in package.json (e.g., "dev", "api", "worker")
  - Let user add custom service names and commands

Question 3: "Configure output destinations?"
  - Default (tmp/logs/latest/) (Recommended)
  - Custom directory
  - Custom directory with combined.log disabled

Question 4: "Set up browser console log capture?"
  - Yes (Recommended) — if Vite or Next.js detected
  - No, server logs only
  - [Skip this question for node-cli projects]


Step 3: Install agent-tail

# Detect package manager from lockfile
# bun.lock → bun
# pnpm-lock.yaml → pnpm
# yarn.lock → yarn
# package-lock.json → npm

<pkg-manager> add -D agent-tail agent-tail-core


Important: The agent-tail umbrella package has a broken bin field that prevents the CLI from being linked. You must also install agent-tail-core explicitly — this is the package that provides the actual agent-tail-core CLI binary. Use agent-tail-core (not agent-tail) as the command name in all scripts.

Step 4: Configure framework plugin

For each detected framework, apply the appropriate configuration. See references/framework-configs.md for exact code.

Vite: Add agentTail() plugin to vite.config
Next.js: Wrap config with withAgentTail(), add AgentTailScript to layout, create browser log API route
Monorepo: Add agent-tail init to root dev script, wrap each package with agent-tail wrap
Node CLI: No plugin needed, just CLI configuration

Step 5: Configure package.json scripts

Update package.json scripts to use agent-tail-core CLI. Transform existing dev scripts:

{
  "scripts": {
    "dev": "agent-tail-core run '<service1>: <original-command>' '<service2>: <original-command>'"
  }
}


If user specified excludes or muting, add flags:

{
  "scripts": {
    "dev": "agent-tail-core run --exclude '[HMR]' --mute worker '<services>'"
  }
}


Step 6: Update .gitignore

Add tmp/ to .gitignore if not already present.

Step 7: Verify setup

After configuration, tell the user:

Run their dev script to verify logs appear in tmp/logs/latest/
Check that individual service logs and combined.log are created
If browser logging was enabled, verify console output appears in the browser log file

<configuration_options> These options can be presented to the user during setup:

Output directory: Where logs are written (default: tmp/logs/latest/)

Excludes: Filter noisy log lines by substring or regex:

Common Vite excludes: [HMR], [vite], Download the React DevTools
Common Next.js excludes: [Fast Refresh], compiled successfully

Service muting: Hide specific services from terminal output while preserving log files:

Useful for noisy frontend dev servers when focused on backend work

Browser log capture: Capture console.*, unhandled errors, and unhandled promise rejections from the browser

Log format: All logs use timestamp + level + message format: [10:30:00.123] [LOG ] Message here

Gitignore warning: Agent-tail warns on startup if tmp/ is not gitignored. Disable with warnOnMissingGitignore: false in plugin options. </configuration_options>

<anti_patterns> For Vite/Next.js projects, the CLI alone does not capture browser console logs. The framework plugin is required for browser log capture.

<success_criteria> Setup is complete when:

agent-tail is installed as a dev dependency
Framework plugin configured (if Vite or Next.js)
package.json dev script wraps services with agent-tail
tmp/ is in .gitignore
User has been told how to verify the setup works </success_criteria>

<reference_guides> Framework-specific configuration code: See references/framework-configs.md </reference_guides>

Weekly Installs
12
Repository
qdhenry/claude-…nd-suite
GitHub Stars
1.2K
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail