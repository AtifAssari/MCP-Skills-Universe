---
title: deepwiki-mcp-skill
url: https://skills.sh/holon-run/uxc/deepwiki-mcp-skill
---

# deepwiki-mcp-skill

skills/holon-run/uxc/deepwiki-mcp-skill
deepwiki-mcp-skill
Installation
$ npx skills add https://github.com/holon-run/uxc --skill deepwiki-mcp-skill
SKILL.md
DeepWiki Skill

Use this skill to query GitHub repository documentation and ask questions about codebases.

Prerequisites
uxc is installed and available in PATH.
Network access to mcp.deepwiki.com/mcp

Note: Repositories must be indexed on DeepWiki first. Visit https://deepwiki.com to index a repository.

Install uxc

Choose one of the following methods:

Homebrew (macOS/Linux):

brew tap holon-run/homebrew-tap
brew install uxc


Install Script (macOS/Linux, review before running):

curl -fsSL https://raw.githubusercontent.com/holon-run/uxc/main/scripts/install.sh -o install-uxc.sh
less install-uxc.sh
bash install-uxc.sh


Cargo:

cargo install uxc

Core Workflow

Use fixed link command by default:

command -v deepwiki-mcp-cli
If missing, create it: uxc link deepwiki-mcp-cli mcp.deepwiki.com/mcp
deepwiki-mcp-cli -h
If command conflict is detected and cannot be safely reused, stop and ask skill maintainers to pick a different fixed command name.

Ask a question about a repository:

deepwiki-mcp-cli ask_question repoName=owner/repo question='your question'

Read wiki structure:

deepwiki-mcp-cli read_wiki_structure repoName=owner/repo

Read wiki contents:

deepwiki-mcp-cli read_wiki_contents repoName=owner/repo
Available Tools
ask_question: Ask any question about a GitHub repository and get an AI-powered response
read_wiki_structure: Get a list of documentation topics for a repository
read_wiki_contents: View documentation about a repository
Usage Examples
Ask about a codebase
deepwiki-mcp-cli ask_question repoName=facebook/react question='How does useState work?'

Explore repository structure
deepwiki-mcp-cli read_wiki_structure '{"repoName":"facebook/react"}'

Read documentation
deepwiki-mcp-cli read_wiki_contents repoName=facebook/react

Output Parsing

The response is an MCP JSON envelope. Extract the content from .data.content[].text.

Notes
Maximum 10 repositories per question
Some popular repositories may already be indexed
Responses are grounded in the actual codebase
deepwiki-mcp-cli <operation> ... is equivalent to uxc mcp.deepwiki.com/mcp <operation> ....
If link setup is temporarily unavailable, use direct uxc mcp.deepwiki.com/mcp ... calls as fallback.
Reference Files
Workflow details: references/usage-patterns.md
Weekly Installs
25
Repository
holon-run/uxc
GitHub Stars
106
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail