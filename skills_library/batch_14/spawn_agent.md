---
title: spawn-agent
url: https://skills.sh/youngchingjui/spawn-agent/spawn-agent
---

# spawn-agent

skills/youngchingjui/spawn-agent/spawn-agent
spawn-agent
Installation
$ npx skills add https://github.com/youngchingjui/spawn-agent --skill spawn-agent
SKILL.md
Spawn Agent

Spawn an independent agent in a separate terminal pane. The agent is fully visible and interactive — the user can watch it work, guide it, and course-correct.

Use $ARGUMENTS as the prompt when the user invokes this skill directly.

Determine the spawn method

Check these in order:

Read saved config at ~/.claude/spawn-agent.json — may already have terminal type and preferences from a previous run.
Check environment variables:
$TMUX set → tmux
$TERM_PROGRAM = vscode → VS Code
$TERM_PROGRAM = iTerm.app → iTerm2
macOS with none of the above → Terminal.app
Linux → check for gnome-terminal, xterm, etc.
Run the detection script if still unsure:
bash "${CLAUDE_SKILL_DIR}/scripts/detect-terminal.sh"

Writes results to ~/.claude/spawn-agent.json.
Ask the user if ambiguous.
Config file

~/.claude/spawn-agent.json:

{
  "terminal": "tmux",
  "split": "vertical",
  "agent_command": "claude"
}

Key	Description	Default
terminal	tmux, iterm2, terminal-app, vscode, linux	auto-detected
split	vertical or horizontal	vertical
agent_command	Command to launch the agent (e.g. claude, codex)	claude
Spawn commands

Replace AGENT_CMD with the configured agent command and PROMPT with your crafted prompt.

tmux
tmux split-window -h -c "$(pwd)" "AGENT_CMD 'PROMPT'"


-h = vertical (side-by-side). -v = horizontal (top-bottom). -c "/other/path" for a different directory.

iTerm2
osascript -e '
tell application "iTerm2"
  tell current session of current window
    set newSession to (split vertically with default profile)
  end tell
  tell newSession
    write text "cd /path/to/project && AGENT_CMD '\''PROMPT'\''"
  end tell
end tell'


Change split vertically to split horizontally for top-bottom.

For convenience, scripts/spawn-iterm.sh wraps the same code above with argument parsing, escaping, and config reading. Optional but useful for auto-approving in Claude settings:

bash "${CLAUDE_SKILL_DIR}/scripts/spawn-iterm.sh" --dir /path/to/project "PROMPT"
bash "${CLAUDE_SKILL_DIR}/scripts/spawn-iterm.sh" --mode vertical --dir /path/to/project "PROMPT"
bash "${CLAUDE_SKILL_DIR}/scripts/spawn-iterm.sh" --mode horizontal --dir /path/to/project "PROMPT"


--mode options: tab (default), vertical (side-by-side split), horizontal (top-bottom split).

Terminal.app
osascript -e '
tell application "Terminal"
  activate
  do script "cd /path/to/project && AGENT_CMD '\''PROMPT'\''"
end tell'


Opens a new window (Terminal.app doesn't support split panes).

VS Code
code -r --command workbench.action.terminal.new


VS Code terminals don't support direct command injection — print instructions for the user to paste.

Linux
# gnome-terminal
gnome-terminal --working-directory="$(pwd)" -- bash -lc "AGENT_CMD 'PROMPT'; exec \$SHELL"

# xterm
xterm -e bash -lc "cd '$(pwd)' && AGENT_CMD 'PROMPT'; exec \$SHELL" &

Rules
Interactive mode only. Never pass flags that suppress interactivity (e.g. --print, -p).
Write a detailed prompt. Include all context the spawned agent needs: what to do, which files matter, expected outcome, constraints.
Weekly Installs
9
Repository
youngchingjui/s…wn-agent
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass