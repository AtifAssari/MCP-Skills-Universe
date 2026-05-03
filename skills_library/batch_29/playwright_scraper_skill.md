---
title: playwright-scraper-skill
url: https://skills.sh/csy12138da/playwright-scraper-skill/playwright-scraper-skill
---

# playwright-scraper-skill

skills/csy12138da/playwright-scraper-skill/playwright-scraper-skill
playwright-scraper-skill
Installation
$ npx skills add https://github.com/csy12138da/playwright-scraper-skill --skill playwright-scraper-skill
SKILL.md
Playwright Scraper Skill

A Playwright-based web scraping skill with anti-bot protection. Choose the best approach based on the target website's anti-bot level.

🎯 Use Case Matrix
Target Website	Anti-Bot Level	Recommended Method	Script
Regular Sites	Low	web_fetch tool	N/A (built-in)
Dynamic Sites	Medium	Playwright Simple	scripts/playwright-simple.js
Cloudflare Protected	High	Playwright Stealth ⭐	scripts/playwright-stealth.js
📦 Installation
cd playwright-scraper-skill
npm install
npx playwright install chromium

🚀 Quick Start
1️⃣ Simple Sites (No Anti-Bot)

Use built-in web_fetch tool for static sites.

2️⃣ Dynamic Sites (Requires JavaScript)

Use Playwright Simple:

node scripts/playwright-simple.js "https://example.com"

3️⃣ Anti-Bot Protected Sites (Cloudflare etc.)

Use Playwright Stealth:

node scripts/playwright-stealth.js "https://m.discuss.com.hk/#hot"


Features:

Hide automation markers (navigator.webdriver = false)
Realistic User-Agent (iPhone, Android)
Random delays to mimic human behavior
Screenshot and HTML saving support
📖 Script Descriptions
scripts/playwright-simple.js
Use Case: Regular dynamic websites
Speed: Fast (3-5 seconds)
Anti-Bot: None
Output: JSON (title, content, URL)
scripts/playwright-stealth.js ⭐
Use Case: Sites with Cloudflare or anti-bot protection
Speed: Medium (5-20 seconds)
Anti-Bot: Medium-High (hides automation, realistic UA)
Output: JSON + Screenshot + HTML file
Verified: 100% success on Discuss.com.hk
🔧 Customization

All scripts support environment variables:

# Set screenshot path
SCREENSHOT_PATH=/path/to/screenshot.png node scripts/playwright-stealth.js URL

# Set wait time (milliseconds)
WAIT_TIME=10000 node scripts/playwright-simple.js URL

# Enable headful mode (show browser)
HEADLESS=false node scripts/playwright-stealth.js URL

# Save HTML
SAVE_HTML=true node scripts/playwright-stealth.js URL

# Custom User-Agent
USER_AGENT="Mozilla/5.0 ..." node scripts/playwright-stealth.js URL

🛡️ Anti-Bot Techniques Summary
✅ Effective Anti-Bot Measures
Hide navigator.webdriver — Essential
Realistic User-Agent — Use real devices (iPhone, Android)
Mimic Human Behavior — Random delays, scrolling
Avoid Framework Signatures — Crawlee, Selenium are easily detected
Use addInitScript (Playwright) — Inject before page load
❌ Ineffective Anti-Bot Measures
Only changing User-Agent — Not enough
Using high-level frameworks (Crawlee) — More easily detected
Docker isolation — Doesn't help with Cloudflare
🔍 Troubleshooting
Issue: 403 Forbidden

Solution: Use playwright-stealth.js

Issue: Cloudflare Challenge Page

Solution:

Increase wait time (10-15 seconds)
Try headless: false (headful mode sometimes has higher success rate)
Consider using proxy IPs
📚 References
Playwright Official Docs
puppeteer-extra-plugin-stealth
Weekly Installs
38
Repository
csy12138da/play…er-skill
GitHub Stars
2
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn