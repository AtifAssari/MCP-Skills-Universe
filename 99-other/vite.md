---
title: vite
url: https://skills.sh/pproenca/dot-skills/vite
---

# vite

skills/pproenca/dot-skills/vite
vite
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill vite
SKILL.md
Vite Best Practices

Comprehensive performance optimization guide for Vite applications. Contains 42 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Configuring Vite for a new project
Troubleshooting slow dev server startup
Optimizing production bundle size
Debugging HMR issues
Writing or evaluating Vite plugins
Migrating from Webpack or other bundlers
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Dependency Pre-bundling	CRITICAL	deps-
2	Plugin Performance	CRITICAL	plugin-
3	Bundle Optimization	CRITICAL	bundle-
4	Import Resolution	HIGH	import-
5	Build Configuration	HIGH	build-
6	Development Server	MEDIUM-HIGH	dev-
7	CSS Optimization	MEDIUM	css-
8	Advanced Patterns	LOW-MEDIUM	advanced-
Quick Reference
1. Dependency Pre-bundling (CRITICAL)
deps-include-large-cjs - Include large dependencies with many modules
deps-exclude-esm - Exclude small ESM dependencies
deps-force-rebundle - Use --force flag for dependency changes
deps-hold-until-crawl - Configure holdUntilCrawlEnd for startup behavior
deps-entries - Configure custom entry points for discovery
deps-linked-packages - Handle linked dependencies in monorepos
2. Plugin Performance (CRITICAL)
plugin-lazy-imports - Use dynamic imports in plugin code
plugin-avoid-long-hooks - Avoid long operations in startup hooks
plugin-transform-early-return - Early return in transform hooks
plugin-audit-community - Audit community plugins for performance
plugin-swc-over-babel - Use SWC instead of Babel for React
3. Bundle Optimization (CRITICAL)
bundle-manual-chunks - Use manualChunks for vendor splitting
bundle-dynamic-imports - Use dynamic imports for route-level splitting
bundle-analyze - Analyze bundle composition
bundle-tree-shaking - Enable effective tree-shaking
bundle-chunk-warning - Address large chunk warnings
bundle-compression - Disable compressed size reporting for large projects
bundle-asset-inlining - Configure asset inlining threshold
4. Import Resolution (HIGH)
import-avoid-barrel - Avoid barrel file imports
import-explicit-extensions - Use explicit file extensions
import-path-aliases - Configure path aliases for clean imports
import-svg-strings - Import SVGs as strings instead of components
import-glob-patterns - Use glob imports carefully
5. Build Configuration (HIGH)
build-modern-target - Target modern browsers
build-minification - Use esbuild for minification
build-sourcemaps - Disable source maps in production
build-css-code-split - Enable CSS code splitting
build-rolldown - Consider Rolldown for faster builds
build-output-dir - Configure output directory and caching
6. Development Server (MEDIUM-HIGH)
dev-server-warmup - Warm up frequently used files
dev-browser-cache - Keep browser cache enabled in DevTools
dev-fs-limits - Increase file descriptor limits on Linux
dev-wsl-polling - Use polling for WSL file watching
dev-https-proxy - Configure HTTPS and proxy for development
7. CSS Optimization (MEDIUM)
css-lightning - Use Lightning CSS instead of PostCSS
css-avoid-preprocessors - Prefer CSS over preprocessors when possible
css-modules - Use CSS Modules for component styles
css-inline-critical - Extract critical CSS for initial paint
8. Advanced Patterns (LOW-MEDIUM)
advanced-ssr-externalize - Externalize dependencies for SSR
advanced-env-static - Use static environment variables
advanced-profiling - Profile build performance
advanced-lib-mode - Configure library mode for package development
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
171
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass