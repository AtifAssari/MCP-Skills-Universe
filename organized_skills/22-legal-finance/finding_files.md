---
rating: ⭐⭐⭐
title: finding-files
url: https://skills.sh/iota9star/my-skills/finding-files
---

# finding-files

skills/iota9star/my-skills/finding-files
finding-files
Installation
$ npx skills add https://github.com/iota9star/my-skills --skill finding-files
SKILL.md
fd: Intuitive File Search

Always invoke fd skill for fast file discovery - do not execute bash commands directly.

Use fd for fast file discovery that's 13-23x faster than find.

Default Strategy

Invoke fd skill for fast file discovery with parallel search and smart defaults. Use when searching for files by name, pattern, or type, especially when performance matters or when working with large directories.

Common workflow: fd skill → other skills (fzf, bat, ripgrep, sd) for further processing.

Key Options
-e ext for extension filtering
-t file|dir for type filtering
-H include hidden files
-I ignore .gitignore
--exclude pattern exclusions
-x exec per file, -X exec batch
{}, {.}, {/} placeholders
When to Use
Quick file searches by pattern
Filter by type, size, extension
Search with depth limits
Batch file operations
Integration with other tools
Common Workflows
fd → fzf → bat: Search files, select interactively, view with syntax highlighting
fd → sd: Find files and perform batch replacements
fd → xargs tool: Execute commands on found files
fd → ripgrep: Search within specific file types
Core Principle

Smart defaults: ignores hidden/.gitignore files, case-insensitive, parallel search - much faster than find.

Detailed Reference

For comprehensive search patterns, filtering options, execution examples, and performance tips, load fd guide when needing:

Advanced filtering patterns (size, time, depth)
Batch execution with placeholders
Performance optimization techniques
Integration with shell scripts
Complex exclusion patterns

The guide includes:

Core search patterns and file discovery
Extension and type filtering techniques
Execution and batch operation examples
Performance optimization strategies
Integration with other tools (xargs, ripgrep)
Advanced filtering and exclusion patterns
Skill Combinations
For Discovery Phase
fd → fzf: Interactive file selection with preview
fd → ripgrep: Search within specific file types
fd → jq/yq: Extract data from found config files
fd → extracting-code-structure: Get structure overview of found files
For Analysis Phase
fd → bat: View found files with syntax highlighting
fd → tokei: Get statistics for specific file sets
fd → jq/yq: Analyze configuration files in directory
For Refactoring Phase
fd → sd: Perform batch replacements across found files
fd → analyzing-code-structure: Apply structural changes to specific file types
fd → xargs: Execute commands on found files
Integration Examples
# Find and edit source files
fd -e py | fzf --multi --preview="bat --color=always {}" | xargs vim

# Find and replace in JavaScript files
fd -e js -x sd "oldPattern" "newPattern"

Weekly Installs
23
Repository
iota9star/my-skills
GitHub Stars
8
First Seen
Feb 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass