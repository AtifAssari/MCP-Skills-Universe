---
title: team-communication-protocols
url: https://skills.sh/wshobson/agents/team-communication-protocols
---

# team-communication-protocols

skills/wshobson/agents/team-communication-protocols
team-communication-protocols
Installation
$ npx skills add https://github.com/wshobson/agents --skill team-communication-protocols
Summary

Structured messaging protocols for coordinating agent teams through direct messages, broadcasts, plan approvals, and graceful shutdown.

Three message types: message for direct teammate coordination, broadcast for critical shared-resource updates, and shutdown_request for graceful termination with approval workflows
Plan approval workflow where teammates in plan mode submit proposals to a lead for review and feedback before execution
Shutdown protocol with rejection handling: lead sends requests, teammates respond with approval or reason, and lead retries or waits for task completion
Teammate discovery via config file using teammate names (not UUIDs) for all messaging and task assignment
Common anti-patterns documented: broadcasting routine updates, sending JSON status messages, ignoring idle teammates, and micromanaging via excessive messages
SKILL.md
Team Communication Protocols

Protocols for effective communication between agent teammates, including message type selection, plan approval workflows, shutdown procedures, and common anti-patterns to avoid.

When to Use This Skill
Establishing communication norms for a new team
Choosing between message types (message, broadcast, shutdown_request)
Handling plan approval workflows
Managing graceful team shutdown
Discovering teammate identities and capabilities
Message Type Selection
message (Direct Message) — Default Choice

Send to a single specific teammate:

{
  "type": "message",
  "recipient": "implementer-1",
  "content": "Your API endpoint is ready. You can now build the frontend form.",
  "summary": "API endpoint ready for frontend"
}


Use for: Task updates, coordination, questions, integration notifications.

broadcast — Use Sparingly

Send to ALL teammates simultaneously:

{
  "type": "broadcast",
  "content": "Critical: shared types file has been updated. Pull latest before continuing.",
  "summary": "Shared types updated"
}


Use ONLY for: Critical blockers affecting everyone, major changes to shared resources.

Why sparingly?: Each broadcast sends N separate messages (one per teammate), consuming API resources proportional to team size.

shutdown_request — Graceful Termination

Request a teammate to shut down:

{
  "type": "shutdown_request",
  "recipient": "reviewer-1",
  "content": "Review complete, shutting down team."
}


The teammate responds with shutdown_response (approve or reject with reason).

Communication Anti-Patterns
Anti-Pattern	Problem	Better Approach
Broadcasting routine updates	Wastes resources, noise	Direct message to affected teammate
Sending JSON status messages	Not designed for structured data	Use TaskUpdate to update task status
Not communicating at integration points	Teammates build against stale interfaces	Message when your interface is ready
Micromanaging via messages	Overwhelms teammates, slows work	Check in at milestones, not every step
Using UUIDs instead of names	Hard to read, error-prone	Always use teammate names
Ignoring idle teammates	Wasted capacity	Assign new work or shut down
Plan Approval Workflow

When a teammate is spawned with plan_mode_required:

Teammate creates a plan using read-only exploration tools
Teammate calls ExitPlanMode which sends a plan_approval_request to the lead
Lead reviews the plan
Lead responds with plan_approval_response:

Approve:

{
  "type": "plan_approval_response",
  "request_id": "abc-123",
  "recipient": "implementer-1",
  "approve": true
}


Reject with feedback:

{
  "type": "plan_approval_response",
  "request_id": "abc-123",
  "recipient": "implementer-1",
  "approve": false,
  "content": "Please add error handling for the API calls"
}

Shutdown Protocol
Graceful Shutdown Sequence
Lead sends shutdown_request to each teammate
Teammate receives request as a JSON message with type: "shutdown_request"
Teammate responds with shutdown_response:
approve: true — Teammate saves state and exits
approve: false + reason — Teammate continues working
Lead handles rejections — Wait for teammate to finish, then retry
After all teammates shut down — Call TeamDelete to remove team resources
Handling Rejections

If a teammate rejects shutdown:

Check their reason (usually "still working on task")
Wait for their current task to complete
Retry shutdown request
If urgent, user can force shutdown
Teammate Discovery

Find team members by reading the config file:

Location: ~/.claude/teams/{team-name}/config.json

Structure:

{
  "members": [
    {
      "name": "security-reviewer",
      "agentId": "uuid-here",
      "agentType": "team-reviewer"
    },
    {
      "name": "perf-reviewer",
      "agentId": "uuid-here",
      "agentType": "team-reviewer"
    }
  ]
}


Always use name for messaging and task assignment. Never use agentId directly.

Troubleshooting

A teammate is not responding to messages. Check the teammate's task status. If it is idle, it may have completed its task and is waiting to be assigned new work or shut down. If it is still active, it may be mid-execution and will process messages once the current operation finishes.

The lead is sending broadcasts for every status update. This is a common anti-pattern. Broadcasts are expensive — each one sends N messages. Use direct messages (type: "message") for point-to-point updates. Reserve broadcasts for critical shared-resource changes like an updated interface contract.

A teammate rejected a shutdown request unexpectedly. The teammate is still working. Check the rejection reason in the shutdown_response content field, wait for the work to finish, then retry. Never force-terminate a teammate that has unsaved work.

A plan_approval_request arrived but the request_id is missing. The teammate called ExitPlanMode without the required request context. Have the teammate re-enter plan mode, complete exploration, and call ExitPlanMode again. The request_id is generated automatically by the plan mode system.

Two teammates are waiting on each other and neither is making progress. This is a deadlock: both are blocked waiting for the other to finish first. The lead should send a direct message to one teammate with a stub or partial result so it can unblock and proceed.

Related Skills
team-composition-patterns — Select agent types and team size before establishing communication norms
parallel-feature-development — Use communication protocols to coordinate integration handoffs between parallel implementers
Weekly Installs
4.6K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass