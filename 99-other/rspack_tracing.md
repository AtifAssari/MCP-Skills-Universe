---
title: rspack-tracing
url: https://skills.sh/rstackjs/agent-skills/rspack-tracing
---

# rspack-tracing

skills/rstackjs/agent-skills/rspack-tracing
rspack-tracing
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill rspack-tracing
SKILL.md
Rspack Tracing & Performance Profiling
When to Use This Skill

Use this skill when you need to:

Diagnose why an Rspack build is slow.
Understand which plugins or loaders are taking the most time.
Analyze a user-provided Rspack trace file.
Guide a user to capture a performance profile.
Workflow
1. Capture a Trace

First, ask the user to run their build with tracing enabled.

# Set environment variables for logging to a file
RSPACK_PROFILE=TRACE RSPACK_TRACE_LAYER=logger RSPACK_TRACE_OUTPUT=./trace.json pnpm build


This will generate a trace file in a timestamped directory like .rspack-profile-{timestamp}-{pid}/trace.json.

See references/tracing-guide.md for more details on configuration.

2. Quick Diagnosis for Crashes/Errors

If the user wants to identify which stage a crash or error occurred in, use tail to quickly view the last events without running the full analysis:

# Navigate to the generated profile directory
cd .rspack-profile-*/

# View the last 20 events to see where the build failed
tail -n 20 trace.json


The last events will show the span names and targets where the build stopped, helping to quickly pinpoint the problematic stage, plugin, or loader.

3. Full Performance Analysis

For detailed performance profiling (not just crash diagnosis), ask the user to run the bundled analysis script on the generated trace file.

# Navigate to the generated profile directory
cd .rspack-profile-*/

# Run the analysis script
node ${CLAUDE_PLUGIN_ROOT}/skills/tracing/scripts/analyze_trace.js trace.json

4. Interpret Results

Use the output from the script to identify bottlenecks. Consult references/bottlenecks.md to map span names to actionable fixes.

5. Locate Slow Plugins

Based on the "Top Slowest Hooks" from the analysis script:

Identify the Hook: Note the hook name (e.g., hook:CompilationOptimizeChunks).
Inspect Configuration: Read rspack.config.js or rsbuild.config.ts.
Map Hook to Plugin: Look for plugins and their sources that tap into that specific hook.
Output: Output the paths, lines and columns of the suspected plugin source code.
Common Scenarios & Quick Fixes
Bottleneck Reference: Mapping spans to concepts.
Tracing Guide: Detailed usage of RSPACK_PROFILE.
Weekly Installs
93
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass