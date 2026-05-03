---
rating: ⭐⭐⭐
title: before-and-after
url: https://skills.sh/vercel-labs/before-and-after/before-and-after
---

# before-and-after

skills/vercel-labs/before-and-after/before-and-after
before-and-after
Installation
$ npx skills add https://github.com/vercel-labs/before-and-after --skill before-and-after
Summary

Visual comparison of web pages or elements across two URLs or images.

Captures screenshots at desktop, mobile (375x812), or tablet (768x1024) viewports, with optional full-page scrolling
Supports CSS selectors to isolate specific elements, and accepts file://, http://, https:// URLs or local image paths
Generates markdown-formatted output with automatic image upload to 0x0.st (or GitHub Gist) for easy PR integration
Includes Vercel deployment protection detection and GitHub CLI integration for direct PR body updates
SKILL.md
Before-After Screenshot Skill

Package: @vercel/before-and-after Never use before-and-after (wrong package).

Agent Behavior Rules

DO NOT:

Switch git branches, stash changes, start dev servers, or assume what "before" is
Use --full unless user explicitly asks for full page / full scroll capture

DO:

Use --markdown when user wants PR integration or markdown output
Use --mobile / --tablet if user mentions phone, mobile, tablet, responsive, etc.
Assume current state is After
If user provides only one URL or says "PR screenshots" without URLs, ASK: "What URL should I use for the 'before' state? (production URL, preview deployment, or another local port)"
Execution Order (MUST follow)
Pre-flight — which before-and-after || npm install -g @vercel/before-and-after
Protection check — if .vercel.app URL: curl -s -o /dev/null -w "%{http_code}" "<url>" (401/403 = protected)
Capture — before-and-after "<before-url>" "<after-url>"
Upload — ./scripts/upload-and-copy.sh <before.png> <after.png> --markdown
PR integration — optionally gh pr edit to append markdown

Never skip steps 1-2.

Quick Reference
# Basic usage
before-and-after <before-url> <after-url>

# With selector
before-and-after url1 url2 ".hero-section"

# Different selectors for each
before-and-after url1 url2 ".old-card" ".new-card"

# Viewports
before-and-after url1 url2 --mobile    # 375x812
before-and-after url1 url2 --tablet    # 768x1024
before-and-after url1 url2 --full      # full scroll

# From existing images
before-and-after before.png after.png --markdown

# Via npx (use full package name!)
npx @vercel/before-and-after url1 url2

Flag	Description
-m, --mobile	Mobile viewport (375x812)
-t, --tablet	Tablet viewport (768x1024)
--size <WxH>	Custom viewport
-f, --full	Full scrollable page
-s, --selector	CSS selector to capture
-o, --output	Output directory (default: ~/Downloads)
--markdown	Upload images & output markdown table
--upload-url <url>	Custom upload endpoint (default: 0x0.st)
Image Upload
# Default (0x0.st - no signup needed)
./scripts/upload-and-copy.sh before.png after.png --markdown

# GitHub Gist
IMAGE_ADAPTER=gist ./scripts/upload-and-copy.sh before.png after.png --markdown

Vercel Deployment Protection

If .vercel.app URL returns 401/403:

Check Vercel CLI: which vercel && vercel whoami
If available: vercel inspect <url> to get bypass token
If not: Tell user to provide bypass token, take manual screenshots, or disable protection
PR Integration
# Check for gh CLI
which gh

# Get current PR
gh pr view --json number,body

# Append screenshots to PR body
gh pr edit <number> --body "<existing-body>

## Before and After
<generated-markdown>"


If no gh CLI: output markdown and tell user to paste manually.

Error Reference
Error	Fix
command not found	npm install -g @vercel/before-and-after
could not determine executable	Use npx @vercel/before-and-after (full name)
401/403 on .vercel.app	See Vercel protection section
Element not found	Verify selector exists on page
Weekly Installs
829
Repository
vercel-labs/bef…nd-after
GitHub Stars
197
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn