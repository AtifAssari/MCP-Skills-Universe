---
rating: ⭐⭐⭐
title: f1-test-drive
url: https://skills.sh/ceedaragents/cyrus/f1-test-drive
---

# f1-test-drive

skills/ceedaragents/cyrus/f1-test-drive
f1-test-drive
Installation
$ npx skills add https://github.com/ceedaragents/cyrus --skill f1-test-drive
SKILL.md
F1 Test Drive

Run comprehensive F1 test drives that validate the full pipeline:

Issue-tracker behavior
EdgeWorker execution flow
Activity rendering/output quality
Mission

Execute test drives that verify:

Issue-tracker correctness
EdgeWorker worktree/session behavior
Activity output visibility and formatting
Test Drive Protocol
Phase 1: Setup

Create a fresh test repository (if needed):

cd apps/f1
./f1 init-test-repo --path /tmp/f1-test-drive-<timestamp>


Start F1 server:

CYRUS_PORT=3600 CYRUS_REPO_PATH=/tmp/f1-test-drive-<timestamp> bun run apps/f1/server.ts &


Verify server health:

CYRUS_PORT=3600 ./f1 ping
CYRUS_PORT=3600 ./f1 status

Phase 2: Issue-Tracker Verification

Create test issue:

CYRUS_PORT=3600 ./f1 create-issue \
  --title "<issue title>" \
  --description "<issue description>"


Verify issue ID and issue creation response.

Phase 3: EdgeWorker Verification

Start agent session:

CYRUS_PORT=3600 ./f1 start-session --issue-id <issue-id>


Monitor activities:

CYRUS_PORT=3600 ./f1 view-session --session-id <session-id>


Verify:

session started
activities appear
agent is processing issue
Phase 4: Renderer Verification

Validate activity payload quality:

expected types (for example thought, action, response)
timestamps present
content well-formed and readable

Validate pagination behavior:

CYRUS_PORT=3600 ./f1 view-session --session-id <session-id> --limit 10 --offset 0

Phase 5: Cleanup

Stop active session:

CYRUS_PORT=3600 ./f1 stop-session --session-id <session-id>


Stop background server process.

Reporting Format

Write report under apps/f1/test-drives/:

# Test Drive #NNN: [Goal Description]

**Date**: YYYY-MM-DD
**Goal**: [One sentence]
**Test Repo**: [Path]

## Verification Results

### Issue-Tracker
- [ ] Issue created
- [ ] Issue ID returned
- [ ] Issue metadata accessible

### EdgeWorker
- [ ] Session started
- [ ] Worktree created (if applicable)
- [ ] Activities tracked
- [ ] Agent processed issue

### Renderer
- [ ] Activity format correct
- [ ] Pagination works
- [ ] Search works

## Session Log
[commands + key outputs + pass/fail]

## Final Retrospective
[what worked, issues, recommendations]

Pass/Fail Criteria

Pass when:

Server starts
Issue created successfully
Session starts and activities appear
Activity payloads are coherent
Session stops cleanly
No unhandled errors

Fail when:

server startup fails
issue creation fails
session does not start
no activities after reasonable wait
malformed activity data
unhandled exceptions
Important Notes
Prefer fixed port 3600 unless already in use.
Use fresh test repos per drive.
Preserve failed state when debugging.
For major runner/harness changes, run at least one F1 end-to-end validation before merge.
Multi-Harness Note

This skill is intentionally harness-agnostic:

Claude subagents can call this skill.
Codex/OpenCode workflows can reference the same skill content.
Harness-specific adapters should be thin wrappers around this canonical skill.
Weekly Installs
79
Repository
ceedaragents/cyrus
GitHub Stars
564
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass