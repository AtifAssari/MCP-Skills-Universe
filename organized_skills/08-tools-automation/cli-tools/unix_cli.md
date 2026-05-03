---
rating: ⭐⭐
title: unix-cli
url: https://skills.sh/pproenca/dot-skills/unix-cli
---

# unix-cli

skills/pproenca/dot-skills/unix-cli
unix-cli
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill unix-cli
SKILL.md
UNIX/POSIX Standards CLI Best Practices

Comprehensive guidelines for building command-line tools that follow UNIX conventions, designed for AI agents and LLMs. Contains 44 rules across 8 categories, prioritized by impact from critical (argument handling, exit codes, output streams) to incremental (configuration and environment).

When to Apply

Reference these guidelines when:

Writing new CLI tools in any language
Parsing command-line arguments and flags
Deciding what goes to stdout vs stderr
Choosing appropriate exit codes
Handling signals like SIGINT and SIGTERM
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Argument & Flag Design	CRITICAL	args-
2	Exit Codes	CRITICAL	exit-
3	Output Streams	CRITICAL	output-
4	Error Handling	HIGH	error-
5	I/O & Composition	HIGH	io-
6	Help & Documentation	MEDIUM-HIGH	help-
7	Signals & Robustness	MEDIUM	signal-
8	Configuration & Environment	MEDIUM	config-
Quick Reference
1. Argument & Flag Design (CRITICAL)
args-use-getopt - Use standard argument parsing libraries
args-provide-long-options - Provide long options for all short options
args-support-double-dash - Support double-dash to terminate options
args-require-help-version - Implement --help and --version options
args-prefer-flags-over-positional - Prefer flags over positional arguments
args-use-standard-flag-names - Use standard flag names
args-never-read-secrets-from-flags - Never read secrets from command-line flags
args-support-option-bundling - Support option bundling
2. Exit Codes (CRITICAL)
exit-zero-for-success - Return zero for success only
exit-use-standard-codes - Use standard exit codes
exit-signal-codes - Use 128+N for signal termination
exit-partial-success - Handle partial success consistently
exit-distinguish-error-types - Distinguish error types with different exit codes
3. Output Streams (CRITICAL)
output-stdout-for-data - Write data to stdout only
output-stderr-for-errors - Write errors and diagnostics to stderr
output-detect-tty - Detect TTY for human-oriented output
output-provide-machine-format - Provide machine-readable output format
output-line-based-text - Use line-based output for text streams
output-respect-no-color - Respect NO_COLOR environment variable
4. Error Handling (HIGH)
error-include-program-name - Include program name in error messages
error-actionable-messages - Make error messages actionable
error-use-strerror - Use strerror for system errors
error-avoid-stack-traces - Avoid stack traces in user-facing errors
error-validate-early - Validate input early and fail fast
5. I/O & Composition (HIGH)
io-support-stdin - Support reading from stdin
io-write-to-stdout - Write output to stdout by default
io-be-stateless - Design stateless operations
io-handle-binary-safely - Handle binary data safely
io-atomic-writes - Use atomic file writes
io-handle-multiple-files - Handle multiple input files consistently
6. Help & Documentation (MEDIUM-HIGH)
help-show-usage-on-error - Show brief usage on argument errors
help-structure-help-output - Structure help output consistently
help-show-defaults - Show default values in help
help-include-examples - Include practical examples in help
help-version-format - Format version output correctly
7. Signals & Robustness (MEDIUM)
signal-handle-sigint - Handle SIGINT gracefully
signal-handle-sigterm - Handle SIGTERM for clean shutdown
signal-handle-sigpipe - Handle SIGPIPE for broken pipes
signal-cleanup-on-second-interrupt - Skip cleanup on second interrupt
8. Configuration & Environment (MEDIUM)
config-follow-xdg - Follow XDG Base Directory Specification
config-precedence-order - Apply configuration in correct precedence order
config-env-naming - Use consistent environment variable naming
config-never-store-secrets - Never store secrets in config files or environment
config-respect-standard-vars - Respect standard environment variables
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
158
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass