---
rating: ⭐⭐⭐
title: repomix
url: https://skills.sh/mrgoonie/claudekit-skills/repomix
---

# repomix

skills/mrgoonie/claudekit-skills/repomix
repomix
Installation
$ npx skills add https://github.com/mrgoonie/claudekit-skills --skill repomix
SKILL.md
Repomix Skill

Repomix packs entire repositories into single, AI-friendly files. Perfect for feeding codebases to LLMs like Claude, ChatGPT, and Gemini.

When to Use

Use when:

Packaging codebases for AI analysis
Creating repository snapshots for LLM context
Analyzing third-party libraries
Preparing for security audits
Generating documentation context
Investigating bugs across large codebases
Creating AI-friendly code representations
Quick Start
Check Installation
repomix --version

Install
# npm
npm install -g repomix

# Homebrew (macOS/Linux)
brew install repomix

Basic Usage
# Package current directory (generates repomix-output.xml)
repomix

# Specify output format
repomix --style markdown
repomix --style json

# Package remote repository
npx repomix --remote owner/repo

# Custom output with filters
repomix --include "src/**/*.ts" --remove-comments -o output.md

Core Capabilities
Repository Packaging
AI-optimized formatting with clear separators
Multiple output formats: XML, Markdown, JSON, Plain text
Git-aware processing (respects .gitignore)
Token counting for LLM context management
Security checks for sensitive information
Remote Repository Support

Process remote repositories without cloning:

# Shorthand
npx repomix --remote yamadashy/repomix

# Full URL
npx repomix --remote https://github.com/owner/repo

# Specific commit
npx repomix --remote https://github.com/owner/repo/commit/hash

Comment Removal

Strip comments from supported languages (HTML, CSS, JavaScript, TypeScript, Vue, Svelte, Python, PHP, Ruby, C, C#, Java, Go, Rust, Swift, Kotlin, Dart, Shell, YAML):

repomix --remove-comments

Common Use Cases
Code Review Preparation
# Package feature branch for AI review
repomix --include "src/**/*.ts" --remove-comments -o review.md --style markdown

Security Audit
# Package third-party library
npx repomix --remote vendor/library --style xml -o audit.xml

Documentation Generation
# Package with docs and code
repomix --include "src/**,docs/**,*.md" --style markdown -o context.md

Bug Investigation
# Package specific modules
repomix --include "src/auth/**,src/api/**" -o debug-context.xml

Implementation Planning
# Full codebase context
repomix --remove-comments --copy

Command Line Reference
File Selection
# Include specific patterns
repomix --include "src/**/*.ts,*.md"

# Ignore additional patterns
repomix -i "tests/**,*.test.js"

# Disable .gitignore rules
repomix --no-gitignore

Output Options
# Output format
repomix --style markdown  # or xml, json, plain

# Output file path
repomix -o output.md

# Remove comments
repomix --remove-comments

# Copy to clipboard
repomix --copy

Configuration
# Use custom config file
repomix -c custom-config.json

# Initialize new config
repomix --init  # creates repomix.config.json

Token Management

Repomix automatically counts tokens for individual files, total repository, and per-format output.

Typical LLM context limits:

Claude Sonnet 4.5: ~200K tokens
GPT-4: ~128K tokens
GPT-3.5: ~16K tokens
Security Considerations

Repomix uses Secretlint to detect sensitive data (API keys, passwords, credentials, private keys, AWS secrets).

Best practices:

Always review output before sharing
Use .repomixignore for sensitive files
Enable security checks for unknown codebases
Avoid packaging .env files
Check for hardcoded credentials

Disable security checks if needed:

repomix --no-security-check

Implementation Workflow

When user requests repository packaging:

Assess Requirements

Identify target repository (local/remote)
Determine output format needed
Check for sensitive data concerns

Configure Filters

Set include patterns for relevant files
Add ignore patterns for unnecessary files
Enable/disable comment removal

Execute Packaging

Run repomix with appropriate options
Monitor token counts
Verify security checks

Validate Output

Review generated file
Confirm no sensitive data
Check token limits for target LLM

Deliver Context

Provide packaged file to user
Include token count summary
Note any warnings or issues
Reference Documentation

For detailed information, see:

Configuration Reference - Config files, include/exclude patterns, output formats, advanced options
Usage Patterns - AI analysis workflows, security audit preparation, documentation generation, library evaluation
Additional Resources
GitHub: https://github.com/yamadashy/repomix
Documentation: https://repomix.com/guide/
MCP Server: Available for AI assistant integration
Weekly Installs
260
Repository
mrgoonie/claude…t-skills
GitHub Stars
2.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn