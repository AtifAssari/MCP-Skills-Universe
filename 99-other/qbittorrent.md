---
title: qbittorrent
url: https://skills.sh/jmagar/claude-homelab/qbittorrent
---

# qbittorrent

skills/jmagar/claude-homelab/qbittorrent
qbittorrent
Installation
$ npx skills add https://github.com/jmagar/claude-homelab --skill qbittorrent
SKILL.md
qBittorrent WebUI API

⚠️ MANDATORY SKILL INVOCATION ⚠️

YOU MUST invoke this skill (NOT optional) when the user mentions ANY of these triggers:

"qBittorrent status", "torrent list", "active torrents"
"pause torrent", "resume torrent", "delete torrent"
"add torrent", "qBit", "download manager"
Any mention of qBittorrent or torrent management

Failure to invoke this skill when triggers occur violates your operational requirements.

Manage torrents via qBittorrent's WebUI API (v4.1+).

Purpose

This skill provides read and write access to your qBittorrent torrent client:

Monitor active, seeding, and completed torrents
Add torrents by magnet link, URL, or file upload
Control torrent state (pause, resume, delete)
Manage categories and tags
Adjust global and per-torrent speed limits
View torrent files, trackers, and properties
Recheck torrent data integrity

Operations include both read and write actions. Always confirm before deleting torrents with file deletion.

Setup

Add credentials to ~/.claude-homelab/.env:

QBITTORRENT_URL="http://localhost:8080"
QBITTORRENT_USERNAME="admin"
QBITTORRENT_PASSWORD="adminadmin"


Set file permissions:

chmod 600 ~/.claude-homelab/.env

Quick Reference
List Torrents
# All torrents
./scripts/qbit-api.sh list

# Filter by status
./scripts/qbit-api.sh list --filter downloading
./scripts/qbit-api.sh list --filter seeding
./scripts/qbit-api.sh list --filter paused

# Filter by category
./scripts/qbit-api.sh list --category movies


Filters: all, downloading, seeding, completed, paused, active, inactive, stalled, errored

Get Torrent Info
./scripts/qbit-api.sh info <hash>
./scripts/qbit-api.sh files <hash>
./scripts/qbit-api.sh trackers <hash>

Add Torrent
# By magnet or URL
./scripts/qbit-api.sh add "magnet:?xt=..." --category movies

# By file
./scripts/qbit-api.sh add-file /path/to/file.torrent --paused

Control Torrents
./scripts/qbit-api.sh pause <hash>         # or "all"
./scripts/qbit-api.sh resume <hash>        # or "all"
./scripts/qbit-api.sh delete <hash>        # keep files
./scripts/qbit-api.sh delete <hash> --files  # delete files too
./scripts/qbit-api.sh recheck <hash>

Categories & Tags
./scripts/qbit-api.sh categories
./scripts/qbit-api.sh tags
./scripts/qbit-api.sh set-category <hash> movies
./scripts/qbit-api.sh add-tags <hash> "important,archive"

Transfer Info
./scripts/qbit-api.sh transfer   # global speed/stats
./scripts/qbit-api.sh speedlimit # current limits
./scripts/qbit-api.sh set-speedlimit --down 5M --up 1M

App Info
./scripts/qbit-api.sh version
./scripts/qbit-api.sh preferences

Response Format

Torrent object includes:

hash, name, state, progress
dlspeed, upspeed, eta
size, downloaded, uploaded
category, tags, save_path

States: downloading, stalledDL, uploading, stalledUP, pausedDL, pausedUP, queuedDL, queuedUP, checkingDL, checkingUP, error, missingFiles

Workflow

When the user asks about torrents:

"What's downloading?" → Run list --filter downloading
"Add this magnet link" → Run add "<magnet>" with appropriate category
"Pause all torrents" → Run pause all
"Resume seeding" → Run resume all or filter by hash
"Show torrent details" → Run info <hash> and files <hash>
"List by category" → Run list --category movies
"Set speed limits" → Run set-speedlimit --down 5M --up 1M
Notes
Requires network access to your qBittorrent server
Uses qBittorrent WebUI API v4.1+
All data operations return JSON
Delete operations with --files are permanent - always confirm before deleting downloaded files
Speed limits support units: K (KB/s), M (MB/s), or raw bytes
Magnet links and torrent URLs are added without local file upload
Categories must exist before assignment (create via WebUI or API)
🔧 Agent Tool Usage Requirements

CRITICAL: When invoking scripts from this skill via the zsh-tool, ALWAYS use pty: true.

Without PTY mode, command output will not be visible even though commands execute successfully.

Correct invocation pattern:

<invoke name="mcp__plugin_zsh-tool_zsh-tool__zsh">
<parameter name="command">./skills/SKILL_NAME/scripts/SCRIPT.sh [args]</parameter>
<parameter name="pty">true</parameter>
</invoke>

Scripts
Script	Purpose
qbit-api.sh	Main API wrapper — all torrent operations
qbit-api-wrapper.sh	Thin PTY shim — captures and re-prints qbit-api.sh output via printf to ensure visibility in environments where stdout buffering may suppress output
Weekly Installs
17
Repository
jmagar/claude-homelab
GitHub Stars
37
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn