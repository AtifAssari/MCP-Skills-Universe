---
title: vcs-change-request
url: https://skills.sh/diegocanepa/agent-skills/vcs-change-request
---

# vcs-change-request

skills/diegocanepa/agent-skills/vcs-change-request
vcs-change-request
Installation
$ npx skills add https://github.com/diegocanepa/agent-skills --skill vcs-change-request
SKILL.md
MR/PR Description Manager
Workflow
Detect Platform: Check if working on GitHub (PR) or GitLab (MR).
Context: Understand the changes and find the related issue number.
Drafting:
Write in English only.
Use Markdown (Titles, Subtitles, Code Snippets, Items).
Use Emojis for a friendly tone.
Use a template from references/templates.md.
MITM Confirmation: ALWAYS present the drafted description to the USER for approval.
Execution: Call the platform-specific tool.
Technical Mapping
Platform	Object	Tool Example
GitHub	Pull Request (PR)	mcp__github__create_pull_request
GitLab	Merge Request (MR)	mcp__gitlab__create_merge_request
Key Rules
Issue Reference: Always link the issue (Closes #123, etc.) to automate status changes.
Title Format: Use feat, fix, refactor, docs, test, chore.
Quality: Refer to DO/DON'T in references/guidelines.md.
Token Efficiency: Focus on value-added context. Skip obvious details.
Examples
GitHub: feat: add oauth support (#123)
GitLab: fix: resolve crash on upload (#456)
Weekly Installs
8
Repository
diegocanepa/agent-skills
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass