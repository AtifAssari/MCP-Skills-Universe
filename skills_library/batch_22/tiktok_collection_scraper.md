---
title: tiktok-collection-scraper
url: https://skills.sh/yulin7645/tiktok-skills/tiktok-collection-scraper
---

# tiktok-collection-scraper

skills/yulin7645/tiktok-skills/tiktok-collection-scraper
tiktok-collection-scraper
Installation
$ npx skills add https://github.com/yulin7645/tiktok-skills --skill tiktok-collection-scraper
SKILL.md
TikTok Collection Scraper

Batch extract TikTok user collection folders and their video links — including play counts, likes, comments, and shares. Zero external API, no paid service, just curl_cffi.

Features
🔓 No login required — works without cookies for public collections (~80% coverage)
🔑 Full access with cookie — get all collections including private ones (100%)
🚀 Zero external API — only needs curl_cffi, no TikHub/RapidAPI/paid services
📥 7 input formats — username, @username, profile URL, video URL, short link, user_id, secUid
📊 Rich metadata — plays, likes, comments, shares per video
⚡ Fast — 50 collections + 300 videos in ~40 seconds
Prerequisites

Ensure curl_cffi is installed:

pip install curl_cffi

Quick Start

Run the bundled script. All paths below are relative to this skill's directory.

# Guest mode (public collections, no cookie needed)
python3 scripts/scrape_collections.py <target> -o /tmp/result.json

# Login mode (all collections, 100% coverage)
python3 scripts/scrape_collections.py <target> --cookie /path/to/cookie.txt -o /tmp/result.json

Supported Input Formats
Format	Example
Username	chengfeng_yulin
@Username	@chengfeng_yulin
Profile URL	https://www.tiktok.com/@chengfeng_yulin
Video URL	https://www.tiktok.com/@user/video/7602514407133941000
Short link	https://vm.tiktok.com/ZMkVKQxsb/
User ID	6811802142106764293
secUid	MS4wLjABAAAA...
Output Format

JSON with structure:

{
  "target": "chengfeng_yulin",
  "secUid": "MS4wLjAB...",
  "uid": "68118...",
  "uniqueId": "chengfeng_yulin",
  "mode": "guest",
  "totalCollections": 50,
  "totalVideos": 308,
  "elapsedSeconds": 40.0,
  "collections": [
    {
      "collectionId": "760379...",
      "name": "收藏夹名称",
      "expected": 3,
      "actual": 3,
      "items": [
        {
          "id": "760251...",
          "url": "https://www.tiktok.com/@author/video/760251...",
          "desc": "Video description...",
          "author": "author_username",
          "plays": 2000000,
          "likes": 25100,
          "comments": 632,
          "shares": 85000
        }
      ]
    }
  ]
}

Cookie
Not needed for public collections (status=3, typically ~50% of folders, ~80% of videos)
Needed for private collections (status=1) — must be the target account's own login cookie
Cookie format: raw cookie string from browser (semicolon-separated key=value pairs)
How It Works

Uses TikTok's internal web APIs with curl_cffi for Chrome TLS fingerprint impersonation:

Resolve user — any input format → secUid (via TikTok's own redirects and page parsing)
Fetch collections — GET /api/user/collection_list/ (no auth needed)
Fetch videos — GET /api/collection/item_list/ with sourceType=113 (the undocumented key parameter)

sourceType=113 is an undocumented parameter discovered through browser request interception. Without it, the API returns success with empty results.

See references/api-notes.md for full API documentation.

Error Handling
⚠️ = fewer videos than expected (likely deleted videos)
❌ = zero videos returned (video removed or API issue)
Script retries failed requests up to 3 times with 5s backoff
Progress is printed to stderr; JSON output goes to stdout (or file with -o)
Weekly Installs
43
Repository
yulin7645/tiktok-skills
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn