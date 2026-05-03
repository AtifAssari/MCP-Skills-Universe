---
rating: ⭐⭐
title: shell
url: https://skills.sh/pproenca/dot-skills/shell
---

# shell

skills/pproenca/dot-skills/shell
shell
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill shell
SKILL.md
Shell Scripts Best Practices (Community)

Comprehensive best practices guide for shell scripting, designed for AI agents and LLMs. Contains 49 rules across 9 categories, prioritized by impact from critical (safety, portability) to incremental (style). Each rule includes detailed explanations, real-world examples comparing incorrect vs. correct implementations, and specific impact metrics.

When to Apply

Reference these guidelines when:

Writing new bash or POSIX shell scripts
Reviewing shell scripts for security vulnerabilities
Debugging scripts that fail silently or behave unexpectedly
Porting scripts between Linux, macOS, and containers
Optimizing shell script performance
Setting up CI/CD pipelines with shell scripts
Rule Categories by Priority
Priority	Category	Impact	Prefix	Rules
1	Safety & Security	CRITICAL	safety-	6
2	Portability	CRITICAL	port-	5
3	Error Handling	HIGH	err-	8
4	Variables & Data	HIGH	var-	5
5	Quoting & Expansion	MEDIUM-HIGH	quote-	6
6	Functions & Structure	MEDIUM	func-	5
7	Testing & Conditionals	MEDIUM	test-	5
8	Performance	LOW-MEDIUM	perf-	6
9	Style & Formatting	LOW	style-	3
Quick Reference
1. Safety & Security (CRITICAL)
safety-command-injection - Prevent command injection from user input
safety-eval-avoidance - Avoid eval for dynamic commands
safety-absolute-paths - Use absolute paths for external commands
safety-temp-files - Create secure temporary files
safety-suid-forbidden - Never use SUID/SGID on shell scripts
safety-argument-injection - Prevent argument injection with double dash
2. Portability (CRITICAL)
port-shebang-selection - Choose shebang based on portability needs
port-avoid-bashisms - Avoid bashisms in POSIX scripts
port-printf-over-echo - Use printf instead of echo for portability
port-export-syntax - Use portable export syntax
port-test-portability - Use portable test constructs
3. Error Handling (HIGH)
err-strict-mode - Use strict mode for error detection
err-exit-codes - Use meaningful exit codes
err-trap-cleanup - Use trap for cleanup on exit
err-stderr-messages - Send error messages to stderr
err-pipefail - Use pipefail to catch pipeline errors
err-check-commands - Check command success explicitly
err-shellcheck - Use ShellCheck for static analysis
err-debug-tracing - Use debug tracing with set -x and PS4
4. Variables & Data (HIGH)
var-use-arrays - Use arrays for lists instead of strings
var-local-scope - Use local for function variables
var-naming-conventions - Follow variable naming conventions
var-readonly-constants - Use readonly for constants
var-default-values - Use parameter expansion for defaults
5. Quoting & Expansion (MEDIUM-HIGH)
quote-always-quote-variables - Always quote variable expansions
quote-dollar-at - Use "$@" for argument passing
quote-command-substitution - Quote command substitutions
quote-brace-expansion - Use braces for variable clarity
quote-here-documents - Use here documents for multi-line strings
quote-glob-safety - Control glob expansion explicitly
6. Functions & Structure (MEDIUM)
func-main-pattern - Use main() function pattern
func-single-purpose - Write single-purpose functions
func-return-values - Use return values correctly
func-documentation - Document functions with header comments
func-avoid-aliases - Prefer functions over aliases
7. Testing & Conditionals (MEDIUM)
test-double-brackets - Use [[ ]] for tests in bash
test-arithmetic - Use (( )) for arithmetic comparisons
test-explicit-empty - Use explicit empty/non-empty string tests
test-file-operators - Use correct file test operators
test-case-patterns - Use case for pattern matching
8. Performance (LOW-MEDIUM)
perf-builtins-over-external - Use builtins over external commands
perf-avoid-subshells - Avoid unnecessary subshells
perf-process-substitution - Use process substitution for temp files
perf-read-files - Read files efficiently
perf-parameter-expansion - Use parameter expansion for string operations
perf-batch-operations - Batch operations instead of loops
9. Style & Formatting (LOW)
style-indentation - Use consistent indentation
style-file-structure - Follow consistent file structure
style-comments - Write useful comments
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Key Sources
Google Shell Style Guide
ShellCheck
Greg's Wiki (wooledge.org)
POSIX Shell Specification
Weekly Installs
373
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