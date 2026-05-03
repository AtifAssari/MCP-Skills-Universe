---
title: coderabbit
url: https://skills.sh/basher83/lunar-claude/coderabbit
---

# coderabbit

skills/basher83/lunar-claude/coderabbit
coderabbit
Installation
$ npx skills add https://github.com/basher83/lunar-claude --skill coderabbit
SKILL.md
CodeRabbit

AI code review tool that catches race conditions, memory leaks, and security vulnerabilities. Integrates with Claude Code for autonomous review-and-fix workflows.

Quick Start: Claude Code Integration

Run CodeRabbit as part of your development workflow:

Implement the feature from the spec, then run coderabbit --prompt-only
in the background and fix any issues found.


Key flags for Claude Code:

--prompt-only - Minimal output optimized for AI agents
--plain - Plain text mode (no interactive UI)
--type uncommitted - Review only uncommitted changes
CLI Commands
# Install
curl -fsSL https://cli.coderabbit.ai/install.sh | sh

# Authenticate (run once per Claude Code session)
coderabbit auth login

# Review code
coderabbit                          # Interactive mode
coderabbit --plain                  # Plain text output
coderabbit --prompt-only            # AI-optimized output
coderabbit --type uncommitted       # Only uncommitted changes
coderabbit --base develop           # Compare against develop branch

Claude Code Workflow

Recommended prompt pattern:

Please implement [feature] and then run coderabbit --prompt-only,
let it run as long as it needs (run it in the background) and fix any issues.


CodeRabbit reviews take 7-30+ minutes. Run in background and check periodically.

Fix prioritization: Fix critical issues first, ignore nits. Run CodeRabbit again after fixes to verify no new issues introduced. Limit to 2 iterations.

GitHub Commands

Use @coderabbitai in PR comments:

Command	Description
@coderabbitai review	Incremental review of new changes
@coderabbitai full review	Complete review from scratch
@coderabbitai pause	Stop automatic reviews
@coderabbitai resume	Restart reviews
@coderabbitai summary	Regenerate PR summary
@coderabbitai generate docstrings	Generate function docs (Pro)
@coderabbitai generate unit tests	Generate tests (Pro)
@coderabbitai resolve	Resolve all CR comments
@coderabbitai configuration	Show current settings

Add @coderabbitai ignore to PR description to disable reviews for that PR.

Configuration (.coderabbit.yaml)
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
language: en-US
tone_instructions: "Be concise and focus on critical issues only"

reviews:
  profile: chill  # or "assertive" for comprehensive feedback
  high_level_summary: true
  auto_review:
    enabled: true
    drafts: false
    ignore_title_keywords:
      - "wip"
      - "draft"

knowledge_base:
  code_guidelines:
    enabled: true
    filePatterns:
      - "**/.cursorrules"
      - "**/claude.md"


CodeRabbit auto-reads claude.md and .cursorrules for coding standards.

Supported Tools

CodeRabbit integrates 40+ linters and security analyzers:

JavaScript/TypeScript: ESLint, Biome, Oxlint
Python: Ruff, Pylint, Flake8
Go: golangci-lint
Security: Gitleaks, Semgrep, OSV Scanner
Infrastructure: Checkov, Hadolint
CI/CD: actionlint, CircleCI

Full tools reference: See references/tools-reference.md

Troubleshooting

CodeRabbit not finding issues:

Check auth: coderabbit auth status
Verify git status: git status
Specify review type: --type uncommitted
Specify base branch: --base develop

Claude Code not applying fixes:

Use --prompt-only mode
Include "run in background" in prompt
Explicitly ask to "fix issues found by CodeRabbit"
References
Overview: references/overview.md
Claude Code Integration: references/claude-code-integration.md
YAML Configuration: references/yaml-configuration-guide.md
GitHub Commands: references/github-commands.md
Tools Reference: references/tools-reference.md
Full Configuration: references/configuration.md
Weekly Installs
10
Repository
basher83/lunar-claude
GitHub Stars
18
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykFail