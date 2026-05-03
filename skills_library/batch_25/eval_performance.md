---
title: eval-performance
url: https://skills.sh/dotnet/skills/eval-performance
---

# eval-performance

skills/dotnet/skills/eval-performance
eval-performance
Installation
$ npx skills add https://github.com/dotnet/skills --skill eval-performance
SKILL.md
MSBuild Evaluation Phases

For a comprehensive overview of MSBuild's evaluation and execution model, see Build process overview.

Initial properties: environment variables, global properties, reserved properties
Imports and property evaluation: process <Import>, evaluate <PropertyGroup> top-to-bottom
Item definition evaluation: <ItemDefinitionGroup> metadata defaults
Item evaluation: <ItemGroup> with Include, Remove, Update, glob expansion
UsingTask evaluation: register custom tasks

Key insight: evaluation happens BEFORE any targets run. Slow evaluation = slow build start even when nothing needs compiling.

Diagnosing Evaluation Performance
Using binlog
Replay the binlog: dotnet msbuild build.binlog -noconlog -fl -flp:v=diag;logfile=full.log
Search for evaluation events: grep -i 'Evaluation started\|Evaluation finished' full.log
Multiple evaluations for the same project = overbuilding
Look for "Project evaluation started/finished" messages and their timestamps
Using /pp (preprocess)
dotnet msbuild -pp:full.xml MyProject.csproj
Shows the fully expanded project with ALL imports inlined
Use to understand: what's imported, import depth, total content volume
Large preprocessed output (>10K lines) = heavy evaluation
Using /clp:PerformanceSummary
Add to build command for timing breakdown
Shows evaluation time separately from target/task execution
Expensive Glob Patterns
Globs like **/*.cs walk the entire directory tree
Default SDK globs are optimized, but custom globs may not be
Problem: globbing over node_modules/, .git/, bin/, obj/ — millions of files
Fix: use <DefaultItemExcludes> to exclude large directories
Fix: be specific with glob paths: src/**/*.cs instead of **/*.cs
Fix: use <EnableDefaultItems>false</EnableDefaultItems> only as last resort (lose SDK defaults)
Check: grep for Compile items in the diagnostic log → if Compile items include unexpected files, globs are too broad
Import Chain Analysis
Deep import chains (>20 levels) slow evaluation
Each import: file I/O + parse + evaluate
Common causes: NuGet packages adding .props/.targets, framework SDK imports, Directory.Build chains
Diagnosis: /pp output → search for <!-- Importing comments to see import tree
Fix: reduce transitive package imports where possible, consolidate imports
Multiple Evaluations
A project evaluated multiple times = wasted work
Common causes: referenced from multiple other projects with different global properties
Each unique set of global properties = separate evaluation
Diagnosis: grep 'Evaluation started.*ProjectName' full.log → if count > 1, check for differing global properties
Fix: normalize global properties, use graph build (/graph)
TreatAsLocalProperty
Prevents property values from flowing to child projects via MSBuild task
Overuse: declaring many TreatAsLocalProperty entries adds evaluation overhead
Correct use: only when you genuinely need to override an inherited property
Property Function Cost
Property functions execute during evaluation
Most are cheap (string operations)
Expensive: $([System.IO.File]::ReadAllText(...)) during evaluation — reads file on every evaluation
Expensive: network calls, heavy computation
Rule: property functions should be fast and side-effect-free
Optimization Checklist
 Check preprocessed output size: dotnet msbuild -pp:full.xml
 Verify evaluation count: should be 1 per project per TFM
 Exclude large directories from globs
 Avoid file I/O in property functions during evaluation
 Minimize import depth
 Use graph build to reduce redundant evaluations
 Check for unnecessary UsingTask declarations
Weekly Installs
230
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