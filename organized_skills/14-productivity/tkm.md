---
rating: ⭐⭐⭐
title: tkm
url: https://skills.sh/jorgemuza/orbit/tkm
---

# tkm

skills/jorgemuza/orbit/tkm
tkm
Installation
$ npx skills add https://github.com/jorgemuza/orbit --skill tkm
SKILL.md
Token Manager (tkm) with orbit CLI

Track AI token consumption, costs, and usage trends across Claude Code sessions. Data is ingested automatically from Claude Code session JSONL files and stored in a local SQLite database.

Prerequisites
orbit CLI installed — if which orbit fails, install with:
macOS/Linux (Homebrew): brew install jorgemuza/tap/orbit
macOS/Linux (script): curl -sSfL https://raw.githubusercontent.com/jorgemuza/orbit/main/install.sh | sh
Windows (Scoop): scoop bucket add jorgemuza https://github.com/jorgemuza/scoop-bucket && scoop install orbit
Claude Code installed and used (session files in ~/.claude/projects/)

No profile or service configuration needed — tkm works entirely with local data.

Quick Reference
# Today's token usage and cost
orbit tkm status

# This week's summary
orbit tkm status --period week

# Daily usage breakdown
orbit tkm usage

# Weekly usage
orbit tkm usage --period weekly

# Monthly usage
orbit tkm usage --period monthly

# Cost breakdown by model
orbit tkm cost

# This calendar month so far (matches latest row of 'tkm usage --period monthly')
orbit tkm cost --period month

# Trailing 30 days (straddles month boundaries)
orbit tkm cost --period month-rolling

# Recent sessions with token counts
orbit tkm sessions

# More sessions
orbit tkm sessions --limit 50

# Filter by project
orbit tkm status --project /path/to/project
orbit tkm usage --project /path/to/project

# Filter by model
orbit tkm usage --model opus

# Force sync session data
orbit tkm sync

# Full re-sync (re-process all files)
orbit tkm sync --full

# JSON output for scripting
orbit tkm status -o json
orbit tkm cost -o json

# Manually record a usage event
orbit tkm track --model claude-opus-4-6 --input 1000 --output 500

# Clear all tracking data
orbit tkm clear --confirm

Core Workflows
Check daily spending
orbit tkm status
orbit tkm cost --period today

Weekly cost review
orbit tkm usage --period weekly --limit 8
orbit tkm cost --period week

Per-project analysis
# Check spending on a specific project
orbit tkm status --period month --project /Users/me/Projects/my-app
orbit tkm sessions --project /Users/me/Projects/my-app

Model cost comparison
orbit tkm cost --period month

Export data for reporting
orbit tkm usage --period monthly -o json > monthly-usage.json
orbit tkm cost -o json > cost-breakdown.json
orbit tkm sessions -o json > sessions.json

Period Semantics

--period accepts: today, yesterday, week (last 7 days), month (calendar month-to-date, e.g. 2026-04-01 → now), month-rolling (trailing 30 days, straddles month boundaries), and all. Use month when you want "this month's spend so far" and want it to agree with tkm usage --period monthly's latest row; use month-rolling when you want a rolling 30-day window.

Data Storage
Database: ~/.config/orbit/tkm.db (SQLite)
Source: ~/.claude/projects/<encoded-path>/<session-id>.jsonl
Auto-sync: Runs automatically on every read command (status, usage, cost, sessions)
Incremental: Only parses new data since last sync (byte-offset tracking)
Retention: Skips files older than 90 days
Pushing Data to Draxarp

Token usage data can be pushed to Draxarp Tracking for centralized analytics:

# Push unpushed events to Draxarp
orbit -p paybook tracking tkm push

# Preview without pushing
orbit -p paybook tracking tkm push --dry-run

# Push with larger batch
orbit -p paybook tracking tkm push --batch-size 500


Uses incremental sync — only pushes events not yet sent. Safe to re-run (Draxarp deduplicates by event hash).

RTK Integration (Optional)

RTK is a companion tool that compresses command output before it reaches the LLM, saving 60-90% of input tokens. orbit tkm handles the analytics side.

Tool	Role
RTK	Compresses command output (git, grep, npm, etc.)
orbit tkm	Tracks usage, calculates costs, reports trends

RTK is optional — tkm works standalone. To add RTK compression:

# Install RTK
brew install rtk-ai/tap/rtk

# Set up Claude Code hooks
rtk init -g

# Verify compression is working
rtk verify

Model Pricing

Default pricing (per million tokens):

Model	Input	Output	Cache Read	Cache Write
claude-opus-4-6	$15.00	$75.00	$1.50	$18.75
claude-sonnet-4-6	$3.00	$15.00	$0.30	$3.75
claude-haiku-4-5	$0.80	$4.00	$0.08	$1.00

For full command details and flags, see references/commands.md.

Weekly Installs
51
Repository
jorgemuza/orbit
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass