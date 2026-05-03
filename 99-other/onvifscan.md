---
title: onvifscan
url: https://skills.sh/brownfinesecurity/iothackbot/onvifscan
---

# onvifscan

skills/brownfinesecurity/iothackbot/onvifscan
onvifscan
Installation
$ npx skills add https://github.com/brownfinesecurity/iothackbot --skill onvifscan
SKILL.md
Onvifscan - ONVIF Security Scanner

You are helping the user scan ONVIF devices for security issues including authentication bypasses and weak credentials using the onvifscan tool.

Tool Overview

Onvifscan is an ONVIF device security scanner that can:

Test for unauthenticated access to ONVIF endpoints
Perform credential brute-forcing attacks
Instructions

When the user asks to scan ONVIF devices, test IP cameras, or assess IoT device security:

Determine scan type:

auth: Authentication and access control testing (recommended to start)
brute: Credential brute-forcing on password-protected endpoints

Get target information:

Ask for the device URL/IP
Determine which scan type to run
Check if they have custom wordlists

Execute the scan:

Use the onvifscan command from the iothackbot bin directory
Format: onvifscan <subcommand> <url> [options]
Subcommands
Auth Scan

Tests ONVIF endpoints for authentication requirements:

onvifscan auth http://192.168.1.100


Options:

-v, --verbose: Show full XML responses
-a, --all: Test ALL endpoints including potentially destructive ones
--format text|json|quiet: Output format
Brute Force

Attempts credential brute-forcing on protected endpoints:

onvifscan brute http://192.168.1.100


Options:

--usernames <file>: Custom usernames wordlist (default: built-in onvif-usernames.txt)
--passwords <file>: Custom passwords wordlist (default: built-in onvif-passwords.txt)
--format text|json|quiet: Output format
Examples

Quick auth check on a device:

onvifscan auth 192.168.1.100


Auth check with verbose output:

onvifscan auth http://192.168.1.100:8080 -v


Brute force with custom wordlists:

onvifscan brute 192.168.1.100 --usernames custom-users.txt --passwords custom-pass.txt

Important Notes
URLs can omit http:// - it will be added automatically
Auth scan is non-destructive and safe to run
Use -a flag with caution - may test destructive endpoints
Brute force is rate-limited to prevent device overload (max 20 attempts by default)
Built-in wordlists located in wordlists/ directory
Weekly Installs
22
Repository
brownfinesecuri…thackbot
GitHub Stars
746
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn