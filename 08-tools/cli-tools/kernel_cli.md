---
rating: ⭐⭐⭐
title: kernel-cli
url: https://skills.sh/kernel/skills/kernel-cli
---

# kernel-cli

skills/kernel/skills/kernel-cli
kernel-cli
Installation
$ npx skills add https://github.com/kernel/skills --skill kernel-cli
SKILL.md
Kernel CLI

The Kernel CLI provides command-line access to Kernel's cloud browser platform for browser automation, serverless app deployment, and infrastructure management.

Installation
Homebrew: brew install kernel/tap/kernel (>=v0.13.4)
npm: npm install -g @onkernel/cli (>=v0.13.4)
Authentication
Preferred: Set KERNEL_API_KEY environment variable
Fallback: Run kernel login for interactive OAuth
Quick Start
# Authenticate
export KERNEL_API_KEY=your_api_key

# Create a browser session
kernel browsers create

# Run Playwright automation
kernel browsers playwright execute <session_id> 'await page.goto("https://example.com")'

# Take a screenshot
kernel browsers computer screenshot <session_id> --to screenshot.png

# Cleanup
kernel browsers delete <session_id> --yes

References
Browser Management - Create, list, view, and delete browser sessions
App Deployment - Deploy TypeScript/Python apps and invoke actions
Computer Controls - OS-level mouse, keyboard, and screenshot capabilities
Process Execution - Execute and manage processes in browser VMs
Profiles - Manage persistent browser profiles
Managed Auth - Auth connections, login sessions, credential providers, auto re-authentication
Proxies - Create and manage datacenter, ISP, residential, and mobile proxies
Browser Pools - Manage pre-warmed browser pools
Extensions - Upload and manage Chrome extensions
Replays - Record and download video replays
Filesystem Operations - Read, write, upload, and download files
Weekly Installs
289
Repository
kernel/skills
GitHub Stars
3
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn