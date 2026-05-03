---
title: zeroclaw
url: https://skills.sh/perseusmx/zeroclaw-skill/zeroclaw
---

# zeroclaw

skills/perseusmx/zeroclaw-skill/zeroclaw
zeroclaw
Installation
$ npx skills add https://github.com/perseusmx/zeroclaw-skill --skill zeroclaw
SKILL.md
ZeroClaw Quick Reference

This skill was verified against the official ZeroClaw docs and GitHub tags on March 28, 2026. Current latest upstream release at verification time: v0.6.5 (released March 27, 2026).

ZeroClaw is a small Rust runtime for autonomous AI assistants with swappable providers, tools, memory, channels, and peripherals.

Core characteristics:

Single binary workflow with fast startup and low memory footprint
Config file: ~/.zeroclaw/config.toml
Workspace marker: ~/.zeroclaw/active_workspace.toml
Workspace data: ~/.zeroclaw/workspace/
Auth profiles: ~/.zeroclaw/auth-profiles.json
Installation
Install
# Homebrew (macOS/Linux)
brew install zeroclaw

# Clone + bootstrap
git clone https://github.com/zeroclaw-labs/zeroclaw.git
cd zeroclaw && ./bootstrap.sh

# Cargo
cargo install zeroclaw

Update
# Preferred when installed via Homebrew
brew upgrade zeroclaw

# Built-in updater
zeroclaw update --check
zeroclaw update
zeroclaw update --instructions

Onboarding
ZEROCLAW_API_KEY="..." zeroclaw onboard --provider openrouter
zeroclaw onboard --interactive
zeroclaw onboard --channels-only
zeroclaw onboard --force


Notes:

Interactive onboarding now supports full overwrite or provider-only updates.
Existing configs are preserved unless you explicitly force replacement.
OpenClaw migration is merge-first.
Essential Commands
Daily Use
zeroclaw agent - Interactive chat
zeroclaw agent -m "message" - Single-message mode
zeroclaw daemon - Start the supervised runtime
zeroclaw gateway - Start the webhook/WhatsApp gateway
Diagnostics
zeroclaw status - Current config and system summary
zeroclaw doctor - Run diagnostics
zeroclaw doctor models --provider <id> - Provider/model checks
zeroclaw doctor traces --limit 20 - Runtime trace inspection
Providers and Models
zeroclaw providers - List providers and aliases
zeroclaw providers-quota - Show quota and health
zeroclaw models refresh - Refresh model catalogs
zeroclaw models refresh --provider <id> - Refresh one provider
Config and Control
zeroclaw config show - Print effective config with masked secrets
zeroclaw config get <dot.path> - Read one value
zeroclaw config set <dot.path> <value> - Persist one value
zeroclaw config schema - Print JSON Schema
zeroclaw estop - Engage emergency stop
zeroclaw estop status|resume - Inspect or resume E-Stop
Channels and Skills
zeroclaw channel list|start|doctor - Channel operations
zeroclaw skills list|install|audit|remove - Skill management
Services, Scheduling, Hardware
zeroclaw service install|start|stop|restart|status|uninstall
zeroclaw cron list|add|add-at|add-every|once|remove
zeroclaw hardware discover|introspect <port>
zeroclaw peripheral list|add <name> <port>|flash
Other
zeroclaw security update-guard-corpus - Refresh security guard corpus
zeroclaw integrations info <name> - Inspect integration details
zeroclaw migrate openclaw [--dry-run] - Import from OpenClaw
zeroclaw completions bash|fish|zsh|powershell|elvish
Providers Overview

The current upstream provider reference documents a broad mixed catalog of hosted, local, and OAuth-backed providers.

Common provider IDs:

Hosted: openrouter, anthropic, openai, gemini, groq, mistral, deepseek, xai, cohere, perplexity, fireworks, novita, vercel, cloudflare, nvidia
Regional/specialized: qwen, doubao, qianfan, glm, zai, minimax, moonshot, stepfun, hunyuan, siliconflow
Local/server: ollama, lmstudio, llamacpp, sglang, vllm, osaurus
Other integrations: cursor, copilot, bedrock, synthetic, opencode

Credential resolution order:

Explicit credential from config or CLI
Provider-specific environment variable
Fallback ZEROCLAW_API_KEY
Fallback API_KEY

Quick custom provider setup:

default_provider = "custom:https://your-api.example.com"
default_model = "your-model-id"


See full catalog and notes: PROVIDERS.md

Channels Overview

The current upstream channels reference documents these active channel surfaces:

cli
telegram, discord, slack, mattermost
matrix, signal, whatsapp, wati
webhook, email, irc
lark, feishu, dingtalk
qq, napcat, linq
imessage, nextcloud_talk, nostr
acp

Runtime chat commands on supported channels:

/models, /models <provider>
/model, /model <model-id>
/new
/approve-request, /approve-confirm, /approve-allow, /approve-deny, /approve-pending, /approve, /unapprove, /approvals

See detailed setup: CHANNELS.md

Configuration Overview

Config resolution at startup:

ZEROCLAW_WORKSPACE
~/.zeroclaw/active_workspace.toml
Default ~/.zeroclaw/config.toml

Basic provider setup:

default_provider = "openrouter"
default_model = "anthropic/claude-sonnet-4-6"
default_temperature = 0.7


Autonomy levels:

Level	Description
supervised	Approval for all risky actions; highest restriction
assisted	Allowlisted commands with moderated automation
full	No approval gating; trusted machines only
[autonomy]
level = "supervised"
workspace_only = true
allowed_commands = ["git", "npm", "cargo", "ls", "cat"]
max_actions_per_hour = 20
max_cost_per_day_cents = 500


Useful sections to know:

[model_providers.<name>] - Named provider profiles and custom endpoints
[observability] - OTel/log tracing and runtime traces
[gateway] - Pairing and bind controls
[security.estop] - Emergency-stop behavior
[skills] - Skill install policy and trusted roots

See config reference: CONFIG.md See security guidance: SECURITY.md

Troubleshooting
Quick Checks
zeroclaw --version
zeroclaw status
zeroclaw doctor
zeroclaw doctor traces --limit 20
zeroclaw channel doctor

Common Issues
Problem	What to check
Provider requests fail	API key source, provider ID, zeroclaw providers, zeroclaw models refresh --provider <id>
Channel connected but silent	Correct allowlist field, bot membership, callback reachability for webhook channels
Config changes ignored	zeroclaw config show, workspace resolution, channel/daemon restart if needed
Updates unclear	zeroclaw update --instructions and zeroclaw --version
Runtime acting too freely	[autonomy] level, allowlists, zeroclaw estop status
Log Capture
RUST_LOG=info zeroclaw daemon 2>&1 | tee /tmp/zeroclaw.log
rg -n "error|warn|channel|provider|estop" /tmp/zeroclaw.log

Weekly Installs
21
Repository
perseusmx/zeroclaw-skill
GitHub Stars
2
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn