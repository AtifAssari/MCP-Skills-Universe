---
rating: ⭐⭐⭐
title: duckducksearch
url: https://skills.sh/xsailor511/duckduck-web-search/duckducksearch
---

# duckducksearch

skills/xsailor511/duckduck-web-search/duckducksearch
duckducksearch
Installation
$ npx skills add https://github.com/xsailor511/duckduck-web-search --skill duckducksearch
SKILL.md
DuckDuckGo Search Skill
Overview

This skill provides web search capabilities using the DuckDuckGo search engine via the duckduckgo-search Python package. It enables text, image, video, and news searches with various filtering options.

Installation
pip install -U duckduckgo_search

Core Functionality
Text Search
from duckduckgo_search import DDGS

# Basic text search
results = DDGS().text("python programming", max_results=10)

# Advanced text search with filters
results = DDGS().text(
    keywords="python programming",
    region="us-en",           # Region: us-en, uk-en, cn-zh, etc.
    safesearch="moderate",    # on, moderate, off
    timelimit="m",           # d (day), w (week), m (month), y (year)
    backend="auto",          # auto, html, lite, bing
    max_results=10
)

Image Search
from duckduckgo_search import DDGS

results = DDGS().images(
    keywords="butterfly",
    region="wt-wt",
    safesearch="off",
    size=None,               # Small, Medium, Large, Wallpaper
    color="Monochrome",      # Color filters
    type_image=None,         # photo, clipart, gif, transparent, line
    layout=None,             # Square, Tall, Wide
    license_image=None,      # any, Public, Share, ShareCommercially, Modify, ModifyCommercially
    max_results=100
)

Video Search
from duckduckgo_search import DDGS

results = DDGS().videos(
    keywords="cars",
    region="wt-wt",
    safesearch="off",
    timelimit="w",
    resolution="high",       # high, standard
    duration="medium",      # short, medium, long
    license_videos=None,    # creativeCommon, youtube
    max_results=50
)

News Search
from duckduckgo_search import DDGS

results = DDGS().news(
    keywords="technology",
    region="us-en",
    safesearch="moderate",
    timelimit="d",          # d, w, m
    max_results=20
)

Available Regions
Region Code	Description
wt-wt	Worldwide (No region)
us-en	United States
uk-en	United Kingdom
cn-zh	China
jp-jp	Japan
kr-kr	Korea
de-de	Germany
fr-fr	France
in-en	India
au-en	Australia
ca-en	Canada
br-pt	Brazil
ru-ru	Russia
Search Operators

Use DuckDuckGo search operators for advanced queries:

Operator	Example	Description
Exact match	"cats and dogs"	Search for exact phrase
Exclude	cats -dogs	Exclude term
Require	cats +dogs	Require term
File type	cats filetype:pdf	Search PDFs, docs, etc.
Site	dogs site:example.com	Search specific site
Exclude site	cats -site:example.com	Exclude site
In title	intitle:dogs	Title must contain
In URL	inurl:cats	URL must contain
Proxy Support
# Using Tor Browser
ddgs = DDGS(proxy="tb", timeout=20)

# Using custom proxy
ddgs = DDGS(proxy="socks5://user:password@host:port", timeout=20)

# Via environment variable
import os
os.environ["DDGS_PROXY"] = "socks5://user:password@host:port"

Error Handling
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import (
    DuckDuckGoSearchException,
    RatelimitException,
    TimeoutException,
    ConversationLimitException,
)

try:
    results = DDGS().text("query", max_results=10)
except RatelimitException:
    print("Rate limit exceeded. Try using a proxy or waiting.")
except TimeoutException:
    print("Request timed out.")
except DuckDuckGoSearchException as e:
    print(f"Search error: {e}")

CLI Usage
# Text search
ddgs text -k "python tutorial"

# Search with region
ddgs text -k "news" -r cn-zh

# Search and save to CSV
ddgs text -k "research filetype:pdf" -m 50 -o results.csv

# Image search
ddgs images -k "landscape" -m 100 -d

# News search
ddgs news -k "technology" -m 50 -t d -o json

Result Format
Text Search Results
{
    "title": "Page Title",
    "href": "https://example.com",
    "body": "Page description..."
}

Image Search Results
{
    "title": "Image Title",
    "image": "https://original-image-url.jpg",
    "thumbnail": "https://thumbnail-url.jpg",
    "url": "https://source-page.com",
    "height": 3860,
    "width": 4044,
    "source": "Bing"
}

Video Search Results
{
    "content": "https://youtube.com/watch?v=...",
    "title": "Video Title",
    "description": "Video description...",
    "duration": "8:22",
    "provider": "YouTube",
    "published": "2024-07-03"
}

News Search Results
{
    "date": "2024-07-03T16:25:22+00:00",
    "title": "News Headline",
    "body": "News article description...",
    "url": "https://news-site.com/article",
    "image": "https://image-url.jpg",
    "source": "News Source Name"
}

Best Practices

Use context manager for proper resource cleanup:

with DDGS() as ddgs:
    results = ddgs.text("query")


Set reasonable max_results to avoid long wait times

Use region parameter for localized results

Implement retry logic for rate limiting:

import time

for attempt in range(3):
    try:
        results = DDGS().text("query", max_results=10)
        break
    except RatelimitException:
        time.sleep(2 ** attempt)


Use proxies for high-volume searches to avoid IP blocks

Notes
This library is for educational purposes only
Not intended for commercial use
Respect DuckDuckGo's Terms of Service
Package has been renamed to ddgs (use pip install ddgs for newer version)
Weekly Installs
99
Repository
xsailor511/duck…b-search
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail