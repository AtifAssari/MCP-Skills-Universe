---
title: deslop
url: https://skills.sh/brianlovin/claude-config/deslop
---

# deslop

skills/brianlovin/claude-config/deslop
deslop
Installation
$ npx skills add https://github.com/brianlovin/claude-config --skill deslop
Summary

Clean up AI-generated code bloat by removing unnecessary comments, defensive checks, and style inconsistencies from your branch.

Analyzes diffs against main to identify and remove extra comments, defensive try/catch blocks, and type-safety workarounds that deviate from codebase patterns
Focuses on changes introduced by AI, preserving intentional human code and existing file conventions
Provides a concise summary of modifications made, keeping feedback to 1–3 sentences
SKILL.md
Remove AI code slop

Check the diff against main, and remove all AI generated slop introduced in this branch.

This includes:

Extra comments that a human wouldn't add or is inconsistent with the rest of the file
Extra defensive checks or try/catch blocks that are abnormal for that area of the codebase (especially if called by trusted / validated codepaths)
Casts to any to get around type issues
Any other style that is inconsistent with the file

Report at the end with only a 1-3 sentence summary of what you changed

Weekly Installs
904
Repository
brianlovin/claude-config
GitHub Stars
334
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass