---
title: wordpress-performance-best-practices
url: https://skills.sh/bartekmis/wordpress-performance-best-practises/wordpress-performance-best-practices
---

# wordpress-performance-best-practices

skills/bartekmis/wordpress-performance-best-practises/wordpress-performance-best-practices
wordpress-performance-best-practices
Installation
$ npx skills add https://github.com/bartekmis/wordpress-performance-best-practises --skill wordpress-performance-best-practices
Summary

WordPress performance optimization guidelines across database, caching, assets, and plugin architecture.

34 rules organized by impact across 8 categories: database optimization, caching strategies, asset management, theme performance, plugin architecture, media optimization, API/AJAX, and advanced patterns
Covers critical areas including WP_Query optimization, transient and object cache usage, proper asset enqueueing, and REST API caching
Designed for code review and generation workflows, with rule prefixes (db-, cache-, asset-, etc.) for quick reference during development
Each rule includes explanations, incorrect/correct code examples, and context to guide WordPress plugin, theme, and custom code development
SKILL.md
WordPress Performance Best Practices

Comprehensive performance optimization guide for WordPress development, designed for AI agents and LLMs. Contains 34 rules across 8 categories, prioritized by impact to guide code review and generation.

When to Apply

Reference these guidelines when:

Writing WordPress plugins or themes
Working with WP_Query or database operations
Implementing caching (transients, object cache)
Optimizing asset loading (scripts, styles)
Reviewing WordPress code for performance issues
Working with REST API or AJAX handlers
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Database Optimization	CRITICAL	db-
2	Caching Strategies	CRITICAL	cache-
3	Asset Management	HIGH	asset-
4	Theme Performance	HIGH	theme-
5	Plugin Architecture	MEDIUM-HIGH	plugin-
6	Media Optimization	MEDIUM	media-
7	API and AJAX	MEDIUM	api-
8	Advanced Patterns	LOW-MEDIUM	advanced-
Quick Reference
1. Database Optimization (CRITICAL)
db-prepared-statements - Always use $wpdb->prepare() for queries
db-avoid-post-not-in - Avoid post__not_in, filter in PHP instead
db-use-wp-query - Use WP_Query/get_posts instead of direct DB queries
db-limit-query-results - Never use posts_per_page => -1
db-meta-query-indexing - Optimize meta queries, consider taxonomies
db-fields-optimization - Use fields => 'ids' when only IDs needed
2. Caching Strategies (CRITICAL)
cache-transients-proper-use - Use transients for external API calls
cache-object-cache - Use wp_cache_* with cache groups
cache-remote-requests - Always cache wp_remote_get responses
cache-invalidation - Implement precise, event-driven invalidation
cache-fragment-caching - Cache expensive template fragments
3. Asset Management (HIGH)
asset-proper-enqueue - Use wp_enqueue_script/style, never hardcode
asset-conditional-loading - Only load assets where needed
asset-defer-async - Use defer/async for non-critical scripts
asset-dequeue-unused - Remove unused plugin assets
asset-minification - Minify assets, use critical CSS
4. Theme Performance (HIGH)
theme-avoid-queries-in-templates - Keep queries out of template files
theme-template-parts - Use get_template_part with data passing
theme-loop-optimization - Optimize loops, use meta/term cache priming
theme-hooks-placement - Use appropriate hook priorities
5. Plugin Architecture (MEDIUM-HIGH)
plugin-conditional-loading - Load code only when needed
plugin-autoloading - Use PSR-4 autoloading
plugin-activation-hooks - Use activation hooks for setup tasks
plugin-hook-removal - Remove hooks properly with matching priority
6. Media Optimization (MEDIUM)
media-responsive-images - Use srcset and sizes attributes
media-lazy-loading - Lazy load below-fold, eager load LCP
media-image-sizes - Define appropriate custom image sizes
7. API and AJAX (MEDIUM)
api-rest-optimization - Optimize REST endpoints, add caching headers
api-admin-ajax - Use REST API for frontend, avoid admin-ajax
api-nonce-validation - Implement proper nonce validation
8. Advanced Patterns (LOW-MEDIUM)
advanced-autoload-optimization - Keep autoloaded options under 800KB
advanced-cron-optimization - Use system cron, batch long tasks
advanced-memory-management - Process in batches, clean up memory
advanced-query-monitor - Profile before optimizing
How to Use

Read individual rule files for detailed explanations and code examples:

rules/db-prepared-statements.md
rules/cache-transients-proper-use.md
rules/_sections.md


Each rule file contains:

Brief explanation of why it matters
Incorrect code example with explanation
Correct code example with explanation
Additional context and references
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
399
Repository
bartekmis/wordp…ractises
GitHub Stars
10
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass