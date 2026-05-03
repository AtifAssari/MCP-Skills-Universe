---
rating: ⭐⭐⭐
title: ralph-tui-create-beads
url: https://skills.sh/subsy/ralph-tui/ralph-tui-create-beads
---

# ralph-tui-create-beads

skills/subsy/ralph-tui/ralph-tui-create-beads
ralph-tui-create-beads
Installation
$ npx skills add https://github.com/subsy/ralph-tui --skill ralph-tui-create-beads
Summary

Convert PRDs to beads (epic + child tasks) for ralph-tui autonomous execution.

Extracts quality gates from PRD and appends them to every bead's acceptance criteria, ensuring consistent validation across all stories
Creates an epic with right-sized child beads, where each story is completable in a single ralph-tui iteration without context overflow
Establishes dependencies between beads using bd dep add to enforce correct execution order: schema → backend → UI → integration
Outputs beads to .beads/beads.jsonl ready for ralph-tui run --tracker beads, with support for browser verification gates on UI stories
SKILL.md
Ralph TUI - Create Beads

Converts PRDs to beads (epic + child tasks) for ralph-tui autonomous execution.

Note: This skill is bundled with ralph-tui's Beads tracker plugin. Future tracker plugins (Linear, GitHub Issues, etc.) will bundle their own task creation skills.

The Job

Take a PRD (markdown file or text) and create beads in .beads/beads.jsonl:

Extract Quality Gates from the PRD's "Quality Gates" section
Create an epic bead for the feature
Create child beads for each user story (with quality gates appended)
Set up dependencies between beads (schema → backend → UI)
Output ready for ralph-tui run --tracker beads
Step 1: Extract Quality Gates

Look for the "Quality Gates" section in the PRD:

## Quality Gates

These commands must pass for every user story:
- `pnpm typecheck` - Type checking
- `pnpm lint` - Linting

For UI stories, also include:
- Verify in browser using dev-browser skill


Extract:

Universal gates: Commands that apply to ALL stories (e.g., pnpm typecheck)
UI gates: Commands that apply only to UI stories (e.g., browser verification)

If no Quality Gates section exists: Ask the user what commands should pass, or use a sensible default like npm run typecheck.

Output Format

Beads use bd create command with HEREDOC syntax to safely handle special characters:

# Create epic (link back to source PRD)
bd create --type=epic \
  --title="[Feature Name]" \
  --description="$(cat <<'EOF'
[Feature description from PRD]
EOF
)" \
  --external-ref="prd:./tasks/feature-name-prd.md"

# Create child bead (with quality gates in acceptance criteria)
bd create \
  --parent=EPIC_ID \
  --title="[Story Title]" \
  --description="$(cat <<'EOF'
[Story description with acceptance criteria INCLUDING quality gates]
EOF
)" \
  --priority=[1-4]


CRITICAL: Always use <<'EOF' (single-quoted) for the HEREDOC delimiter. This prevents shell interpretation of backticks, $variables, and () in descriptions.

Story Size: The #1 Rule

Each story must be completable in ONE ralph-tui iteration (~one agent context window).

ralph-tui spawns a fresh agent instance per iteration with no memory of previous work. If a story is too big, the agent runs out of context before finishing.

Right-sized stories:
Add a database column + migration
Add a UI component to an existing page
Update a server action with new logic
Add a filter dropdown to a list
Too big (split these):
"Build the entire dashboard" → Split into: schema, queries, UI components, filters
"Add authentication" → Split into: schema, middleware, login UI, session handling
"Refactor the API" → Split into one story per endpoint or pattern

Rule of thumb: If you can't describe the change in 2-3 sentences, it's too big.

Story Ordering: Dependencies First

Stories execute in dependency order. Earlier stories must not depend on later ones.

Correct order:

Schema/database changes (migrations)
Server actions / backend logic
UI components that use the backend
Dashboard/summary views that aggregate data

Wrong order:

❌ UI component (depends on schema that doesn't exist yet)
❌ Schema change
Dependencies with bd dep add

Use the bd dep add command to specify which beads must complete first:

# Create the beads first
bd create --parent=epic-123 --title="US-001: Add schema" ...
bd create --parent=epic-123 --title="US-002: Create API" ...
bd create --parent=epic-123 --title="US-003: Build UI" ...

# Then add dependencies (issue depends-on blocker)
bd dep add ralph-tui-002 ralph-tui-001  # US-002 depends on US-001
bd dep add ralph-tui-003 ralph-tui-002  # US-003 depends on US-002


Syntax: bd dep add <issue> <depends-on> — the issue depends on (is blocked by) depends-on.

ralph-tui will:

Show blocked beads as "blocked" until dependencies complete
Never select a bead for execution while its dependencies are open
Include dependency context in the prompt when working on a bead

Correct dependency order:

Schema/database changes (no dependencies)
Backend logic (depends on schema)
UI components (depends on backend)
Integration/polish (depends on UI)
Acceptance Criteria: Quality Gates + Story-Specific

Each bead's description should include acceptance criteria with:

Story-specific criteria from the PRD (what this story accomplishes)
Quality gates from the PRD's Quality Gates section (appended at the end)
Good criteria (verifiable):
"Add investorType column to investor table with default 'cold'"
"Filter dropdown has options: All, Cold, Friend"
"Clicking toggle shows confirmation dialog"
Bad criteria (vague):
❌ "Works correctly"
❌ "User can do X easily"
❌ "Good UX"
❌ "Handles edge cases"
Conversion Rules
Extract Quality Gates from PRD first
Each user story → one bead
First story: No dependencies (creates foundation)
Subsequent stories: Depend on their predecessors (UI depends on backend, etc.)
Priority: Based on dependency order, then document order (0=critical, 2=medium, 4=backlog)
All stories: status: "open"
Acceptance criteria: Story criteria + quality gates appended
UI stories: Also append UI-specific gates (browser verification)
Splitting Large PRDs

If a PRD has big features, split them:

Original:

"Add friends outreach track with different messaging"

Split into:

US-001: Add investorType field to database
US-002: Add type toggle to investor list UI
US-003: Create friend-specific phase progression logic
US-004: Create friend message templates
US-005: Wire up task generation for friends
US-006: Add filter by type
US-007: Update new investor form
US-008: Update dashboard counts

Each is one focused change that can be completed and verified independently.

Example

Input PRD:

# PRD: Friends Outreach

Add ability to mark investors as "friends" for warm outreach.

## Quality Gates

These commands must pass for every user story:
- `pnpm typecheck` - Type checking
- `pnpm lint` - Linting

For UI stories, also include:
- Verify in browser using dev-browser skill

## User Stories

### US-001: Add investorType field to investor table
**Description:** As a developer, I need to categorize investors as 'cold' or 'friend'.

**Acceptance Criteria:**
- [ ] Add investorType column: 'cold' | 'friend' (default 'cold')
- [ ] Generate and run migration successfully

### US-002: Add type toggle to investor list rows
**Description:** As Ryan, I want to toggle investor type directly from the list.

**Acceptance Criteria:**
- [ ] Each row has Cold | Friend toggle
- [ ] Switching shows confirmation dialog
- [ ] On confirm: updates type in database

### US-003: Filter investors by type
**Description:** As Ryan, I want to filter the list to see just friends or cold.

**Acceptance Criteria:**
- [ ] Filter dropdown: All | Cold | Friend
- [ ] Filter persists in URL params


Output beads:

# Create epic (link back to source PRD)
bd create --type=epic \
  --title="Friends Outreach Track" \
  --description="$(cat <<'EOF'
Warm outreach for deck feedback
EOF
)" \
  --external-ref="prd:./tasks/friends-outreach-prd.md"

# US-001: No deps (first - creates schema)
bd create --parent=ralph-tui-abc \
  --title="US-001: Add investorType field to investor table" \
  --description="$(cat <<'EOF'
As a developer, I need to categorize investors as 'cold' or 'friend'.

## Acceptance Criteria
- [ ] Add investorType column: 'cold' | 'friend' (default 'cold')
- [ ] Generate and run migration successfully
- [ ] pnpm typecheck passes
- [ ] pnpm lint passes
EOF
)" \
  --priority=1

# US-002: UI story (gets browser verification too)
bd create --parent=ralph-tui-abc \
  --title="US-002: Add type toggle to investor list rows" \
  --description="$(cat <<'EOF'
As Ryan, I want to toggle investor type directly from the list.

## Acceptance Criteria
- [ ] Each row has Cold | Friend toggle
- [ ] Switching shows confirmation dialog
- [ ] On confirm: updates type in database
- [ ] pnpm typecheck passes
- [ ] pnpm lint passes
- [ ] Verify in browser using dev-browser skill
EOF
)" \
  --priority=2

# Add dependency: US-002 depends on US-001
bd dep add ralph-tui-002 ralph-tui-001

# US-003: UI story
bd create --parent=ralph-tui-abc \
  --title="US-003: Filter investors by type" \
  --description="$(cat <<'EOF'
As Ryan, I want to filter the list to see just friends or cold.

## Acceptance Criteria
- [ ] Filter dropdown: All | Cold | Friend
- [ ] Filter persists in URL params
- [ ] pnpm typecheck passes
- [ ] pnpm lint passes
- [ ] Verify in browser using dev-browser skill
EOF
)" \
  --priority=3

# Add dependency: US-003 depends on US-002
bd dep add ralph-tui-003 ralph-tui-002

Output Location

Beads are written to: .beads/beads.jsonl

After creation, run ralph-tui:

# Work on a specific epic
ralph-tui run --tracker beads --epic ralph-tui-abc

# Or let it pick the best task automatically
ralph-tui run --tracker beads


ralph-tui will:

Work on beads within the specified epic (or select the best available task)
Close each bead when complete
Close the epic when all children are done
Output <promise>COMPLETE</promise> when epic is done
Checklist Before Creating Beads
 Extracted Quality Gates from PRD (or asked user if missing)
 Each story is completable in one iteration (small enough)
 Stories are ordered by dependency (schema → backend → UI)
 Quality gates appended to every bead's acceptance criteria
 UI stories have browser verification (if specified in Quality Gates)
 Acceptance criteria are verifiable (not vague)
 No story depends on a later story (only earlier stories)
 Dependencies added with bd dep add after creating beads
Weekly Installs
754
Repository
subsy/ralph-tui
GitHub Stars
2.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass