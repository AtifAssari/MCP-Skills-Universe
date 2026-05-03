---
title: resource-scout
url: https://skills.sh/nicepkg/ai-workflow/resource-scout
---

# resource-scout

skills/nicepkg/ai-workflow/resource-scout
resource-scout
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill resource-scout
SKILL.md
Resource Scout

Search and discover existing Claude Code skills and MCP servers before building custom solutions.

Quick Search Strategy

For Skills:

WebSearch: site:skillsmp.com [topic] or claude skill [topic]
Check GitHub: awesome-claude-skills [topic]
Browse: skillhub.club, claudeskills.info

For MCP:

WebSearch: MCP server [tool/service name]
Check: glama.ai/mcp/servers, mcpmarket.com
Official: github.com/modelcontextprotocol/servers
Skill Search Workflow
Step 1: Define Need

Before searching, clarify:

What task needs to be accomplished?
What tools/services are involved?
Is it a common pattern (git, testing, API) or domain-specific?
Step 2: Search Marketplaces

Primary sources (largest catalogs):

Source	URL	Best For
SkillsMP	skillsmp.com	71000+ skills, long-tail search
SkillHub.club	skillhub.club	AI-evaluated, quality filter
Claude Skills Hub	claudeskills.info	UI-friendly browsing

Search patterns:

# On SkillsMP
[domain] skill          → "marketing skill", "database skill"
[framework] claude      → "react claude", "fastapi claude"
[task] automation       → "deployment automation"

Step 3: Search GitHub

Curated lists:

github.com/keyuyuan/skillhub-awesome-skills - 精选清单
github.com/VoltAgent/awesome-claude-skills - 生态大全
github.com/ComposioHQ/awesome-claude-skills - 大量通用技能

Ready-to-use repositories:

github.com/alirezarezvani/claude-skills - Content/Marketing
github.com/gked2121/claude-skills - Workflow思维
github.com/Microck/ordinary-claude-skills - 超大集合
github.com/sickn33/antigravity-awesome-skills - 结构化

Search command:

# Use WebSearch tool
site:github.com "claude skill" [topic]
site:github.com "SKILL.md" [topic]

Step 4: Evaluate & Install

When skill found:

Check last update date (prefer recent)
Review SKILL.md for quality
Check if has scripts/references
Install with skill-downloader or manual copy
MCP Server Search Workflow
Step 1: Identify Integration Need

Common patterns:

Database access → postgres, mysql, sqlite MCP
GitHub workflow → github MCP
Cloud services → AWS, GCP, Azure MCPs
Communication → slack, discord MCPs
File systems → filesystem MCP
Step 2: Search Official Sources

Primary:

Official registry: registry.modelcontextprotocol.io
Official repo: github.com/modelcontextprotocol/servers

Directories:

Source	URL	Features
Glama	glama.ai/mcp/servers	Stars, downloads, updates
MCP Market	mcpmarket.com	Skills + MCP combined
mcpservers.org	mcpservers.org	Categorized
PulseMCP	pulsemcp.com/servers	Daily updates
Smithery	smithery.ai	Registry/distribution
Step 3: Search GitHub
# Use WebSearch tool
site:github.com "mcp server" [service]
site:github.com "@modelcontextprotocol" [service]


Awesome lists:

github.com/punkpeye/awesome-mcp-servers
github.com/wong2/awesome-mcp-servers
Step 4: Verify & Configure

When MCP found:

Check compatibility (stdio vs HTTP)
Review required environment variables
Test connection locally
Add to .claude/settings.json
Search by Category
Development Tools
Skills: "code review skill", "git commit skill", "testing skill"
MCP: "github mcp", "gitlab mcp", "jira mcp"

Databases
Skills: "database skill", "sql skill", "migration skill"
MCP: "postgres mcp", "mysql mcp", "mongodb mcp"

Content & Marketing
Skills: "content creator skill", "seo skill", "social media skill"
MCP: "wordpress mcp", "notion mcp"

Cloud & DevOps
Skills: "deployment skill", "kubernetes skill", "terraform skill"
MCP: "aws mcp", "gcp mcp", "azure mcp"

AI & Data
Skills: "data analysis skill", "ml skill"
MCP: "openai mcp", "huggingface mcp"

Complete Source Reference

See references/sources.md for full directory of all skill and MCP sources with detailed descriptions.

Best Practices
Search before build - Always check existing resources first
Prefer maintained - Choose skills with recent updates
Check quality - Review SKILL.md structure and content
Consider combining - Multiple simple skills > one complex custom
Verify security - Review MCP permissions and token scopes
Weekly Installs
257
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn