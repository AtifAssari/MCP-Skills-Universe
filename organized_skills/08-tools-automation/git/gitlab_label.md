---
rating: ⭐⭐⭐
title: gitlab-label
url: https://skills.sh/grandcamel/gitlab-assistant-skills/gitlab-label
---

# gitlab-label

skills/grandcamel/gitlab-assistant-skills/gitlab-label
gitlab-label
Installation
$ npx skills add https://github.com/grandcamel/gitlab-assistant-skills --skill gitlab-label
SKILL.md
Label Skill

Label management operations for GitLab using the glab CLI.

Quick Reference
Operation	Command	Risk
List labels	glab label list	-
Create label	glab label create <name>	⚠️

Risk Legend: - Safe | ⚠️ Caution | ⚠️⚠️ Warning | ⚠️⚠️⚠️ Danger

When to Use This Skill

ALWAYS use when:

User wants to manage project labels
User mentions "label", "tag" (for categorization), "category"
User wants to organize issues or MRs

NEVER use when:

User wants to apply labels to issues/MRs (use gitlab-issue or gitlab-mr)
User wants to manage git tags (use git commands or gitlab-release)
Available Commands
List Labels
glab label list [options]


Options:

Flag	Description
-P, --per-page=<n>	Results per page
--all	Get all labels

Examples:

# List all project labels
glab label list

# List with more results
glab label list --per-page=100

Create Label
glab label create <name> [options]


Options:

Flag	Description
-c, --color=<color>	Label color (hex format, e.g., #ff0000)
-d, --description=<desc>	Label description

Examples:

# Create label with default color
glab label create "needs-review"

# Create label with color
glab label create "bug" -c "#ff0000"

# Create label with color and description
glab label create "priority::high" \
  -c "#dc3545" \
  -d "High priority items requiring immediate attention"

# Create scoped label
glab label create "status::in-progress" \
  -c "#ffc107" \
  -d "Work in progress"

Common Label Patterns
Priority Labels
glab label create "priority::critical" -c "#dc3545" -d "Must fix immediately"
glab label create "priority::high" -c "#fd7e14" -d "Fix in current sprint"
glab label create "priority::medium" -c "#ffc107" -d "Fix soon"
glab label create "priority::low" -c "#28a745" -d "Nice to have"

Type Labels
glab label create "type::bug" -c "#d73a4a" -d "Something isn't working"
glab label create "type::feature" -c "#0366d6" -d "New feature request"
glab label create "type::docs" -c "#0075ca" -d "Documentation"
glab label create "type::refactor" -c "#6f42c1" -d "Code refactoring"

Status Labels
glab label create "status::backlog" -c "#6c757d" -d "In backlog"
glab label create "status::ready" -c "#17a2b8" -d "Ready to start"
glab label create "status::in-progress" -c "#ffc107" -d "Work in progress"
glab label create "status::review" -c "#007bff" -d "In review"
glab label create "status::done" -c "#28a745" -d "Completed"

Workflow Labels
glab label create "needs-review" -c "#d876e3" -d "Needs code review"
glab label create "needs-design" -c "#fbca04" -d "Needs design input"
glab label create "blocked" -c "#b60205" -d "Blocked by external dependency"
glab label create "help-wanted" -c "#008672" -d "Looking for contributors"

GitLab Scoped Labels

GitLab supports scoped labels using the :: separator:

priority::high
status::in-progress
type::bug


Only one label per scope can be applied to an issue/MR, making them mutually exclusive.

Common Workflows
Workflow 1: Set Up New Project Labels
# Create priority labels
glab label create "priority::critical" -c "#dc3545"
glab label create "priority::high" -c "#fd7e14"
glab label create "priority::medium" -c "#ffc107"
glab label create "priority::low" -c "#28a745"

# Create type labels
glab label create "type::bug" -c "#d73a4a"
glab label create "type::feature" -c "#0366d6"
glab label create "type::docs" -c "#0075ca"

Workflow 2: Apply Labels to Issues
# List available labels
glab label list

# Create issue with labels
glab issue create -t "Fix login bug" -l "type::bug,priority::high"

# Update issue labels
glab issue update 42 -l "status::in-progress"

Color Reference

Common colors for labels:

Color	Hex	Use For
Red	#dc3545	Bugs, critical, blocked
Orange	#fd7e14	High priority, warning
Yellow	#ffc107	Medium priority, in-progress
Green	#28a745	Done, low priority, good first issue
Blue	#007bff	Features, info, review
Purple	#6f42c1	Refactor, enhancement
Gray	#6c757d	Backlog, wontfix
Troubleshooting
Issue	Cause	Solution
Authentication failed	Invalid/expired token	Run glab auth login
Label already exists	Duplicate name	Use different name or update existing
Invalid color	Wrong format	Use hex format: #RRGGBB
Permission denied	Not maintainer	Need maintainer+ role
Related Documentation
Safeguards
Quick Reference
Weekly Installs
83
Repository
grandcamel/gitl…t-skills
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass