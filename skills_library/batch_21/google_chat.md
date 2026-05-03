---
title: google-chat
url: https://skills.sh/sanjay3290/ai-skills/google-chat
---

# google-chat

skills/sanjay3290/ai-skills/google-chat
google-chat
Installation
$ npx skills add https://github.com/sanjay3290/ai-skills --skill google-chat
SKILL.md
Google Chat

Lightweight Google Chat integration with standalone OAuth authentication. No MCP server required.

⚠️ Requires Google Workspace account. Personal Gmail accounts are not supported.

First-Time Setup

Authenticate with Google (opens browser):

python scripts/auth.py login


Check authentication status:

python scripts/auth.py status


Logout when needed:

python scripts/auth.py logout

Commands

All operations via scripts/chat.py. Auto-authenticates on first use if not logged in.

# List all spaces you're a member of
python scripts/chat.py list-spaces

# Find a space by name
python scripts/chat.py find-space "Project Alpha"

# Get messages from a space
python scripts/chat.py get-messages spaces/AAAA123 --limit 10

# Send a message to a space
python scripts/chat.py send-message spaces/AAAA123 "Hello team!"

# Send a message with file attachment
python scripts/chat.py send-message spaces/AAAA123 "Here's the report" --attachment /path/to/file.pdf

# Send a direct message
python scripts/chat.py send-dm user@example.com "Hey, quick question..."

# Send a DM with file attachment
python scripts/chat.py send-dm user@example.com "Please review" --attachment /path/to/file.pdf

# Find or create DM space with someone
python scripts/chat.py find-dm user@example.com

# List threads in a space
python scripts/chat.py list-threads spaces/AAAA123

# Create a new space with members
python scripts/chat.py setup-space "New Project" user1@example.com user2@example.com

Space Name Format

Google Chat uses spaces/AAAA123 format. Get space names from list-spaces or find-space.

Token Management

Tokens stored securely using the system keyring:

macOS: Keychain
Windows: Windows Credential Locker
Linux: Secret Service API (GNOME Keyring, KDE Wallet, etc.)

Service name: google-chat-skill-oauth

Automatically refreshes expired tokens using Google's cloud function.

Weekly Installs
136
Repository
sanjay3290/ai-skills
GitHub Stars
246
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail