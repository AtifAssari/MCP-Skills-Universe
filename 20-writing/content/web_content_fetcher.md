---
title: web-content-fetcher
url: https://skills.sh/shino369/claude-code-personal-workspace/web-content-fetcher
---

# web-content-fetcher

skills/shino369/claude-code-personal-workspace/web-content-fetcher
web-content-fetcher
Installation
$ npx skills add https://github.com/shino369/claude-code-personal-workspace --skill web-content-fetcher
SKILL.md
Web Content Fetcher

Expert knowledge for fetching and parsing web content, handling size limitations, JavaScript-rendered sites, and extracting clean article content from HTML.

Overview

This skill provides battle-tested strategies for fetching web content in Claude Code, addressing critical challenges:

WebFetch tool limitation: ~50KB max content size
Read tool limitation: 256KB max file size per call
JavaScript-rendered content: Twitter/X, React SPAs require special handling

Four-tier approach:

Tier 1: WebFetch for small content (< 50KB)
Tier 2: curl + Task agent for any size static content ⭐ DEFAULT
Tier 3: Scripts for edge cases (EUC-JP encoding, complex HTML)
Tier 4: Playwright for JavaScript-rendered sites (Twitter/X, React SPAs)
Quick Tool Limitations
Tool	Max Size	Best For	Limitation
WebFetch	~50KB	Small articles, first attempt	Prompt length constraints
Read	256KB	Reading fetched files	Large files need pagination
curl	Unlimited	Any size content, raw downloads	No parsing
Task agent	Unlimited	Extraction from any size HTML	Handles pagination automatically
Tiered Fetching Strategy
Tier 1: Small Content - WebFetch Direct

Use when: Simple articles, API responses, first attempt on unknown content

Quick example:

WebFetch tool with url and extraction prompt


If fails: "Prompt too long" error → Switch to Tier 2

Tier 2: Any Size Content - curl + Task Agent ⭐ RECOMMENDED

Use when: News articles, blog posts, WebFetch fails, any content of any size

Quick workflow:

# 1. Create directory
mkdir -p output/tasks/YYYYMMDD_taskname/original

# 2. Fetch HTML
curl -s "URL" > output/tasks/YYYYMMDD_taskname/original/raw_html.html

# 3. Extract with Task agent
# Prompt: "Read HTML at [path], extract article content, save to fetched_content.md"


Why default: Handles any size, AI-powered extraction, no script setup needed.

For detailed workflow: See references/workflows.md

Tier 3: Script-Based Extraction - Edge Cases Only

Use when: Task agent struggles with complex HTML or special encoding requirements (EUC-JP)

Available scripts:

scripts/extract_article.js - Standard HTML with Mozilla Readability
scripts/extract_eucjp.js - Japanese EUC-JP encoded sites (4gamer.net)

Quick example:

node .claude/skills/web-content-fetcher/scripts/extract_article.js raw_html.html > fetched_content.md


Note: Try Task agent (Tier 2) first. Scripts only when Task agent explicitly fails.

For script details: See references/advanced-fetching.md

Tier 4: JavaScript-Rendered Content - Playwright

Use when: Twitter/X, React SPAs, dynamic sites, static fetch returns empty/error

Quick example:

node .claude/skills/web-content-fetcher/scripts/fetch_js_content.js \
  "https://x.com/user/status/123456789" \
  --output fetched_content.md


Common sites: Twitter/X, Threads, Instagram, React/Vue/Angular SPAs, AJAX-loaded content

Image Extraction:

Automatically extracts images if exist (Twitter/X, Threads, blogs, etc.)
Captures image URLs with alt text from main content area
Filters out small images (icons/logos) automatically
Output includes structured Media section with URLs for downloading

Setup required (one-time):

cd .claude/skills/web-content-fetcher
pnpm add -D playwright --save-catalog-name=dev
pnpm exec playwright install chromium


For Playwright details: See references/advanced-fetching.md

Decision Tree

Use this flowchart to choose the right approach:

Need to fetch web content?
│
├─ JavaScript-rendered site (Twitter/X, React SPA, dynamic content)?
│  └─ Use Playwright script (Tier 4)
│     └─ See: references/advanced-fetching.md
│
├─ Size unknown or small expected content?
│  └─ Try WebFetch (Tier 1)
│     ├─ Success? → Done ✓
│     └─ "Prompt too long" error? → Use Tier 2
│
├─ Any other case (medium/large content, WebFetch failed)?
│  └─ Use curl + Task agent (Tier 2) ⭐ DEFAULT
│     ├─ Success? → Done ✓
│     └─ Task agent struggles? → Use Tier 3
│        └─ See: references/advanced-fetching.md
│
└─ Edge cases (Task agent fails, special encoding)?
   └─ Use curl + script (Tier 3)
      └─ See: references/advanced-fetching.md

Standard Workflow Quick Reference

Most common pattern (works for 90% of cases):

# 1. Setup
mkdir -p output/tasks/20260111_taskname/original

# 2. Fetch
curl -s "URL" > output/tasks/20260111_taskname/original/raw_html.html

# 3. Extract (Task agent prompt)
"Read HTML file at [path], extract main article content,
remove navigation/ads/sidebars/comments/footer,
save clean markdown to: [path]/fetched_content.md"

# 4. Use
Read: output/tasks/20260111_taskname/original/fetched_content.md


For detailed workflows and patterns: See references/workflows.md

Common Use Cases

Translation with images:

Fetch content (Tier 2 or Tier 4 for JS sites)
Extract to original/fetched_content.md with readable format (includes Media section with image URLs)
Download images using URLs from Media section
Pass to /translate command

Analysis:

Fetch content (Tier 2 or Tier 4)
Extract to original/fetched_content.md with readable format
Read and analyze

Social media posts (Twitter/X, Threads, Instagram):

Use Playwright (Tier 4) directly
Automatically extracts text, images, and metadata
Outputs to fetched_content.md with Media section in a readable format
Download images from extracted URLs
Use for translation/analysis

For all patterns: See references/workflows.md

When Things Go Wrong

Common issues and quick fixes:

Issue	Quick Fix	Details
WebFetch "Prompt too long"	Switch to Tier 2	troubleshooting.md
Read tool file too large	Use Task agent	troubleshooting.md
Garbled Japanese text	EUC-JP encoding issue	troubleshooting.md
JavaScript required	Use Playwright (Tier 4)	troubleshooting.md
Anti-bot protection	Add user agent	troubleshooting.md
Authentication required	Use curl with headers/cookies	troubleshooting.md

For complete troubleshooting guide: See references/troubleshooting.md

Best Practices
Always use task directories: output/tasks/YYYYMMDD_taskname/
Default to Tier 2: curl + Task agent works for nearly all cases
Keep raw HTML: Save to original/raw_html.html for reference (except Tier 4)
Use Playwright for JS sites: Twitter/X, React SPAs, dynamic content
Clean content format: Always save extracted content as markdown
Descriptive naming: Use date prefix (YYYYMMDD_) and descriptive task names
Try simple first: WebFetch → curl + Task agent → Scripts (only if needed)
Task agent for extraction: Let AI handle pagination and parsing complexity
Reference Files

This skill uses progressive disclosure for efficiency. Core information is in this file. Detailed guides are in reference files:

references/workflows.md - Standard workflows, common patterns, directory structure, content extraction priorities
references/advanced-fetching.md - Tier 3 script-based extraction, Tier 4 Playwright details, setup instructions
references/troubleshooting.md - Common issues, solutions, quick reference commands

Read reference files when you need detailed guidance for specific scenarios.

Quick Start Examples

Simple article:

mkdir -p output/tasks/20260111_article/original
curl -s "https://example.com/article" > output/tasks/20260111_article/original/raw_html.html
# Task agent: Extract to fetched_content.md


Twitter/X post:

mkdir -p output/tasks/20260111_twitter/original
node .claude/skills/web-content-fetcher/scripts/fetch_js_content.js \
  "https://x.com/user/status/123" \
  --output output/tasks/20260111_twitter/original/fetched_content.md


Threads post:

mkdir -p output/tasks/20260111_threads/original
node .claude/skills/web-content-fetcher/scripts/fetch_js_content.js \
  "https://www.threads.com/@user/post/ABC123" \
  --output output/tasks/20260111_threads/original/fetched_content.md


Output format with images (works for all sites):

# Title

Main content text here...

### Media

1. Image description or alt text
   - URL: https://example.com/image1.jpg
2. Another image
   - URL: https://example.com/image2.jpg


Note:

Images are automatically extracted from the main content area
Small images (< 100x100px) like icons/logos are filtered out
Image formats: .jpg, .png, .webp, .gif, .svg - all preserved in URLs
When downloading, respect the original file extension

Japanese site (potential encoding issue):

mkdir -p output/tasks/20260111_japanese/original
curl -s "https://4gamer.net/..." > output/tasks/20260111_japanese/original/raw_html.html
# Task agent with encoding detection, or use extract_eucjp.js if needed

Weekly Installs
62
Repository
shino369/claude…orkspace
GitHub Stars
2
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn