---
rating: ⭐⭐⭐
title: publishing-wpf-apps
url: https://skills.sh/christian289/dotnet-with-claudecode/publishing-wpf-apps
---

# publishing-wpf-apps

skills/christian289/dotnet-with-claudecode/publishing-wpf-apps
publishing-wpf-apps
Installation
$ npx skills add https://github.com/christian289/dotnet-with-claudecode --skill publishing-wpf-apps
SKILL.md
WPF Application Publishing Guide

When publishing WPF applications, ask the user about deployment and installer preferences.

Ask User: Deployment Method

Which deployment method do you need?

Framework-Dependent - Small size (~1MB), requires .NET runtime
Self-Contained - Includes runtime (150-200MB), no dependencies
Single-File - One executable (50-80MB compressed)
Ask User: Installer Technology

Which installer/update technology do you prefer?

Velopack (Recommended) - Modern, fast updates, delta updates
MSIX - Windows Store, enterprise deployment
NSIS - Traditional installer, full control
Inno Setup - Simple, widely used
None - Portable/xcopy deployment
Quick Reference
Deployment Methods
Method	Size	Startup	Requirements
Framework-Dependent	~1MB	Fast	.NET runtime
Self-Contained	150-200MB	Fast	None
Single-File	150-200MB	Medium	None
Single-File + Compressed	50-80MB	Slower	None
Installer Technologies
Technology	Auto-Update	Delta Updates	Store	Complexity
Velopack	✅	✅	❌	Low
MSIX	✅	✅	✅	Medium
NSIS	Manual	❌	❌	High
Inno Setup	Manual	❌	❌	Medium
WPF Limitations

⚠️ PublishTrimmed: Not supported (reflection-heavy) ⚠️ PublishAot: Not supported (WPF incompatible)

Basic Commands
# Framework-Dependent
dotnet publish -c Release

# Self-Contained
dotnet publish -c Release -r win-x64 --self-contained true

# Single-File (WPF)
dotnet publish -c Release -r win-x64 --self-contained true \
  -p:PublishSingleFile=true \
  -p:IncludeNativeLibrariesForSelfExtract=true

Additional Resources
WPF Single-File: See WPF-SINGLE-FILE.md
Size Optimization: See SIZE-OPTIMIZATION.md
Installer Options: See INSTALLERS.md
Weekly Installs
14
Repository
christian289/do…audecode
GitHub Stars
28
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass