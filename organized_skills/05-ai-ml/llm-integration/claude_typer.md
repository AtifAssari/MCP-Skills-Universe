---
rating: ⭐⭐
title: claude-typer
url: https://skills.sh/vibe-motion/skills/claude-typer
---

# claude-typer

skills/vibe-motion/skills/claude-typer
claude-typer
Installation
$ npx skills add https://github.com/vibe-motion/skills --skill claude-typer
SKILL.md
Claude Typer
Workflow
Extract the text that should be typed in the animation as prompt.
Run:
skill_dir=""
for base in "${AGENTS_HOME:-$HOME/.agents}" "${CLAUDE_HOME:-$HOME/.claude}" "${CODEX_HOME:-$HOME/.codex}"; do
  if [ -d "$base/skills/claude-typer" ]; then
    skill_dir="$base/skills/claude-typer"
    break
  fi
done
[ -n "$skill_dir" ] || { echo "claude-typer skill not found under ~/.agents, ~/.claude, or ~/.codex"; exit 1; }
/usr/local/bin/python3 "$skill_dir/scripts/render_claude_typer.py" "<prompt>"

Example with explicit size and scale:
/usr/local/bin/python3 "$skill_dir/scripts/render_claude_typer.py" \
  "claude-typer skill可以让智能体做出提示词打字机动效视频，快来试试吧" \
  --video-width 1080 \
  --video-height 600 \
  --claude-width 600 \
  --scale 2

Example matching custom runner + remotion params passthrough:
/usr/local/bin/python3 "$skill_dir/scripts/render_claude_typer.py" \
  "vibe-motion/skills：一个面向智能体的MG动画/视频技能仓库." \
  --runner-prefix "npx -y -p @remotion/cli@4.0.440 -p @remotion/tailwind-v4@4.0.440 remotion" \
  --composition Typer30fps \
  --output-file Typer30fps.mov \
  --codec prores \
  --prores-profile 4444 \
  --pixel-format yuva444p10le \
  --image-format png \
  --audio-codec aac \
  --video-width 1080 \
  --video-height 1080 \
  --claude-width 880

Return the generated video path in the current working directory.
Rendering Behavior
Render remote composition Typer30fps from https://www.laosunwendao.com.
Use @remotion/cli (not remotion package name).
Prefer bunx @remotion/cli first.
Fall back to npx -y -p @remotion/cli@4.0.440 -p @remotion/tailwind-v4@4.0.440 remotion if bunx is unavailable.
Keep transparent MOV defaults:
--fps=30
--codec=prores
--prores-profile=4444
--pixel-format=yuva444p10le
--image-format=png
--scale=2
Keep defaults for stability:
--timeout=300000
--concurrency=1
Auto-detect local Chrome/Chromium and pass --browser-executable when found.
Keep default props from the project; replace prompt, and allow overriding videoWidth / videoHeight / claudeWidth through script args.
Unknown CLI args are passed through to remotion render directly (for advanced flags).
--runner-prefix lets you fully control the runner command (for pinned versions, global resolution behavior, etc.).
Exposed Remotion props for this skill are scalar fields only: prompt, typingSpeedMs, model, videoWidth, videoHeight, claudeWidth, tiltStartX, tiltStartY, tiltEndX, tiltEndY, tiltDurationRatio.
Output File Naming
Save into the current directory as xxx.mov.
Build xxx by condensing the prompt:
Remove common request wrappers like 帮我, 请, 做一个, 生成一个, 制作, 创建 at the start.
Remove illegal filename characters.
Keep Chinese/English letters and digits.
If result is empty, use claude-typer.
Example:
Prompt: 帮我做一个web画板
Output: web画板.mov
Notes
On a clean machine, Node.js + npx is enough for this fallback path, as long as network access to npm and https://www.laosunwendao.com is available.
If both bunx and npx are unavailable, install one of them and retry.
If the output name already exists, Remotion overwrite behavior applies.
If you hit delayRender() timeout, keep --concurrency=1 and raise --timeout-ms as needed.
Weekly Installs
300
Repository
vibe-motion/skills
GitHub Stars
403
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn