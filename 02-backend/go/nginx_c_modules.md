---
title: nginx-c-modules
url: https://skills.sh/pproenca/dot-skills/nginx-c-modules
---

# nginx-c-modules

skills/pproenca/dot-skills/nginx-c-modules
nginx-c-modules
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill nginx-c-modules
SKILL.md
nginx.org C Module Development Best Practices

Comprehensive development guide for nginx C modules, derived from the official nginx development documentation and community expertise. Contains 49 rules across 8 categories, prioritized by impact to guide correct module implementation and prevent common crashes, memory leaks, and undefined behavior.

When to Apply

Reference these guidelines when:

Writing new nginx C modules (handlers, filters, upstream, load-balancers)
Implementing configuration directives and merge logic
Managing memory with nginx pools and shared memory zones
Handling the HTTP request lifecycle (body reading, subrequests, finalization)
Working with nginx's event loop, timers, and thread pools
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Memory Management	CRITICAL	mem-
2	Request Lifecycle	CRITICAL	req-
3	Configuration System	HIGH	conf-
4	Handler Development	HIGH	handler-
5	Filter Chain	MEDIUM-HIGH	filter-
6	Upstream & Proxy	MEDIUM	upstream-
7	Event Loop & Concurrency	MEDIUM	event-
8	Data Structures & Strings	LOW-MEDIUM	ds-
Quick Reference
1. Memory Management (CRITICAL)
mem-pool-allocation - Use Pool Allocation Instead of Heap malloc
mem-check-allocation - Check Every Allocation Return for NULL
mem-pcalloc-structs - Use ngx_pcalloc for Struct Initialization
mem-cleanup-handlers - Register Pool Cleanup Handlers for External Resources
mem-pnalloc-strings - Use ngx_pnalloc for String Data Allocation
mem-pfree-limitations - Avoid Relying on ngx_pfree for Pool Allocations
mem-shared-slab - Use Slab Allocator for Shared Memory Zones
2. Request Lifecycle (CRITICAL)
req-finalize-once - Finalize Requests Exactly Once
req-no-access-after-finalize - Never Access Request After Finalization
req-body-async - Handle Request Body Reading Asynchronously
req-discard-body - Discard Request Body When Not Reading It
req-subrequest-completion - Use Post-Subrequest Handlers for Completion
req-count-reference - Increment Request Count Before Async Operations
req-internal-redirect - Return After Internal Redirect
3. Configuration System (HIGH)
conf-unset-init - Initialize Config Fields with UNSET Constants
conf-merge-all-fields - Merge All Config Fields in merge_loc_conf
conf-context-flags - Use Correct Context Flags for Directives
conf-null-command - Terminate Commands Array with ngx_null_command
conf-custom-handler - Use Custom Handlers for Complex Directive Parsing
conf-module-ctx-null - Set Unused Module Context Callbacks to NULL
conf-build-config - Write Correct config Build Script for Module Compilation
4. Handler Development (HIGH)
handler-send-header-first - Send Header Before Body Output
handler-last-buf - Set last_buf Flag on Final Buffer
handler-phase-registration - Register Phase Handlers in postconfiguration
handler-content-handler - Use content_handler for Location-Specific Response Generation
handler-error-page - Return HTTP Status Codes for Error Responses
handler-empty-response - Use header_only for Empty Body Responses
handler-module-ctx - Use Module Context for Per-Request State
handler-add-variable - Register Custom Variables in preconfiguration
5. Filter Chain (MEDIUM-HIGH)
filter-registration-order - Save and Replace Top Filter in postconfiguration
filter-call-next - Always Call Next Filter in the Chain
filter-check-subrequest - Distinguish Main Request from Subrequest in Filters
filter-buffer-chain-iteration - Iterate Buffer Chains Using cl->next Pattern
filter-buffering-flag - Set Buffering Flag When Accumulating Response Data
6. Upstream & Proxy (MEDIUM)
upstream-create-request - Build Complete Request Buffer in create_request
upstream-process-header - Parse Upstream Response Incrementally in process_header
upstream-peer-free - Track Failures in Peer free Callback
upstream-finalize - Clean Up Resources in finalize_request Callback
upstream-connection-reuse - Enable Keepalive for Upstream Connections
7. Event Loop & Concurrency (MEDIUM)
event-no-blocking - Never Use Blocking Calls in Event Handlers
event-timer-management - Delete Timers Before Freeing Associated Data
event-handle-read-write - Call ngx_handle_read/write_event After I/O Operations
event-thread-pool - Offload Blocking Operations to Thread Pool
event-posted-events - Use Posted Events for Deferred Processing
8. Data Structures & Strings (LOW-MEDIUM)
ds-ngx-str-not-null-terminated - Never Assume ngx_str_t Is Null-Terminated
ds-ngx-str-set-literals - Use ngx_string Macro Only with String Literals
ds-cpymem-pattern - Use ngx_cpymem for Sequential Buffer Writes
ds-list-iteration - Iterate ngx_list_t Using Part-Based Pattern
ds-hash-readonly - Build Hash Tables During Configuration Only
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
119
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass