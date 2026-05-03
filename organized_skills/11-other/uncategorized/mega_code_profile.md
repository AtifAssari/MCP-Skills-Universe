---
rating: ⭐⭐
title: mega-code-profile
url: https://skills.sh/wisdomgraph/mega-code/mega-code-profile
---

# mega-code-profile

skills/wisdomgraph/mega-code/mega-code-profile
mega-code-profile
Installation
$ npx skills add https://github.com/wisdomgraph/mega-code --skill mega-code-profile
SKILL.md
Developer Profile

Set up your developer profile to personalise skill extraction. Profile determines which skills are too basic for your experience level.

Setup
MEGA_DIR="$(cd "${CLAUDE_SKILL_DIR}/../.." && pwd)"
uv run --directory "$MEGA_DIR" python -m mega_code.client.check_auth


If the auth check fails (non-zero exit), show the output to the user and stop.

Interactive Setup (Recommended)

Ask the user for their profile using AskUserQuestion with these fields:

language: Preferred communication language — options: English, Korean, Thai (user can also type a custom language via "Other")
level: Beginner, Intermediate, or Expert
style: Mentor, Formal, or Concise (reserved for future use)

Save with:

uv run --directory "$MEGA_DIR" mega-code profile --language "<language>" --level <level> --style <style>

Show Current Profile
uv run --directory "$MEGA_DIR" mega-code profile

Reset Profile
uv run --directory "$MEGA_DIR" mega-code profile --reset

Profile Storage

Profile is saved in two places:

Remote server — authoritative source, persists across machines. Requires a valid API key (run /mega-code:login first).
Local mirror ~/.local/share/mega-code/profile.json — written only after a successful remote save.
Weekly Installs
28
Repository
wisdomgraph/mega-code
GitHub Stars
43
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass