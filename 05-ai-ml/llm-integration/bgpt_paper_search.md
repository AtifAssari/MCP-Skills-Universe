---
rating: ⭐⭐
title: bgpt-paper-search
url: https://skills.sh/k-dense-ai/scientific-agent-skills/bgpt-paper-search
---

# bgpt-paper-search

skills/k-dense-ai/scientific-agent-skills/bgpt-paper-search
bgpt-paper-search
Installation
$ npx skills add https://github.com/k-dense-ai/scientific-agent-skills --skill bgpt-paper-search
SKILL.md
BGPT Paper Search
Overview

BGPT is a remote MCP server that searches a curated database of scientific papers built from raw experimental data extracted from full-text studies. Unlike traditional literature databases that return titles and abstracts, BGPT returns structured data from the actual paper content — methods, quantitative results, sample sizes, quality assessments, and 25+ metadata fields per paper.

When to Use This Skill

Use this skill when:

Searching for scientific papers with specific experimental details
Conducting systematic or scoping literature reviews
Finding quantitative results, sample sizes, or effect sizes across studies
Comparing methodologies used in different studies
Looking for papers with quality scores or evidence grading
Needing structured data from full-text papers (not just abstracts)
Building evidence tables for meta-analyses or clinical guidelines
Setup

BGPT is a remote MCP server — no local installation required.

Claude Desktop / Claude Code

Add to your MCP configuration:

{
  "mcpServers": {
    "bgpt": {
      "command": "npx",
      "args": ["mcp-remote", "https://bgpt.pro/mcp/sse"]
    }
  }
}

npm (alternative)
npx bgpt-mcp

Usage

Once configured, use the search_papers tool provided by the BGPT MCP server:

Search for papers about: "CRISPR gene editing efficiency in human cells"


The server returns structured results including:

Title, authors, journal, year, DOI
Methods: Experimental techniques, models, protocols
Results: Key findings with quantitative data
Sample sizes: Number of subjects/samples
Quality scores: Study quality assessments
Conclusions: Author conclusions and implications
Pricing
Free tier: 50 searches per network, no API key required
Paid: $0.01 per result with an API key from bgpt.pro/mcp
Weekly Installs
168
Repository
k-dense-ai/scie…t-skills
GitHub Stars
19.9K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass