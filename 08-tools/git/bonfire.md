---
title: bonfire
url: https://skills.sh/vieko/bonfire/bonfire
---

# bonfire

skills/vieko/bonfire/bonfire
bonfire
Installation
$ npx skills add https://github.com/vieko/bonfire --skill bonfire
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Bonfire

Session context persistence for AI coding. Pick up exactly where you left off.

Git root: !git rev-parse --show-toplevel

Routing

Parse $ARGUMENTS to determine action:

Input	Action
start	Read commands/start.md and execute
end	Read commands/end.md and execute
Empty or context question	Read <git-root>/.bonfire/index.md, summarize relevant context, answer
Bootstrap

If .bonfire/index.md doesn't exist when any command runs, create defaults from templates/: .bonfire/index.md (session context) and .bonfire/.gitignore (ignore all).

Weekly Installs
98
Repository
vieko/bonfire
GitHub Stars
9
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass