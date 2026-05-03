---
title: terminal-docs
url: https://skills.sh/mwguerra/claude-code-plugins/terminal-docs
---

# terminal-docs

skills/mwguerra/claude-code-plugins/terminal-docs
terminal-docs
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill terminal-docs
SKILL.md
Terminal Documentation Reference Skill
Overview

This skill provides access to comprehensive terminal and shell systems documentation. Use this skill to look up exact configurations, code patterns, and best practices for terminal-related development.

Documentation Location

All documentation is stored in: /home/mwguerra/projects/mwguerra/claude-code-plugins/terminal-specialist/skills/terminal-docs/references/

Directory Structure
references/
├── 01-fundamentals.md      # TTY/PTY concepts, terminal stack, device files
├── 02-streams.md           # stdin, stdout, stderr, buffering behavior
├── 03-exit-codes.md        # Exit status, POSIX codes, signal exits
├── 04-shells.md            # Shell types, startup files, options
├── 05-dimensions.md        # Terminal size, SIGWINCH, resize handling
├── 06-modes.md             # Canonical/raw mode, termios flags
├── 07-job-control.md       # Sessions, process groups, background jobs
├── 08-environment.md       # TERM, PATH, locale, prompt variables
├── 09-signals.md           # Signal handling, keyboard signals
├── 10-escape-sequences.md  # ANSI codes, colors, cursor control
├── 11-redirection.md       # Pipes, file descriptors, here docs
├── 12-windows.md           # Windows console, ConPTY, PowerShell
├── 13-cross-platform.md    # Portable patterns, platform differences
└── 14-advanced.md          # tmux, screen, recording, graphics

Usage
When to Use This Skill
Before implementing terminal-related functionality
When debugging I/O or stream issues
To verify correct escape sequence syntax
To understand terminal mode behavior
For signal handling patterns
For cross-platform compatibility guidance
Search Workflow
Identify Topic: Determine what documentation is needed
Navigate to File: Go to relevant documentation file
Read Documentation: Extract exact patterns
Apply Knowledge: Use in implementation
Common Lookups
Topic	File
Terminal architecture	01-fundamentals.md
Stream buffering	02-streams.md
Exit codes	03-exit-codes.md
Shell configuration	04-shells.md
Terminal size	05-dimensions.md
Raw mode	06-modes.md
Job control	07-job-control.md
Environment variables	08-environment.md
Signal handling	09-signals.md
ANSI escape codes	10-escape-sequences.md
Pipes and redirection	11-redirection.md
Windows console	12-windows.md
Cross-platform	13-cross-platform.md
Multiplexers	14-advanced.md
Documentation Reading Pattern

When reading documentation:

Find the right file: Match topic to documentation file
Read the overview: Understand the concept
Extract code examples: Copy exact patterns
Note platform specifics: Consider Unix/Windows differences
Check best practices: Apply safety and portability tips
Example Usage
Looking up ANSI Color Codes
Navigate to 10-escape-sequences.md
Find Colors section
Extract:
4-bit color codes (30-37, 40-47)
256-color format
True color format
tput commands
Looking up Signal Handling
Navigate to 09-signals.md
Find relevant section (Bash, C, Python)
Extract:
Signal handler setup
Signal-safe patterns
Cleanup handlers
Looking up Cross-Platform Input
Navigate to 13-cross-platform.md
Find Key Input section
Extract:
Unix termios pattern
Windows msvcrt pattern
Platform detection code
Output

After reading documentation, provide:

Exact code pattern from docs
Platform considerations
Best practices noted
Safety/security notes
Alternative approaches if applicable
Weekly Installs
18
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass