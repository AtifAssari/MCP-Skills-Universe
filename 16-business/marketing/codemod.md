---
title: codemod
url: https://skills.sh/pproenca/dot-skills/codemod
---

# codemod

skills/pproenca/dot-skills/codemod
codemod
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill codemod
SKILL.md
Codemod Best Practices

Comprehensive best practices guide for Codemod (JSSG, ast-grep, workflows), designed for AI agents and LLMs. Contains 48 rules across 11 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new codemods with JSSG or ast-grep
Designing workflow configurations for migrations
Debugging pattern matching or AST traversal issues
Reviewing codemod code for performance and safety
Setting up test fixtures for transform validation
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	AST Understanding	CRITICAL	ast-
2	Pattern Efficiency	CRITICAL	pattern-
3	Parsing Strategy	CRITICAL	parse-
4	Node Traversal	HIGH	traverse-
5	Semantic Analysis	HIGH	semantic-
6	Edit Operations	MEDIUM-HIGH	edit-
7	Workflow Design	MEDIUM-HIGH	workflow-
8	Testing Strategy	MEDIUM	test-
9	State Management	MEDIUM	state-
10	Security and Capabilities	LOW-MEDIUM	security-
11	Package Structure	LOW	pkg-
Quick Reference
1. AST Understanding (CRITICAL)
ast-explore-before-writing - Use AST Explorer before writing patterns
ast-understand-named-vs-anonymous - Understand named vs anonymous nodes
ast-use-kind-for-precision - Use kind constraint for precision
ast-field-access-for-structure - Use field access for structural queries
ast-check-null-before-access - Check null before property access
2. Pattern Efficiency (CRITICAL)
pattern-use-meta-variables - Use meta variables for flexible matching
pattern-avoid-overly-generic - Avoid overly generic patterns
pattern-combine-with-rules - Combine patterns with rule operators
pattern-use-constraints - Use constraints for reusable matching logic
pattern-use-relational-patterns - Use relational patterns for context
pattern-ensure-idempotency - Ensure patterns are idempotent
3. Parsing Strategy (CRITICAL)
parse-select-correct-parser - Select the correct parser for file type
parse-handle-embedded-languages - Handle embedded languages with parseAsync
parse-provide-pattern-context - Provide context for ambiguous patterns
parse-early-return-non-applicable - Early return for non-applicable files
4. Node Traversal (HIGH)
traverse-use-find-vs-findall - Use find() for single match, findAll() for multiple
traverse-single-pass-collection - Collect multiple patterns in single traversal
traverse-use-stopby-for-depth - Use stopBy to control traversal depth
traverse-use-siblings-efficiently - Use sibling navigation efficiently
traverse-cache-repeated-lookups - Cache repeated node lookups
5. Semantic Analysis (HIGH)
semantic-use-file-scope-first - Use file scope semantic analysis first
semantic-check-null-results - Handle null semantic analysis results
semantic-verify-file-ownership - Verify file ownership before cross-file edits
semantic-cache-cross-file-results - Cache semantic analysis results
6. Edit Operations (MEDIUM-HIGH)
edit-batch-before-commit - Batch edits before committing
edit-preserve-formatting - Preserve surrounding formatting in edits
edit-handle-overlapping-ranges - Handle overlapping edit ranges
edit-use-flatmap-for-conditional - Use flatMap for conditional edits
edit-add-imports-correctly - Add imports at correct position
7. Workflow Design (MEDIUM-HIGH)
workflow-order-nodes-by-dependency - Order nodes by dependency
workflow-use-matrix-for-parallelism - Use matrix strategy for parallelism
workflow-use-manual-gates - Use manual gates for critical steps
workflow-validate-before-run - Validate workflows before running
workflow-use-conditional-steps - Use conditional steps for dynamic workflows
8. Testing Strategy (MEDIUM)
test-use-fixture-pairs - Use input/expected fixture pairs
test-cover-edge-cases - Cover edge cases in test fixtures
test-use-strictness-levels - Choose appropriate test strictness level
test-update-fixtures-intentionally - Update test fixtures intentionally
test-run-on-subset-first - Test on file subset before full run
9. State Management (MEDIUM)
state-use-for-resumability - Use state for resumable migrations
state-make-transforms-idempotent - Make transforms idempotent for safe reruns
state-log-progress-for-observability - Log progress for long-running migrations
10. Security and Capabilities (LOW-MEDIUM)
security-minimize-capabilities - Minimize requested capabilities
security-validate-external-inputs - Validate external inputs before use
security-review-before-running-third-party - Review third-party codemods before running
11. Package Structure (LOW)
pkg-use-semantic-versioning - Use semantic versioning for packages
pkg-write-descriptive-metadata - Write descriptive package metadata
pkg-organize-by-convention - Organize package by convention
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For a complete guide with all rules expanded, see AGENTS.md.

Weekly Installs
177
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