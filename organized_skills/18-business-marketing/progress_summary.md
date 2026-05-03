---
rating: ⭐⭐⭐
title: progress-summary
url: https://skills.sh/epicenterhq/epicenter/progress-summary
---

# progress-summary

skills/epicenterhq/epicenter/progress-summary
progress-summary
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill progress-summary
SKILL.md
Progress Summary

Generate conversational summaries of work in progress, using the same style as well-crafted PR descriptions.

Core Principles
Motivation First

Every summary starts with WHY. Not what files changed, not how it works—WHY this work matters.

Good opening:

We've been tackling the session timeout issue that was logging users out mid-upload. The root cause was the session refresh only triggering on navigation, not during background activity.

Bad opening:

We added a keepalive call to the upload handler and updated the session refresh logic.

The reader should understand the PROBLEM before seeing the SOLUTION.

Show Your Thinking

Summaries should reveal the decision-making process:

"We considered X, but Y made more sense because..."
"Initially tried A, which revealed B, leading us to C"
"The tricky part was figuring out where to hook into the existing flow"
Conversational but Precise

Write like explaining to a colleague over coffee. Direct and honest.

"This has been painful" rather than "This presented challenges"
"We hit a wall with" rather than "We encountered difficulties"
Use "we" for collaborative work, "I" for personal observations
Summary Types
Quick Status (verbal check-in)

For "what are you working on" or brief updates:

Working on the auth timeout issue. Found the root cause: session refresh
only fires on navigation, not background activity. Currently implementing
a keepalive mechanism in the upload handler.


2-4 sentences. Problem, finding, current action.

Session Recap (end of work session)

For "summarize what we did" or wrapping up:

Structure:

What problem we tackled
Key decisions made (and why)
What's working now
What's left to do

Example:

We tackled the nested reactivity problem in state management. Users found
it cumbersome to create deeply reactive state with manual get/set properties.

After exploring several approaches, we landed on proxy-based reactivity
because it lets you write idiomatic JavaScript while we get the performance
benefits of immutability under the hood.

The core implementation is working. Still need to optimize for large arrays
and update the migration guide.

Architecture Overview (explaining a complex change)

For "explain what's happening here" on larger work:

Use ASCII diagrams liberally. They're more scannable than prose.

Journey/Evolution Diagrams (when work iterates on previous attempts):

┌─────────────────────────────────────────────────────────────────┐
│  First attempt: Direct Y.Map                                     │
│  Problem: 524,985 bytes storage overhead                         │
└───────────────────────────────────────┬─────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────┐
│  Second attempt: YKeyValue wrapper                               │
│  Result: 271 bytes (1935x improvement!)                          │
│  Problem: Unpredictable conflict resolution                      │
└───────────────────────────────────────┬─────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────┐
│  Current: YKeyValue with LWW timestamps                          │
│  Keeps the storage wins, adds predictable "latest wins"          │
└─────────────────────────────────────────────────────────────────┘


Layer Diagrams (for architectural changes):

┌─────────────────────────────────────────────────────────────────┐
│  defineWorkspace() + workspace.create()                          │  ← High-level
│    Creates Y.Doc internally, binds tables/kv/capabilities        │
├─────────────────────────────────────────────────────────────────┤
│  createTables(ydoc, {...}) / createKv(ydoc, {...})               │  ← Mid-level
│    Binds to existing Y.Doc                                       │
├─────────────────────────────────────────────────────────────────┤
│  defineTable() / defineKv()                                      │  ← Low-level
│    Pure schema definitions                                       │
└─────────────────────────────────────────────────────────────────┘


Flow Diagrams (for data/control flow):

┌────────────────────────────────────────────────────────────────┐
│  Client A (2:00pm)  ──┐                                        │
│                       │──→  Sync  ──→  Winner: Client B        │
│  Client B (3:00pm)  ──┘                                        │
│                                                                │
│  With timestamps: Latest always wins                           │
│  Without: Whoever syncs first wins (unpredictable)             │
└────────────────────────────────────────────────────────────────┘


Comparison Tables (for trade-offs):

┌────────────────────────────────────┬────────────────────────────┐
│  Use Case                          │  Recommendation            │
├────────────────────────────────────┼────────────────────────────┤
│  Real-time collab, simple cases    │  YKeyValue (positional)    │
│  Offline-first, multi-device       │  YKeyValueLww (timestamp)  │
│  Clock sync unreliable             │  YKeyValue (no clock dep)  │
└────────────────────────────────────┴────────────────────────────┘

When to Use Diagrams
Journey diagrams: Work iterates on previous attempts or fixes past decisions
Layer diagrams: Architectural changes with distinct levels
Comparison tables: Trade-offs between approaches
Flow diagrams: How data or control moves between components
What to Avoid
Listing files changed: "Updated auth.ts, session.ts, and upload.ts" — just explain what and why
Corporate speak: "This enhancement leverages our existing infrastructure"
Marketing language: "game-changing", "revolutionary", "seamless"
Dramatic hyperbole: "excruciating pain point" — stick to facts
Bullet point everything: Use flowing paragraphs when possible
Over-explaining simple changes: Match the explanation depth to the complexity
Gathering Context for Summaries

To generate a summary, gather relevant context:

# Current branch state
git status
git log --oneline -10

# What changed from main
git diff main...HEAD --stat
git log main..HEAD --oneline

# Recent activity
git log --oneline --since="1 hour ago"


For Conductor workspaces, use GetWorkspaceDiff to see the full diff.

Read key files that were modified to understand the substance of changes, not just the diff stats.

ASCII Art Characters

For clean diagrams: ┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼ ▼ ▲ ◀ ▶ ──→ ←──

Keep box edges aligned. Use consistent spacing inside boxes.

Weekly Installs
52
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass