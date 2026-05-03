---
rating: ⭐⭐
title: nginx-c-module-design
url: https://skills.sh/pproenca/dot-skills/nginx-c-module-design
---

# nginx-c-module-design

skills/pproenca/dot-skills/nginx-c-module-design
nginx-c-module-design
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill nginx-c-module-design
SKILL.md
nginx.org C Module Directive Design Best Practices

Comprehensive directive design guide for nginx C module authors, focused on creating clear, consistent, and admin-friendly configuration interfaces. Contains 46 rules across 8 categories, prioritized by impact to guide decisions about what to expose, how to name it, and how to evolve it safely.

When to Apply

Reference these guidelines when:

Deciding which values to expose as directives vs hardcode
Naming new directives and choosing argument types
Selecting scope placement (http, server, location)
Setting default values and validation behavior
Designing nginx variables for runtime data
Deprecating or renaming existing directives
Companion Skills

This skill focuses on design decisions (the "what" and "why"). For implementation mechanics, see:

nginx-c-modules — C implementation: memory pools, request lifecycle, config parsing, handlers, filters
nginx-c-perf — Performance: buffers, connections, locks, caching, timeouts
nginx-c-debug — Debugging: crash diagnosis, GDB, tracing, sanitizers
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Exposure Decisions	CRITICAL	expose-
2	Naming Conventions	CRITICAL	naming-
3	Directive Types	HIGH	type-
4	Scope Design	HIGH	scope-
5	Default Values	MEDIUM-HIGH	default-
6	Validation & Error Messages	MEDIUM	valid-
7	Variable Design	MEDIUM	var-
8	Evolution & Compatibility	LOW-MEDIUM	compat-
Quick Reference
1. Exposure Decisions (CRITICAL)
expose-configurable-vs-hardcode - Framework for Configurable vs Hardcoded Values
expose-escape-hatch - Provide Escape Hatches for Hardcoded Defaults
expose-feature-gate - Use Feature Gates for Optional Behavior
expose-too-many-directives - Avoid Over-Configuration
expose-path-resource - Always Expose External Resource Paths
expose-security-surface - Audit Security Implications of Every Exposed Directive
expose-environment-dependent - Expose Values That Vary by Deployment Environment
2. Naming Conventions (CRITICAL)
naming-module-prefix - Use a Consistent Module Prefix for All Directives
naming-sub-prefix-groups - Group Related Directives with Sub-Prefixes
naming-noun-over-verb - Prefer Noun Phrases for Directive Names
naming-no-abbreviations - Avoid Custom Abbreviations in Directive Names
naming-cross-module-consistency - Mirror Nginx Core Suffix Patterns for Analogous Directives
naming-lowercase-underscore - Use Lowercase with Underscores Only
3. Directive Types (HIGH)
type-flag-for-toggles - Use NGX_CONF_FLAG for Binary Toggles
type-enum-over-string - Use Enum Slot for Known Value Sets
type-time-size-units - Use Time and Size Slot Functions for Time and Size Values
type-take-n-fixed-args - Use TAKE1/TAKE2/TAKE12 for Fixed Argument Counts
type-one-more-lists - Use 1MORE for Variable-Length Value Lists
type-avoid-block - Avoid Block Directives for Features
type-custom-handler-complex - Use Custom Handlers for Complex Directive Parsing
4. Scope Design (HIGH)
scope-default-three-levels - Default to http + server + location Scope
scope-http-only-shared-resources - Restrict Shared Resource Directives to http Level Only
scope-server-connection-level - Use http + server Scope for Connection-Level Settings
scope-avoid-if-context - Do Not Support the if Context Unless Fully Tested
scope-location-path-operations - Restrict Path-Routing Directives to Location Context
5. Default Values (MEDIUM-HIGH)
default-zero-config-safe - Ensure Zero-Config Produces Safe Behavior
default-performance-optin - Make Performance Features Opt-In
default-safety-on - Default Security Settings to Restrictive Values
default-generous-timeouts - Default Timeouts to Generous Values
default-zero-unlimited - Use Zero to Mean Unlimited or Disabled for Numeric Limits
default-platform-aware-buffers - Use Platform-Aware Buffer Size Defaults
6. Validation & Error Messages (MEDIUM)
valid-parse-time-check - Validate All Directive Values at Config Parse Time
valid-show-invalid-value - Include the Invalid Value in Error Messages
valid-suggest-range - Include Valid Range or Format in Error Messages
valid-conflict-detection - Detect Conflicting Directives at Merge Time
valid-actionable-guidance - Provide Actionable Guidance in Error Messages
7. Variable Design (MEDIUM)
var-runtime-data-only - Expose Variables for Per-Request Runtime Data Only
var-naming-convention - Name Variables with Module Prefix and Descriptive Suffix
var-dynamic-prefix - Use Dynamic Prefix Variables for Key-Value Data
var-lazy-evaluation - Leverage Lazy Evaluation for Expensive Variables
var-in-directive-values - Support Variables in Directive Values Only When Per-Request Variation Is Needed
var-read-only-diagnostics - Expose Read-Only Diagnostic Variables for Observability
8. Evolution & Compatibility (LOW-MEDIUM)
compat-deprecation-warning - Log Warnings for Deprecated Directives Before Removal
compat-alias-old-directive - Keep Old Directive Name as an Alias
compat-multi-version-window - Maintain a Multi-Version Deprecation Window
compat-document-migration - Document Migration Path in Both Old and New Directive Documentation
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
124
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass