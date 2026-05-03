---
title: gh-cli
url: https://skills.sh/tenequm/claude-plugins/gh-cli
---

# gh-cli

skills/tenequm/claude-plugins/gh-cli
gh-cli
Installation
$ npx skills add https://github.com/tenequm/claude-plugins --skill gh-cli
SKILL.md
GitHub CLI - Remote Analysis & Discovery

Remote repository operations, codebase comparison, and code discovery without cloning.

When to Use
Analyze repositories without cloning
Compare codebases side-by-side
Fetch specific files from any repo
Find trending repositories and code patterns
Search code across GitHub
Quick Operations
Fetch a file remotely
gh api repos/OWNER/REPO/contents/path/file.ts --template '{{.content | base64decode}}'

Get directory listing
gh api repos/OWNER/REPO/contents/PATH

Search code
gh search code "pattern" --language=typescript

Find trending repos
gh search repos --language=rust --sort stars --order desc

Compare Two Codebases

Systematic workflow for comparing repositories to identify similarities and differences.

Example use: "Compare solana-fm/explorer-kit and tenequm/solana-idls"

Step 1: Fetch directory structures
gh api repos/OWNER-A/REPO-A/contents/PATH
gh api repos/OWNER-B/REPO-B/contents/PATH


If comparing a monorepo package, specify the path (e.g., packages/explorerkit-idls).

Step 2: Compare file lists
gh api repos/OWNER-A/REPO-A/contents/PATH -q '.[].name'
gh api repos/OWNER-B/REPO-B/contents/PATH -q '.[].name'


Compare the output of each command to identify files unique to each repo and common files.

Step 3: Fetch key files for comparison

Compare package dependencies:

gh api repos/OWNER-A/REPO-A/contents/package.json --template '{{.content | base64decode}}'
gh api repos/OWNER-B/REPO-B/contents/package.json --template '{{.content | base64decode}}'


Compare main entry points:

gh api repos/OWNER-A/REPO-A/contents/src/index.ts --template '{{.content | base64decode}}'
gh api repos/OWNER-B/REPO-B/contents/src/index.ts --template '{{.content | base64decode}}'

Step 4: Analyze differences

Compare the fetched files to identify:

API Surface

What functions/classes are exported?
Are the APIs similar or completely different?

Dependencies

Shared dependencies (same approach)
Different dependencies (different implementation)

Unique Features

Features only in repo1
Features only in repo2

For detailed comparison strategies, see references/comparison.md.

Discover Trending Content
Find trending repositories
# Most starred repos
gh search repos --sort stars --order desc --limit 20

# Trending in specific language
gh search repos --language=rust --sort stars --order desc

# Recently popular (created in last month)
gh search repos "created:>2024-10-01" --sort stars --order desc

# Trending in specific topic
gh search repos "topic:machine-learning" --sort stars --order desc

Discover popular code patterns
# Find popular implementations
gh search code "function useWallet" --language=typescript --sort indexed

# Find code in popular repos only
gh search code "implementation" "stars:>1000"

# Search specific organization
gh search code "authentication" --owner=anthropics


For complete discovery queries and patterns, see references/discovery.md.

Search Basics
Code search
# Search across all repositories
gh search code "API endpoint" --language=python

# Search in specific organization
gh search code "auth" --owner=anthropics

# Exclude results with negative qualifiers
gh search issues -- "bug report -label:wontfix"

Issue & PR search
# Find open bugs
gh search issues --label=bug --state=open

# Search assigned issues
gh search issues --assignee=@me --state=open


For advanced search syntax, see references/search.md.

Special Syntax
Field name inconsistencies

IMPORTANT: GitHub CLI uses inconsistent field names across commands:

Field	gh repo view	gh search repos
Stars	stargazerCount	stargazersCount
Forks	forkCount	forksCount

Examples:

# ✅ Correct for gh repo view
gh repo view owner/repo --json stargazerCount,forkCount

# ✅ Correct for gh search repos
gh search repos "query" --json stargazersCount,forksCount

Excluding search results

When using negative qualifiers (like -label:bug), use -- to prevent the hyphen from being interpreted as a flag:

gh search issues -- "query -label:bug"


For more syntax gotchas, see references/syntax.md.

Advanced Workflows

For detailed documentation on specific workflows:

Core Workflows:

remote-analysis.md - Advanced file fetching patterns
comparison.md - Complete codebase comparison guide
discovery.md - All trending and discovery queries
search.md - Advanced search syntax
syntax.md - Special syntax and command quirks

GitHub Operations:

repositories.md - Repository operations
pull_requests.md - PR workflows
issues.md - Issue management
actions.md - GitHub Actions
releases.md - Release management

Setup & Configuration:

getting_started.md - Installation and auth
other.md - Environment variables, aliases, config
extensions.md - CLI extensions
Resources
Official docs: https://cli.github.com/manual/
GitHub CLI: https://github.com/cli/cli
Search syntax: https://docs.github.com/en/search-github
Weekly Installs
42
Repository
tenequm/claude-plugins
GitHub Stars
25
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn