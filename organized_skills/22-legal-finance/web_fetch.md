---
rating: ⭐⭐⭐
title: web-fetch
url: https://skills.sh/0xbigboss/claude-code/web-fetch
---

# web-fetch

skills/0xbigboss/claude-code/web-fetch
web-fetch
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill web-fetch
Summary

Fetch web content as clean markdown using markdown-native endpoints, selector-based HTML extraction, or bundled fallback parsing.

Prioritizes markdown-native responses (content-type: text/markdown) before falling back to HTML extraction
Includes pre-configured selectors for common documentation sites (Anthropic, MDN, GitHub) and a generic fallback for article/main content regions
Provides html2markdown with CSS selector support for fine-grained content isolation, excluding navigation, headers, footers, and scripts
Bundles a Bun-based fallback parser for sites where selector-based extraction fails or produces poor output
Requires curl, html2markdown, and bun; includes troubleshooting guidance for markdown detection, selector testing, and client-rendered content limitations
SKILL.md
Web Content Fetching

Fetch web content in this order:

Prefer markdown-native endpoints (content-type: text/markdown)
Use selector-based HTML extraction for known sites
Use the bundled Bun fallback script when selectors fail
Prerequisites

Verify required tools before extracting:

command -v curl >/dev/null || echo "curl is required"
command -v html2markdown >/dev/null || echo "html2markdown is required for HTML extraction"
command -v bun >/dev/null || echo "bun is required for fetch.ts fallback"


Install Bun dependencies for the bundled script:

cd ~/.claude/skills/web-fetch && bun install

Default Workflow

Use this as the default flow for any URL:

URL="<url>"
CONTENT_TYPE="$(curl -sIL "$URL" | awk -F': ' 'tolower($1)=="content-type"{print tolower($2)}' | tr -d '\r' | tail -1)"

if echo "$CONTENT_TYPE" | grep -q "markdown"; then
  curl -sL "$URL"
else
  curl -sL "$URL" \
    | html2markdown \
        --include-selector "article,main,[role=main]" \
        --exclude-selector "nav,header,footer,script,style"
fi

Known Site Selectors
Site	Include Selector	Exclude Selector
platform.claude.com	#content-container	-
docs.anthropic.com	#content-container	-
developer.mozilla.org	article	-
github.com (docs)	article	nav,.sidebar
Generic	article,main,[role=main]	nav,header,footer,script,style

Example:

curl -sL "<url>" \
  | html2markdown \
      --include-selector "#content-container" \
      --exclude-selector "nav,header,footer"

Finding the Right Selector

When a site isn't in the patterns list:

# Check what content containers exist
curl -s "<url>" | grep -o '<article[^>]*>\|<main[^>]*>\|id="[^"]*content[^"]*"' | head -10

# Test a selector
curl -sL "<url>" | html2markdown --include-selector "<selector>" | head -30

# Check line count
curl -sL "<url>" | html2markdown --include-selector "<selector>" | wc -l

Universal Fallback Script

When selectors produce poor output, run the bundled parser:

bun ~/.claude/skills/web-fetch/fetch.ts "<url>"


If already in the skill directory:

bun fetch.ts "<url>"

Options Reference
--include-selector "CSS"  # Keep only matching elements
--exclude-selector "CSS"  # Remove matching elements
--domain "https://..."    # Convert relative links to absolute

Troubleshooting

Empty output with selectors: The page might be markdown-native. Check headers first:

curl -sIL "<url>" | grep -i '^content-type:'


Wrong content selected: The site may have multiple article/main regions:

curl -s "<url>" | grep -o '<article[^>]*>'


html2markdown not found: Install it, then retry selector-based extraction.

bun or script deps missing: Run cd ~/.claude/skills/web-fetch && bun install.

Missing code blocks: Check if the site uses non-standard code formatting.

Client-rendered content: If HTML only has "Loading..." placeholders, the content is JS-rendered. Neither curl nor the Bun script can extract it; use browser-based tools.

Weekly Installs
739
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn