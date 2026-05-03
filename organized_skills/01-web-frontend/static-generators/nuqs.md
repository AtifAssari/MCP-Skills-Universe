---
rating: ⭐⭐
title: nuqs
url: https://skills.sh/pproenca/dot-skills/nuqs
---

# nuqs

skills/pproenca/dot-skills/nuqs
nuqs
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill nuqs
Summary

Type-safe URL query state management for Next.js with 42 prioritized best practices across parser configuration, setup, and server integration.

Covers critical parser configuration (typed parsers, defaults, enums, arrays, JSON, dates) and adapter setup (NuqsAdapter, 'use client' directives, Next.js version compatibility)
Includes high-impact state management patterns using useQueryStates, functional updates, null clearing, and controlled inputs
Provides server integration guidance for Server Components, shallow rendering, useTransition integration, and Next.js 15+ async searchParams
Addresses performance optimization through throttling, debouncing, memoization, and URL serialization utilities
Covers history navigation modes (push vs. replace), debugging techniques, and advanced patterns like custom parsers and shorter URL keys
SKILL.md
Community nuqs Best Practices for Next.js

Comprehensive guide for type-safe URL query state management with nuqs in Next.js applications. Contains 42 rules across 8 categories, prioritized by impact to guide code generation, refactoring, and code review.

When to Apply

Reference these guidelines when:

Implementing URL-based state with nuqs
Setting up nuqs in a Next.js project
Configuring parsers for URL parameters
Integrating URL state with Server Components
Optimizing URL update performance
Debugging nuqs-related issues
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Parser Configuration	CRITICAL	parser-
2	Adapter & Setup	CRITICAL	setup-
3	State Management	HIGH	state-
4	Server Integration	HIGH	server-
5	Performance Optimization	MEDIUM	perf-
6	History & Navigation	MEDIUM	history-
7	Debugging & Testing	LOW-MEDIUM	debug-
8	Advanced Patterns	LOW	advanced-
Quick Reference
1. Parser Configuration (CRITICAL)
parser-use-typed-parsers - Use typed parsers for non-string values
parser-with-default - Use withDefault for non-nullable state
parser-enum-validation - Use enum parsers for constrained values
parser-array-format - Choose correct array parser format
parser-json-validation - Validate JSON parser input
parser-date-format - Select appropriate date parser
parser-index-offset - Use parseAsIndex for 1-based URL display
parser-hex-colors - Use parseAsHex for color values
2. Adapter & Setup (CRITICAL)
setup-nuqs-adapter - Wrap app with NuqsAdapter
setup-use-client - Add 'use client' directive for hooks
setup-import-server - Import server utilities from nuqs/server
setup-nextjs-version - Ensure compatible Next.js version
setup-shared-parsers - Define shared parsers in dedicated file
3. State Management (HIGH)
state-use-query-states - Use useQueryStates for related parameters
state-functional-updates - Use functional updates for derived state
state-clear-with-null - Clear URL parameters with null
state-controlled-inputs - Handle controlled input value properly
state-avoid-derived - Avoid derived state from URL parameters
state-options-inheritance - Use withOptions for parser-level configuration
state-setter-return - Use setter return value for URL access
4. Server Integration (HIGH)
server-search-params-cache - Use createSearchParamsCache for Server Components
server-shallow-false - Use shallow:false to trigger server re-renders
server-use-transition - Integrate useTransition for loading states
server-parse-before-get - Call parse() before get() in Server Components
server-share-parsers - Share parsers between client and server
server-next15-async - Handle async searchParams in Next.js 15+
5. Performance Optimization (MEDIUM)
perf-throttle-updates - Throttle rapid URL updates
perf-clear-on-default - Use clearOnDefault for clean URLs
perf-avoid-rerender - Memoize components using URL state
perf-serialize-utility - Use createSerializer for link URLs
perf-debounce-search - Debounce search input before URL update
6. History & Navigation (MEDIUM)
history-push-navigation - Use history:push for navigation-like state
history-replace-ephemeral - Use history:replace for ephemeral state
history-scroll-behavior - Control scroll behavior on URL changes
history-back-sync - Handle browser back/forward navigation
7. Debugging & Testing (LOW-MEDIUM)
debug-enable-logging - Enable debug logging for troubleshooting
debug-common-errors - Diagnose common nuqs errors
debug-testing - Test components with URL state
8. Advanced Patterns (LOW)
advanced-custom-parsers - Create custom parsers for complex types
advanced-url-keys - Use urlKeys for shorter URLs
advanced-eq-function - Implement eq function for object parsers
advanced-framework-adapters - Use framework-specific adapters
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
709
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