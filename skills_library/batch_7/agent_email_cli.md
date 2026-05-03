---
title: agent-email-cli
url: https://skills.sh/zaddy6/agent-email-skill/agent-email-cli
---

# agent-email-cli

skills/zaddy6/agent-email-skill/agent-email-cli
agent-email-cli
Installation
$ npx skills add https://github.com/zaddy6/agent-email-skill --skill agent-email-cli
Summary

Terminal-based disposable email inbox management for agent automation workflows.

Create temporary mailboxes, poll for new messages with configurable wait/interval, and retrieve full message details including body and source
JSON-native output with key fields (email, messageId, subject, from.address, createdAt) designed for agent parsing and summarization
Manage multiple mailbox profiles locally with accounts list, use, and remove commands; supports default alias for simplified scripting
Built-in safeguards: never logs secrets, surfaces structured error codes and hints, handles auth failures and rate limits with retry guidance
SKILL.md
Agent Email CLI
Overview

Use this skill to operate the agent-email command safely and predictably for agent workflows that need inbox access.

Prefer JSON-native command output and return key fields (email, messageId, subject, createdAt, from.address) in your summaries.

Workflow
Verify CLI availability.
command -v agent-email
agent-email --help


If missing, install:

npm install -g @zaddy6/agentemail
# or
bun install -g @zaddy6/agentemail

Create a mailbox account.
agent-email create


Record these fields from JSON output:

data.email
data.accountId
data.activeEmail

Do not record, repeat, or print secret values such as mailbox passwords or tokens.

Read latest messages.
agent-email read <email|default>


For inbox waiting/polling:

agent-email read <email|default> --wait 30 --interval 2


For full message payloads:

agent-email read <email|default> --full

Retrieve one message in detail.
agent-email show <email|default> <messageId>


Use show when you need body/source details for verification links, codes, or full content extraction.

Manage mailbox profiles.
agent-email accounts list
agent-email use <email|default>
agent-email accounts remove <email>


Avoid commands that require entering secrets on the command line in agent logs.

Delete processed/irrelevant message when requested.
agent-email delete <email|default> <messageId>

Operational Guidance
Keep command output machine-readable; avoid forcing human output unless requested.
Prefer default alias when user does not specify an email.
Never echo, store, or summarize secret values (password, token) from command output.
If command fails, surface the JSON error code and hint fields directly.
For auth failures (AUTH_REQUIRED/401), rerun command once and request user intervention if credentials must be re-established.
For rate limits (RATE_LIMITED/429), retry after short delay.
Troubleshooting
command not found: ensure ~/.bun/bin or npm global bin path is on PATH.
NO_ACTIVE_ACCOUNT: run agent-email create or agent-email use <email>.
ACCOUNT_NOT_FOUND: run agent-email accounts list and pick a valid address.
EOTP during npm publish: use npm trusted publishing for CI or publish locally with OTP.
References
For command cheat sheet and JSON field map, read references/commands.md.
Weekly Installs
2.1K
Repository
zaddy6/agent-email-skill
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail