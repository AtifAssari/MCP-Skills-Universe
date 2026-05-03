---
rating: ⭐⭐
title: iterative-retrieval
url: https://skills.sh/affaan-m/everything-claude-code/iterative-retrieval
---

# iterative-retrieval

skills/affaan-m/everything-claude-code/iterative-retrieval
iterative-retrieval
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill iterative-retrieval
Summary

Progressive context refinement loop for multi-agent workflows solving the subagent context problem.

Four-phase cycle (dispatch, evaluate, refine, loop) that iteratively narrows retrieval to high-relevance files, capping at 3 iterations to balance token usage and context quality
Scores retrieved files on a 0–1 relevance scale and explicitly identifies missing context gaps to drive the next refinement cycle
Learns codebase terminology and patterns during the first cycle, improving subsequent searches without requiring upfront knowledge of project conventions
Designed for spawning subagents on code exploration, bug fixes, and feature implementation tasks where context needs are unpredictable upfront
SKILL.md
Iterative Retrieval Pattern

Solves the "context problem" in multi-agent workflows where subagents don't know what context they need until they start working.

When to Activate
Spawning subagents that need codebase context they cannot predict upfront
Building multi-agent workflows where context is progressively refined
Encountering "context too large" or "missing context" failures in agent tasks
Designing RAG-like retrieval pipelines for code exploration
Optimizing token usage in agent orchestration
The Problem

Subagents are spawned with limited context. They don't know:

Which files contain relevant code
What patterns exist in the codebase
What terminology the project uses

Standard approaches fail:

Send everything: Exceeds context limits
Send nothing: Agent lacks critical information
Guess what's needed: Often wrong
The Solution: Iterative Retrieval

A 4-phase loop that progressively refines context:

┌─────────────────────────────────────────────┐
│                                             │
│   ┌──────────┐      ┌──────────┐            │
│   │ DISPATCH │─────│ EVALUATE │            │
│   └──────────┘      └──────────┘            │
│        ▲                  │                 │
│        │                  ▼                 │
│   ┌──────────┐      ┌──────────┐            │
│   │   LOOP   │─────│  REFINE  │            │
│   └──────────┘      └──────────┘            │
│                                             │
│        Max 3 cycles, then proceed           │
└─────────────────────────────────────────────┘

Phase 1: DISPATCH

Initial broad query to gather candidate files:

// Start with high-level intent
const initialQuery = {
  patterns: ['src/**/*.ts', 'lib/**/*.ts'],
  keywords: ['authentication', 'user', 'session'],
  excludes: ['*.test.ts', '*.spec.ts']
};

// Dispatch to retrieval agent
const candidates = await retrieveFiles(initialQuery);

Phase 2: EVALUATE

Assess retrieved content for relevance:

function evaluateRelevance(files, task) {
  return files.map(file => ({
    path: file.path,
    relevance: scoreRelevance(file.content, task),
    reason: explainRelevance(file.content, task),
    missingContext: identifyGaps(file.content, task)
  }));
}


Scoring criteria:

High (0.8-1.0): Directly implements target functionality
Medium (0.5-0.7): Contains related patterns or types
Low (0.2-0.4): Tangentially related
None (0-0.2): Not relevant, exclude
Phase 3: REFINE

Update search criteria based on evaluation:

function refineQuery(evaluation, previousQuery) {
  return {
    // Add new patterns discovered in high-relevance files
    patterns: [...previousQuery.patterns, ...extractPatterns(evaluation)],

    // Add terminology found in codebase
    keywords: [...previousQuery.keywords, ...extractKeywords(evaluation)],

    // Exclude confirmed irrelevant paths
    excludes: [...previousQuery.excludes, ...evaluation
      .filter(e => e.relevance < 0.2)
      .map(e => e.path)
    ],

    // Target specific gaps
    focusAreas: evaluation
      .flatMap(e => e.missingContext)
      .filter(unique)
  };
}

Phase 4: LOOP

Repeat with refined criteria (max 3 cycles):

async function iterativeRetrieve(task, maxCycles = 3) {
  let query = createInitialQuery(task);
  let bestContext = [];

  for (let cycle = 0; cycle < maxCycles; cycle++) {
    const candidates = await retrieveFiles(query);
    const evaluation = evaluateRelevance(candidates, task);

    // Check if we have sufficient context
    const highRelevance = evaluation.filter(e => e.relevance >= 0.7);
    if (highRelevance.length >= 3 && !hasCriticalGaps(evaluation)) {
      return highRelevance;
    }

    // Refine and continue
    query = refineQuery(evaluation, query);
    bestContext = mergeContext(bestContext, highRelevance);
  }

  return bestContext;
}

Practical Examples
Example 1: Bug Fix Context
Task: "Fix the authentication token expiry bug"

Cycle 1:
  DISPATCH: Search for "token", "auth", "expiry" in src/**
  EVALUATE: Found auth.ts (0.9), tokens.ts (0.8), user.ts (0.3)
  REFINE: Add "refresh", "jwt" keywords; exclude user.ts

Cycle 2:
  DISPATCH: Search refined terms
  EVALUATE: Found session-manager.ts (0.95), jwt-utils.ts (0.85)
  REFINE: Sufficient context (2 high-relevance files)

Result: auth.ts, tokens.ts, session-manager.ts, jwt-utils.ts

Example 2: Feature Implementation
Task: "Add rate limiting to API endpoints"

Cycle 1:
  DISPATCH: Search "rate", "limit", "api" in routes/**
  EVALUATE: No matches - codebase uses "throttle" terminology
  REFINE: Add "throttle", "middleware" keywords

Cycle 2:
  DISPATCH: Search refined terms
  EVALUATE: Found throttle.ts (0.9), middleware/index.ts (0.7)
  REFINE: Need router patterns

Cycle 3:
  DISPATCH: Search "router", "express" patterns
  EVALUATE: Found router-setup.ts (0.8)
  REFINE: Sufficient context

Result: throttle.ts, middleware/index.ts, router-setup.ts

Integration with Agents

Use in agent prompts:

When retrieving context for this task:
1. Start with broad keyword search
2. Evaluate each file's relevance (0-1 scale)
3. Identify what context is still missing
4. Refine search criteria and repeat (max 3 cycles)
5. Return files with relevance >= 0.7

Best Practices
Start broad, narrow progressively - Don't over-specify initial queries
Learn codebase terminology - First cycle often reveals naming conventions
Track what's missing - Explicit gap identification drives refinement
Stop at "good enough" - 3 high-relevance files beats 10 mediocre ones
Exclude confidently - Low-relevance files won't become relevant
Related
The Longform Guide - Subagent orchestration section
continuous-learning skill - For patterns that improve over time
Agent definitions bundled with ECC (manual install path: agents/)
Weekly Installs
3.4K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass