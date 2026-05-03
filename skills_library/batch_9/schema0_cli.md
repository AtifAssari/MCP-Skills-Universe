---
title: schema0-cli
url: https://skills.sh/schema0/skills/schema0-cli
---

# schema0-cli

skills/schema0/skills/schema0-cli
schema0-cli
Installation
$ npx skills add https://github.com/schema0/skills --skill schema0-cli
SKILL.md
Sandbox Commands

The codebase lives on a remote sandbox. All file operations and shell commands go through schema0 sandbox exec. Deployment uses schema0 sandbox deploy.

Command Summary
Command	Purpose
schema0 sandbox exec "<cmd>"	Run a shell command on the remote sandbox
schema0 sandbox read <path>	Read a file from the sandbox
schema0 sandbox write <path>	Write a file to the sandbox
schema0 sandbox ls [path] [-L <depth>]	List directory tree (respects .gitignore)
schema0 sandbox grep <pattern> [--path ..]	Search file contents on the sandbox
schema0 sandbox deploy	Build and deploy the application
schema0 version list	List all versions
schema0 version preview <hash>	Create preview from dev deployment
schema0 version deploy <hash>	Promote preview to production
schema0 whoami	Verify authentication
schema0 secrets list/set/delete	Manage secrets
schema0 doctor	Check deployment readiness
schema0 logs	View deployment logs
schema0 integrations ...	Discover and execute third-party actions
File Operations

Use dedicated file commands instead of sandbox exec "cat ...":

schema0 sandbox read packages/db/src/schema/tasks.ts        # read a file
schema0 sandbox write packages/db/src/schema/tasks.ts       # write (reads from stdin)
schema0 sandbox write path/to/file --content "file content"  # write inline
schema0 sandbox ls packages/db/src/schema                    # list directory tree
schema0 sandbox ls -L 2                                      # limit tree depth
schema0 sandbox grep "createDb" --path packages --include "*.ts"  # search


Relative paths resolve against the project root. Use these commands for all file reads, writes, and searches — they are faster and more reliable than sandbox exec "cat ...".

Key Notes
sandbox deploy handles all builds and migrations internally -- do NOT run build or migrate commands manually before deploying
sandbox exec max timeout is 300000 (5 minutes), default 30000
The sandbox filesystem persists between commands
Integrations use natural language search: schema0 integrations search gmail "send email"
References
references/sandbox-files.md -- sandbox read/write/ls/grep (single-path, not the local Read tool)
references/sandbox-exec.md -- sandbox exec syntax, options, common patterns
references/sandbox-deploy.md -- sandbox deploy options, what it does per platform, notes
references/version-management.md -- version list/preview/deploy/remove/confirm-migration workflow
Weekly Installs
17
Repository
schema0/skills
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass