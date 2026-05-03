---
title: web-scraper
url: https://skills.sh/zephyrwang6/myskill/web-scraper
---

# web-scraper

skills/zephyrwang6/myskill/web-scraper
web-scraper
Installation
$ npx skills add https://github.com/zephyrwang6/myskill --skill web-scraper
SKILL.md
Web Scraper

Fetch web page content and convert to clean markdown format.

Usage

Run the fetch script to get web content:

python3 scripts/fetch_url.py <url> [options]

Options
--timeout <seconds>: Request timeout (default: 30)
--max-length <chars>: Maximum output length (default: 100000)
--raw: Output raw HTML instead of markdown
Examples

Fetch single URL:

python3 scripts/fetch_url.py "https://example.com/article"


Fetch with custom timeout:

python3 scripts/fetch_url.py "https://example.com/article" --timeout 60


Fetch multiple URLs in parallel:

for url in "https://url1.com" "https://url2.com"; do
  python3 scripts/fetch_url.py "$url" &
done
wait

Workflow
Single URL: Run fetch_url.py with the URL
Multiple URLs: Run multiple fetch commands in parallel using background processes
Handle errors: If a URL fails, check:
Network connectivity
URL validity
Website may block automated requests (try different User-Agent or use browser automation)
Output Format

The script converts HTML to clean markdown:

Headings → #, ##, ###, etc.
Lists → - for unordered, 1. for ordered
Bold/Italic → **bold**, *italic*
Code blocks preserved
Navigation, footer, and ads removed
Troubleshooting

403 Forbidden: Website blocks automated requests. Consider:

Some sites require JavaScript rendering (not supported by this script)
Try accessing from a different network

Timeout errors: Increase timeout with --timeout 60

Empty content: Website may require JavaScript to render content

Weekly Installs
240
Repository
zephyrwang6/myskill
GitHub Stars
281
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn