---
title: whapi
url: https://skills.sh/whapi-cloud/whapi-whatsapp-api-skill/whapi
---

# whapi

skills/whapi-cloud/whapi-whatsapp-api-skill/whapi
whapi
Installation
$ npx skills add https://github.com/whapi-cloud/whapi-whatsapp-api-skill --skill whapi
SKILL.md
WHAPI.cloud WhatsApp API — Agent Skill

Practical guide for AI agents building WhatsApp integrations via WHAPI.cloud. Contains rules across 7 categories, prioritized to prevent the most frequent mistakes and cover the most-used API features.

Prerequisites — MCP Setup Check

Before starting any task, verify that the whapi-mcp MCP server is available:

Attempt to call the checkHealth tool.
If it responds successfully — proceed.
If the tool is not found — the MCP server is not installed. Guide the user through installation: references/core-mcp-setup.md.
If the tool returns 404 ("Channel not found") — the token is invalid or the channel does not exist. Guide the user: references/core-mcp-setup.md section "Token is Missing or Invalid".
If the tool responds, check status.text in the response:
status.text	Meaning	Action
AUTH	Connected and operational	Proceed
QR	Waiting for QR code scan	Open the channel dashboard and scan the QR code to pair
INIT	Server initialization	Wait 40-50 seconds; if persists, contact WHAPI support
LAUNCH	Connecting to WhatsApp account	Wait a few seconds; if persists, contact WHAPI support
STOP	Channel deactivated	Check subscription status at panel.whapi.cloud/dashboard
SYNC_ERROR	Sync failure	Log out the channel and reconnect it; GET requests will fail until resolved

For QR pairing: references/core-mcp-setup.md section "Where to Get Your API Token".

When to Apply

Reference these guidelines when:

Setting up the WHAPI MCP in Cursor, Claude Desktop, or any MCP-compatible client
Sending messages (text, media, interactive, polls)
Receiving incoming messages via webhooks
Managing groups, channels (newsletters), or communities
Building bots, broadcast systems, or CRM integrations
Troubleshooting unexpected API behavior
API Coverage and MCP Fallback

This skill covers the most-used operations and prevents the most common mistakes. It does NOT document every WHAPI endpoint.

If the operation you need is not described in any reference file:

Check available MCP tools — whapi-mcp exposes all API methods directly.
Apply core-chat-id.md rules for Chat ID format regardless of the endpoint.
Apply core-auth.md rules for authentication regardless of the endpoint.
Use ONLY parameter names from the MCP tool schema — do NOT invent parameters.
Validate against the WHAPI API Reference if unsure.

The MCP is the source of truth for available methods. The skill is the source of truth for correct usage patterns and anti-hallucination rules.

Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Core Concepts	CRITICAL	core-
2	Messaging	CRITICAL	msg-
3	Receiving	CRITICAL	recv-
4	Groups	HIGH	groups-
5	Channels	HIGH	channels-
6	Communities	MEDIUM	communities-
7	Patterns	HIGH	pattern-
How to Use

Read individual reference files for detailed explanations and code examples:

1. references/core-mcp-setup.md      ← install and configure the MCP first
2. references/core-chat-id.md        ← understand Chat ID formats (most common error)
3. references/core-auth.md           ← authenticate direct REST calls
4. references/msg-type-selection.md  ← choose the right send tool
5. references/recv-webhooks.md       ← set up receiving messages


Each reference file contains:

Why this matters (1-2 sentences)
Incorrect example with explanation
Correct example with explanation
Anti-hallucination checklist (parameters that do NOT exist)
WHAPI-specific notes
References
https://whapi.readme.io/reference — Full API Reference
https://support.whapi.cloud/help-desk — Documentation & FAQ
https://support.whapi.cloud/help-desk/faq/chat-id.-what-is-it-and-how-to-get-it
https://support.whapi.cloud/help-desk/integrations/mcp-model-context-protocol
Weekly Installs
28
Repository
whapi-cloud/wha…pi-skill
GitHub Stars
3
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn