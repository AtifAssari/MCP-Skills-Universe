---
rating: ⭐⭐⭐
title: lighthouse
url: https://skills.sh/onnokh/lighthouse/lighthouse
---

# lighthouse

skills/onnokh/lighthouse/lighthouse
lighthouse
Installation
$ npx skills add https://github.com/onnokh/lighthouse --skill lighthouse
SKILL.md
Google Lighthouse

Comprehensive reference for Google Lighthouse - an open-source, automated tool for improving the quality of web pages. It has audits for performance, accessibility, progressive web apps, SEO and more.

Source: https://github.com/GoogleChrome/lighthouse
NPM Package: https://www.npmjs.com/package/lighthouse
Documentation: https://developer.chrome.com/docs/lighthouse/overview/

Prerequisites
Requirements
Node.js: Version 22 (LTS) or later
Chrome/Chromium: Version 66.0 or later
Installation
# Global installation (recommended)
npm install -g lighthouse

# Or use yarn
yarn global add lighthouse

# Verify installation
lighthouse --version

Chrome Setup

Lighthouse uses Chrome/Chromium. You can:

Use existing Chrome/Chrome Canary installation
Set custom Chrome binary via CHROME_PATH environment variable
Pass custom flags via --chrome-flags
Quick Start
# Basic audit - generates HTML report
lighthouse https://example.com

# View report immediately in browser
lighthouse https://example.com --view

# JSON output to stdout
lighthouse https://example.com --output json

# Save to specific path
lighthouse https://example.com --output-path ./report.html

CLI Options
Output Options
lighthouse <url> --output <format> --output-path <path>

# Output formats (can use multiple)
--output html          # HTML report (default)
--output json          # JSON output
--output csv           # CSV output

# Examples
lighthouse https://example.com --output json                    # JSON to stdout
lighthouse https://example.com --output html --output-path ./audit.html
lighthouse https://example.com --output json --output html      # Both formats

Audit Categories
# Run specific categories only
lighthouse https://example.com --only-categories=performance,accessibility

# Available categories:
# - performance
# - accessibility
# - best-practices
# - seo
# - pwa (Progressive Web App)

# Skip specific audits
lighthouse https://example.com --skip-audits=unused-javascript,offscreen-images

# List all available audits
lighthouse --list-all-audits

Presets & Device Emulation
# Use built-in presets
lighthouse https://example.com --preset=desktop    # Desktop preset
lighthouse https://example.com --preset=perf       # Performance only
lighthouse https://example.com --preset=experimental  # Experimental audits

# Form factor
lighthouse https://example.com --form-factor=mobile   # Mobile (default)
lighthouse https://example.com --form-factor=desktop  # Desktop

# Screen emulation
lighthouse https://example.com --screenEmulation.mobile
lighthouse https://example.com --screenEmulation.width=1280 --screenEmulation.height=720
lighthouse https://example.com --screenEmulation.disabled  # Disable emulation

Network & CPU Throttling
# Throttling methods
--throttling-method=simulate    # Simulate throttling (default, fastest)
--throttling-method=devtools    # Use DevTools throttling
--throttling-method=provided    # No throttling

# Custom throttling settings
--throttling.rttMs=150                    # Network RTT
--throttling.throughputKbps=1600          # Download speed
--throttling.cpuSlowdownMultiplier=4      # CPU slowdown

Chrome Configuration
# Custom Chrome path (via environment variable)
CHROME_PATH=/path/to/chrome lighthouse https://example.com

# Chrome flags
lighthouse https://example.com --chrome-flags="--headless --no-sandbox"
lighthouse https://example.com --chrome-flags="--window-size=412,660"
lighthouse https://example.com --chrome-flags="--disable-gpu --disable-dev-shm-usage"

# Debug protocol settings
--port=9222                    # Use specific debugging port
--hostname=localhost           # Custom hostname

Advanced Options
# Max wait time for page load (milliseconds)
--max-wait-for-load=60000

# Save assets (trace and devtools log)
--save-assets

# Disable full page screenshot (reduces report size)
--disable-full-page-screenshot

# Disable storage reset (keep cache/cookies)
--disable-storage-reset

# Block URL patterns
--blocked-url-patterns="*.png" --blocked-url-patterns="*.jpg"

# Extra HTTP headers
--extra-headers="{\"Cookie\":\"monster=blue\", \"Authorization\":\"Bearer token\"}"

# Locale/language for report
--locale=en

# Plugins
--plugins=lighthouse-plugin-field-performance

Lifecycle Modes
Gather Mode (Collect Artifacts)
# Collect artifacts and save to disk
lighthouse https://example.com --gather-mode

# Save to custom folder
lighthouse https://example.com -G=./artifacts/

# Collects: trace, devtools log, page artifacts

Audit Mode (Process Saved Artifacts)
# Process previously saved artifacts
lighthouse --audit-mode

# Load from custom folder
lighthouse -A=./artifacts/

# Skips browser interaction, runs audits on saved data

Combined Mode
# Normal run + save artifacts for later
lighthouse https://example.com -GA

# With custom folder
lighthouse https://example.com -GA=./my-run/

Configuration File

Create lighthouse-config.js:

module.exports = {
  extends: 'lighthouse:default',
  settings: {
    formFactor: 'desktop',
    throttling: {
      rttMs: 40,
      throughputKbps: 10240,
      cpuSlowdownMultiplier: 1,
    },
    screenEmulation: {
      mobile: false,
      width: 1350,
      height: 940,
      deviceScaleFactor: 1,
      disabled: false,
    },
    emulatedUserAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    onlyCategories: ['performance', 'accessibility', 'best-practices', 'seo'],
  },
};


Use it:

lighthouse https://example.com --config-path=./lighthouse-config.js

Viewing Reports
HTML Reports
# Auto-open in browser
lighthouse https://example.com --view

# Open report manually
open ./example.com_2024-01-01.report.html

JSON Reports
# Generate JSON
lighthouse https://example.com --output=json --output-path=./report.json

# View online at Lighthouse Viewer
cat ./report.json | xclip -selection clipboard
# Then visit: https://googlechrome.github.io/lighthouse/viewer/

Online Viewer

Upload JSON reports to: https://googlechrome.github.io/lighthouse/viewer/

Drag and drop JSON files
Share reports as secret GitHub gists
Compare historical reports
Common Use Cases
Mobile Performance Audit
lighthouse https://example.com \
  --form-factor=mobile \
  --only-categories=performance \
  --preset=perf \
  --view

Desktop Full Audit
lighthouse https://example.com \
  --preset=desktop \
  --view

CI/CD Integration
# Quiet mode for CI
lighthouse https://example.com --quiet --chrome-flags="--headless --no-sandbox"

# JSON output for programmatic processing
lighthouse https://example.com --output=json --quiet > report.json

Batch Auditing
# Audit multiple URLs
for url in https://example.com https://example.com/about; do
  lighthouse "$url" --output=json --output-path="./reports/$(echo $url | sed 's/[^a-zA-Z0-9]/_/g').json"
done

Authenticated Pages
# Pass authentication cookies
lighthouse https://example.com/dashboard \
  --extra-headers="{\"Cookie\":\"sessionid=abc123; auth_token=xyz\"}"

# Or use config file for complex auth

Performance Budgets

Lighthouse doesn't enforce budgets natively, but you can combine with lighthouse-ci:

# Install lighthouse-ci
npm install -g @lhci/cli

# Run with assertions
lhci autorun --config=lighthouserc.js


Example lighthouserc.js:

module.exports = {
  ci: {
    assert: {
      assertions: {
        'categories:performance': ['warn', {minScore: 0.9}],
        'categories:accessibility': ['error', {minScore: 1}],
        'first-contentful-paint': ['warn', {maxNumericValue: 2000}],
      },
    },
  },
};

Troubleshooting
Chrome Won't Start
# Try headless mode
lighthouse https://example.com --chrome-flags="--headless --no-sandbox --disable-gpu"

# Check Chrome version
chrome --version  # Should be 66+

# Specify Chrome path
CHROME_PATH=/usr/bin/google-chrome-stable lighthouse https://example.com

Connection Issues
# Use specific port
lighthouse https://example.com --port=9222

# Allow more time for page load
lighthouse https://example.com --max-wait-for-load=90000

Large Trace Files
# Disable full page screenshot
lighthouse https://example.com --disable-full-page-screenshot

# Don't save assets
# (don't use --save-assets)

Key Metrics Reference
Metric	Target	Description
Performance Score	90+	Overall performance score (0-100)
First Contentful Paint (FCP)	< 1.8s	First text/image painted
Largest Contentful Paint (LCP)	< 2.5s	Largest element painted
Total Blocking Time (TBT)	< 200ms	Main thread blocked time
Cumulative Layout Shift (CLS)	< 0.1	Visual stability score
Speed Index	< 3.4s	Visual completeness speed
Related Tools
Lighthouse CI: Continuous integration for Lighthouse
Lighthouse Viewer: Online report viewer
Lighthouse CLI: This tool (Node module also available)
Chrome DevTools: Built-in Lighthouse panel
Resources
GitHub: https://github.com/GoogleChrome/lighthouse
Documentation: https://developer.chrome.com/docs/lighthouse/
Scoring Guide: https://developer.chrome.com/docs/lighthouse/performance/performance-scoring/
Stack Overflow: https://stackoverflow.com/questions/tagged/lighthouse
Weekly Installs
172
Repository
onnokh/lighthouse
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail