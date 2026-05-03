---
rating: ⭐⭐⭐
title: use-conductor
url: https://skills.sh/89jobrien/steve/use-conductor
---

# use-conductor

skills/89jobrien/steve/use-conductor
use-conductor
Installation
$ npx skills add https://github.com/89jobrien/steve --skill use-conductor
SKILL.md
Use Conductor

Scan the conductor/ directory at project root for structured project management files that provide direction, workflows, and task planning context.

When to Use

Use this skill when:

Starting work on a project that may have conductor files
Looking for project context, guidelines, or current tasks
Needing to understand the project's workflow methodology
Determining what work is in progress or next in queue
Conductor Directory Structure

The conductor system uses this structure:

conductor/
├── product.md              # Product vision and purpose
├── product-guidelines.md   # Standards and conventions
├── tech-stack.md           # Technology decisions
├── workflow.md             # Task execution methodology
├── tracks.md               # Index of active work tracks
├── setup_state.json        # Setup progress state
├── code_styleguides/       # Language-specific style guides
│   ├── general.md
│   └── python.md
└── tracks/                 # Detailed track plans
    └── <track_name>/
        ├── spec.md         # Track specification
        ├── plan.md         # Task checklist with progress
        └── metadata.json   # Track metadata

File Purposes
File	Purpose
product.md	Product vision, target audience, core features
product-guidelines.md	Naming conventions, quality standards, documentation rules
tech-stack.md	Approved technologies and libraries
workflow.md	TDD methodology, task workflow, commit guidelines
tracks.md	High-level index of all work tracks
tracks/<name>/plan.md	Detailed task checklist with [ ], [~], [x] status
tracks/<name>/spec.md	Goals, scope, and success criteria for the track
How to Scan
Check if conductor/ directory exists at project root
If present, read core files to understand project context:
product.md for vision
product-guidelines.md for standards
tracks.md for active work
For active tracks (marked [~]), read the track's plan.md to find current tasks
Follow the workflow methodology defined in workflow.md
Task Status Markers

In plan.md files:

[ ] - Task not started
[~] - Task in progress
[x] - Task completed (may include commit SHA)
Integration with Work

When conductor files are present:

Respect the plan - Follow the task order in plan.md
Update status - Mark tasks as [~] when starting, [x] when done
Follow workflow - Use the TDD methodology if specified
Maintain standards - Follow product-guidelines.md and style guides
Stay in scope - Check spec.md for what's in/out of scope
Example Usage

Before starting work on a project:

User: "What should I work on next?"

Claude: [Checks for conductor/ directory]
        [Reads tracks.md to find active track]
        [Reads tracks/<active>/plan.md to find next [ ] task]
        "According to the conductor plan, the next task is..."

Weekly Installs
22
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass