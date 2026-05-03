---
rating: ⭐⭐
title: mcp-deepwiki
url: https://skills.sh/s-hiraoku/vscode-sidebar-terminal/mcp-deepwiki
---

# mcp-deepwiki

skills/s-hiraoku/vscode-sidebar-terminal/mcp-deepwiki
mcp-deepwiki
Installation
$ npx skills add https://github.com/s-hiraoku/vscode-sidebar-terminal --skill mcp-deepwiki
SKILL.md
DeepWiki MCP
Overview

This skill enables exploration of GitHub repository documentation using the DeepWiki MCP server. DeepWiki provides AI-generated documentation and Q&A capabilities for any GitHub repository.

When to Use This Skill
Researching GitHub repository documentation
Understanding library or framework APIs
Asking specific questions about open-source projects
Exploring repository structure and architecture
Learning how to use unfamiliar libraries
Available Tools
read_wiki_structure

Get a list of documentation topics for a GitHub repository.

Tool: mcp__deepwiki__read_wiki_structure

Parameters:

repoName (required): GitHub repository in "owner/repo" format

Example:

mcp__deepwiki__read_wiki_structure({ repoName: "microsoft/vscode" })

read_wiki_contents

View comprehensive documentation about a GitHub repository.

Tool: mcp__deepwiki__read_wiki_contents

Parameters:

repoName (required): GitHub repository in "owner/repo" format

Example:

mcp__deepwiki__read_wiki_contents({ repoName: "xtermjs/xterm.js" })

ask_question

Ask any question about a GitHub repository and get AI-powered answers.

Tool: mcp__deepwiki__ask_question

Parameters:

repoName (required): GitHub repository in "owner/repo" format
question (required): The question to ask about the repository

Example:

mcp__deepwiki__ask_question({
  repoName: "microsoft/vscode",
  question: "How does the terminal extension handle PTY integration?"
})

Common Workflows
Research a New Library
Get wiki structure to understand available topics
Read full documentation for comprehensive understanding
Ask specific questions about implementation details
Understand VS Code Implementation
mcp__deepwiki__ask_question({
  repoName: "microsoft/vscode",
  question: "How does VS Code implement terminal session persistence?"
})

Explore xterm.js API
mcp__deepwiki__ask_question({
  repoName: "xtermjs/xterm.js",
  question: "What addons are available and how do I use them?"
})

Best Practices
Start with structure: Use read_wiki_structure first to understand available topics
Be specific with questions: Provide context in questions for better answers
Use full repo path: Always use the complete "owner/repo" format
Combine with local code: Use DeepWiki insights together with local codebase exploration
References

For detailed tool parameters, see references/tools.md.

Weekly Installs
24
Repository
s-hiraoku/vscod…terminal
GitHub Stars
18
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn