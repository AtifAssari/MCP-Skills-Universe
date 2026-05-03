---
title: ralph
url: https://skills.sh/scando1993/sugar/ralph
---

# ralph

skills/scando1993/sugar/ralph
ralph
Installation
$ npx skills add https://github.com/scando1993/sugar --skill ralph
SKILL.md
Ralph PRD Converter

Converts existing PRDs to prd.json — the format that drives Ralph-style autonomous agent loops.

Output Format
{
  "project": "[Project Name]",
  "branchName": "phase-a-[scope-kebab-case]",
  "description": "[Feature description]",
  "userStories": [
    {
      "id": "US-001",
      "title": "[Story title]",
      "description": "As a [user], I want [feature] so that [benefit]",
      "acceptanceCriteria": [
        "Criterion 1",
        "Criterion 2",
        "Typecheck passes"
      ],
      "priority": 1,
      "status": "pending",
      "term": 0,
      "votes": [],
      "notes": ""
    }
  ]
}

The Number One Rule: Story Size

Each story must be completable in ONE agent pass (one context window).

Right-sized:

Add a database column and migration
Add a UI component to an existing page
Update a server action with new logic
Write tests for one module

Too big (split these):

"Build the entire dashboard" → split into schema, queries, components, filters
"Add authentication" → split into schema, middleware, login UI, session handling

Rule of thumb: If you cannot describe the change in 2-3 sentences, split it.

Story Ordering: Dependencies First

Stories execute in priority order. Earlier stories must not depend on later ones.

Correct order:

Schema / database changes (migrations)
Server actions / backend logic
UI components that use the backend
Dashboard / summary views that aggregate data
Acceptance Criteria: Must Be Verifiable

Each criterion must be something an agent can CHECK.

Good: "Add status column to tasks table with default 'pending'" Bad: "Works correctly"

Always include as final criterion: "Typecheck passes" For testable logic: also include "Tests pass"

Conversion Rules
Each user story becomes one JSON entry
IDs: Sequential (US-001, US-002, etc.)
Priority: Based on dependency order, then document order
All stories start with status: "pending", term: 0, votes: [], and empty notes
branchName: Derive from feature name, kebab-case
Always add "Typecheck passes" to every story
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"This story is small enough to combine with the next one"	If it has its own acceptance criteria, it's its own story.
"I don't need Typecheck passes for this one"	EVERY story includes "Typecheck passes". No exceptions.
"This description is obvious, no need for detail"	An agent with ZERO context will read this. Be explicit.
Consensus Format Example

For consensus mode, add a consensus config to the prd.json root and set initial story fields:

{
  "project": "my-app",
  "branchName": "phase-a-feature",
  "description": "Feature with consensus verification",
  "consensus": {
    "quorumSize": 3,
    "requiredMajority": 2,
    "implementModel": "sonnet",
    "verifyModel": "sonnet",
    "escalationModel": "opus",
    "maxTerms": 5
  },
  "userStories": [
    {
      "id": "US-001",
      "title": "Example story",
      "description": "As a developer, I need...",
      "acceptanceCriteria": ["Criterion 1", "Typecheck passes"],
      "priority": 1,
      "status": "pending",
      "term": 0,
      "votes": [],
      "notes": ""
    }
  ]
}

Splitting Large PRDs

Original: "Add user notification system"

Split into:

US-001: Add notifications table to database
US-002: Create notification service
US-003: Add notification bell icon to header
US-004: Create notification dropdown panel
US-005: Add mark-as-read functionality

Each is one focused change that can be completed and verified independently.

Weekly Installs
12
Repository
scando1993/sugar
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass