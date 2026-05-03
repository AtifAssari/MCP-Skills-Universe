---
title: atlassian-cli
url: https://skills.sh/onnokh/atlassian-cli/atlassian-cli
---

# atlassian-cli

skills/onnokh/atlassian-cli/atlassian-cli
atlassian-cli
Installation
$ npx skills add https://github.com/onnokh/atlassian-cli --skill atlassian-cli
SKILL.md
Atlassian CLI (acli)

Use acli to automate and operate Atlassian Cloud workflows from the terminal (Jira, Admin, and Rovo Dev).

Workflow
Install or upgrade acli (pick the OS-specific path).
Authenticate (pick token vs OAuth vs admin API key).
Discover the exact command/flags via acli help ... and --help.
Prefer machine-readable output (--json) for automation; parse with jq.
Handle bulk operations with --ignore-errors where appropriate; capture trace IDs on unexpected errors.
Decision Tree
Install / Upgrade
Which OS?
  macOS:
    - Preferred: Homebrew
    - Fallback: download binary + put on PATH
  Linux:
    - Preferred: apt (Debian/Ubuntu) or yum (RHEL/CentOS)
    - Fallback: download binary to /usr/local/bin or ~/.local/bin
  Windows:
    - Download acli.exe via PowerShell (Invoke-WebRequest)
Upgrade:
  - Homebrew: brew upgrade acli
  - apt/yum: upgrade package
  - binary installs: re-download and replace


Read references/install.md for exact commands.

Authenticate
What are you trying to access?
  Jira Cloud:
    - API token (non-interactive, CI-friendly)
    - OAuth (interactive): acli jira auth login --web
  Atlassian Admin (org admin):
    - API key (admin commands)
  Rovo Dev:
    - API token login, then: acli rovodev run


Read references/auth.md for exact login commands.

Secrets Handling (Do This By Default)
Avoid putting tokens/keys directly in the command line.
Prefer stdin from a secret store/CI secret variable.
Never print tokens/keys into logs, diffs, or chat transcripts.
Command Discovery Pattern
Show top-level help: acli --help
Show product help: acli jira --help, acli admin --help, acli rovodev --help
Show deep help: acli jira workitem create --help
Use acli help [path] when unsure where a command lives.
Automation Patterns
Chain commands with && when later steps must only run on success.
Redirect tabular output (--csv) to files.
Use --json | jq ... to extract specific fields.

Read references/automation.md.

Shell Completion

Enable completion for bash/zsh/fish/powershell.

Read references/shell-completion.md.

Troubleshooting
Capture trace IDs from unexpected errors for support tickets.
Use --ignore-errors for bulk operations where partial success is acceptable.
Use --generate-input-json / --generate-json on commands that support JSON-driven workflows.

Read references/troubleshooting.md.

References
references/install.md
references/auth.md
references/automation.md
references/shell-completion.md
references/troubleshooting.md
Weekly Installs
128
Repository
onnokh/atlassian-cli
GitHub Stars
2
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass