---
title: react-doctor
url: https://skills.sh/millionco/react-doctor/react-doctor
---

# react-doctor

skills/millionco/react-doctor/react-doctor
react-doctor
Installation
$ npx skills add https://github.com/millionco/react-doctor --skill react-doctor
Summary

Automated React codebase scanner that detects security, performance, correctness, and architecture issues.

Generates a 0-100 diagnostic score with actionable findings across four categories: security vulnerabilities, performance bottlenecks, correctness errors, and architectural problems
Designed for post-change workflows: run after code modifications, fix flagged issues, then re-run to verify improvements
Supports verbose output and diff mode to highlight changes between scans
Ideal for code review checkpoints, feature completion, and bug-fix verification in React projects
SKILL.md
React Doctor

Scans React codebases for security, performance, correctness, and architecture issues. Outputs a 0–100 health score.

After making React code changes:

Run npx -y react-doctor@latest . --verbose --diff and check the score did not regress.

If the score dropped, fix the regressions before committing.

For general cleanup or code improvement:

Run npx -y react-doctor@latest . --verbose (without --diff) to scan the full codebase. Fix issues by severity — errors first, then warnings.

Command
npx -y react-doctor@latest . --verbose --diff

Flag	Purpose
.	Scan current directory
--verbose	Show affected files and line numbers per rule
--diff	Only scan changed files vs base branch
--score	Output only the numeric score
Weekly Installs
7.4K
Repository
millionco/react-doctor
GitHub Stars
6.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn