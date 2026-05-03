---
rating: ⭐⭐⭐
title: svelte-code-writer
url: https://skills.sh/sveltejs/ai-tools/svelte-code-writer
---

# svelte-code-writer

skills/sveltejs/ai-tools/svelte-code-writer
svelte-code-writer
Installation
$ npx skills add https://github.com/sveltejs/ai-tools --skill svelte-code-writer
Summary

CLI tools for Svelte 5 documentation lookup and code analysis with built-in autofixer.

Three core commands: list-sections to browse available docs, get-documentation to fetch full documentation for specific topics, and svelte-autofixer to analyze code and suggest fixes
Autofixer supports Svelte 4 and 5 targeting via --svelte-version flag and async mode via --async option
Accepts both inline code (with escaped $ characters) and file paths for analysis
Designed for use within the svelte-file-editor agent when creating, editing, or analyzing .svelte components and .svelte.ts/.svelte.js modules
SKILL.md
Svelte 5 Code Writer
CLI Tools

You have access to @sveltejs/mcp CLI for Svelte-specific assistance. Use these commands via npx:

List Documentation Sections
npx @sveltejs/mcp list-sections


Lists all available Svelte 5 and SvelteKit documentation sections with titles and paths.

Get Documentation
npx @sveltejs/mcp get-documentation "<section1>,<section2>,..."


Retrieves full documentation for specified sections. Use after list-sections to fetch relevant docs.

Example:

npx @sveltejs/mcp get-documentation "$state,$derived,$effect"

Svelte Autofixer
npx @sveltejs/mcp svelte-autofixer "<code_or_path>" [options]


Analyzes Svelte code and suggests fixes for common issues.

Options:

--async - Enable async Svelte mode (default: false)
--svelte-version - Target version: 4 or 5 (default: 5)

Examples:

# Analyze inline code (escape $ as \$)
npx @sveltejs/mcp svelte-autofixer '<script>let count = \$state(0);</script>'

# Analyze a file
npx @sveltejs/mcp svelte-autofixer ./src/lib/Component.svelte

# Target Svelte 4
npx @sveltejs/mcp svelte-autofixer ./Component.svelte --svelte-version 4


Important: When passing code with runes ($state, $derived, etc.) via the terminal, escape the $ character as \$ to prevent shell variable substitution.

Workflow
Uncertain about syntax? Run list-sections then get-documentation for relevant topics
Reviewing/debugging? Run svelte-autofixer on the code to detect issues
Always validate - Run svelte-autofixer before finalizing any Svelte component
Weekly Installs
4.3K
Repository
sveltejs/ai-tools
GitHub Stars
238
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn