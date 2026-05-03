---
rating: ⭐⭐⭐
title: linkers-lto
url: https://skills.sh/mohitmishra786/low-level-dev-skills/linkers-lto
---

# linkers-lto

skills/mohitmishra786/low-level-dev-skills/linkers-lto
linkers-lto
Installation
$ npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill linkers-lto
SKILL.md
Linkers and LTO
Purpose

Guide agents through linker selection, common linker flags, link-order issues, LTO setup, and symbol-visibility management.

Triggers
"I'm getting undefined reference at link time"
"How do I enable LTO for a real project?"
"Which linker should I use: ld, gold, or lld?"
"How do I reduce binary size with --gc-sections?"
"How do I write or understand a linker script?"
"I have duplicate symbol or weak symbol issues"
Workflow
1. Linker selection
Linker	Invocation	Strengths
GNU ld (BFD)	default on Linux	Universal, stable
gold	-fuse-ld=gold	Faster than ld for C++; supports LTO plugins
lld (LLVM)	-fuse-ld=lld	Fastest, parallel, required for Clang LTO
# Use lld with GCC or Clang
gcc -fuse-ld=lld -o prog ...
clang -fuse-ld=lld -o prog ...

# Check which linker is used
gcc -v -o prog main.c 2>&1 | grep 'Invoking'

2. Essential linker flags
# Pass linker flags via compiler driver:
# -Wl,flag1,flag2   (comma-separated, no spaces)
# -Wl,flag1 -Wl,flag2  (separate -Wl options)

gcc main.c -o prog \
  -Wl,-rpath,/opt/mylibs/lib \     # runtime library search path
  -Wl,--as-needed \                 # only link libraries that are actually used
  -Wl,--gc-sections \               # remove unused sections (requires -ffunction-sections -fdata-sections)
  -Wl,-z,relro \                    # mark relocations read-only after startup
  -Wl,-z,now \                      # resolve all symbols at startup (full RELRO)
  -L/opt/mylibs/lib -lfoo

3. Link order matters (GNU ld)

GNU ld processes archives left-to-right. A library must come after the objects that need it.

# Wrong: libfoo provides symbols needed by main.o
gcc main.o -lfoo libdep.a -o prog   # can fail if libdep.a needs libfoo

# Correct: dependencies after dependents
gcc main.o -lfoo -ldep -o prog

# If there are circular deps between archives:
gcc main.o -Wl,--start-group -lfoo -lbar -Wl,--end-group -o prog
# --start-group/--end-group: repeat search until no new symbols resolved

4. LTO with GCC
# Compile
gcc -O2 -flto -ffunction-sections -fdata-sections -c foo.c -o foo.o
gcc -O2 -flto -ffunction-sections -fdata-sections -c bar.c -o bar.o

# Link (must pass -flto again)
gcc -O2 -flto -Wl,--gc-sections foo.o bar.o -o prog

# Archives: must use gcc-ar / gcc-ranlib, not plain ar
gcc-ar rcs libfoo.a foo.o
gcc-ranlib libfoo.a


Parallel LTO:

gcc -O2 -flto=auto foo.o bar.o -o prog   # uses jobserver
gcc -O2 -flto=4   foo.o bar.o -o prog    # 4 parallel jobs

5. LTO with Clang / lld
# Full LTO
clang -O2 -flto -fuse-ld=lld foo.c bar.c -o prog

# ThinLTO (faster, nearly same quality)
clang -O2 -flto=thin -fuse-ld=lld foo.c bar.c -o prog

# LTO with cmake: set globally
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION ON)   # enables -flto


ThinLTO caches work: subsequent builds that reuse unchanged modules are faster. Cache location: specify with -Wl,--thinlto-cache-dir=/tmp/thinlto-cache.

6. Dead-code stripping
# Compile with per-function/per-data sections
gcc -O2 -ffunction-sections -fdata-sections -c foo.c -o foo.o

# Link with garbage collection
gcc -Wl,--gc-sections foo.o -o prog

# Verify what was removed
gcc -Wl,--gc-sections -Wl,--print-gc-sections foo.o -o prog 2>&1 | head -20


On macOS, the linker strips dead code by default (-dead_strip).

7. Symbol visibility

Controlling visibility reduces DSO size and enables better LTO:

# Hide all symbols by default, export explicitly
gcc -fvisibility=hidden -O2 -shared -fPIC foo.c -o libfoo.so

# In source, mark exports:
__attribute__((visibility("default"))) int my_public_function(void);


Or use a version script:

# foo.ver
{
  global: my_public_function; my_other_public;
  local: *;
};

gcc -Wl,--version-script=foo.ver -shared -fPIC -o libfoo.so foo.o

8. Common linker errors
Error	Cause	Fix
undefined reference to 'foo'	Missing library or wrong order	Add -lfoo; move after the object that needs it
multiple definition of 'foo'	Symbol defined in two TUs	Remove duplicate; use static or extern
cannot find -lfoo	Library not in search path	Add -L/path/to/lib; install dev package
relocation truncated	Address overflow in relocation	Use -mcmodel=large; restructure image
version 'GLIBC_2.33' not found	Binary needs newer glibc	Link statically or rebuild on older host
circular reference	Archives mutually depend	Use --start-group/--end-group
9. Linker map file
# Generate a map file (shows symbol → section → file)
gcc -Wl,-Map=prog.map -o prog foo.o bar.o
less prog.map


Useful for debugging binary size and symbol placement.

For a comprehensive linker and LTO flags reference, see references/flags.md.

Related skills
Use skills/binaries/elf-inspection for examining the resulting binary
Use skills/compilers/gcc or skills/compilers/clang for compile-phase LTO flags
Use skills/binaries/binutils for ar, strip, objcopy
Weekly Installs
96
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