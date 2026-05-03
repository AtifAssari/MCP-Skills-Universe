---
rating: ⭐⭐⭐
title: advanced_tools
url: https://skills.sh/tao3k/omni-dev-fusion/advanced_tools
---

# advanced_tools

skills/tao3k/omni-dev-fusion/advanced_tools
advanced_tools
Installation
$ npx skills add https://github.com/tao3k/omni-dev-fusion --skill advanced_tools
SKILL.md
Advanced Tools Skill (Batch Replace, Smart Search, Smart Find)

You have loaded the Advanced Tools (Find & Search) Skill.

The Search Engine of Agentic OS

This skill is the PRIMARY gateway for locating anything in the project. It wraps high-performance Rust tools.

Category	Tool	Implementation	Best For
Locator	smart_find	fd-find	Finding FILES by name/path
Searcher	smart_search	ripgrep	Finding TEXT inside files
Refactor	batch_replace	Rust/Python	Multi-file search and replace
Available Tools
smart_find: Fast File Location

ALWAYS use this to find files. Superior to ls or list_directory for discovery.

def smart_find(
    pattern: str = ".",      # Regex or glob for filename
    extension: str = None,   # Filter: 'py', 'rs', 'md'
    exclude: str = None,     # Patterns to ignore
    search_mode: str = "filename" # "filename" (fd) or "content" (rg -l)
) -> dict

smart_search: Fast Code Search

ALWAYS use this to find code content. The gold standard for grep.

def smart_search(
    pattern: str,            # Text or regex to find (REQUIRED)
    file_globs: str = None,  # Filter: "*.py *.ts"
    case_sensitive: bool = True,
    context_lines: int = 0
) -> dict

batch_replace: Safe Refactoring

RECOMMENDED for mass changes. Always includes a dry-run preview.

def batch_replace(
    pattern: str,            # Find this
    replacement: str,        # Replace with this
    file_glob: str = "**/*",
    dry_run: bool = True     # Default is PREVIEW for safety
) -> dict

Batch Replace Command (Primary Query Anchor)

batch replace is the canonical query phrase for this tool in documentation and routing. Use batch_replace when you need deterministic multi-file replacement with dry-run safety.

Linked Notes
Related: Code Tools Skill
Related: Skill Routing Value Standard
Use Cases & Intention
"Find all python files" -> smart_find(extension="py")
"Where is the Kernel defined?" -> smart_search(pattern="class Kernel")
"Find files containing API_KEY" -> smart_find(pattern="API_KEY", search_mode="content")
"Rename variable 'old_name' to 'new_name'" -> batch_replace(...)
Important Rules
Discovery First: If you don't know where a file is, use smart_find.
Context Matters: Use smart_search with context_lines to understand match surroundings.
Respect Ignored: All tools automatically respect .gitignore.
Prefer Patterns: Use specific regex patterns to reduce noise.
Weekly Installs
15
Repository
tao3k/omni-dev-fusion
GitHub Stars
9
First Seen
Jan 24, 2026