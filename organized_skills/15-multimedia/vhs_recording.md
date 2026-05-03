---
rating: ⭐⭐⭐
title: vhs-recording
url: https://skills.sh/athola/claude-night-market/vhs-recording
---

# vhs-recording

skills/athola/claude-night-market/vhs-recording
vhs-recording
Installation
$ npx skills add https://github.com/athola/claude-night-market --skill vhs-recording
SKILL.md
VHS Recording Skill

Generate professional terminal recordings from VHS tape files.

When To Use
Recording terminal sessions with VHS tape scripts
Creating terminal demo recordings for documentation
When NOT To Use
Browser-based workflows - use scry:browser-recording instead
Non-terminal demos or GUI applications
Overview

VHS converts declarative tape files into animated GIFs of terminal sessions. Tape files define commands, timing, and terminal appearance.

Required TodoWrite Items
- Locate and validate tape file
- Check VHS installation status
- Execute VHS recording
- Verify output GIF creation

Module Reference
See modules/tape-syntax.md for VHS tape file directives
See modules/execution.md for recording workflow details
Workflow
Phase 1: Validate Tape File
Confirm tape file exists at specified path
Read tape file contents
Verify required directives:
Output directive specifies GIF destination
At least one action command (Type, Enter, etc.)
Phase 2: Check VHS Installation
which vhs && vhs --version


If not installed:

# Linux/WSL
go install github.com/charmbracelet/vhs@latest

# macOS
brew install charmbracelet/tap/vhs

# Also requires ttyd and ffmpeg

Phase 3: Execute Recording
vhs <tape-file.tape>


VHS will:

Parse tape file directives
Launch virtual terminal (ttyd)
Execute commands with timing
Capture frames
Encode to GIF using ffmpeg
Phase 4: Verify Output
Check GIF file exists at Output path
Verify file size is non-zero
Report success with output location
Exit Criteria
GIF file created at specified Output path
File size indicates successful recording (typically >50KB)
No error messages from VHS execution
Troubleshooting
Common Issues

If vhs is not found, verify that your Go bin directory is in your PATH (typically ~/go/bin). If the recording fails to start, ensure ttyd and ffmpeg are installed, as VHS depends on them for terminal emulation and video encoding. For "permission denied" errors when writing the GIF, check that the output directory exists and is writable.

Weekly Installs
28
Repository
athola/claude-n…t-market
GitHub Stars
265
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass