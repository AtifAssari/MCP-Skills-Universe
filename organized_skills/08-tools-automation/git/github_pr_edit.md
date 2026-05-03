---
rating: ⭐⭐
title: github-pr-edit
url: https://skills.sh/yiyousiow000814/xauusd-calendar-agent/github-pr-edit
---

# github-pr-edit

skills/yiyousiow000814/xauusd-calendar-agent/github-pr-edit
github-pr-edit
Installation
$ npx skills add https://github.com/yiyousiow000814/xauusd-calendar-agent --skill github-pr-edit
SKILL.md
GitHub PR Edit (Title/Body/Comments)

Edit PR title/body/comments on Windows. Use gh when available; otherwise use the GitHub REST API.

Before You Start
Identify:
owner and repo (e.g. yiyousiow000814/XAUUSD-Calendar-Agent)
PR number (e.g. 111)
If using gh, confirm it is available and authenticated:
gh --version
gh auth status

If the repo is private, unauthenticated GitHub API requests often return 404 Not Found. Treat 404 as “likely unauthorized” unless you are sure the repo/PR does not exist.
Option A (Preferred): GitHub CLI (gh)

If gh is installed and authenticated:

# Update title and body (use stdin/body-file to avoid literal \n issues)
@'
<markdown body>
'@ | gh pr edit 111 --title "chore: ..." --body-file -


Add a comment:

@'
Summary:
- ...
'@ | gh pr comment 111 --body-file -

Option B: GitHub REST API (PowerShell, no gh)
1) Get an auth token (do not print it)

Preferred sources (pick the first available):

$env:GITHUB_TOKEN or $env:GH_TOKEN
Reuse the credential Git already has (works if you previously authenticated with a PAT):
$cred = "protocol=https`nhost=github.com`n`n" | git credential fill
$token = (($cred | Select-String -Pattern '^password=').Line).Substring(9)


Do not Write-Host $token, do not log headers.

2) Build headers (minimal)
$headers = @{
  Authorization = "token $token"
  'User-Agent'  = 'codex-cli'
  Accept        = 'application/vnd.github+json'
}

3) Sanity check auth (useful when you see 404)
Invoke-RestMethod -Method Get -Uri "https://api.github.com/repos/<owner>/<repo>" -Headers $headers |
  Select-Object full_name, private


If this fails with 404, your token likely lacks access.

4) Update PR title/body

Use UTF-8 bytes for reliable encoding (Chinese text, punctuation).

$payload = @{
  title = 'chore: ...'
  body  = @"
Summary:
- ...
"@
} | ConvertTo-Json -Depth 5

$bytes = [System.Text.Encoding]::UTF8.GetBytes($payload)

Invoke-RestMethod -Method Patch `
  -Uri "https://api.github.com/repos/<owner>/<repo>/pulls/<number>" `
  -Headers $headers `
  -ContentType 'application/json; charset=utf-8' `
  -Body $bytes

5) Add a PR comment (optional)

PR comments are issue comments:

$payload = @{ body = "Summary:`n- ..." } | ConvertTo-Json -Depth 5
$bytes = [System.Text.Encoding]::UTF8.GetBytes($payload)

Invoke-RestMethod -Method Post `
  -Uri "https://api.github.com/repos/<owner>/<repo>/issues/<number>/comments" `
  -Headers $headers `
  -ContentType 'application/json; charset=utf-8' `
  -Body $bytes

Deterministic Helper Script (Recommended)

Use the bundled script for fewer quoting/encoding mistakes:

.codex/skills/github-pr-edit/scripts/patch_pr.ps1
Weekly Installs
40
Repository
yiyousiow000814…ar-agent
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass