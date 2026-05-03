---
rating: ⭐⭐⭐
title: brewdoc:memory
url: https://skills.sh/kochetkov-ma/claude-brewcode/brewdoc:memory
---

# brewdoc:memory

skills/kochetkov-ma/claude-brewcode/brewdoc:memory
brewdoc:memory
Installation
$ npx skills add https://github.com/kochetkov-ma/claude-brewcode --skill brewdoc:memory
SKILL.md
Memory Optimizer

Optimizes Claude Code memory files through 4 interactive steps.

No context: fork — must run in main conversation to spawn agents.

Phase 0: Load Context

Determine memory directory ($MEMORY_DIR):

CUSTOM_DIR=$(cat .claude/settings.json 2>/dev/null | jq -r '.autoMemoryDirectory // empty')
if [ -n "$CUSTOM_DIR" ]; then
  MEMORY_DIR="$(git rev-parse --show-toplevel)/$CUSTOM_DIR"
else
  MEMORY_DIR=~/.claude/projects/<hash>/memory
fi


Read .claude/settings.json (if exists) → extract autoMemoryDirectory. If set → resolve as <git-root>/<autoMemoryDirectory>. If not set → use legacy ~/.claude/projects/<hash>/memory/ glob pattern.

Glob all memory files: $MEMORY_DIR/*.md (or ~/.claude/projects/**/memory/*.md for legacy)

Read ~/.claude/CLAUDE.md and project CLAUDE.md (if exists)

Glob .claude/rules/*.md — read all project rules

Read ~/.claude/rules/*.md — read all global rules

Build context map:

memory_dir: $MEMORY_DIR
memory_files: [paths]
claude_md_sections: [sections]
rules_files: [paths with content]

Step 1: Analysis — Remove Duplicates (Interactive)

Goal: Find memory entries that duplicate content already in CLAUDE.md or rules.

Spawn Explore agent to cross-reference all loaded files
Identify entries where:
Same rule already in CLAUDE.md
Same pattern already in a rules file
Contradicts CLAUDE.md (CLAUDE.md wins)
Show analysis:
Found X duplicate/redundant entries (Y% of memory):
| Entry | Memory File | Already In | Action |
|-------|-------------|------------|--------|
| "Use grepai first" | MEMORY.md:5 | rules/grepai-first.md | DELETE |
...

AskUserQuestion: "Delete X duplicate entries (Y% of memory)? This is safe — content exists elsewhere."
Options: "Yes, delete all" / "Review each" / "Skip this step"
Apply deletion using Edit tool if approved
Step 2: Migration — Move to Rules/CLAUDE.md (Interactive)

Goal: Identify remaining memory entries better suited to persistent config files.

Decision tree (per entry):

Applies to ALL projects + IS a rule/constraint → ~/.claude/rules/
Applies to THIS project only + IS a rule → .claude/rules/
IS an architectural decision → project CLAUDE.md
IS a fact/pattern reusable across sessions → KEEP in memory
Show categorization:
X entries suitable for migration:
| Entry | Current Location | Target | Reduction |
|-------|-----------------|--------|-----------|
| "Always use BD_PLUGIN_ROOT" | MEMORY.md:12 | .claude/rules/brewdoc.md | 15 tokens |
...
Total: X entries → ~Y tokens saved

AskUserQuestion: "Migrate X entries to rules/CLAUDE.md?"
Options: "Yes, migrate all" / "Review each" / "Skip this step"
If approved:
Create/append to target rule files via Edit
Remove migrated entries from memory via Edit
If target file doesn't exist, create it
Step 3: Compression (Interactive)

Goal: Compress remaining entries using LLM-efficient formatting.

Compression techniques:

Prose → table row
Multiple related entries → single table
Verbose description → imperative one-liner
List of examples → pattern + one example
Show compression preview:
Compression opportunities found:
| Before | After | Savings |
|--------|-------|---------|
| "When you need to... always use..." | "Use X for Y" | 8 tokens |
...
Total: ~Y% token reduction (~Z tokens)

Show 2-3 specific before/after samples.
AskUserQuestion: "Compress remaining memory? (~Y% reduction)"
Options: "Yes, compress all" / "Skip compression"
Apply compression via Edit (bottom-up order to preserve line numbers)
Step 4: Validation (Automatic)

Goal: Verify final state and clean orphaned references.

Spawn reviewer agent to verify:
No broken file path references in memory files
No contradictions between memory and CLAUDE.md
Memory files are well-formed markdown
Clean broken references (Edit tool)
Check for orphaned memory files (files in $MEMORY_DIR with no MEMORY.md reference)
Report orphaned files and ask to delete

Final Report:

## Memory Optimization Complete

### Summary
| Metric | Before | After | Saved |
|--------|--------|-------|-------|
| Total entries | X | Y | Z |
| Duplicate entries | X | 0 | — |
| Migrated entries | — | — | X |
| Token estimate | ~X | ~Y | ~Z (~P%) |

### Changes Made
- Step 1: Deleted X duplicate entries
- Step 2: Migrated X entries to rules/CLAUDE.md
- Step 3: Compressed X entries (Y% reduction)
- Step 4: Fixed X broken references, removed X orphaned files

### Final Memory Structure
{directory listing of $MEMORY_DIR}

Weekly Installs
14
Repository
kochetkov-ma/cl…brewcode
GitHub Stars
25
First Seen
Mar 2, 2026