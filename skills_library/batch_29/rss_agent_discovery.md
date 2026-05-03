---
title: rss-agent-discovery
url: https://skills.sh/brooksy4503/rss-agent-discovery/rss-agent-discovery
---

# rss-agent-discovery

skills/brooksy4503/rss-agent-discovery/rss-agent-discovery
rss-agent-discovery
Installation
$ npx skills add https://github.com/brooksy4503/rss-agent-discovery --skill rss-agent-discovery
SKILL.md
RSS Agent Discovery

AI agent-focused RSS feed discovery tool with machine-parseable JSON output.

Quick start
npx -y rss-agent-discovery https://vercel.com


Output:

{
  "success": true,
  "results": [{
    "url": "https://vercel.com/",
    "feeds": [{
      "url": "https://vercel.com/atom",
      "title": "atom",
      "type": "atom"
    }],
    "error": null,
    "diagnostics": []
  }]
}

Core workflow
npx -y rss-agent-discovery <url> [url2] [url3]...


Parse JSON output:

npx -y rss-agent-discovery https://example.com | jq '.results[0].feeds'

Output schema
{
  success: boolean,           // true if no URLs had errors
  partialResults?: boolean,   // true if success=false but some feeds found
  results: [{
    url: string,              // scanned URL
    feeds: [{
      url: string,            // feed URL
      title: string,          // feed title from HTML
      type: 'rss' | 'atom' | 'unknown'
    }],
    error: string | null,     // error message if scan failed (timeout errors normalized to "Timeout")
    diagnostics?: string[]    // optional array of warning messages for non-fatal issues
  }]
}

Output contract

Default behavior (without --verbose):

JSON-only output to stdout (machine-parseable)
No stderr output (clean for programmatic consumption)
All errors and warnings included in JSON structure

Verbose mode (--verbose):

JSON output to stdout (unchanged)
Debug logging to stderr (useful for troubleshooting)
Additional context about skipped URLs, validation failures, etc.

Recommended integration pattern:

Parse stdout as JSON (always valid JSON, even on errors)
Check success field for overall status
Check partialResults if success === false to see if any feeds were found
Check error field in each result for URL-specific failures
Check diagnostics array for warnings and non-fatal issues
Use --verbose flag only when troubleshooting or debugging
Exit codes
0 - One or more feeds found (or --help / --version used)
1 - No feeds found
2 - Error occurred

Use exit code for automation:

npx -y rss-agent-discovery https://example.com
if [ $? -eq 0 ]; then
  echo "Feeds found!"
fi

Options
--timeout <ms>          # Timeout per URL (default: 10000)
--skip-blogs           # Skip blog subdirectory scanning
--max-blogs <n>        # Limit blog scans (default: 3)
--blog-paths <paths>   # Custom blog paths (comma or pipe separated)
--verbose              # Enable debug logging to stderr (default: JSON-only output)
--help                 # Show help
--version              # Show version


Examples:

npx -y rss-agent-discovery --timeout 15000 https://example.com
npx -y rss-agent-discovery --skip-blogs https://example.com
npx -y rss-agent-discovery --blog-paths '/blog,/news,/articles' https://example.com
npx -y rss-agent-discovery --blog-paths '/blog|/updates' https://example.com
npx -y rss-agent-discovery --max-blogs 5 https://example.com

Features
Discovers feeds from HTML <link> tags
Tests common paths (/rss.xml, /atom, /feed, etc.)
Scans blog subdirectories (/blog, /news, /articles)
Parallel processing for multiple URLs
Deduplicates feeds across all sources
Validates feeds actually return XML
JSON-only output to stdout (clean by default, no stderr)
Errors and warnings included in JSON structure
Timeout errors normalized to consistent "Timeout" message
Common patterns
Single URL discovery
npx -y rss-agent-discovery https://example.com | jq '.results[0].feeds[].url'

Multiple URLs (parallel)
npx -y rss-agent-discovery https://site1.com https://site2.com https://site3.com

Extract all feed URLs
npx -y rss-agent-discovery https://example.com | jq -r '.results[0].feeds[].url'

Check if feeds exist without parsing
npx -y rss-agent-discovery https://example.com
exit_code=$?
[ $exit_code -eq 0 ] && echo "Feeds found"

Custom timeout for slow sites
npx -y rss-agent-discovery --timeout 20000 https://slow-site.com

Skip blog scanning for faster results
npx -y rss-agent-discovery --skip-blogs https://example.com

Integration examples
Shell script
#!/bin/bash
# No need to redirect stderr - it's clean by default
result=$(npx -y rss-agent-discovery "$1")
if [ $? -eq 0 ]; then
  echo "Found feeds:"
  echo "$result" | jq '.results[0].feeds'
fi

Python
import subprocess
import json

result = subprocess.run(
  ['npx', '-y', 'rss-agent-discovery', url],
  capture_output=True,
  text=True
)

if result.returncode == 0:
  data = json.loads(result.stdout)
  feeds = data['results'][0]['feeds']

JavaScript/Node.js
const { execSync } = require('child_process');
const result = JSON.parse(
  execSync('npx -y rss-agent-discovery https://example.com').toString()
);
const feeds = result.results[0].feeds;

Why use this tool

Existing RSS discovery tools (rss-url-finder, rss-finder) are designed for humans:

Output human-readable text
Don't validate feeds exist
Lack structured machine output

This tool is designed for AI agents:

JSON-only output to stdout (machine-parseable)
Clean output by default (no stderr unless --verbose is enabled)
All errors and warnings included in JSON structure
Semantic exit codes
Validates feeds return XML
Timeout errors normalized to consistent format
Discovers feeds AI agents miss
Testing

Test the tool works:

npx -y rss-agent-discovery https://vercel.com
npx -y rss-agent-discovery https://news.ycombinator.com

More information
NPM: https://www.npmjs.com/package/rss-agent-discovery
GitHub: https://github.com/brooksy4503/rss-agent-discovery
Weekly Installs
118
Repository
brooksy4503/rss…iscovery
GitHub Stars
2
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn