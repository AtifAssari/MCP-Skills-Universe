---
title: codex-review
url: https://skills.sh/alinaqi/claude-bootstrap/codex-review
---

# codex-review

skills/alinaqi/claude-bootstrap/codex-review
codex-review
Installation
$ npx skills add https://github.com/alinaqi/claude-bootstrap --skill codex-review
SKILL.md
OpenAI Codex Code Review Skill

Use OpenAI's Codex CLI for specialized code review with GPT-5.2-Codex - trained specifically for detecting bugs, security flaws, and code quality issues.

Sources: Codex CLI | GitHub | Code Review Cookbook

Why Codex for Code Review?
Feature	Benefit
GPT-5.2-Codex	Specialized training for code review
88% detection rate	Bugs, security flaws, style issues (LiveCodeBench)
Structured output	JSON schema for consistent findings
GitHub native	@codex review in PR comments
Headless mode	CI/CD automation without TUI
Installation
Prerequisites
# Check Node.js version (requires 22+)
node --version

# Install Node.js 22 if needed
# macOS
brew install node@22

# Or via nvm
nvm install 22
nvm use 22

Install Codex CLI
# Via npm (recommended)
npm install -g @openai/codex

# Via Homebrew (macOS)
brew install --cask codex

# Verify installation
codex --version

Authentication

Option 1: ChatGPT Subscription (Plus, Pro, Team, Edu, Enterprise)

codex
# Follow prompts to sign in with ChatGPT account


Option 2: OpenAI API Key

# Set environment variable
export OPENAI_API_KEY=sk-proj-...

# Or add to shell profile
echo 'export OPENAI_API_KEY=sk-proj-...' >> ~/.zshrc

# Run Codex
codex

Shell Completions (Optional)
# Bash
codex completion bash >> ~/.bashrc

# Zsh
codex completion zsh >> ~/.zshrc

# Fish
codex completion fish > ~/.config/fish/completions/codex.fish

Interactive Code Review
Launch Review Mode
# Start Codex
codex

# In the TUI, type:
/review

Review Presets
Preset	Use Case
Review against base branch	Before opening PR - diffs against upstream
Review uncommitted changes	Before committing - staged + unstaged + untracked
Review a commit	Analyze specific SHA from history
Custom instructions	e.g., "Focus on security vulnerabilities"
Example Session
$ codex
> /review

Select review type:
❯ Review against a base branch
  Review uncommitted changes
  Review a commit
  Custom review instructions

Select base branch: main

Reviewing changes...

┌─────────────────────────────────────────────────────────────┐
│ CODE REVIEW FINDINGS                                        │
├─────────────────────────────────────────────────────────────┤
│ 🔴 CRITICAL: SQL Injection vulnerability                    │
│    File: src/api/users.ts:45                                │
│    Issue: User input directly interpolated in query         │
│    Fix: Use parameterized queries                           │
├─────────────────────────────────────────────────────────────┤
│ 🟠 HIGH: Missing authentication check                       │
│    File: src/api/admin.ts:23                                │
│    Issue: Admin endpoint accessible without auth            │
│    Fix: Add requireAuth middleware                          │
├─────────────────────────────────────────────────────────────┤
│ 🟡 MEDIUM: Inefficient database query                       │
│    File: src/services/orders.ts:89                          │
│    Issue: N+1 query pattern in loop                         │
│    Fix: Use batch query or JOIN                             │
└─────────────────────────────────────────────────────────────┘

Headless Mode (Automation)
Basic Usage
# Simple review
codex exec "review the code for bugs and security issues"

# Review with JSON output
codex exec --json "review uncommitted changes" > review.json

# Save final message to file
codex exec --output-last-message review.txt "review the diff against main"

Full Automation (CI/CD)
# Full auto mode (use only in isolated runners!)
codex exec \
  --full-auto \
  --json \
  --output-last-message findings.txt \
  --sandbox read-only \
  -m gpt-5.2-codex \
  "Review this code for bugs, security issues, and performance problems"

Structured Output with Schema
# Define output schema
cat > review-schema.json << 'EOF'
{
  "type": "object",
  "properties": {
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "severity": { "enum": ["critical", "high", "medium", "low"] },
          "title": { "type": "string" },
          "file": { "type": "string" },
          "line": { "type": "integer" },
          "description": { "type": "string" },
          "suggestion": { "type": "string" }
        },
        "required": ["severity", "title", "file", "description"]
      }
    },
    "summary": { "type": "string" },
    "approved": { "type": "boolean" }
  },
  "required": ["findings", "summary", "approved"]
}
EOF

# Run with schema validation
codex exec \
  --output-schema review-schema.json \
  --output-last-message review.json \
  "Review the staged changes and output findings"

GitHub Integration
Option 1: PR Comment Trigger

In any pull request, add a comment:

@codex review


Codex will respond with a standard GitHub code review.

Option 2: GitHub Action
# .github/workflows/codex-review.yml
name: Codex Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Codex Review
        uses: openai/codex-action@main
        with:
          openai_api_key: ${{ secrets.OPENAI_API_KEY }}
          model: gpt-5.2-codex
          safety_strategy: drop-sudo

Option 3: Manual Headless in CI
# .github/workflows/codex-review.yml
name: Codex Code Review

on:
  pull_request:

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '22'

      - name: Install Codex CLI
        run: npm install -g @openai/codex

      - name: Run Review
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          # Get diff
          git diff origin/${{ github.base_ref }}...HEAD > diff.txt

          # Run Codex review
          codex exec \
            --full-auto \
            --sandbox read-only \
            --output-last-message review.md \
            "Review this git diff for bugs, security issues, and code quality: $(cat diff.txt)"

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('review.md', 'utf8');
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: `## 🤖 Codex Code Review\n\n${review}`
            });

GitLab CI/CD
# .gitlab-ci.yml
codex-review:
  image: node:22
  stage: review
  script:
    - npm install -g @openai/codex
    - |
      codex exec \
        --full-auto \
        --sandbox read-only \
        --output-last-message review.md \
        "Review the merge request changes for bugs and security issues"
    - cat review.md
  artifacts:
    paths:
      - review.md
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

Jenkins Pipeline
pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {
        stage('Install Codex') {
            steps {
                sh 'npm install -g @openai/codex'
            }
        }

        stage('Code Review') {
            steps {
                sh '''
                    codex exec \
                      --full-auto \
                      --sandbox read-only \
                      --output-last-message review.md \
                      "Review the code changes for bugs and security issues"
                '''
            }
        }

        stage('Publish Results') {
            steps {
                archiveArtifacts artifacts: 'review.md'
                script {
                    def review = readFile('review.md')
                    echo "Code Review Results:\n${review}"
                }
            }
        }
    }
}

Configuration
Config File
# ~/.codex/config.toml

[model]
default = "gpt-5.2-codex"  # Best for code review

[sandbox]
default = "read-only"  # Safe for reviews

[review]
# Custom review instructions applied to all reviews
instructions = """
Focus on:
1. Security vulnerabilities (OWASP Top 10)
2. Performance issues (N+1 queries, memory leaks)
3. Error handling gaps
4. Type safety issues
"""

Per-Project Config
# .codex/config.toml (in project root)

[review]
instructions = """
This is a Python FastAPI project. Focus on:
- Async/await correctness
- Pydantic model validation
- SQL injection via SQLAlchemy
- Authentication/authorization gaps
"""

CLI Quick Reference
# Interactive
codex                          # Start TUI
/review                        # Open review presets

# Headless
codex exec "prompt"            # Non-interactive execution
codex exec --json "prompt"     # JSON output
codex exec --full-auto "prompt"  # No approval prompts

# Key Flags
--output-last-message FILE     # Save response to file
--output-schema FILE           # Validate against JSON schema
--sandbox read-only            # Restrict file access
-m gpt-5.2-codex              # Use best review model
--json                         # Machine-readable output

# Resume
codex exec resume SESSION_ID   # Continue previous session

Comparison: Claude vs Codex Review
Aspect	Claude (Built-in)	Codex CLI
Setup	None (already in Claude Code)	Install CLI + auth
Model	Claude	GPT-5.2-Codex (specialized)
Context	Full conversation context	Fresh context per review
Integration	Native	GitHub, GitLab, Jenkins
Output	Markdown	JSON schema support
Best for	Quick reviews, in-flow	CI/CD, critical PRs
Security Considerations
CI/CD Safety
# Always use these flags in CI/CD:
--sandbox read-only           # Prevent file modifications
--safety-strategy drop-sudo   # Revoke elevated permissions

API Key Protection
# GitHub Actions - use secrets
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

# Never hardcode keys
# Never echo keys in logs

Public Repositories

For public repos, use drop-sudo safety strategy to prevent Codex from reading its own API key during execution.

Troubleshooting
Issue	Solution
codex: command not found	Run npm install -g @openai/codex
Node.js version error	Upgrade to Node.js 22+
Authentication failed	Re-run codex and sign in again
API key invalid	Check OPENAI_API_KEY env var
Timeout in CI	Add --timeout 300 flag
Rate limited	Reduce frequency or upgrade plan
Anti-Patterns
Using --dangerously-bypass-approvals-and-sandbox casually - Only in isolated CI runners
Exposing API keys in logs - Use secrets management
Skipping sandbox in CI - Always use --sandbox read-only
Ignoring findings - Review and address or document exceptions
Running on every commit - Use on PRs only to save costs
Weekly Installs
157
Repository
alinaqi/claude-bootstrap
GitHub Stars
591
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn