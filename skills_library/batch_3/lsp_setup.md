---
title: lsp-setup
url: https://skills.sh/github/awesome-copilot/lsp-setup
---

# lsp-setup

skills/github/awesome-copilot/lsp-setup
lsp-setup
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill lsp-setup
SKILL.md
LSP Setup for GitHub Copilot CLI

UTILITY SKILL — installs and configures Language Server Protocol servers for Copilot CLI. USE FOR: "setup LSP", "install language server", "configure LSP for Java", "add TypeScript LSP", "enable code intelligence", "I need go-to-definition", "find references not working", "need better code understanding" DO NOT USE FOR: general coding tasks, IDE/editor LSP configuration, non-Copilot-CLI setups

Workflow
Ask the language — use ask_user to ask which programming language(s) the user wants LSP support for
Detect the OS — run uname -s (or check for Windows via $env:OS / %OS%) to determine macOS, Linux, or Windows
Look up the LSP server — read references/lsp-servers.md for known servers, install commands, and config snippets
Ask scope — use ask_user to ask whether the config should be user-level (~/.copilot/lsp-config.json) or repo-level (lsp.json at the repo root or .github/lsp.json)
Install the server — run the appropriate install command for the detected OS
Write the config — merge the new server entry into the chosen config file (~/.copilot/lsp-config.json for user-level; lsp.json or .github/lsp.json for repo-level). If a repo-level config already exists, keep using that location; otherwise ask the user which repo-level location they prefer. Create the file if missing and preserve existing entries.
Verify — confirm the LSP binary is on $PATH and the config file is valid JSON
Configuration Format

Copilot CLI reads LSP configuration from user-level or repo-level locations, and repo-level config takes precedence over user-level config:

User-level: ~/.copilot/lsp-config.json
Repo-level: lsp.json (repo root) or .github/lsp.json

The JSON structure:

{
  "lspServers": {
    "<server-key>": {
      "command": "<binary>",
      "args": ["--stdio"],
      "fileExtensions": {
        ".<ext>": "<languageId>",
        ".<ext2>": "<languageId>"
      }
    }
  }
}

Key rules
command is the binary name (must be on $PATH) or an absolute path.
args almost always includes "--stdio" to use standard I/O transport.
fileExtensions maps each file extension (with leading dot) to a Language ID.
Multiple servers can coexist in lspServers.
When merging into an existing file, never overwrite other server entries — only add or update the target language key.
Behavior
Always use ask_user with choices when asking the user to pick a language or scope.
If the language is not listed in references/lsp-servers.md, search the web for " LSP server" and guide the user through manual configuration.
If a package manager is not available (e.g. no Homebrew on macOS), suggest alternative install methods from the reference file.
After installation, run which <binary> (or where.exe on Windows) to confirm the binary is accessible.
Show the user the final config JSON before writing it.
If the config file already exists, read it first and merge — do not clobber.
Verification

After setup, tell the user:

Type /exit to quit Copilot CLI — this is required so the new LSP configuration is loaded on next launch
Re-launch copilot in a project with files of the configured language
Run /lsp to check the server status
Try code intelligence features like go-to-definition or hover
Weekly Installs
537
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn