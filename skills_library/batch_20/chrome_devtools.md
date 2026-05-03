---
title: chrome-devtools
url: https://skills.sh/jackspace/claudeskillz/chrome-devtools
---

# chrome-devtools

skills/jackspace/claudeskillz/chrome-devtools
chrome-devtools
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill chrome-devtools
SKILL.md
Chrome DevTools Agent Skill

Browser automation via executable Puppeteer scripts. All scripts output JSON for easy parsing.

Quick Start

CRITICAL: Always check pwd before running scripts.

Installation
Step 1: Install System Dependencies (Linux/WSL only)

On Linux/WSL, Chrome requires system libraries. Install them first:

pwd  # Should show current working directory
cd .claude/skills/chrome-devtools/scripts
./install-deps.sh  # Auto-detects OS and installs required libs


Supports: Ubuntu, Debian, Fedora, RHEL, CentOS, Arch, Manjaro

macOS/Windows: Skip this step (dependencies bundled with Chrome)

Step 2: Install Node Dependencies
npm install  # Installs puppeteer, debug, yargs

Step 3: Install ImageMagick (Optional, Recommended)

ImageMagick enables automatic screenshot compression to keep files under 5MB:

macOS:

brew install imagemagick


Ubuntu/Debian/WSL:

sudo apt-get install imagemagick


Windows:

# Option 1: Chocolatey (recommended)
choco install imagemagick

# Option 2: Scoop
scoop install imagemagick

# Option 3: WinGet
winget install ImageMagick.ImageMagick

# Option 4: Manual download from https://imagemagick.org/script/download.php#windows


Fedora/RHEL/CentOS:

sudo dnf install ImageMagick
# or for older versions:
sudo yum install ImageMagick


Arch/Manjaro:

sudo pacman -S imagemagick


Verify installation:

# Linux/macOS:
magick -version  # or: convert -version

# Windows:
magick -version
# or: magick.exe -version


Without ImageMagick, screenshots >5MB will not be compressed (may fail to load in Gemini/Claude).

Test
node navigate.js --url https://example.com
# Output: {"success": true, "url": "https://example.com", "title": "Example Domain"}

Available Scripts

All scripts are in .claude/skills/chrome-devtools/scripts/

CRITICAL: Always check pwd before running scripts.

Script Usage
./scripts/README.md
Core Automation
navigate.js - Navigate to URLs
screenshot.js - Capture screenshots (full page or element)
click.js - Click elements
fill.js - Fill form fields
evaluate.js - Execute JavaScript in page context
Analysis & Monitoring
snapshot.js - Extract interactive elements with metadata
console.js - Monitor console messages/errors
network.js - Track HTTP requests/responses
performance.js - Measure Core Web Vitals + record traces
Usage Patterns
Single Command
pwd  # Should show current working directory
cd .claude/skills/chrome-devtools/scripts
node screenshot.js --url https://example.com --output ./docs/screenshots/page.png


Important: Always save screenshots to ./docs/screenshots directory.

Automatic Image Compression

Screenshots are automatically compressed if they exceed 5MB to ensure compatibility with Gemini API and Claude Code (which have 5MB limits). This uses ImageMagick internally:

# Default: auto-compress if >5MB
node screenshot.js --url https://example.com --output page.png

# Custom size threshold (e.g., 3MB)
node screenshot.js --url https://example.com --output page.png --max-size 3

# Disable compression
node screenshot.js --url https://example.com --output page.png --no-compress


Compression behavior:

PNG: Resizes to 90% + quality 85 (or 75% + quality 70 if still too large)
JPEG: Quality 80 + progressive encoding (or quality 60 if still too large)
Other formats: Converted to JPEG with compression
Requires ImageMagick installed (see imagemagick skill)

Output includes compression info:

{
  "success": true,
  "output": "/path/to/page.png",
  "compressed": true,
  "originalSize": 8388608,
  "size": 3145728,
  "compressionRatio": "62.50%",
  "url": "https://example.com"
}

Chain Commands (reuse browser)
# Keep browser open with --close false
node navigate.js --url https://example.com/login --close false
node fill.js --selector "#email" --value "user@example.com" --close false
node fill.js --selector "#password" --value "secret" --close false
node click.js --selector "button[type=submit]"

Parse JSON Output
# Extract specific fields with jq
node performance.js --url https://example.com | jq '.vitals.LCP'

# Save to file
node network.js --url https://example.com --output /tmp/requests.json

Execution Protocol
Working Directory Verification

BEFORE executing any script:

Check current working directory with pwd
Verify in .claude/skills/chrome-devtools/scripts/ directory
If wrong directory, cd to correct location
Use absolute paths for all output files

Example:

pwd  # Should show: .../chrome-devtools/scripts
# If wrong:
cd .claude/skills/chrome-devtools/scripts

Output Validation

AFTER screenshot/capture operations:

Verify file created with ls -lh <output-path>
Read screenshot using Read tool to confirm content
Check JSON output for success:true
Report file size and compression status

Example:

node screenshot.js --url https://example.com --output ./docs/screenshots/page.png
ls -lh ./docs/screenshots/page.png  # Verify file exists
# Then use Read tool to visually inspect

Restart working directory to the project root.
Error Recovery

If script fails:

Check error message for selector issues
Use snapshot.js to discover correct selectors
Try XPath selector if CSS selector fails
Verify element is visible and interactive

Example:

# CSS selector fails
node click.js --url https://example.com --selector ".btn-submit"
# Error: waiting for selector ".btn-submit" failed

# Discover correct selector
node snapshot.js --url https://example.com | jq '.elements[] | select(.tagName=="BUTTON")'

# Try XPath
node click.js --url https://example.com --selector "//button[contains(text(),'Submit')]"

Common Mistakes

❌ Wrong working directory → output files go to wrong location ❌ Skipping output validation → silent failures ❌ Using complex CSS selectors without testing → selector errors ❌ Not checking element visibility → timeout errors

✅ Always verify pwd before running scripts ✅ Always validate output after screenshots ✅ Use snapshot.js to discover selectors ✅ Test selectors with simple commands first

Common Workflows
Web Scraping
node evaluate.js --url https://example.com --script "
  Array.from(document.querySelectorAll('.item')).map(el => ({
    title: el.querySelector('h2')?.textContent,
    link: el.querySelector('a')?.href
  }))
" | jq '.result'

Performance Testing
PERF=$(node performance.js --url https://example.com)
LCP=$(echo $PERF | jq '.vitals.LCP')
if (( $(echo "$LCP < 2500" | bc -l) )); then
  echo "✓ LCP passed: ${LCP}ms"
else
  echo "✗ LCP failed: ${LCP}ms"
fi

Form Automation
node fill.js --url https://example.com --selector "#search" --value "query" --close false
node click.js --selector "button[type=submit]"

Error Monitoring
node console.js --url https://example.com --types error,warn --duration 5000 | jq '.messageCount'

Script Options

All scripts support:

--headless false - Show browser window
--close false - Keep browser open for chaining
--timeout 30000 - Set timeout (milliseconds)
--wait-until networkidle2 - Wait strategy

See ./scripts/README.md for complete options.

Output Format

All scripts output JSON to stdout:

{
  "success": true,
  "url": "https://example.com",
  ... // script-specific data
}


Errors go to stderr:

{
  "success": false,
  "error": "Error message"
}

Finding Elements

Use snapshot.js to discover selectors:

node snapshot.js --url https://example.com | jq '.elements[] | {tagName, text, selector}'

Troubleshooting
Common Errors

"Cannot find package 'puppeteer'"

Run: npm install in the scripts directory

"error while loading shared libraries: libnss3.so" (Linux/WSL)

Missing system dependencies
Fix: Run ./install-deps.sh in scripts directory
Manual install: sudo apt-get install -y libnss3 libnspr4 libasound2t64 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1

"Failed to launch the browser process"

Check system dependencies installed (Linux/WSL)
Verify Chrome downloaded: ls ~/.cache/puppeteer
Try: npm rebuild then npm install

Chrome not found

Puppeteer auto-downloads Chrome during npm install
If failed, manually trigger: npx puppeteer browsers install chrome
Script Issues

Element not found

Get snapshot first to find correct selector: node snapshot.js --url <url>

Script hangs

Increase timeout: --timeout 60000
Change wait strategy: --wait-until load or --wait-until domcontentloaded

Blank screenshot

Wait for page load: --wait-until networkidle2
Increase timeout: --timeout 30000

Permission denied on scripts

Make executable: chmod +x *.sh

Screenshot too large (>5MB)

Install ImageMagick for automatic compression
Manually set lower threshold: --max-size 3
Use JPEG format instead of PNG: --format jpeg --quality 80
Capture specific element instead of full page: --selector .main-content

Compression not working

Verify ImageMagick installed: magick -version or convert -version
Check file was actually compressed in output JSON: "compressed": true
For very large pages, use --selector to capture only needed area
Reference Documentation

Detailed guides available in ./references/:

CDP Domains Reference - 47 Chrome DevTools Protocol domains
Puppeteer Quick Reference - Complete Puppeteer API patterns
Performance Analysis Guide - Core Web Vitals optimization
Advanced Usage
Custom Scripts

Create custom scripts using shared library:

import { getBrowser, getPage, closeBrowser, outputJSON } from './lib/browser.js';
// Your automation logic

Direct CDP Access
const client = await page.createCDPSession();
await client.send('Emulation.setCPUThrottlingRate', { rate: 4 });


See reference documentation for advanced patterns and complete API coverage.

External Resources
Puppeteer Documentation
Chrome DevTools Protocol
Scripts README
Weekly Installs
34
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail