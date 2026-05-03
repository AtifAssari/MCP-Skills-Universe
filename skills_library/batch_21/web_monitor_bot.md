---
title: web-monitor-bot
url: https://skills.sh/tianqiye/tockstalk-bot/web-monitor-bot
---

# web-monitor-bot

skills/tianqiye/tockstalk-bot/web-monitor-bot
web-monitor-bot
Installation
$ npx skills add https://github.com/tianqiye/tockstalk-bot --skill web-monitor-bot
SKILL.md
Web Monitor Bot
Overview

Create automated website monitoring systems with analytics dashboards. This skill generates a complete monitoring solution including a Playwright-based bot, configurable cron scheduling, real-time analytics dashboard, and intelligent notification system. Use when the user needs to track website changes, detect availability, or monitor specific conditions over time.

When to Use This Skill

Invoke this skill when the user requests:

"Monitor this website for changes"
"Alert me when this product is back in stock"
"Check this booking page every 5 minutes"
"Track when appointment slots become available"
"Watch this page and show me usage patterns"
Any scenario requiring periodic automated web checks with data analysis
Quick Start Workflow
1. Initial Setup

Run the interactive setup script to create a new monitoring project:

bash scripts/setup-monitor.sh


The script will:

Create project directory
Copy template files
Configure target URL and notification settings
Install dependencies
Set up cron schedule
Initialize analytics
2. Customize Detection Logic

Edit bot.js to implement custom monitoring logic. Look for TODO comments:

// TODO: Customize selector logic for your use case
const selector = process.env.TARGET_SELECTOR || 'body';

// TODO: Add custom detection logic here
// Examples:
// - Check if element exists
// - Extract and compare text
// - Verify button state
// - Monitor price changes


Common patterns are documented in references/playwright-selectors.md.

3. Test the Bot

Run manually to verify detection logic:

node bot.js


Check that:

Page loads correctly
Selectors find target elements
Detection logic works as expected
Analytics are logged to analytics.json
4. Activate Monitoring

Add to crontab for automated checking:

(crontab -l 2>/dev/null; echo "*/5 * * * * /path/to/project/run-bot.sh >> /path/to/project/bot.log 2>&1") | crontab -

5. View Analytics

Start the dashboard server:

./start-analytics.sh


Open http://localhost:3002 to view:

Total check count and match rate
Hourly activity patterns
Day-of-week trends
Real-time activity timeline
Common Use Cases
Use Case 1: Product Stock Monitor

User request: "Alert me when this product comes back in stock"

Implementation steps:

Set TARGET_URL to product page
Customize bot logic to check for "Add to Cart" button:
const addToCartButton = page.locator('button:has-text("Add to Cart")');
const isAvailable = await addToCartButton.isEnabled();

if (isAvailable) {
  await log('🛒 PRODUCT AVAILABLE!');
  analyticsData.foundMatch = true;
}

Set cron to check every 5-15 minutes
Configure Slack webhook for instant notifications
Use Case 2: Appointment Slot Tracker

User request: "Monitor this DMV website for available appointment dates"

Implementation steps:

Set TARGET_URL to appointment page
Customize to find available date elements:
const availableDates = await page.$$('.calendar-day.available');

if (availableDates.length > 0) {
  await log(`📅 Found ${availableDates.length} available dates!`);
  analyticsData.foundMatch = true;
  analyticsData.data.dates = availableDates.length;
}

Check every 5-10 minutes during business hours
Use analytics to identify when slots typically appear
Use Case 3: Event Ticket Monitor

User request: "Watch this Ticketmaster page for concert tickets"

Implementation steps:

Set TARGET_URL to event page
Check for ticket availability indicators:
const soldOutMessage = await page.locator('text=Sold Out').count();

if (soldOutMessage === 0) {
  await log('🎟️ TICKETS AVAILABLE!');
  analyticsData.foundMatch = true;
}

Peak window pattern: More frequent checks when tickets release
Analytics show release patterns for future events
Use Case 4: Restaurant Reservation Bot

User request: "Check this Tock restaurant every 5 minutes for open tables"

Implementation steps:

Set TARGET_URL to restaurant booking page
Implement login logic if required (save cookies for session persistence)
Add Cloudflare detection after page load
Check calendar for available days with human-like behavior:
// Check for Cloudflare first
await detectCloudflare(page, context, 'booking page');

// Random delay before checking calendar
await page.waitForTimeout(randomDelay(1000, 2000));

const availableDays = await page.$$('[data-testid="calendar-day"][aria-disabled="false"]');

if (availableDays.length > 0) {
  await log(`📅 Found ${availableDays.length} available days!`);

  // Human-like click on first available day
  await humanClick(page, '[data-testid="calendar-day"][aria-disabled="false"]');
}

Use peak window pattern for known release times (6pm PT, etc.)
Analytics track cloudflareBlocked to identify blocking patterns
Analytics Dashboard Features

The auto-generated dashboard (dashboard.html) provides:

Real-Time Metrics:

Total checks performed
Match rate percentage
Time since last check
Peak vs off-peak statistics

Pattern Visualization:

Hourly heatmap: Identifies when changes typically occur
Day-of-week chart: Shows weekly patterns
Timeline graph: Visual history of recent checks
Activity feed: Live feed of recent events

Use Analytics For:

Optimization: Adjust cron schedule based on actual patterns
Validation: Confirm bot is running and detecting correctly
Insights: Discover when target conditions actually occur
Reporting: Share monitoring data with stakeholders
Notification Strategy

The template implements smart notification logic:

Always notify (via Slack/webhook):

✅ Match found (target condition met)
❌ Critical errors (login failures, selector errors)
🚨 First detection of availability

Console only (no notifications):

⚪ No match found (routine check)
🔑 Session reuse
📊 Analytics logging

To customize notification behavior, edit the log() vs consoleLog() function calls in bot.js.

Cron Scheduling Patterns

Common patterns documented in references/cron-patterns.md:

High-Frequency Monitoring:

*/5 * * * * /path/to/run-bot.sh  # Every 5 minutes


Business Hours Only:

*/10 9-17 * * 1-5 /path/to/run-bot.sh  # Every 10 min, 9-5 weekdays


Peak Window Pattern:

59 19 * * * /path/to/peak-run.sh      # 4 rapid checks at known time
*/15 * * * * /path/to/run-bot.sh      # Every 15 min otherwise

Session Persistence

The bot template includes cookie-based session management:

// Saves cookies after login
await saveCookies(context);

// Loads cookies on next run (avoids re-login)
const hasCookies = await loadCookies(context);


Benefits:

Faster execution (skip login flow)
Avoid rate limiting from repeated logins
Maintain user state across checks

Update the login logic in bot.js for website-specific authentication.

Anti-Detection Features (Production-Tested)

The bot template includes production-tested anti-detection utilities to reduce Cloudflare challenges and bot detection:

Random Delays

Replace fixed timing with random delays to avoid robotic patterns:

// Bad: Fixed timing (robotic)
await page.waitForTimeout(3000);

// Good: Random timing (human-like)
await page.waitForTimeout(randomDelay(2000, 4000));

Human-Like Mouse Movement

Simulate natural cursor movement before clicks:

// Bad: Instant click (teleporting cursor)
await page.click('.button');

// Good: Mouse movement + random position click
await humanClick(page, '.button');


This function:

Moves cursor in curved path (random steps)
Clicks random position within element (not exact center)
Adds random hesitation before click (100-300ms)
Intelligent Cloudflare Handling

Automatically detect and handle Cloudflare Turnstile challenges:

// Check for Cloudflare after page load
await detectCloudflare(page, context, 'initial load');


Features:

Smart polling: Checks every 10s for up to 90s (not single wait)
Block tracking: Tracks consecutive/total blocks in cloudflare-blocks.json
Auto-screenshots: cloudflare-detected.png, cloudflare-cleared.png, cloudflare-timeout.png
Cookie persistence: Saves session immediately after challenge clears
Progress updates: Console logs every 30s
Alert on repeated blocks: Warns if 3+ consecutive blocks occur

Block Analytics:

const blocks = getCloudflareBlocks();
console.log(`Consecutive blocks: ${blocks.consecutive}`);
console.log(`Total blocks: ${blocks.total}`);
console.log(`Last 10 events:`, blocks.history.slice(-10));


The analytics.json file tracks cloudflareBlocked: boolean per run for pattern analysis.

Stealth Mode

The template uses playwright-extra with puppeteer-extra-plugin-stealth to mask automation signals:

const { chromium } = require('playwright-extra');
const stealth = require('puppeteer-extra-plugin-stealth')();
chromium.use(stealth);


This hides common bot indicators like navigator.webdriver, headless Chrome flags, and automation properties.

Usage in Custom Detection Logic

Integrate anti-detection utilities in custom monitoring code:

// Example: Check availability with human-like behavior
await page.waitForTimeout(randomDelay(1000, 2000)); // Random delay
const available = await page.locator('.available-slot').count() > 0;

if (available) {
  await humanClick(page, '.available-slot'); // Mouse movement
  await page.waitForTimeout(randomDelay(500, 1000));
  // ... continue workflow
}

Concurrency Protection

The template includes lock file management to prevent overlapping executions:

checkLock();    // Exit if another instance is running
createLock();   // Create lock for this instance
removeLock();   // Clean up on exit


This ensures:

No duplicate checks
Safe cron scheduling
Clean process management
Advanced Customization
Peak Window Detection

Add time-based logic for higher-traffic periods:

const now = new Date();
const hour = now.getUTCHours();
const isPeakWindow = (hour === 19 && minute === 59);  // 7:59 PM UTC

// Use longer timeouts during peak
const timeout = isPeakWindow ? 60000 : 30000;

Screenshot on Match

Capture evidence when target condition is met:

if (foundMatch) {
  await page.screenshot({ path: `match-${Date.now()}.png` });
  await log('📸 Screenshot saved');
}

Multi-Page Monitoring

Check multiple pages in sequence:

const urls = [url1, url2, url3];
for (const url of urls) {
  await page.goto(url);
  await checkConditions(page);
}

Troubleshooting

Bot not detecting changes:

Run manually with DEBUG=true node bot.js
Check selectors in browser DevTools
Verify page loads completely (increase timeouts)
Review references/playwright-selectors.md for selector techniques

Cron not running:

Verify cron service: systemctl status cron
Check crontab: crontab -l
Review logs: tail -f /path/to/bot.log
Test script manually: bash run-bot.sh

Dashboard not showing data:

Verify analytics.json exists and has data
Check server is running: ps aux | grep analytics-server
Verify port is available: netstat -tuln | grep 3002
Check browser console for errors
Resources
Scripts
setup-monitor.sh - Interactive project initialization
References
playwright-selectors.md - Element finding techniques and patterns
cron-patterns.md - Common scheduling configurations
Assets
bot-template.js - Configurable Playwright monitoring bot
analytics-server.js - Express server for dashboard
dashboard.html - Real-time analytics visualization
package.json - Node.js dependencies
.env.example - Configuration template
Weekly Installs
14
Repository
tianqiye/tockstalk-bot
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn