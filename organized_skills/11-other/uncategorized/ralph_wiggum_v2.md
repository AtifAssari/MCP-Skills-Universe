---
rating: ⭐⭐
title: ralph-wiggum-v2
url: https://skills.sh/adaptationio/skrillz/ralph-wiggum-v2
---

# ralph-wiggum-v2

skills/adaptationio/skrillz/ralph-wiggum-v2
ralph-wiggum-v2
Installation
$ npx skills add https://github.com/adaptationio/skrillz --skill ralph-wiggum-v2
SKILL.md
Ralph Wiggum v2 - Autonomous TDD Development Loop
Quick Start
/ralph-wiggum-v2:ralph-loop --project "diablo-starcraft" --completion-promise "DIABLO_STARCRAFT_COMPLETE"

Overview

Autonomous TDD development loop that uses parallel agent swarms to review code, discover issues, and fix them with test-first methodology until convergence criteria are met.

Workflow
Phase 1: Discovery & Initialization
Locate or create state file: {project}/.ralph/state.json
Locate or create categories file: {project}/.ralph/categories.json
Bootstrap categories from codebase structure if empty
Phase 2: Parallel Agent Review Swarm

Spawn 3-5 parallel agents with:

Random category (weighted toward lowest scores)
Random subcategory within that category
Random review style (never same as last 3 used)
Unique focus area (no overlap between agents)
Phase 3: TDD Implementation Cycle

For each finding:

Write failing test first
Implement minimal fix
Verify test passes
Update state
Phase 4: Category Evolution

After each iteration:

Merge new discoveries
Recalculate scores
Meta-review (every 5 iterations)
Phase 5: Convergence Detection

Complete when:

10 consecutive clean iterations
All category scores >= 95/100
All tests passing
Game runs without crashes
State Schema
{
  "project": "diablo-starcraft",
  "iteration": 0,
  "consecutiveCleanIterations": 0,
  "requiredCleanIterations": 10,
  "completionPromise": "DIABLO_STARCRAFT_COMPLETE",
  "categories": {},
  "discoveryLog": [],
  "lastReviewStyles": [],
  "agentHistory": [],
  "startedAt": "<timestamp>",
  "lastUpdated": "<timestamp>"
}

Categories Schema
{
  "categories": {
    "<category_name>": {
      "score": 50,
      "maxScore": 100,
      "subcategories": {
        "<subcategory_name>": {
          "score": 50,
          "issues": [],
          "lastReviewed": null,
          "reviewCount": 0
        }
      },
      "discoveredAt": 0,
      "lastUpdated": "<timestamp>"
    }
  }
}

Review Styles
Code Quality
Style	Focus
NITPICKER	Formatting, naming, tiny inconsistencies
REFACTORER	Duplication, abstraction opportunities
DRY_ENFORCER	Copy-paste code, repeated patterns
TYPE_ZEALOT	Type safety, any usage, casting
SOLID_ADHERENT	SOLID principle violations
API_PURIST	Interface design, contracts, signatures
Reliability
Style	Focus
DEBUGGER	Logic errors, off-by-one, wrong operators
EDGE_CASE_HUNTER	Boundary conditions, null/undefined
ERROR_HANDLER	Missing try/catch, unhandled promises
STATE_MACHINE_ANALYST	Invalid state transitions
CONCURRENCY_EXPERT	Race conditions, async bugs
MEMORY_LEAK_HUNTER	Listeners not removed, growing arrays
Performance
Style	Focus
PERFORMANCE_HAWK	O(n²), unnecessary renders, hot paths
ALLOCATION_AUDITOR	Object churn, GC pressure
RENDER_OPTIMIZER	DOM thrashing, layout thrashing
Security
Style	Focus
SECURITY_AUDITOR	XSS, injection, unsafe operations
INPUT_VALIDATOR	Unsanitized user input
Architecture
Style	Focus
ARCHITECT	Coupling, cohesion, separation of concerns
DEPENDENCY_AUDITOR	Circular deps, tight coupling
LAYER_GUARDIAN	Layer violations, wrong abstractions
Testing
Style	Focus
TEST_SKEPTIC	Coverage gaps, weak assertions
MUTATION_TESTER	Tests that always pass
INTEGRATION_ANALYST	Unit vs integration gaps
Game-Specific
Style	Focus
DIABLO_VETERAN	ARPG conventions, loot, skills, combat feel
STARCRAFT_FAN	Faction identity, unit feel, SC universe
GAME_FEEL_EXPERT	Juice, polish, responsiveness
BALANCE_DESIGNER	Numbers, progression, fairness
PLAYER_PSYCHOLOGY	Motivation, reward loops
SPEEDRUNNER	Exploits, sequence breaks
COMPLETIONIST	Missing edge cases in content
FIRST_TIME_USER	Onboarding, confusion points
Meta
Style	Focus
FRESH_EYES	What would confuse a new developer?
DOCUMENTATION_STICKLER	Missing/wrong comments
FUTURE_MAINTAINER	Technical debt accumulation
Agent Output Format
{
  "agentId": "<uuid>",
  "category": "<category>",
  "subcategory": "<subcategory>",
  "reviewStyle": "<style>",
  "filesReviewed": ["<paths>"],
  "findings": [
    {
      "severity": "critical|major|minor|nitpick",
      "type": "<issue_type>",
      "location": "<file:line>",
      "description": "<what's wrong>",
      "suggestedFix": "<how to fix>",
      "requiresTest": true,
      "testWritten": false,
      "fixed": false,
      "newSubcategory": null
    }
  ],
  "scoreAdjustment": 0,
  "newCategoriesDiscovered": [],
  "cleanReview": false
}

Hard Requirements
 PLAYABLE_LOCAL - Runs in browser, playable start-to-finish
 TDD_ENFORCED - No fix without failing test first
 ZERO_CRASHES - No unhandled exceptions in any path
 ALL_TESTS_PASS - 100% test suite green
 SCORES_95_PLUS - Every category at 95+/100
 CLEAN_CONVERGENCE - 10 consecutive clean iterations
Iteration Loop
LOOP:
  1. Load state from .ralph/state.json
  2. Load categories from .ralph/categories.json
  3. Increment iteration counter
  4. Select 3-5 lowest-scoring categories for review
  5. Spawn parallel review agents (use Task tool)
  6. Collect findings from all agents
  7. Sort findings by severity (critical → major → minor)
  8. TDD fix each finding:
     a. Write failing test
     b. Implement minimal fix
     c. Verify test passes
     d. Run full test suite
  9. Update scores and state
  10. Check convergence criteria:
      - All agents returned cleanReview: true?
      - No critical/major findings?
      - All tests passing?
      - No new categories discovered?
  11. IF clean: consecutiveCleanIterations++
      IF dirty: consecutiveCleanIterations = 0
  12. IF consecutiveCleanIterations >= 10 AND all scores >= 95:
      → CONVERGED: Run final verification
      ELSE: → Continue loop

Final Verification

When convergence criteria met:

Full test suite run
TypeScript strict mode check
Build production bundle
Verify game loads and plays
Generate completion report
Output: {COMPLETION_PROMISE} achieved
Game-Specific Categories (Diablo-StarCraft)
Auto-discovered from codebase:
engine/ → Engine (Game, Camera)
mechanics/ → Mechanics (Player, Ability, Item)
ai/ → AI (Enemy, Pathfinding)
graphics/ → Graphics (Renderer, VFX)
audio/ → Audio (AudioManager)
physics/ → Physics (Collision)
world/ → World (Tilemap)
persistence/ → Persistence (SaveManager)
input/ → Input (InputManager)
utils/ → Utils (isometric)
Game system categories:
Combat → Damage, resistance, crits, DOTs
Skills → Abilities, cooldowns, scaling
Loot → Drops, rarity, equipment
Progression → XP, levels, stats
Waves → Spawning, difficulty, bosses
UI/HUD → Health bars, buffs, minimap
Save/Load → Persistence, state restoration
Weekly Installs
20
Repository
adaptationio/skrillz
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass