---
title: ez-ui
url: https://skills.sh/araa47/ez-ha/ez-ui
---

# ez-ui

skills/araa47/ez-ha/ez-ui
ez-ui
Installation
$ npx skills add https://github.com/araa47/ez-ha --skill ez-ui
SKILL.md
ez-ui — Home Assistant Web UI Access
Local access

Home Assistant UI is available at:

http://<HA_HOST>:8123


From inside the ez-ha addon container, use:

http://homeassistant:8123


The HA_URL env var is set automatically inside the addon.

Authentication

API requests use HA_TOKEN (set automatically inside the addon).

For browser-based access, run browser-login (see scripts/browser-login.mjs) to authenticate the browser session:

browser-login                   # Uses HA_BROWSER_USER / HA_BROWSER_PASS from addon config
browser-login <user> <pass>     # Or pass credentials explicitly


The session is persisted in /data/browser-profile/state.json and can be loaded by Playwright:

const context = await browser.newContext({
    storageState: "/data/browser-profile/state.json"
});


Tip: Create a dedicated HA user without 2FA for the agent.

Browser testing with Playwright

browser-login uses Playwright under the hood. Playwright pierces shadow DOM automatically via role-based selectors, which is far more reliable than manual shadow DOM traversal.

# Take a screenshot of a dashboard
npx playwright screenshot http://homeassistant:8123/lovelace/0 dashboard.png

# Use Playwright in a Node.js script
node -e '
const { chromium } = require("playwright");
(async () => {
    const browser = await chromium.launch({
        executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
        headless: true, args: ["--no-sandbox"]
    });
    const context = await browser.newContext({
        storageState: "/data/browser-profile/state.json"
    });
    const page = await context.newPage();
    await page.goto("http://homeassistant:8123/lovelace/0");
    await page.screenshot({ path: "dashboard.png" });
    await browser.close();
})();
'

Key UI paths
Path	Description
/lovelace/	Default dashboard
/config/	Settings & configuration panel
/config/automation/	Automation editor
/config/script/	Script editor
/config/scene/	Scene editor
/developer-tools/	Developer tools (services, states, templates)
/developer-tools/state	Entity state browser
/developer-tools/service	Service call tester
/developer-tools/template	Jinja2 template tester
/history/	History graphs
/logbook/	Logbook
/map/	Map view
Weekly Installs
10
Repository
araa47/ez-ha
GitHub Stars
3
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail