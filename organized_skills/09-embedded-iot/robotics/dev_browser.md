---
rating: ⭐⭐
title: dev-browser
url: https://skills.sh/sawyerhood/dev-browser/dev-browser
---

# dev-browser

skills/sawyerhood/dev-browser/dev-browser
dev-browser
Installation
$ npx skills add https://github.com/sawyerhood/dev-browser --skill dev-browser
Summary

Browser automation with persistent page state across sequential scripts.

Two modes: standalone Chromium (default) or extension mode connecting to user's existing Chrome browser with authentication already in place
Discover page elements via ARIA snapshot accessibility tree, then interact using element references; alternatively read source code to write direct selectors
Small, focused scripts that run incrementally—each script does one action (navigate, click, fill, check), then you evaluate state and decide next steps
Built on Playwright Page API with helpers for waiting (page load, selectors, URLs), screenshots, and error recovery through persistent page state
SKILL.md
Dev Browser

A CLI for controlling browsers with sandboxed JavaScript scripts.

Installation
npm install -g dev-browser
dev-browser install

Usage

Run dev-browser --help to learn more.

Weekly Installs
1.8K
Repository
sawyerhood/dev-browser
GitHub Stars
6.0K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail