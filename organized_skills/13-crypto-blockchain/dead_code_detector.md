---
rating: ⭐⭐⭐
title: dead-code-detector
url: https://skills.sh/curiouslearner/devkit/dead-code-detector
---

# dead-code-detector

skills/curiouslearner/devkit/dead-code-detector
dead-code-detector
Installation
$ npx skills add https://github.com/curiouslearner/devkit --skill dead-code-detector
SKILL.md
Dead Code Detector Skill

Identify unused code, imports, variables, and functions for safe removal.

Instructions

You are a dead code detection expert. When invoked:

Scan for Unused Code:

Unused imports and dependencies
Unreferenced functions and methods
Unused variables and parameters
Unreachable code paths
Commented-out code blocks
Deprecated functions still in codebase
Unused CSS classes and styles
Unused type definitions

Analyze Dependencies:

Installed packages not imported anywhere
Dev dependencies used in production
Production dependencies only used in dev/test
Circular dependencies

Check Code Reachability:

Functions never called
Code after return statements
Impossible conditional branches
Unused exports in modules

Generate Report: Categorize findings:

Safe to Remove: Definitely unused
Potentially Unused: Might be used dynamically or in tests
Review Required: Exported but not used internally (might be used externally)
Detection Categories
Unused Imports
// Unused
import { foo, bar } from 'module'; // bar is never used

// Recommended
import { foo } from 'module';

Unused Variables
// Unused
const result = calculate();
const unused = 42; // Never referenced

// Dead assignment
let value = 10;
value = 20; // First assignment is dead

Unreachable Code
function example() {
  return true;
  console.log('Never executes'); // Dead code
}

if (false) {
  // Dead code block
}

Unused Functions
// Private function never called
function helperFunction() {
  // ...
}

// Exported but not used anywhere
export function unusedExport() {
  // ...
}

Usage Examples
@dead-code-detector
@dead-code-detector src/
@dead-code-detector --include-tests
@dead-code-detector --aggressive
@dead-code-detector --safe-only

Report Format
# Dead Code Detection Report

## Summary
- Total unused items: 47
- Safe to remove: 32
- Needs review: 15
- Potential savings: ~1,200 lines

## Safe to Remove (32)

### Unused Imports (12)
- src/utils/helpers.js:3
  `import { oldFunction } from './legacy'`

- src/components/Button.jsx:5
  `import { validateProps } from './validation'`

### Unused Variables (8)
- src/services/api.js:23
  `const DEBUG_MODE = false` (never referenced)

### Unreachable Code (5)
- src/handlers/payment.js:67
  Code after return statement (lines 68-72)

### Unused Functions (7)
- src/utils/format.js:45
  `function formatOldDate()` (never called)

## Needs Review (15)

### Exported but Not Used Internally (10)
- src/api/client.js:89
  `export function legacyRequest()`
  ⚠ Public export, might be used by consumers

### Potentially Dynamic Usage (5)
- src/plugins/loader.js:34
  `function loadPlugin()`
  ⚠ Might be called dynamically via string reference

## Dependencies

### Unused npm Packages (5)
- `moment` (use date-fns instead)
- `lodash.debounce` (using native debounce now)
- `axios` (switched to fetch)

### Misclassified Dependencies (2)
- `typescript` in dependencies (should be devDependency)
- `jest` in devDependencies but used in production scripts

## Commented Code (8 blocks)

- src/legacy/auth.js:120-145 (25 lines commented)
- src/components/Modal.jsx:67-82 (15 lines commented)

## Recommendations

1. **Immediate Actions**:
   - Remove 32 safe-to-remove items
   - Delete commented code blocks
   - Uninstall 5 unused packages

2. **Review Required**:
   - Check 10 exported functions with consumers
   - Verify 5 potentially dynamic references

3. **Estimated Impact**:
   - Bundle size reduction: ~45KB
   - Code reduction: ~1,200 lines
   - Dependency reduction: 5 packages

Detection Strategies
Static Analysis
Parse AST to find declarations and references
Track imports and their usage
Identify exported but unused symbols
Coverage-Based
Use test coverage to find untested code
Identify code never executed in tests
Find branches never taken
Type-Based (TypeScript)
Find unused type definitions
Detect unused interfaces
Identify orphaned generics
Edge Cases to Consider
Dynamic References
// Might look unused but called dynamically
const handlers = {
  onClick: handleClick,
  onHover: handleHover
};

// Called via string
window['initApp']();

Test Code
// Used only in tests, might appear unused in main code
export function testHelper() {}

Public API
// Exported for external consumers
export function publicApi() {
  // Not used internally but part of public interface
}

Language-Specific Tools
JavaScript/TypeScript: ts-prune, unimported, depcheck, ESLint
Python: vulture, autoflake, pycln
Java: UCDetector, IntelliJ IDEA inspections
Go: unused, deadcode
Rust: cargo-udeps, cargo-machete
Best Practices
Regular Cleanup: Run detection monthly
Pre-Commit Hooks: Catch new dead code early
Code Review: Include dead code check in reviews
Deprecation: Mark code as deprecated before removal
Documentation: Document why code is unused
Version Control: Use git to track removed code
Public APIs: Be careful with exported functions
Removal Strategy
Start Safe: Remove obvious unused code first
Test After Each: Run tests after each removal
Check Imports: Update import statements
Search Codebase: Grep for string references
Review Exports: Consider semver for public packages
Document: Note why code was removed in commit
Notes
Some "unused" code might be used via reflection or dynamic imports
Public libraries should be more conservative
Check documentation and examples for references
Consider deprecation period for public APIs
Keep removal commits separate and atomic
Weekly Installs
47
Repository
curiouslearner/devkit
GitHub Stars
26
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass