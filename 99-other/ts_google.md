---
title: ts-google
url: https://skills.sh/pproenca/dot-skills/ts-google
---

# ts-google

skills/pproenca/dot-skills/ts-google
ts-google
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill ts-google
SKILL.md
Google TypeScript Best Practices

Comprehensive TypeScript style guide based on Google's internal standards, designed for AI agents and LLMs. Contains 45 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new TypeScript code
Organizing modules and imports
Designing type annotations and interfaces
Creating classes and functions
Reviewing code for style consistency
Refactoring existing TypeScript code
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Module Organization	CRITICAL	module-
2	Type Safety	CRITICAL	types-
3	Class Design	HIGH	class-
4	Function Patterns	HIGH	func-
5	Control Flow	MEDIUM-HIGH	control-
6	Error Handling	MEDIUM	error-
7	Naming & Style	MEDIUM	naming-
8	Literals & Coercion	LOW-MEDIUM	literal-
Quick Reference
1. Module Organization (CRITICAL)
module-named-exports - Use named exports over default exports
module-no-mutable-exports - Avoid mutable exports
module-es6-modules - Use ES6 modules exclusively
module-no-namespaces - Avoid TypeScript namespaces
module-import-paths - Use relative paths for project imports
module-import-type - Use import type for type-only imports
module-export-api-surface - Minimize exported API surface
2. Type Safety (CRITICAL)
types-no-any - Never use the any type
types-prefer-interfaces - Prefer interfaces over type aliases for objects
types-explicit-structural - Explicitly annotate structural types
types-nullable-patterns - Handle nullable types correctly
types-array-syntax - Use consistent array type syntax
types-no-wrapper-types - Never use wrapper object types
types-prefer-map-set - Prefer Map and Set over index signatures
types-no-empty-object - Avoid empty object type
3. Class Design (HIGH)
class-parameter-properties - Use parameter properties for constructor assignment
class-readonly-properties - Mark properties readonly when never reassigned
class-no-private-fields - Use TypeScript private over private fields
class-no-static-containers - Avoid container classes with only static members
class-constructor-parens - Always use parentheses in constructor calls
class-no-prototype-manipulation - Never manipulate prototypes directly
4. Function Patterns (HIGH)
func-declarations-over-expressions - Prefer function declarations over expressions
func-arrow-concise-bodies - Use concise arrow function bodies appropriately
func-avoid-this-rebinding - Avoid rebinding this
func-rest-parameters - Use rest parameters over arguments
func-generator-syntax - Use correct generator function syntax
func-default-parameters - Use default parameters sparingly
5. Control Flow (MEDIUM-HIGH)
control-always-use-braces - Always use braces for control structures
control-triple-equals - Always use triple equals
control-for-of-iteration - Prefer for-of over for-in for arrays
control-switch-default - Always include default case in switch
control-no-assignment-in-condition - Avoid assignment in conditional expressions
6. Error Handling (MEDIUM)
error-throw-errors - Always throw Error instances
error-catch-unknown - Type catch clause variables as unknown
error-empty-catch-comments - Document empty catch blocks
error-avoid-assertions - Avoid type and non-null assertions
7. Naming & Style (MEDIUM)
naming-identifier-styles - Use correct identifier naming styles
naming-descriptive-names - Use descriptive names
naming-no-decorative-underscores - Avoid decorative underscores
naming-no-interface-prefix - No I prefix for interfaces
naming-constants - Use CONSTANT_CASE for true constants
8. Literals & Coercion (LOW-MEDIUM)
literal-single-quotes - Use single quotes for strings
literal-number-formats - Use correct number literal formats
literal-explicit-coercion - Use explicit type coercion
literal-array-constructor - Avoid Array constructor
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
Weekly Installs
229
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