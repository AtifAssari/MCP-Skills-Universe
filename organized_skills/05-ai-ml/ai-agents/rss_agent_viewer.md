---
rating: ⭐⭐⭐
title: rss-agent-viewer
url: https://skills.sh/brooksy4503/rss-agent-viewer/rss-agent-viewer
---

# rss-agent-viewer

skills/brooksy4503/rss-agent-viewer/rss-agent-viewer
rss-agent-viewer
Installation
$ npx skills add https://github.com/brooksy4503/rss-agent-viewer --skill rss-agent-viewer
Summary

Terminal-based RSS/Atom feed reader with discovery, search, and OPML import/export.

Discover feeds from any website, subscribe to feeds with optional timeout configuration, and read articles from single or multiple feeds with caching and parallel fetching
Search across all subscribed feeds locally or discover new feeds via web search (agent-built-in or Exa API) with auto-subscribe and read options
Clean up broken and duplicate feeds, import/export subscriptions via OPML, and manage feed database with configurable timeouts and result limits
Supports full-text search with author and date filtering, feed-diverse results (one latest per feed), and environment variable or config file setup
SKILL.md
RSS Agent Viewer

CLI RSS/Atom feed viewer with built-in discovery, caching, and search.

Quick start
npx -y rss-agent-viewer init
npx -y rss-agent-viewer discover https://vercel.com
npx -y rss-agent-viewer add https://vercel.com/atom
npx -y rss-agent-viewer read

Core workflow
# Initialize config + database
rss-viewer init

# Discover feeds for a site
rss-viewer discover https://example.com

# Subscribe to a feed (optional: --timeout for slow feeds)
rss-viewer add https://example.com/feed.xml
rss-viewer add https://slow-site.com/feed.xml --timeout 30000

# List feeds and read articles
rss-viewer feeds
rss-viewer read

Common commands
rss-viewer init
rss-viewer add <url>
rss-viewer discover <url>
rss-viewer feeds
rss-viewer remove <url>
rss-viewer read [url]
rss-viewer search <query>
rss-viewer discover-search <query>
rss-viewer import <file>
rss-viewer export
rss-viewer cache <action>
rss-viewer cleanup

Usage patterns
Discover and subscribe
rss-viewer discover https://example.com
rss-viewer add https://example.com/rss.xml

Read a single feed
rss-viewer read https://example.com/rss.xml

Read all feeds (fetches fresh by default)
# Fetches fresh articles from all feeds in parallel
rss-viewer read

# Use cached data only (skip network requests)
rss-viewer read --cached

# Limit results
rss-viewer read --limit 10

# One latest article per feed (feed-diverse results)
rss-viewer read --latest-per-feed --limit 10

# Timeouts (for slow feeds or many feeds)
rss-viewer read --timeout 15000 --overall-timeout 180000

Clean up invalid feeds
# Remove broken and duplicate feeds
rss-viewer cleanup

# Preview what would be removed
rss-viewer cleanup --dry-run

# Only remove broken feeds
rss-viewer cleanup --broken

# Only remove duplicates
rss-viewer cleanup --duplicates

Search across all feeds
# Local database search (enhanced with full-text search)
rss-viewer search "open source"

# Web search + discovery + add + search in one command
rss-viewer discover-search "Rust programming" --auto-add --read

# Using Exa API (BYOK)
rss-viewer discover-search "AI safety" \
  --provider exa \
  --max-results 5 \
  --auto-add \
  --read

Import OPML
rss-viewer import feeds.opml

Export feeds
rss-viewer export

Search Options
Local Database Search
rss-viewer search "React 19" --limit 10
rss-viewer search "TypeScript" --author "Dan" --since "2024-01-01"

Web Search with Discovery
# Use agent's built-in search (default)
rss-viewer discover-search "micro-frontends" --auto-add --read

# Use Exa API (requires EXA_API_KEY)
export EXA_API_KEY="your-api-key"
rss-viewer discover-search "WebGPU" \
  --provider exa \
  --max-results 5 \
  --category Development \
  --auto-add \
  --read \
  --limit 20

Configuration

Environment Variables:

EXA_API_KEY="your-api-key"                    # Exa API key (optional)
RSS_FEED_TIMEOUT=10000                        # Per-feed fetch timeout (ms)
RSS_VIEWER_SEARCH_PROVIDER="agent|exa"        # Search provider (default: agent)
RSS_VIEWER_MAX_WEB_RESULTS=10                 # Max web search results
RSS_VIEWER_SEARCH_LIMIT=20                    # Max article results
RSS_VIEWER_BOOST_RECENT=false                 # Boost recent articles in search
EXA_API_URL="https://api.exa.ai/search"       # Custom Exa endpoint (optional)


Config File (~/.config/rss-viewer/config.json):

{
  "webSearchProvider": "exa",
  "exaApiKey": "your-api-key",
  "feedTimeout": 10000,
  "overallTimeout": 120000,
  "maxWebResults": 10,
  "searchResultsLimit": 20,
  "boostRecentSearch": false
}

When to use this tool
Manage and read RSS/Atom feeds from the terminal
Discover feed URLs from a website
Search across multiple subscriptions with full-text search
Discover new feeds from web search queries
Automate feed discovery and subscription workflow
Import or export subscriptions via OPML
Clean up broken or duplicate feeds from database
More information
GitHub: https://github.com/brooksy4503/rss-agent-viewer
Weekly Installs
462
Repository
brooksy4503/rss…t-viewer
GitHub Stars
4
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn