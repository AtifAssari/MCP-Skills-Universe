---
rating: ⭐⭐
title: ffind
url: https://skills.sh/brownfinesecurity/iothackbot/ffind
---

# ffind

skills/brownfinesecurity/iothackbot/ffind
ffind
Installation
$ npx skills add https://github.com/brownfinesecurity/iothackbot --skill ffind
SKILL.md
Ffind - Advanced File Finder with Extraction

You are helping the user find and analyze files with advanced type detection and optional filesystem extraction capabilities using the ffind tool.

Tool Overview

Ffind analyzes files and directories, identifies file types, and can extract filesystems (ext2/3/4, F2FS) for deeper analysis. It's designed for firmware and IoT device analysis.

Instructions

When the user asks to analyze files, find specific file types, or extract filesystems:

Understand the target:

Ask what path(s) they want to analyze
Determine if they want to extract filesystems or just analyze
Ask if they want all file types or just artifact types

Execute the analysis:

Use the ffind command from the iothackbot bin directory
Basic usage: ffind <path> [<path2> ...]
To extract filesystems: ffind <path> -e
Custom extraction directory: ffind <path> -e -d /path/to/output
Show all file types: ffind <path> -a
Verbose output: ffind <path> -v

Output formats:

--format text (default): Human-readable colored output with type summaries
--format json: Machine-readable JSON
--format quiet: Minimal output

Extraction capabilities:

Supports ext2/ext3/ext4 filesystems (requires e2fsprogs)
Supports F2FS filesystems (requires f2fs-tools)
Requires sudo privileges for extraction
Default extraction location: /tmp/ffind_<timestamp>
Examples

Analyze a firmware file to see file types:

ffind /path/to/firmware.bin


Extract all filesystems from a firmware image:

sudo ffind /path/to/firmware.bin -e


Analyze multiple files and show all types:

ffind /path/to/file1.bin /path/to/file2.bin -a


Extract to a custom directory:

sudo ffind /path/to/firmware.bin -e -d /tmp/my-extraction

Important Notes
Extraction requires root/sudo privileges
Requires external tools: e2fsprogs, f2fs-tools, util-linux
Identifies "artifact" file types relevant to security analysis by default
Use -a flag to see all file types including common formats
Weekly Installs
20
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