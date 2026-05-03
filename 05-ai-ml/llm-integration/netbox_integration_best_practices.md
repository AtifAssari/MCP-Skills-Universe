---
title: netbox-integration-best-practices
url: https://skills.sh/netboxlabs/netbox-best-practices/netbox-integration-best-practices
---

# netbox-integration-best-practices

skills/netboxlabs/netbox-best-practices/netbox-integration-best-practices
netbox-integration-best-practices
Installation
$ npx skills add https://github.com/netboxlabs/netbox-best-practices --skill netbox-integration-best-practices
SKILL.md
NetBox Integration Best Practices Skill

This skill provides best practices guidance for building integrations and automations with NetBox REST and GraphQL APIs.

Target Audience
Engineers building integrations atop NetBox APIs
Teams planning new automations with Claude
Developers learning NetBox API best practices

Scope: This skill covers API integration patterns. It does NOT cover plugin development, custom scripts, or NetBox administration.

NetBox Version Requirements
Feature	Version Required
REST API	All versions
GraphQL API	2.9+
v2 Tokens	4.5+ (use these!)
v1 Token Deprecation	4.7+ (migrate before this)

Primary target: NetBox 4.4+ with 4.5+ for v2 token features.

When to Apply This Skill

Apply these practices when:

Building new NetBox API integrations
Reviewing existing integration code
Troubleshooting performance issues
Planning automation architecture
Writing scripts that interact with NetBox
Priority Levels
Level	Description	Action
CRITICAL	Security vulnerabilities, data loss, severe performance	Must fix immediately
HIGH	Significant performance/reliability impact	Should fix soon
MEDIUM	Notable improvements, best practices	Plan to address
LOW	Minor improvements, optional	Consider when convenient
Quick Reference
Authentication
Use v2 tokens on NetBox 4.5+: Bearer nbt_<key>.<token>
Migrate from v1 before NetBox 4.7 (deprecation planned)
REST API
Always paginate: ?limit=100 (max 1000)
Use PATCH for partial updates, not PUT
Use ?brief=True for list operations
Exclude config_context: ?exclude=config_context (major performance impact)
Avoid ?q= search filter at scale; use specific filters
Bulk operations use list endpoints with JSON arrays (not separate endpoints)
GraphQL
Use the query optimizer: netbox-graphql-query-optimizer
Always paginate every list query
Paginate at every level of nesting
Beware offset pagination at scale: Deep offsets are slow; use ID range filtering in 4.5.x, cursor-based in 4.6.0+ (#21110)
Request only needed fields
Keep depth ≤3, never exceed 5
Performance
Exclude config_context from device lists
Use brief mode for large lists
Parallelize independent requests
Data Ingestion (Diode)
For high-volume data ingestion, use Diode instead of direct API
Specify dependencies by name, not ID—Diode resolves or creates them
No dependency order needed—Diode handles object creation order
Use pip install netboxlabs-diode-sdk for Python
Use REST/GraphQL API for reading; use Diode for writing/populating
Branching (Plugin)

Requires netbox-branching plugin.

Lifecycle: Create → Wait (PROVISIONING→READY) → Work → Sync → Merge
Context header: X-NetBox-Branch: {schema_id} (8-char ID, not name)
Async operations: sync/merge/revert return Job objects—poll for completion
Dry-run: All async ops accept {"commit": false} for validation
Rules by Category
Authentication Rules
Rule	Impact	Description
auth-use-v2-tokens	CRITICAL	Use v2 tokens on NetBox 4.5+
auth-provisioning-endpoint	MEDIUM	Use provisioning endpoint for automated token creation
REST API Rules
Rule	Impact	Description
rest-list-endpoint-bulk-ops	CRITICAL	Use list endpoints for bulk operations
rest-pagination-required	HIGH	Always paginate list requests
rest-patch-vs-put	HIGH	Use PATCH for partial updates
rest-brief-mode	HIGH	Use ?brief=True for lists
rest-field-selection	HIGH	Use ?fields= to select fields
rest-exclude-config-context	HIGH	Exclude config_context from device lists
rest-avoid-search-filter-at-scale	HIGH	Avoid q= with large datasets
rest-filtering-expressions	MEDIUM	Use lookup expressions
rest-custom-field-filters	MEDIUM	Filter by custom fields
rest-nested-serializers	LOW	Understand nested serializers
rest-ordering-results	LOW	Use ordering parameter
rest-options-discovery	LOW	Use OPTIONS for discovery
GraphQL Rules
Rule	Impact	Description
graphql-use-query-optimizer	CRITICAL	Use query optimizer
graphql-always-paginate	CRITICAL	Paginate every list query
graphql-pagination-at-each-level	HIGH	Paginate nested lists
graphql-select-only-needed	HIGH	Request only needed fields
graphql-calibrate-optimizer	HIGH	Calibrate against production
graphql-max-depth	HIGH	Keep depth ≤3
graphql-prefer-filters	MEDIUM	Filter server-side
graphql-vs-rest-decision	MEDIUM	Choose appropriate API
graphql-complexity-budgets	LOW	Establish complexity budgets
Performance Rules
Rule	Impact	Description
perf-exclude-config-context	HIGH	Exclude config_context
perf-brief-mode-lists	HIGH	Use brief mode for lists
Data Modeling Rules
Rule	Impact	Description
data-dependency-order	CRITICAL	Create objects in dependency order
data-site-hierarchy	MEDIUM	Understand site hierarchy
data-ipam-hierarchy	MEDIUM	Understand IPAM hierarchy
data-custom-fields	MEDIUM	Use custom fields properly
data-tags-usage	MEDIUM	Use tags for classification
data-tenant-isolation	MEDIUM	Use tenants for separation
data-natural-keys	MEDIUM	Use natural keys
Integration Rules
Rule	Impact	Description
integ-diode-ingestion	HIGH	Use Diode for high-volume data ingestion
integ-pynetbox-client	HIGH	Use pynetbox for Python
integ-branch-api-workflow	HIGH	Complete branching lifecycle (plugin)
integ-branch-context-header	HIGH	Branch context with X-NetBox-Branch header (plugin)
integ-branch-async-operations	MEDIUM	Job polling for sync/merge/revert (plugin)
integ-webhook-configuration	MEDIUM	Configure webhooks
integ-change-tracking	LOW	Query object changes
External References
Official Documentation
NetBox Documentation
REST API Guide
GraphQL API Guide
Essential Tools
pynetbox - Official Python client
netbox-graphql-query-optimizer - Query analysis (essential for GraphQL)
Diode - Data ingestion service (for high-volume writes)
Diode Python SDK - Python client for Diode
NetBox Branching - Change management plugin (optional)
Community
NetBox GitHub
NetBox Discussions
Reference Documentation
Document	Purpose
HUMAN.md	Human-readable guide for engineers
netbox-integration-guidelines.md	Comprehensive technical reference
Weekly Installs
86
Repository
netboxlabs/netb…ractices
GitHub Stars
23
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass