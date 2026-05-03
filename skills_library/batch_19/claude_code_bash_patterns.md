---
title: claude-code-bash-patterns
url: https://skills.sh/secondsky/claude-skills/claude-code-bash-patterns
---

# claude-code-bash-patterns

skills/secondsky/claude-skills/claude-code-bash-patterns
claude-code-bash-patterns
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill claude-code-bash-patterns
SKILL.md
Claude Code Bash Patterns

Status: Production Ready ✅ | Last Verified: 2025-11-18

Quick Start
Basic Command
ls -la

Command Chaining
bun install && bun run build && bun test

Hooks

Create .claude-hook-pretooluse.sh:

#!/usr/bin/env bash
# PreToolUse hook - runs before every Bash command

echo "Running: $1"


Load references/hooks-examples.md for complete hook patterns.

The Five Core Patterns
1. Sequential Operations (&&)

Use when: Each command depends on previous success

git add . && git commit -m "message" && git push


Why: Stops chain if any command fails

2. Parallel Operations (Multiple tool calls)

Use when: Commands are independent

Message with multiple Bash tool calls in parallel


Load references/cli-tool-integration.md for parallel patterns.

3. Session Persistence

Use when: Need to maintain state across commands

# Set environment variable
export API_KEY="sk-..."

# Use in later commands (same session)
curl -H "Authorization: Bearer $API_KEY" api.example.com

4. Background Processes

Use when: Long-running tasks

npm run dev &
# Get PID with $!

5. Hooks for Automation

Use when: Need pre/post command logic

Load references/hooks-examples.md for all hook types.

Critical Rules
Always Do ✅
Use && for sequential dependencies (not semicolons)
Quote paths with spaces (cd "path with spaces")
Check environment before destructive ops (rm, git push --force)
Use specialized tools first (Read, Grep, Glob before Bash)
Set timeouts for long operations (up to 10 minutes)
Validate inputs before passing to shell commands
Use hooks for repeated patterns (logging, validation)
Maintain session state (export variables once)
Handle errors explicitly (check exit codes)
Document custom commands in .claude/commands/
Never Do ❌
Never use ; for dependent commands (use &&)
Never skip quoting paths with spaces
Never run rm -rf without confirmation
Never expose secrets in command output
Never ignore timeout limits (max 10 min)
Never use bash for file operations when specialized tools exist
Never chain with newlines (use && or ; explicitly)
Never force-push to main without explicit user request
Never skip hooks (--no-verify) without user request
Never use interactive commands (git rebase -i, git add -i)
Git Workflows
Basic Commit
git add . && git commit -m "feat: add feature"

Commit with Testing
npm test && git add . && git commit -m "fix: bug fix" && git push

Pull Request
git checkout -b feature/new && git add . && git commit -m "feat: new feature" && git push -u origin feature/new


Load references/git-workflows.md for complete workflows including:

Feature branch workflow
PR creation automation
Commit message conventions
Pre-commit validation
Hooks: Advanced Automation
PreToolUse Hook

.claude-hook-pretooluse.sh:

#!/usr/bin/env bash
COMMAND="$1"

# Log all commands
echo "[$(date)] Running: $COMMAND" >> ~/claude-commands.log

# Block dangerous patterns
if [[ "$COMMAND" =~ rm\ -rf\ / ]]; then
    echo "❌ Blocked dangerous command"
    exit 1
fi

Hook Types
pretooluse - Before every Bash command
stop - Before conversation ends
user-prompt-submit - After user submits message

Load references/hooks-examples.md for all hook types and examples.

CLI Tool Integration
npm/bun
bun install && bun run build

wrangler (Cloudflare)
bunx wrangler deploy

gh (GitHub CLI)
gh pr create --title "Fix bug" --body "Description"


Load references/cli-tool-integration.md for complete tool patterns.

Custom Commands

Create .claude/commands/deploy.md:

---
description: Deploy to production
---

Run these steps:
1. Run tests: `npm test`
2. Build: `npm run build`
3. Deploy: `wrangler deploy`


User can invoke with: /deploy

Load templates/custom-command-template.md for template.

Security
Allowlisting Tools

settings.json:

{
  "dangerousCommandsAllowList": [
    "git push --force"
  ]
}

Secrets Management
# ✅ Good: Use environment variables
export API_KEY="$SECURE_VALUE"

# ❌ Bad: Hardcode secrets
curl -H "Authorization: Bearer sk-abc123..."


Load references/security-best-practices.md for complete security guide.

Common Use Cases
Use Case 1: Test Before Commit
npm test && git add . && git commit -m "message"

Use Case 2: Deploy with Validation
npm run lint && npm test && npm run build && bunx wrangler deploy

Use Case 3: Multi-Repo Operations
cd repo1 && git pull && cd ../repo2 && git pull

Use Case 4: Background Process
npm run dev &


Load references/cli-tool-integration.md for more patterns.

Troubleshooting
Issue: Command times out

Solution: Increase timeout or use background mode

# Background mode
npm run dev &

Issue: Path with spaces fails

Solution: Quote the path

cd "path with spaces/file.txt"

Issue: Hook blocks command

Solution: Check hook logic in .claude-hook-pretooluse.sh

Load references/troubleshooting-guide.md for all issues.

When to Load References
Load references/git-workflows.md when:
Setting up git automation
Creating PRs programmatically
Need commit message conventions
Want pre-commit validation patterns
Load references/hooks-examples.md when:
Creating custom hooks
Need hook templates
Want validation patterns
Implementing logging/security
Load references/cli-tool-integration.md when:
Orchestrating multiple CLI tools
Need tool-specific patterns
Want parallel execution examples
Troubleshooting tool integration
Load references/security-best-practices.md when:
Configuring security guards
Setting up allowlisting
Managing secrets
Preventing dangerous operations
Load references/troubleshooting-guide.md when:
Debugging command failures
Encountering timeouts
Hooks behaving unexpectedly
Session state issues
Using Bundled Resources
References (references/)
git-workflows.md - Complete git automation patterns
hooks-examples.md - All hook types with examples
cli-tool-integration.md - Tool orchestration patterns
security-best-practices.md - Security configuration guide
troubleshooting-guide.md - Common issues and solutions
Templates (templates/)
custom-command-template.md - Custom command template
settings.json - Security settings example
.envrc.example - Environment variables example
github-workflow.yml - GitHub Actions integration
dangerous-commands.json - Dangerous patterns list
Examples
Feature Development Workflow
git checkout -b feature/oauth && \
  npm test && \
  git add . && \
  git commit -m "feat(auth): add OAuth support" && \
  git push -u origin feature/oauth

CI/CD Pipeline
npm run lint && \
  npm test && \
  npm run build && \
  bunx wrangler deploy

Multi-Project Update
cd project1 && bun install && cd ../project2 && bun install

Official Documentation
Claude Code Bash Tool: https://docs.claude.com/en/docs/claude-code/tools
Hooks: https://docs.claude.com/en/docs/claude-code/hooks
Custom Commands: https://docs.claude.com/en/docs/claude-code/custom-commands

Questions? Issues?

Check references/troubleshooting-guide.md for common issues
Review references/git-workflows.md for git patterns
See references/hooks-examples.md for automation
Load references/security-best-practices.md for security
Weekly Installs
172
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass