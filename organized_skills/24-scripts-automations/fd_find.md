---
rating: ⭐⭐⭐
title: fd-find
url: https://skills.sh/site/skills.volces.com/fd-find
---

# fd-find

skills/skills.volces.com/fd-find
fd-find
$ npx skills add https://skills.volces.com/skills/clawhub/arnarsson
SKILL.md
fd - Fast File Finder

User-friendly alternative to find with smart defaults.

Quick Start
Basic search
# Find files by name
fd pattern

# Find in specific directory
fd pattern /path/to/dir

# Case-insensitive
fd -i pattern

Common patterns
# Find all Python files
fd -e py

# Find multiple extensions
fd -e py -e js -e ts

# Find directories only
fd -t d pattern

# Find files only
fd -t f pattern

# Find symlinks
fd -t l

Advanced Usage
Filtering
# Exclude patterns
fd pattern -E "node_modules" -E "*.min.js"

# Include hidden files
fd -H pattern

# Include ignored files (.gitignore)
fd -I pattern

# Search all (hidden + ignored)
fd -H -I pattern

# Maximum depth
fd pattern -d 3

Execution
# Execute command on results
fd -e jpg -x convert {} {.}.png

# Parallel execution
fd -e md -x wc -l

# Use with xargs
fd -e log -0 | xargs -0 rm

Regex patterns
# Full regex search
fd '^test.*\.js$'

# Match full path
fd --full-path 'src/.*/test'

# Glob pattern
fd -g "*.{js,ts}"

Time-based filtering
# Modified within last day
fd --changed-within 1d

# Modified before specific date
fd --changed-before 2024-01-01

# Created recently
fd --changed-within 1h

Size filtering
# Files larger than 10MB
fd --size +10m

# Files smaller than 1KB
fd --size -1k

# Specific size range
fd --size +100k --size -10m

Output formatting
# Absolute paths
fd --absolute-path

# List format (like ls -l)
fd --list-details

# Null separator (for xargs)
fd -0 pattern

# Color always/never/auto
fd --color always pattern

Common Use Cases

Find and delete old files:

fd --changed-before 30d -t f -x rm {}


Find large files:

fd --size +100m --list-details


Copy all PDFs to directory:

fd -e pdf -x cp {} /target/dir/


Count lines in all Python files:

fd -e py -x wc -l | awk '{sum+=$1} END {print sum}'


Find broken symlinks:

fd -t l -x test -e {} \; -print


Search in specific time window:

fd --changed-within 2d --changed-before 1d

Integration with other tools

With ripgrep:

fd -e js | xargs rg "pattern"


With fzf (fuzzy finder):

vim $(fd -t f | fzf)


With bat (cat alternative):

fd -e md | xargs bat

Performance Tips
fd is typically much faster than find
Respects .gitignore by default (disable with -I)
Uses parallel traversal automatically
Smart case: lowercase = case-insensitive, any uppercase = case-sensitive
Tips
Use -t for type filtering (f=file, d=directory, l=symlink, x=executable)
-e for extension is simpler than -g "*.ext"
{} in -x commands represents the found path
{.} strips the extension
{/} gets basename, {//} gets directory
Documentation

GitHub: https://github.com/sharkdp/fd Man page: man fd

Weekly Installs
22
Source
skills.volces.c…rnarsson
First Seen
Mar 19, 2026