---
rating: ⭐⭐
title: setup
url: https://skills.sh/everyinc/compound-engineering-plugin/setup
---

# setup

skills/everyinc/compound-engineering-plugin/setup
setup
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill setup
SKILL.md
Compound Engineering Setup

Project-level configuration for compound-engineering workflows.

Current State

Review agent selection is handled automatically by the ce:review skill, which uses intelligent tiered selection based on diff content. No per-project configuration is needed for code reviews.

If this skill is invoked, inform the user:

Review agent configuration is no longer needed — ce:review automatically selects the right reviewers based on your diff. Project-specific review context (e.g., "we serve 10k req/s" or "watch for N+1 queries") belongs in your project's CLAUDE.md or AGENTS.md, where all agents already read it.

Future Use

This skill is reserved for future project-level configuration needs beyond review agent selection.

Weekly Installs
393
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass