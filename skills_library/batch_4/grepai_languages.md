---
title: grepai-languages
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-languages
---

# grepai-languages

skills/yoanbernabeu/grepai-skills/grepai-languages
grepai-languages
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-languages
SKILL.md
GrepAI Supported Languages

This skill covers the programming languages supported by GrepAI for indexing and call graph analysis.

When to Use This Skill
Checking if your language is supported
Configuring language-specific settings
Understanding trace capabilities per language
Troubleshooting language-related issues
Supported Languages Overview

GrepAI supports indexing for all text-based files, but has enhanced support for specific programming languages.

Full Support (Index + Trace)
Language	Extensions	Index	Trace
Go	.go	✅	✅
JavaScript	.js, .jsx	✅	✅
TypeScript	.ts, .tsx	✅	✅
Python	.py	✅	✅
PHP	.php	✅	✅
C	.c, .h	✅	✅
C++	.cpp, .hpp, .cc, .cxx, .hh	✅	✅
Rust	.rs	✅	✅
Zig	.zig	✅	✅
C#	.cs	✅	✅
Java	.java	✅	✅
Pascal/Delphi	.pas, .dpr	✅	✅
Index Only (No Trace)
Language	Extensions	Index	Trace
Ruby	.rb	✅	❌
Swift	.swift	✅	❌
Kotlin	.kt, .kts	✅	❌
Scala	.scala	✅	❌
Lua	.lua	✅	❌
Shell	.sh, .bash, .zsh	✅	❌
SQL	.sql	✅	❌
HTML	.html, .htm	✅	❌
CSS	.css, .scss, .less	✅	❌
Markdown	.md, .mdx	✅	❌
YAML	.yaml, .yml	✅	❌
JSON	.json	✅	❌
TOML	.toml	✅	❌
XML	.xml	✅	❌
Language Configuration
Enabling/Disabling Languages for Trace
# .grepai/config.yaml
trace:
  enabled_languages:
    - .go
    - .js
    - .ts
    - .jsx
    - .tsx
    - .py
    - .php
    - .rs
    - .c
    - .cpp
    - .cs
    - .java

Excluding Certain Extensions
trace:
  enabled_languages:
    - .go
    # Exclude JavaScript intentionally
    # - .js

  exclude_patterns:
    - "*_test.go"
    - "*.spec.ts"

Language-Specific Tips
Go
trace:
  enabled_languages:
    - .go
  exclude_patterns:
    - "*_test.go"
    - "mock_*.go"
    - "*_mock.go"


Trace accuracy: Excellent. Go's explicit syntax makes tracing very reliable.

JavaScript/TypeScript
trace:
  enabled_languages:
    - .js
    - .jsx
    - .ts
    - .tsx
  exclude_patterns:
    - "*.test.js"
    - "*.spec.ts"
    - "*.d.ts"  # Type declarations


Trace accuracy: Good. Some dynamic patterns may be missed.

Python
trace:
  enabled_languages:
    - .py
  exclude_patterns:
    - "test_*.py"
    - "*_test.py"
    - "conftest.py"


Trace accuracy: Good. Dynamic imports and decorators may be missed.

C/C++
trace:
  enabled_languages:
    - .c
    - .h
    - .cpp
    - .hpp
    - .cc
    - .cxx
  exclude_patterns:
    - "*_test.cpp"


Trace accuracy: Good. Macros and templates may affect accuracy.

Rust
trace:
  enabled_languages:
    - .rs
  exclude_patterns:
    - "**/tests/**"
    - "**/benches/**"


Trace accuracy: Excellent. Rust's explicit syntax aids accurate tracing.

PHP
trace:
  enabled_languages:
    - .php
  exclude_patterns:
    - "*Test.php"
    - "**/tests/**"


Trace accuracy: Good. Magic methods may not be fully traced.

Java
trace:
  enabled_languages:
    - .java
  exclude_patterns:
    - "*Test.java"
    - "**/test/**"


Trace accuracy: Good. Reflection-based calls may be missed.

C#
trace:
  enabled_languages:
    - .cs
  exclude_patterns:
    - "*Tests.cs"
    - "**/Tests/**"


Trace accuracy: Good. Delegates and events may be partially traced.

Multi-Language Projects

For projects with multiple languages:

trace:
  enabled_languages:
    # Backend (Go)
    - .go
    # Frontend (TypeScript)
    - .ts
    - .tsx
    # Shared (SQL, etc.)
    - .sql  # Index only

  exclude_patterns:
    - "*_test.go"
    - "*.spec.ts"

Index vs Trace Explained
Index (Semantic Search)
Works on any text file
Code is chunked and embedded
Enables semantic search
No language-specific parsing required
Trace (Call Graphs)
Requires language-specific parsing
Extracts function definitions and calls
Builds caller/callee relationships
Uses regex (fast) or tree-sitter (precise)
Trace Modes by Language
Language	Fast Mode	Precise Mode
Go	✅	✅
JavaScript	✅	✅
TypeScript	✅	✅
Python	✅	✅
PHP	✅	✅
C/C++	✅	✅
Rust	✅	✅
Zig	✅	✅
C#	✅	✅
Java	✅	✅
Pascal	✅	⚠️ Limited
Adding Custom Extensions

If you have non-standard extensions, they'll be indexed but not traced:

# Custom extension files will be indexed
ignore:
  # Only add patterns for files you DON'T want indexed
  - "*.generated.go"

File Type Detection

GrepAI uses file extensions for detection. It does NOT use:

Shebangs (#!/usr/bin/env python)
File content analysis
.editorconfig
Unsupported Languages (Index Works, No Trace)

These languages can be indexed for semantic search but don't have trace support:

Ruby
Swift
Kotlin
Scala
Elixir
Clojure
Haskell
OCaml
F#
Erlang
R
Julia
Perl
Groovy

Workaround: Use semantic search to find code, then manually trace.

Best Practices
Enable only needed languages: Faster trace building
Exclude test files: Cleaner trace results
Use precise mode for accuracy: When trace results seem incomplete
Match your tech stack: Configure based on your actual languages
Checking Language Support
# Check what's being indexed
grepai status

# Will show file counts by type

Common Issues

❌ Problem: Files not being indexed ✅ Solution: Check file isn't in ignore patterns

❌ Problem: Trace missing for language ✅ Solution: Ensure language is in enabled_languages

❌ Problem: Wrong language detected ✅ Solution: GrepAI uses extensions only; rename files if needed

Output Format

Language support summary:

📚 GrepAI Language Support

Full Support (Index + Trace):
- Go (.go)
- JavaScript (.js, .jsx)
- TypeScript (.ts, .tsx)
- Python (.py)
- PHP (.php)
- C/C++ (.c, .cpp, .h, .hpp)
- Rust (.rs)
- Zig (.zig)
- C# (.cs)
- Java (.java)
- Pascal (.pas, .dpr)

Index Only (No Trace):
- Ruby, Swift, Kotlin, Scala
- Shell scripts, SQL, HTML, CSS
- Config files (YAML, JSON, TOML)
- Documentation (Markdown)

Your config enables trace for:
- .go, .js, .ts, .py

Weekly Installs
422
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