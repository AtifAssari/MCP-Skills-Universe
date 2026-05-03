---
title: convert-url-html-to-md
url: https://skills.sh/1naichii/ai-code-tools/convert-url-html-to-md
---

# convert-url-html-to-md

skills/1naichii/ai-code-tools/convert-url-html-to-md
convert-url-html-to-md
Installation
$ npx skills add https://github.com/1naichii/ai-code-tools --skill convert-url-html-to-md
SKILL.md
Convert URL HTML to Markdown

Extract web content as markdown using a two-phase approach for comprehensive documentation gathering.

Two-Phase Workflow

For optimal documentation extraction:

Discovery (clean=false): Get full page including navigation and sidebars to discover all documentation URLs
Extraction (clean=true): Extract main content from discovered URLs
Usage
# From the skill directory
cd ~/.claude/skills/convert-url-html-to-md

# Clean mode - main content only (recommended for docs)
node scripts/convert_url.js <url> --clean=true

# Full page mode - includes nav/sidebar (for discovering URLs)
node scripts/convert_url.js <url> --clean=false

# Default is clean=true
node scripts/convert_url.js <url>

Examples
# Get all navigation links from a docs site
node scripts/convert_url.js https://ui.shadcn.com/docs --clean=false

# Extract specific documentation content
node scripts/convert_url.js https://ui.shadcn.com/docs/components/radix/aspect-ratio --clean=true

Installation

Dependencies are included. Run once:

cd ~/.claude/skills/convert-url-html-to-md
npm install

Output

The script outputs markdown directly to stdout. Redirect to file if needed:

node scripts/convert_url.js <url> --clean=true > output.md

Credits

This skill is based on urltomarkdown by Lee Hanken, licensed under MIT. Modified and adapted as a Claude skill by 1naichii.

Weekly Installs
39
Repository
1naichii/ai-code-tools
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn