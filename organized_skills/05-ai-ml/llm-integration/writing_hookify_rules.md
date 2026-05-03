---
rating: ⭐⭐⭐
title: writing hookify rules
url: https://skills.sh/anthropics/claude-code/writing-hookify-rules
---

# writing hookify rules

skills/anthropics/claude-code/Writing Hookify Rules
Writing Hookify Rules
Installation
$ npx skills add https://github.com/anthropics/claude-code --skill 'Writing Hookify Rules'
Summary

Define patterns and messages that trigger Claude warnings or blocks on specific agent actions.

Supports four event types (bash commands, file edits, agent stop, user prompts) plus an "all" catch-all, each with regex or multi-condition matching
Rules use markdown files with YAML frontmatter stored in .claude/hookify.{name}.local.md; changes take effect immediately on next tool use
Two matching modes: simple pattern field for single-condition rules, or advanced conditions array for multi-field logic with operators like regex_match, contains, equals, and starts_with
Actions default to warn (show message, allow operation) or can be set to block (prevent operation or stop session)
Includes regex pattern guide with common metacharacters, escaping rules, and examples for detecting dangerous commands, debug code, security risks, and sensitive files
SKILL.md
Writing Hookify Rules
Overview

Hookify rules are markdown files with YAML frontmatter that define patterns to watch for and messages to show when those patterns match. Rules are stored in .claude/hookify.{rule-name}.local.md files.

Rule File Format
Basic Structure
---
name: rule-identifier
enabled: true
event: bash|file|stop|prompt|all
pattern: regex-pattern-here
---

Message to show Claude when this rule triggers.
Can include markdown formatting, warnings, suggestions, etc.

Frontmatter Fields

name (required): Unique identifier for the rule

Use kebab-case: warn-dangerous-rm, block-console-log
Be descriptive and action-oriented
Start with verb: warn, prevent, block, require, check

enabled (required): Boolean to activate/deactivate

true: Rule is active
false: Rule is disabled (won't trigger)
Can toggle without deleting rule

event (required): Which hook event to trigger on

bash: Bash tool commands
file: Edit, Write, MultiEdit tools
stop: When agent wants to stop
prompt: When user submits a prompt
all: All events

action (optional): What to do when rule matches

warn: Show message but allow operation (default)
block: Prevent operation (PreToolUse) or stop session (Stop events)
If omitted, defaults to warn

pattern (simple format): Regex pattern to match

Used for simple single-condition rules
Matches against command (bash) or new_text (file)
Python regex syntax

Example:

event: bash
pattern: rm\s+-rf

Advanced Format (Multiple Conditions)

For complex rules with multiple conditions:

---
name: warn-env-file-edits
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.env$
  - field: new_text
    operator: contains
    pattern: API_KEY
---

You're adding an API key to a .env file. Ensure this file is in .gitignore!


Condition fields:

field: Which field to check
For bash: command
For file: file_path, new_text, old_text, content
operator: How to match
regex_match: Regex pattern matching
contains: Substring check
equals: Exact match
not_contains: Substring must NOT be present
starts_with: Prefix check
ends_with: Suffix check
pattern: Pattern or string to match

All conditions must match for rule to trigger.

Message Body

The markdown content after frontmatter is shown to Claude when the rule triggers.

Good messages:

Explain what was detected
Explain why it's problematic
Suggest alternatives or best practices
Use formatting for clarity (bold, lists, etc.)

Example:

⚠️ **Console.log detected!**

You're adding console.log to production code.

**Why this matters:**
- Debug logs shouldn't ship to production
- Console.log can expose sensitive data
- Impacts browser performance

**Alternatives:**
- Use a proper logging library
- Remove before committing
- Use conditional debug builds

Event Type Guide
bash Events

Match Bash command patterns:

---
event: bash
pattern: sudo\s+|rm\s+-rf|chmod\s+777
---

Dangerous command detected!


Common patterns:

Dangerous commands: rm\s+-rf, dd\s+if=, mkfs
Privilege escalation: sudo\s+, su\s+
Permission issues: chmod\s+777, chown\s+root
file Events

Match Edit/Write/MultiEdit operations:

---
event: file
pattern: console\.log\(|eval\(|innerHTML\s*=
---

Potentially problematic code pattern detected!


Match on different fields:

---
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.tsx?$
  - field: new_text
    operator: regex_match
    pattern: console\.log\(
---

Console.log in TypeScript file!


Common patterns:

Debug code: console\.log\(, debugger, print\(
Security risks: eval\(, innerHTML\s*=, dangerouslySetInnerHTML
Sensitive files: \.env$, credentials, \.pem$
Generated files: node_modules/, dist/, build/
stop Events

Match when agent wants to stop (completion checks):

---
event: stop
pattern: .*
---

Before stopping, verify:
- [ ] Tests were run
- [ ] Build succeeded
- [ ] Documentation updated


Use for:

Reminders about required steps
Completion checklists
Process enforcement
prompt Events

Match user prompt content (advanced):

---
event: prompt
conditions:
  - field: user_prompt
    operator: contains
    pattern: deploy to production
---

Production deployment checklist:
- [ ] Tests passing?
- [ ] Reviewed by team?
- [ ] Monitoring ready?

Pattern Writing Tips
Regex Basics

Literal characters: Most characters match themselves

rm matches "rm"
console.log matches "console.log"

Special characters need escaping:

. (any char) → \. (literal dot)
( ) → \( \) (literal parens)
[ ] → \[ \] (literal brackets)

Common metacharacters:

\s - whitespace (space, tab, newline)
\d - digit (0-9)
\w - word character (a-z, A-Z, 0-9, _)
. - any character
+ - one or more
* - zero or more
? - zero or one
| - OR

Examples:

rm\s+-rf         Matches: rm -rf, rm  -rf
console\.log\(   Matches: console.log(
(eval|exec)\(    Matches: eval( or exec(
chmod\s+777      Matches: chmod 777, chmod  777
API_KEY\s*=      Matches: API_KEY=, API_KEY =

Testing Patterns

Test regex patterns before using:

python3 -c "import re; print(re.search(r'your_pattern', 'test text'))"


Or use online regex testers (regex101.com with Python flavor).

Common Pitfalls

Too broad:

pattern: log    # Matches "log", "login", "dialog", "catalog"


Better: console\.log\(|logger\.

Too specific:

pattern: rm -rf /tmp  # Only matches exact path


Better: rm\s+-rf

Escaping issues:

YAML quoted strings: "pattern" requires double backslashes \\s
YAML unquoted: pattern: \s works as-is
Recommendation: Use unquoted patterns in YAML
File Organization

Location: All rules in .claude/ directory Naming: .claude/hookify.{descriptive-name}.local.md Gitignore: Add .claude/*.local.md to .gitignore

Good names:

hookify.dangerous-rm.local.md
hookify.console-log.local.md
hookify.require-tests.local.md
hookify.sensitive-files.local.md

Bad names:

hookify.rule1.local.md (not descriptive)
hookify.md (missing .local)
danger.local.md (missing hookify prefix)
Workflow
Creating a Rule
Identify unwanted behavior
Determine which tool is involved (Bash, Edit, etc.)
Choose event type (bash, file, stop, etc.)
Write regex pattern
Create .claude/hookify.{name}.local.md file in project root
Test immediately - rules are read dynamically on next tool use
Refining a Rule
Edit the .local.md file
Adjust pattern or message
Test immediately - changes take effect on next tool use
Disabling a Rule

Temporary: Set enabled: false in frontmatter Permanent: Delete the .local.md file

Examples

See ${CLAUDE_PLUGIN_ROOT}/examples/ for complete examples:

dangerous-rm.local.md - Block dangerous rm commands
console-log-warning.local.md - Warn about console.log
sensitive-files-warning.local.md - Warn about editing .env files
Quick Reference

Minimum viable rule:

---
name: my-rule
enabled: true
event: bash
pattern: dangerous_command
---

Warning message here


Rule with conditions:

---
name: my-rule
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.ts$
  - field: new_text
    operator: contains
    pattern: any
---

Warning message


Event types:

bash - Bash commands
file - File edits
stop - Completion checks
prompt - User input
all - All events

Field options:

Bash: command
File: file_path, new_text, old_text, content
Prompt: user_prompt

Operators:

regex_match, contains, equals, not_contains, starts_with, ends_with
Weekly Installs
–
Repository
anthropics/claude-code
GitHub Stars
119.8K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass