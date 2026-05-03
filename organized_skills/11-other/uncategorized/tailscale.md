---
rating: ⭐⭐⭐
title: tailscale
url: https://skills.sh/jmagar/claude-homelab/tailscale
---

# tailscale

skills/jmagar/claude-homelab/tailscale
tailscale
Installation
$ npx skills add https://github.com/jmagar/claude-homelab --skill tailscale
SKILL.md
Tailscale Skill

⚠️ MANDATORY SKILL INVOCATION ⚠️

YOU MUST invoke this skill (NOT optional) when the user mentions ANY of these triggers:

"Tailscale status", "tailnet devices", "VPN status"
"Tailscale peers", "who's connected", "exit nodes"
"check Tailscale", "tailnet monitoring", "Tailscale"
Any mention of Tailscale or VPN network management

Failure to invoke this skill when triggers occur violates your operational requirements.

Purpose

Hybrid skill using both the Tailscale CLI (local machine operations) and the Tailscale API (tailnet-wide management). Read-Write (Safe) — no destructive operations; writes include creating auth keys and toggling network features.

Operation type	Method	Requires API key
Status, ping, netcheck, whois	CLI	No
Serve, funnel, file transfer, SSH	CLI	No
List all devices, user mgmt, DNS	API	Yes
Create/revoke auth keys	API	Yes
Setup

API config (optional, for tailnet-wide operations) is stored in ~/.claude-homelab/.env:

TAILSCALE_API_KEY="tskey-api-k..."
TAILSCALE_TAILNET="-"


Get your API key from: Tailscale Admin Console → Settings → Keys → Generate API Key

The TAILSCALE_TAILNET can be - (auto-detect), your org name, or email domain.

Local Operations (CLI)

These work on the current machine only.

Status & Diagnostics
# Current status (peers, connection state)
tailscale status
tailscale status --json | jq '.Peer | to_entries[] | {name: .value.HostName, ip: .value.TailscaleIPs[0], online: .value.Online}'

# Network diagnostics (NAT type, DERP, UDP)
tailscale netcheck
tailscale netcheck --format=json

# Get this machine's Tailscale IP
tailscale ip -4

# Identify a Tailscale IP
tailscale whois 100.x.x.x

Connectivity
# Ping a peer (shows direct vs relay)
tailscale ping <hostname-or-ip>

# Connect/disconnect
tailscale up
tailscale down

# Use an exit node
tailscale up --exit-node=<node-name>
tailscale exit-node list
tailscale exit-node suggest

File Transfer (Taildrop)
# Send files to a device
tailscale file cp myfile.txt <device-name>:

# Receive files (moves from inbox to directory)
tailscale file get ~/Downloads
tailscale file get --wait ~/Downloads  # blocks until file arrives

Expose Services
# Share locally within tailnet (private)
tailscale serve 3000
tailscale serve https://localhost:8080

# Share publicly to internet
tailscale funnel 8080

# Check what's being served
tailscale serve status
tailscale funnel status

SSH
# SSH via Tailscale (uses MagicDNS)
tailscale ssh user@hostname

# Enable SSH server on this machine
tailscale up --ssh

Tailnet-Wide Operations (API)

These manage your entire tailnet. Requires API key.

List All Devices
./scripts/ts-api.sh devices

# With details
./scripts/ts-api.sh devices --verbose

Device Details
./scripts/ts-api.sh device <device-id-or-name>

Check Online Status
# Quick online check for all devices
./scripts/ts-api.sh online

Authorize/Delete Device
./scripts/ts-api.sh authorize <device-id>
./scripts/ts-api.sh delete <device-id>

Device Tags & Routes
./scripts/ts-api.sh tags <device-id> tag:server,tag:prod
./scripts/ts-api.sh routes <device-id>

Auth Keys
# Create a reusable auth key
./scripts/ts-api.sh create-key --reusable --tags tag:server

# Create ephemeral key (device auto-removes when offline)
./scripts/ts-api.sh create-key --ephemeral

# List keys
./scripts/ts-api.sh keys

DNS Management
./scripts/ts-api.sh dns                 # Show DNS config
./scripts/ts-api.sh dns-nameservers     # List nameservers
./scripts/ts-api.sh magic-dns on|off    # Toggle MagicDNS

ACLs
./scripts/ts-api.sh acl                 # Get current ACL
./scripts/ts-api.sh acl-validate <file> # Validate ACL file

Common Use Cases

"Who's online right now?"

./scripts/ts-api.sh online


"Send this file to my phone"

tailscale file cp document.pdf my-phone:


"Expose my dev server publicly"

tailscale funnel 3000


"Create a key for a new server"

./scripts/ts-api.sh create-key --reusable --tags tag:server --expiry 7d


"Is the connection direct or relayed?"

tailscale ping my-server

🔧 Agent Tool Usage Requirements

CRITICAL: When invoking scripts from this skill via the zsh-tool, ALWAYS use pty: true.

Without PTY mode, command output will not be visible even though commands execute successfully.

Correct invocation pattern:

<invoke name="mcp__plugin_zsh-tool_zsh-tool__zsh">
<parameter name="command">./skills/SKILL_NAME/scripts/SCRIPT.sh [args]</parameter>
<parameter name="pty">true</parameter>
</invoke>

Weekly Installs
19
Repository
jmagar/claude-homelab
GitHub Stars
37
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn