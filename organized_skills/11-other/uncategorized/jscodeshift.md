---
rating: ⭐⭐
title: jscodeshift
url: https://skills.sh/pproenca/dot-skills/jscodeshift
---

# jscodeshift

skills/pproenca/dot-skills/jscodeshift
jscodeshift
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill jscodeshift
SKILL.md
Facebook/Meta jscodeshift Best Practices

Comprehensive best practices guide for jscodeshift codemod development, designed for AI agents and LLMs. Contains 40 rules across 8 categories, prioritized by impact from critical (parser configuration, AST traversal) to incremental (advanced patterns). Each rule includes detailed explanations, real-world examples, and specific impact metrics.

When to Apply

Reference these guidelines when:

Writing new jscodeshift codemods for code migrations
Debugging transform failures or unexpected behavior
Optimizing codemod performance on large codebases
Reviewing codemod code for correctness
Testing codemods for edge cases and regressions
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Parser Configuration	CRITICAL	parser-
2	AST Traversal Patterns	CRITICAL	traverse-
3	Node Filtering	HIGH	filter-
4	AST Transformation	HIGH	transform-
5	Code Generation	MEDIUM	codegen-
6	Testing Strategies	MEDIUM	test-
7	Runner Optimization	LOW-MEDIUM	runner-
8	Advanced Patterns	LOW	advanced-
Quick Reference
1. Parser Configuration (CRITICAL)
parser-typescript-config - Use correct parser for TypeScript files
parser-flow-annotation - Use Flow parser for Flow-typed code
parser-babel5-compat - Avoid default babel5compat for modern syntax
parser-export-declaration - Export parser from transform module
parser-astexplorer-match - Match AST Explorer parser to jscodeshift parser
2. AST Traversal Patterns (CRITICAL)
traverse-find-specific-type - Use specific node types in find() calls
traverse-two-pass-pattern - Use two-pass pattern for complex transforms
traverse-early-return - Return early when no transformation needed
traverse-find-filter-pattern - Use find() with filter object over filter() chain
traverse-closest-scope - Use closestScope() for scope-aware transforms
traverse-avoid-repeated-find - Avoid repeated find() calls for same node type
3. Node Filtering (HIGH)
filter-path-parent-check - Check parent path before transformation
filter-import-binding - Track import bindings for accurate usage detection
filter-nullish-checks - Add nullish checks before property access
filter-jsx-context - Distinguish JSX context from regular JavaScript
filter-computed-properties - Handle computed property keys in filters
4. AST Transformation (HIGH)
transform-builder-api - Use builder API for creating AST nodes
transform-replacewith-callback - Use replaceWith callback for context-aware transforms
transform-insert-import - Insert imports at correct position
transform-preserve-comments - Preserve comments when replacing nodes
transform-renameto - Use renameTo for variable renaming
transform-remove-unused-imports - Remove unused imports after transformation
5. Code Generation (MEDIUM)
codegen-tosource-options - Configure toSource() for consistent formatting
codegen-preserve-style - Preserve original code style with recast
codegen-template-literals - Use template literals for complex node creation
codegen-print-width - Set appropriate print width for long lines
6. Testing Strategies (MEDIUM)
test-inline-snapshots - Use defineInlineTest for input/output verification
test-negative-cases - Write negative test cases first
test-dry-run-exploration - Use dry run mode for codebase exploration
test-fixture-files - Use fixture files for complex test cases
test-parse-errors - Test for parse error handling
7. Runner Optimization (LOW-MEDIUM)
runner-parallel-workers - Configure worker count for optimal parallelization
runner-ignore-patterns - Use ignore patterns to skip non-source files
runner-extensions-filter - Filter files by extension
runner-batch-processing - Process large codebases in batches
runner-verbose-output - Use verbose output for debugging transforms
8. Advanced Patterns (LOW)
advanced-compose-transforms - Compose multiple transforms into pipelines
advanced-scope-analysis - Use scope analysis for safe variable transforms
advanced-multi-file-state - Share state across files with options
advanced-custom-collections - Create custom collection methods
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For a single comprehensive document containing all rules, see AGENTS.md.

Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
161
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass