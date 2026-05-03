---
title: bmad-orchestrator
url: https://skills.sh/aj-geddes/claude-code-bmad-skills/bmad-orchestrator
---

# bmad-orchestrator

skills/aj-geddes/claude-code-bmad-skills/bmad-orchestrator
bmad-orchestrator
Installation
$ npx skills add https://github.com/aj-geddes/claude-code-bmad-skills --skill bmad-orchestrator
SKILL.md
BMAD Orchestrator

Purpose: Core orchestrator for the BMAD Method (Breakthrough Method for Agile AI-Driven Development), managing workflows, tracking status, and routing users through structured development phases.

When to Use This Skill

Use this skill when:

User requests /workflow-init or /init - Initialize BMAD in a project
User requests /workflow-status or /status - Check progress and get recommendations
User mentions "BMAD setup" or "start BMAD workflow"
Project needs structured development methodology
Coordination between multiple development phases is required
Core Responsibilities
Project Initialization - Set up BMAD directory structure and configuration
Status Tracking - Monitor progress across 4 development phases
Workflow Routing - Direct users to appropriate next steps based on project state
Progress Management - Maintain workflow status and completion tracking
BMAD Method Overview
4 Development Phases
Analysis (Optional) - Research, brainstorming, product brief
Planning (Required) - PRD or Tech Spec based on project complexity
Solutioning (Conditional) - Architecture design for medium+ projects
Implementation (Required) - Sprint planning, stories, development
Project Levels
Level 0: Single atomic change (1 story) - Quick fixes, small tweaks
Level 1: Small feature (1-10 stories) - Single feature additions
Level 2: Medium feature set (5-15 stories) - Multiple related features
Level 3: Complex integration (12-40 stories) - System integrations
Level 4: Enterprise expansion (40+ stories) - Large-scale projects

Planning Requirements by Level:

Level 0-1: Tech Spec required, PRD optional/recommended
Level 2+: PRD required, Tech Spec optional
Level 2+: Architecture required
Available Commands
/workflow-init or /init

Initialize BMAD structure in the current project.

Steps:

Create directory structure:

bmad/
├── config.yaml
└── agent-overrides/

docs/
├── bmm-workflow-status.yaml
└── stories/

.claude/commands/bmad/ (if not exists)


Collect project information:

Project name
Project type (web-app, mobile-app, api, game, library, other)
Project level (0-4)

Create project config using config.template.yaml

Create workflow status file with conditional requirements based on level:

Use workflow-status template
Set PRD: required if level >= 2, else recommended
Set Tech-spec: required if level <= 1, else optional
Set Architecture: required if level >= 2, else optional

Display initialization summary and recommend next workflow

Offer to start recommended workflow

Example interaction:

User: /workflow-init

Orchestrator: I'll initialize BMAD for your project.
[Collects info, creates files...]

✓ BMAD Method initialized!

Project: MyApp
Type: web-app
Level: 2 (Medium feature set)

Configuration: bmad/config.yaml
Status tracking: docs/bmm-workflow-status.yaml

Recommended next step: Create Product Brief with /product-brief
This will help define your product vision and requirements.

Would you like to start with /product-brief?

/workflow-status or /status

Check project status and get recommendations for next steps.

Steps:

Load project config (bmad/config.yaml)
Load workflow status (docs/bmm-workflow-status.yaml)
Determine current phase and next recommended workflow
Display status with visual indicators
Offer to execute recommended workflow

Status Indicators:

✓ = Completed (shows file path)
⚠ = Required but not started
→ = Current phase
= Optional/not required

Example interaction:

User: /status

Orchestrator: Checking your project status...

Project: MyApp (Web Application, Level 2)

✓ Phase 1: Analysis
  ✓ product-brief (docs/product-brief-myapp-2025-01-11.md)

→ Phase 2: Planning [CURRENT]
  ⚠ prd (required - NOT STARTED)
  - tech-spec (optional)

Phase 3: Solutioning
  - architecture (required)

Phase 4: Implementation
  - sprint-planning (required)

Recommended next step: Create PRD with /prd command

Would you like to run /prd to create your PRD?


If project not initialized:

Inform user BMAD not detected
Offer to run /workflow-init
Workflow Routing Logic

After determining project status, route users to specialized workflows:

Analysis workflows: /product-brief, /brainstorm, /research
Planning workflows: /prd, /tech-spec
UX workflows: /create-ux-design
Architecture workflows: /architecture
Sprint workflows: /sprint-planning, /create-story
Development workflows: /dev-story, /code-review

Recommendation logic:

If no product-brief and project new → Recommend: /product-brief
If product-brief complete, no PRD/tech-spec:
Level 0-1 → Recommend: /tech-spec
Level 2+ → Recommend: /prd
If PRD/tech-spec complete, no architecture, level 2+ → Recommend: /architecture
If planning complete → Recommend: /sprint-planning
If sprint active → Recommend: /create-story or /dev-story

See REFERENCE.md for detailed routing logic.

Configuration Files
Project Config (bmad/config.yaml)
project_name: "MyApp"
project_type: "web-app"  # web-app, mobile-app, api, game, library, other
project_level: 2         # 0-4
output_folder: "docs"
communication_language: "English"

Workflow Status (docs/bmm-workflow-status.yaml)

Tracks completion of each workflow with status values:

"optional" - Can be skipped
"recommended" - Strongly suggested
"required" - Must be completed
"{file-path}" - Completed (shows output file)
"skipped" - Explicitly skipped

See templates/config.template.yaml for full template.

Helper Scripts

Execute via Bash tool:

init-project.sh - Automated project initialization

bash scripts/init-project.sh --name "MyApp" --type web-app --level 2


check-status.sh - Display current workflow status

bash scripts/check-status.sh


validate-config.sh - Validate YAML configuration

bash scripts/validate-config.sh bmad/config.yaml


See scripts documentation for details.

Error Handling

Config missing:

Suggest /workflow-init
Explain BMAD not initialized

Invalid YAML:

Show error location
Offer to fix or reinitialize

Template missing:

Use inline fallback
Log warning
Continue operation

Status file inconsistent:

Validate against project level
Offer to regenerate
Integration with Other Skills

This orchestrator coordinates with specialized BMAD skills:

business-analyst - Analysis phase workflows
product-manager - Planning phase workflows
system-architect - Architecture design
scrum-master - Sprint and story management
developer - Development workflows

When routing to these skills, pass context:

Current project config
Workflow status
Project level
Output folder location
Token Optimization
Use script automation for repetitive tasks
Reference REFERENCE.md for detailed logic
Load files only when needed
Keep status displays concise
Delegate detailed work to specialized skills
Subagent Strategy

This skill leverages parallel subagents to maximize context utilization (each agent has up to 1M tokens on Claude Sonnet 4.6 / Opus 4.6).

Workflow Status Check Workflow

Pattern: Fan-Out Research Agents: 3-4 parallel agents

Agent	Task	Output
Agent 1	Check project config and validate structure	bmad/outputs/config-status.md
Agent 2	Analyze workflow status file and phase completion	bmad/outputs/workflow-status.md
Agent 3	Scan docs directory for completed artifacts	bmad/outputs/artifacts-status.md
Agent 4	Generate recommendations based on project level	bmad/outputs/recommendations.md

Coordination:

Launch all agents with shared project context
Each agent writes status findings to designated output
Main context synthesizes results into unified status report
Display visual status indicators and next steps
Project Initialization Workflow

Pattern: Parallel Section Generation Agents: 3 parallel agents

Agent	Task	Output
Agent 1	Create directory structure and validate paths	bmad/outputs/directory-setup.md
Agent 2	Generate project config from template	bmad/config.yaml
Agent 3	Generate workflow status file with level-based requirements	docs/bmm-workflow-status.yaml

Coordination:

Gather project information from user (sequential)
Launch parallel agents to create structures and configs
Main context validates all outputs and displays summary
Example Subagent Prompt
Task: Analyze workflow status and determine current phase
Context: Read bmad/config.yaml and docs/bmm-workflow-status.yaml
Objective: Identify completed workflows, current phase, and required next steps
Output: Write analysis to bmad/outputs/workflow-status.md

Deliverables:
1. List of completed workflows with file paths
2. Current phase determination
3. Required vs optional next workflows
4. Blocking issues or missing dependencies

Constraints:
- Use project level to determine requirements
- Flag any inconsistencies in status file

Notes for Claude
This is the entry point for BMAD workflows
Always check if project is initialized before operations
Maintain phase-based progression (don't skip required phases)
Use TodoWrite for multi-step initialization
Keep responses focused and actionable
Hand off to specialized skills for detailed workflows
Update workflow status after completing workflows
Quick Reference
Detailed routing logic: REFERENCE.md
Workflow phases: resources/workflow-phases.md
Config template: templates/config.template.yaml
Init script: scripts/init-project.sh
Status script: scripts/check-status.sh
Weekly Installs
280
Repository
aj-geddes/claud…d-skills
GitHub Stars
407
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass