---
title: error-handling
url: https://skills.sh/mwguerra/claude-code-plugins/error-handling
---

# error-handling

skills/mwguerra/claude-code-plugins/error-handling
error-handling
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill error-handling
SKILL.md
Error Handling Skill

Handle errors intelligently by leveraging past solutions and building a knowledge base of fixes.

Core Workflow
When Encountering an Error
Recognize the error - Identify the error message and its type
Search for solutions - Check if a similar error was solved before
Apply or adapt - Use the found solution or develop a new one
Log for future - After solving, log the error and solution
Error Recognition

Recognize errors from multiple sources:

Source	Indicators
Bash commands	Non-zero exit code, stderr output, error keywords
Playwright/Browser	Console errors, network failures, page crashes
Log files	Error patterns in file content
Build output	Compilation failures, missing dependencies
API responses	HTTP 4xx/5xx status codes, error JSON
User messages	User describes or pastes an error

Error type keywords to watch for:

PHP/Laravel: Fatal error, SQLSTATE, Exception, Class not found
JavaScript: TypeError, ReferenceError, Cannot find module
Python: Traceback, ImportError, AttributeError
Database: Connection refused, Access denied, Table doesn't exist
Docker: container is not running, port already allocated
Searching for Solutions

When an error is encountered:

# Search the error memory database
bash $CLAUDE_PLUGIN_ROOT/scripts/search.sh "<error message>" --max 5


Interpret confidence levels:

100%: Exact match - apply solution directly
70-99%: Very similar - solution likely works, may need minor adaptation
50-69%: Related error - review solution for applicability
30-49%: Loosely related - use as reference only
Logging New Errors

After solving an error not found in the database:

bash $CLAUDE_PLUGIN_ROOT/scripts/log-error.sh --json '{
  "errorMessage": "<full error message>",
  "project": "<project name>",
  "projectPath": "<working directory>",
  "source": "<bash|playwright|read|user|build|api|other>",
  "whatHappened": "<what was being done when error occurred>",
  "cause": "<root cause of the error>",
  "solution": "<how it was fixed>",
  "rationale": "<why the solution works>",
  "fileChanged": "<optional: file that was modified>",
  "codeBefore": "<optional: code before fix>",
  "codeAfter": "<optional: code after fix>",
  "tags": ["tag1", "tag2"]
}'

Error Source Classification

Classify errors by their origin for better matching:

Source	When to Use
bash	Errors from shell commands, scripts, CLI tools
playwright	Browser errors, page load failures, element not found
read	Errors found when reading log files or error outputs
user	Errors the user describes or pastes directly
build	Compilation errors, asset building failures
api	HTTP errors, API response errors
other	Anything that doesn't fit above categories
Tagging Guidelines

Use consistent tags for better searchability:

Technology tags:

Languages: php, javascript, python, typescript
Frameworks: laravel, react, vue, filament, livewire
Tools: docker, composer, npm, git

Domain tags:

database, api, auth, forms, validation
routing, middleware, permissions, migrations
testing, deployment, configuration

Error type tags:

connection, syntax, runtime, type-error
missing-dependency, permission, timeout
Available Commands
Command	Purpose
/error-memory:search <query>	Search for similar errors
/error-memory:log	Log a new error interactively
/error-memory:list	List all stored errors
/error-memory:show <id>	View full error details
/error-memory:stats	View database statistics
/error-memory:migrate	Import from old solved-errors.md
/error-memory:init	Initialize the database
Proactive Error Handling
Before Running Commands

If about to run a command that commonly fails:

Consider what errors might occur
Have error handling ready (try/catch, error codes)
Know where to look for solutions
After Errors Occur
Don't immediately retry the same thing
Search for the error first
Understand the cause before applying a fix
Verify the fix actually resolved the issue
Log the solution for future reference
Recognizing Patterns

Watch for recurring error patterns:

Same error type across projects → systemic issue
Same project with multiple errors → architectural problem
Same tag appearing often → skill gap to address
Integration with CLAUDE.md

The error memory system enhances the existing CLAUDE.md instruction to log errors to ~/.claude/solved-errors.md by providing:

Structured storage instead of markdown
Intelligent search with fuzzy matching
Usage tracking and statistics
Automatic error detection via hooks

The old solved-errors.md can be migrated with /error-memory:migrate.

Additional Resources

For detailed error patterns and matching algorithm:

references/error-patterns.md - Common error patterns by technology
Weekly Installs
15
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass