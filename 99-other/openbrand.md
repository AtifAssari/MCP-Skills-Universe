---
title: openbrand
url: https://skills.sh/ethanjyx/openbrand/openbrand
---

# openbrand

skills/ethanjyx/openbrand/openbrand
openbrand
Installation
$ npx skills add https://github.com/ethanjyx/openbrand --skill openbrand
SKILL.md
OpenBrand

Extract brand assets from any website URL — logos, colors, backdrop images, and brand name.

Setup
MCP Server (recommended for Claude Code / Cursor)
claude mcp add --transport stdio \
  --env OPENBRAND_API_KEY=your_api_key \
  openbrand -- npx -y openbrand-mcp


Get your free API key at openbrand.sh/dashboard.

Once configured, use the extract_brand_assets tool with a URL to get structured brand data.

npm package (no API key needed)
npm add openbrand

import { extractBrandAssets } from "openbrand";

const result = await extractBrandAssets("https://stripe.com");
if (result.ok) {
  // result.data.brand_name → "Stripe"
  // result.data.logos → LogoAsset[]
  // result.data.colors → ColorAsset[]
  // result.data.backdrop_images → BackdropAsset[]
}

API
curl "https://openbrand.sh/api/extract?url=https://stripe.com" \
  -H "Authorization: Bearer your_api_key"

What it extracts
Asset	Sources
Logos	Favicons, apple-touch-icons, header/nav logos, inline SVGs (with dimension probing)
Brand colors	theme-color meta tags, manifest.json, dominant colors from logo imagery
Backdrop images	og:image, CSS backgrounds, hero/banner images
Brand name	og:site_name, application-name, logo alt text, page title
Response format
{
  "brandName": "Stripe",
  "logos": [
    { "url": "https://...", "type": "favicon", "resolution": { "width": 32, "height": 32, "aspect_ratio": 1 } }
  ],
  "colors": [
    { "hex": "#635bff", "usage": "primary" },
    { "hex": "#0a2540", "usage": "secondary" }
  ],
  "backdrops": [
    { "url": "https://...", "description": "Hero image" }
  ]
}

When to use this skill
Building a landing page or UI that matches a client's brand
Generating brand style guides or design tokens
Creating branded email templates or marketing materials
Populating brand fields in a CMS or design tool
Any task where you need logos, colors, or imagery from a website
Weekly Installs
59
Repository
ethanjyx/openbrand
GitHub Stars
732
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn