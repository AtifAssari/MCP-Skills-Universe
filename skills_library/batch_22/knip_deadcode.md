---
title: knip-deadcode
url: https://skills.sh/pproenca/dot-skills/knip-deadcode
---

# knip-deadcode

skills/pproenca/dot-skills/knip-deadcode
knip-deadcode
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill knip-deadcode
SKILL.md
Community Knip Dead Code Detection Best Practices

Comprehensive guide for detecting and removing dead code in JavaScript and TypeScript projects using Knip. Contains 43 rules across 8 categories, prioritized by impact to guide configuration, CI integration, and cleanup workflows.

When to Apply

Reference these guidelines when:

Configuring Knip for a new project or monorepo
Investigating false positives or false negatives
Setting up CI pipelines to prevent dead code regressions
Using auto-fix to clean up unused code
Optimizing Knip performance for large codebases
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Configuration Foundations	CRITICAL	config-
2	Entry Point Strategy	CRITICAL	entry-
3	Workspace & Monorepo	HIGH	workspace-
4	Dependency Analysis	HIGH	deps-
5	Export Detection	MEDIUM-HIGH	exports-
6	CI Integration	MEDIUM	ci-
7	Auto-Fix Workflow	MEDIUM	fix-
8	Performance Optimization	LOW-MEDIUM	perf-
Quick Reference
1. Configuration Foundations (CRITICAL)
config-avoid-broad-ignore - Avoid broad ignore patterns
config-configure-path-aliases - Configure path aliases in Knip
config-enable-plugins-explicitly - Enable framework plugins explicitly
config-run-without-config - Run without config first for baseline
config-separate-entry-project - Separate entry files from project files
config-use-json-schema - Use JSON schema for configuration validation
config-use-negation-patterns - Use negation patterns for exclusions
config-use-production-mode - Use production mode for shipping code analysis
2. Entry Point Strategy (CRITICAL)
entry-add-dynamic-imports - Add dynamic import targets as entry points
entry-exclude-test-files - Exclude test files from production entries
entry-include-all-entry-points - Include all application entry points
entry-include-bin-scripts - Include binary scripts as entry points
entry-use-compilers - Use compilers for non-standard file types
entry-use-plugin-entries - Use plugin entry points for frameworks
entry-verify-with-debug - Verify entry points with debug mode
3. Workspace & Monorepo (HIGH)
workspace-configure-root-workspace - Configure root workspace explicitly
workspace-ignore-specific - Ignore specific workspaces when needed
workspace-isolate-for-strict - Isolate workspaces for strict dependency checking
workspace-list-cross-deps - List cross-workspace dependencies explicitly
workspace-per-workspace-plugins - Configure plugins per workspace
workspace-use-workspace-globs - Use workspace globs for consistent configuration
4. Dependency Analysis (HIGH)
deps-add-unlisted-deps - Add unlisted dependencies to package.json
deps-avoid-transitive-reliance - Avoid relying on transitive dependencies
deps-configure-plugin-deps - Configure plugins for tool-specific dependencies
deps-fix-files-first - Fix unused files before dependencies
deps-ignore-conditional-deps - Ignore conditionally loaded dependencies
deps-remove-obsolete-types - Remove obsolete type definition packages
5. Export Detection (MEDIUM-HIGH)
exports-check-class-members - Check class members for unused code
exports-enable-entry-exports - Enable entry export checking for private packages
exports-handle-reexports - Handle re-exports in barrel files
exports-ignore-same-file - Ignore exports used in same file
exports-tag-public-api - Tag public API exports with JSDoc
exports-trace-usage - Trace export usage before removal
exports-use-include-libs - Use include libs for type-based consumption
6. CI Integration (MEDIUM)
ci-add-to-pipeline - Add Knip to CI pipeline
ci-separate-production-check - Separate production and default mode checks
ci-use-cache - Enable cache for faster CI runs
ci-use-max-issues - Use max issues for gradual adoption
ci-use-reporters - Use appropriate reporters for CI output
ci-watch-mode-local - Use watch mode for local development
7. Auto-Fix Workflow (MEDIUM)
fix-allow-remove-files - Explicitly allow file removal
fix-format-after-fix - Format code after auto-fix
fix-review-before-commit - Review auto-fix changes before commit
fix-update-deps-after - Update package manager after dependency fix
fix-use-fix-type - Use fix type for targeted cleanup
8. Performance Optimization (LOW-MEDIUM)
perf-filter-issue-types - Filter issue types for focused analysis
perf-limit-output - Limit output for large codebases
perf-profile-performance - Profile performance for slow analysis
perf-use-bun-runtime - Use Bun runtime for faster analysis
perf-use-cache-flag - Enable cache for repeated analysis
perf-use-workspace-filter - Filter workspaces for faster monorepo analysis
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
150
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