---
rating: ⭐⭐
title: rails-hotwire
url: https://skills.sh/pproenca/dot-skills/rails-hotwire
---

# rails-hotwire

skills/pproenca/dot-skills/rails-hotwire
rails-hotwire
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill rails-hotwire
SKILL.md
Community Rails Hotwire Best Practices

Comprehensive guide for building interactive Rails applications with Hotwire (Turbo + Stimulus), maintained by Community. Contains 53 rules across 9 categories, prioritized by impact to guide automated refactoring and code generation. Follows the DHH "One Person Framework" philosophy: the server renders HTML, Turbo makes it feel like an SPA, Stimulus adds the sprinkle of JS where needed.

When to Apply

Reference these guidelines when:

Configuring Turbo Drive navigation, prefetching, and caching behavior
Adding Turbo Frames for partial page updates and lazy loading
Delivering Turbo Streams for surgical DOM mutations
Broadcasting real-time updates over ActionCable
Enabling Turbo 8 morphing for page refreshes
Writing Stimulus controllers for client-side behavior
Handling errors in Turbo navigation, frames, and WebSocket connections
Choosing between Drive, Frames, Streams, Morphing, and Stimulus
Testing Hotwire interactions in system and integration tests
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Navigation & Drive	CRITICAL	drive-
2	Turbo Frames	CRITICAL	frame-
3	Turbo Streams	HIGH	stream-
4	Broadcasting & Real-Time	HIGH	bcast-
5	Morphing & Page Refresh	HIGH	morph-
6	Performance Optimization	MEDIUM-HIGH	perf-
7	Stimulus Patterns	MEDIUM-HIGH	stim-
8	Architecture Decisions	MEDIUM	arch-
9	Testing Hotwire	MEDIUM	test-
Quick Reference
1. Navigation & Drive (CRITICAL)
drive-prefetch-links - Enable link prefetching for instant navigation
drive-form-submissions - Use Turbo Drive for form submissions
drive-visit-actions - Control history with visit actions
drive-cache-control - Configure Turbo cache for preview pages
drive-selective-disable - Disable Turbo Drive on incompatible pages
drive-progress-bar - Customize the Turbo progress bar
drive-confirm-dialog - Use data-turbo-confirm for destructive actions
drive-error-recovery - Handle Turbo navigation and fetch errors gracefully
2. Turbo Frames (CRITICAL)
frame-lazy-loading - Defer frame loading until viewport entry
frame-scope-navigation - Scope navigation within frames
frame-src-navigation - Use src for dynamic frame content
frame-break-out - Handle frame breakout for redirects
frame-promote-visits - Promote frame navigation to page visits
frame-dom-id - Use dom_id for frame identification
frame-empty-state - Provide meaningful frame loading states
3. Turbo Streams (HIGH)
stream-progressive-enhance - Always provide HTML fallback for streams
stream-action-selection - Choose the right stream action for DOM mutations
stream-multi-target - Use targets for multi-element updates
stream-http-delivery - Deliver streams via HTTP for form responses
stream-websocket-source - Connect WebSocket sources in the body
stream-custom-actions - Register custom stream actions for complex DOM updates
4. Broadcasting & Real-Time (HIGH)
bcast-model-broadcasts - Use broadcasts_refreshes for simple model updates
bcast-debounce-n1 - Debounce broadcasts to prevent N+1 broadcast storms
bcast-scope-streams - Scope broadcast streams to accounts or users
bcast-refresh-over-replace - Prefer broadcast refresh over granular stream updates
bcast-avoid-view-logic-in-models - Keep broadcasting logic out of models
bcast-signed-stream-names - Use signed stream names for security
bcast-reconnect-handling - Handle WebSocket disconnection and reconnection
5. Morphing & Page Refresh (HIGH)
morph-enable-page-refresh - Enable morphing for page refreshes
morph-permanent-elements - Mark stateful elements as permanent
morph-scroll-preservation - Preserve scroll position during morphing
morph-stimulus-reconnect - Handle Stimulus controller reconnection after morph
morph-frame-refresh - Use refresh='morph' on frames for additive content
morph-vs-streams - Choose morphing over complex stream orchestration
6. Performance Optimization (MEDIUM-HIGH)
perf-optimistic-ui - Implement optimistic UI updates before server confirmation
perf-batch-streams - Batch multiple stream updates into single responses
perf-frame-caching - Cache Turbo Frame responses with fragment caching
perf-prefetch-strategic - Disable prefetch on expensive endpoints
perf-memory-leak-prevention - Clean up subscriptions and event listeners
7. Stimulus Patterns (MEDIUM-HIGH)
stim-outlets-communication - Use outlets for cross-controller communication
stim-values-reactive-state - Use Values API for reactive controller state
stim-action-descriptors - Use declarative action descriptors over addEventListener
stim-small-reusable-controllers - Keep Stimulus controllers small and reusable
8. Architecture Decisions (MEDIUM)
arch-progressive-enhancement - Follow the progressive enhancement hierarchy
arch-frame-vs-stream-decision - Use frames for scoped navigation, streams for multi-target updates
arch-importmap-management - Pin JavaScript dependencies with import maps
arch-avoid-client-state - Keep state on the server, not the client
arch-stimulus-boundaries - Use Stimulus only for client-side behavior
9. Testing Hotwire (MEDIUM)
test-system-test-async - Wait for Turbo updates in system tests
test-stream-assertions - Use Turbo Stream test helpers in integration tests
test-broadcast-assertions - Assert broadcasts with Turbo test helpers
test-frame-navigation - Test frame navigation with scoped assertions
test-websocket-timing - Handle WebSocket connection timing in system tests
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
175
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