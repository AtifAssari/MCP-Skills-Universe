---
rating: ⭐⭐⭐
title: customaize-agent:create-command
url: https://skills.sh/neolabhq/context-engineering-kit/customaize-agent:create-command
---

# customaize-agent:create-command

skills/neolabhq/context-engineering-kit/customaize-agent:create-command
customaize-agent:create-command
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill customaize-agent:create-command
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Command Creator Assistant

This meta-command helps create other commands by:

Understanding the command's purpose
Determining its category and pattern
Choosing command location (project vs user)
Generating the command file
Creating supporting resources
Updating documentation

<command_categories>

Planning Commands (Specialized)

Feature ideation, proposals, PRDs
Complex workflows with distinct stages
Interactive, conversational style
Create documentation artifacts
Examples: @/.claude/commands/01_brainstorm-feature.md @/.claude/commands/02_feature-proposal.md

Implementation Commands (Generic with Modes)

Technical execution tasks
Mode-based variations (ui, core, mcp, etc.)
Follow established patterns
Update task states
Example: @/.claude/commands/implement.md

Analysis Commands (Specialized)

Review, audit, analyze
Generate reports or insights
Read-heavy operations
Provide recommendations
Example: @/.claude/commands/review.md

Workflow Commands (Specialized)

Orchestrate multiple steps
Coordinate between areas
Manage dependencies
Track progress
Example: @/.claude/commands/04_feature-planning.md

Utility Commands (Generic or Specialized)

Tools, helpers, maintenance
Simple operations
May or may not need modes </command_categories>

<command_frontmatter>

CRITICAL: Every Command Must Start with Frontmatter

All command files MUST begin with YAML frontmatter enclosed in --- delimiters:

---
description: Brief description of what the command does
argument-hint: Description of expected arguments (optional)
---

Frontmatter Fields

description (REQUIRED):

One-line summary of the command's purpose
Clear, concise, action-oriented
Example: "Guided feature development with codebase understanding and architecture focus"

argument-hint (OPTIONAL):

Describes what arguments the command accepts
Examples:
"Optional feature description"
"File path to analyze"
"Component name and location"
"None required - interactive mode"
Example Frontmatter by Command Type
# Planning Command
---
description: Interactive brainstorming session for new feature ideas
argument-hint: Optional initial feature concept
---

# Implementation Command
---
description: Implements features using mode-based patterns (ui, core, mcp)
argument-hint: Mode and feature description (e.g., 'ui: add dark mode toggle')
---

# Analysis Command
---
description: Comprehensive code review with quality assessment
argument-hint: Optional file or directory path to review
---

# Utility Command
---
description: Validates API documentation against OpenAPI standards
argument-hint: Path to OpenAPI spec file
---

Placement
Frontmatter MUST be the very first content in the file
No blank lines before the opening ---
One blank line after the closing --- before content begins </command_frontmatter>

<command_features>

Slash Command Features
Namespacing

Use subdirectories to group related commands. Subdirectories appear in the command description but don't affect the command name.

Example:

.claude/commands/frontend/component.md creates /component with description "(project:frontend)"
~/.claude/commands/component.md creates /component with description "(user)"

Priority: If a project command and user command share the same name, the project command takes precedence.

Arguments
All Arguments with $ARGUMENTS

Captures all arguments passed to the command:

# Command definition
echo 'Fix issue #$ARGUMENTS following our coding standards' > .claude/commands/fix-issue.md

# Usage
> /fix-issue 123 high-priority
# $ARGUMENTS becomes: "123 high-priority"

Individual Arguments with $1, $2, etc.

Access specific arguments individually using positional parameters:

# Command definition
echo 'Review PR #$1 with priority $2 and assign to $3' > .claude/commands/review-pr.md

# Usage
> /review-pr 456 high alice
# $1 becomes "456", $2 becomes "high", $3 becomes "alice"

Bash Command Execution

Execute bash commands before the slash command runs using the ! prefix. The output is included in the command context.

Note: You must include allowed-tools with the Bash tool.

---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context

- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

File References

Include file contents using the @ prefix to reference files:

Review the implementation in @src/utils/helpers.js
Compare @src/old-version.js with @src/new-version.js

Thinking Mode

Slash commands can trigger extended thinking by including extended thinking keywords.

Frontmatter Options
Frontmatter	Purpose	Default
allowed-tools	List of tools the command can use	Inherits from conversation
argument-hint	Expected arguments for auto-completion	None
description	Brief description of the command	First line from prompt
model	Specific model string	Inherits from conversation
disable-model-invocation	Prevent Skill tool from calling this command	false

Example with all frontmatter options:

---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
argument-hint: [message]
description: Create a git commit
model: claude-3-5-haiku-20241022
---

Create a git commit with message: $ARGUMENTS


</command_features>

<pattern_research>

Before Creating: Study Similar Commands

List existing commands in target directory:

# For project commands
ls -la /.claude/commands/

# For user commands
ls -la ~/.claude/commands/


Read similar commands for patterns:

Check the frontmatter (description and argument-hint)
How do they structure sections?
What MCP tools do they use?
How do they handle arguments?
What documentation do they reference?

Common patterns to look for:

# MCP tool usage for tasks
Use tool: mcp__scopecraft-cmd__task_create
Use tool: mcp__scopecraft-cmd__task_update
Use tool: mcp__scopecraft-cmd__task_list

# NOT CLI commands
❌ Run: scopecraft task list
✅ Use tool: mcp__scopecraft-cmd__task_list


Standard references to include:

@/docs/organizational-structure-guide.md
@/docs/command-resources/{relevant-templates}
@/docs/claude-commands-guide.md </pattern_research>

<interview_process>

Phase 1: Understanding Purpose

"Let's create a new command. First, let me check what similar commands exist..."

Use Glob to find existing commands in the target category

"Based on existing patterns, please describe:"

What problem does this command solve?
Who will use it and when?
What's the expected output?
Is it interactive or batch?
Phase 2: Category Classification

Based on responses and existing examples:

Is this like existing planning commands? (Check: brainstorm-feature, feature-proposal)
Is this like implementation commands? (Check: implement.md)
Does it need mode variations?
Should it follow analysis patterns? (Check: review.md)
Phase 3: Pattern Selection

Study similar commands first:

# Read a similar command
@{similar-command-path}

# Note patterns:
- Task description style
- Argument handling
- MCP tool usage
- Documentation references
- Human review sections

Phase 4: Command Location

🎯 Critical Decision: Where should this command live?

Project Command (/.claude/commands/)

Specific to this project's workflow
Uses project conventions
References project documentation
Integrates with project MCP tools

User Command (~/.claude/commands/)

General-purpose utility
Reusable across projects
Personal productivity tool
Not project-specific

Ask: "Should this be:

A project command (specific to this codebase)
A user command (available in all projects)?"
Phase 5: Resource Planning

Check existing resources:

# Check templates
ls -la /docs/command-resources/planning-templates/
ls -la /docs/command-resources/implement-modes/

# Check which guides exist
ls -la /docs/


</interview_process>

<generation_patterns>

Critical: Copy Patterns from Similar Commands

Before generating, read similar commands and note:

Frontmatter (MUST BE FIRST):

---
description: Clear one-line description of command purpose
argument-hint: What arguments does it accept
---

No blank lines before opening ---
One blank line after closing ---
description is REQUIRED
argument-hint is OPTIONAL

MCP Tool Usage:

# From existing commands
Use mcp__scopecraft-cmd__task_create
Use mcp__scopecraft-cmd__feature_get
Use mcp__scopecraft-cmd__phase_list


Standard References:

<context>
Key Reference: @/docs/organizational-structure-guide.md
Template: @/docs/command-resources/planning-templates/{template}.md
Guide: @/docs/claude-commands-guide.md
</context>


Task Update Patterns:

<task_updates>
After implementation:
1. Update task status to appropriate state
2. Add implementation log entries
3. Mark checklist items as complete
4. Document any decisions made
</task_updates>


Human Review Sections:

<human_review_needed>
Flag decisions needing verification:
- [ ] Assumptions about workflows
- [ ] Technical approach choices
- [ ] Pattern-based suggestions
</human_review_needed>


</generation_patterns>

<implementation_steps>

Create Command File

Determine location based on project/user choice
Generate content following established patterns
Include all required sections

Create Supporting Files (if project command)

Templates in /docs/command-resources/
Mode guides if generic command
Example documentation

Update Documentation (if project command)

Add to claude-commands-guide.md
Update feature-development-workflow.md if workflow command
Add to README if user-facing

Test the Command

Create example usage scenarios
Verify argument handling
Check MCP tool integration </implementation_steps>

<creation_checklist> Before finalizing:

 Includes YAML frontmatter with description (required) and argument-hint (optional)
 Frontmatter is the very first content (no blank lines before opening ---)
 Studied similar commands in the category
 Command follows naming conventions (use numeric prefix for ordered workflows)
 Includes proper task/context structure
 References @organizational-structure-guide.md
 Uses MCP tools (not CLI) - check existing patterns
 Includes human review sections
 Has clear examples like other commands
 Updates task states appropriately
 Creates proper documentation
 Follows established patterns from similar commands
 Correct command prefix (project: or user:) </creation_checklist>

<example_session> User: "I need a command to help validate our API documentation"

🔍 Research: Let me check existing analysis commands...

Use Read tool to examine: /.claude/commands/review.md

I notice the review command:

Uses MCP tools for task operations
Includes human review sections
References organizational structure
Has clear output formatting

🤔 Question: Can you tell me more about this API documentation validation?

What format is the documentation in?
What aspects need validation?
Should it create tasks for issues found?

User: "It's OpenAPI specs, need to check for completeness and consistency"

💡 Category: This is an Analysis command similar to 'review'.

🔍 Pattern Check: Looking at review.md, I see it:

<task>
You are a code reviewer conducting a comprehensive review...
</task>

<mcp_usage>
Always use MCP tools:
- mcp__scopecraft-cmd__task_list
- mcp__scopecraft-cmd__task_update
</mcp_usage>


🎯 Location Question: Should this be:

A project command (specific to this API project)
A user command (useful for all your API projects)

User: "Project command - it needs to reference our specific API standards"

✅ Creating project command: /.claude/commands/validate-api.md

Generated command (following review.md patterns):

---
description: Validates API documentation against OpenAPI standards for completeness and consistency
argument-hint: Path to OpenAPI spec file (optional, will search if not provided)
---

<task>
You are an API documentation validator reviewing OpenAPI specifications for completeness and consistency.
</task>

<context>
References:
- API Standards: @/docs/api-standards.md
- Organizational Structure: @/docs/organizational-structure-guide.md
Similar to: @/.claude/commands/review.md
</context>

<validation_process>
1. Load OpenAPI spec files
2. Check required endpoints documented
3. Validate response schemas
4. Verify authentication documented
5. Check for missing examples
</validation_process>

<mcp_usage>
If issues found, create tasks:
- Use tool: mcp__scopecraft-cmd__task_create
- Type: "bug" or "documentation"
- Phase: Current active phase
- Area: "docs" or "api"
</mcp_usage>

<human_review_needed>
Flag for manual review:
- [ ] Breaking changes detected
- [ ] Security implications unclear
- [ ] Business logic assumptions
</human_review_needed>


</example_session>

<final_output> After gathering all information:

Command Created:

Location: {chosen location}
Name: {command-name}
Category: {category}
Pattern: {specialized/generic}

Resources Created:

Supporting templates: {list}
Documentation updates: {list}

Usage Instructions:

Command: /{prefix}:{name}
Example: {example usage}

Next Steps:

Test the command
Refine based on usage
Add to command documentation </final_output>
Weekly Installs
440
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 27, 2026