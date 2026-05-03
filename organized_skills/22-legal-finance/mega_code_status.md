---
rating: ⭐⭐
title: mega-code-status
url: https://skills.sh/wisdomgraph/mega-code/mega-code-status
---

# mega-code-status

skills/wisdomgraph/mega-code/mega-code-status
mega-code-status
Installation
$ npx skills add https://github.com/wisdomgraph/mega-code --skill mega-code-status
SKILL.md
MEGA-Code Status

Show current MEGA-Code status and pending items.

Setup
MEGA_DIR="$(cd "${CLAUDE_SKILL_DIR}/../.." && pwd)"
uv run --directory "$MEGA_DIR" python -m mega_code.client.check_auth


If the auth check fails (non-zero exit), show the output to the user and stop.

Pipeline Status
uv run --directory "$MEGA_DIR" mega-code pipeline-status 2>/dev/null || true

Quick Status
ls -la ~/.local/share/mega-code/data/pending-skills/ ~/.local/share/mega-code/data/pending-strategies/ 2>/dev/null || echo "No pending items"

Detailed Pending Items

Uses ls checks to avoid zsh glob errors on empty directories.

SKILLS_DIR="$HOME/.local/share/mega-code/data/pending-skills"
STRATS_DIR="$HOME/.local/share/mega-code/data/pending-strategies"

echo "=== Pending Skills ==="
if [ -d "$SKILLS_DIR" ] && [ "$(ls -A "$SKILLS_DIR" 2>/dev/null)" ]; then
  for dir in "$SKILLS_DIR"/*/; do
    name=$(basename "$dir")
    desc=$(grep -m1 "description:" "$dir/SKILL.md" 2>/dev/null | cut -d: -f2- | head -c 60)
    echo "  $name:$desc"
  done
else
  echo "  (none)"
fi

echo "=== Pending Strategies ==="
if [ -d "$STRATS_DIR" ] && [ "$(ls -A "$STRATS_DIR" 2>/dev/null)" ]; then
  for file in "$STRATS_DIR"/*.md; do
    name=$(basename "$file" .md)
    desc=$(grep -m1 "^# " "$file" | cut -c3- | head -c 60)
    echo "  $name: $desc"
  done
else
  echo "  (none)"
fi

Output Locations
Type	Pending Location	Installed Location
Skills	~/.local/share/mega-code/data/pending-skills/{name}/	.claude/skills/{name}/SKILL.md
Strategies	~/.local/share/mega-code/data/pending-strategies/{name}.md	.claude/rules/mega-code/{name}.md
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