---
title: defuddle
url: https://skills.sh/kepano/obsidian-skills/defuddle
---

# defuddle

skills/kepano/obsidian-skills/defuddle
defuddle
Installation
$ npx skills add https://github.com/kepano/obsidian-skills --skill defuddle
Summary

Extract clean markdown from web pages, removing clutter and navigation to minimize token usage.

Converts web page content to readable markdown using the --md flag, stripping ads, navigation, and boilerplate
Supports output to file with -o flag and extraction of specific metadata properties (title, description, domain) via -p
Offers multiple output formats: markdown, JSON with both HTML and markdown versions, or raw HTML
Preferred alternative to WebFetch for standard web pages, documentation, articles, and blog posts where token efficiency matters
SKILL.md
Defuddle

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: npm install -g defuddle

Usage

Always use --md for markdown output:

defuddle parse <url> --md


Save to file:

defuddle parse <url> --md -o content.md


Extract specific metadata:

defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain

Output formats
Flag	Format
--md	Markdown (default choice)
--json	JSON with both HTML and markdown
(none)	HTML
-p <name>	Specific metadata property
Weekly Installs
16.7K
Repository
kepano/obsidian-skills
GitHub Stars
28.1K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn