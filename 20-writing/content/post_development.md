---
title: post-development
url: https://skills.sh/mwguerra/claude-code-plugins/post-development
---

# post-development

skills/mwguerra/claude-code-plugins/post-development
post-development
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill post-development
SKILL.md
Post-Development Skill

This skill enables comprehensive post-development preparation for app launches, including marketing materials, SEO, and content generation.

When to Use

Use this skill when:

Preparing an application for launch
Creating marketing materials for an app
Generating SEO data for public pages
Creating personas and marketing strategies
Generating social media ads
Writing showcase articles
Designing landing pages
Capabilities
1. Project Analysis
Detect project type and tech stack
Discover public routes
Extract product information from docs
2. SEO Analysis (/post-development:seo)
Generate meta tags for all pages
Create keyword strategies
Produce Open Graph specifications
Generate sitemap
3. Screenshot Capture (/post-development:screenshots)
Capture all public pages
Multiple viewports (desktop, tablet, mobile)
Light and dark mode
Focus on key sections
4. Persona Creation (/post-development:personas)
Create detailed buyer personas
Develop marketing strategies
Generate CTAs for all channels
5. Ad Generation (/post-development:ads)
Instagram, Facebook, LinkedIn, Twitter
Multiple ad formats per platform
A/B variations
6. Article Writing (/post-development:articles)
3 showcase articles
Different angles (story, tutorial, case study)
SEO optimized
7. Landing Pages (/post-development:landing)
Persona-specific designs
All sections specified
Copy and image recommendations
Usage
Initialize
/post-development:run init --base-url http://localhost:3000

Run All Tasks
/post-development:run run

Run Specific Task
/post-development:run run --task seo

Check Status
/post-development:run status

Output Directory Structure
.post-development/
├── post-development.json     # Master plan
├── seo/
│   ├── pages/               # SEO data per page
│   └── assets/              # Favicon, OG image specs
├── screenshots/
│   ├── desktop/
│   ├── tablet/
│   └── mobile/
├── personas/
│   ├── personas/            # Individual persona files
│   ├── strategies/          # Marketing strategies
│   └── cta/                 # CTA collections
├── ads/
│   ├── instagram/
│   ├── facebook/
│   ├── linkedin/
│   └── twitter/
├── articles/
│   ├── article-1/
│   ├── article-2/
│   └── article-3/
└── landing-pages/
    └── [persona-name]/

Task Dependencies

Tasks run in dependency order:

seo → no dependencies
screenshots → no dependencies
personas → depends on seo
ads → depends on personas, screenshots
articles → depends on personas, screenshots
landing → depends on personas, screenshots, articles
Requirements
For screenshots: Playwright installed (npm install -D playwright)
For screenshots: App running at baseUrl
For articles: Screenshots completed first
For landing pages: All prior tasks completed
Example Workflow
# 1. Initialize project
/post-development:run init --base-url http://localhost:3000

# 2. Run everything
/post-development:run run

# 3. Or run tasks individually
/post-development:run seo
/post-development:run screenshots
/post-development:run personas
/post-development:run ads
/post-development:run articles
/post-development:run landing

# 4. Check progress anytime
/post-development:run status

Weekly Installs
20
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn