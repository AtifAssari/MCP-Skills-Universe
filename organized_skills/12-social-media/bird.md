---
rating: ⭐⭐⭐
title: bird
url: https://skills.sh/liewcf/agent-skills/bird
---

# bird

skills/liewcf/agent-skills/bird
bird
Installation
$ npx skills add https://github.com/liewcf/agent-skills --skill bird
SKILL.md
Bird - X/Twitter CLI

Guide for using the bird CLI tool to interact with X/Twitter content.

Quick Start

Install bird globally:

npm install -g @steipete/bird
# or
pnpm add -g @steipete/bird
# or
bun add -g @steipete/bird
# one-shot (no install)
bunx @steipete/bird whoami
# or
brew install steipete/tap/bird


Verify authentication:

bird whoami          # Show logged-in account
bird check           # Check available credentials

Common Tasks
Read Tweets and Threads
# Read a single tweet
bird read <tweet-url-or-id>
bird <tweet-url-or-id>              # shorthand

# Read a thread (tweet + replies)
bird thread <tweet-url-or-id>

# Get replies only
bird replies <tweet-url-or-id>

# Output as JSON for processing
bird read <id> --json
bird thread <id> --json --max-pages 3

Search Tweets
# Basic search
bird search "query" -n 10

# Search from a specific user
bird search "from:username" -n 20

# Get all results (paginated)
bird search "query" --all --json

# Search with date filters
bird search "query since:2024-01-01" -n 50

Get User Content
# User's tweets
bird user-tweets @username -n 20
bird user-tweets @username -n 50 --json

# User mentions
bird mentions --user @username -n 10

Manage Bookmarks
# List bookmarks
bird bookmarks -n 20
bird bookmarks --all --json

# From a specific folder
bird bookmarks --folder-id <id> -n 10

# Remove a bookmark
bird unbookmark <tweet-id-or-url>

Get News and Trending
# AI-curated news
bird news --ai-only -n 10

# Sports/Entertainment news
bird news --sports -n 15
bird news --entertainment -n 10

# Include related tweets
bird news --with-tweets --tweets-per-item 3 -n 10

# Trending topics
bird trending -n 10

Post Tweets (use with caution)
# Send a tweet
bird tweet "hello world"

# Reply to a tweet
bird reply <tweet-id-or-url> "my reply"

Process JSON Output

Use jq to extract specific fields from JSON output:

# Get tweet text only
bird read <id> --json | jq -r '.text'

# Get user info
bird user-tweets @user -n 5 --json | jq '.[] | {name: .user.name, handle: .user.screen_name}'

# Extract media URLs
bird read <id> --json | jq -r '.media[]?.url'

# Save to file
bird user-tweets @user --all --json > tweets.json

Authentication

Bird uses cookie-based authentication (no API keys required). Use --auth-token / --ct0 to pass cookies directly, or --cookie-source for browser cookies.

Browser cookie sources:

Safari, Chrome, or Firefox (macOS)
Chromium variants (Arc/Brave/etc): use --chrome-profile-dir
Choose the cookie order with --cookie-source, and specific Firefox profile with --firefox-profile
--cookie-source is repeatable: safari|chrome|firefox|all|none
Config File

Global: ~/.config/bird/config.json5
Project: ./.birdrc.json5

Example:

{
  cookieSource: ["chrome"],
  chromeProfileDir: "/path/to/Arc/Profile",
  chromeProfile: "Default",
  firefoxProfile: "default-release",
  cookieTimeoutMs: 10000,
  timeoutMs: 20000,
  quoteDepth: 1
}


Environment variables:

BIRD_TIMEOUT_MS
BIRD_COOKIE_TIMEOUT_MS
BIRD_QUOTE_DEPTH
BIRD_QUERY_IDS_CACHE
Important Notes
Uses undocumented X/Twitter GraphQL API - may break without notice
Recommendation: Use for reading only. Tweeting may trigger blocks.
Rate limits apply - use --delay <ms> to add delays between requests
Pagination (when supported): search, bookmarks, likes, following, and followers require --all or --cursor with --max-pages; list-timeline treats --max-pages as --all
Troubleshooting

Query IDs stale (404 errors):

bird query-ids --fresh


Query IDs cache:

Default: ~/.config/bird/query-ids-cache.json
Override: BIRD_QUERY_IDS_CACHE=/path/to/file.json

Cookie extraction fails:

Confirm you're logged into X/Twitter in the browser
Try a different --cookie-source order
For Arc/Brave, pass --chrome-profile-dir

Auth fails with flags/env:

Ensure --auth-token and --ct0 are from the same session
Try browser cookies instead of flags for a quick sanity check
Reference

See references/commands.md for complete command documentation.

Weekly Installs
43
Repository
liewcf/agent-skills
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail