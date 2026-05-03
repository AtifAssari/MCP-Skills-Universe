---
title: setup-ralph
url: https://skills.sh/glittercowboy/taches-cc-resources/setup-ralph
---

# setup-ralph

skills/glittercowboy/taches-cc-resources/setup-ralph
setup-ralph
Installation
$ npx skills add https://github.com/glittercowboy/taches-cc-resources --skill setup-ralph
SKILL.md

<essential_principles>

What is Ralph?

Ralph is Geoffrey Huntley's autonomous AI coding methodology that uses iterative loops with task selection, execution, and validation. In its purest form, it's a Bash loop:

while :; do cat PROMPT.md | claude ; done


The loop feeds a prompt file to Claude, the agent completes one task, updates the implementation plan, commits changes, then exits. The loop restarts immediately with fresh context.

Core Philosophy

The Ralph Wiggum Technique is deterministically bad in an undeterministic world. Ralph solves context accumulation by starting each iteration with fresh context—the core insight behind Geoffrey's approach.

Three Phases, Two Prompts, One Loop
Planning Phase: Gap analysis (specs vs code) outputs prioritized TODO list—no implementation, no commits
Building Phase: Picks tasks from plan, implements, runs tests (backpressure), commits
Observation Phase: You sit on the loop, not in it—engineer the setup and environment that allows Ralph to succeed
Key Principles

Your Role: Ralph does all the work, including deciding which planned work to implement next and how to implement it. Your job is to engineer the environment.

Backpressure: Create backpressure via tests, typechecks, lints, builds that reject invalid/unacceptable work.

Observation: Watch, especially early on. Prompts evolve through observed failure patterns.

Context Efficiency: With ~176K usable tokens from 200K window, allocating 40-60% to "smart zone" means tight tasks with one task per loop achieves maximum context utilization.

File I/O as State: The plan file persists between isolated loop executions, serving as deterministic shared state—no sophisticated orchestration needed.

Remote Backup: The loop automatically creates a private GitHub repo and pushes after each commit. This protects against accidental data loss from autonomous operations. Requires gh CLI authenticated. Disable with RALPH_BACKUP=false.

Safety Rules: PROMPT_build.md includes critical safety rules prohibiting dangerous operations like rm -rf on project directories. Tests must run in isolated temp directories. </essential_principles>

Set up a new Ralph loop - Initialize Ralph structure in a directory
Understand Ralph concepts - Learn about the technique and how it works
Customize existing loop - Modify prompts or configuration
Troubleshoot Ralph - Debug loop issues or improve performance

Wait for response before proceeding.

After reading the workflow, follow it exactly.

<reference_index>

Domain Knowledge

All in references/:

Core Concepts: ralph-fundamentals.md - Three phases, two prompts, one loop Structure: project-structure.md - Required files and directory layout Prompts: prompt-design.md - Planning vs building mode instructions Backpressure: validation-strategy.md - Tests, lints, builds as steering Best Practices: operational-learnings.md - AGENTS.md guidance and evolution </reference_index>

<workflows_index>

Workflow	Purpose
setup-new-loop.md	Initialize Ralph structure in a directory
understand-ralph.md	Learn Ralph concepts and philosophy
customize-loop.md	Modify prompts or loop configuration
troubleshoot-loop.md	Debug loop issues and improve performance
</workflows_index>	

<success_criteria> Skill is successful when:

User understands which workflow they need
Appropriate workflow loaded based on intent
All required references loaded by workflow
User can set up and run Ralph loops independently </success_criteria>
Weekly Installs
78
Repository
glittercowboy/t…esources
GitHub Stars
1.9K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass