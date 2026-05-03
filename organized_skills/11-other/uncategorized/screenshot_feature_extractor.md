---
rating: ⭐⭐
title: screenshot-feature-extractor
url: https://skills.sh/davila7/claude-code-templates/screenshot-feature-extractor
---

# screenshot-feature-extractor

skills/davila7/claude-code-templates/screenshot-feature-extractor
screenshot-feature-extractor
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill screenshot-feature-extractor
SKILL.md
Screenshot Analyzer (Multi-Agent)

Extract product features from UI screenshots using a coordinated multi-agent analysis pipeline.

Core principle: Describe WHAT to build (features/interactions), NOT HOW (no tech stack).

Multi-Agent Architecture

This skill orchestrates 5 specialized agents for comprehensive analysis:

                    ┌─────────────────┐
                    │   Coordinator   │
                    │   (this skill)  │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  UI Analyzer    │ │  Interaction    │ │   Business      │
│  (parallel)     │ │   Analyzer      │ │    Analyzer     │
│                 │ │  (parallel)     │ │   (parallel)    │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             ▼
                    ┌─────────────────┐
                    │   Synthesizer   │
                    │   (sequential)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Reviewer     │
                    │   (sequential)  │
                    └─────────────────┘

Process
Phase 1: Screenshot Collection

Gather all screenshots to analyze:

Read the screenshot file(s) provided by the user
For each screenshot, note the file path and any context provided
If multiple screenshots, determine if they are from the same product
Phase 2: Parallel Analysis

Launch THREE Task agents IN PARALLEL for each screenshot:

Agent 1: screenshot-ui-analyzer

Analyze this screenshot for UI components, layout structure, and design patterns.
Screenshot: [file path]
Return your analysis as JSON.


Agent 2: screenshot-interaction-analyzer

Analyze this screenshot for user interactions, navigation flows, and state transitions.
Screenshot: [file path]
Return your analysis as JSON.


Agent 3: screenshot-business-analyzer

Analyze this screenshot for business functions, data entities, and domain logic.
Screenshot: [file path]
Return your analysis as JSON.


IMPORTANT: Use the Task tool with THREE parallel calls in a single message to maximize efficiency.

Phase 3: Synthesis

After all parallel analyses complete, launch the synthesizer agent:

Agent 4: screenshot-synthesizer

Synthesize these analysis results into a unified development task list.

UI Analysis:
[paste UI analyzer result]

Interaction Analysis:
[paste Interaction analyzer result]

Business Analysis:
[paste Business analyzer result]

Product Name: [product name]
Output file: docs/plans/YYYY-MM-DD-<product>-features.md

Phase 4: Review

Launch the reviewer agent to validate the output:

Agent 5: screenshot-reviewer

Review this task list for completeness and quality.

Original screenshot(s): [file paths]
Task list: [synthesized output]

If issues found, provide corrections.

Phase 5: Output
Write final task list to docs/plans/YYYY-MM-DD-<product>-features.md
Use format from references/output-format.md
Present summary to user
Key Guidelines
Use - [ ] checkbox format for all tasks
Break features into small, executable subtasks
Focus on user interactions, not implementation details
For multiple screenshots: deduplicate features across all screens
For competitive analysis: highlight unique features and gaps
Benefits of Multi-Agent Approach
Thoroughness - Three specialized perspectives catch more details
Speed - Parallel analysis reduces total time
Quality - Synthesis + Review ensures coherent, complete output
Specialization - Each agent focuses on its domain expertise
Weekly Installs
378
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn