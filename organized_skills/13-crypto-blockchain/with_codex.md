---
rating: ⭐⭐⭐
title: with-codex
url: https://skills.sh/seika139/dotfiles/with-codex
---

# with-codex

skills/seika139/dotfiles/with-codex
with-codex
Installation
$ npx skills add https://github.com/seika139/dotfiles --skill with-codex
SKILL.md
With Codex - Claude and Codex Collaboration

This skill enables collaboration between Claude Code and OpenAI Codex CLI for second opinions, validation, and collaborative problem-solving.

CRITICAL REQUIREMENT

Claude Code MUST be running inside a tmux session for this skill to work.

If not in tmux, inform the user: "このスキルを使用するには、tmuxセッション内でClaude Codeを起動する必要があります。以下のコマンドを実行してください:

tmux new-session -s claude
claude


"

Environment Requirements
WSL (Ubuntu) with tmux installed
OpenAI Codex CLI installed and authenticated in WSL
Claude Code running inside a tmux session
Skill scripts at: ~/.claude/skills/with-codex/scripts/
Standard Workflow (MUST FOLLOW)

When this skill is triggered, ALWAYS execute these steps in order:

Step 1: Setup - Split pane and start Codex
~/.claude/skills/with-codex/scripts/codex-manager.sh setup


This splits the current tmux pane:

Left pane: Claude Code (current)
Right pane: Codex CLI (newly created, with dark background)
Step 2: Claude performs its own analysis first

Analyze the user's request independently before querying Codex.

Step 3: Send the same prompt to Codex
~/.claude/skills/with-codex/scripts/codex-manager.sh send "YOUR_PROMPT_HERE"


Replace YOUR_PROMPT_HERE with the actual question/task from the user.

Step 4: Wait for Codex response
~/.claude/skills/with-codex/scripts/codex-manager.sh wait 60


Wait up to 60 seconds for Codex to complete its response.

Step 5: Capture Codex output
~/.claude/skills/with-codex/scripts/codex-manager.sh capture 200


Capture the last 200 lines of Codex's output.

Step 6: Present combined results

Present results in this format:

## Claude's Analysis
[Your independent analysis]

## Codex's Analysis
[Captured response from Codex]

## Synthesis
- **Agreement**: [Points where both AIs agree]
- **Differences**: [Alternative perspectives from Codex]
- **Recommendation**: [Best combined approach]

Step 7: Cleanup (when conversation ends or user requests)
~/.claude/skills/with-codex/scripts/codex-manager.sh cleanup

Available Commands
Command	Description
setup	Split pane and start Codex on the right
send "prompt"	Send prompt to Codex pane
capture [lines]	Capture Codex output (default: 100 lines)
wait [timeout]	Wait for response to stabilize (default: 60s)
cleanup	Close the Codex pane
status	Check pane status
focus	Switch focus to Codex pane
Error Handling

If setup fails with "Not running inside tmux":

Inform user they need to start Claude Code inside tmux
Provide the commands: tmux new-session -s claude then claude
Alternative: Non-Interactive Mode

Only use when tmux is unavailable or user explicitly requests:

codex exec "your prompt" 2>/dev/null

Best Practices
ALWAYS use tmux interactive mode by default
Let user see both AIs working side-by-side
Wait adequate time (30-60s) for complex Codex queries
Present both perspectives without bias
Acknowledge both AIs can be wrong - user makes final decision
Weekly Installs
21
Repository
seika139/dotfiles
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass