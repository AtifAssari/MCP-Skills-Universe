---
rating: ⭐⭐⭐
title: clawmail
url: https://skills.sh/joelhooks/joelclaw/clawmail
---

# clawmail

skills/joelhooks/joelclaw/clawmail
clawmail
Installation
$ npx skills add https://github.com/joelhooks/joelclaw --skill clawmail
SKILL.md
Clawmail

Canonical agent coordination contract for joelclaw.

joelclaw mail is the only supported mail access surface for pi agents. Do not call mcp_agent_mail HTTP endpoints directly from agent prompts or role instructions.

Interfaces
Canonical interface
joelclaw mail ... (CLI)
Pi wrapper tools (allowed, but still CLI-backed)

These wrappers shell to joelclaw mail under the hood:

Tool	CLI equivalent
mail_send	joelclaw mail send
mail_inbox	joelclaw mail inbox
mail_read	joelclaw mail read
mail_reserve	joelclaw mail reserve
mail_release	joelclaw mail release
mail_status	joelclaw mail status
Required Protocol (default for shared work)
Check inbox before touching files
joelclaw mail inbox --agent <AgentName> --unread
Announce active scope
joelclaw mail send --from <AgentName> --to <AgentName|team> --subject "Starting: <work>" "intent + paths + expected output"
Reserve file paths before edits
joelclaw mail reserve --agent <AgentName> --paths "path/a.ts,path/b.ts" [--ttl-seconds 900]
If work runs long, renew reservation lease
joelclaw mail renew --agent <AgentName> --paths "path/a.ts" [--extend-seconds 900]
Send status/handoff updates during work
joelclaw mail send --subject "Status: ..." ...
Release reservations after commit/handoff
joelclaw mail release --agent <AgentName> --paths "..."
or --all when done with all reserved paths
Subject Taxonomy (for searchability + steering)

Use these prefixes consistently:

Starting: — work start / intent announcement
Task: — handoff or assignment
Status: — progress update
Blocked: — dependency/incident requiring intervention
Done: — completion with artifact/commit IDs

Daily steering uses these signals to detect protocol drift.

Command Quick Reference
# server + inbox health
joelclaw mail status

# register / refresh identity metadata
joelclaw mail register --agent MaroonReef --program pi --model gpt-5.4 --task "interactive"

# send a coordination message
joelclaw mail send --from MaroonReef --to BlueFox --subject "Task: update prompt docs" "Please edit SYSTEM.md and roles/*.md"

# inbox / read
joelclaw mail inbox --agent MaroonReef --unread
joelclaw mail read --agent MaroonReef --id 12

# reservations
joelclaw mail reserve --agent MaroonReef --paths "SYSTEM.md,roles/interactive.md" --ttl-seconds 900
joelclaw mail renew --agent MaroonReef --paths "SYSTEM.md" --extend-seconds 900
joelclaw mail release --agent MaroonReef --paths "SYSTEM.md,roles/interactive.md"
joelclaw mail release --agent MaroonReef --all

# audit/search
joelclaw mail locks
joelclaw mail search --query "Starting:"

Reliability Checks
Verify protocol health quickly
joelclaw mail status
joelclaw mail locks
joelclaw mail search --query "Starting:"
joelclaw mail search --query "Status:"


joelclaw mail locks should reflect active advisory file reservations from the local git-mailbox file_reservations/ artifacts when that repo is available. This matters because the raw /mail/api/locks endpoint can under-report file reservations while still showing mailbox-internal archive/commit locks.

If search is degraded (DB/tool errors)
Treat signal counts as unreliable.
Continue using protocol anyway (announce/reserve/release).
Escalate to mail backend health repair and log findings.
If CLI flags are rejected unexpectedly
Your compiled ~/.bun/bin/joelclaw may be stale relative to source.
Rebuild CLI from packages/cli/src/cli.ts and retry.
Prompt Authoring Checklist (shore up prompts)

Any prompt/role/system contract that mentions coordination should:

Reference clawmail as canonical protocol skill.
State that mail access is via joelclaw mail (wrappers allowed, direct MCP not allowed).
Include at minimum: inbox check, announce, reserve, release.
Require path context in coordination messages.
Encourage subject prefixes (Starting:, Task:, Status:, Blocked:, Done:).
Avoid filler about mail when no shared edits/coordination are involved.
Steering Loop Integration

pi/extensions/session-lifecycle runs a daily monitor+steer review and emits:

agent-mail/steering.reviewed

Snapshot path:

~/.joelclaw/workspace/agent-mail-steering/YYYY-MM-DD.json

Use steering hints to tighten protocol compliance when drift is detected.

Related
skills/agent-mail/SKILL.md (compatibility alias)
joelclaw mail --help
ADR-0172: Agent Mail via MCP Agent Mail
Weekly Installs
28
Repository
joelhooks/joelclaw
GitHub Stars
55
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass