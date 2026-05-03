---
rating: ⭐⭐⭐
title: grepai-ignore-patterns
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-ignore-patterns
---

# grepai-ignore-patterns

skills/yoanbernabeu/grepai-skills/grepai-ignore-patterns
grepai-ignore-patterns
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-ignore-patterns
SKILL.md
GrepAI Ignore Patterns

This skill covers how to configure ignore patterns to exclude files and directories from GrepAI indexing.

When to Use This Skill
Excluding test files from search results
Ignoring generated or vendored code
Reducing index size by excluding unnecessary files
Customizing which files GrepAI indexes
How Ignore Patterns Work

GrepAI uses two sources for ignore patterns:

.grepai/config.yaml - Custom patterns you define
.gitignore - Automatically respected
Configuration Location
# .grepai/config.yaml
ignore:
  - pattern1
  - pattern2

Pattern Syntax
Directory Patterns
ignore:
  # Exact directory name (matches anywhere)
  - node_modules
  - vendor
  - __pycache__

  # With trailing slash (explicit directory)
  - dist/
  - build/
  - coverage/

File Patterns
ignore:
  # Exact filename
  - package-lock.json
  - yarn.lock

  # Wildcard patterns
  - "*.min.js"
  - "*.min.css"
  - "*.map"
  - "*.lock"

Path Patterns
ignore:
  # Paths containing substring
  - /tests/
  - /spec/
  - /__tests__/

  # Specific paths
  - src/generated/
  - api/swagger/

Glob Patterns
ignore:
  # Double star (recursive)
  - "**/test/**"
  - "**/mock/**"

  # Single star (single level)
  - "*.test.js"
  - "*.spec.ts"
  - "*_test.go"

Default Ignore Patterns

GrepAI's default configuration includes:

ignore:
  # Version control
  - .git
  - .svn
  - .hg

  # GrepAI itself
  - .grepai

  # Package managers
  - node_modules
  - vendor
  - .npm
  - .yarn

  # Build outputs
  - target
  - dist
  - build
  - out

  # Cache directories
  - __pycache__
  - .pytest_cache
  - .mypy_cache
  - .cache

  # Framework outputs
  - .next
  - .nuxt
  - .output

Common Ignore Configurations
JavaScript/TypeScript Project
ignore:
  - node_modules
  - dist
  - build
  - coverage
  - .nyc_output
  - "*.min.js"
  - "*.bundle.js"
  - "*.map"
  - package-lock.json
  - yarn.lock
  - pnpm-lock.yaml

Go Project
ignore:
  - vendor
  - bin
  - "*.pb.go"       # Protobuf generated
  - "*_mock.go"     # Mocks
  - "mocks/"
  - go.sum

Python Project
ignore:
  - __pycache__
  - .pytest_cache
  - .mypy_cache
  - .venv
  - venv
  - env
  - "*.pyc"
  - "*.pyo"
  - .eggs
  - "*.egg-info"
  - dist
  - build

Rust Project
ignore:
  - target
  - Cargo.lock
  - "*.rlib"

Java/Kotlin Project
ignore:
  - target
  - build
  - .gradle
  - "*.class"
  - "*.jar"
  - "*.war"

Monorepo
ignore:
  # Common
  - node_modules
  - dist
  - build
  - coverage

  # Specific packages to exclude
  - packages/legacy/
  - packages/deprecated/

  # Generated
  - "**/generated/**"
  - "**/__generated__/**"

Excluding Test Files

To focus search on production code:

ignore:
  # Test directories
  - tests/
  - test/
  - __tests__/
  - spec/

  # Test files by pattern
  - "*.test.js"
  - "*.test.ts"
  - "*.spec.js"
  - "*.spec.ts"
  - "*_test.go"
  - "test_*.py"
  - "*_test.py"


Alternative: Use search boosting instead to penalize (not exclude) tests:

search:
  boost:
    penalties:
      - pattern: /tests/
        factor: 0.5
      - pattern: _test.
        factor: 0.5

Excluding Generated Code
ignore:
  # Generated markers
  - "**/generated/**"
  - "*.generated.*"
  - "*.gen.*"

  # Specific generators
  - "*.pb.go"           # Protobuf
  - "*.graphql.ts"      # GraphQL codegen
  - "*.d.ts"            # TypeScript declarations
  - "swagger_*.go"      # Swagger
  - "openapi_*.ts"      # OpenAPI

Excluding Documentation
ignore:
  - docs/
  - documentation/
  - "*.md"
  - "*.mdx"
  - "*.rst"

Verifying Ignore Patterns

Check what's being indexed:

# Check index status
grepai status

# Output shows file count
# If too high, add more ignore patterns

Common Issues

❌ Problem: Index is too large ✅ Solution: Add more ignore patterns for dependencies and generated files

❌ Problem: Search returns vendor/test code ✅ Solution: Either ignore or use boosting penalties

❌ Problem: Pattern not working ✅ Solution: Check syntax - use quotes for patterns with special characters:

ignore:
  - "*.min.js"  # Correct
  - *.min.js    # May cause YAML parsing issues


❌ Problem: Need to include previously ignored files ✅ Solution: Remove from ignore list and re-run grepai watch

Best Practices
Start with defaults: Add patterns as needed
Exclude dependencies: Always ignore node_modules, vendor, etc.
Exclude build outputs: dist, build, target
Exclude lock files: Large, not useful for search
Consider boosting vs ignoring: Penalize instead of exclude for test files
Quote special characters: "*.min.js" not *.min.js
Re-indexing After Changes

After modifying ignore patterns:

# Stop existing daemon
grepai watch --stop

# Clear index and restart
rm .grepai/index.gob
grepai watch

Output Format

After configuring ignore patterns:

✅ Ignore Patterns Configured

   Patterns: 15 configured

   Categories:
   - Directories: node_modules, vendor, dist, build
   - File types: *.min.js, *.map, *.lock
   - Paths: /tests/, /docs/

   Also respecting: .gitignore

   Run 'grepai watch' to re-index with new patterns.

Weekly Installs
403
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass