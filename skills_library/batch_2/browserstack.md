---
title: browserstack
url: https://skills.sh/alirezarezvani/claude-skills/browserstack
---

# browserstack

skills/alirezarezvani/claude-skills/browserstack
browserstack
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill browserstack
SKILL.md
BrowserStack Integration

Run Playwright tests on BrowserStack's cloud grid for cross-browser and cross-device testing.

Prerequisites

Environment variables must be set:

BROWSERSTACK_USERNAME — your BrowserStack username
BROWSERSTACK_ACCESS_KEY — your access key

If not set, inform the user how to get them from browserstack.com/accounts/settings and stop.

Capabilities
1. Configure for BrowserStack
/pw:browserstack setup


Steps:

Check current playwright.config.ts
Add BrowserStack connect options:
// Add to playwright.config.ts
import { defineConfig } from '@playwright/test';

const isBS = !!process.env.BROWSERSTACK_USERNAME;

export default defineConfig({
  // ... existing config
  projects: isBS ? [
    {
      name: "chromelatestwindows-11",
      use: {
        connectOptions: {
          wsEndpoint: `wss://cdp.browserstack.com/playwright?caps=${encodeURIComponent(JSON.stringify({
            'browser': 'chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '11',
            'browserstack.username': process.env.BROWSERSTACK_USERNAME,
            'browserstack.accessKey': process.env.BROWSERSTACK_ACCESS_KEY,
          }))}`,
        },
      },
    },
    {
      name: "firefoxlatestwindows-11",
      use: {
        connectOptions: {
          wsEndpoint: `wss://cdp.browserstack.com/playwright?caps=${encodeURIComponent(JSON.stringify({
            'browser': 'playwright-firefox',
            'browser_version': 'latest',
            'os': 'Windows',
            'os_version': '11',
            'browserstack.username': process.env.BROWSERSTACK_USERNAME,
            'browserstack.accessKey': process.env.BROWSERSTACK_ACCESS_KEY,
          }))}`,
        },
      },
    },
    {
      name: "webkitlatestos-x-ventura",
      use: {
        connectOptions: {
          wsEndpoint: `wss://cdp.browserstack.com/playwright?caps=${encodeURIComponent(JSON.stringify({
            'browser': 'playwright-webkit',
            'browser_version': 'latest',
            'os': 'OS X',
            'os_version': 'Ventura',
            'browserstack.username': process.env.BROWSERSTACK_USERNAME,
            'browserstack.accessKey': process.env.BROWSERSTACK_ACCESS_KEY,
          }))}`,
        },
      },
    },
  ] : [
    // ... local projects fallback
  ],
});

Add npm script: "test:e2e:cloud": "npx playwright test --project='chrome@*' --project='firefox@*' --project='webkit@*'"
2. Run Tests on BrowserStack
/pw:browserstack run


Steps:

Verify credentials are set
Run tests with BrowserStack projects:
BROWSERSTACK_USERNAME=$BROWSERSTACK_USERNAME \
BROWSERSTACK_ACCESS_KEY=$BROWSERSTACK_ACCESS_KEY \
npx playwright test --project='chrome@*' --project='firefox@*'

Monitor execution
Report results per browser
3. Get Build Results
/pw:browserstack results


Steps:

Call browserstack_get_builds MCP tool
Get latest build's sessions
For each session:
Status (pass/fail)
Browser and OS
Duration
Video URL
Log URLs
Format as summary table
4. Check Available Browsers
/pw:browserstack browsers


Steps:

Call browserstack_get_browsers MCP tool
Filter for Playwright-compatible browsers
Display available browser/OS combinations
5. Local Testing
/pw:browserstack local


For testing localhost or staging behind firewall:

Install BrowserStack Local: npm install -D browserstack-local
Add local tunnel to config
Provide setup instructions
MCP Tools Used
Tool	When
browserstack_get_plan	Check account limits
browserstack_get_browsers	List available browsers
browserstack_get_builds	List recent builds
browserstack_get_sessions	Get sessions in a build
browserstack_get_session	Get session details (video, logs)
browserstack_update_session	Mark pass/fail
browserstack_get_logs	Get text/network logs
Output
Cross-browser test results table
Per-browser pass/fail status
Links to BrowserStack dashboard for video/screenshots
Any browser-specific failures highlighted
Weekly Installs
994
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn