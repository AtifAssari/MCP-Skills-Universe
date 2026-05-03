---
title: crawler
url: https://skills.sh/gn00678465/crawler-skill/crawler
---

# crawler

skills/gn00678465/crawler-skill/crawler
crawler
Installation
$ npx skills add https://github.com/gn00678465/crawler-skill --skill crawler
SKILL.md
Crawler Skill

Converts any URL into clean markdown using a robust 3-tier fallback chain.

Quick start
uv run scripts/crawl.py --url https://example.com --output reports/example.md


Markdown is saved to the file specified by --output. Progress/errors go to stderr. Exit code 0 on success, 1 if all scrapers fail.

How it works

The script tries each tier in order and returns the first success:

Tier	Module	Requires
1	Firecrawl (firecrawl_scraper.py)	FIRECRAWL_API_KEY env var (optional; falls back if missing)
2	Jina Reader (jina_reader.py)	Nothing — free, no key needed
3	Scrapling (scrapling_scraper.py)	Local headless browser (auto-installs via pip)
File layout
crawler-skill/
├── SKILL.md            ← this file
├── scripts/
│   ├── crawl.py               ← main CLI entry point (PEP 723 inline deps)
│   └── src/
│       ├── domain_router.py       ← URL-to-tier routing rules
│       ├── firecrawl_scraper.py   ← Tier 1: Firecrawl API
│       ├── jina_reader.py         ← Tier 2: Jina r.jina.ai proxy
│       └── scrapling_scraper.py   ← Tier 3: local headless scraper
└── tests/
    └── test_crawl.py          ← 70 pytest tests (all passing)

Usage examples
# Basic fetch — tries Firecrawl, falls back to Jina, then Scrapling
# Always prefer using --output to avoid terminal encoding issues
uv run scripts/crawl.py --url https://docs.python.org/3/ --output reports/python_docs.md

# If no --output is provided, markdown goes to stdout (not recommended on Windows)
uv run scripts/crawl.py --url https://example.com

# With a Firecrawl API key for best results
FIRECRAWL_API_KEY=fc-... uv run scripts/crawl.py --url https://example.com --output reports/example.md

URL requirements

Only http:// and https:// URLs are accepted. Passing any other scheme (ftp://, file://, javascript:, a bare path, etc.) exits with code 1 and prints a clear error — no scraping is attempted.

Saving Reports

When the user asks to save the crawled content or a summary to a file, ALWAYS use the --output argument and save the file into the reports/ directory at the project root (for example, {project_root}/reports). If the directory does not exist, the script will create it.

Example: If asked to "save to result.md", you should run: uv run scripts/crawl.py --url <URL> --output reports/result.md

Point at a self-hosted Firecrawl instance
FIRECRAWL_API_URL=http://localhost:3002 uv run scripts/crawl.py --url https://example.com

Content validation

Each scraper validates its output before returning success:

Minimum 100 characters of content (rejects empty/error pages)
Detection of CAPTCHA / bot-verification pages (Firecrawl)
Detection of Cloudflare interstitial pages (Scrapling — escalates to StealthyFetcher)
Detection of Jina error page indicators (Error:, Access Denied, etc.)
Domain routing

Certain hostnames bypass one or more scraper tiers to avoid known compatibility issues. The logic lives in scripts/src/domain_router.py.

Domain	Skipped tiers	Active chain
medium.com (and subdomains)	firecrawl	jina → scrapling
mp.weixin.qq.com	firecrawl + jina	scrapling only
everything else	—	firecrawl → jina → scrapling

Sub-domain matching follows a suffix rule: blog.medium.com matches the medium.com rule because its hostname ends with .medium.com. An exact sub-domain like other.weixin.qq.com does not match mp.weixin.qq.com.

Running tests
uv run pytest tests/ -v


All 70 tests use mocking — no network calls, no API keys required.

Dependencies (auto-installed by uv run)
firecrawl-py>=2.0 — Firecrawl Python SDK
httpx>=0.27 — HTTP client for Jina Reader
scrapling>=0.2 — Headless scraping with stealth support
html2text>=2024.2.26 — HTML-to-markdown conversion
When to invoke this skill

Invoke crawl.py whenever you need the text content of a web page:

result = subprocess.run(
    ["uv", "run", "scripts/crawl.py", "--url", url],
    capture_output=True, text=True
)
if result.returncode == 0:
    markdown = result.stdout


Or simply run it directly from the terminal as shown in Quick start above.

Weekly Installs
94
Repository
gn00678465/crawler-skill
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn