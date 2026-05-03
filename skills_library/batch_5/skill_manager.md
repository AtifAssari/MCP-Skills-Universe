---
title: skill-manager
url: https://skills.sh/kkkkhazix/khazix-skills/skill-manager
---

# skill-manager

skills/kkkkhazix/khazix-skills/skill-manager
skill-manager
Installation
$ npx skills add https://github.com/kkkkhazix/khazix-skills --skill skill-manager
SKILL.md
Skill Lifecycle Manager

This skill helps you maintain your library of GitHub-wrapped skills by automating the detection of updates and assisting in the refactoring process.

Core Capabilities
Audit: Scans your local skills folder for skills with github_url metadata.
Check: Queries GitHub (via git ls-remote) to compare local commit hashes against the latest remote HEAD.
Report: Generates a status report identifying which skills are "Stale" or "Current".
Update Workflow: Provides a structured process for the Agent to upgrade a skill.
Inventory Management: Lists all local skills and provides deletion capabilities.
Usage

Trigger: /skill-manager check or "Scan my skills for updates" Trigger: /skill-manager list or "List my skills" Trigger: /skill-manager delete <skill_name> or "Delete skill <skill_name>"

Workflow 1: Check for Updates
Run Scanner: The agent runs scripts/scan_and_check.py to analyze all skills.
Review Report: The script outputs a JSON summary. The Agent presents this to the user.
Example: "Found 3 outdated skills: yt-dlp (behind 50 commits), ffmpeg-tool (behind 2 commits)..."
Workflow 2: Update a Skill

Trigger: "Update [Skill Name]" (after a check)

Fetch New Context: The agent fetches the new README from the remote repo.
Diff Analysis:
The agent compares the new README with the old SKILL.md.
Identifies new features, deprecated flags, or usage changes.
Refactor:
The agent rewrites SKILL.md to reflect the new capabilities.
The agent updates the github_hash in the frontmatter.
The agent (optionally) attempts to update the wrapper.py if CLI args have changed.
Verify: Runs a quick validation (if available).
Scripts
scripts/scan_and_check.py: The workhorse. Scans directories, parses Frontmatter, fetches remote tags, returns status.
scripts/update_helper.py: (Optional) Helper to backup files before update.
scripts/list_skills.py: Lists all installed skills with type and version.
scripts/delete_skill.py: Permanently removes a skill folder.
Metadata Requirements

This manager relies on the github-to-skills metadata standard:

github_url: Source of truth.
github_hash: State of truth.
Weekly Installs
299
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