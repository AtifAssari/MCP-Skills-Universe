---
title: web-scraper
url: https://skills.sh/agentbay-ai/agentbay-skills/web-scraper
---

# web-scraper

skills/agentbay-ai/agentbay-skills/web-scraper
web-scraper
Installation
$ npx skills add https://github.com/agentbay-ai/agentbay-skills --skill web-scraper
SKILL.md
Web Scraper

Fetch web page content (text + images) and save as HTML or Markdown locally.

Minimal dependencies: Only requires requests and beautifulsoup4 - no browser automation.

Default behavior: Downloads images to local images/ directory automatically.

Quick start
Single page
{baseDir}/scripts/scrape.py --url "https://example.com" --format html --output /tmp/page.html
{baseDir}/scripts/scrape.py --url "https://example.com" --format md --output /tmp/page.md

Recursive (follow links)
{baseDir}/scripts/scrape.py --url "https://docs.example.com" --format md --recursive --max-depth 2 --output ~/Downloads/docs-archive

Setup

Requires Python 3.8+ and minimal dependencies:

cd {baseDir}
pip install -r requirements.txt


Or install manually:

pip install requests beautifulsoup4


Note: No browser or driver needed - uses pure HTTP requests.

Inputs to collect
Single page mode
URL: The web page to scrape (required)
Format: html or md (default: html)
Output path: Where to save the file (default: current directory with auto-generated name)
Images: Downloads images by default (use --no-download-images to disable)
Recursive mode (--recursive)
URL: Starting point for recursive scraping
Format: html or md
Output directory: Where to save all scraped pages
Max depth: How many levels deep to follow links (default: 2)
Max pages: Maximum total pages to scrape (default: 50)
Domain filter: Whether to stay within same domain (default: yes)
Images: Downloads images by default
Conversation Flow
Ask user for the URL to scrape
Ask preferred output format (HTML or Markdown)
Note: Both formats include text and images by default
HTML: Preserves original structure with downloaded images
Markdown: Clean text format with downloaded images in images/ folder
For recursive mode: Ask max depth and max pages (optional, has sensible defaults)
Ask where to save (or suggest a default path like /tmp/ or ~/Downloads/)
Run the script and confirm success
Show the saved file/directory path
Examples
Single Page Scraping
Save as HTML
{baseDir}/scripts/scrape.py --url "https://docs.openclaw.ai/start/quickstart" --format html --output ~/Downloads/openclaw-quickstart.html

Save as Markdown (with images, default)
{baseDir}/scripts/scrape.py --url "https://en.wikipedia.org/wiki/Web_scraping" --format md --output ~/Documents/web-scraping.md


Result: Creates web-scraping.md + images/ folder with all downloaded images (text + images).

Without downloading images (optional)
{baseDir}/scripts/scrape.py --url "https://example.com" --format md --no-download-images


Result: Only text + image URLs (not downloaded locally).

Auto-generate filename
{baseDir}/scripts/scrape.py --url "https://example.com" --format html
# Saves to: example-com-{timestamp}.html

Recursive Scraping
Basic recursive crawl (depth 2, same domain, with images)
{baseDir}/scripts/scrape.py --url "https://docs.example.com" --format md --recursive --output ~/Downloads/docs-archive


Output structure (text + images for all pages):

docs-archive/
├── index.md
├── getting-started.md
├── api/
│   ├── authentication.md
│   └── endpoints.md
└── images/              # Shared images from all pages
    ├── logo.png
    └── diagram.svg

Deep crawl with custom limits
{baseDir}/scripts/scrape.py \
  --url "https://blog.example.com" \
  --format html \
  --recursive \
  --max-depth 3 \
  --max-pages 100 \
  --output ~/Archives/blog-backup

Ignore robots.txt (use with caution)
{baseDir}/scripts/scrape.py \
  --url "https://example.com" \
  --format md \
  --recursive \
  --no-respect-robots \
  --rate-limit 1.0

Faster scraping (reduced rate limit)
{baseDir}/scripts/scrape.py \
  --url "https://yoursite.com" \
  --format md \
  --recursive \
  --rate-limit 0.2

Features
Single Page Mode
HTML output: Preserves original page structure
✅ Clean, readable HTML document
✅ All images downloaded to images/ folder
✅ Suitable for offline viewing
Markdown output: Extracts clean text content
✅ Auto-downloads images to local images/ directory (default)
✅ Converts image URLs to relative paths
✅ Clean, readable format for archiving
✅ Fallback to original URLs if download fails
Use --no-download-images flag to keep original URLs only
Simple and fast: Pure HTTP requests, no browser needed
Auto filename: Generates safe filename from URL if not specified
Recursive Mode (--recursive)
✅ Intelligent link discovery: Automatically follows all links on crawled pages
✅ Depth control: --max-depth limits how many levels deep to crawl (default: 2)
✅ Page limit: --max-pages caps total pages to prevent runaway crawls (default: 50)
✅ Domain filtering: --same-domain keeps crawl within starting domain (default: on)
✅ robots.txt compliance: Respects site's crawling rules by default
✅ Rate limiting: --rate-limit adds delay between requests (default: 0.5s)
✅ Smart URL filtering: Skips images, scripts, CSS, and duplicate URLs
✅ Progress tracking: Real-time console output with success/fail/skip counts
✅ Organized output: Preserves URL structure in directory hierarchy
✅ Efficient crawling: Sequential with rate limiting to respect servers
Guardrails
Single Page Mode
Respect robots.txt and site terms of service
Some sites may block automated access; this tool uses standard HTTP requests
Large pages with many images may take time to download
Recursive Mode
Start small: Test with --max-depth 1 --max-pages 10 first
Respect robots.txt: Default is on; only use --no-respect-robots for your own sites
Rate limiting: Default 0.5s is polite; don't go below 0.2s for public sites
Same domain: Strongly recommended to keep --same-domain enabled
Monitor progress: Watch for high fail rates (may indicate blocking)
Storage: Recursive crawls can generate many files; ensure sufficient disk space
Legal: Ensure you have permission to crawl and archive the target site
Troubleshooting
Connection errors: Check your internet connection and URL validity
403/blocked: Some sites block scrapers; the tool uses realistic User-Agent headers
Timeout: Increase --timeout flag for slow-loading pages (value in seconds)
Image download fails: Images will fall back to original URLs
Missing images: Some sites use JavaScript to load images dynamically (not supported)
Weekly Installs
155
Repository
agentbay-ai/age…y-skills
GitHub Stars
35
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn