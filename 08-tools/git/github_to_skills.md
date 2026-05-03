---
rating: ⭐⭐⭐
title: github-to-skills
url: https://skills.sh/kkkkhazix/khazix-skills/github-to-skills
---

# github-to-skills

skills/kkkkhazix/khazix-skills/github-to-skills
github-to-skills
Installation
$ npx skills add https://github.com/kkkkhazix/khazix-skills --skill github-to-skills
SKILL.md
GitHub to Skills Factory

This skill automates the conversion of GitHub repositories into fully functional AI skills.

Core Functionality
Analysis: Fetches repository metadata (Description, README, Latest Commit Hash).
Scaffolding: Creates a standardized skill directory structure.
Metadata Injection: Generates SKILL.md with extended frontmatter (tracking source, version, hash) for future automated management.
Wrapper Generation: Creates a scripts/wrapper.py (or similar) to interface with the tool.
Usage

Trigger: /GitHub-to-skills <github_url> or "Package this repo into a skill: "

Required Metadata Schema

Every skill created by this factory MUST include the following extended YAML frontmatter in its SKILL.md. This is critical for the skill-manager to function later.

---
name: <kebab-case-repo-name>
description: <concise-description-for-agent-triggering>
# EXTENDED METADATA (MANDATORY)
github_url: <original-repo-url>
github_hash: <latest-commit-hash-at-time-of-creation>
version: <tag-or-0.1.0>
created_at: <ISO-8601-date>
entry_point: scripts/wrapper.py # or main script
dependencies: # List main dependencies if known, e.g., ["yt-dlp", "ffmpeg"]
---

Workflow
Fetch Info: The agent first runs scripts/fetch_github_info.py to get the raw data from the repo.
Plan: The agent analyzes the README to understand how to invoke the tool (CLI args, Python API, etc.).
Generate: The agent uses the skill-creator patterns to write the SKILL.md and wrapper scripts, ensuring the extended metadata is present.
Verify: Checks if the commit hash was correctly captured.
Resources
scripts/fetch_github_info.py: Utility to scrape/API fetch repo details (README, Hash, Tags).
scripts/create_github_skill.py: Orchestrator to scaffold the folder and write the initial files.
Best Practices for Generated Skills
Isolation: The generated skill should install its own dependencies (e.g., in a venv or via uv/pip) if possible, or clearly state them.
Progressive Disclosure: Do not dump the entire repo into the skill. Only include the necessary wrapper code and reference the original repo for deep dives.
Idempotency: The github_hash field allows the future skill-manager to check if remote_hash != local_hash to trigger updates.
Weekly Installs
260
Repository
kkkkhazix/khazix-skills
GitHub Stars
7.7K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn