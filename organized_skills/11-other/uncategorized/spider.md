---
rating: ⭐⭐⭐
title: spider
url: https://skills.sh/johnlindquist/claude/spider
---

# spider

skills/johnlindquist/claude/spider
spider
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill spider
SKILL.md
Web Spider

Crawl and analyze websites.

Prerequisites
# curl for fetching
curl --version

# Gemini for analysis
pip install google-generativeai
export GEMINI_API_KEY=your_api_key

# Optional: better HTML parsing
npm install -g puppeteer
pip install beautifulsoup4

Basic Crawling
Fetch Page
# Simple fetch
curl -s "https://example.com"

# With headers
curl -s -H "User-Agent: Mozilla/5.0" "https://example.com"

# Follow redirects
curl -sL "https://example.com"

# Save to file
curl -s "https://example.com" -o page.html

# Get headers only
curl -sI "https://example.com"

# Get headers and body
curl -sD - "https://example.com"

Extract Links
# Extract all links from a page
curl -s "https://example.com" | grep -oE 'href="[^"]*"' | sed 's/href="//;s/"$//'

# Filter to specific domain
curl -s "https://example.com" | grep -oE 'href="https?://example\.com[^"]*"'

# Unique links
curl -s "https://example.com" | grep -oE 'href="[^"]*"' | sort -u

Quick Site Scan
#!/bin/bash
URL=$1
echo "=== Scanning: $URL ==="

echo ""
echo "### Response Info ###"
curl -sI "$URL" | head -20

echo ""
echo "### Links Found ###"
curl -s "$URL" | grep -oE 'href="[^"]*"' | sort -u | head -20

echo ""
echo "### Scripts ###"
curl -s "$URL" | grep -oE 'src="[^"]*\.js[^"]*"' | sort -u

echo ""
echo "### Meta Tags ###"
curl -s "$URL" | grep -oE '<meta[^>]*>' | head -10

AI-Powered Analysis
Page Analysis
CONTENT=$(curl -s "https://example.com")

gemini -m pro -o text -e "" "Analyze this webpage:

$CONTENT

Provide:
1. What is this page about?
2. Key information/content
3. Navigation structure
4. Technical observations (framework, libraries)
5. SEO observations"

Security Scan
URL="https://example.com"

# Gather information
HEADERS=$(curl -sI "$URL")
CONTENT=$(curl -s "$URL" | head -1000)

gemini -m pro -o text -e "" "Security scan this website:

URL: $URL

HEADERS:
$HEADERS

CONTENT SAMPLE:
$CONTENT

Check for:
1. Missing security headers (CSP, HSTS, X-Frame-Options)
2. Exposed sensitive information
3. Potential vulnerabilities in scripts/forms
4. Cookie security settings
5. HTTPS configuration"

Extract Structured Data
CONTENT=$(curl -s "https://example.com/products")

gemini -m pro -o text -e "" "Extract structured data from this page:

$CONTENT

Extract into JSON format:
- Product names
- Prices
- Descriptions
- Any available metadata"

Multi-Page Crawling
Crawl and Analyze
#!/bin/bash
BASE_URL=$1
MAX_PAGES=${2:-10}

# Get initial links
LINKS=$(curl -s "$BASE_URL" | grep -oE "href=\"$BASE_URL[^\"]*\"" | sed 's/href="//;s/"$//' | sort -u | head -$MAX_PAGES)

echo "Found $(echo "$LINKS" | wc -l) pages"

for link in $LINKS; do
  echo ""
  echo "=== $link ==="
  TITLE=$(curl -s "$link" | grep -oE '<title>[^<]*</title>' | sed 's/<[^>]*>//g')
  echo "Title: $TITLE"
done

Sitemap Processing
# Fetch and parse sitemap
curl -s "https://example.com/sitemap.xml" | grep -oE '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g'

# Crawl pages from sitemap
curl -s "https://example.com/sitemap.xml" | \
  grep -oE '<loc>[^<]*</loc>' | \
  sed 's/<[^>]*>//g' | \
  while read url; do
    echo "Processing: $url"
    # Your processing here
  done

Specific Extractions
Extract Text Content
# Remove HTML tags (basic)
curl -s "https://example.com" | sed 's/<[^>]*>//g' | tr -s ' \n'

# Using python
curl -s "https://example.com" | python3 -c "
from html.parser import HTMLParser
import sys

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data.strip())

p = TextExtractor()
p.feed(sys.stdin.read())
print(' '.join(filter(None, p.text)))
"

Extract API Endpoints
CONTENT=$(curl -s "https://example.com/app.js")

# Find API calls in JS
echo "$CONTENT" | grep -oE "(fetch|axios|http)\(['\"][^'\"]*['\"]" | sort -u

# AI extraction
gemini -m pro -o text -e "" "Extract API endpoints from this JavaScript:

$CONTENT

List all:
- API URLs
- HTTP methods used
- Request patterns"

Monitor Changes
#!/bin/bash
URL=$1
HASH_FILE="/tmp/page-hash-$(echo $URL | md5sum | cut -d' ' -f1)"

CURRENT=$(curl -s "$URL" | md5sum | cut -d' ' -f1)

if [ -f "$HASH_FILE" ]; then
  PREVIOUS=$(cat "$HASH_FILE")
  if [ "$CURRENT" != "$PREVIOUS" ]; then
    echo "Page changed: $URL"
    # Notify or log
  fi
fi

echo "$CURRENT" > "$HASH_FILE"

Best Practices
Respect robots.txt - Check before crawling
Rate limit - Don't overwhelm servers
Set User-Agent - Identify your crawler
Handle errors - Sites go down, pages 404
Cache responses - Don't re-fetch unnecessarily
Be ethical - Only crawl what you're allowed to
Check ToS - Some sites prohibit scraping
Weekly Installs
132
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn