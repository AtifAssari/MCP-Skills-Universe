---
title: ast-grep
url: https://skills.sh/pproenca/dot-skills/ast-grep
---

# ast-grep

skills/pproenca/dot-skills/ast-grep
ast-grep
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill ast-grep
SKILL.md
ast-grep Community Best Practices

Comprehensive best practices guide for ast-grep rule writing and usage, maintained by the ast-grep community. Contains 46 rules across 8 categories, prioritized by impact to guide automated rule generation and code transformation.

When to Apply

Reference these guidelines when:

Writing new ast-grep rules for linting or search
Debugging patterns that don't match expected code
Optimizing rule performance for large codebases
Setting up ast-grep projects with proper organization
Reviewing ast-grep rules for correctness and maintainability
General Workflow

Follow this workflow when creating ast-grep rules for code search:

Step 1: Understand the Query

Clarify what you want to find:

Target programming language
Edge cases to handle
What to include vs exclude
Step 2: Create Example Code

Write a sample code snippet representing the desired match pattern.

Step 3: Write the ast-grep Rule

Choose the right approach:

Use pattern for simple structures
Use kind with has/inside for complex structures
Combine with all, any, or not for compound queries
Always use stopBy: end for relational rules (inside, has) to ensure complete search
Step 4: Test the Rule
# Inspect AST structure
ast-grep run --pattern '[code]' --lang [language] --debug-query=ast

# Test inline rule
echo "[code]" | ast-grep scan --inline-rules "[rule]" --stdin

# Test from file
ast-grep scan --rule [file.yml] [path]

Step 5: Search the Codebase

Deploy the validated rule:

# Search with pattern (simple matches)
ast-grep run --pattern '[pattern]' --lang [language] [path]

# Search with rule file (complex queries)
ast-grep scan --rule [file.yml] [path]

# Apply fixes interactively
ast-grep scan --rule [file.yml] --interactive [path]

Quick Tips
Always use stopBy: end - Ensures complete subtree traversal for relational rules
Start simple, add complexity - Begin with patterns, progress to kinds, then relational rules
Debug with AST inspection - Use --debug-query=ast to verify structure matching
Escape in inline rules - Use \$VAR or single quotes for shell commands
Test in playground first - Use https://ast-grep.github.io/playground.html for rapid iteration
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Pattern Correctness	CRITICAL	pattern-
2	Meta Variable Usage	CRITICAL	meta-
3	Rule Composition	HIGH	compose-
4	Constraint Design	HIGH	const-
5	Rewrite Correctness	MEDIUM-HIGH	rewrite-
6	Project Organization	MEDIUM	org-
7	Performance Optimization	MEDIUM	perf-
8	Testing & Debugging	LOW-MEDIUM	test-
Quick Reference
1. Pattern Correctness (CRITICAL)
pattern-valid-syntax - Use valid parseable code as patterns
pattern-language-aware - Account for language-specific syntax differences
pattern-context-selector - Use context and selector for code fragments
pattern-avoid-comments-strings - Avoid matching inside comments and strings
pattern-strictness-levels - Configure pattern strictness appropriately
pattern-kind-vs-pattern - Choose kind or pattern based on specificity needs
pattern-debug-ast - Use debug query to inspect AST structure
pattern-nthchild-matching - Use nthChild for index-based positional matching
pattern-range-matching - Use range for character position matching
2. Meta Variable Usage (CRITICAL)
meta-naming-convention - Follow meta variable naming conventions
meta-single-node - Match single AST nodes with meta variables
meta-reuse-binding - Reuse meta variables to enforce equality
meta-underscore-noncapture - Use underscore prefix for non-capturing matches
meta-named-vs-unnamed - Use double dollar for unnamed node matching
meta-multi-match-lazy - Understand multi-match variables are lazy
3. Rule Composition (HIGH)
compose-all-for-and-logic - Use all for AND logic between rules
compose-any-for-or-logic - Use any for OR logic between rules
compose-not-for-exclusion - Use not for exclusion patterns
compose-inside-for-context - Use inside for contextual matching
compose-has-for-children - Use has for child node requirements
compose-matches-for-reuse - Use matches for rule reusability
compose-precedes-follows - Use precedes and follows for sequential positioning
compose-field-targeting - Use field to target specific sub-nodes
4. Constraint Design (HIGH)
const-kind-filter - Use kind constraints to filter meta variables
const-regex-filter - Use regex constraints for text patterns
const-not-inside-not - Avoid constraints inside not rules
const-pattern-constraint - Use pattern constraints for structural filtering
const-post-match-timing - Understand constraints apply after matching
5. Rewrite Correctness (MEDIUM-HIGH)
rewrite-preserve-semantics - Preserve program semantics in rewrites
rewrite-meta-variable-reference - Reference all necessary meta variables in fix
rewrite-transform-operations - Use transform for complex rewrites
rewrite-test-before-deploy - Test rewrites on representative code
rewrite-syntax-validity - Ensure fix templates produce valid syntax
6. Project Organization (MEDIUM)
org-project-structure - Use standard project directory structure
org-unique-rule-ids - Use unique descriptive rule IDs
org-severity-levels - Assign appropriate severity levels
org-file-filtering - Use file filtering for targeted rules
org-message-clarity - Write clear actionable messages
7. Performance Optimization (MEDIUM)
perf-specific-patterns - Use specific patterns over generic ones
perf-stopby-boundaries - Use stopBy to limit search depth
perf-thread-parallelism - Leverage parallel scanning with threads
perf-avoid-regex-heavy - Avoid heavy regex in hot paths
8. Testing & Debugging (LOW-MEDIUM)
test-valid-invalid-cases - Write both valid and invalid test cases
test-snapshot-updates - Use snapshot testing for fix verification
test-playground-first - Test patterns in playground first
test-edge-cases - Test edge cases and boundary conditions
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document
AGENTS.md - Complete compiled guide with all rules
Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
150
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass