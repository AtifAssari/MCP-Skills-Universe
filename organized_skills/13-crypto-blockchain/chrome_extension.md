---
rating: ⭐⭐
title: chrome-extension
url: https://skills.sh/pproenca/dot-skills/chrome-extension
---

# chrome-extension

skills/pproenca/dot-skills/chrome-extension
chrome-extension
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill chrome-extension
SKILL.md
Chrome Extension Best Practices

Comprehensive performance and code quality guide for Chrome Extensions (Manifest V3). Contains 67 rules across 12 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new Chrome extension code
Migrating from Manifest V2 to Manifest V3
Optimizing service worker lifecycle and state management
Implementing content scripts for page interaction
Debugging performance issues in extensions
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Service Worker Lifecycle	CRITICAL	sw-
2	Content Script Optimization	CRITICAL	content-
3	Message Passing Efficiency	HIGH	msg-
4	Storage Operations	HIGH	storage-
5	Network & Permissions	MEDIUM-HIGH	net-
6	Memory Management	MEDIUM	mem-
7	UI Performance	MEDIUM	ui-
8	API Usage Patterns	LOW-MEDIUM	api-
9	Code Style & Naming	MEDIUM	style-
10	Component Patterns	MEDIUM	comp-
11	Error Handling	HIGH	err-
12	Testing Patterns	MEDIUM	test-
Quick Reference
1. Service Worker Lifecycle (CRITICAL)
sw-persist-state-storage - Persist state with chrome.storage instead of global variables
sw-avoid-keepalive - Avoid artificial service worker keep-alive patterns
sw-use-alarms-api - Use chrome.alarms instead of setTimeout/setInterval
sw-return-true-async - Return true from message listeners for async responses
sw-register-listeners-toplevel - Register event listeners at top level
sw-use-offscreen-for-dom - Use offscreen documents for DOM APIs
2. Content Script Optimization (CRITICAL)
content-use-specific-matches - Use specific URL match patterns
content-use-document-idle - Use document_idle for content script injection
content-programmatic-injection - Prefer programmatic injection over manifest declaration
content-minimize-script-size - Minimize content script bundle size
content-batch-dom-operations - Batch DOM operations to minimize reflows
content-use-mutation-observer - Use MutationObserver instead of polling
3. Message Passing Efficiency (HIGH)
msg-use-ports-for-frequent - Use port connections for frequent message exchange
msg-minimize-payload-size - Minimize message payload size
msg-debounce-frequent-events - Debounce high-frequency events before messaging
msg-check-lasterror - Always check chrome.runtime.lastError
msg-avoid-broadcast-to-all-tabs - Avoid broadcasting messages to all tabs
4. Storage Operations (HIGH)
storage-batch-operations - Batch storage operations instead of individual calls
storage-choose-correct-type - Choose the correct storage type for your use case
storage-cache-frequently-accessed - Cache frequently accessed storage values
storage-use-session-for-temp - Use storage.session for temporary runtime data
storage-avoid-storing-large-blobs - Avoid storing large binary blobs
5. Network & Permissions (MEDIUM-HIGH)
net-use-declarativenetrequest - Use declarativeNetRequest instead of webRequest
net-request-minimal-permissions - Request minimal required permissions
net-use-activetab - Use activeTab permission instead of broad host permissions
net-limit-csp-modifications - Avoid modifying Content Security Policy headers
6. Memory Management (MEDIUM)
mem-cleanup-event-listeners - Clean up event listeners when content script unloads
mem-avoid-detached-dom - Avoid holding references to detached DOM nodes
mem-avoid-closure-leaks - Avoid accidental closure memory leaks
mem-clear-intervals-timeouts - Clear intervals and timeouts on cleanup
mem-use-weak-collections - Use WeakMap and WeakSet for DOM element references
7. UI Performance (MEDIUM)
ui-minimize-popup-bundle - Minimize popup bundle size for fast startup
ui-render-with-cached-data - Render popup UI with cached data first
ui-batch-badge-updates - Batch badge updates to avoid flicker
ui-use-options-page-lazy - Lazy load options page sections
8. API Usage Patterns (LOW-MEDIUM)
api-use-promises-over-callbacks - Use promise-based API calls over callbacks
api-query-tabs-efficiently - Query tabs with specific filters
api-avoid-redundant-api-calls - Avoid redundant API calls in loops
api-use-alarms-minperiod - Respect alarms API minimum period
api-handle-context-invalidated - Handle extension context invalidated errors
api-use-declarative-content - Use declarative content API for page actions
9. Code Style & Naming (MEDIUM)
style-boolean-naming - Use is/has/should prefixes for boolean variables
style-cache-naming - Use consistent cache variable naming
style-constants - Define constants for magic values
style-directory-structure - Organize code by feature/layer
style-file-naming - Use consistent file naming conventions
style-function-naming - Use descriptive function names
style-import-type - Use type-only imports for types
style-index-entry-points - Use index files for module entry points
style-message-enums - Use enums for message types
style-type-naming - Use PascalCase for types and interfaces
10. Component Patterns (MEDIUM)
comp-adapter-interface - Use adapter pattern for browser APIs
comp-content-script-structure - Structure content scripts consistently
comp-css-class-patterns - Use BEM or prefixed CSS classes
comp-manager-class - Use manager classes for complex state
comp-type-guards - Use type guards for runtime validation
comp-ui-components - Create reusable UI components
11. Error Handling (HIGH)
err-context-invalidation - Handle extension context invalidation
err-early-return - Use early returns for error handling
err-null-coalescing - Use nullish coalescing for defaults
err-promise-barrier - Use promise barriers for coordination
err-storage-operations - Handle storage operation failures
err-url-parsing - Safely parse URLs with try/catch
err-validation-pattern - Validate inputs at boundaries
12. Testing Patterns (MEDIUM)
test-browser-api-mocking - Mock chrome APIs in tests
test-organization - Organize tests by feature
test-validation-functions - Test validation functions thoroughly
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Full Compiled Document

For a complete guide with all rules in a single document, see AGENTS.md.

Reference Files
File	Description
AGENTS.md	Complete compiled guide with all rules
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
434
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn