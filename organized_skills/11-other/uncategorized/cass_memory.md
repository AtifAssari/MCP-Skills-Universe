---
rating: ⭐⭐⭐
title: cass-memory
url: https://skills.sh/johnlindquist/claude/cass-memory
---

# cass-memory

skills/johnlindquist/claude/cass-memory
cass-memory
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill cass-memory
SKILL.md
CASS Memory - Contextual Learning System

Build and use a personal playbook of coding patterns learned from your sessions.

Prerequisites

The cm CLI should be available (part of cass-memory system).

Initialize:

cm init
# Or with a starter playbook
cm init --starter typescript
cm init --starter react
cm init --starter python
cm init --starter go

CLI Reference
Get Context for a Task
# THE main command - get relevant rules before starting work
cm context "Description of your task" --json


This returns:

Relevant rules from your playbook
Anti-patterns to avoid
History snippets from similar past work
Reflection (Extract Patterns)
# Run reflection on recent sessions
cm reflect --json

# Specify lookback period
cm reflect --days 7 --json
cm reflect --days 30 --json

Playbook Management
# List all rules
cm playbook list --json

# Get specific rule details
cm playbook get b-8f3a2c --json

# Add a new rule
cm playbook add "Always use optional chaining for nested object access" --json

Feedback on Rules
# Mark rule as helpful
cm mark b-8f3a2c --helpful --json
cm mark b-8f3a2c --helpful --reason "Prevented null error" --json

# Mark rule as harmful
cm mark b-8f3a2c --harmful --json
cm mark b-8f3a2c --harmful --reason "Caused false positive" --json

Record Session Outcomes
# Record success
cm outcome --status success --json
cm outcome --status success --rules "b-8f3a2c,b-4d2e1f" --json

# Record failure
cm outcome --status failure --text "Build failed due to type error" --json

# Mixed results
cm outcome --status mixed --text "Partial completion" --json

Statistics
# Get playbook stats
cm stats --json

Top Rules
# Show most effective rules
cm top --json
cm top 5 --json
cm top 20 --json

Health Check
# Check system health
cm doctor --json

# Auto-fix issues
cm doctor --fix --json

Find Stale Rules
# Rules without recent feedback
cm stale --json
cm stale --days 30 --json
cm stale --days 60 --json

Validate Rules
# Validate a proposed rule against history
cm validate "Proposed rule text" --json

Explain Rule Origin
# Show evidence and reasoning for a rule
cm why b-8f3a2c --json

Usage Statistics
cm usage --json

Starter Playbooks
# List available starters
cm starters --json

Workflow Patterns
Session Start
# Get context before starting a task
cm context "Implement user authentication with JWT" --json

During Work

When a rule helps:

cm mark b-8f3a2c --helpful --json


When a rule leads astray:

cm mark b-8f3a2c --harmful --reason "Not applicable to this framework" --json

Session End
# Record outcome
cm outcome --status success --rules "b-8f3a2c,b-4d2e1f" --json

Periodic Maintenance
# Weekly: Run reflection to extract new patterns
cm reflect --days 7 --json

# Monthly: Review stale rules
cm stale --days 30 --json

# Check system health
cm doctor --json

Building Your Playbook
# Manually add a pattern you've learned
cm playbook add "Use React.memo() for components receiving complex objects as props" --json

# After adding, use it in context queries
cm context "Create a list component with filtering" --json

Rule Lifecycle
Creation - Rules emerge from reflection or manual addition
Usage - Rules surface in context queries
Feedback - Mark as helpful/harmful based on experience
Evolution - High-feedback rules rise, low-feedback rules become stale
Retirement - Stale rules get reviewed and pruned
Best Practices
Always get context first - Run cm context "task" before starting work
Provide feedback - Mark rules as helpful/harmful
Record outcomes - Track session success/failure
Run reflection regularly - Weekly reflection extracts new patterns
Review stale rules - Don't let old rules accumulate
Add rules manually - When you learn something important
Integration Tips
Pre-Task Context

Before any significant coding task:

CONTEXT=$(cm context "Your task description" --json)
# Use context to inform your approach

Post-Session Recording

At end of coding session:

cm outcome --status success --text "Completed feature X" --json

Weekly Installs
29
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass