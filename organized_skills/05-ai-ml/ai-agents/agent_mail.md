---
rating: ⭐⭐⭐
title: agent-mail
url: https://skills.sh/johnlindquist/claude/agent-mail
---

# agent-mail

skills/johnlindquist/claude/agent-mail
agent-mail
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill agent-mail
SKILL.md
Agent Mail System

Communication system for coordinating multiple agents.

Overview

Agent mail enables:

Message passing between agents
File reservation to prevent conflicts
Session tracking across agents
Thread-based conversations
Session Management
Start Agent Session

Register agent and get inbox:

# Initialize session
curl -X POST http://localhost:3847/api/session/start \
  -H "Content-Type: application/json" \
  -d '{
    "project_path": "/path/to/project",
    "program": "claude-code",
    "model": "opus-4",
    "agent_name": "agent-1",
    "task_description": "Working on auth module"
  }'

List Agents
curl http://localhost:3847/api/agents?project_path=/path/to/project

Agent Info
curl http://localhost:3847/api/agents/agent-1?project_path=/path/to/project

Messaging
Send Message
curl -X POST http://localhost:3847/api/mail/send \
  -H "Content-Type: application/json" \
  -d '{
    "project_path": "/path/to/project",
    "sender_name": "agent-1",
    "to": ["agent-2"],
    "subject": "Auth module complete",
    "body_md": "## Summary\nAuth implementation is done.\n\n## Files changed\n- src/auth/*",
    "importance": "normal",
    "ack_required": false
  }'

Check Inbox
curl "http://localhost:3847/api/mail/inbox?project_path=/path/to/project&agent_name=agent-1"

Reply to Message
curl -X POST http://localhost:3847/api/mail/reply \
  -H "Content-Type: application/json" \
  -d '{
    "project_path": "/path/to/project",
    "message_id": 123,
    "sender_name": "agent-2",
    "body_md": "Thanks! I'\''ll start on the API integration."
  }'

Acknowledge Message
curl -X POST http://localhost:3847/api/mail/ack \
  -H "Content-Type: application/json" \
  -d '{
    "project_path": "/path/to/project",
    "agent_name": "agent-2",
    "message_id": 123
  }'

Search Messages
curl "http://localhost:3847/api/mail/search?project_path=/path/to/project&query=authentication"

File Reservations

Prevent conflicts when multiple agents edit files.

Reserve Files
curl -X POST http://localhost:3847/api/files/reserve \
  -H "Content-Type: application/json" \
  -d '{
    "project_path": "/path/to/project",
    "agent_name": "agent-1",
    "paths": ["src/auth/*.ts", "src/config.ts"],
    "exclusive": true,
    "reason": "Implementing authentication",
    "ttl_seconds": 3600
  }'

Check Reservations
curl "http://localhost:3847/api/files/reservations?project_path=/path/to/project"

Release Files
curl -X POST http://localhost:3847/api/files/release \
  -H "Content-Type: application/json" \
  -d '{
    "project_path": "/path/to/project",
    "agent_name": "agent-1",
    "paths": ["src/auth/*.ts"]
  }'

Thread Management
Get Thread Summary
curl "http://localhost:3847/api/mail/thread/THREAD_ID/summary?project_path=/path/to/project"

Thread Operations

Threads are automatically created when replying to messages.

Coordination Patterns
Task Handoff
Agent 1 completes task:
1. Reserve output files
2. Complete work
3. Send message to Agent 2 with handoff details
4. Release file reservations

Agent 2 receives:
1. Get inbox
2. Reserve input files
3. Continue work
4. Acknowledge receipt

Parallel Work
Coordinator:
1. Reserve coordination files
2. Send tasks to agents
3. Wait for completion messages
4. Merge results

Workers:
1. Reserve assigned files
2. Complete task
3. Send completion message
4. Release files

Review Request
Author:
1. Complete code
2. Send review request to reviewer agents
3. Wait for feedback

Reviewers:
1. Get inbox
2. Review code (read-only, no reservation needed)
3. Send feedback message

Health Check
curl http://localhost:3847/api/health

Message Importance Levels
Level	Use Case
low	FYI, status updates
normal	Standard communication
high	Needs attention soon
urgent	Blocking, needs immediate response
Best Practices
Reserve before editing - Prevent conflicts
Use meaningful subjects - Easy inbox scanning
Acknowledge important - Confirm receipt when ack_required
Release promptly - Don't hold reservations unnecessarily
Use threads - Keep related messages together
Check inbox regularly - Don't miss messages
Handoff cleanly - Include all needed context
Weekly Installs
26
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass