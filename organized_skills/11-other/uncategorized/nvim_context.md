---
rating: ⭐⭐
title: nvim-context
url: https://skills.sh/majjoha/dotfiles/nvim-context
---

# nvim-context

skills/majjoha/dotfiles/nvim-context
nvim-context
Installation
$ npx skills add https://github.com/majjoha/dotfiles --skill nvim-context
SKILL.md
Neovim context provider
Purpose

Provides live context from the user's Neovim editor session to help answer context-aware questions about code.

How it works
Executes the nvim-context tool to get the current editor state.
Returns JSON data including cursor position, open file, visual selection and diagnostics.
Use this information to understand references like "this line", "the selection", "current file", etc.
Usage examples
"What's wrong with this line?" → Check diagnostics at cursor
"Explain the selected code" → Analyze visual selection
"What file am I in?" → Return current file path
"Show me all errors" → List all LSP diagnostics
Technical details

To use this skill, execute the nvim-context CLI command which outputs JSON:

{
  "cursor": {
    "line": 43,
    "col": 3
  },
  "file": "/path/to/current/file.rb",
  "selection": null,
  "diagnostics": []
}

Implementation

When this skill is loaded, execute nvim-context via Bash and parse the JSON output to understand the current editor state. Use the returned data to answer user questions about their code.

Weekly Installs
14
Repository
majjoha/dotfiles
GitHub Stars
17
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass