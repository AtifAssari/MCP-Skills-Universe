---
title: dump-collect
url: https://skills.sh/dotnet/skills/dump-collect
---

# dump-collect

skills/dotnet/skills/dump-collect
dump-collect
Installation
$ npx skills add https://github.com/dotnet/skills --skill dump-collect
SKILL.md
.NET Crash Dump Collection

This skill configures and collects crash dumps for modern .NET applications (CoreCLR and NativeAOT) on Linux, macOS, and Windows — including containers.

Stop Signals

🚨 Read before starting any workflow.

Stop after dumps are enabled or collected. Do not open, analyze, or triage dump files.
If the user already has a dump file, this skill does not cover analysis. Let them know analysis is out of scope.
Do not install analysis tools (dotnet-dump analyze, windbg). Only install collection tools (dotnet-dump collect). Using lldb for on-demand dump capture on macOS is allowed — it ships with Xcode command-line tools and is not being used for analysis.
Do not trace root cause of crashes. Report the dump file location and move on.
Do not modify application code. Configuration is environment-only (env vars, OS settings, container specs).
Step 1 — Identify the Scenario

Ask or determine:

Goal: Enable automatic crash dumps, or capture a dump from a running process right now?
Platform: Linux, macOS, or Windows? Running in a container (Docker/Kubernetes)?
Runtime: CoreCLR or NativeAOT?
Detecting CoreCLR vs NativeAOT

From a binary file (Linux/macOS):

# CoreCLR — has IL metadata / managed entry point
strings <binary> | grep -q "CorExeMain" && echo "CoreCLR"

# NativeAOT — has Redhawk runtime symbols
strings <binary> | grep -q "Rhp" && echo "NativeAOT"

# On macOS/Linux, also try:
nm <binary> 2>/dev/null | grep -qi "Rhp" && echo "NativeAOT"


From a binary file (Windows):

# CoreCLR — has a CLI header (IL entry point)
dumpbin /clrheader <binary.exe> | Select-String "CLI Header" -Quiet

# NativeAOT — no CLI header, has Redhawk symbols
dumpbin /symbols <binary.exe> | Select-String "Rhp" -Quiet


From a running process (Linux):

# Resolve the binary, then use the same file checks
BINARY=$(readlink /proc/<pid>/exe)
strings "$BINARY" | grep -q "CorExeMain" && echo "CoreCLR" || echo "NativeAOT"


From a running process (macOS):

# Resolve the binary path from the running process
BINARY=$(ps -o comm= -p <pid>)
strings "$BINARY" | grep -q "CorExeMain" && echo "CoreCLR" || echo "NativeAOT"


From a running process (Windows PowerShell):

# CoreCLR — loads coreclr.dll
(Get-Process -Id <pid>).Modules.ModuleName -contains "coreclr.dll"

# .NET Framework — loads clr.dll (this skill does not apply)
(Get-Process -Id <pid>).Modules.ModuleName -contains "clr.dll"


If the app is .NET Framework (clr.dll), stop. This skill covers modern .NET (CoreCLR and NativeAOT) only.

If neither CoreCLR nor NativeAOT is detected, stop. This skill only applies to .NET applications — do not proceed.

Step 2 — Load the Appropriate Reference

Based on the scenario identified in Step 1, read the relevant reference file:

Scenario	Reference
CoreCLR app (any platform)	references/coreclr-dumps.md
NativeAOT app (any platform)	references/nativeaot-dumps.md
Any app in Docker or Kubernetes	references/container-dumps.md (then also load the runtime-specific reference)
Step 3 — Execute

Follow the instructions in the loaded reference to configure or collect dumps. Always:

Confirm the dump output directory exists and has write permissions before enabling collection.
Report the dump file path back to the user after collection succeeds.
Verify configuration took effect — for env vars, echo them; for OS settings, read them back.
Remind the user to disable automatic dumps if they were enabled temporarily — remove or unset DOTNET_DbgEnableMiniDump and related env vars to avoid accumulating dump files.
Weekly Installs
220
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