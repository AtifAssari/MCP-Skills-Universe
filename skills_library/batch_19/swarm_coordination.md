---
title: swarm-coordination
url: https://skills.sh/dralgorhythm/claude-agentic-framework/swarm-coordination
---

# swarm-coordination

skills/dralgorhythm/claude-agentic-framework/swarm-coordination
swarm-coordination
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill swarm-coordination
SKILL.md
Swarm Coordination

Protocols and patterns for consistent, conflict-free multi-agent development. Follow these guidelines when working alongside other Claude Code agents in the same codebase.

Core Principles
Beads as Source of Truth: All work items tracked via bd commands
File Locking: Hooks automatically manage file locks - respect them
Session Isolation: Each agent has a unique session ID for tracking
Clean Handoffs: Always leave state that another agent can continue
File-Based Output

Workers write results to scratchpad/<task-id>.md, not direct context. Only durable artifacts (ADRs, plans, PRDs) go to artifacts/. Orchestrator creates output targets before launching workers; workers write to assigned files; orchestrator reads and synthesizes.

Workflows
Starting Work
 Check Beads: Run bd ready to find unblocked issues
 Claim Work: Update issue status: bd update <id> --status in_progress
 Check Conflicts: Review .claude/hooks/.file-tracker.log for recent edits
 Coordinate: If another agent is active, coordinate via Beads comments
During Work
 Atomic Changes: Make small, complete changes that don't leave broken state
 Frequent Commits: Commit often to reduce merge conflicts
 Update Progress: Add comments to Beads issues for visibility
 Respect Locks: If a file is locked, wait or work on something else
Completing Work
 Run Tests: Verify changes don't break existing functionality
 Close Issue: bd close <id> --reason "Completed: <description>"
 Sync Beads: bd sync to share updates with other agents
 Clean State: Commit all changes, leave no uncommitted work
Conflict Prevention
File Lock Protocol

Hooks automatically acquire/release locks. If you encounter a lock:

# Check who holds the lock
cat .claude/hooks/.locks/<filename>.lock

# Lock automatically expires after 60 seconds
# If urgent, coordinate via Beads or wait

Merge Conflict Strategy
Pull frequently: Keep your branch up to date
Small PRs: Easier to merge than large changes
Coordinate: Use Beads to claim files/features before editing
Resolve quickly: Address conflicts immediately when detected
Communication Patterns
Handoff Message

When ending a session with incomplete work:

# Create handoff for next agent
echo '{"message": "Continue implementing auth middleware. Tests passing but needs error handling in src/auth.ts:45"}' > .claude/hooks/.state/handoff.json

Issue Comments (via Beads)
# Add context for other agents
bd comment <issue-id> "Implemented base class. Needs: validation, tests, docs"

Multi-Agent Patterns
Queen-Worker Pattern

For complex tasks, one agent orchestrates while others execute:

Queen: Plans, decomposes, assigns via Beads
Workers: Claim issues, implement, report completion
Sync Point: All workers sync before final integration
Parallel Streams

For independent features:

Create separate Beads issues for each stream
Each agent claims one stream
Avoid editing same files across streams
Merge streams at defined integration points
State Files
File	Purpose
.claude/hooks/.state/session_*.json	Active agent sessions
.claude/hooks/.state/handoff.json	Handoff messages between sessions
.claude/hooks/.locks/*.lock	File edit locks
.claude/hooks/.file-tracker.log	Recent file modifications
Best Practices
Check Before Edit: Always verify no active locks on target files
Complete Units: Finish logical units of work before switching
Document Intent: Use Beads issues to declare what you're working on
Test Locally: Run tests before pushing to catch issues early
Sync Often: Keep Beads and git in sync with other agents
Emergency Procedures
Deadlock Detection

If agents are waiting on each other:

# Check active sessions
ls -la .claude/hooks/.state/session_*.json

# Check active locks
ls -la .claude/hooks/.locks/

# Force release stale locks (use with caution)
find .claude/hooks/.locks -mmin +5 -delete

Recovery from Conflict
Save current work to a new branch
Sync with main: git fetch && git rebase origin/main
Resolve conflicts file by file
Update Beads: bd sync
Continue work
Integration with Beads
# View all open work
bd list --status open

# Get ready (unblocked) items
bd ready --sort hybrid

# Claim an issue
bd update <id> --status in_progress --assignee claude

# Add dependency
bd dep add <blocking-id> <blocked-id> --type blocks

# Complete work
bd close <id> --reason "Implemented feature X"

# Sync state
bd sync

Weekly Installs
34
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass