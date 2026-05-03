---
rating: ⭐⭐⭐
title: binlog-failure-analysis
url: https://skills.sh/dotnet/skills/binlog-failure-analysis
---

# binlog-failure-analysis

skills/dotnet/skills/binlog-failure-analysis
binlog-failure-analysis
Installation
$ npx skills add https://github.com/dotnet/skills --skill binlog-failure-analysis
SKILL.md
Analyzing MSBuild Failures with Binary Logs

Use MSBuild's built-in binlog replay to convert binary logs into searchable text logs, then analyze with standard tools (grep, cat, head, tail, find).

Build Error Investigation (Primary Workflow)
Step 1: Replay the binlog to text logs

Replay produces multiple focused log files in one pass:

dotnet msbuild build.binlog -noconlog \
  -fl  -flp:v=diag;logfile=full.log;performancesummary \
  -fl1 -flp1:errorsonly;logfile=errors.log \
  -fl2 -flp2:warningsonly;logfile=warnings.log


PowerShell note: Use -flp:"v=diag;logfile=full.log;performancesummary" (quoted semicolons).

Step 2: Read the errors
cat errors.log


This gives all errors with file paths, line numbers, error codes, and project context.

Step 3: Search for context around specific errors
# Find all occurrences of a specific error code with surrounding context
grep -n -B2 -A2 "CS0246" full.log

# Find which projects failed to compile
grep -i "CoreCompile.*FAILED\|Build FAILED\|error MSB" full.log

# Find project build order and results
grep "done building project\|Building with" full.log | head -50

Step 4: Detect cascading failures

Projects that never reached CoreCompile failed because a dependency failed, not their own code:

# List all projects that ran CoreCompile
grep 'Target "CoreCompile"' full.log | grep -oP 'project "[^"]*"'

# Compare against projects that had errors to identify cascading failures
grep "project.*FAILED" full.log

Step 5: Examine project files for root causes
# Read the .csproj of the failing project
cat path/to/Services/Services.csproj

# Check PackageReference and ProjectReference entries
grep -n "PackageReference\|ProjectReference" path/to/Services/Services.csproj


Write your diagnosis as soon as you have enough information. Do not over-investigate.

Additional Workflows
Performance Investigation
# The PerformanceSummary is at the end of full.log
tail -100 full.log   # shows target/task timing summary
grep "Target Performance Summary\|Task Performance Summary" -A 50 full.log

Dependency/Evaluation Issues
# Check evaluation properties
grep -i "OutputPath\|IntermediateOutputPath\|TargetFramework" full.log | head -30
# Check item groups
grep "PackageReference\|ProjectReference" full.log | head -30

Replay reference
Command	Purpose
dotnet msbuild X.binlog -noconlog -fl -flp:v=diag;logfile=full.log;performancesummary	Full diagnostic log with perf summary
dotnet msbuild X.binlog -noconlog -fl -flp:errorsonly;logfile=errors.log	Errors only
dotnet msbuild X.binlog -noconlog -fl -flp:warningsonly;logfile=warnings.log	Warnings only
grep -n "PATTERN" full.log	Search for patterns in the replayed log
dotnet msbuild -pp:preprocessed.xml Proj.csproj	Preprocess — inline all imports into one file
Generating a binlog (only if none exists)
dotnet build /bl:build.binlog

Common error patterns
CS0246 / "type not found" → Missing PackageReference — check the .csproj
MSB4019 / "imported project not found" → SDK install or global.json issue
NU1605 / "package downgrade" → Version conflict in package graph
MSB3277 / "version conflicts" → Binding redirect or version alignment issue
Project failed at ResolveProjectReferences → Cascading failure from a dependency
Weekly Installs
216
Repository
dotnet/skills
GitHub Stars
1.5K
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass