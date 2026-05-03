---
rating: ⭐⭐
title: git-guardrails-claude-code
url: https://skills.sh/mattpocock/skills/git-guardrails-claude-code
---

# git-guardrails-claude-code

skills/mattpocock/skills/git-guardrails-claude-code
git-guardrails-claude-code
Installation
$ npx skills add https://github.com/mattpocock/skills --skill git-guardrails-claude-code
Summary

Intercept and block dangerous git commands before Claude executes them via PreToolUse hooks.

Blocks five command categories: git push (including --force), git reset --hard, git clean, git branch -D, and git checkout/git restore on tracked files
Installs as a bash hook script to either project scope (.claude/settings.json) or globally (~/.claude/settings.json)
Customizable blocklist: edit the hook script to add or remove patterns based on your safety requirements
Claude receives an authority denial message when attempting blocked commands, preventing destructive operations
SKILL.md
Setup Git Guardrails

Sets up a PreToolUse hook that intercepts and blocks dangerous git commands before Claude executes them.

What Gets Blocked
git push (all variants including --force)
git reset --hard
git clean -f / git clean -fd
git branch -D
git checkout . / git restore .

When blocked, Claude sees a message telling it that it does not have authority to access these commands.

Steps
1. Ask scope

Ask the user: install for this project only (.claude/settings.json) or all projects (~/.claude/settings.json)?

2. Copy the hook script

The bundled script is at: scripts/block-dangerous-git.sh

Copy it to the target location based on scope:

Project: .claude/hooks/block-dangerous-git.sh
Global: ~/.claude/hooks/block-dangerous-git.sh

Make it executable with chmod +x.

3. Add hook to settings

Add to the appropriate settings file:

Project (.claude/settings.json):

{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}


Global (~/.claude/settings.json):

{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}


If the settings file already exists, merge the hook into existing hooks.PreToolUse array — don't overwrite other settings.

4. Ask about customization

Ask if user wants to add or remove any patterns from the blocked list. Edit the copied script accordingly.

5. Verify

Run a quick test:

echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>


Should exit with code 2 and print a BLOCKED message to stderr.

Weekly Installs
5.3K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass