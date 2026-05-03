---
title: mole-mac-cleanup
url: https://skills.sh/bjesuiter/skills/mole-mac-cleanup
---

# mole-mac-cleanup

skills/bjesuiter/skills/mole-mac-cleanup
mole-mac-cleanup
Installation
$ npx skills add https://github.com/bjesuiter/skills --skill mole-mac-cleanup
SKILL.md
Mole - Mac Cleanup & Optimization Tool

Repo: https://github.com/tw93/Mole Command: mo (not mole!) Install: brew install mole

Note for humans: mo without params opens an interactive TUI mode. Not useful for agents, but you might wanna try it manually! 😉

What It Does

All-in-one toolkit combining CleanMyMac, AppCleaner, DaisyDisk, and iStat Menus:

Deep cleaning — removes caches, logs, browser leftovers
Smart uninstaller — removes apps + hidden remnants
Disk insights — visualizes usage, manages large files
Live monitoring — real-time system stats
Project artifact purge — cleans node_modules, target, build, etc.
Non-Interactive Commands (Clawd-friendly)
Preview / Dry Run (ALWAYS USE FIRST)
mo clean --dry-run              # Preview cleanup plan
mo clean --dry-run --debug      # Detailed preview with risk levels & file info
mo optimize --dry-run           # Preview optimization actions
mo optimize --dry-run --debug   # Detailed optimization preview

Execute Cleanup
mo clean                        # Run deep cleanup (caches, logs, browser data, trash)
mo clean --debug                # Cleanup with detailed logs

System Optimization
mo optimize                     # Rebuild caches, reset services, refresh Finder/Dock
mo optimize --debug             # With detailed operation logs


What mo optimize does:

Rebuild system databases and clear caches
Reset network services
Refresh Finder and Dock
Clean diagnostic and crash logs
Remove swap files and restart dynamic pager
Rebuild launch services and Spotlight index
Whitelist Management
mo clean --whitelist            # Manage protected cache paths
mo optimize --whitelist         # Manage protected optimization rules

Project Artifact Purge
mo purge                        # Clean old build artifacts (node_modules, target, venv, etc.)
mo purge --paths                # Configure which directories to scan


Config file: ~/.config/mole/purge_paths

Installer Cleanup
mo installer                    # Find/remove .dmg, .pkg, .zip installers


Scans: Downloads, Desktop, Homebrew caches, iCloud, Mail attachments

Setup & Maintenance
mo touchid                      # Configure Touch ID for sudo
mo completion                   # Set up shell tab completion
mo update                       # Update Mole itself
mo remove                       # Uninstall Mole from system
mo --version                    # Show installed version
mo --help                       # Show help

Typical Workflow

Check what would be cleaned:

mo clean --dry-run --debug


If looks good, run cleanup:

mo clean


Optimize system (after cleanup):

mo optimize --dry-run
mo optimize


Clean dev project artifacts:

mo purge

What Gets Cleaned (mo clean)
User app cache
Browser cache (Chrome, Safari, Firefox)
Developer tools (Xcode, Node.js, npm)
System logs and temp files
App-specific cache (Spotify, Dropbox, Slack)
Trash
Notes
Terminal: Best with Ghostty, Alacritty, kitty, WezTerm. iTerm2 has issues.
Safety: Use --dry-run first. Built with strict protections.
Debug: Add --debug for detailed logs.
Weekly Installs
29
Repository
bjesuiter/skills
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail