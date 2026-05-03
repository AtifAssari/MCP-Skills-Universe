---
rating: ⭐⭐⭐
title: glean-cli-chat
url: https://skills.sh/gleanwork/glean-cli/glean-cli-chat
---

# glean-cli-chat

skills/gleanwork/glean-cli/glean-cli-chat
glean-cli-chat
Installation
$ npx skills add https://github.com/gleanwork/glean-cli --skill glean-cli-chat
SKILL.md
glean chat

PREREQUISITE: Read ../glean-cli/SKILL.md for auth, global flags, and security rules.

Have a conversation with Glean AI. Streams response to stdout.

glean chat [flags]

Flags
Flag	Type	Default	Description
--dry-run	boolean	false	Print request body without sending
--json	string		Complete JSON chat request body (overrides individual flags)
--message	string		Chat message (positional arg) (required)
--save	boolean	true	Save the chat session
--timeout	integer	30000	Request timeout in milliseconds
Examples
glean chat "What are the company holidays?"
glean chat --json '{"messages":[{"author":"USER","messageType":"CONTENT","fragments":[{"text":"What is Glean?"}]}]}'

Discovering Commands
# Show machine-readable schema for this command
glean schema chat

# List all available commands
glean schema | jq '.commands'

Weekly Installs
35
Repository
gleanwork/glean-cli
GitHub Stars
45
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass