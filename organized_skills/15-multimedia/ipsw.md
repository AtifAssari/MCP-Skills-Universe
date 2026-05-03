---
rating: ⭐⭐⭐
title: ipsw
url: https://skills.sh/blacktop/ipsw-skill/ipsw
---

# ipsw

skills/blacktop/ipsw-skill/ipsw
ipsw
Installation
$ npx skills add https://github.com/blacktop/ipsw-skill --skill ipsw
SKILL.md
IPSW - Apple Reverse Engineering Toolkit

Install: brew install blacktop/tap/ipsw

Choose Your Workflow
Goal	Start Here
Download/extract firmware	Firmware Acquisition
Reverse engineer userspace	Userspace RE
Analyze kernel/KEXTs	Kernel Analysis
Research entitlements	Entitlements
Dump private API headers	Class Dump
Analyze standalone binary	Mach-O Analysis
Firmware Acquisition
# Download latest IPSW for device
ipsw download ipsw --device iPhone16,1 --latest

# Download with automatic kernel/DSC extraction
ipsw download ipsw --device iPhone16,1 --latest --kernel --dyld

# Extract components from local IPSW
ipsw extract --kernel iPhone16,1_18.0_Restore.ipsw
ipsw extract --dyld --dyld-arch arm64e iPhone16,1_18.0_Restore.ipsw

# Remote extraction (no full download)
ipsw extract --kernel --remote <IPSW_URL>


See references/download.md for device identifiers and advanced options.

Userspace RE (dyld_shared_cache)

macOS DSC: /System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld/dyld_shared_cache_arm64e

Essential Commands
Command	Purpose
dyld a2s <DSC> <ADDR>	Address → symbol (triage crash LR/PC)
dyld symaddr <DSC> <SYM> --image <DYLIB>	Symbol → address
dyld disass <DSC> --vaddr <ADDR>	Disassemble at address
dyld disass <DSC> --symbol <SYM> --image <DYLIB>	Disassemble by symbol
dyld xref <DSC> <ADDR> --all	Find all references to address
dyld dump <DSC> <ADDR> --size 256	Dump raw bytes at address
dyld str <DSC> "pattern" --image <DYLIB>	Search strings
dyld objc --class <DSC> --image <DYLIB>	List ObjC classes
dyld extract <DSC> <DYLIB> -o ./out/	Extract dylib for external tools
Common Workflow
# 1. Resolve address from crash/trace
ipsw dyld a2s $DSC 0x1bc39e1e0
# → -[SomeClass someMethod:] + 0x40

# 2. Disassemble around that address
ipsw dyld disass $DSC --vaddr 0x1bc39e1e0

# 3. Find who calls this function
ipsw dyld xref $DSC 0x1bc39e1a0 --all

# 4. Extract string/data referenced in disassembly
ipsw dyld dump $DSC 0x1bc39e200 --size 64


Tip: Always use --image <DYLIB> - it's 10x+ faster.

See references/dyld.md for complete DSC commands.

Kernel Analysis
# List all KEXTs
ipsw kernel kexts kernelcache.release.iPhone16,1

# Extract specific KEXT
ipsw kernel extract kernelcache sandbox --output ./kexts/

# Dump syscalls
ipsw kernel syscall kernelcache

# Diff KEXTs between versions
ipsw kernel kexts --diff kernelcache_17.0 kernelcache_18.0


See references/kernel.md for KEXT extraction and kernel analysis.

Entitlements
# Single binary entitlements
ipsw macho info --ent /path/to/binary

# Build searchable database from IPSW
ipsw ent --sqlite ent.db --ipsw iOS18.ipsw

# Query database
ipsw ent --sqlite ent.db --key "com.apple.private.security.no-sandbox"
ipsw ent --sqlite ent.db --key "platform-application"
ipsw ent --sqlite ent.db --key "com.apple.private.tcc.manager"


See references/entitlements.md for common entitlements and query patterns.

Class Dump

Dump Objective-C headers from binaries or dyld_shared_cache:

# Dump all headers from framework in DSC
ipsw class-dump $DSC SpringBoardServices --headers -o ./headers/

# Dump specific class
ipsw class-dump $DSC Security --class SecKey

# Filter by pattern
ipsw class-dump $DSC UIKit --class 'UIApplication.*' --headers -o ./headers/

# Include runtime addresses (for hooking)
ipsw class-dump $DSC Security --re


See references/class-dump.md for filtering and output options.

Mach-O Analysis
# Full binary info
ipsw macho info /path/to/binary

# Disassemble function
ipsw macho disass /path/to/binary --symbol _main

# Get entitlements and signature
ipsw macho info --ent /path/to/binary
ipsw macho info --sig /path/to/binary


See references/macho.md for complete Mach-O commands.

Reference Files
references/download.md - Firmware download, device IDs, extraction
references/dyld.md - Complete DSC commands (a2s, xref, dump, str, extract)
references/kernel.md - Kernel and KEXT analysis
references/entitlements.md - Entitlements database and queries
references/class-dump.md - ObjC header dumping
references/macho.md - Mach-O binary analysis
Tips
Symbol caching: First a2s/symaddr creates .a2s cache - subsequent lookups are instant
Use --image flag: Specifying dylib is 10x+ faster for DSC operations
JSON output: Most commands support --json for scripting
Device IDs: Use ipsw device-list to find device identifiers
Weekly Installs
78
Repository
blacktop/ipsw-skill
GitHub Stars
53
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn