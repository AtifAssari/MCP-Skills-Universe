---
title: nebula-scrape-url
url: https://skills.sh/acquia/nebula/nebula-scrape-url
---

# nebula-scrape-url

skills/acquia/nebula/nebula-scrape-url
nebula-scrape-url
Installation
$ npx skills add https://github.com/acquia/nebula --skill nebula-scrape-url
SKILL.md
Scraping URLs for design reference

This applies to web page URLs only. Do not use this for:

Figma URLs (use the Figma MCP instead)
GitHub URLs (read the code directly)
Documentation URLs (read or search as needed)
Workflow

Run the scraper to capture screenshots and HTML:

node scripts/scrape-page.js <url>


Review the output in scraped/<timestamp>/:

screenshot-desktop.png - Desktop layout reference
screenshot-tablet.png - Tablet layout reference
screenshot-mobile.png - Mobile layout reference
page.html - Full HTML for structure reference

Use the screenshots to understand the visual design (layout, spacing, colors, typography).

Use the HTML to understand the content structure and hierarchy.

Build the components using the nebula-component-creation skill.

Example

User prompt: "Build me this page: https://example.com/pricing"

Run: node scripts/scrape-page.js https://example.com/pricing
Review the screenshots to understand the layout
Review the HTML to understand the structure
Create components that match the design using Tailwind CSS
Weekly Installs
10
Repository
acquia/nebula
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn