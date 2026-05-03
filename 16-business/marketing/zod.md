---
rating: ⭐⭐
title: zod
url: https://skills.sh/pproenca/dot-skills/zod
---

# zod

skills/pproenca/dot-skills/zod
zod
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill zod
Summary

Schema validation best practices for TypeScript with 43 prioritized rules across type safety, parsing, and error handling.

Covers 8 rule categories from schema definition and parsing (CRITICAL) through type inference, error handling, and performance (LOW-MEDIUM)
Distinguishes safeParse() for user input, parseAsync() for async refinements, and parse() for trusted data; emphasizes validation at system boundaries
Provides guidance on z.infer for type inference, z.unknown() over z.any(), discriminated unions, and schema composition patterns
Includes error handling strategies: custom messages, flatten() for forms, path tracking for nested errors, and internationalization support
References individual rule files with code examples and a compiled full guide (AGENTS.md) for detailed explanations
SKILL.md
Zod Best Practices

Comprehensive schema validation guide for Zod in TypeScript applications. Contains 43 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new Zod schemas
Choosing between parse() and safeParse()
Implementing type inference with z.infer
Handling validation errors for user feedback
Composing complex object schemas
Using refinements and transforms
Optimizing bundle size and validation performance
Reviewing Zod code for best practices
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Schema Definition	CRITICAL	schema-
2	Parsing & Validation	CRITICAL	parse-
3	Type Inference	HIGH	type-
4	Error Handling	HIGH	error-
5	Object Schemas	MEDIUM-HIGH	object-
6	Schema Composition	MEDIUM	compose-
7	Refinements & Transforms	MEDIUM	refine-
8	Performance & Bundle	LOW-MEDIUM	perf-
Quick Reference
1. Schema Definition (CRITICAL)
schema-use-primitives-correctly - Use correct primitive schemas for each type
schema-use-unknown-not-any - Use z.unknown() instead of z.any() for type safety
schema-avoid-optional-abuse - Avoid overusing optional fields
schema-string-validations - Apply string validations at schema definition
schema-use-enums - Use enums for fixed string values
schema-coercion-for-form-data - Use coercion for form and query data
2. Parsing & Validation (CRITICAL)
parse-use-safeparse - Use safeParse() for user input
parse-async-for-async-refinements - Use parseAsync for async refinements
parse-handle-all-issues - Handle all validation issues not just first
parse-validate-early - Validate at system boundaries
parse-avoid-double-validation - Avoid validating same data twice
parse-never-trust-json - Never trust JSON.parse output
3. Type Inference (HIGH)
type-use-z-infer - Use z.infer instead of manual types
type-input-vs-output - Distinguish z.input from z.infer for transforms
type-export-schemas-and-types - Export both schemas and inferred types
type-branded-types - Use branded types for domain safety
type-enable-strict-mode - Enable TypeScript strict mode
4. Error Handling (HIGH)
error-custom-messages - Provide custom error messages
error-use-flatten - Use flatten() for form error display
error-path-for-nested - Use issue.path for nested error location
error-i18n - Implement internationalized error messages
error-avoid-throwing-in-refine - Return false instead of throwing in refine
5. Object Schemas (MEDIUM-HIGH)
object-strict-vs-strip - Choose strict() vs strip() for unknown keys
object-partial-for-updates - Use partial() for update schemas
object-pick-omit - Use pick() and omit() for schema variants
object-extend-for-composition - Use extend() for adding fields
object-optional-vs-nullable - Distinguish optional() from nullable()
object-discriminated-unions - Use discriminated unions for type narrowing
6. Schema Composition (MEDIUM)
compose-shared-schemas - Extract shared schemas into reusable modules
compose-intersection - Use intersection() for type combinations
compose-lazy-recursive - Use z.lazy() for recursive schemas
compose-preprocess - Use preprocess() for data normalization
compose-pipe - Use pipe() for multi-stage validation
7. Refinements & Transforms (MEDIUM)
refine-vs-superrefine - Choose refine() vs superRefine() correctly
refine-transform-coerce - Distinguish transform() from refine() and coerce()
refine-add-path - Add path to refinement errors
refine-defaults - Use default() for optional fields with defaults
refine-catch - Use catch() for fault-tolerant parsing
8. Performance & Bundle (LOW-MEDIUM)
perf-cache-schemas - Cache schema instances
perf-zod-mini - Use Zod Mini for bundle-sensitive applications
perf-avoid-dynamic-creation - Avoid dynamic schema creation in hot paths
perf-lazy-loading - Lazy load large schemas
perf-arrays - Optimize large array validation
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Individual rules: references/{prefix}-{slug}.md
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Related Skills
For React Hook Form integration, see react-hook-form skill
For API client generation, see orval skill
Sources
Zod Official Documentation
Zod v4 Release Notes
Zod GitHub Repository
Zod Mini
Total TypeScript Zod Tutorial
Weekly Installs
1.9K
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass