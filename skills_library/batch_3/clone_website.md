---
title: clone-website
url: https://skills.sh/julianromli/ai-skills/clone-website
---

# clone-website

skills/julianromli/ai-skills/clone-website
clone-website
Installation
$ npx skills add https://github.com/julianromli/ai-skills --skill clone-website
Summary

Transform any website into production-ready Next.js 16 code using Firecrawl.

Scrapes target websites and extracts HTML/markdown, with fallback crawling if initial scrape fails
Mandatory analysis phase presents detected sections, design tokens, images, and file structure to user before code generation
Generates complete Next.js 16 projects with TypeScript, Tailwind CSS v4, Shadcn UI components, and Lucide icons
Supports partial cloning by section (hero, pricing, footer) or full-page replication with automatic image download and Unsplash fallbacks
Mobile-first responsive design using Tailwind arbitrary values and CSS variables for design token consistency
SKILL.md
Clone Website Skill

Transform any website into production-ready Next.js 16 code using Firecrawl MCP.

Workflow

Execute these 3 phases in order. Never skip Phase 2.

Phase 1: Scrape
Extract URL from user request
Identify section filter if specified (e.g., "hero only", "just the pricing")
Scrape using Firecrawl:
firecrawl-mcp___firecrawl_scrape:
  url: [TARGET_URL]
  formats: ["markdown", "html"]
  onlyMainContent: true

If scrape fails, fallback to firecrawl-mcp___firecrawl_crawl
Phase 2: Analysis (MANDATORY)

STOP. Present analysis to user before ANY code generation.

Read references/analysis-template.md and fill out the template with:

Detected sections and component breakdown
Extracted design tokens (colors, typography, spacing)
Image inventory with download/fallback status
Proposed file structure

Ask user: "Ready to proceed? (y/n or request modifications)"

Do not generate code until user confirms.

Phase 3: Code Generation

After user confirmation, generate files in this order:

app/globals.css - Design tokens as CSS variables
app/layout.tsx - Root layout with SEO metadata
components/landing/[Section].tsx - Each component
app/page.tsx - Main page composing components
Download images to public/images/

Reference references/tech-stack.md for Next.js 16 conventions. Reference references/component-patterns.md for component structure.

Tech Stack (Fixed)
Layer	Technology
Framework	Next.js 16 (App Router)
Language	TypeScript (strict)
Styling	Tailwind CSS v4
Components	Shadcn UI
Icons	Lucide React
Font	Geist Sans (default) or extracted
Image Handling
Extract all image URLs from scraped content
Attempt download via fetch
On failure, use Unsplash fallback:
Hero: https://images.unsplash.com/photo-[id]?w=1920&h=1080
Avatars: https://images.unsplash.com/photo-[id]?w=100&h=100
Features: Prefer Lucide icons over images
Save to public/images/ with descriptive kebab-case names
Partial Cloning

Parse user request for section filters:

Request	Action
"clone the hero from X"	Generate only Hero.tsx
"clone pricing and footer"	Generate Pricing.tsx + Footer.tsx
"clone X" (no filter)	Full page clone
Code Standards
Mobile-first responsive design
Use Tailwind arbitrary values for pixel-perfection: w-[347px]
Extract repeated colors to CSS variables
Use cn() utility for conditional classes
Add brief comments only for non-obvious patterns
Prefer gap-* over margins for flex/grid spacing
Use size-* over w-* h-* when values match
Weekly Installs
727
Repository
julianromli/ai-skills
GitHub Stars
155
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn