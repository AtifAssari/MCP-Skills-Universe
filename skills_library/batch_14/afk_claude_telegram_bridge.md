---
title: afk-claude-telegram-bridge
url: https://skills.sh/gmotyl/afk-claude-telegram-bridge-skill/afk-claude-telegram-bridge
---

# afk-claude-telegram-bridge

skills/gmotyl/afk-claude-telegram-bridge-skill/afk-claude-telegram-bridge
afk-claude-telegram-bridge
Installation
$ npx skills add https://github.com/gmotyl/afk-claude-telegram-bridge-skill --skill afk-claude-telegram-bridge
SKILL.md
AFK Claude Telegram Bridge

Remote-control Claude Code sessions from your phone via Telegram when AFK (away from keyboard).

When to Use
"set up telegram bridge" / "configure telegram AFK"
"enable remote control" / "activate AFK mode"
"I want to control Claude from my phone"
Installing this skill on a new machine
What This Skill Does

Installs a complete Telegram ↔ Claude Code bridge that allows you to:

Approve/deny tool calls from Telegram inline keyboards
Continue tasks by sending new instructions when Claude finishes
Auto-approve read-only tools (Read, Glob, Grep, WebSearch, WebFetch)
Multi-session support — up to 4 concurrent sessions (S1-S4)
Zero native dependencies — uses Node.js built-in node:sqlite for session state and IPC (no native addons to compile)
Installation

Install via curl (recommended):

curl -fsSL https://raw.githubusercontent.com/gmotyl/afk-claude-telegram-bridge/main/install.sh | bash


Or from a local clone:

git clone https://github.com/gmotyl/afk-claude-telegram-bridge.git
cd afk-claude-telegram-bridge
npm install && npm run deploy


The installer downloads pre-built binaries from GitHub and handles everything:

Copies hook.js, bridge.js, cli.js, hook.sh to ~/.claude/hooks/telegram-bridge/
Installs /afk, /back, and /afk-reset commands to ~/.claude/commands/
Registers Stop, Notification, and PreToolUse hooks in ~/.claude/settings.json
Prompts for your bot token and auto-detects your Telegram group

Restart Claude Code after installation to load the new commands.

Prerequisites

Before running the installer, create a Telegram bot:

Open Telegram -> search @BotFather -> send /newbot
Name it "Claude Bridge" (or your preferred name)
Copy the bot token
Create a Telegram Group with Topics enabled
Add the bot to the group as Administrator
Send a message in the group (so the bot can detect it)
Usage
Activate AFK Mode

In any Claude Code session:

/afk


You'll see a confirmation on Telegram: "📡 S1 — AFK Activated"

Deactivate AFK Mode
/back

From Telegram

When Claude needs approval for a tool call, you'll see:

🔐 S1 — Permission Request
Tool: Bash
`npm install express`
[✅ Approve] [❌ Deny]


When Claude finishes a task:

✅ S1 — Task Complete
I've implemented the login form...
[🛑 Let it stop]


Reply with text to send Claude a new instruction!

Multi-Session

With multiple sessions, prefix instructions:

S1: now add unit tests
S2: push to remote

File Structure

After installation:

~/.claude/hooks/telegram-bridge/
  hook.sh        — Bash wrapper (Claude Code calls this)
  hook.js        — Compiled hook entry point (Node.js)
  bridge.js      — Compiled Telegram daemon (Node.js)
  config.json    — Bot token, group ID, settings
  bridge.db      — SQLite database (sessions, events, state)
  active_count   — Marker file for fast bash gate check
  daemon.log     — Daemon log

~/.claude/commands/
  afk.md         — /afk command
  back.md        — /back command
  afk-reset.md   — /afk-reset command

Commands Reference
Command	Description
hook.sh --activate <session_id> [project]	Activate AFK mode
hook.sh --deactivate <session_id>	Deactivate AFK mode
hook.sh --reset	Nuclear reset (kill daemons, clear state)
hook.sh --status	Show active sessions
hook.sh --setup	Configure bot token/chat_id
hook.sh --help	Show help
Troubleshooting
Daemon log: cat ~/.claude/hooks/telegram-bridge/daemon.log
Status: ~/.claude/hooks/telegram-bridge/hook.sh --status
Manual start: node ~/.claude/hooks/telegram-bridge/bridge.js
Kill daemon: Check PID in state.json, then kill <pid>
Dependencies
Node.js 22.5+ (required for built-in node:sqlite)
bash
Telegram bot token
How SQLite is Used

The bridge uses SQLite (via Node.js built-in node:sqlite) as its persistence and IPC layer:

Session management — tracks active AFK sessions, slot assignments, and Claude Code session bindings
Event queue — daemon and hooks communicate through a shared events table (permission requests, stop events, instructions)
Permission batching — buffers rapid-fire tool approval requests into single Telegram messages
Concurrent access — WAL mode allows the daemon (writer) and hooks (readers) to operate simultaneously without conflicts
Crash recovery — daemon reconstructs state from the database on restart
Changelog

See CHANGELOG.md for release history.

Credits

Originally built by Greg Motyl (@gmotyl).

Weekly Installs
23
Repository
gmotyl/afk-clau…ge-skill
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail