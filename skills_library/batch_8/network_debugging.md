---
title: network-debugging
url: https://skills.sh/aj-geddes/useful-ai-prompts/network-debugging
---

# network-debugging

skills/aj-geddes/useful-ai-prompts/network-debugging
network-debugging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill network-debugging
SKILL.md
Network Debugging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Network debugging identifies connectivity issues, latency problems, and data transmission errors that impact application performance.

When to Use
Slow loading times
Failed requests
Intermittent connectivity
CORS errors
SSL/TLS issues
API communication problems
Quick Start

Minimal working example:

Chrome DevTools Network Tab:

Columns:
  - Name: Request file/endpoint
  - Status: HTTP status code
  - Type: Resource type (xhr, fetch, etc)
  - Initiator: What triggered request
  - Size: Resource size / transferred size
  - Time: Total time to complete
  - Waterfall: Timeline visualization

Timeline Breakdown:
  - Queueing: Waiting in queue
  - DNS: Domain name resolution
  - Initial connection: TCP handshake
  - SSL: SSL/TLS negotiation
  - Request sent: Time to send request
  - Waiting (TTFB): Time to first byte
  - Content Download: Receiving response

---
Network Conditions:

Throttling Presets:
  - Fast 3G: 1.6 Mbps down, 750 Kbps up
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Browser Network Tools	Browser Network Tools
Common Network Issues	Common Network Issues
Debugging Tools & Techniques	Debugging Tools & Techniques
Checklist	Checklist
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
332
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail