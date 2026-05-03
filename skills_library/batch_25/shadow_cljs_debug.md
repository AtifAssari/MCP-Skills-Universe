---
title: shadow-cljs-debug
url: https://skills.sh/riatzukiza/devel/shadow-cljs-debug
---

# shadow-cljs-debug

skills/riatzukiza/devel/shadow-cljs-debug
shadow-cljs-debug
Installation
$ npx skills add https://github.com/riatzukiza/devel --skill shadow-cljs-debug
SKILL.md
Skill: Shadow-CLJS Debug
Goal

To systematically identify and fix compilation errors, dependency issues, and configuration problems in shadow-cljs projects.

Use This Skill When
shadow-cljs compile fails.
The build hangs or loops indefinitely.
You see "Undeclared Var", "No such namespace", or "Analysis Error".
You suspect a dependency is missing.
Do Not Use This Skill When
The error is clearly a syntax error (use clojure-syntax-rescue).
Steps
Analyze Error:
Read the error message fully. Is it a compilation error or a dependency error?
Undeclared Var: You forgot to (:require [namespace :as alias]) or are using a function that doesn't exist.
No such namespace: The file path does not match the namespace declaration, or the package is not installed.
Check Config:
Read shadow-cljs.edn. Is the build ID correct? Are source paths included?
Read deps.edn (if used). Is the dependency listed?
Read package.json. Is the npm package installed?
Clean State:
If behavior is weird or inconsistent, delete the cache: rm -rf .shadow-cljs .cpcache.
Restart the watch process.
Verify Interop:
npm: Ensure you use (:require ["package-name" :as pkg]) for npm packages.
Globals: Use js/window or js/console for globals, do not require them.
Fix & Retry:
Apply the fix.
Run npx shadow-cljs compile <build-id> (or release for production).
Output
A successful compilation (exit code 0).
Strong Hints
Constraint: Never edit the output files (for example public/js/main.js). Only edit .cljs source.
Tip: Shadow-CLJS relies heavily on package.json for JS deps. If an npm import fails, check node_modules first (workspace-dependency-check).
Tip: (:require [foo.bar :as bar]) requires a file at src/foo/bar.cljs. Check file paths match namespaces exactly.
Suggested Next Skills

Check the Skill Graph for the full workflow.

clojure-syntax-rescue
workspace-dependency-check
Weekly Installs
9
Repository
riatzukiza/devel
GitHub Stars
2
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass