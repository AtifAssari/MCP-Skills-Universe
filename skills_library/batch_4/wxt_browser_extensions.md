---
title: wxt-browser-extensions
url: https://skills.sh/pproenca/dot-skills/wxt-browser-extensions
---

# wxt-browser-extensions

skills/pproenca/dot-skills/wxt-browser-extensions
wxt-browser-extensions
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill wxt-browser-extensions
SKILL.md
Community WXT Browser Extensions Best Practices

Comprehensive performance optimization guide for WXT browser extension development. Contains 49 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation. Updated for WXT v0.20+.

When to Apply

Reference these guidelines when:

Writing new WXT browser extension code
Implementing service worker background scripts
Injecting content scripts into web pages
Setting up messaging between extension contexts
Configuring manifest permissions and resources
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Service Worker Lifecycle	CRITICAL	svc-
2	Content Script Injection	CRITICAL	inject-
3	Messaging Architecture	HIGH	msg-
4	Storage Patterns	HIGH	store-
5	Bundle Optimization	MEDIUM-HIGH	bundle-
6	Manifest Configuration	MEDIUM	manifest-
7	UI Performance	MEDIUM	ui-
8	TypeScript Patterns	LOW-MEDIUM	ts-
Quick Reference
1. Service Worker Lifecycle (CRITICAL)
svc-register-listeners-synchronously - Register listeners synchronously to prevent missed events
svc-avoid-global-state - Use storage instead of in-memory state
svc-keep-alive-patterns - Keep service worker alive for long operations
svc-handle-install-update - Handle install and update lifecycle events
svc-offscreen-documents - Use offscreen documents for DOM operations
svc-declarative-net-request - Use declarative rules for network blocking
2. Content Script Injection (CRITICAL)
inject-use-main-function - Place runtime code inside main() function
inject-choose-correct-world - Select ISOLATED or MAIN world appropriately
inject-run-at-timing - Configure appropriate runAt timing
inject-use-ctx-invalidated - Handle context invalidation on update
inject-dynamic-registration - Use runtime registration for conditional injection
inject-all-frames - Configure allFrames for iframe handling
inject-spa-navigation - Handle SPA navigation with wxt:locationchange
3. Messaging Architecture (HIGH)
msg-type-safe-messaging - Use @webext-core/messaging for type-safe protocols
msg-return-true-for-async - Return true for async message handlers (raw API)
msg-use-tabs-sendmessage - Use tabs.sendMessage for content scripts
msg-use-ports-for-streams - Use ports for streaming communication
msg-handle-no-receiver - Handle missing message receivers
msg-avoid-circular-messages - Prevent circular message loops
4. Storage Patterns (HIGH)
store-use-define-item - Use storage.defineItem for type-safe access
store-choose-storage-area - Select appropriate storage area
store-batch-operations - Group related data into single defineItem
store-watch-for-changes - Use watch() for reactive updates
store-handle-quota-errors - Handle storage quota errors
store-versioned-migrations - Use versioning for schema migrations
5. Bundle Optimization (MEDIUM-HIGH)
bundle-split-entrypoints - Split code by entrypoint
bundle-analyze-size - Analyze and monitor bundle size
bundle-tree-shake-icons - Use direct imports for icon libraries
bundle-externalize-wasm - Load WASM dynamically
bundle-minify-content-scripts - Minimize content script size
6. Manifest Configuration (MEDIUM)
manifest-minimal-permissions - Request minimal permissions
manifest-use-optional-permissions - Use optional permissions progressively
manifest-web-accessible-resources - Scope web accessible resources
manifest-content-security-policy - Configure CSP correctly
manifest-cross-browser-compatibility - Support multiple browsers
7. UI Performance (MEDIUM)
ui-use-shadow-dom - Use Shadow DOM for injected UI
ui-defer-rendering - Defer popup rendering until needed
ui-cleanup-on-unmount - Clean up UI on unmount
ui-sidepanel-persistence - Preserve sidepanel state
ui-position-fixed-iframe - Use iframe for complex UI
ui-avoid-layout-thrashing - Batch DOM reads and writes
8. TypeScript Patterns (LOW-MEDIUM)
ts-use-imports-module - Use #imports virtual module and auto-imports
ts-use-browser-not-chrome - Use browser namespace over chrome
ts-type-entrypoint-options - Type entrypoint options explicitly
ts-augment-browser-types - Augment types for missing APIs
ts-strict-null-checks - Enable strict null checks
ts-import-meta-env - Use import.meta for build info
ts-avoid-any - Avoid any type in handlers
ts-path-aliases - Use path aliases for imports
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
463
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn