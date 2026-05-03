---
rating: ⭐⭐⭐
title: manage-backlog
url: https://skills.sh/pjt222/development-guides/manage-backlog
---

# manage-backlog

skills/pjt222/development-guides/manage-backlog
manage-backlog
Installation
$ npx skills add https://github.com/pjt222/development-guides --skill manage-backlog
SKILL.md
Manage a Product Backlog

Create, prioritize, and maintain a backlog of work items that serves as the single source of truth for what needs to be done, applicable to both agile and classic project methodologies.

When to Use
Starting a new project and converting scope into actionable items
Ongoing backlog grooming before sprint planning
Re-prioritizing work after stakeholder feedback or scope changes
Splitting oversized items into implementable pieces
Reviewing and archiving completed or cancelled items
Inputs
Required: Project scope (from charter, WBS, or stakeholder input)
Optional: Existing backlog file (BACKLOG.md) to update
Optional: Prioritization framework preference (MoSCoW, value/effort, WSJF)
Optional: Estimation scale (story points, T-shirt sizes, person-days)
Optional: Sprint or iteration feedback requiring backlog updates
Procedure
Step 1: Create or Load Backlog Structure

If no backlog exists, create BACKLOG.md with standard columns. If one exists, read and validate structure.

# Product Backlog: [Project Name]
## Last Updated: [YYYY-MM-DD]

### Summary
- **Total Items**: [N]
- **Ready for Sprint**: [N]
- **In Progress**: [N]
- **Done**: [N]
- **Cancelled**: [N]

### Backlog Items
| ID | Title | Type | Priority | Estimate | Status | Sprint |
|----|-------|------|----------|----------|--------|--------|
| B-001 | [Title] | Feature | Must | 5 | Ready | — |
| B-002 | [Title] | Bug | Should | 2 | Ready | — |
| B-003 | [Title] | Task | Could | 3 | New | — |

### Item Details

#### B-001: [Title]
- **Type**: Feature | Bug | Task | Spike | Tech Debt
- **Priority**: Must | Should | Could | Won't
- **Estimate**: [Points or size]
- **Status**: New | Ready | In Progress | Done | Cancelled
- **Acceptance Criteria**:
  - [ ] [Criterion 1]
  - [ ] [Criterion 2]
- **Notes**: [Context, links, dependencies]

#### B-002: [Title]
...


Expected: BACKLOG.md exists with valid structure and summary statistics.

On failure: If the file is malformed, restructure it preserving existing item data.

Step 2: Write or Refine Items

For each new item, write it as a user story or requirement:

User story format: "As a [role], I want [capability] so that [benefit]"
Requirement format: "[System/Component] shall [behavior] when [condition]"

Each item must have:

Unique ID (B-NNN, incrementing)
Clear title (imperative verb form)
Type classification
At least 2 acceptance criteria (testable, binary pass/fail)

Example:

#### B-005: Enable User Login with OAuth
- **Type**: Feature
- **Priority**: Must
- **Estimate**: 5
- **Status**: Ready
- **Acceptance Criteria**:
  - [ ] User can log in using GitHub OAuth
  - [ ] User session persists for 24 hours
  - [ ] Failed login shows clear error message
- **Notes**: Requires OAuth app registration in GitHub


Expected: All items have titles, types, and acceptance criteria.

On failure: Items without acceptance criteria are marked Status: New (not Ready). They cannot enter a sprint.

Step 3: Prioritize Using MoSCoW or Value/Effort

Apply the chosen prioritization framework:

MoSCoW (default):

Must: Project fails without this. Non-negotiable.
Should: Important but project can succeed without it. Include if capacity allows.
Could: Nice to have. Include only if no impact on Must/Should items.
Won't: Explicitly excluded from current scope. Documented for future consideration.

Value/Effort Matrix (alternative):

	Low Effort	High Effort
High Value	Do First (Quick Wins)	Do Second (Big Bets)
Low Value	Do Third (Fill-ins)	Don't Do (Money Pits)

Sort the backlog table: Must items first (by value within Must), then Should, then Could.

Expected: Every item has a priority. Backlog is sorted by priority.

On failure: If stakeholders disagree on priorities, escalate Must vs Should decisions to the project sponsor.

Step 4: Groom — Split, Estimate, and Refine

Review items for sprint-readiness. For each item:

Split if estimate > 8 points (or > 1 week effort): decompose into 2-4 smaller items
Estimate using the project's chosen scale
Refine vague acceptance criteria into testable conditions
Mark Ready when the item has title, acceptance criteria, estimate, and no blockers

Document splitting:

**Split**: B-003 split into B-003a, B-003b, B-003c (original archived)

#### B-003a: Set Up Database Schema
- **Type**: Task
- **Priority**: Must
- **Estimate**: 3
- **Status**: Ready
- **Acceptance Criteria**:
  - [ ] Users table created with email, name fields
  - [ ] Migrations run successfully on dev environment

#### B-003b: Implement User CRUD Operations
- **Type**: Task
- **Priority**: Must
- **Estimate**: 5
- **Status**: Ready
- **Acceptance Criteria**:
  - [ ] Create user endpoint returns 201 with user object
  - [ ] Update user endpoint validates required fields


Expected: All Must and Should items are in Ready status.

On failure: Items that can't be estimated need a Spike (time-boxed research task) added to the backlog.

Step 5: Update Summary and Archive

Update the summary statistics. Move Done and Cancelled items to an archive section:

### Archive
| ID | Title | Status | Sprint | Completed |
|----|-------|--------|--------|-----------|
| B-001 | Enable User Login with OAuth | Done | S-003 | 2025-03-15 |
| B-004 | Add Dark Mode Theme | Cancelled | — | 2025-03-10 |


Update the summary by counting items in each status:

# Count Ready items
grep "| Ready |" BACKLOG.md | wc -l

# Count In Progress items
grep "| In Progress |" BACKLOG.md | wc -l

# Count Done items
grep "| Done |" BACKLOG.md | wc -l


Expected: Summary statistics match actual item counts. Archive section contains all closed items.

On failure: If counts don't match, recount by grepping Status values and update the summary manually.

Validation
 BACKLOG.md exists with standard structure
 Every item has a unique ID, title, type, priority, and status
 All Must and Should items have acceptance criteria
 Items are sorted by priority (Must first, then Should, then Could)
 No item estimated at > 8 points without being split
 Summary statistics are accurate
 Done/Cancelled items are archived
Common Pitfalls
No acceptance criteria: Items without criteria can't be verified as done. Every item needs at least 2 testable criteria.
Everything is Must priority: If >50% of items are Must, priorities are not real. Force-rank within Must.
Zombie items: Items sitting in the backlog for months without progress should be re-evaluated or cancelled.
Estimates without context: Story points are relative — a team must have a reference item (e.g., "B-001 is our 3-point reference").
Splitting creates fragments: When splitting, ensure each child item is independently deliverable and valuable.
Backlog as dumping ground: The backlog is not a wish list. Regularly prune items that no longer align with project goals.
Missing dependencies: Note blocking items in the Notes field. A blocked item should not be marked Ready.
Related Skills
draft-project-charter — charter scope feeds initial backlog creation
create-work-breakdown-structure — WBS work packages can become backlog items
plan-sprint — sprint planning selects from the top of the backlog
generate-status-report — backlog burn-down feeds status reports
conduct-retrospective — retrospective improvement items feed back into the backlog
Weekly Installs
15
Repository
pjt222/developm…t-guides
GitHub Stars
12
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass