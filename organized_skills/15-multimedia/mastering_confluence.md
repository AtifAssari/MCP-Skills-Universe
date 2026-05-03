---
rating: ⭐⭐⭐
title: mastering-confluence
url: https://skills.sh/spillwavesolutions/mastering-confluence-agent-skill/mastering-confluence
---

# mastering-confluence

skills/spillwavesolutions/mastering-confluence-agent-skill/mastering-confluence
mastering-confluence
Installation
$ npx skills add https://github.com/spillwavesolutions/mastering-confluence-agent-skill --skill mastering-confluence
SKILL.md
Confluence Management Skill

Type: Project | Version: 2.2.0

Manage Confluence documentation: download pages to Markdown, upload with images, convert between formats, integrate diagrams, search with CQL.

Contents
Critical Constraints
Quick Start
Core Capabilities
Checklists
Reference Documentation
Scripts
Critical Constraints

DO NOT USE MCP FOR PAGE UPLOADS - Size limits apply (~10-20KB max)

# Use REST API scripts instead:
python3 scripts/upload_confluence_v2.py document.md --id PAGE_ID


MCP tools are fine for reading pages but fail for uploading large content.

Quick Start
Upload Markdown to Confluence
# Update existing page
python3 scripts/upload_confluence_v2.py document.md --id 780369923

# Create new page
python3 scripts/upload_confluence_v2.py document.md --space DEV --parent-id 123456

# Preview first (recommended)
python3 scripts/upload_confluence_v2.py document.md --id 780369923 --dry-run

Download Confluence to Markdown
# Single page
python3 scripts/download_confluence.py 123456789

# With child pages
python3 scripts/download_confluence.py --download-children 123456789

# Multiple pages
python3 scripts/download_confluence.py 123456 456789 789012

Convert Markdown to Wiki Markup
python3 scripts/convert_markdown_to_wiki.py input.md output.wiki

Search Confluence (via MCP)
mcp__atlassian__confluence_search({
  query: 'space = "DEV" AND text ~ "API" AND created >= startOfYear()'
})

Core Capabilities
Capability	Tool/Script	Reference
Upload pages with images	upload_confluence_v2.py	upload_guide
Download pages to Markdown	download_confluence.py	download_guide
Convert Markdown ↔ Wiki	convert_markdown_to_wiki.py	conversion_guide
Search pages (CQL)	MCP confluence_search	cql_reference
Wiki Markup syntax	-	wiki_markup_guide
Render Mermaid diagrams	render_mermaid.py	image_handling
Git-to-Confluence sync	mark CLI	mark_tool_guide
Troubleshooting	-	troubleshooting_guide
Checklists
Upload Checklist

Copy and track progress:

Upload Progress:
- [ ] Diagrams converted to PNG/SVG (if Mermaid/PlantUML present)
- [ ] All images use markdown syntax: ![alt](path)
- [ ] No raw Confluence XML in markdown
- [ ] All image files verified to exist
- [ ] Dry-run tested: `--dry-run`
- [ ] Upload executed with v2 script (not MCP)
- [ ] Page URL verified accessible

Download Checklist
Download Progress:
- [ ] Page ID obtained from Confluence URL
- [ ] Credentials configured in .env file
- [ ] Output directory specified
- [ ] --download-children flag set (if hierarchy needed)
- [ ] Download completed successfully
- [ ] Attachments downloaded to {Page}_attachments/
- [ ] Frontmatter contains correct metadata

Image Handling

Standard Workflow:

Convert diagrams (if Mermaid/PlantUML):

# Mermaid
mmdc -i diagram.mmd -o diagram.png -b transparent

# PlantUML
plantuml diagram.puml -tpng


Reference in markdown (always use markdown syntax):

![Architecture Diagram](./diagrams/architecture.png)


Upload (script handles attachments):

python3 scripts/upload_confluence_v2.py document.md --id PAGE_ID


Common Mistakes:

Using raw XML: <ac:image>... - Gets HTML-escaped, appears as text
Using MCP for uploads - Size limits cause failures
Forgetting to convert diagrams - Code blocks don't render
Reference Documentation
Document	Purpose
upload_guide.md	Complete upload workflow
download_guide.md	Complete download workflow
wiki_markup_guide.md	Wiki Markup syntax reference
conversion_guide.md	Markdown ↔ Wiki Markup rules
image_handling_best_practices.md	Diagrams and images
troubleshooting_guide.md	Common errors and fixes
mark_tool_guide.md	Git-to-Confluence sync
confluence_storage_format.md	API storage format
cql_reference.md	CQL query syntax
atlassian_mcp_tools.md	MCP tool reference
Scripts
Script	Purpose
upload_confluence_v2.py	Upload Markdown with images (no size limits)
download_confluence.py	Download pages to Markdown with attachments
convert_markdown_to_wiki.py	Convert Markdown to Wiki Markup
render_mermaid.py	Render Mermaid diagrams to PNG/SVG
generate_mark_metadata.py	Generate mark CLI metadata headers
confluence_auth.py	Shared authentication utilities
Dependencies
pip install atlassian-python-api md2cf python-dotenv PyYAML mistune \
            requests markdownify beautifulsoup4

Prerequisites
Required
Atlassian MCP Server (mcp__atlassian) with Confluence credentials
Optional

mark CLI: Git-to-Confluence sync

brew install kovetskiy/mark/mark


Mermaid CLI: Diagram rendering

npm install -g @mermaid-js/mermaid-cli

When Not to Use
Simple page reads → Use MCP directly
No images/diagrams, small content → MCP may work
Jira issues → Use Jira-specific tools

Version: 2.2.0 | Last Updated: 2025-12-28

Weekly Installs
43
Repository
spillwavesoluti…nt-skill
GitHub Stars
9
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn