---
title: clean-code
url: https://skills.sh/pproenca/dot-skills/clean-code
---

# clean-code

skills/pproenca/dot-skills/clean-code
clean-code
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill clean-code
SKILL.md
Robert C. Martin (Uncle Bob) Clean Code Best Practices

Comprehensive software craftsmanship guide based on Robert C. Martin's "Clean Code: A Handbook of Agile Software Craftsmanship", updated with modern corrections where the original 2008 advice has been superseded. Contains 48 rules across 10 categories, prioritized by impact to guide code reviews, refactoring decisions, and new development. Examples are primarily in Java but principles are language-agnostic.

When to Apply

Reference these guidelines when:

Writing new functions, classes, or modules
Naming variables, functions, classes, or files
Reviewing code for maintainability issues
Refactoring existing code to improve clarity
Writing or improving unit tests
Wrapping third-party dependencies
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Meaningful Names	CRITICAL	name-
2	Functions	CRITICAL	func-
3	Comments	HIGH	cmt-
4	Formatting	HIGH	fmt-
5	Error Handling	HIGH	err-
6	Objects and Data Structures	MEDIUM-HIGH	obj-
7	Boundaries	MEDIUM-HIGH	bound-
8	Classes and Systems	MEDIUM-HIGH	class-
9	Unit Tests	MEDIUM	test-
10	Emergence and Simple Design	MEDIUM	emerge-
Quick Reference
1. Meaningful Names (CRITICAL)
name-intention-revealing - Use names that reveal intent
name-avoid-disinformation - Avoid misleading names
name-meaningful-distinctions - Make meaningful distinctions
name-pronounceable - Use pronounceable names
name-searchable - Use searchable names
name-avoid-encodings - Avoid encodings in names
name-class-noun - Use noun phrases for class names
name-method-verb - Use verb phrases for method names
2. Functions (CRITICAL)
func-small - Keep functions small
func-one-thing - Functions should do one thing
func-abstraction-level - Maintain one level of abstraction
func-minimize-arguments - Minimize function arguments
func-no-side-effects - Avoid side effects
func-command-query-separation - Separate commands from queries
func-dry - Do not repeat yourself
3. Comments (HIGH)
cmt-express-in-code - Express yourself in code, not comments
cmt-explain-intent - Use comments to explain intent
cmt-avoid-redundant - Avoid redundant comments
cmt-avoid-commented-out-code - Delete commented-out code
cmt-warning-consequences - Use warning comments for consequences
4. Formatting (HIGH)
fmt-vertical-formatting - Use vertical formatting for readability
fmt-horizontal-alignment - Avoid horizontal alignment
fmt-team-rules - Follow team formatting rules
fmt-indentation - Respect indentation rules
5. Error Handling (HIGH)
err-use-exceptions - Separate error handling from happy path
err-write-try-catch-first - Write try-catch-finally first
err-provide-context - Provide context with exceptions
err-define-by-caller-needs - Define exceptions by caller needs
err-avoid-null - Avoid returning and passing null
6. Objects and Data Structures (MEDIUM-HIGH)
obj-data-abstraction - Hide data behind abstractions
obj-data-object-asymmetry - Understand data/object anti-symmetry
obj-law-of-demeter - Follow the Law of Demeter
obj-avoid-hybrids - Avoid hybrid data-object structures
obj-dto - Use DTOs for data transfer
7. Boundaries (MEDIUM-HIGH)
bound-wrap-third-party - Wrap third-party APIs
bound-learning-tests - Write learning tests for third-party code
8. Classes and Systems (MEDIUM-HIGH)
class-small - Keep classes small
class-cohesion - Maintain class cohesion
class-organize-for-change - Organize classes for change
class-isolate-from-change - Isolate classes from change
class-separate-concerns - Separate construction from use
9. Unit Tests (MEDIUM)
test-first-law - Follow the three laws of TDD
test-keep-clean - Keep tests clean
test-one-assert - One concept per test
test-first-principles - Follow FIRST principles
test-build-operate-check - Use Build-Operate-Check pattern
10. Emergence and Simple Design (MEDIUM)
emerge-simple-design - Follow the four rules of simple design
emerge-expressiveness - Maximize expressiveness
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
373
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