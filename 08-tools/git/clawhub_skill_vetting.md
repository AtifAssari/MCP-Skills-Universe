---
rating: ⭐⭐
title: clawhub-skill-vetting
url: https://skills.sh/hugomrtz/skill-vetting-clawhub/clawhub-skill-vetting
---

# clawhub-skill-vetting

skills/hugomrtz/skill-vetting-clawhub/clawhub-skill-vetting
clawhub-skill-vetting
Installation
$ npx skills add https://github.com/hugomrtz/skill-vetting-clawhub --skill clawhub-skill-vetting
Summary

Security-first vetting workflow for evaluating ClawHub skills before installation.

Mandatory code review scanning for exfiltration, secrets access, eval/exec, and obfuscation across all files
Six-step vetting process covering source reputation, permission scope, recent activity, community feedback, and safe installation practices
Produces structured SKILL VETTING REPORT with go/no-go recommendation, confidence scoring, and explicit red flag callouts
Includes reference checklist with commands, risk indicators, and sandbox installation guidance for uncertain cases
SKILL.md
ClawHub Skill Vetting
Overview

Apply a strict, security‑first vetting workflow before installing any ClawHub skill. Prioritize code review, permission scope, domain listing, and risk scoring.

Workflow
Source check — author reputation, stars/downloads, last update, reviews.
Code review (MANDATORY) — scan all files for exfiltration, secrets access, eval/exec, obfuscation.
Permission scope — files, commands, network; confirm minimal scope.
Recent activity — detect suspicious bursts.
Community check — Discord/GitHub Discussions.
Install safely — sandbox + inspect permissions.
Reference

Use references/vetting-guide.md for the full checklist, commands, red flags, confidence scoring, and report template.

Output expectations
Produce the SKILL VETTING REPORT format.
Provide a go/no‑go recommendation with reasons.
If unclear, recommend sandbox install only or reject.
Call out any red flags explicitly.
Include a confidence score and threshold.
Weekly Installs
1.5K
Repository
hugomrtz/skill-…-clawhub
GitHub Stars
4
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn