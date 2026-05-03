---
title: ninja
url: https://skills.sh/mohitmishra786/low-level-dev-skills/ninja
---

# ninja

skills/mohitmishra786/low-level-dev-skills/ninja
ninja
Installation
$ npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill ninja
SKILL.md
Ninja
Purpose

Guide agents through Ninja as a build executor: diagnosing failures, controlling parallelism, generating from CMake, and understanding the .ninja file format when needed.

Triggers
"Ninja is failing — how do I get more output?"
"How do I use Ninja with CMake?"
"How many parallel jobs does Ninja use?"
"How do I add a custom build step in Ninja?"
"What is a build.ninja file?"
Workflow
1. Ninja as a CMake generator

The most common use of Ninja is as the build executor for CMake:

# Configure with Ninja
cmake -S . -B build -G Ninja
cmake --build build                    # uses ninja internally

# Or invoke ninja directly
cd build && ninja

# Specify parallelism
ninja -j4
ninja -j$(nproc)

# Build specific target
ninja myapp
ninja install


CMake also supports Ninja Multi-Config:

cmake -S . -B build -G "Ninja Multi-Config"
cmake --build build --config Release
cmake --build build --config Debug

2. Verbose output and diagnostics
# Show full commands (not just [CC] foo.c)
ninja -v

# Dry run (show what would be built)
ninja -n

# Show why a target needs rebuilding
ninja -d explain myapp

# Print all targets
ninja -t targets all

# Print targets grouped by rule
ninja -t targets rule cc

# Dependency graph (graphviz)
ninja -t graph myapp | dot -Tsvg -o deps.svg

3. Common Ninja flags
Flag	Effect
-j N	Parallel jobs (default: CPUs + 2)
-l N	Don't start new jobs if load average > N
-k N	Keep going after N failures (default 1)
-v	Verbose: show full command lines
-n	Dry run
-C dir	Change to dir before doing anything
-t tool	Run a sub-tool (clean, query, targets, graph, compdb)
4. Cleaning
ninja -t clean          # remove build outputs
ninja -t clean -g       # also remove generated files


Or via CMake:

cmake --build build --target clean

5. compile_commands.json

Ninja (via CMake) can generate a compile_commands.json for IDE integration and clang-tidy:

cmake -S . -B build -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
ln -sf build/compile_commands.json .

6. build.ninja format (reference)

Rarely hand-written, but useful to understand for debugging:

# Variable
cflags = -Wall -O2

# Rule
rule cc
  command = gcc $cflags -c $in -o $out
  description = CC $in

# Build edge
build foo.o: cc foo.c

# Phony target
build all: phony foo.o

# Default target
default all


Key concepts:

rule: defines how to produce outputs from inputs
build: instantiates a rule with specific files
$in / $out: automatic variables for inputs/outputs
phony: a target that is always considered out of date (like .PHONY in make)
7. Ninja sub-tools
# List all build targets
ninja -t targets

# Query dependencies of a target
ninja -t query myapp

# Clean (already mentioned)
ninja -t clean

# Generate compile_commands.json (if supported by generator)
ninja -t compdb cc cxx > compile_commands.json

# List rules
ninja -t rules

8. Common issues
Issue	Cause	Fix
ninja: error: 'foo.o', needed by 'prog', missing and no known rule to make it	Missing build rule	Regenerate with CMake; check add_executable source list
Build not picking up changes	Stale build.ninja	Re-run cmake -S . -B build
Very slow parallel build	-j too high for I/O-bound build	Use -l$(nproc) to limit by load
Circular dependency	Rule depends on itself	Check CMake target dependencies

For the full Ninja command reference, build.ninja format details, and CMake integration patterns, see references/cheatsheet.md.

Related skills
Use skills/build-systems/cmake for CMake configuration that generates Ninja files
Use skills/build-systems/make for Make-based projects
Weekly Installs
101
Repository
mohitmishra786/…v-skills
GitHub Stars
80
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass