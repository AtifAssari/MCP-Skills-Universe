---
rating: ⭐⭐⭐
title: plugin-settings
url: https://skills.sh/anthropics/claude-plugins-official/plugin-settings
---

# plugin-settings

skills/anthropics/claude-plugins-official/plugin-settings
plugin-settings
Originally fromanthropics/claude-code
Installation
$ npx skills add https://github.com/anthropics/claude-plugins-official --skill plugin-settings
Summary

Store per-project plugin configuration and state in .claude/plugin-name.local.md files with YAML frontmatter.

Settings files use YAML frontmatter for structured configuration and markdown body for additional context or prompts
Hooks, commands, and agents can read settings to customize behavior without requiring code changes
Includes bash parsing patterns for extracting individual fields (strings, booleans, numerics) and markdown body content
Common patterns include toggling hook activation, managing agent state, and driving configuration-based behavior
Settings changes require Claude Code restart; files should be gitignored and user-managed, not committed to version control
SKILL.md
Plugin Settings Pattern for Claude Code Plugins
Overview

Plugins can store user-configurable settings and state in .claude/plugin-name.local.md files within the project directory. This pattern uses YAML frontmatter for structured configuration and markdown content for prompts or additional context.

Key characteristics:

File location: .claude/plugin-name.local.md in project root
Structure: YAML frontmatter + markdown body
Purpose: Per-project plugin configuration and state
Usage: Read from hooks, commands, and agents
Lifecycle: User-managed (not in git, should be in .gitignore)
File Structure
Basic Template
---
enabled: true
setting1: value1
setting2: value2
numeric_setting: 42
list_setting: ["item1", "item2"]
---

# Additional Context

This markdown body can contain:
- Task descriptions
- Additional instructions
- Prompts to feed back to Claude
- Documentation or notes

Example: Plugin State File

.claude/my-plugin.local.md:

---
enabled: true
strict_mode: false
max_retries: 3
notification_level: info
coordinator_session: team-leader
---

# Plugin Configuration

This plugin is configured for standard validation mode.
Contact @team-lead with questions.

Reading Settings Files
From Hooks (Bash Scripts)

Pattern: Check existence and parse frontmatter

#!/bin/bash
set -euo pipefail

# Define state file path
STATE_FILE=".claude/my-plugin.local.md"

# Quick exit if file doesn't exist
if [[ ! -f "$STATE_FILE" ]]; then
  exit 0  # Plugin not configured, skip
fi

# Parse YAML frontmatter (between --- markers)
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$STATE_FILE")

# Extract individual fields
ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//' | sed 's/^"\(.*\)"$/\1/')
STRICT_MODE=$(echo "$FRONTMATTER" | grep '^strict_mode:' | sed 's/strict_mode: *//' | sed 's/^"\(.*\)"$/\1/')

# Check if enabled
if [[ "$ENABLED" != "true" ]]; then
  exit 0  # Disabled
fi

# Use configuration in hook logic
if [[ "$STRICT_MODE" == "true" ]]; then
  # Apply strict validation
  # ...
fi


See examples/read-settings-hook.sh for complete working example.

From Commands

Commands can read settings files to customize behavior:

---
description: Process data with plugin
allowed-tools: ["Read", "Bash"]
---

# Process Command

Steps:
1. Check if settings exist at `.claude/my-plugin.local.md`
2. Read configuration using Read tool
3. Parse YAML frontmatter to extract settings
4. Apply settings to processing logic
5. Execute with configured behavior

From Agents

Agents can reference settings in their instructions:

---
name: configured-agent
description: Agent that adapts to project settings
---

Check for plugin settings at `.claude/my-plugin.local.md`.
If present, parse YAML frontmatter and adapt behavior according to:
- enabled: Whether plugin is active
- mode: Processing mode (strict, standard, lenient)
- Additional configuration fields

Parsing Techniques
Extract Frontmatter
# Extract everything between --- markers
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")

Read Individual Fields

String fields:

VALUE=$(echo "$FRONTMATTER" | grep '^field_name:' | sed 's/field_name: *//' | sed 's/^"\(.*\)"$/\1/')


Boolean fields:

ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//')
# Compare: if [[ "$ENABLED" == "true" ]]; then


Numeric fields:

MAX=$(echo "$FRONTMATTER" | grep '^max_value:' | sed 's/max_value: *//')
# Use: if [[ $MAX -gt 100 ]]; then

Read Markdown Body

Extract content after second ---:

# Get everything after closing ---
BODY=$(awk '/^---$/{i++; next} i>=2' "$FILE")

Common Patterns
Pattern 1: Temporarily Active Hooks

Use settings file to control hook activation:

#!/bin/bash
STATE_FILE=".claude/security-scan.local.md"

# Quick exit if not configured
if [[ ! -f "$STATE_FILE" ]]; then
  exit 0
fi

# Read enabled flag
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$STATE_FILE")
ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//')

if [[ "$ENABLED" != "true" ]]; then
  exit 0  # Disabled
fi

# Run hook logic
# ...


Use case: Enable/disable hooks without editing hooks.json (requires restart).

Pattern 2: Agent State Management

Store agent-specific state and configuration:

.claude/multi-agent-swarm.local.md:

---
agent_name: auth-agent
task_number: 3.5
pr_number: 1234
coordinator_session: team-leader
enabled: true
dependencies: ["Task 3.4"]
---

# Task Assignment

Implement JWT authentication for the API.

**Success Criteria:**
- Authentication endpoints created
- Tests passing
- PR created and CI green


Read from hooks to coordinate agents:

AGENT_NAME=$(echo "$FRONTMATTER" | grep '^agent_name:' | sed 's/agent_name: *//')
COORDINATOR=$(echo "$FRONTMATTER" | grep '^coordinator_session:' | sed 's/coordinator_session: *//')

# Send notification to coordinator
tmux send-keys -t "$COORDINATOR" "Agent $AGENT_NAME completed task" Enter

Pattern 3: Configuration-Driven Behavior

.claude/my-plugin.local.md:

---
validation_level: strict
max_file_size: 1000000
allowed_extensions: [".js", ".ts", ".tsx"]
enable_logging: true
---

# Validation Configuration

Strict mode enabled for this project.
All writes validated against security policies.


Use in hooks or commands:

LEVEL=$(echo "$FRONTMATTER" | grep '^validation_level:' | sed 's/validation_level: *//')

case "$LEVEL" in
  strict)
    # Apply strict validation
    ;;
  standard)
    # Apply standard validation
    ;;
  lenient)
    # Apply lenient validation
    ;;
esac

Creating Settings Files
From Commands

Commands can create settings files:

# Setup Command

Steps:
1. Ask user for configuration preferences
2. Create `.claude/my-plugin.local.md` with YAML frontmatter
3. Set appropriate values based on user input
4. Inform user that settings are saved
5. Remind user to restart Claude Code for hooks to recognize changes

Template Generation

Provide template in plugin README:

## Configuration

Create `.claude/my-plugin.local.md` in your project:

\`\`\`markdown
---
enabled: true
mode: standard
max_retries: 3
---

# Plugin Configuration

Your settings are active.
\`\`\`

After creating or editing, restart Claude Code for changes to take effect.

Best Practices
File Naming

✅ DO:

Use .claude/plugin-name.local.md format
Match plugin name exactly
Use .local.md suffix for user-local files

❌ DON'T:

Use different directory (not .claude/)
Use inconsistent naming
Use .md without .local (might be committed)
Gitignore

Always add to .gitignore:

.claude/*.local.md
.claude/*.local.json


Document this in plugin README.

Defaults

Provide sensible defaults when settings file doesn't exist:

if [[ ! -f "$STATE_FILE" ]]; then
  # Use defaults
  ENABLED=true
  MODE=standard
else
  # Read from file
  # ...
fi

Validation

Validate settings values:

MAX=$(echo "$FRONTMATTER" | grep '^max_value:' | sed 's/max_value: *//')

# Validate numeric range
if ! [[ "$MAX" =~ ^[0-9]+$ ]] || [[ $MAX -lt 1 ]] || [[ $MAX -gt 100 ]]; then
  echo "⚠️  Invalid max_value in settings (must be 1-100)" >&2
  MAX=10  # Use default
fi

Restart Requirement

Important: Settings changes require Claude Code restart.

Document in your README:

## Changing Settings

After editing `.claude/my-plugin.local.md`:
1. Save the file
2. Exit Claude Code
3. Restart: `claude` or `cc`
4. New settings will be loaded


Hooks cannot be hot-swapped within a session.

Security Considerations
Sanitize User Input

When writing settings files from user input:

# Escape quotes in user input
SAFE_VALUE=$(echo "$USER_INPUT" | sed 's/"/\\"/g')

# Write to file
cat > "$STATE_FILE" <<EOF
---
user_setting: "$SAFE_VALUE"
---
EOF

Validate File Paths

If settings contain file paths:

FILE_PATH=$(echo "$FRONTMATTER" | grep '^data_file:' | sed 's/data_file: *//')

# Check for path traversal
if [[ "$FILE_PATH" == *".."* ]]; then
  echo "⚠️  Invalid path in settings (path traversal)" >&2
  exit 2
fi

Permissions

Settings files should be:

Readable by user only (chmod 600)
Not committed to git
Not shared between users
Real-World Examples
multi-agent-swarm Plugin

.claude/multi-agent-swarm.local.md:

---
agent_name: auth-implementation
task_number: 3.5
pr_number: 1234
coordinator_session: team-leader
enabled: true
dependencies: ["Task 3.4"]
additional_instructions: Use JWT tokens, not sessions
---

# Task: Implement Authentication

Build JWT-based authentication for the REST API.
Coordinate with auth-agent on shared types.


Hook usage (agent-stop-notification.sh):

Checks if file exists (line 15-18: quick exit if not)
Parses frontmatter to get coordinator_session, agent_name, enabled
Sends notifications to coordinator if enabled
Allows quick activation/deactivation via enabled: true/false
ralph-loop Plugin

.claude/ralph-loop.local.md:

---
iteration: 1
max_iterations: 10
completion_promise: "All tests passing and build successful"
---

Fix all the linting errors in the project.
Make sure tests pass after each fix.


Hook usage (stop-hook.sh):

Checks if file exists (line 15-18: quick exit if not active)
Reads iteration count and max_iterations
Extracts completion_promise for loop termination
Reads body as the prompt to feed back
Updates iteration count on each loop
Quick Reference
File Location
project-root/
└── .claude/
    └── plugin-name.local.md

Frontmatter Parsing
# Extract frontmatter
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")

# Read field
VALUE=$(echo "$FRONTMATTER" | grep '^field:' | sed 's/field: *//' | sed 's/^"\(.*\)"$/\1/')

Body Parsing
# Extract body (after second ---)
BODY=$(awk '/^---$/{i++; next} i>=2' "$FILE")

Quick Exit Pattern
if [[ ! -f ".claude/my-plugin.local.md" ]]; then
  exit 0  # Not configured
fi

Additional Resources
Reference Files

For detailed implementation patterns:

references/parsing-techniques.md - Complete guide to parsing YAML frontmatter and markdown bodies
references/real-world-examples.md - Deep dive into multi-agent-swarm and ralph-loop implementations
Example Files

Working examples in examples/:

read-settings-hook.sh - Hook that reads and uses settings
create-settings-command.md - Command that creates settings file
example-settings.md - Template settings file
Utility Scripts

Development tools in scripts/:

validate-settings.sh - Validate settings file structure
parse-frontmatter.sh - Extract frontmatter fields
Implementation Workflow

To add settings to a plugin:

Design settings schema (which fields, types, defaults)
Create template file in plugin documentation
Add gitignore entry for .claude/*.local.md
Implement settings parsing in hooks/commands
Use quick-exit pattern (check file exists, check enabled field)
Document settings in plugin README with template
Remind users that changes require Claude Code restart

Focus on keeping settings simple and providing good defaults when settings file doesn't exist.

Weekly Installs
1.9K
Repository
anthropics/clau…official
GitHub Stars
18.4K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass