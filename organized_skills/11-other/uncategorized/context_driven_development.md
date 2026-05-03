---
rating: ⭐⭐⭐
title: context-driven-development
url: https://skills.sh/wshobson/agents/context-driven-development
---

# context-driven-development

skills/wshobson/agents/context-driven-development
context-driven-development
Installation
$ npx skills add https://github.com/wshobson/agents --skill context-driven-development
Summary

Structured project context management through persistent, synchronized documentation artifacts.

Creates and maintains five core artifacts in a conductor/ directory: product.md (vision/goals), tech-stack.md (dependencies/architecture), workflow.md (development practices), tracks.md (work unit registry), and product-guidelines.md (communication standards)
Scaffolds new projects interactively or extracts context from existing codebases, pre-populating artifacts based on discovered patterns
Validates artifact consistency before implementation and synchronizes documents as the project evolves, ensuring AI interactions and team alignment remain consistent across sessions
Supports greenfield and brownfield projects with context lifecycle management, validation checklists, and integration patterns for IDEs, git hooks, and CI/CD pipelines
SKILL.md
Context-Driven Development

Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentation.

When to Use This Skill
Setting up new projects with Conductor
Understanding the relationship between context artifacts
Maintaining consistency across AI-assisted development sessions
Onboarding team members to an existing Conductor project
Deciding when to update context documents
Managing greenfield vs brownfield project contexts
Core Philosophy

Context-Driven Development treats project context as a first-class artifact managed alongside code. Instead of relying on ad-hoc prompts or scattered documentation, establish a persistent, structured foundation that informs all AI interactions.

Key principles:

Context precedes code: Define what you're building and how before implementation
Living documentation: Context artifacts evolve with the project
Single source of truth: One canonical location for each type of information
AI alignment: Consistent context produces consistent AI behavior
The Workflow

Follow the Context → Spec & Plan → Implement workflow:

Context Phase: Establish or verify project context artifacts exist and are current
Specification Phase: Define requirements and acceptance criteria for work units
Planning Phase: Break specifications into phased, actionable tasks
Implementation Phase: Execute tasks following established workflow patterns
Artifact Relationships
product.md - Defines WHAT and WHY

Purpose: Captures product vision, goals, target users, and business context.

Contents:

Product name and one-line description
Problem statement and solution approach
Target user personas
Core features and capabilities
Success metrics and KPIs
Product roadmap (high-level)

Update when:

Product vision or goals change
New major features are planned
Target audience shifts
Business priorities evolve
product-guidelines.md - Defines HOW to Communicate

Purpose: Establishes brand voice, messaging standards, and communication patterns.

Contents:

Brand voice and tone guidelines
Terminology and glossary
Error message conventions
User-facing copy standards
Documentation style

Update when:

Brand guidelines change
New terminology is introduced
Communication patterns need refinement
tech-stack.md - Defines WITH WHAT

Purpose: Documents technology choices, dependencies, and architectural decisions.

Contents:

Primary languages and frameworks
Key dependencies with versions
Infrastructure and deployment targets
Development tools and environment
Testing frameworks
Code quality tools

Update when:

Adding new dependencies
Upgrading major versions
Changing infrastructure
Adopting new tools or patterns
workflow.md - Defines HOW to Work

Purpose: Establishes development practices, quality gates, and team workflows.

Contents:

Development methodology (TDD, etc.)
Git workflow and commit conventions
Code review requirements
Testing requirements and coverage targets
Quality assurance gates
Deployment procedures

Update when:

Team practices evolve
Quality standards change
New workflow patterns are adopted
tracks.md - Tracks WHAT'S HAPPENING

Purpose: Registry of all work units with status and metadata.

Contents:

Active tracks with current status
Completed tracks with completion dates
Track metadata (type, priority, assignee)
Links to individual track directories

Update when:

New tracks are created
Track status changes
Tracks are completed or archived

See references/artifact-templates.md for copy-paste starter templates.

Context Maintenance Principles
Keep Artifacts Synchronized

Ensure changes in one artifact reflect in related documents:

New feature in product.md → Update tech-stack.md if new dependencies needed
Completed track → Update product.md to reflect new capabilities
Workflow change → Update all affected track plans
Update tech-stack.md When Adding Dependencies

Before adding any new dependency:

Check if existing dependencies solve the need
Document the rationale for new dependencies
Add version constraints
Note any configuration requirements
Update product.md When Features Complete

After completing a feature track:

Move feature from "planned" to "implemented" in product.md
Update any affected success metrics
Document any scope changes from original plan
Verify Context Before Implementation

Before starting any track:

Read all context artifacts
Flag any outdated information
Propose updates before proceeding
Confirm context accuracy with stakeholders
Greenfield vs Brownfield Handling
Greenfield Projects (New)

For new projects:

Run /conductor:setup to create all artifacts interactively
Answer questions about product vision, tech preferences, and workflow
Generate initial style guides for chosen languages
Create empty tracks registry

Characteristics:

Full control over context structure
Define standards before code exists
Establish patterns early
Brownfield Projects (Existing)

For existing codebases:

Run /conductor:setup with existing codebase detection
System analyzes existing code, configs, and documentation
Pre-populate artifacts based on discovered patterns
Review and refine generated context

Characteristics:

Extract implicit context from existing code
Reconcile existing patterns with desired patterns
Document technical debt and modernization plans
Preserve working patterns while establishing standards
Benefits
Team Alignment
New team members onboard faster with explicit context
Consistent terminology and conventions across the team
Shared understanding of product goals and technical decisions
AI Consistency
AI assistants produce aligned outputs across sessions
Reduced need to re-explain context in each interaction
Predictable behavior based on documented standards
Institutional Memory
Decisions and rationale are preserved
Context survives team changes
Historical context informs future decisions
Quality Assurance
Standards are explicit and verifiable
Deviations from context are detectable
Quality gates are documented and enforceable
Directory Structure
conductor/
├── index.md              # Navigation hub linking all artifacts
├── product.md            # Product vision and goals
├── product-guidelines.md # Communication standards
├── tech-stack.md         # Technology preferences
├── workflow.md           # Development practices
├── tracks.md             # Work unit registry
├── setup_state.json      # Resumable setup state
├── code_styleguides/     # Language-specific conventions
│   ├── python.md
│   ├── typescript.md
│   └── ...
└── tracks/
    └── <track-id>/
        ├── spec.md
        ├── plan.md
        ├── metadata.json
        └── index.md

Context Lifecycle
Creation: Initial setup via /conductor:setup
Validation: Verify before each track
Evolution: Update as project grows
Synchronization: Keep artifacts aligned
Archival: Document historical decisions
Context Validation Checklist

Before starting implementation on any track, validate context:

Product Context
 product.md reflects current product vision
 Target users are accurately described
 Feature list is up to date
 Success metrics are defined
Technical Context
 tech-stack.md lists all current dependencies
 Version numbers are accurate
 Infrastructure targets are correct
 Development tools are documented
Workflow Context
 workflow.md describes current practices
 Quality gates are defined
 Coverage targets are specified
 Commit conventions are documented
Track Context
 tracks.md shows all active work
 No stale or abandoned tracks
 Dependencies between tracks are noted
Common Anti-Patterns

Avoid these context management mistakes:

Stale Context

Problem: Context documents become outdated and misleading. Solution: Update context as part of each track's completion process.

Context Sprawl

Problem: Information scattered across multiple locations. Solution: Use the defined artifact structure; resist creating new document types.

Implicit Context

Problem: Relying on knowledge not captured in artifacts. Solution: If you reference something repeatedly, add it to the appropriate artifact.

Context Hoarding

Problem: One person maintains context without team input. Solution: Review context artifacts in pull requests; make updates collaborative.

Over-Specification

Problem: Context becomes so detailed it's impossible to maintain. Solution: Keep artifacts focused on decisions that affect AI behavior and team alignment.

Integration with Development Tools
IDE Integration

Configure your IDE to display context files prominently:

Pin conductor/product.md for quick reference
Add tech-stack.md to project notes
Create snippets for common patterns from style guides
Git Hooks

Consider pre-commit hooks that:

Warn when dependencies change without tech-stack.md update
Remind to update product.md when feature branches merge
Validate context artifact syntax
CI/CD Integration

Include context validation in pipelines:

Check tech-stack.md matches actual dependencies
Verify links in context documents resolve
Ensure tracks.md status matches git branch state
Session Continuity

Conductor supports multi-session development through context persistence:

Starting a New Session
Read index.md to orient yourself
Check tracks.md for active work
Review relevant track's plan.md for current task
Verify context artifacts are current
Ending a Session
Update plan.md with current progress
Note any blockers or decisions made
Commit in-progress work with clear status
Update tracks.md if status changed
Handling Interruptions

If interrupted mid-task:

Mark task as [~] with note about stopping point
Commit work-in-progress to feature branch
Document any uncommitted decisions in plan.md
Best Practices
Read context first: Always read relevant artifacts before starting work
Small updates: Make incremental context changes, not massive rewrites
Link decisions: Reference context when making implementation choices
Version context: Commit context changes alongside code changes
Review context: Include context artifact reviews in code reviews
Validate regularly: Run context validation checklist before major work
Communicate changes: Notify team when context artifacts change significantly
Preserve history: Use git to track context evolution over time
Question staleness: If context feels wrong, investigate and update
Keep it actionable: Every context item should inform a decision or behavior
Weekly Installs
5.8K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass