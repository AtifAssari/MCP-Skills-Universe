---
title: ask
url: https://skills.sh/yeachan-heo/oh-my-claudecode/ask
---

# ask

skills/yeachan-heo/oh-my-claudecode/ask
ask
Installation
$ npx skills add https://github.com/yeachan-heo/oh-my-claudecode --skill ask
SKILL.md
Ask

Use OMC's canonical advisor skill to route a prompt through the local Claude, Codex, or Gemini CLI and persist the result as an ask artifact.

Usage
/oh-my-claudecode:ask <claude|codex|gemini> <question or task>


Examples:

/oh-my-claudecode:ask codex "review this patch from a security perspective"
/oh-my-claudecode:ask gemini "suggest UX improvements for this flow"
/oh-my-claudecode:ask claude "draft an implementation plan for issue #123"

Routing

Required execution path — always use this command:

omc ask {{ARGUMENTS}}


Do NOT manually construct raw provider CLI commands. Never run codex, claude, or gemini directly to fulfill this skill. The omc ask wrapper handles correct flag selection, artifact persistence, and provider-version compatibility automatically. Manually assembling provider CLI flags will produce incorrect or outdated invocations.

Requirements
The selected local CLI must be installed and authenticated.
Verify availability with the matching command:
claude --version
codex --version
gemini --version

Artifacts

omc ask writes artifacts to:

.omc/artifacts/ask/<provider>-<slug>-<timestamp>.md


Task: {{ARGUMENTS}}

Weekly Installs
181
Repository
yeachan-heo/oh-…audecode
GitHub Stars
32.3K
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass