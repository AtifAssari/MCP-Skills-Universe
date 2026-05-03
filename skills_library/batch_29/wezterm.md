---
title: wezterm
url: https://skills.sh/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/wezterm
---

# wezterm

skills/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/wezterm
wezterm
Installation
$ npx skills add https://github.com/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill wezterm
SKILL.md
WezTerm Skill

Use the wezterm CLI to control and interact with WezTerm terminal instances.

CLI Location
/Applications/WezTerm.app/Contents/MacOS/wezterm


Or add to PATH for easier access.

Listing and Connecting

List all WezTerm panes:

wezterm cli list


List in JSON format:

wezterm cli list --format json


List clients (GUI windows):

wezterm cli list-clients

Pane Management

Get current pane ID:

wezterm cli get-pane-direction


Split pane horizontally (new pane to right):

wezterm cli split-pane --right


Split pane vertically (new pane below):

wezterm cli split-pane --bottom


Split with specific command:

wezterm cli split-pane --right -- htop


Move focus between panes:

wezterm cli activate-pane-direction up
wezterm cli activate-pane-direction down
wezterm cli activate-pane-direction left
wezterm cli activate-pane-direction right


Activate specific pane by ID:

wezterm cli activate-pane --pane-id <pane-id>

Tab Management

Create new tab:

wezterm cli spawn


Create tab with command:

wezterm cli spawn -- vim


Create tab in specific domain:

wezterm cli spawn --domain-name SSH:server


Activate tab by index:

wezterm cli activate-tab --tab-index 0


Activate tab relative:

wezterm cli activate-tab --tab-relative 1   # next tab
wezterm cli activate-tab --tab-relative -1  # previous tab

Sending Commands to Panes

Send text to a pane:

wezterm cli send-text --pane-id <pane-id> "ls -la\n"


Send text to current pane:

wezterm cli send-text "echo hello\n"

Workspaces

List workspaces:

wezterm cli list --format json | jq '.[].workspace' | sort -u

Zoom

Toggle pane zoom:

wezterm cli zoom-pane --toggle


Zoom pane:

wezterm cli zoom-pane --zoom


Unzoom:

wezterm cli zoom-pane --unzoom

Multiplexer Domains

List domains (local, SSH, etc.):

wezterm cli list --format json | jq '.[].domain_name' | sort -u


Connect to SSH domain:

wezterm cli spawn --domain-name SSH:myserver

Configuration

Config file:

~/.config/wezterm/wezterm.lua


Show effective config:

wezterm show-keys

Launching

Start new window:

wezterm start


Start with command:

wezterm start -- htop


Start in directory:

wezterm start --cwd /path/to/dir


Connect to running mux server:

wezterm connect unix

Weekly Installs
46
Repository
dicklesworthsto…grations
GitHub Stars
63
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass