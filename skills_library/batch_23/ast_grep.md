---
title: ast-grep
url: https://skills.sh/knoopx/pi/ast-grep
---

# ast-grep

skills/knoopx/pi/ast-grep
ast-grep
Installation
$ npx skills add https://github.com/knoopx/pi --skill ast-grep
SKILL.md

ast-grep (ast-grep or sg) searches code by AST structure, not text. Patterns must be valid parseable code with $VAR meta-variables for wildcards.

Core Commands
# Search with pattern
ast-grep run -l ts --pattern 'console.log($X)' src/

# Search in directory (auto-detects language)
ast-grep run --pattern '$FUNC()' agent/extensions/

Pattern Syntax
$VAR — matches single AST node (uppercase only: $MOD, $_, $_123)
$$$VAR — matches zero or more nodes (function args, statements)
$_VAR — non-capturing (same name can match different content)
Patterns must be valid code: import { $X } from "$Y" works, from $X fails
Common Patterns
Find re-exports (barrel files)
ast-grep run -l ts --pattern 'export * from "$Y"' ./
ast-grep run -l ts --pattern 'export { $$$X } from "$Y"' ./
ast-grep run -l ts --pattern 'export type * from "$Y"' ./

Find all imports from a module
ast-grep run -l ts --pattern 'import { $$$X } from "$MOD"' ./

Find function calls with specific structure
ast-grep run -l ts --pattern 'console.log($MSG)' ./
ast-grep run -l ts --pattern 'fetch($URL).then($H)' ./

Detect anti-patterns
# await inside Promise.all
ast-grep run -l ts --pattern 'await $X' ./ \
  --selector call_expression \
  --pattern 'Promise.all($$_)'

Tips
Use --debug-query=ast to see parsed AST structure
Check playground for pattern validation
Patterns fail silently if not parseable — verify with --debug-query
Weekly Installs
40
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass