---
rating: ⭐⭐
title: extract-project-logo
url: https://skills.sh/tradingstrategy-ai/web3-ethereum-defi/extract-project-logo
---

# extract-project-logo

skills/tradingstrategy-ai/web3-ethereum-defi/extract-project-logo
extract-project-logo
Installation
$ npx skills add https://github.com/tradingstrategy-ai/web3-ethereum-defi --skill extract-project-logo
SKILL.md
Extract project logo

This skill extracts a project's official logo from its website or related sources, prioritising high-quality vector formats and official brand assets.

Required inputs

Before starting, gather the following from the user:

Website URL - The project's main website (e.g., https://example.com)
Save path - Local filesystem path where the logo should be saved (e.g., ./logos/example-logo.svg)
Format preference (optional) - Preferred format: SVG (recommended), PNG, or any

If any required input is missing, ask the user before proceeding.

Save all project logos in the target folder. We will pick variants and post-process those later.

There is no universal standard how artist name their logo files for dark and light variants. In our case, we always say

light: light (white) text on dark or transparent background
dark: dark (black) text on white or transparent background

Following vocabulary is used:

Brand mark: same as logo mark, the logo without the brand name text
Word mark: the logo with the brand name text
Step 1: Search for brand kit or media resources

The highest quality logos are typically found in official brand/media kits. Search for these pages:

Navigate to the website and look for links in the footer or header:

"Brand", "Brand Kit", "Brand Assets", "Brand Guidelines"
"Media", "Media Kit", "Press", "Press Kit"
"Resources", "Downloads", "Assets"

Try common URL patterns:

{base_url}/brand
{base_url}/brand-kit
{base_url}/media
{base_url}/press
{base_url}/assets
{base_url}/resources

If a brand kit is found:

Look for downloadable logo packages (often ZIP files)
Prefer SVG or vector formats over raster images
Choose the most square logo variant if multiple options exist
If both light and dark themes are present, get both
If colourful option exist, get it as well

If a brand kit is found with suitable logos, proceed to Step 5.

Step 2: Check GitHub repository

Many projects host their logos in their GitHub repositories:

Find the project's GitHub repository (often linked in website footer/header)

Search these common locations:

/assets/ or /images/ directories
/branding/ or /brand/ directories
/public/ directory (for web apps)
/docs/ or /documentation/ directories
Root directory (README badges, logo files)

Check the README.md for embedded logos:

Look for <img> tags or markdown image syntax
These often point to high-quality logo files

Search for files named:

logo.svg, logo.png, logo-*.svg
{project-name}.svg, {project-name}-logo.*
brand.*, icon.*

If a suitable logo is found, proceed to Step 4.

Step 3: Extract from website directly

If no brand kit or GitHub assets are available, extract the logo from the website:

Option A: Using MCP Playwright (recommended for dynamic sites)

Use the MCP Playwright tool to:

Navigate to the homepage

Look for logo elements in the header (typically top-left):

Search for <img> tags with class/id containing "logo"
Check for <svg> elements in the header
Look for elements with role="img" and logo-related aria labels

Extract the image source URL or SVG content

Option B: Check meta tags and favicon

Open Graph image - Check for <meta property="og:image"> tag

Often a high-quality image suitable for social sharing
May include branding elements

Favicon - Check for high-resolution favicon:

<link rel="icon" type="image/svg+xml"> (best - vector)
<link rel="apple-touch-icon"> (usually 180x180 PNG)
/favicon.ico (low resolution, last resort)

Twitter Card image - Check <meta name="twitter:image">

Step 4: Extract from Twitter

Get the project logo from their Twitter (also known as X.com) avatar image.

Step 5: Extract from Coingecko

Get the project logo from their Coingecko.

Step 6: Download and save

For SVG files:

Download the raw SVG content
Ensure the file is valid XML
Save with .svg extension

For raster images (PNG, etc.):

Download the highest resolution available
Verify file integrity after download
Save with appropriate extension

Verify the saved file:

Open the file to confirm it displays correctly
Check file size is reasonable (not 0 bytes or corrupted)
Download methods

Using curl:

curl -o "{save_path}" "{logo_url}"


Using Python:

import requests

response = requests.get("{logo_url}")
with open("{save_path}", "wb") as f:
    f.write(response.content)


For SVG content extracted directly:

with open("{save_path}", "w") as f:
    f.write(svg_content)

Step 7: Report results to user

Provide the user with:

Source location - Where the logo was found (brand kit URL, GitHub path, etc.)
File details - Format, dimensions (for raster), file size
Saved path - Confirm where the file was saved
Alternative versions - Note if other variants are available (dark mode, icon-only, etc.)
Step 8: Save the report as Markdown file next to the logos
Create a Markdown file in the folder where logos where saved
Include the same information as for the user report
Include links to the web pages, brand pages and brand kits used
Troubleshooting
No logo found

If no suitable logo can be found:

Check if the project uses a different primary domain
Look for the project on social media (Twitter/X, LinkedIn) - profile images are often logos
Search "[project name] logo" on image search engines
Check DeFiLlama, CoinGecko, or similar aggregators for crypto projects
Ask the user if they have alternative sources or contacts
Dynamic/JavaScript-rendered logos

If the logo is rendered via JavaScript:

Use MCP Playwright to load the page fully
Wait for dynamic content to render
Extract from the rendered DOM
Logo requires authentication

If brand assets are behind a login:

Inform the user
Provide the URL to the brand kit page
Ask the user to download manually or provide credentials (if appropriate)
Weekly Installs
63
Repository
tradingstrategy…eum-defi
GitHub Stars
806
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn