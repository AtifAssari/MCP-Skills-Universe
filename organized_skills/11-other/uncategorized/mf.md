---
rating: ⭐⭐
title: mf
url: https://skills.sh/module-federation/core/mf
---

# mf

skills/module-federation/core/mf
mf
Installation
$ npx skills add https://github.com/module-federation/core --skill mf
SKILL.md
MF — Module Federation All-in-One Skill
Step 1: Identify the sub-skill

Parse $ARGUMENTS and map to a reference file in the reference/ directory (same directory as this file):

Sub-command (case-insensitive)	Aliases	Reference file
docs	doc, help, ?	reference/docs.md
context	ctx, info, status	reference/context.md
module-info	module, remote, manifest	reference/module-info.md
integrate	init, setup, add	reference/integrate.md
type-check	types, ts, dts	reference/type-check.md
shared-deps	shared, deps, singleton	reference/shared-deps.md
perf	performance, hmr, speed	reference/perf.md
config-check	config, plugin, exposes	reference/config-check.md
bridge-check	bridge, sub-app	reference/bridge-check.md
runtime-error	runtime-code, runtime-008, runtime-001, remote-entry	reference/runtime-error.md

If no explicit sub-command is found, detect intent from the full input:

Signal in input	Reference file
Question about MF concepts, API, configuration options	reference/docs.md
"integrate", "add MF", "setup", "scaffold", "new project"	reference/integrate.md
"type error", "TS error", "@mf-types", "dts", "typescript"	reference/type-check.md
"shared", "singleton", "duplicate", "antd", "transformImport"	reference/shared-deps.md
"slow", "HMR", "performance", "build speed", "ts-go"	reference/perf.md
"plugin", "asyncStartup", "exposes key", "config"	reference/config-check.md
"bridge", "sub-app", "export-app", "createRemoteAppComponent"	reference/bridge-check.md
"RUNTIME-001", "RUNTIME-008", "runtime error code", "remote entry load failed", "ScriptNetworkError", "ScriptExecutionError", "container missing", "window[remoteEntryKey]"	reference/runtime-error.md
"manifest", "remoteEntry URL", "module info", "publicPath"	reference/module-info.md
"context", "what is configured", "MF role", "bundler"	reference/context.md

If still ambiguous, show the user the sub-command table above and ask them to pick.

Step 2: Load and execute the reference

Read the matched file from the reference/ directory (same directory as this SKILL.md).

Execute all instructions in that file, passing the remaining arguments (everything after the sub-command token, or the full $ARGUMENTS if intent-detected) as ARGS.

Weekly Installs
357
Repository
module-federation/core
GitHub Stars
2.5K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn