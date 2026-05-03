---
title: work-intake
url: https://skills.sh/nicepkg/ai-workflow/work-intake
---

# work-intake

skills/nicepkg/ai-workflow/work-intake
work-intake
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill work-intake
SKILL.md
Work Intake
Overview

Every work request flows through intake. This skill determines scope, gathers requirements, and routes to the appropriate workflow.

Core principle: No work is too small to track, no work is too large to decompose.

Announce at start: "I'm using work-intake to understand and scope this request before beginning."

The Intake Flow
┌─────────────────────────────────────────────────────────────────────┐
│                        REQUEST RECEIVED                              │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│               STEP 0: PROJECT BOARD READINESS (GATE)                │
│  Is GITHUB_PROJECT_NUM set?                                         │
│  Is project board accessible?                                       │
│  Are required fields configured?                                    │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CLARIFYING QUESTIONS                              │
│  What is the user trying to achieve?                                │
│  What does success look like?                                        │
│  What constraints exist?                                             │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      SCOPE ASSESSMENT                                │
│  How much investigation is needed?                                   │
│  How many deliverables?                                              │
│  How many unknowns?                                                  │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┬───────────────┐
              ▼               ▼               ▼               ▼
         ┌────────┐     ┌──────────┐    ┌──────────┐    ┌──────────┐
         │TRIVIAL │     │  SMALL   │    │  LARGE   │    │ MASSIVE  │
         │        │     │          │    │          │    │          │
         │1 issue │     │1-3 issues│    │1 epic    │    │Initiative│
         │no unkn.│     │few unkn. │    │research  │    │multi-epic│
         └───┬────┘     └────┬─────┘    └────┬─────┘    └────┬─────┘
             │               │               │               │
             ▼               ▼               ▼               ▼
      issue-prerequisite  issue-prerequisite  epic-management  initiative-
      + project-board-    + decomposition    + research spikes  architecture
        enforcement       + project-board-  + project-board-  + project-board-
                           enforcement       enforcement       enforcement

Step 0: Project Board Readiness (GATE)

Before any work intake, verify project board infrastructure is ready.

This is a gate. Do not proceed to clarifying questions until this passes.

# Derive defaults from GITHUB_PROJECT if provided
if [ -z "$GITHUB_PROJECT_NUM" ] && [ -n "$GITHUB_PROJECT" ]; then
  NUM_CANDIDATE=$(echo "$GITHUB_PROJECT" | sed -E 's#.*/projects/([0-9]+).*#\1#')
  if [ -n "$NUM_CANDIDATE" ] && [ "$NUM_CANDIDATE" != "$GITHUB_PROJECT" ]; then
    export GITHUB_PROJECT_NUM="$NUM_CANDIDATE"
    echo "Derived GITHUB_PROJECT_NUM=$GITHUB_PROJECT_NUM from GITHUB_PROJECT"
  fi
fi

if [ -z "$GH_PROJECT_OWNER" ] && [ -n "$GITHUB_OWNER" ]; then
  export GH_PROJECT_OWNER="$GITHUB_OWNER"
  echo "Derived GH_PROJECT_OWNER=$GH_PROJECT_OWNER from GITHUB_OWNER"
fi

if [ -z "$GH_PROJECT_OWNER" ] && [ -n "$GITHUB_PROJECT" ]; then
  OWNER_CANDIDATE=$(echo "$GITHUB_PROJECT" | sed -E 's#https://github.com/(orgs|users)/([^/]+)/projects/[0-9]+#\2#')
  if [ -n "$OWNER_CANDIDATE" ] && [ "$OWNER_CANDIDATE" != "$GITHUB_PROJECT" ]; then
    export GH_PROJECT_OWNER="$OWNER_CANDIDATE"
    echo "Derived GH_PROJECT_OWNER=$GH_PROJECT_OWNER from GITHUB_PROJECT"
  fi
fi

if [ -z "$GH_PROJECT_OWNER" ]; then
  REMOTE_URL=$(git remote get-url origin 2>/dev/null || true)
  OWNER_CANDIDATE=$(echo "$REMOTE_URL" | sed -E 's#(git@|https://)github.com[:/]+([^/]+)/[^/]+(\.git)?#\2#')
  if [ -n "$OWNER_CANDIDATE" ] && [ "$OWNER_CANDIDATE" != "$REMOTE_URL" ]; then
    export GH_PROJECT_OWNER="$OWNER_CANDIDATE"
    echo "Derived GH_PROJECT_OWNER=$GH_PROJECT_OWNER from git remote"
  fi
fi

# Verify environment variables are set
if [ -z "$GITHUB_PROJECT_NUM" ]; then
  echo "BLOCKED: GITHUB_PROJECT_NUM not set"
  echo "Set with: export GITHUB_PROJECT_NUM=<number>"
  exit 1
fi

if [ -z "$GH_PROJECT_OWNER" ]; then
  echo "BLOCKED: GH_PROJECT_OWNER not set"
  echo "Set with: export GH_PROJECT_OWNER=@me  # or org name"
  exit 1
fi

# Verify project is accessible
if ! gh project view "$GITHUB_PROJECT_NUM" --owner "$GH_PROJECT_OWNER" --format json > /dev/null 2>&1; then
  echo "BLOCKED: Cannot access project $GITHUB_PROJECT_NUM"
  echo "Verify project exists and you have access"
  exit 1
fi

# Verify required fields exist
FIELDS=$(gh project field-list "$GITHUB_PROJECT_NUM" --owner "$GH_PROJECT_OWNER" --format json | jq -r '.fields[].name')

for required in "Status" "Priority"; do
  if ! echo "$FIELDS" | grep -q "^$required$"; then
    echo "WARNING: Required field '$required' not found in project"
    echo "Consider adding this field for full tracking support"
  fi
done
if ! echo "$FIELDS" | grep -q "^Type$" && ! echo "$FIELDS" | grep -q "^Issue Type$"; then
  echo "WARNING: Required field 'Type' (or 'Issue Type') not found in project"
  echo "Consider adding this field for full tracking support"
fi

echo "Project board ready: $GITHUB_PROJECT_NUM"


If gate fails:

Configure missing environment variables
Create project board if needed
Add required fields (Status, Type, Priority)
Re-run readiness check

Skill: project-board-enforcement

Step 1: Clarifying Questions

Before scoping, understand the request.

Do not ask questions that can be answered from the repo. First inspect:

README.md, FEATURES.md, BRANDING.md, docs/, Storybook, and existing routes/pages
Existing GitHub issues and project board items

Only ask the user for information that is still missing after reviewing the repo.

Essential Questions
Question	Purpose
"What are you trying to achieve?"	Understand the goal, not just the task
"What does success look like?"	Define acceptance criteria
"Who/what is affected?"	Identify scope of impact
"Are there constraints I should know about?"	Time, tech, compatibility
"Is this part of something larger?"	Link to existing initiatives
Discovery Questions (for unclear requests)
Question	Reveals
"Can you walk me through how this would be used?"	User journey, edge cases
"What exists today?"	Starting point, migration needs
"What have you already tried?"	Failed approaches, constraints
"Is there prior art or examples?"	Design direction
Step 2: Scope Assessment

Evaluate the request against these criteria:

Scope Matrix
Factor	Trivial	Small	Large	Massive
Unknowns	None	Few, answerable	Many, need research	Extensive, need spikes
Deliverables	1 thing	2-5 things	6-20 things	20+ things
Code areas	1-2 files	3-10 files	10+ files	Multiple systems
Dependencies	None	Internal only	External services	New infrastructure
Duration	< 1 session	1-3 sessions	1-2 weeks	Weeks to months
Criteria	1-2	3-5	6-15	15+
Scope Decision
IF unknowns == none AND deliverables <= 2:
  → TRIVIAL: Use issue-prerequisite directly

IF unknowns == few AND deliverables <= 5:
  → SMALL: Use issue-prerequisite, maybe issue-decomposition

IF unknowns == many OR deliverables > 5:
  → LARGE: Use epic-management with research spikes

IF unknowns == extensive OR deliverables > 20 OR new_infrastructure:
  → MASSIVE: Use initiative-architecture

Step 3: Route to Appropriate Workflow
Trivial Scope
**Assessment:** This is a trivial request (single deliverable, no unknowns).

**Next step:** Creating a single issue using `issue-prerequisite`.


Route to: issue-prerequisite

Small Scope
**Assessment:** This is a small request (few deliverables, minimal unknowns).

**Plan:**
1. Create parent issue for the request
2. If needed, decompose into 2-3 sub-issues
3. Begin implementation

**Next step:** Creating issue structure using `issue-prerequisite`.


Route to: issue-prerequisite → maybe issue-decomposition

Large Scope
**Assessment:** This is a large request requiring structured planning.

**Unknowns identified:**
- [ ] Unknown 1 - needs investigation
- [ ] Unknown 2 - needs research spike

**High-level deliverables:**
1. Deliverable A
2. Deliverable B
...

**Next step:** Creating epic structure using `epic-management`.


Route to: epic-management (which will create research spikes as needed)

Massive Scope
**Assessment:** This is a massive request requiring full initiative architecture.

**Why massive:**
- [Reason: extensive unknowns / new infrastructure / multi-system / etc.]

**Initial unknowns:**
- [ ] Does X exist?
- [ ] How does Y work?
- [ ] What are constraints of Z?

**Potential scope:**
- Multiple epics likely
- New capabilities needed
- Significant research required

**Next step:** Beginning initiative architecture using `initiative-architecture`.


Route to: initiative-architecture

Resumability Checkpoint

Before routing, document the intake in memory:

# Store intake assessment
mcp__memory__create_entities([{
  "name": "Intake-[DATE]-[SHORT_DESC]",
  "entityType": "WorkIntake",
  "observations": [
    "Request: [Original request]",
    "Scope: [Trivial/Small/Large/Massive]",
    "Unknowns: [List]",
    "Route: [Target skill]",
    "Status: [Routing/In Progress/Complete]"
  ]
}])

Examples
Example: Trivial

Request: "Make the login page button a little lighter."

Intake:

Goal: Adjust button color
Success: Button is lighter
Unknowns: None (CSS change)
Deliverables: 1 (color change)
Scope: TRIVIAL

→ Route to issue-prerequisite

Example: Large

Request: "Add dark mode to the application."

Intake:

Goal: Theme switching capability
Success: Users can toggle dark/light mode
Unknowns:
Current theming approach?
Component library support?
Persistence mechanism?
Deliverables: ~10 (theme tokens, components, toggle, persistence, etc.)
Scope: LARGE

→ Route to epic-management

Example: Massive

Request: "Add the ability for users to log in by clicking on a popup in their phone."

Intake:

Goal: Mobile push notification login
Success: User receives push, taps, logged in
Unknowns:
Is there a mobile app? → Research spike
Push notification infrastructure? → Research spike
Authentication flow design? → Research spike
Security requirements? → Research spike
Deliverables: 30+ (app work, backend, auth, notifications, etc.)
Scope: MASSIVE

→ Route to initiative-architecture

Red Flags That Indicate Larger Scope

Watch for these phrases that suggest the request is larger than it appears:

Phrase	Likely Scope
"Just add..." + new capability	Large (new capability = infrastructure)
"Users should be able to..."	Large (user-facing = full stack)
"Integrate with..."	Large (external = API, auth, error handling)
"Like [other product]..."	Massive (feature parity = extensive)
"Mobile/app/notification"	Massive (unless app exists)
"Real-time/sync/live"	Large (infrastructure)
Never Turn Away Work

No matter how massive the request:

Acknowledge the goal - "I understand you want X"
Explain the process - "This will require structured planning"
Begin investigation - Start with what we don't know
Document everything - Every decision, every finding
Break it down - Until we have tractable pieces

The path from "massive request" to "implementation" is:

Massive Request
    → Initiative Architecture (document unknowns, create research spikes)
    → Research Spikes (answer unknowns)
    → Epic Structure (group deliverables)
    → Issue Decomposition (create tractable tasks)
    → Implementation (one issue at a time)

Checklist
 Project board readiness verified (Step 0 gate passed)
 GITHUB_PROJECT_NUM and GH_PROJECT_OWNER set
 Asked clarifying questions
 Understood the goal (not just the task)
 Identified unknowns
 Counted deliverables
 Assessed scope (Trivial/Small/Large/Massive)
 Documented intake in memory
 Routed to appropriate skill (with project-board-enforcement)

Skill: project-board-enforcement

Gate: Cannot proceed to any downstream skill without project board readiness verified.

Weekly Installs
28
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn