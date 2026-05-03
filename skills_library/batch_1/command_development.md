---
title: command-development
url: https://skills.sh/anthropics/claude-plugins-official/command-development
---

# command-development

skills/anthropics/claude-plugins-official/command-development
command-development
Originally fromanthropics/claude-code
Installation
$ npx skills add https://github.com/anthropics/claude-plugins-official --skill command-development
Summary

Markdown-based slash commands for defining reusable prompts with dynamic arguments, file references, and bash execution.

Commands are instructions written for Claude (not users), stored as .md files in .claude/commands/, ~/.claude/commands/, or plugin directories
YAML frontmatter configures description, allowed tools, model selection, and argument hints; use $ARGUMENTS, $1, $2 for dynamic substitution and @file-path syntax for file inclusion
Bash execution via backticks gathers dynamic context; allowed-tools restricts access (e.g., Bash(git:*) for git-only commands)
Organize commands in flat or namespaced structures; plugin commands access ${CLAUDE_PLUGIN_ROOT} for portable resource references and can integrate with agents, skills, and hooks
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Command Development for Claude Code

Note: The .claude/commands/ directory is a legacy format. For new skills, use the .claude/skills/<name>/SKILL.md directory format. Both are loaded identically — the only difference is file layout. See the skill-development skill for the preferred format.

Overview

Slash commands are frequently-used prompts defined as Markdown files that Claude executes during interactive sessions. Understanding command structure, frontmatter options, and dynamic features enables creating powerful, reusable workflows.

Key concepts:

Markdown file format for commands
YAML frontmatter for configuration
Dynamic arguments and file references
Bash execution for context
Command organization and namespacing
Command Basics
What is a Slash Command?

A slash command is a Markdown file containing a prompt that Claude executes when invoked. Commands provide:

Reusability: Define once, use repeatedly
Consistency: Standardize common workflows
Sharing: Distribute across team or projects
Efficiency: Quick access to complex prompts
Critical: Commands are Instructions FOR Claude

Commands are written for agent consumption, not human consumption.

When a user invokes /command-name, the command content becomes Claude's instructions. Write commands as directives TO Claude about what to do, not as messages TO the user.

Correct approach (instructions for Claude):

Review this code for security vulnerabilities including:

- SQL injection
- XSS attacks
- Authentication issues

Provide specific line numbers and severity ratings.


Incorrect approach (messages to user):

This command will review your code for security issues.
You'll receive a report with vulnerability details.


The first example tells Claude what to do. The second tells the user what will happen but doesn't instruct Claude. Always use the first approach.

Command Locations

Project commands (shared with team):

Location: .claude/commands/
Scope: Available in specific project
Label: Shown as "(project)" in /help
Use for: Team workflows, project-specific tasks

Personal commands (available everywhere):

Location: ~/.claude/commands/
Scope: Available in all projects
Label: Shown as "(user)" in /help
Use for: Personal workflows, cross-project utilities

Plugin commands (bundled with plugins):

Location: plugin-name/commands/
Scope: Available when plugin installed
Label: Shown as "(plugin-name)" in /help
Use for: Plugin-specific functionality
File Format
Basic Structure

Commands are Markdown files with .md extension:

.claude/commands/
├── review.md           # /review command
├── test.md             # /test command
└── deploy.md           # /deploy command


Simple command:

Review this code for security vulnerabilities including:

- SQL injection
- XSS attacks
- Authentication bypass
- Insecure data handling


No frontmatter needed for basic commands.

With YAML Frontmatter

Add configuration using YAML frontmatter:

---
description: Review code for security issues
allowed-tools: Read, Grep, Bash(git:*)
model: sonnet
---

Review this code for security vulnerabilities...

YAML Frontmatter Fields
description

Purpose: Brief description shown in /help Type: String Default: First line of command prompt

---
description: Review pull request for code quality
---


Best practice: Clear, actionable description (under 60 characters)

allowed-tools

Purpose: Specify which tools command can use Type: String or Array Default: Inherits from conversation

---
allowed-tools: Read, Write, Edit, Bash(git:*)
---


Patterns:

Read, Write, Edit - Specific tools
Bash(git:*) - Bash with git commands only
* - All tools (rarely needed)

Use when: Command requires specific tool access

model

Purpose: Specify model for command execution Type: String (sonnet, opus, haiku) Default: Inherits from conversation

---
model: haiku
---


Use cases:

haiku - Fast, simple commands
sonnet - Standard workflows
opus - Complex analysis
argument-hint

Purpose: Document expected arguments for autocomplete Type: String Default: None

---
argument-hint: [pr-number] [priority] [assignee]
---


Benefits:

Helps users understand command arguments
Improves command discovery
Documents command interface
disable-model-invocation

Purpose: Prevent SlashCommand tool from programmatically calling command Type: Boolean Default: false

---
disable-model-invocation: true
---


Use when: Command should only be manually invoked

Dynamic Arguments
Using $ARGUMENTS

Capture all arguments as single string:

---
description: Fix issue by number
argument-hint: [issue-number]
---

Fix issue #$ARGUMENTS following our coding standards and best practices.


Usage:

> /fix-issue 123
> /fix-issue 456


Expands to:

Fix issue #123 following our coding standards...
Fix issue #456 following our coding standards...

Using Positional Arguments

Capture individual arguments with $1, $2, $3, etc.:

---
description: Review PR with priority and assignee
argument-hint: [pr-number] [priority] [assignee]
---

Review pull request #$1 with priority level $2.
After review, assign to $3 for follow-up.


Usage:

> /review-pr 123 high alice


Expands to:

Review pull request #123 with priority level high.
After review, assign to alice for follow-up.

Combining Arguments

Mix positional and remaining arguments:

Deploy $1 to $2 environment with options: $3


Usage:

> /deploy api staging --force --skip-tests


Expands to:

Deploy api to staging environment with options: --force --skip-tests

File References
Using @ Syntax

Include file contents in command:

---
description: Review specific file
argument-hint: [file-path]
---

Review @$1 for:

- Code quality
- Best practices
- Potential bugs


Usage:

> /review-file src/api/users.ts


Effect: Claude reads src/api/users.ts before processing command

Multiple File References

Reference multiple files:

Compare @src/old-version.js with @src/new-version.js

Identify:

- Breaking changes
- New features
- Bug fixes

Static File References

Reference known files without arguments:

Review @package.json and @tsconfig.json for consistency

Ensure:

- TypeScript version matches
- Dependencies are aligned
- Build configuration is correct

Bash Execution in Commands

Commands can execute bash commands inline to dynamically gather context before Claude processes the command. This is useful for including repository state, environment information, or project-specific context.

When to use:

Include dynamic context (git status, environment vars, etc.)
Gather project/repository state
Build context-aware workflows

Implementation details: For complete syntax, examples, and best practices, see references/plugin-features-reference.md section on bash execution. The reference includes the exact syntax and multiple working examples to avoid execution issues

Command Organization
Flat Structure

Simple organization for small command sets:

.claude/commands/
├── build.md
├── test.md
├── deploy.md
├── review.md
└── docs.md


Use when: 5-15 commands, no clear categories

Namespaced Structure

Organize commands in subdirectories:

.claude/commands/
├── ci/
│   ├── build.md        # /build (project:ci)
│   ├── test.md         # /test (project:ci)
│   └── lint.md         # /lint (project:ci)
├── git/
│   ├── commit.md       # /commit (project:git)
│   └── pr.md           # /pr (project:git)
└── docs/
    ├── generate.md     # /generate (project:docs)
    └── publish.md      # /publish (project:docs)


Benefits:

Logical grouping by category
Namespace shown in /help
Easier to find related commands

Use when: 15+ commands, clear categories

Best Practices
Command Design
Single responsibility: One command, one task
Clear descriptions: Self-explanatory in /help
Explicit dependencies: Use allowed-tools when needed
Document arguments: Always provide argument-hint
Consistent naming: Use verb-noun pattern (review-pr, fix-issue)
Argument Handling
Validate arguments: Check for required arguments in prompt
Provide defaults: Suggest defaults when arguments missing
Document format: Explain expected argument format
Handle edge cases: Consider missing or invalid arguments
---
argument-hint: [pr-number]
---

$IF($1,
Review PR #$1,
Please provide a PR number. Usage: /review-pr [number]
)

File References
Explicit paths: Use clear file paths
Check existence: Handle missing files gracefully
Relative paths: Use project-relative paths
Glob support: Consider using Glob tool for patterns
Bash Commands
Limit scope: Use Bash(git:*) not Bash(*)
Safe commands: Avoid destructive operations
Handle errors: Consider command failures
Keep fast: Long-running commands slow invocation
Documentation
Add comments: Explain complex logic
Provide examples: Show usage in comments
List requirements: Document dependencies
Version commands: Note breaking changes
---
description: Deploy application to environment
argument-hint: [environment] [version]
---

<!--
Usage: /deploy [staging|production] [version]
Requires: AWS credentials configured
Example: /deploy staging v1.2.3
-->

Deploy application to $1 environment using version $2...

Common Patterns
Review Pattern
---
description: Review code changes
allowed-tools: Read, Bash(git:*)
---

Files changed: !`git diff --name-only`

Review each file for:

1. Code quality and style
2. Potential bugs or issues
3. Test coverage
4. Documentation needs

Provide specific feedback for each file.

Testing Pattern
---
description: Run tests for specific file
argument-hint: [test-file]
allowed-tools: Bash(npm:*)
---

Run tests: !`npm test $1`

Analyze results and suggest fixes for failures.

Documentation Pattern
---
description: Generate documentation for file
argument-hint: [source-file]
---

Generate comprehensive documentation for @$1 including:

- Function/class descriptions
- Parameter documentation
- Return value descriptions
- Usage examples
- Edge cases and errors

Workflow Pattern
---
description: Complete PR workflow
argument-hint: [pr-number]
allowed-tools: Bash(gh:*), Read
---

PR #$1 Workflow:

1. Fetch PR: !`gh pr view $1`
2. Review changes
3. Run checks
4. Approve or request changes

Troubleshooting

Command not appearing:

Check file is in correct directory
Verify .md extension present
Ensure valid Markdown format
Restart Claude Code

Arguments not working:

Verify $1, $2 syntax correct
Check argument-hint matches usage
Ensure no extra spaces

Bash execution failing:

Check allowed-tools includes Bash
Verify command syntax in backticks
Test command in terminal first
Check for required permissions

File references not working:

Verify @ syntax correct
Check file path is valid
Ensure Read tool allowed
Use absolute or project-relative paths
Plugin-Specific Features
CLAUDE_PLUGIN_ROOT Variable

Plugin commands have access to ${CLAUDE_PLUGIN_ROOT}, an environment variable that resolves to the plugin's absolute path.

Purpose:

Reference plugin files portably
Execute plugin scripts
Load plugin configuration
Access plugin templates

Basic usage:

---
description: Analyze using plugin script
allowed-tools: Bash(node:*)
---

Run analysis: !`node ${CLAUDE_PLUGIN_ROOT}/scripts/analyze.js $1`

Review results and report findings.


Common patterns:

# Execute plugin script

!`bash ${CLAUDE_PLUGIN_ROOT}/scripts/script.sh`

# Load plugin configuration

@${CLAUDE_PLUGIN_ROOT}/config/settings.json

# Use plugin template

@${CLAUDE_PLUGIN_ROOT}/templates/report.md

# Access plugin resources

@${CLAUDE_PLUGIN_ROOT}/docs/reference.md


Why use it:

Works across all installations
Portable between systems
No hardcoded paths needed
Essential for multi-file plugins
Plugin Command Organization

Plugin commands discovered automatically from commands/ directory:

plugin-name/
├── commands/
│   ├── foo.md              # /foo (plugin:plugin-name)
│   ├── bar.md              # /bar (plugin:plugin-name)
│   └── utils/
│       └── helper.md       # /helper (plugin:plugin-name:utils)
└── plugin.json


Namespace benefits:

Logical command grouping
Shown in /help output
Avoid name conflicts
Organize related commands

Naming conventions:

Use descriptive action names
Avoid generic names (test, run)
Consider plugin-specific prefix
Use hyphens for multi-word names
Plugin Command Patterns

Configuration-based pattern:

---
description: Deploy using plugin configuration
argument-hint: [environment]
allowed-tools: Read, Bash(*)
---

Load configuration: @${CLAUDE_PLUGIN_ROOT}/config/$1-deploy.json

Deploy to $1 using configuration settings.
Monitor deployment and report status.


Template-based pattern:

---
description: Generate docs from template
argument-hint: [component]
---

Template: @${CLAUDE_PLUGIN_ROOT}/templates/docs.md

Generate documentation for $1 following template structure.


Multi-script pattern:

---
description: Complete build workflow
allowed-tools: Bash(*)
---

Build: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/build.sh`
Test: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/test.sh`
Package: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/package.sh`

Review outputs and report workflow status.


See references/plugin-features-reference.md for detailed patterns.

Integration with Plugin Components

Commands can integrate with other plugin components for powerful workflows.

Agent Integration

Launch plugin agents for complex tasks:

---
description: Deep code review
argument-hint: [file-path]
---

Initiate comprehensive review of @$1 using the code-reviewer agent.

The agent will analyze:

- Code structure
- Security issues
- Performance
- Best practices

Agent uses plugin resources:

- ${CLAUDE_PLUGIN_ROOT}/config/rules.json
- ${CLAUDE_PLUGIN_ROOT}/checklists/review.md


Key points:

Agent must exist in plugin/agents/ directory
Claude uses Task tool to launch agent
Document agent capabilities
Reference plugin resources agent uses
Skill Integration

Leverage plugin skills for specialized knowledge:

---
description: Document API with standards
argument-hint: [api-file]
---

Document API in @$1 following plugin standards.

Use the api-docs-standards skill to ensure:

- Complete endpoint documentation
- Consistent formatting
- Example quality
- Error documentation

Generate production-ready API docs.


Key points:

Skill must exist in plugin/skills/ directory
Mention skill name to trigger invocation
Document skill purpose
Explain what skill provides
Hook Coordination

Design commands that work with plugin hooks:

Commands can prepare state for hooks to process
Hooks execute automatically on tool events
Commands should document expected hook behavior
Guide Claude on interpreting hook output

See references/plugin-features-reference.md for examples of commands that coordinate with hooks

Multi-Component Workflows

Combine agents, skills, and scripts:

---
description: Comprehensive review workflow
argument-hint: [file]
allowed-tools: Bash(node:*), Read
---

Target: @$1

Phase 1 - Static Analysis:
!`node ${CLAUDE_PLUGIN_ROOT}/scripts/lint.js $1`

Phase 2 - Deep Review:
Launch code-reviewer agent for detailed analysis.

Phase 3 - Standards Check:
Use coding-standards skill for validation.

Phase 4 - Report:
Template: @${CLAUDE_PLUGIN_ROOT}/templates/review.md

Compile findings into report following template.


When to use:

Complex multi-step workflows
Leverage multiple plugin capabilities
Require specialized analysis
Need structured outputs
Validation Patterns

Commands should validate inputs and resources before processing.

Argument Validation
---
description: Deploy with validation
argument-hint: [environment]
---

Validate environment: !`echo "$1" | grep -E "^(dev|staging|prod)$" || echo "INVALID"`

If $1 is valid environment:
Deploy to $1
Otherwise:
Explain valid environments: dev, staging, prod
Show usage: /deploy [environment]

File Existence Checks
---
description: Process configuration
argument-hint: [config-file]
---

Check file exists: !`test -f $1 && echo "EXISTS" || echo "MISSING"`

If file exists:
Process configuration: @$1
Otherwise:
Explain where to place config file
Show expected format
Provide example configuration

Plugin Resource Validation
---
description: Run plugin analyzer
allowed-tools: Bash(test:*)
---

Validate plugin setup:

- Script: !`test -x ${CLAUDE_PLUGIN_ROOT}/bin/analyze && echo "✓" || echo "✗"`
- Config: !`test -f ${CLAUDE_PLUGIN_ROOT}/config.json && echo "✓" || echo "✗"`

If all checks pass, run analysis.
Otherwise, report missing components.

Error Handling
---
description: Build with error handling
allowed-tools: Bash(*)
---

Execute build: !`bash ${CLAUDE_PLUGIN_ROOT}/scripts/build.sh 2>&1 || echo "BUILD_FAILED"`

If build succeeded:
Report success and output location
If build failed:
Analyze error output
Suggest likely causes
Provide troubleshooting steps


Best practices:

Validate early in command
Provide helpful error messages
Suggest corrective actions
Handle edge cases gracefully

For detailed frontmatter field specifications, see references/frontmatter-reference.md. For plugin-specific features and patterns, see references/plugin-features-reference.md. For command pattern examples, see examples/ directory.

Weekly Installs
2.0K
Repository
anthropics/clau…official
GitHub Stars
18.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn