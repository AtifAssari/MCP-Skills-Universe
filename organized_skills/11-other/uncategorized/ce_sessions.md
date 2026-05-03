---
rating: ⭐⭐⭐
title: ce-sessions
url: https://skills.sh/everyinc/compound-engineering-plugin/ce-sessions
---

# ce-sessions

skills/everyinc/compound-engineering-plugin/ce-sessions
ce-sessions
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill ce-sessions
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

/ce-sessions

Search your session history.

Usage
/ce-sessions [question or topic]
/ce-sessions

Pre-resolved context

Repo name (pre-resolved): !common=$(git rev-parse --path-format=absolute --git-common-dir 2>/dev/null); repo="${common%/.git}"; echo "${repo##*/}"

Git branch (pre-resolved): !git rev-parse --abbrev-ref HEAD 2>/dev/null || true

If the lines above resolved to plain values (a folder name like my-repo and a branch name like feat/my-branch), they are ready to pass to the agent. If they still contain backtick command strings or are empty, they did not resolve — omit them from the dispatch and let the agent derive them at runtime.

Execution

If no argument is provided, ask what the user wants to know about their session history. Use the platform's blocking question tool: AskUserQuestion in Claude Code (call ToolSearch with select:AskUserQuestion first if its schema isn't loaded), request_user_input in Codex, ask_user in Gemini, ask_user in Pi (requires the pi-ask-user extension). Fall back to asking in plain text only when no blocking tool exists in the harness or the call errors (e.g., Codex edit modes) — not because a schema load is required. Never silently skip the question.

Dispatch ce-session-historian with the user's question as the task prompt. Omit the mode parameter so the user's configured permission settings apply. Include in the dispatch prompt:

The user's question
The current working directory
The repo name and git branch from pre-resolved context (only if they resolved to plain values — do not pass literal command strings)
Weekly Installs
162
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass