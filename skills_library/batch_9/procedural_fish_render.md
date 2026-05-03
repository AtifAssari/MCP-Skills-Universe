---
title: procedural-fish-render
url: https://skills.sh/vibe-motion/skills/procedural-fish-render
---

# procedural-fish-render

skills/vibe-motion/skills/procedural-fish-render
procedural-fish-render
Installation
$ npx skills add https://github.com/vibe-motion/skills --skill procedural-fish-render
SKILL.md
Procedural Fish Render
Workflow
Resolve skill_dir and run the helper script:
skill_dir=""
for base in "${AGENTS_HOME:-$HOME/.agents}" "${CLAUDE_HOME:-$HOME/.claude}" "${CODEX_HOME:-$HOME/.codex}"; do
  if [ -d "$base/skills/procedural-fish-render" ]; then
    skill_dir="$base/skills/procedural-fish-render"
    break
  fi
done
[ -n "$skill_dir" ] || { echo "procedural-fish-render skill not found under ~/.agents, ~/.claude, or ~/.codex"; exit 1; }

/usr/local/bin/python3 "$skill_dir/scripts/render_procedural_fish.py"

Optional parameters:
/usr/local/bin/python3 "$skill_dir/scripts/render_procedural_fish.py" \
  --workspace "$(pwd)" \
  --output "out/procedural-fish-custom.mov" \
  --props-file "shared/project/render-presets/default.json"

Return the final absolute video path printed by the script.
Behavior
Repository source is fixed to https://github.com/vibe-motion/procedural-fish by default.
If local repo exists, the script performs git fetch + git checkout main + git pull --ff-only.
If local repo does not exist, the script clones it.
Rendering always uses project command pnpm run remotion:render.
Default output is out/procedural-fish-transparent.mov.
Default props file is shared/project/render-presets/default.json.
Weekly Installs
270
Repository
vibe-motion/skills
GitHub Stars
403
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn