---
rating: ⭐⭐⭐
title: jetbrains-vmoptions
url: https://skills.sh/buyoung/skills/jetbrains-vmoptions
---

# jetbrains-vmoptions

skills/buyoung/skills/jetbrains-vmoptions
jetbrains-vmoptions
Installation
$ npx skills add https://github.com/buyoung/skills --skill jetbrains-vmoptions
SKILL.md
JetBrains IDE VM Options

Generate .vmoptions configurations for JetBrains IDEs. Output as Markdown code blocks (one option per line, # comments). Do not generate files directly.

Workflow
1. Identify IDE version (blocking)

Read prerequisite-check.md for validation logic. IDE version determines the JDK (17 vs 21), which controls which GC collectors and flags are available. Never skip this step — wrong version means wrong recommendations.

2. Understand the user's goal

Match the user's problem to a tuning strategy:

User says	Primary goal	Start with
"freezes", "hangs", "lag", "UI stutter"	Low GC pause times	gc-options.md → ZGC/Shenandoah
"slow indexing", "build is slow"	Throughput	gc-options.md → G1GC/Parallel
"out of memory", "OOM", "large project"	Memory capacity	memory-options.md → heap sizing
"startup is slow"	Fast startup	common-options.md → tiered compilation
"general tuning", "optimize"	Balanced	All references as needed
3. Compose options from references

Read only the relevant reference files. Each reference includes flag descriptions, defaults, usage notes, and example configurations.

File	Content	Read when
prerequisite-check.md	IDE version validation, JDK mapping	Always (step 1)
gc-options.md	GC selection and tuning flags	GC-related goals
memory-options.md	Heap, code cache, metaspace, large pages	Memory-related goals
common-options.md	Compiler, strings, diagnostics, threads	Performance/startup goals
4. Self-review before presenting
Verify every flag is compatible with the user's JDK version
Remove flags that conflict with each other (e.g., two different GC activations)
Remove flags the user didn't ask about and doesn't need — lean configs are better
Include a brief comment explaining each section's purpose
5. Present with context

Show the final .vmoptions block with:

A header comment noting the IDE version and JDK
Grouped sections (Memory, GC, Performance, Diagnostics)
A short explanation of each non-obvious choice
Scope
Supported: IDE versions 222+ (JDK 17) and 243+ (JDK 21)
GC collectors: Generational ZGC, ZGC, G1GC, Shenandoah, Parallel, Serial
Tuning areas: Memory, code cache, metaspace, GC, compiler, strings, diagnostics
Not in scope: OS-level tuning, plugin configuration, IDE settings (non-JVM), or IDE versions below 222
Output Example
# JetBrains IDE VM Options
# IntelliJ IDEA 2024.3 (version 243, JDK 21)

# Memory
-Xms2g
-Xmx4g

# Garbage Collector: Generational ZGC
-XX:+UseZGC
-XX:+ZGenerational

# Performance
-XX:ReservedCodeCacheSize=512m
-XX:+UseStringDeduplication
-XX:SoftRefLRUPolicyMSPerMB=50

# Diagnostics
-XX:+HeapDumpOnOutOfMemoryError
-XX:CICompilerCount=2

Weekly Installs
18
Repository
buyoung/skills
GitHub Stars
12
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass