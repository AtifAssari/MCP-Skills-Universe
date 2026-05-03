---
title: file-operations
url: https://skills.sh/mhattingpete/claude-skills-marketplace/file-operations
---

# file-operations

skills/mhattingpete/claude-skills-marketplace/file-operations
file-operations
Installation
$ npx skills add https://github.com/mhattingpete/claude-skills-marketplace --skill file-operations
SKILL.md
File Operations

Analyze files and retrieve metadata using Claude's native tools without modifying files.

When to Use
"analyze [file]"
"get file info for [file]"
"how many lines in [file]"
"compare [file1] and [file2]"
"file statistics"
Core Operations
File Size & Metadata
stat -f "%z bytes, modified %Sm" [file_path]  # Single file
ls -lh [directory]                             # Multiple files
du -h [file_path]                              # Human-readable size

Line Counts
wc -l [file_path]                              # Single file
wc -l [file1] [file2]                          # Multiple files
find [dir] -name "*.py" | xargs wc -l          # Directory total

Content Analysis

Use Read to analyze structure, then count functions/classes/imports.

Pattern Search
Grep(pattern="^def ", output_mode="count", path="src/")        # Count functions
Grep(pattern="TODO|FIXME", output_mode="content", -n=true)    # Find TODOs
Grep(pattern="^import ", output_mode="count")                 # Count imports

Find Files
Glob(pattern="**/*.py")

Workflow Examples
Comprehensive File Analysis
Get size/mod time: stat -f "%z bytes, modified %Sm" file.py
Count lines: wc -l file.py
Read file: Read(file_path="file.py")
Count functions: Grep(pattern="^def ", output_mode="count")
Count classes: Grep(pattern="^class ", output_mode="count")
Compare File Sizes
Find files: Glob(pattern="src/**/*.py")
Get sizes: ls -lh src/**/*.py
Total size: du -sh src/*.py
Code Quality Metrics
Total lines: find . -name "*.py" | xargs wc -l
Test files: find . -name "test_*.py" | wc -l
TODOs: Grep(pattern="TODO|FIXME|HACK", output_mode="count")
Find Largest Files
find . -type f -not -path "./node_modules/*" -exec du -h {} + | sort -rh | head -20

Best Practices
Non-destructive: Use Read/stat/wc, never modify
Efficient: Read small files fully, use Grep for large files
Context-aware: Compare to project averages, suggest optimizations
Integration

Works with:

code-auditor: Comprehensive analysis
code-transfer: After identifying large files
codebase-documenter: Understanding file purposes
Weekly Installs
269
Repository
mhattingpete/cl…ketplace
GitHub Stars
563
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass