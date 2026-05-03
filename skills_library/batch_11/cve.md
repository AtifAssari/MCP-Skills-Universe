---
title: cve
url: https://skills.sh/fullykubed/nixos-config/cve
---

# cve

skills/fullykubed/nixos-config/CVE
CVE
Installation
$ npx skills add https://github.com/fullykubed/nixos-config --skill CVE
SKILL.md

You manage CVE vulnerabilities through their complete lifecycle in a NixOS system. Based on the user's request, you will select and follow the appropriate workflow.

When Invoked

Gather Context: Determine the current state:

Has a vulnix scan been run recently?
Is the user asking about a specific CVE?
Are there existing patches to review?

Determine Intent: Analyze the user's request to identify:

Are they looking to find new vulnerabilities?
Do they have a specific CVE to fix?
Do they want to review existing patches?
Look for trigger words from the Workflow Routing table

Select Workflow: Select the appropriate workflow based on the user's intent and trigger words:

Does the user want to find vulnerabilities? → IdentifyCVE
Does the user have a specific CVE to fix? → ResolveCVE
Does the user want to review existing patches? → ReviewPatches
When in doubt: Ask the user which workflow they want to use

Execute Workflow: Report to the user "Running using the CVE skill..." You MUST read the workflow document completely before proceeding, then follow the workflow's process completely

Report Results: Summarize what was accomplished and suggest next steps

Workflow Routing
Workflow	Trigger Words	When to Use
IdentifyCVE	"scan", "check", "find", "detect", "identify", "triage", "vulnerabilities", "run vulnix"	User wants to scan their system and identify real CVE vulnerabilities (includes triaging false positives)
ResolveCVE	"fix", "patch", "resolve", "whitelist", "apply", "mitigate", "CVE-XXXX-XXXXX"	User has a specific CVE they want to fix via patch or whitelist
ReviewPatches	"review", "audit", "check patches", "verify", "existing patches", "patch status"	User wants to review existing CVE patches in the repository
File Structure
<repo>/
├── modules/
│   ├── patches/
│   │   ├── default.nix                      # Imports all per-package submodules
│   │   └── <package>/
│   │       ├── default.nix                  # NixOS module with overlay (nixpkgs, nixpkgs-unstable, or both)
│   │       └── CVE-XXXX-XXXXX.patch         # Individual patch files
│   └── common/
│       ├── stdenv/default.nix               # Custom stdenv hardening (applied to both nixpkgs sets)
│       └── vulnix-scanner/
│           ├── default.nix                  # Vulnix scanner service + wrapper
│           └── whitelist.toml               # CVE whitelist (auto-applied)
└── flake.nix                                # Imports modules

Whitelist

The system vulnix command is wrapped to automatically apply the whitelist. No need to pass -w manually - just run vulnix --system and whitelisted CVEs are filtered out.

Whitelist Organization (REQUIRED)

The whitelist file MUST be organized into clearly labeled sections:

Section	Contents
HASKELL ECOSYSTEM	Package name collisions with C/Rust/JS libs
JENKINS PLUGIN COLLISIONS	Jenkins plugins vs CLI tools
VS CODE EXTENSION COLLISIONS	VS Code extensions vs CLI tools
DIFFERENT SOFTWARE - SAME NAME	Unrelated software sharing names
PLATFORM/DISTRO SPECIFIC	CVEs for other platforms/distros
ALREADY PATCHED VERSIONS	CVEs fixed in installed versions
EOL/LEGACY SOFTWARE	Accepted risk for EOL dependencies
BUNDLED DEPENDENCIES	Older libs bundled in other packages

When adding whitelist entries:

Add to the correct section (create if needed)
Document what top-level package pulls in the dependency
Include version info and what the CVE actually affects
Set until dates for accepted risks
Quick Reference
CVSS Priority Levels
Score	Severity	Priority
9.0-10.0	Critical	Immediate
7.0-8.9	High	High
4.0-6.9	Medium	Moderate
0.1-3.9	Low	Low
Common False Positive Patterns
Pattern	Example	Why It's False
Haskell vs other	curl-0.4.46 (Haskell)	Different software, same name
Distro-specific	"Debian avahi package"	NixOS uses upstream
Platform-specific	"Discord macOS"	Linux version differs
Already fixed	Fixed in "2.4.2", have 2.4.16	Version already patched
Weekly Installs
16
Repository
fullykubed/nixos-config
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn