---
rating: ⭐⭐
title: github-trending-analyzer
url: https://skills.sh/jackjin1997/clawforge/github-trending-analyzer
---

# github-trending-analyzer

skills/jackjin1997/clawforge/github-trending-analyzer
github-trending-analyzer
Installation
$ npx skills add https://github.com/jackjin1997/clawforge --skill github-trending-analyzer
SKILL.md
GitHub Trending Analyzer

Use this skill to provide a comprehensive, categorized summary of the latest trending repositories on GitHub, including daily, weekly, and monthly lists.

Workflow
Fetch Data: Use the provided script to fetch trending data for three time spans:
Daily: scripts/fetch_trending.sh daily
Weekly: scripts/fetch_trending.sh weekly
Monthly: scripts/fetch_trending.sh monthly
Full Inventory: List every single project found in each list. Do not omit any repositories.
Cross-List Deduplication: Note projects that appear in multiple spans (e.g., "appears in both Weekly and Monthly").
Deep Categorization: Group ALL discovered projects into logical buckets.
Hyperlinking: Every project mentioned MUST include its full GitHub URL.
Observation: Identify 3-5 high-level trends across the entire data set.
Categorization Taxonomy
⌨️ Terminal Agents & AI Coding: CLI tools, IDE plugins (Neovim/VSCode), and automated coding assistants.
🛡️ Autonomous Security: Pentesting agents, vulnerability scanners, and model jailbreak/un-censoring tools.
🧠 Memory & Knowledge Management: Agent memory layers, long-term persistence, and next-gen RAG/indexing.
⚙️ AI Infra & Protocols: MCP, SDKs, orchestration frameworks, and specialized model deployments (e.g., Cloudflare Workers).
🔓 Prompt Engineering & Data: System prompt collections, datasets, and meta-prompting tools.
🛠️ Productivity & Specialized Apps: Finance AI, media servers, diagram tools, and general AI assistants.
Output Structure
📅 Part 1: Full Trending Lists

Provide bulleted lists for Daily, Weekly, and Monthly, with short descriptions for each.

🏗️ Part 2: Categorized Analysis

Provide Markdown tables for each category:

Project	Span	Description
user/repo	D/W/M	Summary...
💡 Part 3: Strategic Insights

Summarize the current "vibe" of GitHub (e.g., "The shift from Web to CLI").

Weekly Installs
30
Repository
jackjin1997/clawforge
GitHub Stars
7
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn