---
title: oclif-patterns
url: https://skills.sh/vanman2024/cli-builder/oclif-patterns
---

# oclif-patterns

skills/vanman2024/cli-builder/oclif-patterns
oclif-patterns
Installation
$ npx skills add https://github.com/vanman2024/cli-builder --skill oclif-patterns
SKILL.md
oclif Enterprise CLI Patterns

Provides comprehensive patterns for building production-grade CLIs with oclif framework.

Core Capabilities
1. Command Structure
Single and multi-command CLIs
Flag definitions (string, boolean, integer, custom)
Argument parsing with validation
Command inheritance and base classes
Async command execution
2. Plugin System
Installable plugins
Plugin discovery and loading
Hook system for extensibility
Plugin commands and lifecycle
3. Auto-Documentation
Auto-generated help text
README generation
Command reference docs
Flag and argument documentation
4. Testing Patterns
Command unit tests
Integration testing
Mock stdin/stdout
Fixture management
Test helpers
Implementation Guide
Command Creation

Use templates:

templates/command-basic.ts - Simple command with flags
templates/command-advanced.ts - Complex command with validation
templates/command-async.ts - Async operations
templates/base-command.ts - Custom base class

Key patterns:

Import Command from '@oclif/core'
Define flags using Flags object
Define args using Args object
Implement async run() method
Use this.log() for output
Use this.error() for errors
Flag Patterns

Common flags:

String: Flags.string({ description, required, default })
Boolean: Flags.boolean({ description, allowNo })
Integer: Flags.integer({ description, min, max })
Custom: Flags.custom<T>({ parse: async (input) => T })
Multiple: Flags.string({ multiple: true })

Best practices:

Always provide clear descriptions
Use char for common short flags
Set required vs optional explicitly
Provide sensible defaults
Validate in parse function for custom flags
Argument Patterns

Definition:

static args = {
  name: Args.string({ description: 'Name', required: true }),
  file: Args.file({ description: 'File path', exists: true })
}


Access in run():

const { args } = await this.parse(MyCommand)

Plugin Development

Use templates:

templates/plugin-package.json - Plugin package.json
templates/plugin-command.ts - Plugin command structure
templates/plugin-hooks.ts - Hook implementations

Plugin structure:

my-plugin/
├── package.json (oclif configuration)
├── src/
│   ├── commands/ (plugin commands)
│   └── hooks/ (lifecycle hooks)
├── test/ (plugin tests)
└── README.md

Testing Setup

Use templates:

templates/test-command.ts - Command test template
templates/test-helpers.ts - Test utilities
templates/test-setup.ts - Test configuration

Testing approach:

Use @oclif/test for test helpers
Mock stdin/stdout with fancy-test
Test flag parsing separately
Test command execution
Test error handling
Use fixtures for file operations
Auto-Documentation

Generated automatically:

Command help via --help flag
README.md with command reference
Usage examples
Flag and argument tables

Use scripts:

scripts/generate-docs.sh - Generate all documentation
scripts/update-readme.sh - Update README with commands
Quick Start Examples
Create Basic Command
# Use template
./scripts/create-command.sh my-command basic

# Results in: src/commands/my-command.ts

Create Plugin
# Use template
./scripts/create-plugin.sh my-plugin

# Results in: plugin directory structure

Run Tests
# Use test helpers
npm test
# or with coverage
npm run test:coverage

Validation Scripts

Available validators:

scripts/validate-command.sh - Check command structure
scripts/validate-plugin.sh - Verify plugin structure
scripts/validate-tests.sh - Ensure test coverage
Templates Reference
TypeScript Commands
command-basic.ts - Simple command pattern
command-advanced.ts - Full-featured command
command-async.ts - Async/await patterns
base-command.ts - Custom base class
command-with-config.ts - Configuration management
Plugin System
plugin-package.json - Plugin package.json
plugin-command.ts - Plugin command
plugin-hooks.ts - Hook implementations
plugin-manifest.json - Plugin manifest
Testing
test-command.ts - Command unit test
test-helpers.ts - Test utilities
test-setup.ts - Test configuration
test-integration.ts - Integration test
Configuration
tsconfig.json - TypeScript config
package.json - oclif package.json
.eslintrc.json - ESLint config
Examples Directory

See examples/ for complete working examples:

examples/basic-cli/ - Simple CLI with commands
examples/plugin-cli/ - CLI with plugin support
examples/enterprise-cli/ - Full enterprise setup
Common Patterns
Error Handling
if (!valid) {
  this.error('Invalid input', { exit: 1 })
}

Spinner/Progress
const spinner = ux.action.start('Processing')
// ... work
ux.action.stop()

Prompts
const answer = await ux.prompt('Continue?')

Table Output
ux.table(data, { columns: [...] })

Requirements
Node.js 18+
TypeScript 5+
@oclif/core ^3.0.0
@oclif/test for testing
Knowledge of TypeScript decorators (optional but helpful)
Best Practices
Command Design: Keep commands focused, single responsibility
Flags: Use descriptive names, provide help text
Testing: Test command parsing and execution separately
Documentation: Let oclif generate docs, keep them updated
Plugins: Design for extensibility from the start
Error Messages: Provide actionable error messages
TypeScript: Use strict mode, define proper types
Async: Use async/await, handle promises properly
Advanced Features
Custom Flag Types

Create reusable custom flag parsers for complex validation.

Hook System

Implement hooks for: init, prerun, postrun, command_not_found.

Topic Commands

Organize commands into topics (e.g., mycli topic:command).

Auto-Update

Use @oclif/plugin-update for automatic CLI updates.

Analytics

Integrate analytics to track command usage.

Weekly Installs
15
Repository
vanman2024/cli-builder
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass