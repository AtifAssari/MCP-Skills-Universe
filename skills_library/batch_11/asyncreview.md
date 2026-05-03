---
title: asyncreview
url: https://skills.sh/asyncfuncai/asyncreview/asyncreview
---

# asyncreview

skills/asyncfuncai/asyncreview/asyncreview
asyncreview
Installation
$ npx skills add https://github.com/asyncfuncai/asyncreview --skill asyncreview
SKILL.md
AsyncReview CLI
When to use this skill

Use this skill when the user:

Asks to review a GitHub pull request
Wants AI feedback on code changes in a PR
Needs to check if a PR breaks existing functionality
Asks questions about a GitHub issue or PR
Wants to verify if something was missed in a code change
How to use this skill
Check prerequisites — Verify GEMINI_API_KEY is set
Check if repo is private — Use gh repo view to determine if GITHUB_TOKEN is required
Set GITHUB_TOKEN if needed — Use gh auth token for private repos
Get the PR/Issue URL — Ask user if not provided
Formulate a question — Convert user's request into a specific question
Run the review command — Execute npx asyncreview review --url <URL> -q "<question>"
Present the results — Share the AI's findings with sources
Prerequisites
1. Check for GEMINI_API_KEY (Required)

Before running any command, check for GEMINI_API_KEY:

echo $GEMINI_API_KEY


If empty or not set, ask the user to provide their Gemini API key:

"AsyncReview requires a Gemini API key. Please set GEMINI_API_KEY in your environment or provide it now."

Then set it:

export GEMINI_API_KEY="user-provided-key"

2. Check if Repository is Private (Critical)

IMPORTANT: Before reviewing a PR/Issue, you MUST check if the repository is private. If it is, GITHUB_TOKEN is REQUIRED.

Step 1: Extract owner and repo from URL

From a URL like https://github.com/owner/repo/pull/123, extract:

owner: owner
repo: repo
Step 2: Check repository visibility

Option A: Using GitHub CLI (if available)

gh repo view owner/repo --json isPrivate -q '.isPrivate'


Option B: Without GitHub CLI (using curl)

# Try to access the repo via GitHub API without authentication
curl -s -o /dev/null -w "%{http_code}" https://api.github.com/repos/owner/repo


Possible outcomes:

With gh:

true → Repository is private, GITHUB_TOKEN is REQUIRED
false → Repository is public, GITHUB_TOKEN is optional
Error (e.g., "not found") → May indicate private repo without auth, or repo doesn't exist

With curl:

200 → Repository is public, GITHUB_TOKEN is optional (but recommended for higher rate limits)
404 → Repository is private or doesn't exist, GITHUB_TOKEN is REQUIRED
403 → Rate limited, need GITHUB_TOKEN
Step 3: If private, ensure GITHUB_TOKEN is set
# Check if GITHUB_TOKEN is already set
echo $GITHUB_TOKEN


If empty or not set, obtain it using one of these methods:

Option A: Using GitHub CLI (if available)

# Get token from GitHub CLI (must be authenticated with `gh auth login` first)
export GITHUB_TOKEN=$(gh auth token)

# Verify it's set
echo $GITHUB_TOKEN


If gh auth token fails, authenticate first:

gh auth login


Option B: Without GitHub CLI (create token via web)

Go to GitHub: https://github.com/settings/tokens
Click "Generate new token" → "Generate new token (classic)"
Give it a descriptive name (e.g., "AsyncReview CLI")
Select scopes:
✅ repo (Full control of private repositories)
Click "Generate token"
Copy the token (you won't see it again!)
Set it in your terminal:
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Verify it's set
echo $GITHUB_TOKEN


Security tip: For better security, consider creating a fine-grained token with minimal permissions:

Go to: https://github.com/settings/personal-access-tokens/new
Select specific repositories
Grant only "Contents" read permission

Then run the review with the token:

npx asyncreview review --url <URL> -q "question" --github-token $GITHUB_TOKEN


Or set it as an environment variable for the session:

export GITHUB_TOKEN=$(gh auth token)
npx asyncreview review --url <URL> -q "question"

Quick start
npx asyncreview review --url <PR_URL> -q "question"   # Review a PR
npx asyncreview review --url <PR_URL> --expert        # Expert code review
npx asyncreview review --url <PR_URL> --output markdown     # Markdown output

Core workflow
Get PR URL from user
Run review with specific question
Read the step-by-step reasoning output
Model can fetch files outside the diff autonomously
Commands
Review
npx asyncreview review --url <url> -q "question"      # Review with question
npx asyncreview review --url <url> -q "q" --output markdown # Markdown output
npx asyncreview review --url <url> -q "q" -o json     # JSON output


URL formats supported:

https://github.com/owner/repo/pull/123
https://github.com/owner/repo/issues/456
Environment variables
GEMINI_API_KEY="your-key"         # Required: Google Gemini API key
GITHUB_TOKEN="ghp_xxx"            # Optional: For private repos / higher rate limits

Example: Review a PR
npx asyncreview review \
  --url https://github.com/stanfordnlp/dspy/pull/9223 \
  -q "Does this change break any existing callers?"


Output shows:

Step number
💭 Reasoning (what the AI is thinking)
📝 Code (Python being executed)
📤 Output (REPL result)
Final answer with sources
Example: Check if feature exists elsewhere
npx asyncreview review \
  --url https://github.com/owner/repo/pull/123 \
  -q "Fetch src/utils.py and check if deprecated_func is still used"


The AI will:

Search for the file path
Fetch the file via GitHub API
Analyze content in the Python sandbox
Report findings with evidence
Example: Review a Private Repository PR

Complete workflow for private repositories:

# Step 1: Extract owner/repo from URL
# URL: https://github.com/myorg/private-repo/pull/42
# owner="myorg", repo="private-repo"

# Step 2: Check if repository is private

## Option A: With GitHub CLI
gh repo view myorg/private-repo --json isPrivate -q '.isPrivate'
# Output: true (it's private!)

## Option B: Without GitHub CLI (using curl)
curl -s -o /dev/null -w "%{http_code}" https://api.github.com/repos/myorg/private-repo
# Output: 404 (likely private or doesn't exist)

# Step 3: Ensure GITHUB_TOKEN is set
echo $GITHUB_TOKEN

## If empty, Option A: Get from GitHub CLI
export GITHUB_TOKEN=$(gh auth token)

## If empty, Option B: Create via web (https://github.com/settings/tokens)
## Then:
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Step 4: Run the review with the token
npx asyncreview review \
  --url https://github.com/myorg/private-repo/pull/42 \
  -q "Does this PR introduce any security vulnerabilities?" \
  --github-token $GITHUB_TOKEN

# Alternative: Token is already in environment, no flag needed
npx asyncreview review \
  --url https://github.com/myorg/private-repo/pull/42 \
  -q "Does this PR introduce any security vulnerabilities?"


If you get a 404 or authentication error: The repository is likely private, and you need to provide GITHUB_TOKEN.

Output formats
Format	Flag	Description
Pretty	(default)	Rich terminal output with boxes
Markdown	--output markdown or -o markdown	Markdown formatted
JSON	--output json or -o json	Machine-readable
Expert Code Review

Use --expert flag for comprehensive PR reviews covering SOLID principles, security, performance, and code quality:

# Full expert review (no question needed)
npx asyncreview review --url <PR_URL> --expert

# Expert review with additional custom question
npx asyncreview review --url <PR_URL> --expert -q "Also check for breaking API changes"


Expert review analyzes:

SOLID Principles - SRP, OCP, LSP, ISP, DIP violations
Security - XSS, injection, auth gaps, race conditions, secrets
Code Quality - Error handling, N+1 queries, boundary conditions
Removal Candidates - Dead code, unused imports

Output includes:

Severity-tagged findings (P0 Critical → P3 Low)
Suggested fixes for P0/P1 issues
Overall assessment: APPROVE / REQUEST_CHANGES / COMMENT
Weekly Installs
76
Repository
asyncfuncai/asyncreview
GitHub Stars
434
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail