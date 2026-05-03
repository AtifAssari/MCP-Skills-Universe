---
rating: ⭐⭐⭐
title: go-code-review
url: https://skills.sh/cxuu/golang-skills/go-code-review
---

# go-code-review

skills/cxuu/golang-skills/go-code-review
go-code-review
Installation
$ npx skills add https://github.com/cxuu/golang-skills --skill go-code-review
Summary

Systematic Go code review against community style standards and best practices.

Covers 15+ review categories: formatting, documentation, error handling, naming, concurrency, interfaces, data structures, security, declarations, functions, style, logging, imports, generics, and testing
Includes automated pre-review checks via gofmt, go vet, and golangci-lint to catch mechanical issues before manual review
Organizes findings by severity (must-fix, should-fix, nit) using a consistent template for clear communication
References specialized skills for deeper dives into error handling, naming conventions, concurrency patterns, and testing strategies
SKILL.md
Go Code Review Checklist
Review Procedure

Use assets/review-template.md when formatting the output of a code review to ensure consistent structure with Must Fix / Should Fix / Nits severity grouping.

Run gofmt -d . and go vet ./... to catch mechanical issues first
Read the diff file-by-file; for each file, check the categories below in order
Flag issues with specific line references and the rule name
After reviewing all files, re-read flagged items to verify they're genuine issues
Summarize findings grouped by severity (must-fix, should-fix, nit)

Validation: After completing the review, re-read the diff once more to verify every flagged issue is real. Remove any finding you cannot justify with a specific line reference.

Formatting
 gofmt: Code is formatted with gofmt or goimports → go-linting
Documentation
 Comment sentences: Comments are full sentences starting with the name being described, ending with a period → go-documentation
 Doc comments: All exported names have doc comments; non-trivial unexported declarations too → go-documentation
 Package comments: Package comment appears adjacent to package clause with no blank line → go-documentation
 Named result parameters: Only used when they clarify meaning (e.g., multiple same-type returns), not just to enable naked returns → go-documentation
Error Handling
 Handle errors: No discarded errors with _; handle, return, or (exceptionally) panic → go-error-handling
 Error strings: Lowercase, no punctuation (unless starting with proper noun/acronym) → go-error-handling
 In-band errors: No magic values (-1, "", nil); use multiple returns with error or ok bool → go-error-handling
 Indent error flow: Handle errors first and return; keep normal path at minimal indentation → go-error-handling
Naming
 MixedCaps: Use MixedCaps or mixedCaps, never underscores; unexported is maxLength not MAX_LENGTH → go-naming
 Initialisms: Keep consistent case: URL/url, ID/id, HTTP/http (e.g., ServeHTTP, xmlHTTPRequest) → go-naming
 Variable names: Short names for limited scope (i, r, c); longer names for wider scope → go-naming
 Receiver names: One or two letter abbreviation of type (c for Client); no this, self, me; consistent across methods → go-naming
 Package names: No stuttering (use chubby.File not chubby.ChubbyFile); avoid util, common, misc → go-packages
 Avoid built-in names: Don't shadow error, string, len, cap, append, copy, new, make → go-declarations
Concurrency
 Goroutine lifetimes: Clear when/whether goroutines exit; document if not obvious → go-concurrency
 Synchronous functions: Prefer sync over async; let callers add concurrency if needed → go-concurrency
 Contexts: First parameter; not in structs; no custom Context types; pass even if you think you don't need to → go-context
Interfaces
 Interface location: Define in consumer package, not implementor; return concrete types from producers → go-interfaces
 No premature interfaces: Don't define before used; don't define "for mocking" on implementor side → go-interfaces
 Receiver type: Use pointer if mutating, has sync fields, or is large; value for small immutable types; don't mix → go-interfaces
Data Structures
 Empty slices: Prefer var t []string (nil) over t := []string{} (non-nil zero-length) → go-data-structures
 Copying: Be careful copying structs with pointer/slice fields; don't copy *T methods' receivers by value → go-data-structures
Security
 Crypto rand: Use crypto/rand for keys, not math/rand → go-defensive
 Don't panic: Use error returns for normal error handling; panic only for truly exceptional cases → go-defensive
Declarations and Initialization
 Group similar: Related var/const/type in parenthesized blocks; separate unrelated → go-declarations
 var vs :=: Use var for intentional zero values; := for explicit assignments → go-declarations
 Reduce scope: Move declarations close to usage; use if-init to limit variable scope → go-declarations
 Struct init: Always use field names; omit zero fields; var for zero structs → go-declarations
 Use any: Prefer any over interface{} in new code → go-declarations
Functions
 File ordering: Types → constructors → exported methods → unexported → utilities → go-functions
 Signature formatting: All args on own lines with trailing comma when wrapping → go-functions
 Naked parameters: Add /* name */ comments for ambiguous bool/int args, or use custom types → go-functions
 Printf naming: Functions accepting format strings end in f for go vet → go-functions
Style
 Line length: No rigid limit, but avoid uncomfortably long lines; break by semantics, not arbitrary length → go-style-core
 Naked returns: Only in short functions; explicit returns in medium/large functions → go-style-core
 Pass values: Don't use pointers just to save bytes; pass string not *string for small fixed-size types → go-performance
 String concatenation: + for simple; fmt.Sprintf for formatting; strings.Builder for loops → go-performance
Logging
 Use slog: New code uses log/slog, not log or fmt.Println for operational logging → go-logging
 Structured fields: Log messages use static strings with key-value attributes, not fmt.Sprintf → go-logging
 Appropriate levels: Debug for developer tracing, Info for notable events, Warn for recoverable issues, Error for failures → go-logging
 No secrets in logs: PII, credentials, and tokens are never logged → go-logging
Imports
 Import groups: Standard library first, then blank line, then external packages → go-packages
 Import renaming: Avoid unless collision; rename local/project-specific import on collision → go-packages
 Import blank: import _ "pkg" only in main package or tests → go-packages
 Import dot: Only for circular dependency workarounds in tests → go-packages
Generics
 When to use: Only when multiple types share identical logic and interfaces don't suffice → go-generics
 Type aliases: Use definitions for new types; aliases only for package migration → go-generics
Testing
 Examples: Include runnable Example functions or tests demonstrating usage → go-documentation
 Useful test failures: Messages include what was wrong, inputs, got, and want; order is got != want → go-testing
 TestMain: Use only when all tests need common setup with teardown; prefer scoped helpers first → go-testing
 Real transports: Prefer httptest.NewServer + real client over mocking HTTP → go-testing
Automated Checks

Run automated pre-review checks:

bash scripts/pre-review.sh ./...         # text output
bash scripts/pre-review.sh --json ./...  # structured JSON output


Or manually: gofmt -l <path> && go vet ./... && golangci-lint run ./...

Fix any issues before proceeding to the checklist above. For linter setup and configuration, see go-linting.

Integrative Example

Read references/WEB-SERVER.md when building a production HTTP server and want to verify your code applies concurrency, error handling, context, documentation, and naming conventions together.

Related Skills
Style foundations: See go-style-core when resolving formatting debates or applying the clarity > simplicity > concision priority
Linting setup: See go-linting when configuring golangci-lint or adding automated checks to CI
Error strategy: See go-error-handling when reviewing error wrapping, sentinel errors, or the handle-once pattern
Naming conventions: See go-naming when evaluating identifier names, receiver names, or package-symbol stuttering
Testing patterns: See go-testing when reviewing test code for table-driven structure, failure messages, or helper usage
Concurrency safety: See go-concurrency when reviewing goroutine lifetimes, channel usage, or mutex placement
Logging practices: See go-logging when reviewing log usage, structured logging, or slog configuration
Weekly Installs
677
Repository
cxuu/golang-skills
GitHub Stars
82
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass