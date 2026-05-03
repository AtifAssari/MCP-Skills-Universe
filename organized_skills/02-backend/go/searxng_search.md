---
rating: ⭐⭐⭐
title: searxng-search
url: https://skills.sh/ypares/agent-skills/searxng-search
---

# searxng-search

skills/ypares/agent-skills/searxng-search
searxng-search
Installation
$ npx skills add https://github.com/ypares/agent-skills --skill searxng-search
Summary

Local metasearch engine aggregating results from multiple sources with JSON output and package repository support.

Supports 20+ search categories including general web, Cargo/crates.io, npm, GitHub repositories, IT resources, academic papers, news, images, and videos
Returns structured JSON with result metadata (title, URL, content, engines, score, publish date) plus answer boxes, suggestions, and infoboxes
Auto-detects podman or docker, starts SearXNG on localhost:8888 with minimal configuration, and provides curl-based query interface
Includes workarounds for PyPI searches via direct API or qypi CLI, and Nushell helper function for streamlined queries
SKILL.md
SearXNG Search

SearXNG is a privacy-respecting metasearch engine that you can run locally. It aggregates results from multiple search engines and package repositories, returning clean JSON output.

Quick Start

Start SearXNG:

start-searxng --detach


This will:

Auto-detect podman or docker
Create a minimal config with JSON output enabled
Start SearXNG on http://localhost:8888
Wait until ready

Stop SearXNG:

podman stop searxng  # or: docker stop searxng


Custom port:

start-searxng --port 9999 --detach

Quick Reference
Task	Command	Category
General web search	curl "http://localhost:8888/search?q=<query>&format=json"	general
Search Cargo/crates.io	curl "http://localhost:8888/search?q=<crate>&format=json&categories=cargo"	cargo
Search npm packages	curl "http://localhost:8888/search?q=<pkg>&format=json&categories=packages"	packages
Search code repositories	curl "http://localhost:8888/search?q=<query>&format=json&categories=repos"	repos
Search IT resources	curl "http://localhost:8888/search?q=<query>&format=json&categories=it"	it
Limit results	Add &limit=N to URL	-
Multiple categories	&categories=cat1,cat2	-
Available Categories

Run to see all categories:

curl -s "http://localhost:8888/config" | jq '.categories'


Notable categories:

general: General web search (default)
cargo: Rust crates from crates.io
packages: Multi-repo (npm, rubygems, haskell/hoogle, hex, packagist, metacpan, pub.dev, pkg.go.dev, docker hub, alpine, etc.)
it: IT/tech resources (includes GitHub, Docker Hub, crates.io)
repos: Code repositories
code: Code search
scientific publications: Academic papers
news, videos, images, books, etc.

See package-engine-status.md for comprehensive package search testing results.

JSON Response Structure
{
  "query": "search term",
  "number_of_results": 0,
  "results": [
    {
      "url": "https://example.com",
      "title": "Result Title",
      "content": "Snippet of content...",
      "publishedDate": "2025-01-01T00:00:00",
      "engine": "duckduckgo",
      "engines": ["duckduckgo", "startpage"],
      "score": 3.0,
      "category": "general"
    }
  ],
  "answers": [],          // Direct answers/infoboxes
  "suggestions": [],      // Search suggestions
  "corrections": [],      // Query corrections
  "infoboxes": [],       // Knowledge panels
  "unresponsive_engines": []
}

Common Usage Patterns
1. Package Repository Searches

Cargo/Rust crates:

curl -s "http://localhost:8888/search?q=tokio&format=json&categories=cargo" | \
  jq '.results[] | {title, url, content}'


npm packages:

curl -s "http://localhost:8888/search?q=express&format=json&categories=packages" | \
  jq '.results[] | select(.engines[] == "npm") | {title, url, content}'


PyPI packages (workaround - see below):

# PyPI engine is enabled but not returning results in current SearXNG config
# Use direct API or qypi CLI instead (see PyPI Workaround section)

2. Web Search with Filtering

IT/Tech search:

curl -s "http://localhost:8888/search?q=rust+async&format=json&categories=it" | \
  jq '.results[0:5] | .[] | {title, url, engines}'


GitHub repositories:

curl -s "http://localhost:8888/search?q=machine+learning&format=json&categories=repos" | \
  jq '.results[] | select(.engines[] == "github") | {title, url}'

3. Extracting Specific Information

Get top 3 results:

curl -s "http://localhost:8888/search?q=rust+ownership&format=json" | \
  jq '.results[0:3] | .[] | {title, url, content}'


Check which engines returned results:

curl -s "http://localhost:8888/search?q=python&format=json" | \
  jq '.results[0].engines'


Get answer boxes/infoboxes:

curl -s "http://localhost:8888/search?q=rust+language&format=json" | \
  jq '.infoboxes, .answers'

PyPI Workaround

Since PyPI is not returning results in SearXNG (despite being enabled), use these alternatives:

Option 1: Direct PyPI JSON API
# Search (limited to simple package name matching)
curl -s "https://pypi.org/pypi/<package>/json" | jq '.info | {name, summary, version, home_page}'

# Example:
curl -s "https://pypi.org/pypi/requests/json" | jq '.info.summary'

Option 2: qypi CLI tool
# Install
uvx qypi search pandas --json

# Get package info
uvx qypi info requests --json

# List releases
uvx qypi releases flask --json


See references/pypi-direct-search.md for more details.

Integration with Nushell

Create a helper function:

def searx [
  query: string,
  --category (-c): string = "general",
  --limit (-l): int = 10
] {
  http get $"http://localhost:8888/search?q=($query | url encode)&format=json&categories=($category)"
  | get results
  | first $limit
  | select title url content engines
}


Usage:

searx "tokio async" --category cargo --limit 5
searx "flask tutorial" --category general

Debugging

Check SearXNG config:

curl -s "http://localhost:8888/config" | jq '.engines[] | select(.name == "pypi")'


Check for engine errors:

curl -s "http://localhost:8888/search?q=test&format=json" | jq '.unresponsive_engines'


Test specific engine:

curl -s "http://localhost:8888/search?q=flask&format=json&engines=pypi" | jq .

Known Issues
PyPI engine enabled but not working: Use direct API or qypi CLI as workaround
Cargo category sometimes returns empty: Try categories=packages or categories=it which also include crates.io
Rate limiting: SearXNG may rate-limit if too many requests in quick succession
Configuration
Using the Helper Script (Recommended)

The start-searxng script creates a minimal configuration automatically:

start-searxng --help


Default config includes:

use_default_settings: true (inherits all SearXNG defaults)
JSON format enabled
Rate limiting disabled (for local use)
Secret key (change in production!)
Using Your Own Config
start-searxng --config /path/to/your/config/dir


Your config directory should contain settings.yml.

Manual Container Start
# Create config
mkdir -p /tmp/searxng-config
cat > /tmp/searxng-config/settings.yml << 'EOF'
use_default_settings: true
search:
  formats:
    - html
    - json
server:
  secret_key: "change-me-in-production"
  bind_address: "0.0.0.0"
  port: 8080
EOF

# Start with podman
podman run --rm -d --name searxng \
  -p 8888:8080 \
  -v /tmp/searxng-config:/etc/searxng:Z \
  docker.io/searxng/searxng:latest

# Or with docker
docker run --rm -d --name searxng \
  -p 8888:8080 \
  -v /tmp/searxng-config:/etc/searxng \
  docker.io/searxng/searxng:latest

Check Logs
podman logs searxng  # or: docker logs searxng

Advanced Config

See SearXNG Settings Documentation for all options.

Minimal config to add JSON output to defaults:

use_default_settings: true
search:
  formats:
    - html
    - json

Weekly Installs
522
Repository
ypares/agent-skills
GitHub Stars
24
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn