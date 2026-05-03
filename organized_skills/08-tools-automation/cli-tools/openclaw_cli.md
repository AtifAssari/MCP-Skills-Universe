---
rating: ⭐⭐⭐
title: openclaw-cli
url: https://skills.sh/irangareddy/openclaw-essentials/openclaw-cli
---

# openclaw-cli

skills/irangareddy/openclaw-essentials/openclaw-cli
openclaw-cli
Installation
$ npx skills add https://github.com/irangareddy/openclaw-essentials --skill openclaw-cli
SKILL.md
OpenClaw CLI

Complete reference for openclaw command-line interface operations.

When to Use

Managing OpenClaw gateway, agents, channels, skills, hooks, and automation.

Core Commands
Setup & Onboarding

Initial setup:

# Quick onboarding with daemon install
openclaw onboard --install-daemon

# Setup workspace and config
openclaw setup --workspace ~/.openclaw/workspace

# Interactive configuration
openclaw configure


Health check:

openclaw doctor

Gateway Management

Run gateway:

# Interactive mode
openclaw gateway

# With specific port
openclaw gateway --port 18789

# With tailscale
openclaw gateway --tailscale serve


Gateway service:

# Install as system service
openclaw gateway install

# Control service
openclaw gateway start
openclaw gateway stop
openclaw gateway restart
openclaw gateway status


Gateway health:

openclaw status
openclaw status --deep     # Probe channels
openclaw health

Agent Management

List agents:

openclaw agents list
openclaw agents list --bindings    # Show routing


Add agent:

# Interactive wizard
openclaw agents add <name>

# Non-interactive
openclaw agents add dev \
  --workspace ~/.openclaw/workspace-dev \
  --model claude-sonnet-4.5 \
  --non-interactive


Delete agent:

openclaw agents delete <id>


Set identity:

# From IDENTITY.md
openclaw agents set-identity --agent main --from-identity

# Explicit values
openclaw agents set-identity --agent main \
  --name "MyAgent" \
  --emoji "🤖" \
  --avatar avatars/bot.png

Skills Management

List skills:

openclaw skills list
openclaw skills list --eligible    # Only ready skills
openclaw skills list --json        # JSON output


Skill info:

openclaw skills info <skill-name>


Check eligibility:

openclaw skills check

Hooks Management

List hooks:

openclaw hooks list
openclaw hooks list --eligible
openclaw hooks list --verbose      # Show missing requirements


Hook info:

openclaw hooks info <hook-name>


Enable/disable:

openclaw hooks enable session-memory
openclaw hooks disable command-logger


Install hooks:

# From npm
openclaw hooks install @openclaw/my-hooks

# Local directory
openclaw hooks install ./my-hooks

# Link (development)
openclaw hooks install -l ./my-hooks


Update hooks:

openclaw hooks update <id>
openclaw hooks update --all

Channel Management

List channels:

openclaw channels list


Channel status:

openclaw channels status
openclaw channels status --probe


Add channel:

# Interactive
openclaw channels add

# Telegram bot
openclaw channels add --channel telegram \
  --account alerts \
  --name "Alerts Bot" \
  --token $TELEGRAM_BOT_TOKEN

# Discord
openclaw channels add --channel discord \
  --account work \
  --token $DISCORD_BOT_TOKEN


Remove channel:

openclaw channels remove --channel telegram --account alerts
openclaw channels remove --channel discord --account work --delete


WhatsApp login:

openclaw channels login --channel whatsapp


Channel logs:

openclaw channels logs
openclaw channels logs --channel whatsapp --lines 100

Models & Authentication

Status:

openclaw models status
openclaw models status --probe               # Live check
openclaw models status --probe-provider anthropic


List models:

openclaw models list
openclaw models list --all
openclaw models list --provider anthropic


Set default:

openclaw models set claude-sonnet-4.5
openclaw models set-image claude-sonnet-4.5


Auth setup:

# Anthropic (recommended)
claude setup-token
openclaw models auth setup-token --provider anthropic

# Or paste token
openclaw models auth paste-token --provider anthropic


Fallbacks:

openclaw models fallbacks list
openclaw models fallbacks add claude-opus-4.6
openclaw models fallbacks remove claude-haiku-4.5
openclaw models fallbacks clear


Scan for models:

openclaw models scan
openclaw models scan --set-default

Messaging

Send message:

openclaw message send \
  --target +15555550123 \
  --message "Hello from OpenClaw"

# Discord channel
openclaw message send \
  --channel discord \
  --target channel:123456 \
  --message "Deployment complete"


Send poll:

openclaw message poll \
  --channel discord \
  --target channel:123 \
  --poll-question "Lunch?" \
  --poll-option "Pizza" \
  --poll-option "Sushi"


Other message operations:

openclaw message read --target +15555550123
openclaw message react --target <id> --emoji "👍"
openclaw message edit --target <id> --message "Updated"
openclaw message delete --target <id>

Browser Control

Status & control:

openclaw browser status
openclaw browser start
openclaw browser stop
openclaw browser tabs


Navigate:

openclaw browser open https://example.com
openclaw browser navigate https://example.com --target-id <id>


Interact:

openclaw browser click "#submit-button"
openclaw browser type "#email" "user@example.com"
openclaw browser press Enter


Capture:

openclaw browser screenshot
openclaw browser screenshot --full-page
openclaw browser snapshot --format ai


Profiles:

openclaw browser profiles
openclaw browser create-profile --name dev
openclaw browser delete-profile --name old

Nodes & Devices

List nodes:

openclaw nodes list
openclaw nodes status --connected


Node operations:

# Describe node
openclaw nodes describe --node <id>

# Run command on node
openclaw nodes run --node <id> --cwd /path -- ls -la

# Notify (macOS)
openclaw nodes notify --node <id> \
  --title "Build Complete" \
  --body "Success" \
  --sound default


Camera:

openclaw nodes camera list --node <id>
openclaw nodes camera snap --node <id> --facing front
openclaw nodes camera clip --node <id> --duration 10s


Canvas:

openclaw nodes canvas snapshot --node <id>
openclaw nodes canvas present --node <id> --target index.html
openclaw nodes canvas hide --node <id>


Screen recording:

openclaw nodes screen record --node <id> --duration 30s

System Commands

System event:

openclaw system event --text "Deployment complete" --mode now


Heartbeat:

openclaw system heartbeat last
openclaw system heartbeat enable
openclaw system heartbeat disable


Presence:

openclaw system presence

Cron Jobs

List jobs:

openclaw cron list
openclaw cron list --all
openclaw cron status


Add job:

# System event every hour
openclaw cron add \
  --name "hourly-check" \
  --every "1h" \
  --system-event "Hourly check"

# Message at specific time
openclaw cron add \
  --name "morning-reminder" \
  --at "09:00" \
  --message "Good morning!"


Manage jobs:

openclaw cron enable <id>
openclaw cron disable <id>
openclaw cron rm <id>
openclaw cron run <id>


Job runs:

openclaw cron runs --id <id> --limit 10

Configuration

Get/set config:

# Get value
openclaw config get agents.defaults.model.primary

# Set value
openclaw config set agents.defaults.model.primary "claude-sonnet-4.5"

# Unset value
openclaw config unset some.config.path

Memory Operations

Memory status:

openclaw memory status


Index memory:

openclaw memory index


Search memory:

openclaw memory search "GraphQL implementation patterns"

Logs

Tail logs:

openclaw logs
openclaw logs --follow
openclaw logs --limit 200
openclaw logs --json

Sandbox

List sandboxes:

openclaw sandbox list


Recreate sandbox:

openclaw sandbox recreate

Security

Security audit:

openclaw security audit
openclaw security audit --deep
openclaw security audit --fix

Plugins

List plugins:

openclaw plugins list
openclaw plugins list --json


Plugin info:

openclaw plugins info <plugin-id>


Install plugin:

openclaw plugins install <path-or-spec>


Enable/disable:

openclaw plugins enable <id>
openclaw plugins disable <id>


Plugin health:

openclaw plugins doctor

Update & Maintenance

Update OpenClaw:

openclaw update


Reset config:

openclaw reset --scope config
openclaw reset --scope config+creds+sessions
openclaw reset --scope full


Uninstall:

openclaw uninstall --service
openclaw uninstall --state
openclaw uninstall --workspace
openclaw uninstall --all

Global Flags

Available everywhere:

--dev               # Use ~/.openclaw-dev for isolation
--profile <name>    # Use ~/.openclaw-<name>
--no-color         # Disable ANSI colors
--json             # Machine-readable output
-V, --version      # Show version

Common Workflows
First-Time Setup
# 1. Onboard with daemon
openclaw onboard --install-daemon

# 2. Pair WhatsApp (or other channel)
openclaw channels login

# 3. Start gateway
openclaw gateway

# 4. Test with message
openclaw message send --target +1234567890 --message "Test"

Multi-Agent Setup
# 1. Add agent
openclaw agents add work --workspace ~/.openclaw/workspace-work

# 2. Set identity
openclaw agents set-identity --agent work --from-identity

# 3. Add binding (in openclaw.json)
# bindings: [{ agentId: "work", match: { channel: "discord" } }]

# 4. List to verify
openclaw agents list --bindings

Hook Automation
# 1. Enable session memory hook
openclaw hooks enable session-memory

# 2. Enable command logger
openclaw hooks enable command-logger

# 3. Verify
openclaw hooks check

# 4. Restart gateway
openclaw gateway restart

Channel Setup
# 1. Add Telegram bot
openclaw channels add --channel telegram \
  --account alerts \
  --token $TELEGRAM_BOT_TOKEN

# 2. Verify
openclaw channels status

# 3. Send test message
openclaw message send --channel telegram \
  --target <chat-id> \
  --message "Bot online"

Model Configuration
# 1. Setup auth
claude setup-token

# 2. Set default model
openclaw models set claude-sonnet-4.5

# 3. Add fallbacks
openclaw models fallbacks add claude-opus-4.6
openclaw models fallbacks add claude-haiku-4.5

# 4. Verify
openclaw models status

Debugging

Check gateway status:

openclaw status --deep
openclaw doctor
openclaw health


View logs:

openclaw logs --follow
openclaw channels logs --lines 200


Test channel:

openclaw channels status --probe


Check skills/hooks:

openclaw skills check
openclaw hooks check
openclaw plugins doctor

Tips
Use --json for scripting - All commands support JSON output
Profile isolation - Use --profile for testing without affecting main config
Doctor fixes - Run openclaw doctor regularly to catch issues
Logs location - ~/.openclaw/logs/ for file logs
Config location - ~/.openclaw/openclaw.json
Workspace - ~/.openclaw/workspace (or custom path)
Resources
OpenClaw Docs
CLI Reference
Multi-Agent Routing
Hooks System
Skills System
Weekly Installs
277
Repository
irangareddy/ope…sentials
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail