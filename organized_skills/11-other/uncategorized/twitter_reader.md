---
rating: ⭐⭐
title: twitter-reader
url: https://skills.sh/nicepkg/ai-workflow/twitter-reader
---

# twitter-reader

skills/nicepkg/ai-workflow/twitter-reader
twitter-reader
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill twitter-reader
SKILL.md
Twitter Reader

Fetch Twitter/X post content without needing JavaScript or authentication.

Prerequisites

You need a Jina API key to use this skill:

Visit https://jina.ai/ to sign up (free tier available)
Get your API key from the dashboard
Set the environment variable:
export JINA_API_KEY="your_api_key_here"

Quick Start

For a single tweet, use curl directly:

curl "https://r.jina.ai/https://x.com/USER/status/TWEET_ID" \
  -H "Authorization: Bearer ${JINA_API_KEY}"


For multiple tweets, use the bundled script:

scripts/fetch_tweets.sh url1 url2 url3

What Gets Returned
Title: Post author and content preview
URL Source: Original tweet link
Published Time: GMT timestamp
Markdown Content: Full post text with media descriptions
Bundled Scripts
fetch_tweet.py

Python script for fetching individual tweets.

python scripts/fetch_tweet.py https://x.com/user/status/123 output.md

fetch_tweets.sh

Bash script for batch fetching multiple tweets.

scripts/fetch_tweets.sh \
  "https://x.com/user/status/123" \
  "https://x.com/user/status/456"

URL Formats Supported
https://x.com/USER/status/ID
https://twitter.com/USER/status/ID
https://x.com/... (redirects work automatically)
Environment Variables
JINA_API_KEY: Required. Your Jina.ai API key for accessing the reader API
Weekly Installs
45
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn