---
title: eng-codebase-cleanup
url: https://skills.sh/hungv47/agent-skills/eng-codebase-cleanup
---

# eng-codebase-cleanup

skills/hungv47/agent-skills/eng-codebase-cleanup
eng-codebase-cleanup
Installation
$ npx skills add https://github.com/hungv47/agent-skills --skill eng-codebase-cleanup
SKILL.md
Codebase Cleanup

Reorganize and clean codebases without breaking functionality.

Workflow
Phase 1: Analysis

Before touching anything, understand the codebase.

Map the directory structure

find . -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" | head -100
tree -L 3 -I 'node_modules|.git|__pycache__|.next|dist|build|venv|.venv' || find . -maxdepth 3 -type d | grep -v node_modules | grep -v .git


Identify entry points and config files

package.json, pyproject.toml, requirements.txt, Cargo.toml
Main entry files (index., main., app., server.)
Config files (.config.js, .env, tsconfig.json)

Run scripts/analyze_codebase.py to generate dependency report

Ask clarifying questions if needed

What is the primary tech stack?
Are there specific directories to preserve?
Any files that look dead but are actually used?
Phase 2: Identify Cleanup Targets

Safe to remove without verification:

Empty directories
.DS_Store, Thumbs.db, desktop.ini
Duplicate package lock files (keep one)
pycache, .pyc, .pyo files
node_modules/.cache
Coverage reports, test artifacts
Editor configs if inconsistent (.idea, .vscode with personal settings)
Backup files (*.bak, *.backup, *~, *.swp)
Log files (*.log)
Compiled outputs if source exists

Requires dependency check before removal:

Unused source files (verify no imports)
Orphan test files (verify not in test config)
Unused assets/images
Old migration files (check if applied)
Commented-out code blocks
Unused dependencies in package.json/requirements.txt

Never remove without explicit permission:

Config files (might be environment-specific)
Database files or migrations
CI/CD configs
License files
README or docs
Phase 3: Reorganization Patterns

Standard directory structures by stack:

JavaScript/TypeScript:

src/
  components/    # UI components
  pages/         # Page components or routes
  hooks/         # Custom hooks
  utils/         # Helper functions
  services/      # API calls, external services
  types/         # TypeScript types
  constants/     # Constants, enums
  assets/        # Static files
tests/
  unit/
  integration/


Python:

src/<package_name>/
  __init__.py
  core/          # Core business logic
  api/           # API routes/endpoints
  models/        # Data models
  services/      # Business services
  utils/         # Utilities
tests/
  unit/
  integration/
  fixtures/


File naming conventions:

Components: PascalCase (Button.tsx)
Utilities: camelCase (formatDate.ts)
Constants: UPPER_SNAKE_CASE or kebab-case file
Tests: *.test.ts, .spec.ts, or test_.py
Phase 4: Execute Changes

Create backup commit before changes

git add -A && git commit -m "Pre-cleanup snapshot" 2>/dev/null || echo "No git or nothing to commit"


Remove safe-to-delete files first

find . -name ".DS_Store" -delete 2>/dev/null
find . -name "*.pyc" -delete 2>/dev/null
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find . -type d -empty -delete 2>/dev/null


Reorganize file structure

Move files in batches by category
Update imports after each batch
Run tests or type checks between batches if available

Update import paths

Check all files for old import paths
Use grep to find remaining references to old paths
Verify build still works after import updates

Remove dead code

Check for unused functions/variables with the analyzer script
Remove commented-out code older than current work
Phase 5: Validation

Run existing tests if available

npm test 2>/dev/null || yarn test 2>/dev/null || pytest 2>/dev/null || echo "No test runner found"


Run type checker if TypeScript

npx tsc --noEmit 2>/dev/null || echo "TypeScript check skipped"


Run linter if configured

npm run lint 2>/dev/null || npx eslint . 2>/dev/null || echo "No linter found"


Verify the app builds

npm run build 2>/dev/null || yarn build 2>/dev/null || echo "Build check skipped"


List manual verification needed for features that lack test coverage

Decision Rules

When to consolidate directories:

Fewer than 3 files with no clear growth path
Multiple directories with same purpose (utils, helpers, lib)
Deeply nested single-file directories

When to split directories:

More than 15-20 files in one directory
Mixed concerns in same directory
Files with different lifecycle

When NOT to reorganize:

Active feature development in that area
No test coverage for affected code
Team conventions exist (ask first)
Monorepo with workspace dependencies
Common Pitfalls
Moving files breaks dynamic imports (check for require variables, import())
Barrel files (index.ts re-exports) can hide dependency issues
CSS/SCSS imports may use relative paths
Asset paths in code may be hardcoded
Environment-specific configs might reference paths
Weekly Installs
10
Repository
hungv47/agent-skills
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass