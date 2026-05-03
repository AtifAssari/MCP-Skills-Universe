---
title: function call tracing
url: https://skills.sh/gadievron/raptor/function-call-tracing
---

# function call tracing

skills/gadievron/raptor/Function Call Tracing
Function Call Tracing
Installation
$ npx skills add https://github.com/gadievron/raptor --skill 'Function Call Tracing'
SKILL.md
Function Call Tracing
Purpose

Trace all function calls in C/C++ programs with per-thread logs and Perfetto visualization.

Components
1. Instrumentation Library (trace_instrument.c)

Captures function entry/exit, writes per-thread logs.

Build:

gcc -c -fPIC trace_instrument.c -o trace_instrument.o
gcc -shared trace_instrument.o -o libtrace.so -ldl -lpthread

2. Perfetto Converter (trace_to_perfetto.cpp)

Converts logs to Chrome JSON for Perfetto UI.

Build:

g++ -O3 -std=c++17 trace_to_perfetto.cpp -o trace_to_perfetto

Usage
Step 1: Add to Build
CFLAGS += -finstrument-functions -g
LDFLAGS += -L. -ltrace -ldl -lpthread

Step 2: Build Target
make

Step 3: Run
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
./program
# Creates trace_<tid>.log files

Step 4: Convert to Perfetto
./trace_to_perfetto trace_*.log -o trace.json
# Open trace.json in ui.perfetto.dev

Log Format
[seq] [timestamp] [dots] [ENTRY|EXIT!] function_name
[0] [1.000000000]  [ENTRY] main
[1] [1.000050000] . [ENTRY] helper
[2] [1.000100000] . [EXIT!] helper
[3] [1.000150000]  [EXIT!] main

Dots indicate call depth
Timestamp in seconds.nanoseconds
One log file per thread
When User Requests Tracing
Steps
Copy trace_instrument.c and trace_to_perfetto.cpp to project
Build instrumentation library
Add -finstrument-functions to CFLAGS
Add -L. -ltrace -ldl -lpthread to LDFLAGS
Build project
Set LD_LIBRARY_PATH and run
Convert logs: ./trace_to_perfetto trace_*.log -o trace.json
Provide link to ui.perfetto.dev
Build System Detection

Makefile: Add flags conditionally

ENABLE_TRACE ?= 0
ifeq ($(ENABLE_TRACE),1)
    CFLAGS += -finstrument-functions -g
    LDFLAGS += -L. -ltrace -ldl -lpthread
endif


CMake: Add option

option(ENABLE_TRACE "Enable tracing" OFF)
if(ENABLE_TRACE)
    add_compile_options(-finstrument-functions -g)
    link_libraries(trace dl pthread)
endif()

Output
trace_.log: Per-thread text logs
trace.json: Perfetto Chrome JSON format
View at https://ui.perfetto.dev
Perfetto JSON Format

Function ENTRY → "B" (begin) event Function EXIT! → "E" (end) event All threads aligned by timestamp in single file.

Weekly Installs
–
Repository
gadievron/raptor
GitHub Stars
2.0K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass