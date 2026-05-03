---
title: ezbookkeeping
url: https://skills.sh/mayswind/ezbookkeeping/ezbookkeeping
---

# ezbookkeeping

skills/mayswind/ezbookkeeping/ezbookkeeping
ezbookkeeping
Installation
$ npx skills add https://github.com/mayswind/ezbookkeeping --skill ezbookkeeping
SKILL.md
ezBookkeeping API Tools
Usage
List all supported commands

Linux / macOS

sh scripts/ebktools.sh list


Windows

scripts\ebktools.ps1 list

Show help for a specific command

Linux / macOS

sh scripts/ebktools.sh help <command>


Windows

scripts\ebktools.ps1 help <command>

Call API

Linux / macOS

sh scripts/ebktools.sh [global-options] <command> [command-options]


Windows

scripts\ebktools.ps1 [global-options] <command> [command-options]

Troubleshooting

If the script reports that the environment variable EBKTOOL_SERVER_BASEURL or EBKTOOL_TOKEN is not set, user can define them as system environment variables, or create a .env file in the user home directory that contains these two variables and place it there.

The meanings of these environment variables are as follows:

Variable	Required	Description
EBKTOOL_SERVER_BASEURL	Required	ezBookkeeping server base URL (e.g., http://localhost:8080)
EBKTOOL_TOKEN	Required	ezBookkeeping API token
Reference

ezBookkeeping: https://ezbookkeeping.mayswind.net

Weekly Installs
32
Repository
mayswind/ezbookkeeping
GitHub Stars
4.7K
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass