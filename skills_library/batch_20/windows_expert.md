---
title: windows-expert
url: https://skills.sh/jackspace/claudeskillz/windows-expert
---

# windows-expert

skills/jackspace/claudeskillz/windows-expert
windows-expert
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill windows-expert
SKILL.md
Windows-expert
Instructions

When helping with Windows-related tasks:

Use /mnt/c/ paths for Windows drives in WSL
Use wslpath for path conversion: wslpath -w (Linux to Windows), wslpath -u (Windows to Linux)
Windows executables can be called from WSL: cmd.exe, powershell.exe, *.exe
Be aware of file permissions and line ending differences (CRLF vs LF)
Provide PowerShell examples alongside bash when relevant
Use modern PowerShell conventions (cmdlets, pipelines)
Suggest PowerShell Core (pwsh) for cross-platform scripts
Help with Registry operations (Get-ItemProperty, Set-ItemProperty)
Windows Services management
Task Scheduler for automation
Windows networking (netsh, Get-NetAdapter)
NTFS permissions and ACLs
Path length limitations (260 char limit)
Case sensitivity differences
Drive letter handling
Windows Defender/Firewall interactions
WSL2 networking quirks (bridge mode, port forwarding)
Examples

Add examples of how to use this skill here.

Notes
This skill was auto-generated
Edit this file to customize behavior
Weekly Installs
104
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn