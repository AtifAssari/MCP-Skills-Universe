---
title: code-simplifier
url: https://skills.sh/pproenca/dot-skills/code-simplifier
---

# code-simplifier

skills/pproenca/dot-skills/code-simplifier
code-simplifier
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill code-simplifier
SKILL.md
Community Code Simplification Best Practices

Comprehensive code simplification guide for AI agents and LLMs. Contains 47 rules across 8 categories, prioritized by impact from critical (context discovery, behavior preservation) to incremental (language idioms). Each rule includes detailed explanations, real-world examples comparing incorrect vs. correct implementations, and specific impact metrics.

Core Principles
Context First: Understand project conventions before making any changes
Behavior Preservation: Change how code is written, never what it does
Scope Discipline: Focus on recently modified code, keep diffs small
Clarity Over Brevity: Explicit, readable code beats clever one-liners
When to Apply

Reference these guidelines when:

Simplifying or cleaning up recently modified code
Reducing nesting, complexity, or duplication
Improving naming and readability
Applying language-specific idiomatic patterns
Reviewing code for maintainability issues
Rule Categories by Priority
Priority	Category	Impact	Prefix	Rules
1	Context Discovery	CRITICAL	ctx-	4
2	Behavior Preservation	CRITICAL	behave-	6
3	Scope Management	HIGH	scope-	5
4	Control Flow Simplification	HIGH	flow-	9
5	Naming and Clarity	MEDIUM-HIGH	name-	6
6	Duplication Reduction	MEDIUM	dup-	5
7	Dead Code Elimination	MEDIUM	dead-	5
8	Language Idioms	LOW-MEDIUM	idiom-	7
Quick Reference
1. Context Discovery (CRITICAL)
ctx-read-claude-md - Always read CLAUDE.md before simplifying
ctx-detect-lint-config - Check for linting and formatting configs
ctx-follow-existing-patterns - Match existing code style in file and project
ctx-project-over-generic - Project conventions override generic best practices
2. Behavior Preservation (CRITICAL)
behave-preserve-outputs - Preserve all return values and outputs
behave-preserve-errors - Preserve error messages, types, and handling
behave-preserve-api - Preserve public function signatures and types
behave-preserve-side-effects - Preserve side effects (logging, I/O, state changes)
behave-no-semantics-change - Forbid subtle semantic changes
behave-verify-before-commit - Verify behavior preservation before finalizing
3. Scope Management (HIGH)
scope-recent-code-only - Focus on recently modified code only
scope-minimal-diff - Keep changes small and reviewable
scope-no-unrelated-refactors - No unrelated refactors
scope-no-global-rewrites - Avoid global rewrites and architectural changes
scope-respect-boundaries - Respect module and component boundaries
4. Control Flow Simplification (HIGH)
flow-early-return - Use early returns to reduce nesting
flow-guard-clauses - Use guard clauses for preconditions
flow-no-nested-ternaries - Never use nested ternary operators
flow-explicit-over-dense - Prefer explicit control flow over dense expressions
flow-flatten-nesting - Flatten deep nesting to maximum 2-3 levels
flow-single-responsibility - Each code block should do one thing
flow-positive-conditions - Prefer positive conditions over double negatives
flow-optional-chaining - Use optional chaining and nullish coalescing
flow-boolean-simplification - Simplify boolean expressions
5. Naming and Clarity (MEDIUM-HIGH)
name-intention-revealing - Use intention-revealing names
name-nouns-for-data - Use nouns for data, verbs for actions
name-avoid-abbreviations - Avoid cryptic abbreviations
name-consistent-vocabulary - Use consistent vocabulary throughout
name-avoid-generic - Avoid generic names
name-string-interpolation - Prefer string interpolation over concatenation
6. Duplication Reduction (MEDIUM)
dup-rule-of-three - Apply the rule of three
dup-no-single-use-helpers - Avoid single-use helper functions
dup-extract-for-clarity - Extract only when it improves clarity
dup-avoid-over-abstraction - Prefer duplication over premature abstraction
dup-data-driven - Use data-driven patterns over repetitive conditionals
7. Dead Code Elimination (MEDIUM)
dead-remove-unused - Delete unused code artifacts
dead-delete-not-comment - Delete code, never comment it out
dead-remove-obvious-comments - Remove comments that state the obvious
dead-keep-why-comments - Keep comments that explain why, not what
dead-remove-todo-fixme - Remove stale TODO/FIXME comments
8. Language Idioms (LOW-MEDIUM)
idiom-ts-strict-types - Use strict types over any (TypeScript)
idiom-ts-const-assertions - Use const assertions and readonly (TypeScript)
idiom-rust-question-mark - Use ? for error propagation (Rust)
idiom-rust-iterator-chains - Use iterator chains when clearer (Rust)
idiom-python-comprehensions - Use comprehensions for simple transforms (Python)
idiom-go-error-handling - Handle errors immediately (Go)
idiom-prefer-language-builtins - Prefer language and stdlib builtins
Workflow
Discover context: Read CLAUDE.md, lint configs, examine existing patterns
Identify scope: Focus on recently modified code unless asked to expand
Apply transformations: Use rules in priority order (CRITICAL first)
Verify behavior: Ensure outputs, errors, and side effects remain identical
Keep diffs minimal: Small, focused changes that are easy to review
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
331
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass