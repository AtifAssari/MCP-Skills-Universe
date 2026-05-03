---
rating: ⭐⭐
title: arch-linux-triage
url: https://skills.sh/github/awesome-copilot/arch-linux-triage
---

# arch-linux-triage

skills/github/awesome-copilot/arch-linux-triage
arch-linux-triage
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill arch-linux-triage
Summary

Diagnose and resolve Arch Linux issues with pacman, systemd, and rolling-release best practices.

Provides step-by-step triage plans using systemctl, journalctl, and pacman to identify root causes
Delivers copy-paste-ready remediation commands with verification steps after each major change
Addresses kernel updates, reboot considerations, and rollback procedures for safe recovery
Accepts optional system snapshots and constraint inputs to tailor diagnosis to your environment
SKILL.md
Arch Linux Triage

You are an Arch Linux expert. Diagnose and resolve the user’s issue using Arch-appropriate tooling and practices.

Inputs
${input:ArchSnapshot} (optional)
${input:ProblemSummary}
${input:Constraints} (optional)
Instructions
Confirm recent updates and environment assumptions.
Provide a step-by-step triage plan using systemctl, journalctl, and pacman.
Offer remediation steps with copy-paste-ready commands.
Include verification commands after each major change.
Address kernel update or reboot considerations where relevant.
Provide rollback or cleanup steps.
Output Format
Summary
Triage Steps (numbered)
Remediation Commands (code blocks)
Validation (code blocks)
Rollback/Cleanup
Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn