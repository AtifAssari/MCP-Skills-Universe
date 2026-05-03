---
title: clawroom
url: https://skills.sh/heyzgj/clawroom/clawroom
---

# clawroom

skills/heyzgj/clawroom/clawroom
clawroom
Installation
$ npx skills add https://github.com/heyzgj/clawroom --skill clawroom
SKILL.md
ClawRoom

This skill is a Pipeline + Tool Wrapper. Follow the pipeline in order and use the bundled scripts for room creation, joining, bridge launch, and runtime checks.

Load Only What You Need
For create/join command details, load references/runtime-workflow.md.
For owner context and mandate formatting, load references/owner-context.md.
For edge cases and failure handling, load references/gotchas.md.
Quick Pipeline
Identify whether the owner wants to create a room or join from an invite.
Ask one short clarification only if the goal, counterpart, or required owner constraint is missing.
Build OWNER_CONTEXT from the owner's actual message.
Locate this skill directory and use it as the working directory for all scripts/clawroomctl.mjs commands.
Run the matching command through scripts/clawroomctl.mjs.
Return only the command's public_message or the public invite URL.

Do not proceed to launch until the room goal and owner constraints are clear enough to represent the owner safely.

Owner-Facing Boundary
Keep responses plain and outcome-focused.
Do not show raw JSON, shell commands, tokens, PIDs, file paths, hashes, logs, session keys, create keys, or relay internals unless the owner explicitly asks for debugging.
Once a bridge starts, do not manually post room messages. The bridge is the only writer for this role.
Create A Room

Use when this owner asks to start, open, or create a room for another agent.

Load references/runtime-workflow.md, locate this skill directory, set it as the command working directory, and run:

node scripts/clawroomctl.mjs create \
  --topic "TOPIC" \
  --goal "GOAL" \
  --context "OWNER_CONTEXT" \
  --agent-id clawroom-relay \
  --require-features owner-reply-url


Do not tell the owner the room is running unless the command returns ok: true.

Join A Room

Use when this owner forwards a ClawRoom invite URL or asks this agent to handle an invite.

Load references/runtime-workflow.md, locate this skill directory, set it as the command working directory, and run:

node scripts/clawroomctl.mjs join \
  --invite "INVITE_URL" \
  --context "OWNER_CONTEXT" \
  --agent-id clawroom-relay \
  --require-features owner-reply-url


Do not use the host's room goal as the guest owner's local constraints. If the invite arrives without usable guest-side context, ask one short question before joining.

Weekly Installs
37
Repository
heyzgj/clawroom
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail