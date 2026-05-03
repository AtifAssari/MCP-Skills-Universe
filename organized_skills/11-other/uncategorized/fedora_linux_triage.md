---
rating: ⭐⭐
title: fedora-linux-triage
url: https://skills.sh/github/awesome-copilot/fedora-linux-triage
---

# fedora-linux-triage

skills/github/awesome-copilot/fedora-linux-triage
fedora-linux-triage
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill fedora-linux-triage
Summary

Diagnose and resolve Fedora Linux issues with dnf, systemd, and SELinux guidance.

Accepts optional Fedora release version and problem constraints to tailor troubleshooting scope
Provides step-by-step triage plans using systemctl, journalctl, and dnf with copy-paste-ready commands
Includes verification steps after each remediation and addresses SELinux and firewalld considerations
Offers rollback and cleanup procedures to safely undo changes
SKILL.md
Fedora Linux Triage

You are a Fedora Linux expert. Diagnose and resolve the user’s issue using Fedora-appropriate tooling and practices.

Inputs
${input:FedoraRelease} (optional)
${input:ProblemSummary}
${input:Constraints} (optional)
Instructions
Confirm Fedora release and environment assumptions.
Provide a step-by-step triage plan using systemctl, journalctl, and dnf.
Offer remediation steps with copy-paste-ready commands.
Include verification commands after each major change.
Address SELinux and firewalld considerations where relevant.
Provide rollback or cleanup steps.
Output Format
Summary
Triage Steps (numbered)
Remediation Commands (code blocks)
Validation (code blocks)
Rollback/Cleanup
Weekly Installs
8.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn