---
rating: ⭐⭐
title: 37signals-rails
url: https://skills.sh/pproenca/dot-skills/37signals-rails
---

# 37signals-rails

skills/pproenca/dot-skills/37signals-rails
37signals-rails
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill 37signals-rails
SKILL.md
37signals Rails Best Practices

Comprehensive coding principles and conventions for Ruby on Rails applications, as practiced at 37signals (Basecamp, HEY, Fizzy). Contains 56 rules across 8 categories, prioritized by architectural impact. Derived from official 37signals sources: the Fizzy codebase, STYLE.md, AGENTS.md, the Rails Doctrine, DHH's "On Writing Software Well" series, and the unofficial 37signals style guide (265 Fizzy PRs).

When to Apply

Reference these guidelines when:

Writing new Rails controllers, models, or views
Deciding between gems and vanilla Rails
Modeling state and database schema
Setting up background jobs, caching, or real-time features
Reviewing code for 37signals-style conventions
Refactoring toward rich domain models
Choosing authentication or authorization approach
Adding Stimulus controllers or Turbo patterns
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Architecture Fundamentals	CRITICAL	arch-
2	Controllers & REST	CRITICAL	ctrl-
3	Domain Modeling	HIGH	model-
4	State Management	HIGH	state-
5	Database & Infrastructure	HIGH	db-
6	Views & Frontend	MEDIUM	view-
7	Code Style	MEDIUM	style-
8	Testing	MEDIUM	test-
Quick Reference
1. Architecture Fundamentals (CRITICAL)
arch-rich-models - Rich Domain Models Over Service Objects
arch-vanilla-rails - Vanilla Rails is Plenty
arch-avoid-patterns - Deliberately Avoided Patterns and Gems
arch-earn-abstractions - Earn Abstractions Through Rule of Three
arch-build-before-gems - Build It Yourself Before Reaching for Gems
arch-ship-to-learn - Start Simple — Add Complexity Only After Validation
arch-domain-facades - Domain Models as Facades Over Internal Complexity
arch-single-business-layer - Single Layer for Business Logic
arch-custom-auth - Custom Passwordless Auth Over Devise
2. Controllers & REST (CRITICAL)
ctrl-crud-only - CRUD Controllers Over Custom Actions
ctrl-model-as-resources - Model Non-CRUD Operations as Separate Resources
ctrl-thin-controllers - Thin Controllers with Rich Domain Models
ctrl-params-expect - Use params.expect() for Parameter Validation
ctrl-controller-concerns - Controller Concerns for Cross-Cutting Behavior
ctrl-nested-resources - Nested Resources with scope module
3. Domain Modeling (HIGH)
model-concerns - Concerns for Horizontal Code Sharing
model-normalizes - Use normalizes Macro for Data Cleaning
model-store-accessor - Use store_accessor for JSON Column Access
model-delegated-type - Use delegated_type for Polymorphism
model-counter-caches - Counter Caches to Prevent N+1 Count Queries
model-touch-chains - Touch Chains for Cache Invalidation
model-callbacks-auxiliary - Callbacks for Auxiliary Complexity
model-event-tracking - Polymorphic Event Model for Activity Tracking
model-poro-namespacing - Namespace POROs Under Parent Models
4. State Management (HIGH)
state-records-over-booleans - Records as State Over Boolean Columns
state-timestamps - Timestamps for State Transitions
state-enums - Enums for Categorical States
state-db-constraints - Database Constraints Over ActiveRecord Validations
state-write-time - Compute at Write Time Not Read Time
5. Database & Infrastructure (HIGH)
db-backed-everything - Database-Backed Everything
db-solid-queue - Solid Queue for Background Jobs
db-solid-cable - Solid Cable for Real-Time Pub/Sub
db-solid-cache - Solid Cache for Application Caching
db-multi-tenancy - Path-Based Multi-Tenancy with Current.account
db-uuid-primary-keys - UUIDs as Primary Keys
db-no-foreign-keys - No Foreign Key Constraints
6. Views & Frontend (MEDIUM)
view-turbo-frames - Turbo Frames for Scoped Page Fragments
view-turbo-streams - Turbo Streams for Real-Time Updates
view-stimulus-targets - Stimulus Targets Over CSS Selectors
view-stimulus-design - Stimulus Controller Design Principles
view-helpers-not-partials - Extract Logic to Helpers Not Partials
view-progressive-enhancement - Progressive Enhancement as Primary Pattern
view-fragment-caching - Fragment Caching for View Performance
view-http-caching - HTTP Caching with fresh_when and ETags
7. Code Style (MEDIUM)
style-conditionals - Expanded Conditionals Over Guard Clauses
style-method-ordering - Methods Ordered by Call Sequence
style-positive-names - Use Positive Names for Methods and Scopes
style-naming-return-values - Method Names Reflect Return Values
style-visibility-modifiers - Visibility Modifier Formatting
style-bang-methods - Bang Methods Only When Non-Bang Exists
style-async-naming - Use _later and _now Suffixes for Async Operations
8. Testing (MEDIUM)
test-minitest - Minitest Over RSpec
test-fixtures - Database Fixtures Over FactoryBot
test-no-damage - No Test-Induced Design Damage
test-no-system-tests - Integration Tests Over System Tests
test-behavior - Test Behavior Not Implementation
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
141
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